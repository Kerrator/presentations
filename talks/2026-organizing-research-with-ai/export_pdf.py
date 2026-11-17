#!/usr/bin/env python3
"""Export the deck to a landscape PDF through Chrome's DevTools protocol (standard library only).

The plain `chrome --print-to-pdf` route races reveal's print layout and can emit a letter-size
fallback, so this waits until every slide has its .pdf-page wrapper before printing.

    python3 -m http.server 8137 --bind 127.0.0.1      (in this folder, another terminal)
    python3 export_pdf.py [port]
"""
import base64
import json
import os
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8137
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEBUG_PORT = 9347


class Socket:
    """Just enough WebSocket for DevTools: masked text frames out, any length in."""

    def __init__(self, url):
        host, rest = url[len("ws://"):].split("/", 1)
        name, port = host.split(":")
        self.sock = socket.create_connection((name, int(port)))
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall(
            f"GET /{rest} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode()
        )
        while b"\r\n\r\n" not in self.sock.recv(4096):
            pass
        self.next_id = 0

    def read(self, n):
        data = b""
        while len(data) < n:
            data += self.sock.recv(n - len(data))
        return data

    def send(self, text):
        payload, mask = text.encode(), os.urandom(4)
        head = b"\x81" + (
            struct.pack("!BH", 0x80 | 126, len(payload)) if len(payload) > 125 else bytes([0x80 | len(payload)])
        )
        self.sock.sendall(head + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(payload)))

    def receive(self):
        message = b""
        while True:
            first, second = self.read(2)
            length = second & 0x7F
            if length == 126:
                length = struct.unpack("!H", self.read(2))[0]
            elif length == 127:
                length = struct.unpack("!Q", self.read(8))[0]
            message += self.read(length)
            if first & 0x80:
                return message.decode()

    def call(self, method, **params):
        self.next_id += 1
        self.send(json.dumps({"id": self.next_id, "method": method, "params": params}))
        while True:
            reply = json.loads(self.receive())
            if reply.get("id") == self.next_id:
                return reply.get("result", reply)

    def evaluate(self, expression):
        return self.call("Runtime.evaluate", expression=expression, returnByValue=True)["result"].get("value")


def main():
    profile = tempfile.mkdtemp(prefix="deck-pdf-")
    chrome = subprocess.Popen(
        [CHROME, "--headless=new", "--disable-gpu", f"--remote-debugging-port={DEBUG_PORT}",
         f"--user-data-dir={profile}", "--window-size=1280,960", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        for _ in range(50):
            try:
                pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{DEBUG_PORT}/json"))
                break
            except OSError:
                time.sleep(0.2)
        page = Socket(next(p for p in pages if p["type"] == "page")["webSocketDebuggerUrl"])
        page.call("Page.enable")
        page.call("Page.navigate", url=f"http://127.0.0.1:{PORT}/?print-pdf")
        slides = 0
        for _ in range(100):
            time.sleep(0.3)
            slides = page.evaluate("document.querySelectorAll('.reveal .slides section').length") or 0
            ready = page.evaluate(
                "document.querySelectorAll('.pdf-page').length + ':' + "
                "[...document.images].every(i => i.complete) + ':' + document.fonts.status"
            )
            if slides and ready == f"{slides}:true:loaded":
                break
        else:
            sys.exit(f"print layout never settled: {ready}")
        time.sleep(2.0)  # the guidepost bar is injected after pdf-ready
        bars = page.evaluate("document.querySelectorAll('.guidebar-print').length")
        pdf = page.call("Page.printToPDF", printBackground=True, preferCSSPageSize=True,
                        marginTop=0, marginBottom=0, marginLeft=0, marginRight=0)
        out = HERE / f"{HERE.name}.pdf"
        out.write_bytes(base64.b64decode(pdf["data"]))
        print(f"{out.name}: {slides} slides, {bars} with the section bar")
    finally:
        chrome.terminate()


if __name__ == "__main__":
    main()
