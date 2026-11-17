#!/usr/bin/env python3
"""Draw the deck's diagrams as SVG files beside this script.

Run from the talk folder: python3 assets/make_figures.py
(wiki-chain.svg has its own script, make_wiki_chain.py.)
"""
from pathlib import Path

INK, MUTED, GOLD, BLUE, PANEL, RULE = "#e8eaee", "#9aa1ad", "#FABD0F", "#8fb0dc", "#2a2c31", "#3a3d44"
DIM = "#4a4e57"
MONO = "ui-monospace, 'SF Mono', Menlo, monospace"
SANS = "system-ui, -apple-system, 'Segoe UI', sans-serif"
HERE = Path(__file__).resolve().parent

DEFS = "<defs>" + "".join(
    f'<marker id="a-{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
    f'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{c}"/></marker>'
    for n, c in (("gold", GOLD), ("muted", MUTED), ("blue", BLUE))
) + "</defs>"
COLOR_NAME = {GOLD: "gold", MUTED: "muted", BLUE: "blue"}


def box(x, y, w, h, stroke=RULE, fill=PANEL, sw=2, rx=10, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def text(x, y, s, size=24, fill=INK, anchor="middle", mono=False, bold=False):
    fam = f' font-family="{MONO}"' if mono else ""
    wt = ' font-weight="700"' if bold else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{fam}{wt}>{s}</text>'


def arrow(x1, y1, x2, y2, color=MUTED, sw=3, dash=None, both=False):
    n = COLOR_NAME[color]
    d = f' stroke-dasharray="{dash}"' if dash else ""
    start = f' marker-start="url(#a-{n})"' if both else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d} '
            f'marker-end="url(#a-{n})"{start}/>')


def save(name, w, h, parts, label, up=0):
    out = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">',
           DEFS, f'<g font-family="{SANS}" transform="translate(0,{-up})">', *parts, "</g>", "</svg>"]
    (HERE / name).write_text("\n".join(out) + "\n")
    print("wrote", name)


# ---- 1. tokens ------------------------------------------------------------
def tokens():
    p = [text(640, 50, "Gold nanoparticles melt at a lower temperature", 34, MUTED)]
    p.append(arrow(640, 72, 640, 118, MUTED))
    chips = ["Gold", " nano", "particles", " melt", " at", " a", " lower", " temperature"]
    widths = [len(c.strip()) * 19 + 34 for c in chips]
    gap = 14
    x = (1280 - sum(widths) - gap * (len(chips) - 1)) / 2
    centres = []
    for c, w in zip(chips, widths):
        last = c == chips[-1]
        p.append(box(x, 135, w, 62, GOLD if last else BLUE, sw=3 if last else 2))
        p.append(text(x + w / 2, 176, c.strip(), 28, INK, mono=True))
        centres.append(x + w / 2)
        x += w + gap
    # every earlier token links into the last one
    for cx in centres[:-1]:
        mid = (cx + centres[-1]) / 2
        depth = 215 + (centres[-1] - cx) * 0.2
        p.append(f'<path d="M {cx} 200 Q {mid} {depth} {centres[-1]} 200" fill="none" stroke="{GOLD}" '
                 'stroke-width="2.5" opacity="0.8"/>')
    p.append(text(640, 345, "8 tokens. Each one is read together with all the others.", 28, INK))
    save("tokens.svg", 1280, 370, p, "A sentence cut into eight tokens, with links from every earlier token "
         "into the last one.")


