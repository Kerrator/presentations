# Presentations

My system for building talks: **reveal.js**, authored with **Claude Code**, fully
**offline**, with handwriting fonts, LaTeX/chemistry math, embedded Blender animations,
live Apple Pencil inking, and PDF export. One self-contained folder per talk.

## Why this setup

- **Claude writes the deck.** A talk is plain HTML, so iterating is a conversation
  ("add a drill-down under Methods; embed this Blender clip; make the title use my
  handwriting font"). No proprietary format, no lock-in.
- **2D "spider-web" navigation.** Horizontal slides are the section spine; vertical
  slides are drill-downs that hang beneath each section. The menu and ESC overview let
  you jump anywhere — useful for Q&A.
- **Offline by construction.** Every library and asset is vendored locally, so a talk
  runs with the Wi-Fi off.

## Quick start

```bash
git clone <this-repo> && cd presentations
./setup.sh                         # vendors reveal.js, KaTeX, chalkboard, menu into template/lib
./new-talk.sh 2026-my-talk         # scaffold a self-contained talk
cd talks/2026-my-talk
python3 -m http.server 8000        # preview at http://localhost:8000
```

Then point Claude Code at the talk folder and describe the slides. It follows the
conventions in [`CLAUDE.md`](CLAUDE.md).

## Add your handwriting font

See [`fonts/README.md`](fonts/README.md). Short version: make a font on the iPad
(iFontMaker or Calligraphr), drop `myhand.woff2` into `fonts/`, run `./setup.sh`.

## Keyboard shortcuts (during a talk)

| Key | Action |
|-----|--------|
| ← → ↑ ↓ | Navigate the spider-web (sections / drill-downs) |
| `S` | Presenter view (speaker notes + timer + next-slide preview) |
| `ESC` / `O` | Slide overview map |
| `C` | Annotate the current slide (chalkboard) |
| `B` | Blank chalkboard |
| `D` | Download annotations as JSON |
| `F` | Fullscreen |
| menu button (top-left) | Jump to any slide |

## Export a PDF (do this before every talk)

Open `http://localhost:8000/?print-pdf`, then Print → **Save as PDF** (Chrome; enable
background graphics, margins None). The PDF is your offline backup **and** the
high-fidelity surface for Apple Pencil annotation in GoodNotes/Notability — the
chalkboard plugin has no palm rejection, so for serious inking, annotate the PDF.

## Updating libraries

Bump versions in `package.json`, then `./setup.sh`. Existing talks keep their own pinned
copies, so they never break.

## Troubleshooting

- **Math/Markdown not rendering** — you opened `index.html` as a `file://`. Serve it
  (`python3 -m http.server`) instead.
- **Equation won't render** — KaTeX supports most but not all LaTeX. Simplify the macro
  or render that one equation as an SVG into `assets/`.
- **Video won't play offline** — make sure the `.mp4` is in the talk's `assets/`, not
  linked remotely, and that you serve from a folder (not a single embedded HTML file).

## Licensing

Bundled libraries are MIT (reveal.js, KaTeX, reveal.js-plugins/chalkboard,
reveal.js-menu); see each package for details. Your slide content and fonts are yours —
add a `LICENSE` for your own material if you publish this repo.
