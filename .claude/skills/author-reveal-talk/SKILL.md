---
name: author-reveal-talk
description: >-
  Use when creating, revising, or verifying a talk in this offline-first reveal.js
  presentation system — scaffolding a new deck, structuring slides into the
  horizontal-spine / vertical-drilldown "spider-web", turning source material (notes,
  a paper, a teaching doc) into a deck, embedding offline math / code / SVG figures,
  fixing slides that overflow or clip, keeping a deck fully offline, or exporting the
  landscape PDF backup. Triggers: "make/build a talk", "add a slide/section", "this
  slide is cut off", "turn this into slides", "export the PDF".
---

# Authoring a reveal.js talk (offline-first)

The contract is in `AGENTS.md`; this is the procedure. Read
[`references/workflow.md`](references/workflow.md) and
[`references/verification.md`](references/verification.md) for the detail — don't inline them.

## The loop

1. **Scaffold.** `./new-talk.sh <slug>` copies `template/` (with its own vendored `lib/`) into
   `talks/<slug>/`. Edit `talks/<slug>/index.html`; never edit `template/` to build a talk.
2. **Structure the spine.** 4–6 **horizontal** sections (the spine a listener walks); push detail
   into **vertical** drill-downs. Slide text is terse phrases; full prose goes in
   `<aside class="notes">`. See `references/workflow.md` for turning source material into a spine and
   the **one-idea-per-slide** rule (bullets and any figure/code/table get separate slides — reveal
   does not auto-shrink).
3. **Keep it offline.** Vendored `lib/` + local `assets/` only. Figures are **self-contained SVG**
   (system fonts, internal `url(#...)` refs only, no external `href`/`<image>`/web fonts). A rich SVG
   that carries its own caption beats a figure plus a separate display-math line.
4. **Verify in a browser — this is mandatory, not optional.** Serve the folder, then run the
   overflow audit and offline checks in `references/verification.md`: zero slides overflow the
   ~960×700 area, KaTeX/figures/code render, **no CDN/remote URL**, speaker notes present.
5. **Export the landscape PDF backup** into the talk folder (`references/verification.md`).

## Known pitfalls (all cost real time if skipped)

- **KaTeX path:** the math plugin appends `/dist/`, so the init value is `local: 'lib/katex'`
  (pointing at `lib/katex/dist` doubles it → 404, math silently doesn't render).
- **`data-line-numbers`:** digits/ranges only (`"6"`, `"3-5"`). Never put code text there — an
  embedded quote breaks the HTML attribute.
- **Long code lines** clip the box; allow `white-space: pre-wrap` and shrink the font.
- **Figure + display-math on one slide** overflows; let the SVG carry the formula, drop the
  standalone math, or give math its own slide.
- **PDF export:** use `@page { size: landscape }` (the keyword); a fixed-px `@page` size collapses
  reveal's per-slide pagination to one blank page.

## Output shape

A finished talk is a self-contained `talks/<slug>/` that passes every item in the `AGENTS.md`
"done" list. When you build one programmatically from structured source, keep the generator so the
deck is reproducible if the source changes; verify the *rendered* result in a browser regardless.