# ---- 2. two places to work -----------------------------------------------
def two_places():
    p = [box(470, 20, 340, 76, BLUE), text(640, 68, "the model, in the cloud", 26)]
    # left: chat
    p += [f'<path d="M 520 96 L 290 180" stroke="{MUTED}" stroke-width="3" fill="none"/>',
          box(110, 180, 360, 76, MUTED), text(290, 228, "chat in a browser", 28),
          arrow(290, 400, 290, 262, MUTED, dash="9 7"),
          text(312, 340, "you copy and paste", 24, MUTED, "start"),
          box(110, 404, 360, 130, RULE), text(290, 452, "your files", 26, MUTED),
          text(290, 494, "the chat cannot open them", 21, MUTED)]
    # right: agent
    p += [f'<path d="M 760 96 L 990 180" stroke="{GOLD}" stroke-width="3" fill="none"/>',
          box(810, 180, 360, 76, GOLD, sw=3), text(990, 228, "agent on your computer", 28, GOLD, bold=True),
          arrow(900, 262, 900, 398, GOLD, both=True),
          text(924, 306, "opens files", 24, INK, "start"),
          text(924, 338, "runs commands", 24, INK, "start"),
          text(924, 370, "saves changes", 24, INK, "start"),
          box(730, 404, 520, 130, GOLD, sw=3), text(990, 446, "your folder", 26, INK)]
    for i, lab in enumerate(["papers", "code", "data", "notes"]):
        p += [box(752 + i * 122, 468, 110, 46, RULE, fill="#1f2125", rx=6),
              text(807 + i * 122, 499, lab, 21, MUTED, mono=True)]
    save("two-places.svg", 1280, 556, p, "Left: a browser chat reaches the model, and your files reach the chat "
         "only when you copy and paste. Right: an agent on your computer reaches the same model and opens "
         "files, runs commands and saves changes in your folder.")


# ---- 3. files opened ------------------------------------------------------
def files_opened():
    p = []
    hot = {3, 17, 22, 40, 41, 42, 77}
    for i in range(96):
        r, c = divmod(i, 16)
        on = i in hot
        p.append(box(40 + c * 56, 60 + r * 56, 44, 44, GOLD if on else RULE, fill=GOLD if on else PANEL, rx=5))
    p += [text(488, 440, "96 files in the folder", 26, MUTED),
          text(1105, 220, "7", 190, GOLD, bold=True),
          text(1105, 280, "files opened", 32, INK),
          text(1105, 360, "28 seconds", 28, MUTED)]
    save("files-opened.svg", 1280, 470, p, "A grid of 96 files with 7 marked gold: the agent opened 7 files "
         "and answered in 28 seconds.")


# ---- 4. the folder outlasts the chat --------------------------------------
def folder_keeps():
    p = []
    for i, lab in enumerate(["Monday's session", "Thursday's session", "a session on the laptop"]):
        x = 60 + i * 400
        p += [box(x, 40, 340, 100, MUTED, dash="9 7"), text(x + 170, 86, lab, 26, INK),
              text(x + 170, 120, "ends, and forgets", 21, MUTED),
              arrow(x + 120, 146, x + 120, 332, GOLD), text(x + 104, 245, "writes", 22, GOLD, "end"),
              arrow(x + 220, 332, x + 220, 146, BLUE), text(x + 236, 245, "reads", 22, BLUE, "start")]
    p += [box(40, 340, 1200, 130, GOLD, sw=3), text(640, 394, "the folder", 32, GOLD, bold=True),
          text(640, 440, "notes · decisions · results · wiki.md", 25, INK),
          arrow(60, 500, 1220, 500, MUTED, sw=2), text(640, 534, "time", 21, MUTED)]
    save("folder-keeps.svg", 1280, 550, p, "Three sessions come and go; each reads from and writes to the same "
         "folder, which stays.")


# ---- 5. across computers --------------------------------------------------
def across_computers():
    p = [box(440, 20, 400, 86, GOLD, sw=3), text(640, 60, "home repo", 30, GOLD, bold=True),
         text(640, 90, "on a git server", 21, MUTED)]
    for i, lab in enumerate(["laptop", "Linux box", "a labmate's computer"]):
        x = 40 + i * 420
        cx = x + 180
        p += [f'<path d="M 640 106 L {cx} 250" stroke="{GOLD}" stroke-width="3" fill="none" '
              'marker-end="url(#a-gold)"/>',
              box(x, 256, 360, 230, BLUE), text(cx, 300, lab, 27, INK),
              box(x + 30, 326, 300, 134, RULE, fill="#1f2125", rx=6),
              text(cx, 362, "research-home/", 23, GOLD, mono=True),
              text(cx, 398, "same wiki files", 21, MUTED), text(cx, 430, "same skills, same repos", 21, MUTED)]
    p += [box(432, 150, 416, 52, RULE, fill="#1b1c1f", rx=6),
          text(640, 184, "git clone, then ./bootstrap.sh", 22, INK, mono=True)]
    save("across-computers.svg", 1280, 506, p, "One home repo on a git server is cloned to a laptop, a Linux box "
         "and a labmate's computer; each gets the same folder.")


