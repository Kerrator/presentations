# Delivering a talk from an iPad (presenting · Apple Pencil ink)

Findings verified against the vendored chalkboard v2.3.3 (reveal.js-plugins 4.6.0), reveal 6.0.1,
and iPadOS Safari behaviour (2026-07). Two modes exist — pick one before the talk, not at the podium.

## The short version

| Goal | Best path today |
|---|---|
| Present slides | Either mode; a standalone iPad navigates fully by touch |
| Ink live | Sidecar, or standalone Safari (the vendored plugin is patched stylus-only) |
| Serious annotation / markup | The landscape **PDF in GoodNotes/Notability** (the durable copy) |
| Presenter notes on stage | Sidecar (press **S** on the Mac), or the notes-included PDF on a second device |

## Mode 1 — connected to the Mac via Sidecar (recommended for live ink)

1. Serve on the Mac: `cd talks/<slug> && python3 -m http.server 8000`.
2. Drag the browser fullscreen onto the iPad's Sidecar display; feed the projector as usual.
3. Ink with the Pencil. It arrives as **mouse events**, which the chalkboard already handles, and
   fingers don't drive Mac apps — so palm rejection is effectively free on macOS ≤ 26
   (macOS 27 loosened finger input into Sidecar: rehearse once before relying on it).
4. The Mac keyboard supplies everything touch cannot: **C** annotate, **B** board, **D** download
   ink, **S** presenter view, **DEL/BACKSPACE** clear, **X/Y** cycle colours.

Caveats: a Pencil barrel/secondary click maps to *erase* (the plugin's `button == 2` branch); the
pointer auto-hides after 5 s of stillness (`hideInactiveCursor: false` if that bothers you).

## Mode 2 — standalone iPad

**Serving.** Safari cannot open a talk from `file://`; serve on-device. Primary recipe: **a-Shell**
(free, bundles Python) — sync the talk folder via Files/iCloud, then

```
cd <talk-folder> && python3 -m http.server 8000    # open http://localhost:8000 in Safari
```

localhost works with Wi-Fi fully off. WorldWideWeb.app is the no-terminal GUI equivalent. The
GitHub Pages URL also works but **only with live internet** — there is no service worker, so a
loaded tab does not survive going offline. Never bet a venue on it.

**Presenting: works by touch.** Swipe or the control arrows advance; the menu hamburger (bottom-left)
jumps to any slide. No touch gesture exists for the ESC overview, pause/blackout, or fullscreen —
plan around the menu instead.

**Inking: patched to be usable (2026-07); one honest limit remains.**

- **Palm rejection is patched in**: the vendored plugin is stylus-only where the platform reports
  `Touch.touchType` (iPadOS Safari), so the Pencil inks and a resting palm/finger does not.
  `chalkboard: { stylusOnly: false }` restores finger drawing. Test once on the real iPad before a
  talk — this is a local patch, not upstream behaviour.
- **Touch entry exists**: the on-screen ink bar (bottom-left: pen / board / clear) replaces the
  C/B/DEL keys. Colour and eraser are on the palette that appears while inking.
- **D-download is still unreliable** in iPadOS Safari (blob-URL download quirks) — export ink from
  the Mac, or use the PDF path. Ink survives a reload (per-talk `storage` key, sessionStorage) but
  dies with the tab.

**Presenter view: none.** **S** opens a popup that becomes a same-screen tab on iPadOS, and external
displays mirror — so standalone notes = the notes-included PDF on a second device or on paper.

**Projection.** USB-C/HDMI out mirrors the screen and works offline (no notes). AirPlay also
mirrors but needs a network — avoid at flaky venues.

## The two PDFs (both made on the Mac; the iPad only consumes them)

- **Deck PDF** (`?print-pdf`, landscape): the GoodNotes/Notability inking surface and the
  conference backup. Required by the `AGENTS.md` done-list.
- **Notes PDF** (`?print-pdf&showNotes=separate-page`): the spoken script — the deck PDF omits
  speaker notes entirely, and this deck's prose lives in the notes. Carry both.

PDF export is desktop-Chrome-only; iPad "Chrome" is WebKit and cannot produce it.

## Chalkboard facts worth knowing (v2.3.3)

- Ink is **memory-only** unless `chalkboard: { storage: '<talk>-chalkboard' }` is set — a reload or
  Safari tab-eviction mid-talk destroys annotations. sessionStorage still dies with the tab; the
  PDF is the durable copy.
- `src: 'chalkboard.json'` preloads drawings (pre-drawn overlays), offline-safe.
- A stroke cannot flip slides: the canvas sets `data-prevent-swipe` and reveal ignores pen-type
  pointers for swipe navigation; the idle canvas is click-through, so normal touch nav is unaffected.
- The blank board's up/down chevrons render via the **menu plugin's** vendored Font Awesome. If a
  talk ever drops the menu plugin, add a Font Awesome link or those glyphs go empty.
- The index-rail CSS needs iPadOS 15.4+ (`:has()`); older iPads lose the rail cosmetically, nothing
  else breaks.

## The applied fixes (2026-07), and how they are maintained

1. **Stylus-only patch** (vendored, in the talk and `template/lib/`): an `inkingTouch()` helper
   gates the chalkboard's `touchstart`/`touchmove`/`touchend` so only `touchType === 'stylus'` (or
   platforms that report no `touchType` at all) inks; palm-lift mid-stroke does not cut the Pencil
   line. Config: `chalkboard: { stylusOnly: false }` disables it. Upstream is still 2.3.3 with no
   stylus support — the patch lives in `patches/chalkboard-stylus-only.patch` and **`setup.sh`
   re-applies it after every re-vendor** (if it stops applying after a version bump, re-derive it
   from this section and `git diff`).
2. **Touch ink bar**: fixed-position pen / board / clear buttons (bottom-left) in the talk and
   template `index.html`, calling the plugin's public `RevealChalkboard` API. Styled in
   `custom.css` (`.inkbar`), hidden in print, icons from the menu plugin's vendored Font Awesome.
3. **Per-talk ink `storage`**: the template config carries `storage: 'TALK_SLUG-chalkboard'` and
   `new-talk.sh` substitutes the slug, so two talks served from the same origin never share ink.
4. **Video pattern** is now `<video data-autoplay muted playsinline controls src=...>` in CLAUDE.md
   and the template example (iOS autoplay policy rejects the first unmuted play).
5. **Viewport meta** dropped the no-op `user-scalable=no` / `maximum-scale` attributes (ignored
   since iOS 10).
