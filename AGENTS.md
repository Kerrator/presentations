# AGENTS.md — Presentations

Canonical, tool-neutral contract for this repo. Any coding agent (or human) reads this first.
Tool-specific notes live in adapter files: `CLAUDE.md` imports this (`@AGENTS.md`) and adds only
Claude-Code-specific authoring detail.

## Purpose

An **offline-first reveal.js presentation system**. Each talk is a self-contained folder of plain
HTML — the HTML *is* the deck, no build step, no framework. An agent authors and revises a talk by
editing that HTML in conversation ("add a drill-down under Methods", "embed this Blender clip").

## The one invariant: stay offline

These talks are delivered on possibly-flaky conference Wi-Fi. **Never reference a CDN or any remote
URL** for code, styles, fonts, or media. Every asset lives inside the talk folder, under `lib/`
(libraries, vendored) or `assets/` (figures, videos). If something needs the network to render, it
is wrong. This is the load-bearing rule; everything else is convenience.

## Repository layout

| Path | Holds | Notes |
|---|---|---|
| `AGENTS.md`, `CLAUDE.md` | This contract + the Claude authoring adapter | Always read |
| `template/` | The reusable starter deck (its own vendored `lib/`) | Copy per talk; never present it directly |
| `talks/<slug>/` | One self-contained talk (`index.html`, `css/`, `assets/`, `lib/`) | Permanent offline archive |
| `index.html` | The talks landing page (manual `<li>` list) | Served at the Pages root |
| `fonts/` | Master copy of the handwriting font | Copied into a talk by `setup.sh` |
| `new-talk.sh` | Scaffolds `talks/<slug>/` from `template/` | |
| `setup.sh` | Re-vendors `template/lib/` from pinned versions in `package.json` | |
| `.claude/skills/author-reveal-talk/` | The talk-authoring skill (offline discipline, structure, build-from-source, verification) | Discovered automatically |

A private, machine-local layer (personal workflow notes + critical-Claude reference) may be
symlinked in as `CONTEXT.md` from a separate config repo; it is hidden from this repo's git and is
**optional** — the repo is fully functional without it.

## Authoring model: a spider-web, not a flat stack

reveal.js is 2D; use it deliberately.

- **Horizontal slides** (left/right) are the **spine** — the top-level sections a listener walks.
  Keep the spine short (4–6 sections).
- **Vertical slides** (up/down) are **drill-downs** that hang beneath a section — detail you descend
  into and can skip. Push depth down so the overview stays legible.
- Slide text is **terse** (phrases, not paragraphs); full sentences go in **speaker notes**
  (`<aside class="notes">`). The menu (top-left) and **ESC** overview allow non-linear jumps for Q&A.

reveal does **not** auto-shrink slides. A slide that overflows the ~960×700 area is clipped, so
**one idea per slide**: bullets and any figure/code/table each get their own (vertical) slide.

## Build / verify loop

1. `./new-talk.sh <slug>` → edit `talks/<slug>/index.html`.
2. Serve it: `cd talks/<slug> && python3 -m http.server 8000` → `http://localhost:8000`
   (math/figures need a real server; `file://` won't do).
3. Export the PDF backup: open `…/?print-pdf`, Print → Save as PDF (landscape).

A talk is **done** only when all of these hold (verify them, don't assume):

1. Opens and advances from a local server.
2. **No network**: math, figures, and videos render with Wi-Fi off. No CDN/remote URL anywhere in
   `index.html` or `css/custom.css`.
3. **No overflow**: no slide's content exceeds the slide area (audit every leaf slide).
4. Speaker notes present; presenter view (**S**) works.
5. A landscape **PDF export** exists in the talk folder (offline backup + Apple-Pencil inking surface).

## Working rules

- Keep this file and adapters short and role-pure (< ~150 lines). **No step-by-step procedures
  here** — those live in the `author-reveal-talk` skill.
- Default working posture: the smallest change that satisfies the request and passes the verify
  loop. Don't add build steps, frameworks, or dependencies that aren't already vendored in `lib/`;
  if a new library is genuinely needed, add it to `package.json` + `setup.sh`, never a CDN link.
- Share **project** assets only (this public repo). Personal config stays in the private layer.
- This repo is **public** (GitHub Pages). Treat everything committed here as world-readable.
