# Verifying a talk (offline · no overflow · PDF)

Verification is mandatory — a deck that *looks* right in source routinely clips slides or silently
fails to render math. Serve it and check in a real browser.

```
cd talks/<slug> && python3 -m http.server 8000   # http://localhost:8000
```

## 1 · Offline / no-CDN (the load-bearing invariant)

Grep the authored files (vendored `lib/` is exempt; the SVG namespace is not a fetch):

```
grep -noE "https?://[^\"' )]+" index.html css/custom.css | grep -viE "w3\.org"   # expect NONE
grep -oE '(src|href)="[^"]+"' index.html | sort -u                                # all local: css/ lib/ assets/
```

For each SVG in `assets/`, confirm no external fetch: `xlink:href`/`href`/`<image>` pointing out, or
web-font `url()`. Internal `url(#...)` marker refs and the `xmlns="http://www.w3.org/2000/svg"`
namespace are fine. Then test with Wi-Fi **off**.

## 2 · Per-slide overflow audit (run in the page console / preview eval)

reveal doesn't auto-shrink, so measure every *leaf* slide against the configured height. This walks
the whole deck and returns the overflowing ones:

```js
(() => {
  Reveal.configure({ transition: 'none', fragments: false });   // show all fragments = worst case
  const H = Reveal.getConfig().height || 700;
  const stacks = document.querySelectorAll('.reveal .slides > section');
  const over = [];
  for (let h = 0; h < stacks.length; h++) {
    const vs = stacks[h].matches('.stack')
      ? stacks[h].querySelectorAll(':scope > section') : [stacks[h]];
    for (let v = 0; v < vs.length; v++) {
      Reveal.slide(h, v);
      const el = Reveal.getCurrentSlide();         // the LEAF slide (not the parent stack)
      void el.offsetHeight;                          // force reflow
      if (el.scrollHeight > H + 6) {
        const head = (el.querySelector('h1,h2,h3') || {}).textContent || '';
        over.push({ h, v, scrollH: el.scrollHeight, head: head.slice(0, 44) });
      }
    }
  }
  return JSON.stringify({ overflowing: over.length, slides: over });
})()
```

`overflowing: 0` is the pass condition. Use `Reveal.getCurrentSlide()` — querying `section.present`
returns the parent *stack* and reports a misleading summed height. Fix overflow by splitting the
slide (bullets vs media), shrinking fonts, or trimming a table; then re-run until zero.

## 3 · Render checks

- `document.querySelectorAll('.katex').length > 0` if the deck has math, and no leftover raw `$$` in
  body text. If KaTeX didn't load, check the init path is `local: 'lib/katex'` (the plugin appends
  `/dist/`) and that the script src resolved (not `lib/katex/dist/dist/...`).
- Every `img.fig` has `naturalWidth > 0` (figure loaded).
- `<pre code>` is highlighted and not horizontally clipped (`scrollWidth <= clientWidth`).
- `document.querySelectorAll('aside.notes').length` > 0; presenter view (**S**) shows them.

## 4 · Landscape PDF backup

Manual: open `http://localhost:8000/?print-pdf`, Print → Save as PDF (Chrome; background graphics
on, margins None, **landscape**). Headless:

```
chrome --headless=new --disable-gpu --no-pdf-header-footer --no-margins \
  --virtual-time-budget=20000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="talks/<slug>/<slug>.pdf" "http://localhost:PORT/?print-pdf"
```

Requires `@media print { @page { size: landscape; margin: 0 } }` in `css/custom.css`. **Do not** set
a fixed-px `@page` size — it collapses reveal's per-slide pagination to a single blank page. Verify
the result: landscape MediaBox (width > height), one page per slide, figures present.