# ---- 6. home layout -------------------------------------------------------
def home_layout():
    p = [box(20, 20, 1240, 510, GOLD, fill="#232428", sw=3, rx=14),
         text(50, 66, "research-home/", 30, GOLD, "start", mono=True, bold=True),
         text(330, 64, "the home repo: it holds only these files", 22, MUTED, "start")]
    x = 50
    for lab in ["wiki.md", "repos.txt", "bootstrap.sh", "skills"]:
        w = len(lab) * 14 + 36
        p += [box(x, 88, w, 44, GOLD, rx=6), text(x + w / 2, 118, lab, 21, INK, mono=True)]
        x += w + 14
    cols = [("papers/", 50, 540), ("code/", 610, 300), ("tooling/", 930, 300)]
    for name, cx, cw in cols:
        p += [box(cx, 160, cw, 296, RULE, fill=PANEL),
              text(cx + 20, 200, name, 26, INK, "start", mono=True),
              box(cx + cw - 122, 174, 104, 36, GOLD, rx=6), text(cx + cw - 70, 199, "wiki.md", 18, INK, mono=True)]
    for i in range(7):
        r, c = divmod(i, 4)
        bx, by = 75 + c * 126, 232 + r * 72
        p += [box(bx, by, 112, 56, BLUE, fill="#1f2125", rx=6), text(bx + 56, by + 36, f"pub{i + 1}", 22, INK, mono=True)]
    p += [box(75, 376, 364, 56, BLUE, fill="#1f2125", rx=6), text(257, 412, "paper-library", 22, INK, mono=True)]
    for i, lab in enumerate(["pykmc", "pylatkmc", "analysis-tools"]):
        p += [box(630, 232 + i * 72, 260, 56, BLUE, fill="#1f2125", rx=6),
              text(760, 268 + i * 72, lab, 22, INK, mono=True)]
    p += [box(950, 232, 260, 56, BLUE, fill="#1f2125", rx=6), text(1080, 268, "paper-catalogue-mcp", 19, INK, mono=True)]
    p += [box(50, 478, 30, 30, BLUE, fill="#1f2125", rx=5),
          text(94, 501, "a git repo of its own, with its own history. The home repo ignores it.", 22, MUTED, "start")]
    save("home-layout.svg", 1280, 550, p, "The home folder holds wiki.md, repos.txt, bootstrap.sh and skills, and "
         "three folders, papers, code and tooling, each with a wiki.md and nested git repos.")


# ---- 7. papers by topic ---------------------------------------------------
def topics():
    p = []
    heads = [("topic", 175), ("sub-topic", 485), ("repo", 765), ("paper note", 1090)]
    for lab, cx in heads:
        p.append(text(cx, 40, lab, 22, BLUE))
    col1 = [("Dealloying", False), ("Diffusion and defects", False), ("KMC methods", True)]
    for i, (lab, hot) in enumerate(col1):
        y = 70 + i * 130
        p += [box(30, y, 290, 64, GOLD if hot else RULE, sw=3 if hot else 2),
              text(175, y + 41, lab, 24, INK if hot else MUTED)]
    col2 = [("Prior art", True, 250), ("kART and ART", False, 380)]
    for lab, hot, y in col2:
        p += [box(370, y, 230, 64, GOLD if hot else RULE, sw=3 if hot else 2),
              text(485, y + 41, lab, 24, INK if hot else MUTED),
              f'<path d="M 320 362 C 345 362, 345 {y + 32}, 370 {y + 32}" fill="none" '
              f'stroke="{GOLD if hot else RULE}" stroke-width="{3 if hot else 2}"/>']
    p += [box(650, 250, 230, 64, GOLD, sw=3), text(765, 280, "pub3", 24, INK, mono=True),
          text(765, 303, "5 papers", 18, MUTED),
          f'<path d="M 600 282 L 650 282" stroke="{GOLD}" stroke-width="3"/>',
          box(650, 380, 230, 64, RULE), text(765, 410, "pub2", 24, MUTED, mono=True),
          text(765, 433, "2 papers", 18, MUTED),
          f'<path d="M 600 412 L 650 412" stroke="{RULE}" stroke-width="2"/>']
    for i, lab in enumerate(["Kara2009", "LefevreLopez2024", "VanDerVen2001"]):
        y = 140 + i * 84
        p += [box(940, y, 300, 60, GOLD, sw=3), text(1090, y + 39, lab, 22, INK, mono=True),
              f'<path d="M 880 282 C 910 282, 910 {y + 30}, 940 {y + 30}" fill="none" stroke="{GOLD}" stroke-width="3"/>']
    p += [text(1090, 420, "and 2 more", 20, MUTED),
          f'<path d="M 30 490 L 880 490" stroke="{BLUE}" stroke-width="2"/>',
          text(455, 522, "papers/wiki.md", 22, BLUE, mono=True),
          f'<path d="M 940 490 L 1240 490" stroke="{BLUE}" stroke-width="2"/>',
          text(1090, 522, "pub3/wiki.md", 22, BLUE, mono=True)]
    save("topics.svg", 1280, 540, p, "papers/wiki.md lists topics and sub-topics and names the repo that holds "
         "papers on each; pub3/wiki.md lists the paper notes under the same sub-topic.")


