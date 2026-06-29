# CLAUDE.md — Claude authoring adapter for presentations

Read the shared repository contract first:

@AGENTS.md

This file adds only the **Claude-Code-specific authoring detail** — how to put math, code, figures,
video, notes, and live ink on a slide, plus preview/PDF specifics. The purpose, the offline
invariant, the repo layout, the spider-web model, and the build/verify/done loop all live in
`AGENTS.md` and are not repeated here.

## Where the procedure lives

For building or revising a whole talk — scaffold → structure the spine from source material → keep
it offline → audit every slide for overflow → export the PDF backup — invoke the
**`author-reveal-talk`** skill (via the Skill tool) rather than reconstructing the steps from memory.
The skill carries the checklists and the browser overflow-audit snippet.

A private, machine-local `CONTEXT.md` may be symlinked in (from a separate config repo). It holds
personal workflow notes and a critical-Claude reference. It is **optional** — absent for public
clones, and the repo is fully functional without it. If present, read it.

## How to add things to a slide

- **Math (KaTeX, offline):** inline `$E_\mathrm{f}$`, display `$$ ... $$`. The mhchem extension is
  loaded, so chemistry works: `$$\ce{CO2 + 3 H2 -> CH3OH + H2O}$$`. KaTeX covers most LaTeX but not
  everything; if an exotic macro fails, simplify it or render that one equation as an SVG into
  `assets/`. Note the math plugin appends `/dist/`, so the init path is `local: 'lib/katex'`.
- **Code:** `<pre><code class="language-python" data-trim data-line-numbers> ... </code></pre>`. Use
  `data-line-numbers="6"` (or `"3-5"`) to step/highlight — **digits and ranges only**; never put
  code text in that attribute (an embedded quote breaks the HTML). Keep lines short or they wrap.
- **Step-by-step reveals:** add `class="fragment"` to any element.
- **Figures:** put SVG/PNG in `assets/` and `<img src="assets/figure.svg">`. Prefer self-contained
  SVG (system fonts, no external `href`/`<image>`); a rich SVG can carry its own caption and is
  cleaner than a figure + a separate display-math line that tends to overflow.
- **Blender animations:** keep the `.mp4` in `assets/`. Inline:
  `<video data-autoplay controls src="assets/clip.mp4"></video>`. Full-bleed background:
  `<section data-background-video="assets/anim.mp4" data-background-video-loop data-background-video-muted>`.
- **Speaker notes:** `<aside class="notes"> full prose </aside>` inside a slide. Press **S** for the
  presenter view (notes + timer + next-slide preview). Slides stay terse; sentences live here.

## Live inking (Apple Pencil) — and its honest limit

The chalkboard plugin is enabled: **C** annotates the current slide, **B** opens a blank chalkboard,
**D** downloads drawings as JSON. It takes Pencil/touch input in iPad Safari/Chrome but **has no palm
rejection**. For serious annotation, export the deck to PDF (below) and ink on it in
GoodNotes/Notability — always carry that PDF anyway.

## Previewing

Math, Markdown, and external assets need a real server — `file://` won't do.

```
cd talks/<slug> && python3 -m http.server 8000   # then open http://localhost:8000
```

## Exporting a PDF (always do this before a talk)

Open the deck with `?print-pdf` appended (`http://localhost:8000/?print-pdf`), then Print → **Save as
PDF** (Chrome, enable "Background graphics", margins None, **landscape**). Headless equivalent:
`chrome --headless=new --no-pdf-header-footer --print-to-pdf=out.pdf "http://localhost:PORT/?print-pdf"`
with a `@media print { @page { size: landscape; margin: 0 } }` rule in `custom.css` (a fixed-px
`@page` size collapses reveal's pagination — use the keyword). This PDF is the inking surface and the
conference backup.

## Conventions for this author

- Domain: nuclear alloys (Ni–Fe–Cr–Al, Zr), CO₂ catalysis, kinetic Monte Carlo, k-ART. Tools:
  Quantum ESPRESSO (DFT), LAMMPS (MD), NWChem, pyKMC. Use correct terminology and units; don't dumb
  down the science.
- Writing: Canadian spelling (Canadian Press style, Canadian Oxford Dictionary). Slide text terse —
  phrases, not paragraphs. Put sentences in speaker notes.
- Adding the handwriting font: drop `myhand.woff2` into `fonts/`, run `./setup.sh`; the deck picks it
  up automatically via the `@font-face` in `css/custom.css`.
