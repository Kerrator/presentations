#!/usr/bin/env python3
"""Draw assets/wiki-chain.svg: the wiki.md chain in ~/research-home and the files one question opened.

Run from the talk folder: python3 assets/make_wiki_chain.py
"""
from pathlib import Path

INK, MUTED, GOLD, BLUE, PANEL, RULE = "#e8eaee", "#9aa1ad", "#FABD0F", "#8fb0dc", "#2a2c31", "#3a3d44"
MONO = "ui-monospace, 'SF Mono', Menlo, monospace"
SANS = "system-ui, -apple-system, 'Segoe UI', sans-serif"

# name: (x, y, width, height, label, followed in the demo question)
BOX = {
    "root": (30, 262, 180, 52, "wiki.md", True),
    "papers": (290, 150, 215, 48, "papers/wiki.md", True),
    "code": (290, 352, 215, 48, "code/wiki.md", True),
    "tooling": (290, 492, 215, 48, "tooling/wiki.md", False),
    "pubs": (585, 96, 300, 44, "pub1 ... pub7 /wiki.md", False),
    "library": (585, 152, 300, 44, "paper-library/wiki.md", False),
    "pykmc": (585, 268, 300, 44, "pykmc/wiki.md", False),
    "pylatkmc": (585, 324, 300, 44, "pylatkmc/wiki.md", False),
    "tools": (585, 380, 300, 44, "analysis-tools/wiki.md", True),
    "mcp": (585, 494, 300, 44, "paper-catalogue-mcp/wiki.md", False),
    "n1": (960, 66, 300, 40, "pub3 Sauve-Lacoursiere2022", True),
    "n2": (960, 114, 300, 40, "pub3 LefevreLopez2024", True),
    "n3": (960, 162, 300, 40, "pub1 Piochaud2014", True),
    "hist": (960, 336, 300, 40, "barrier_histogram/wiki.md", True),
    "classifier": (960, 384, 300, 40, "event_classifier/wiki.md", False),
    "sample": (960, 432, 300, 40, "sample-data/wiki.md", False),
}
EDGES = [
    ("root", "papers", True), ("root", "code", True), ("root", "tooling", False),
    ("papers", "pubs", False), ("papers", "library", False),
    ("code", "pykmc", False), ("code", "pylatkmc", False), ("code", "tools", True),
    ("tooling", "mcp", False),
    ("pubs", "n1", False), ("pubs", "n2", False), ("pubs", "n3", False),
    ("tools", "hist", True), ("tools", "classifier", False), ("tools", "sample", False),
]


def right(name):
    x, y, w, h, *_ = BOX[name]
    return x + w, y + h / 2


def left(name):
    x, y, w, h, *_ = BOX[name]
    return x, y + h / 2


out = [
    '<svg viewBox="0 0 1280 600" xmlns="http://www.w3.org/2000/svg" role="img" '
    'aria-label="The wiki.md chain: the root wiki links to papers, code and tooling; each links one '
    'level down. Gold marks what one question opened.">',
    f'<g font-family="{SANS}">',
]
for a, b, hot in EDGES:
    (x1, y1), (x2, y2) = right(a), left(b)
    mid = (x1 + x2) / 2
    out.append(
        f'<path d="M {x1} {y1} C {mid} {y1}, {mid} {y2}, {x2} {y2}" fill="none" '
        f'stroke="{GOLD if hot else RULE}" stroke-width="{3 if hot else 2}"/>'
    )
# The catalogue search: from papers/wiki.md over the pub wikis to the three notes.
x1, y1 = BOX["papers"][0] + 108, BOX["papers"][1]
out.append(
    f'<path d="M {x1} {y1} C {x1} 30, 800 34, 952 86" fill="none" stroke="{GOLD}" '
    'stroke-width="3" stroke-dasharray="9 7"/>'
)
out.append(f'<text x="420" y="40" font-size="21" fill="{GOLD}">paper search</text>')

for name, (x, y, w, h, label, hot) in BOX.items():
    out.append(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{PANEL}" '
        f'stroke="{GOLD if hot else RULE}" stroke-width="{3 if hot else 2}"/>'
    )
    size = 18 if len(label) >= 25 else 20 if w >= 300 else 23
    out.append(
        f'<text x="{x + w / 2}" y="{y + h / 2 + 7}" font-family="{MONO}" font-size="{size}" '
        f'text-anchor="middle" fill="{INK if hot else MUTED}">{label}</text>'
    )

out += [
    f'<text x="120" y="246" font-size="20" fill="{BLUE}" text-anchor="middle">loaded at the start</text>',
    f'<text x="120" y="340" font-size="18" fill="{MUTED}" text-anchor="middle">~/research-home</text>',
    f'<text x="397" y="590" font-size="20" fill="{BLUE}" text-anchor="middle">one link down</text>',
    f'<text x="735" y="590" font-size="20" fill="{BLUE}" text-anchor="middle">two links down</text>',
    f'<text x="1110" y="590" font-size="20" fill="{BLUE}" text-anchor="middle">notes and tool pages</text>',
    f'<text x="1110" y="52" font-size="18" fill="{MUTED}" text-anchor="middle">paper notes</text>',
    f'<text x="1110" y="322" font-size="18" fill="{MUTED}" text-anchor="middle">analysis-tools</text>',
    "</g>",
    "</svg>",
]
Path(__file__).with_name("wiki-chain.svg").write_text("\n".join(out) + "\n")
