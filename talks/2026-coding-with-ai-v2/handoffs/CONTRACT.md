# Section-interview contract — Coding with AI v2

You are one bounded session designing ONE section of this talk with Stephen, live. This file is the
shared contract; your section brief (`section-0N-*.md`) carries the section-specific context. Read
both fully before saying anything to Stephen. This folder's `FOUNDATION.md` is the authoritative
decision record; your brief points you at the parts that bind your section.

## Working state

- Branch: `claude/claude-presentation-v2-scope-453c9c` of the presentations repo. The v2 deck exists
  only on this branch. If your session did not start on it, check it out (or add a worktree from it)
  before doing anything else.
- The deck: `talks/2026-coding-with-ai-v2/index.html`. One file, no build step. Serve to preview:
  `cd talks/2026-coding-with-ai-v2 && python3 -m http.server 8032` → http://localhost:8032
- The current draft passed an evidence-fidelity audit and a language audit on 2026-07-13. It is a
  STARTING POINT, not a commitment: Stephen may keep, rework, or discard any of it.

## The interview protocol

1. **Elicit before you show.** Begin by asking Stephen what he wants this section to accomplish and
   include: the takeaway he cares about, the stories or evidence he wants in, anything he already
   knows he dislikes in the current draft. One question at a time. Do not lead with the existing
   slides; do not let the draft anchor him.
2. **Then walk the section slide by slide.** For each slide: show or describe the current draft
   version, offer one to three genuinely different alternatives (content, framing, or visual), and
   recommend one with a reason. Go back and forth until you converge.
3. **A slide is settled only when Stephen explicitly locks it.** Fluent agreement is not a lock;
   ask for the lock.
4. **New ideas are welcome.** If Stephen wants a slide, story, or visual the draft lacks, design it
   with him, within the foundation's guardrails. If he contradicts a locked foundation decision,
   point out the conflict, and if he confirms, record the change (see below) rather than silently
   diverging.

## File ownership

- Edit ONLY your section's block of `index.html`, between its `<!-- ============ N · ... -->`
  banner comment and the next section's banner. Never touch other sections, the title slide, the
  closing markup, or the `Reveal.initialize` block.
- CSS: reuse the existing classes below. If you genuinely need a new rule, ADD it to the end of
  `css/custom.css` under a `/* §N additions */` comment; never modify existing rules.
- New figures go in `assets/` as self-contained SVG (system fonts, no external refs; palette below).

## Style system — "The Invisible Variable"

Dark scientific keynote; the missing goal, context, or physical reference is revealed in gold.
Palette: near-black `#212121` canvas · white headings · light ink `#e8eaee` · muted `#9aa1ad` ·
soft blue `#8fb0dc` (secondary) · deep blue `#002452` (fills) · gold `#FABD0F` (ONLY the one
revealed/missing/decisive element) · red `#B90E31` (wrong science only).

Classes: `.kicker` (+`<span class="n">` section number) · `.take` (gold-bar takeaway) · `.goldline`
(gold key sentence) · `.gold` · `.wrong` (red strike) · `.redtext` · `.lead` · `.big` · `.small` ·
`.pair > div(.hot|.cold|.bad) > .label` (contrast cards) · `table.vocab` + `td.term` ·
`table.plain` · `img.shot` (screenshot frame) · `img.fig` · `.evidence` (mono caption).

## Hard rules (non-negotiable)

- **Offline:** no CDN or remote URL for anything that renders. Plain-text repo refs are fine.
- **One idea per slide;** reveal does not auto-shrink (~960×700). Bullets OR one media element.
- **Terse slides, full notes:** sentences live in `<aside class="notes">`, in Stephen's first-person
  voice.
- **No em dashes anywhere.** Canadian spelling (behaviour, labour, neighbour; -ize verbs;
  "minimise" is Stephen's retained form).
- Gold stays scarce; red means wrong science, nothing else.
- Evidence guardrails in FOUNDATION.md bind everything (single observed car-wash failure, no
  leaderboard; HTST catch credited to an external expected value; MECH 479 aggregate, no
  misconduct claim; handoffs labelled Stephen's account; threshold 8 is his decision; etc.).

## Before you finish

1. Serve the deck and run the overflow audit from
   `.claude/skills/author-reveal-talk/references/verification.md` — zero overflowing leaves.
2. Confirm every image loads and every leaf in your section has speaker notes.
3. If a new durable decision emerged, append it to this folder's `FOUNDATION.md` under
   "V2 scope decisions" with the next decision number.
4. Commit ONLY your section's files, plain message, no AI attribution of any kind.
5. Tell Stephen which sections remain and stop.
