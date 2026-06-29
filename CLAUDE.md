# CLAUDE.md — playbook for authoring presentations

This repo is an **offline-first reveal.js presentation system**. You (Claude Code)
author each talk by writing plain HTML. There is no build step and no framework to
learn — the HTML *is* the deck.

## The one rule that governs everything: stay offline

These talks are delivered at conferences on possibly-flaky Wi-Fi. **Never reference a
CDN or any remote URL for code, styles, fonts, or media.** Every asset must live
inside the talk folder, under `lib/` (libraries, already vendored) or `assets/`
(figures, videos). If something needs a network connection to render, it is wrong.

## Repo layout

```
template/            the reusable starter deck — copy this per talk, never present it directly
  index.html         wired for math, code, chalkboard, menu, speaker notes
  css/custom.css     house style + handwriting @font-face
  css/fonts/         the handwriting font (copied in by setup.sh)
  lib/               vendored reveal.js v6, KaTeX, chalkboard, menu (offline)
  assets/            figures and Blender .mp4s for that talk
talks/               one self-contained folder per real talk (e.g. talks/2026-mrs-zr-alloys/)
fonts/               master copy of the handwriting font + instructions
setup.sh             re-vendors lib/ from pinned versions in package.json
new-talk.sh          scaffolds talks/<slug>/ from template/
```

## Starting a new talk

Run `./new-talk.sh <slug>` (e.g. `2026-mrs-fall-zr-alloys`). That copies the whole
template — including its own `lib/` — into `talks/<slug>/`, so the folder is a
permanent, self-contained, offline archive. Then edit `talks/<slug>/index.html`.
Never edit files in `template/` to build a talk; only edit it to change the house default.

## The structure: a "spider-web", not a flat stack

reveal.js is 2D. Use it deliberately:

- **Horizontal slides** (left/right) are the **spine** — the top-level sections a
  listener walks through: Motivation → Methods → Results → Outlook.
- **Vertical slides** (up/down) are **drill-downs** that hang beneath a section —
  detail you descend into and can skip past. Nest them with a `<section>` wrapping
  several child `<section>`s.
- This maps a research talk onto a map: the audience sees the spine, and each section
  has optional depth. The slide **menu** (top-left) and **ESC** overview let you (or a
  questioner) jump anywhere non-linearly.

Keep the spine short (4–6 sections). Push detail down into verticals so the overview
stays legible.

## How to add things

- **Math (KaTeX, offline):** inline `$E_\mathrm{f}$`, display `$$ ... $$`. The mhchem
  extension is loaded, so chemical equations work: `$$\ce{CO2 + 3 H2 -> CH3OH + H2O}$$`.
  KaTeX covers most LaTeX but not everything; if an exotic macro fails, simplify it or
  render that one equation as an SVG into `assets/`.
- **Code:** `<pre><code class="language-python" data-trim data-line-numbers> ... </code></pre>`.
  Use `data-line-numbers="3-5"` to highlight/step through lines.
- **Step-by-step reveals:** add `class="fragment"` to any element.
- **Figures:** put SVG/PNG in `assets/` and `<img src="assets/figure.svg">`. Prefer SVG.
- **Blender animations:** keep the `.mp4` in `assets/`. Inline:
  `<video data-autoplay controls src="assets/clip.mp4"></video>`. Full-bleed background:
  `<section data-background-video="assets/anim.mp4" data-background-video-loop data-background-video-muted>`.
  reveal pauses video automatically when you navigate away.
- **Speaker notes:** `<aside class="notes"> ... </aside>` inside a slide. Press **S**
  during the talk for the presenter view (notes + timer + next-slide preview).

## Live inking (Apple Pencil) — and its honest limit

The chalkboard plugin is enabled: **C** annotates the current slide, **B** opens a
blank chalkboard, **D** downloads drawings as JSON. It accepts Pencil/touch input in
iPad Safari/Chrome **but has no palm rejection** — resting a hand can leave stray
marks. For quick marks during a talk it's fine. When high-fidelity annotation matters,
the reliable path is: export the deck to PDF (below) and ink on it in
GoodNotes/Notability with real palm rejection. Always carry that PDF anyway.

## Previewing

Math, Markdown, and external assets need a real server — `file://` won't do. From a
talk folder:

```
cd talks/<slug> && python3 -m http.server 8000   # then open http://localhost:8000
```

## Exporting a PDF (always do this before a talk)

Open the deck with `?print-pdf` appended to the URL
(`http://localhost:8000/?print-pdf`), then the browser's Print dialog → **Save as PDF**.
Use Chrome, enable "Background graphics", set margins to None. This PDF is both the
inking fallback and the conference backup if anything misbehaves live.

## Conventions for this author

- Domain: nuclear alloys (Ni–Fe–Cr–Al, Zr), CO₂ catalysis, k-ART. Tools: Quantum
  ESPRESSO (DFT), LAMMPS (MD), NWChem. Use correct terminology and units; don't
  dumb down the science.
- Writing: Canadian spelling (Canadian Press style, Canadian Oxford Dictionary).
  Slide text should be terse — phrases, not paragraphs. Put sentences in speaker notes.
- Keep each talk self-contained and offline. Don't introduce dependencies that aren't
  already vendored in `lib/`; if a new library is genuinely needed, add it to
  `package.json` and `setup.sh` rather than linking a CDN.

## Definition of done for a talk

1. Opens and advances correctly from a local server.
2. All math, figures, and videos render with **no network** (test with Wi-Fi off).
3. Speaker notes present; presenter view (S) works.
4. A PDF export exists in the talk folder as backup + for Pencil annotation.
5. No CDN/remote URLs anywhere in `index.html` or `custom.css`.