# ---- 8. keep the wiki up to date -----------------------------------------
def keep_current():
    cards = [("You add", ["a repo, a folder", "or a note"], BLUE),
             ("Slim entry in the wiki", ["what it is,", "and a link to it"], GOLD),
             ("A script checks", ["that every link", "still works"], GOLD)]
    p = []
    for i, (head, lines, col) in enumerate(cards):
        x = 30 + i * 430
        p += [box(x, 40, 360, 220, col, sw=3), text(x + 180, 100, head, 30, INK, bold=True)]
        for j, ln in enumerate(lines):
            p.append(text(x + 180, 160 + j * 40, ln, 25, MUTED))
        if i < 2:
            p.append(arrow(x + 368, 150, x + 422, 150, MUTED, sw=4))
    save("keep-current.svg", 1280, 300, p, "Three steps: you add a repo, folder or note; it gets a slim entry in "
         "the wiki; a script checks the links.")


# ---- 9. three add-ons -----------------------------------------------------
def three_addons():
    p = [box(450, 170, 380, 150, GOLD, sw=3), text(640, 236, "the agent", 32, GOLD, bold=True),
         text(640, 276, "what it is reading now", 22, MUTED)]
    # skill
    p += [box(40, 185, 300, 120, BLUE), text(190, 236, "Skill", 30, INK, bold=True),
          text(190, 274, "find-paper", 22, MUTED, mono=True),
          arrow(346, 245, 444, 245, BLUE),
          text(190, 346, "written steps, read", 22, INK), text(190, 376, "when the task needs them", 22, INK)]
    # subagent
    p += [box(940, 185, 300, 120, BLUE), text(1090, 236, "Subagent", 30, INK, bold=True),
          text(1090, 274, "paper-reader", 22, MUTED, mono=True),
          arrow(836, 222, 934, 222, BLUE), text(885, 208, "a task", 20, MUTED),
          arrow(934, 272, 836, 272, GOLD), text(885, 300, "a summary", 20, GOLD),
          text(1090, 346, "a second agent that reads", 22, INK), text(1090, 376, "on its own and reports back", 22, INK)]
    # tool server
    p += [box(450, 420, 380, 110, BLUE), text(640, 466, "Tool server (MCP)", 30, INK, bold=True),
          text(640, 504, "blender", 22, MUTED, mono=True),
          arrow(640, 326, 640, 414, BLUE, both=True),
          text(860, 466, "a program the agent can call:", 22, INK, "start"),
          text(860, 496, "here, Blender, to make animations", 22, INK, "start")]
    save("three-addons.svg", 1280, 410, p, "The agent in the centre with three add-ons: a skill feeds it written "
         "steps, a subagent takes a task and returns a summary, and a tool server is a program it can call.", up=140)


