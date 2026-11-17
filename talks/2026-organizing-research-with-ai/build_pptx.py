#!/usr/bin/env python3
"""Build an editable PowerPoint of this talk: native text boxes and shapes, not a raster.

Run from the talk folder:  ~/.venvs/mech479/bin/python build_pptx.py
Helpers are copied from talks/2026-mech479-reading-with-ai/build_pptx.py.
Needs python-pptx and rsvg-convert (SVG figures are converted to PNG in .pptx-build/).
Speaker notes are read from index.html, one <aside class="notes"> per slide, in order.
Most slides are a title, one figure from assets/ and one line; that text is repeated here by hand,
so an edit to index.html must be made here too.
"""
import html
import re
import subprocess
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Pt

HERE = Path(__file__).resolve().parent
# A rebuild overwrites OUT. Once the .pptx has been edited by hand, rename it before running this.
OUT = HERE / "2026-organizing-research-with-ai.pptx"
BUILD = HERE / ".pptx-build"

# Canvas: the deck's 960 x 700 px at 96 px/in.
W, H = 960, 700
PX = 9525  # EMU per px

BG, PANEL, INK, MUTED = "212121", "2A2C31", "E8EAEE", "9AA1AD"
GOLD, BLUE, RED, RULE, BUBBLE = "FABD0F", "8FB0DC", "E0566D", "3A3D44", "34373E"
SANS, MONO = "Arial", "Courier New"

SECTIONS = ["How an LLM works", "Why on your computer", "One home folder",
            "Skills, subagents, MCP", "Demo"]


def rgb(h):
    return RGBColor.from_string(h)


def px(v):
    return Emu(int(v * PX))


def notes_from_html():
    src = (HERE / "index.html").read_text()
    out = []
    for m in re.finditer(r'<aside class="notes">(.*?)</aside>', src, re.S):
        text = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
        out.append(" ".join(text.split()))
    return out


def png(name, width=1600):
    """Return a PNG path for an asset, converting SVG once."""
    src = HERE / "assets" / name
    if src.suffix != ".svg":
        return src
    BUILD.mkdir(exist_ok=True)
    dst = BUILD / (src.stem + ".png")
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        # rsvg does not resolve system-ui, and its fallback has other widths, so name a real font.
        svg = re.sub(r"system-ui, -apple-system, 'Segoe UI', sans-serif", "Helvetica Neue", src.read_text())
        # rsvg also drops a space at a <tspan> edge unless whitespace is preserved.
        svg = svg.replace("<text ", '<text xml:space="preserve" ')
        svg = re.sub(r"(<text[^>]*>)\s*\n\s*(<tspan)", r"\1\2", svg)
        svg = re.sub(r"(</tspan>)\s*\n\s*(</text>)", r"\1\2", svg)
        subprocess.run(["rsvg-convert", "-w", str(width), "-o", str(dst)], input=svg.encode(), check=True)
    return dst


