# Building a deck — structure & from-source workflow

## The spider-web structure

reveal.js is 2D. Map a talk onto it deliberately:

- **Horizontal (spine):** the 4–6 top-level sections a listener walks (e.g. Hook → Reframe →
  Foundations → Method → Climax → Takeaways). Keep it short so the ESC overview stays legible.
- **Vertical (drill-downs):** detail hanging beneath a section — descend or skip. A section with
  drill-downs is one `<section>` wrapping several child `<section>`s; the first child is the
  section's spine slide, the rest are the drill-downs.
- **Terse on the slide, prose in the notes.** Bullets are phrases/fragments; the sentences the
  presenter actually says go in `<aside class="notes">`. This is what makes a 45-min talk: the notes
  carry the talk, the slides carry the landmarks.

## One idea per slide (reveal does not auto-shrink)

A slide taller than the ~960×700 logical area is clipped — content silently disappears off the
bottom. So:

- ~5 short bullets **or** one media element (figure / code / table) per slide, not both.
- When a drill-down has bullets *and* a figure/code block, split it: a bullets slide, then a media
  slide (same heading) directly beneath it.
- Tables that are tall: shrink the font, split into two side-by-side columns, and truncate long
  cells (full text in the notes). A reference table the audience can't read is worse than a curated
  one they can.
- Long headings cost vertical room — they wrap at 2–3 lines at default size. Reduce `h2`/`h3` if a
  bullets slide is tight.

## From source material to a deck

When a deck is built from a body of source (notes, a paper, a teaching collection):

1. **Mine** the sources for the teachable claims, the concrete examples that anchor each abstract
   point, exact terminology, memorable lines, and any code/math. Stay faithful — don't invent.
2. **Design the spine** — a coherent arc (often Hook → Reframe → Foundations → Method → Climax →
   Takeaways) that delivers everything substantive, with full speakable notes per slide and a
   recurring concrete example threaded through.
3. **Generate**, then verify the rendered result (see `verification.md`). If you generate the HTML
   programmatically from a structured outline, keep the generator script — it makes the deck
   reproducible when the source changes, and you re-run + re-verify instead of hand-patching.

## Figures: self-contained SVG

Prefer SVG authored to be fully offline and presentation-scale:

- `viewBox` ~ `0 0 1280 720` (16:9), scalable.
- **No external references** — no `<image href>`, no web fonts, no CDN. Internal `url(#marker)`
  refs (arrowheads, gradients) are fine; the only `http` allowed is the SVG namespace.
- System fonts: `font-family="system-ui, -apple-system, Segoe UI, sans-serif"`.
- A rich SVG can embed its own formula, legend, and caption — cleaner than a figure plus a separate
  KaTeX line (which tends to overflow). Place figures in `assets/` and `<img src="assets/x.svg">`.