# ---- 10. what is loaded at the start -------------------------------------
def startup_bar():
    total, width, x0, y, h = 26.5, 1200, 40, 150, 90
    segs = [("the agent itself", 22.7, DIM, INK), ("built-in skills", 2.7, "#6b7280", INK), ("this folder", 1.1, GOLD, GOLD)]
    p, x = [], x0
    for lab, v, fill, col in segs:
        w = width * v / total
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>')
        if v > 5:
            p += [text(x + w / 2, y + 40, lab, 28, INK), text(x + w / 2, y + 74, f"{v}k tokens", 24, INK)]
        elif fill != GOLD:
            p += [text(x + w / 2, y - 46, lab, 24, MUTED), text(x + w / 2, y - 16, f"{v}k", 24, MUTED)]
        x += w
    gx = x0 + width - width * 1.1 / total / 2
    p += [f'<path d="M {gx} {y + h} L {gx} 300 L 1010 300" stroke="{GOLD}" stroke-width="3" fill="none"/>',
          text(1000, 290, "this folder: 1.1k tokens", 34, GOLD, "end", bold=True),
          text(1000, 344, "rules 523 · root wiki 271 · 2 skills 100 · subagent 56 · paper search 82", 23, INK, "end"),
          text(40, 110, "26.5k tokens loaded before the first question", 26, MUTED, "start")]
    save("startup-bar.svg", 1280, 310, p, "A bar of 26.5 thousand tokens loaded at the start: 22.7k for the agent "
         "itself, 2.7k for built-in skills and 1.1k for this folder.", up=60)


# ---- 10b. keep the always-loaded part slim --------------------------------
def slim_start():
    p = [text(40, 48, "the context window", 24, MUTED, "start"),
         f'<rect x="40" y="66" width="150" height="92" fill="{GOLD}"/>',
         f'<rect x="190" y="66" width="1050" height="92" fill="{DIM}"/>',
         text(715, 104, "room for the work", 28, INK),
         text(715, 138, "your question, the files it opens, its answer", 22, INK),
         f'<path d="M 115 158 L 115 214" stroke="{GOLD}" stroke-width="3" fill="none"/>',
         box(40, 214, 520, 176, GOLD, sw=3),
         text(300, 262, "Always loaded", 30, GOLD, bold=True),
         text(300, 308, "skill descriptions · root wiki · rules", 24, INK),
         text(300, 352, "1.1k tokens for the demo folder", 24, GOLD),
         arrow(568, 302, 712, 302, GOLD, sw=4),
         text(640, 284, "points to", 22, GOLD),
         box(720, 214, 520, 176, BLUE, dash="9 7"),
         text(980, 262, "Read only when needed", 30, INK, bold=True),
         text(980, 308, "skill steps · deeper wikis", 24, INK),
         text(980, 352, "papers · code · data", 24, MUTED)]
    save("slim-start.svg", 1280, 410, p, "The context window as a bar: a thin slice is always loaded, skill "
         "descriptions, the root wiki and rules, and it points to what is read only when needed: skill steps, "
         "deeper wikis, papers, code and data. The rest of the window is room for the work.")


# ---- 11, 12. four numbered cards -----------------------------------------
def cards(name, items, label, arrows):
    p = []
    for i, (head, lines, mono) in enumerate(items):
        x = 20 + i * 320
        p += [box(x, 30, 280, 270, GOLD, sw=2),
              f'<circle cx="{x + 140}" cy="90" r="34" fill="{GOLD}"/>',
              text(x + 140, 103, str(i + 1), 36, "#1b1c1f", bold=True),
              text(x + 140, 176, head, 27, INK, bold=True, mono=mono)]
        for j, ln in enumerate(lines):
            p.append(text(x + 140, 224 + j * 34, ln, 22, MUTED))
        if arrows and i < 3:
            p.append(arrow(x + 284, 165, x + 314, 165, MUTED, sw=3))
    save(name, 1280, 330, p, label)


def demo_steps():
    cards("demo-steps.svg", [
        ("/context", ["what is loaded", "before a question"], True),
        ("One question", ["a paper repo and", "a code repo"], False),
        ("Seven subagents", ["one per paper repo,", "at the same time"], False),
        ("A new computer", ["clone, then", "one script"], False),
    ], "Four demo steps: /context, one question across two repos, seven subagents, a new computer.", False)


def start_steps():
    cards("start-steps.svg", [
        ("One root folder", ["put your repos", "under it"], False),
        ("wiki.md", ["one line", "per repo"], True),
        ("git init", ["ignore the", "nested repos"], True),
        ("Grow it", ["a new wiki.md when", "a folder gets big"], False),
    ], "Four steps to start: one root folder, a wiki.md, git init, and a new wiki.md as folders grow.", True)


if __name__ == "__main__":
    for f in (tokens, two_places, files_opened, folder_keeps, across_computers, home_layout, topics,
              keep_current, three_addons, slim_start, demo_steps, start_steps):
        f()
