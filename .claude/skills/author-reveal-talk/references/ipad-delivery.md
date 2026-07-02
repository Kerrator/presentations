# Delivering a talk from an iPad (presenting · Apple Pencil ink)

Findings verified against the vendored chalkboard v2.3.3 (reveal.js-plugins 4.6.0), reveal 6.0.1,
and iPadOS Safari behaviour (2026-07). Two modes exist — pick one before the talk, not at the podium.

## The short version

| Goal | Best path today |
|---|---|
| Present slides | Either mode; a standalone iPad navigates fully by touch |
| Ink live with your palm on the glass | **Sidecar** (iPad as Mac display; the Pencil is the pointer) |
| Serious annotation / markup | The landscape **PDF in GoodNotes/Notability** (native palm rejection) |
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

**Inking: limited until the planned patches land (see below).**

- **No palm rejection** — finger, palm, and Pencil draw identically. Hover; don't rest the hand.
- **No touch path into ink mode** — C/B are keyboard bindings, and this vendored build has no
  on-screen toggle buttons (the `toggle*Button` config options are dead code; the buttons live in
  the un-vendored `customcontrols` sibling plugin). Without a hardware keyboard you cannot start
  annotating.
- **D-download is unreliable** in iPadOS Safari (blob-URL download quirks) — export ink from the
  Mac, or use the PDF path.

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

## Planned fixes (agreed 2026-07, not yet applied)

1. **Pencil-only patch** (< 10 lines, vendored): gate the chalkboard's `touchstart`/`touchmove` on
   `touch.touchType === 'stylus'`, moving the unconditional `preventDefault` behind the gate so
   finger swipes still navigate. Upstream master is still 2.3.3 with no stylus support — patch,
   don't upgrade. Apply to the talk **and** `template/lib/`; re-apply after any `setup.sh` re-vendor.
2. **Touch toggle buttons**: small fixed-position buttons calling the public
   `RevealChalkboard.toggleNotesCanvas()` / `.toggleChalkboard()` API, added in `template/`.
3. **`storage` on by default** in the template's chalkboard config.
4. **Video guidance**: `<video data-autoplay muted playsinline controls src=...>` — iOS autoplay
   policy rejects the first unmuted play (reveal auto-adds `playsinline` on iPad and retries muted,
   but declaring both is the reliable form; Blender clips are silent anyway).
5. **Drop the no-op viewport attributes** (`user-scalable=no`, `maximum-scale`) — iOS has ignored
   them since iOS 10; they protect nothing during inking.