class Deck:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = px(W), px(H)
        self.blank = self.prs.slide_layouts[6]
        self.notes = notes_from_html()
        self.count = {}

    def slide(self, section=None, title=None, title_size=38, title_color=INK, kicker=None):
        s = self.prs.slides.add_slide(self.blank)
        fill = s.background.fill
        fill.solid()
        fill.fore_color.rgb = rgb(BG)
        n = len(self.prs.slides) - 1
        if n < len(self.notes):
            s.notes_slide.notes_text_frame.text = self.notes[n]
        self.cur = s
        y = 22
        if section:
            self.text(20, y, 900, 24, [(f"{section}", GOLD, True),
                                       (f"  ·  {SECTIONS[section - 1].upper()}", BLUE, True)], size=14)
            y = 52
            self.guidebar(section)
        elif kicker:
            self.text(20, y, 900, 24, kicker.upper(), size=14, color=BLUE, bold=True)
            y = 52
        if title:
            self.text(20, y, 920, 64, title, size=title_size, color=title_color, bold=True)
        return s

    def text(self, x, y, w, h, runs, size=22, color=INK, bold=False, font=SANS,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, spacing=1.15, italic=False):
        """runs: a string, or a list of paragraphs; a paragraph is a string or a list of
        (text, color, bold) tuples. Colour and bold default to the box's."""
        tb = self.cur.shapes.add_textbox(px(x), px(y), px(w), px(h))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = anchor
        for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
            setattr(tf, m, 0)
        paras = [runs] if isinstance(runs, str) else runs
        if paras and isinstance(paras[0], tuple):
            paras = [paras]
        for i, para in enumerate(paras):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            p.line_spacing = spacing
            if i:
                p.space_before = Pt(size * 0.35)
            for part in ([(para,)] if isinstance(para, str) else para):
                t = part[0]
                c = part[1] if len(part) > 1 and part[1] else color
                b = part[2] if len(part) > 2 else bold
                r = p.add_run()
                r.text = t
                r.font.size, r.font.name, r.font.bold, r.font.italic = Pt(size), font, b, italic
                r.font.color.rgb = rgb(c)
        return tb

    def box(self, x, y, w, h, fill=PANEL, shape=MSO_SHAPE.RECTANGLE):
        sh = self.cur.shapes.add_shape(shape, px(x), px(y), px(w), px(h))
        sh.fill.solid()
        sh.fill.fore_color.rgb = rgb(fill)
        sh.line.fill.background()
        sh.shadow.inherit = False
        if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
            sh.adjustments[0] = 0.08
        return sh

    def card(self, x, y, w, h, top=None, left=None, fill=PANEL):
        """A panel with a coloured top or left edge."""
        self.box(x, y, w, h, fill)
        if top:
            self.box(x, y, w, 4, top)
        if left:
            self.box(x, y, 4, h, left)

    def bubble(self, x, y, w, h, runs, mine=False, hot=False, size=16, color=INK, font=SANS):
        """A chat turn. Mine: right-hand grey bubble. Model: panel with a blue or gold edge."""
        if mine:
            self.box(x, y, w, h, BUBBLE, MSO_SHAPE.ROUNDED_RECTANGLE)
        else:
            self.card(x, y, w, h, left=GOLD if hot else BLUE)
        self.text(x + 14, y + 8, w - 26, h - 16, runs, size=size, color=color, font=font,
                  anchor=MSO_ANCHOR.MIDDLE, spacing=1.2)

    def image(self, name, y, max_h, max_w=900):
        from PIL import Image
        p = png(name)
        iw, ih = Image.open(p).size
        scale = min(max_w / iw, max_h / ih)
        w, h = iw * scale, ih * scale
        self.cur.shapes.add_picture(str(p), px((W - w) / 2), px(y), px(w), px(h))
        return y + h

    def take(self, y, runs, size=22, h=64):
        """The takeaway line with a gold edge."""
        self.box(20, y, 4, h, GOLD)
        self.text(38, y, 890, h, runs, size=size, anchor=MSO_ANCHOR.MIDDLE)

    def evidence(self, y, s):
        self.text(20, y, 920, 18, s, size=11, color=MUTED, font=MONO)

    def guidebar(self, current):
        gap, x0 = 10, 12
        seg = (W - 2 * x0 - gap * (len(SECTIONS) - 1)) / len(SECTIONS)
        self.count[current] = self.count.get(current, 0) + 1
        for i, name in enumerate(SECTIONS, start=1):
            x = x0 + (i - 1) * (seg + gap)
            on = i == current
            self.text(x, 676, seg, 14, f"{i} · {name}", size=7, color=INK if on else MUTED, bold=on)
            self.box(x, 692, seg, 3, GOLD if i <= current else RULE)

    def bullets(self, y, lines, size=24, gap=52, x=20, w=900, numbered=False):
        for i, line in enumerate(lines):
            yy = y + i * gap
            if numbered:
                self.text(x, yy, 30, gap - 8, f"{i + 1}.", size=size, color=GOLD, bold=True,
                          anchor=MSO_ANCHOR.MIDDLE)
            else:
                self.box(x + 6, yy + (gap - 8) / 2 - 4, 9, 9, INK, MSO_SHAPE.OVAL)
            self.text(x + 36, yy, w - 36, gap - 8, line, size=size, anchor=MSO_ANCHOR.MIDDLE)
        return y + len(lines) * gap

    def code(self, x, y, w, h, source, size=13, panel=True):
        """Monospace lines in a panel, one paragraph per line, no paragraph spacing."""
        if panel:
            self.box(x, y, w, h, "1B1C1F")
        tb = self.cur.shapes.add_textbox(px(x + 14), px(y + 10), px(w - 28), px(h - 20))
        tf = tb.text_frame
        tf.word_wrap = True
        for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
            setattr(tf, m, 0)
        for i, line in enumerate(source.strip("\n").split("\n")):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.line_spacing = 1.08
            r = p.add_run()
            r.text = line if line else " "
            r.font.size, r.font.name = Pt(size), MONO
            r.font.color.rgb = rgb(INK)

    def table(self, y, rows, widths, size=17, row_h=40, header=True, x=20):
        """Rows of cells; a cell is a string or a list of (text, colour, bold) runs."""
        for i, row in enumerate(rows):
            cx, head = x, header and i == 0
            h = row_h if isinstance(row_h, (int, float)) else row_h[i]
            for cell, w in zip(row, widths):
                self.text(cx, y, w - 14, h, cell, size=size, color=BLUE if head else INK,
                          bold=head, anchor=MSO_ANCHOR.MIDDLE, spacing=1.1)
                cx += w
            y += h
            self.box(x, y, sum(widths), 2 if head else 1, RULE)
        return y

    def gold(self, y, line, size=28, h=50):
        self.text(20, y, 920, h, line, size=size, color=GOLD, bold=True)


def build():
    d = Deck()

    def fig(section, title, name, max_h, take=None, gold=None, y=125, title_size=38, take_h=48):
        """A slide that is a title, one figure and one line."""
        d.slide(section, title, title_size=title_size)
        yb = d.image(name, y, max_h, max_w=920)
        if take:
            d.take(yb + 22, take, h=take_h)
        if gold:
            d.gold(yb + 26, gold, size=28)

    # 0 · Title
    d.slide()
    d.text(60, 150, 840, 170, "Organizing research with AI", size=54, bold=True, spacing=1.05)
    d.text(60, 345, 840, 80, [("One home folder, a wiki file in each folder, and ", MUTED),
                              ("an agent that runs on your computer", GOLD)], size=24)
    d.text(60, 455, 840, 60, [[("Stephen Kerr", INK, True)],
                              [("Queen's University · 17 November 2026", MUTED)]], size=18)

    # 1 · How an LLM works
    fig(1, "What is a token?", "tokens.svg", 330, gold="A token gets its meaning from the tokens around it.", y=140)
    fig(1, "Text in, one token out", "transformer-loop.svg", 400,
        take=[("The model writes ", INK), ("one token at a time", GOLD, True), (", then reads everything again.", INK)])
    fig(1, "Inside the transformer", "transformer-layers.svg", 400,
        take=[("The last position ", INK), ("gathers from every earlier token", GOLD, True),
              (", layer after layer.", INK)])
    fig(1, "Keep context small and relevant", "context-zones.svg", 400,
        gold="Everything in the window is read again on every turn.", y=130)

    # 2 · Why on your computer
    fig(2, "Two places to work", "two-places.svg", 400,
        take=[("Same model. ", INK), ("What changes is what it can reach.", GOLD, True)])
    fig(2, "It reads only what it needs", "files-opened.svg", 340,
        take=[("The agent chooses what to open. ", INK), ("The folder has to show it where things are.", GOLD, True)],
        y=140)

    d.slide(2, "It can run and check")
    d.code(20, 135, 920, 150, """
$ python3 tools/event_classifier/classify.py sample-data/events.csv
family       count   mean eV   min eV
hop             60     0.616    0.432
exchange        40     0.919    0.782
concerted       20     1.312    1.087
""", size=16)
    d.take(315, [("An answer from ", INK), ("output", GOLD, True), (", not from memory.", INK)], h=48)

    fig(2, "The chat ends. The folder stays.", "folder-keeps.svg", 400,
        gold="Anything worth keeping goes in a file.")
    fig(2, "Git carries it across computers", "across-computers.svg", 380,
        take=[("Clone once, and ", INK), ("every computer has the same setup", GOLD, True), (".", INK)],
        title_size=36)

    # 3 · One home folder
    fig(3, "One folder, 13 git repos", "home-layout.svg", 395,
        take=[("Each project keeps its own git history. ", INK), ("The home repo holds the wiki files.", GOLD, True)])

    d.slide(3, "wiki.md: one line per folder")
    d.code(20, 140, 920, 170, """
# wiki: research-home

- [papers/](papers/wiki.md): 7 publication repos, papers by topic
- [code/](code/wiki.md): two KMC codes and the analysis tools
- [tooling/](tooling/wiki.md): the paper search tool
""", size=17)
    d.take(340, [("What the folder is, then a link. ", INK), ("The agent reads this file first.", GOLD, True)], h=48)

    fig(3, "Each wiki.md links to the next", "wiki-chain.svg", 425,
        take=[("The agent follows the links. ", INK), ("Gold: what it opened for one question.", GOLD, True)], y=118)
    fig(3, "Papers by topic", "topics.svg", 400,
        take=[("Topic, then repo, then ", INK), ("one note per paper", GOLD, True), (".", INK)])
    fig(3, "Keep the wiki up to date", "keep-current.svg", 270,
        take=[("Keeping the wiki up to date ", INK), ("improves agent performance", GOLD, True), (".", INK)], y=150)

    # 4 · Skills, subagents, MCP
    fig(4, "Three add-ons", "three-addons.svg", 330,
        take=[("A subagent reads the full paper in its own context window. ", INK),
              ("The main agent gets back only the relevant part.", GOLD, True)], y=145, take_h=70)
    fig(4, "Keep what is always loaded slim", "slim-start.svg", 310,
        take=[("Few tokens spent on finding your way, ", INK),
              ("enough to know where to look and how", GOLD, True), (".", INK)], y=140, take_h=70)

    # 5 · Demo
    fig(5, "Four things to watch", "demo-steps.svg", 250, y=170)
    fig(5, "Start with one folder", "start-steps.svg", 250,
        gold="An agent is only as good as what it can find.", y=160)

    d.slide(5, "Questions?")
    yb = d.image("qr-skills.svg", 140, 340)
    d.text(20, yb + 24, 920, 50, "github.com/Kerrator/skills", size=28, color=GOLD, bold=True,
           align=PP_ALIGN.CENTER)

    # Extra
    d.slide(None, "Three limits", kicker="Extra")
    d.bullets(150, ["What the agent reads goes to the model provider",
                    "It runs commands as you: read each permission prompt",
                    "It can misread a file: ask for the path and open it"], gap=70)

    d.slide(None, "The question, step by step", kicker="Extra")
    d.text(20, 122, 920, 56, "“Which papers held here deal with vacancy diffusion in concentrated Ni-Fe-Cr "
           "alloys, and which script in this folder would give me the distribution of barriers in an "
           "event table?”", size=16, color=MUTED)
    d.code(20, 190, 920, 200, """
 1 Skill   find-paper                          9 search  "vacancy diffusion"
 2 Read    code/wiki.md                       10 Read    pub3/notes/Sauve-Lacoursiere2022.md
 3 Read    papers/wiki.md                     11 Read    pub3/notes/LefevreLopez2024.md
 4 Read    code/analysis-tools/wiki.md        12 Read    pub1/notes/Piochaud2014.md
 5 (load the catalogue tools)                 13 search  "Fe-Ni-Cr"
 6 Read    tools/barrier_histogram/wiki.md    14 search  "Ni-Fe-Cr"
 7 search  "vacancy Ni-Fe-Cr"                 15 search  "NiFeCr"
 8 search  "vacancy concentrated"             16 search  "vacancy Cr"
""", size=12)
    d.evidence(404, "16 steps · 28 s · context 26.5k to 47k tokens")

    d.slide(None, "The answer it gave", kicker="Extra")
    d.card(20, 130, 920, 330, left=RULE)
    d.text(42, 144, 880, 300, [
        [("Sauvé-Lacoursière (2022)", INK, True),
         (", Unexpected role of prefactors in defects diffusion: the case of vacancies in the "
          "55Fe-28Ni-17Cr concentrated solid-solution alloys. Acta Materialia 237, 118153. ", INK),
         ("papers/pub3/notes/Sauve-Lacoursiere2022.md", GOLD)],
        [("Lefèvre López (2024)", INK, True),
         (", Harmonic transition state theory applied to vacancy diffusion pre-exponential factors in "
          "a concentrated solid-solution alloy. Physical Review Materials 8, 013609. ", INK),
         ("papers/pub3/notes/LefevreLopez2024.md", GOLD)],
        [("Piochaud (2014)", INK, True),
         (", adjacent: point defects in fcc Fe-10Ni-20Cr by DFT; energetics, not diffusion. "
          "Physical Review B 89, 024101. ", INK), ("papers/pub1/notes/Piochaud2014.md", GOLD)],
        [("Script: ", INK, True),
         ("code/analysis-tools/tools/barrier_histogram/barrier_histogram.py", GOLD),
         (". “I have not run it or opened the script itself; this comes from its wiki.”", INK)],
    ], size=15, spacing=1.2)

    d.slide(None, "Seven subagents: the numbers", kicker="Extra")
    d.text(20, 122, 920, 44, "“What does each paper repo under papers/ hold on surface diffusion or surface "
           "transport? Use one paper-reader subagent per repo.”", size=16, color=MUTED)
    yb = d.table(176, [
        ["Subagents", "7, one per publication repo"],
        ["Tool calls inside the subagents", "50"],
        ["Tool calls in the main agent", [("8", GOLD, True)]],
        ["Main context after the answer", "50k tokens"],
        ["Time", "72 s"],
    ], [470, 450], size=18, row_h=40, header=False)
    d.take(yb + 30, [("It found papers in pub1, pub3, pub4 and pub5 that the topic list ", INK),
                     ("misses", GOLD, True), (".", INK)], size=20, h=48)

    assert len(d.prs.slides) == len(d.notes), (len(d.prs.slides), len(d.notes))
    d.prs.save(OUT)
    print(f"wrote {OUT.name}: {len(d.prs.slides)} slides, {len(d.notes)} notes")


if __name__ == "__main__":
    build()
