# Public Skills repo: decision record and build plan

Scoped 2026-07-27 via `interview-design-decisions`. Ten decisions locked below, then a phased plan
naming every file in all four repos. Nothing has been built yet.

The repo exists because the talk promises it. `index.html:1016` currently says *"It currently lives
in a private repo; I am moving it into a public one for the group to use."* This plan makes that
sentence true and puts the address on the slide.

---

## Locked decisions

**R1. The repo is a curated showcase, not a toolkit.**
A visitor who scans the QR mid-talk gets a small set of well-maintained Skills to read as worked
examples. No installer, no profiles, no eval harness. Rejected: shipping `install-profile.sh` +
`profiles/`, mirroring `ai-workflow-engineering` publicly, and a method-only teaching repo.

**R2. Public files are hand-authored, not synced. There is no export script.**
Not an export, not a subtree, not a snapshot script. `ai-workflow-engineering` stays private and
remains where the working copies evolve. Accepted cost: the two copies diverge, managed by R9.

> **Amended 2026-07-27, after R11.** The original wording said "independent hand-authored rewrites".
> That no longer applies to the three adopted Skills: rewriting Matt Pocock's prose to sound like
> Stephen's, while a column truthfully labels it as adapted, works against the labelling. Those three
> ship close to as-published. All five instead get **minimal edits**: strip bookkeeping, fix dangling
> references, make each folder self-contained.

**R3. Five Skills ship.**
`interview-design-decisions`, `diagnosing-bugs`, `handoff`, `writing-great-skills`,
`refine-instruction-surface`. Roughly 950 lines total including `references/`.
`review-analysis-claims` was considered and dropped.

**R4. The repo is `github.com/Kerrator/skills`.**
Owner `Kerrator`, consistent with `presentations`, `WinterAtomics`, `ai-workflow-engineering`,
`claude-configs`. Short enough to read aloud and type from a slide.

**R5. Skill files carry no provenance metadata.**
The `<!-- Vendored skill ... SOURCE-SHA ... Re-sync from upstream -->` blocks are internal
maintenance bookkeeping and are stripped entirely. A public Skill file is the procedure and nothing
else.

**R6. MIT attribution lives in `LICENSE` + `CREDITS.md`.**
MIT requires the notice travel with the code but not inside each file, so R5 and this are compatible.
`CREDITS.md` names the affected Skills, the upstream repo, and the copyright holder.

> **Corrected 2026-07-27.** This decision was taken believing **two** Skills were adapted. Checking
> all five against a local clone of `mattpocock/skills` showed **three**, and that the in-file vendor
> headers are not a reliable signal. See R11 for the evidence and the fix.

**R7. Skill folders sit at the repo root.**
`handoff/`, `interview-design-decisions/`, `diagnosing-bugs/`, `writing-great-skills/`,
`refine-instruction-surface/`, plus `README.md`, `LICENSE`, `CREDITS.md`. The repo name already says
"skills", so no `skills/skills/` nesting. Each folder keeps its own `references/` and `scripts/`.

**R8. The README is a minimal index with a short design section.**
What each Skill does, a short "how these were designed" part, how to install one, licence pointer.
Explicitly not a long essay and not a restatement of the talk. The weight sits in the Skill files,
which are already well written.

**R9. Drift is managed by a dated line plus one pointer.**
The README states these are public versions current as of a stated date, written for a reader rather
than exported. `ai-workflow-engineering` gains one short note recording which five have public
counterparts, so the coupling is discoverable later without being remembered. No sync process.

**R10. The private `handoff` Skill is corrected first, then the public one is written from it.**
`skills/method/handoff/SKILL.md` lines 31 and 86 tell the agent to reach for compaction when
barreling at one continuous problem. FOUNDATION decision 120 records the opposite position: *"I do
not think you should hit compaction often if ever."* That decision routed around the file rather
than fixing it. This plan fixes it at the source, so both copies state the same, correct thing.

**R11. Each Skill's origin is stated in the README index.** (2026-07-27, after the provenance check.)
Verified against a local clone of `mattpocock/skills`, three of the five are that repo's work with
small edits, not two:

| Skill | Evidence |
|---|---|
| `writing-great-skills` | One word changed in an 82-line `SKILL.md`, one in a 195-line `GLOSSARY.md`. `docs/adoptions.md` (2026-07-03) says "vendored verbatim". Carries **no** in-file vendor header. |
| `diagnosing-bugs` | 134 upstream lines; ~7 differ substantively. `hitl-loop.template.sh` byte-identical. |
| `interview-design-decisions` | Upstream's `grilling`, renamed; body word-for-word bar two phrasings and a dropped closing line. |
| `handoff` | Original. 97 lines against upstream's 16, written independently after a Pocock video. |
| `refine-instruction-surface` | Original, built in-repo. |

MIT permits redistribution with the notice retained, so this is not a legal problem; it is a
representational one, since the slide says "Every Skill I maintain lives in one repo". The fix: the
minimal-index README gains an **Origin** column reading "original" or "adapted from
mattpocock/skills". Files stay clean per R5, and `CREDITS.md` covers three.

**Deck-facing decision (to be recorded as FOUNDATION 122 at build time).**
The URL and QR go on the existing drill-down "One shelf, under version control"
(`index.html:998`), and the stale private-repo speaker note at `:1016` is rewritten to present
tense. No new slides, no spine reflow, no guidepost renumbering.

---

## Assumptions made without asking

Correct any of these on read; they are not interview-locked.

1. Local clone at `/Users/stephenkerr/skills`, matching the other repos at `~`.
   **Collision found and resolved, 2026-07-27.** That path was already taken by a clone of
   `mattpocock/skills`, which is also the upstream of three of the five Skills here. Stephen's call:
   the upstream clone was renamed to `~/Matt_Skills` (remote and history untouched), freeing `~/skills`
   for this repo. R4's name `Kerrator/skills` therefore stands, and the local path now matches it.
2. The GitHub repo is created **public only once the content is final**, so nothing half-written is
   world-readable. Local `git init` and commits happen first.
3. The README index says these are five Skills from a larger shelf. This is what covers the
   `review-analysis-claims` gap: the talk twice offers a claims-review Skill as its "not only
   coding" example (`index.html:761` and the `:843` notes), and that Skill is not shipping. No slide
   change is proposed for it.
4. The QR encodes `https://github.com/Kerrator/skills`, generated offline with the already-installed
   `qrencode -t SVG`. No new dependency, no CDN, invariant intact.
5. `diagnosing-bugs` keeps `scripts/hitl-loop.template.sh`; it is self-contained and referenced only
   from within its own folder.

---

## Phase 0 — Correct the private handoff Skill (`ai-workflow-engineering`)

Prerequisite for Phase 1, per R10.

| File | Change |
|---|---|
| `skills/method/handoff/SKILL.md:31` | Drop "barreling at one continuous problem (that's compaction)" as a *recommended* alternative; restate as the case where a handoff is unnecessary, without endorsing automatic compaction for durable work. |
| `skills/method/handoff/SKILL.md:86` | Same for the failure-mode line "reach for compaction". |
| `skills/method/handoff/SKILL.md:3` | Check the description's "instead of compacting" framing still reads correctly after the edits. |
| `evals/method/handoff/eval.md` | Read it. If the expected behaviour asserts the old stance, update it in the same commit. |

Verify: the file no longer recommends automatic compaction as the path for continuous work, and says
nothing durable should depend on it.

## Phase 1 — Build `/Users/stephenkerr/skills` locally

| File | Notes |
|---|---|
| `interview-design-decisions/SKILL.md` | Rewrite. Strip vendor comment (R5). ~20 lines today, the shortest of the five. |
| `diagnosing-bugs/SKILL.md` | Rewrite. Strip vendor comment. **Phase 6 fix:** line 150 points at `agents/engineering/improve-codebase-architecture.md` via the Task tool, which will not exist publicly. Rewrite generically: keep the discipline (ask the prevention question after the fix is in, hand off architectural answers with specifics) and name no file. |
| `diagnosing-bugs/scripts/hitl-loop.template.sh` | Carry over, check for local paths. |
| `handoff/SKILL.md` | Rewrite from the Phase 0 corrected original. |
| `handoff/references/handoff-template.md` | Carry over as rewrite. |
| `handoff/references/round-trip-diy-subagent.md` | Carry over as rewrite. |
| `writing-great-skills/SKILL.md` | Rewrite. |
| `writing-great-skills/GLOSSARY.md` | Carry over as rewrite; `SKILL.md` bolds terms defined here, so the pair must stay consistent. |
| `refine-instruction-surface/SKILL.md` | Rewrite. |
| `refine-instruction-surface/references/failure-modes.md` | Carry over as rewrite. |
| `refine-instruction-surface/references/tier-table.md` | Carry over; mentions `~/.claude/CLAUDE.md`, which is a generic path and fine. |
| `README.md` | Minimal index per R8: opening line, five-Skill table, short "how these were designed", install instructions, dated snapshot line per R9, licence pointer. Notes these are five from a larger shelf (assumption 3). |
| `LICENSE` | MIT, copyright Stephen Kerr 2026. |
| `CREDITS.md` | Names `interview-design-decisions` and `diagnosing-bugs` as adaptations of `mattpocock/skills`, MIT copyright 2026 Matt Pocock, with the upstream MIT text. |
| `.gitignore` | Minimal (`.DS_Store`). |

Then `git init`, one commit.

Verify before publishing: five valid `SKILL.md` frontmatter blocks (`name`, `description`, and
`disable-model-invocation` where it applies); zero vendor comment blocks; zero references to files
outside each Skill's own folder; no `/Users/`, no institution, project, or colleague names; `LICENSE`
and `CREDITS.md` present.

## Phase 2 — Publish (needs an explicit go-ahead)

`gh repo create Kerrator/skills --public --source . --push`. Outward-facing and effectively
irreversible once indexed, so this waits on a clear yes even though the plan is approved.

## Phase 3 — Deck edit (this worktree, branch `claude/skills-portfolio-repo-15cf08`)

| File | Change |
|---|---|
| `assets/qr-skills.svg` | `qrencode -t SVG -o assets/qr-skills.svg "https://github.com/Kerrator/skills"`. Offline, no new dependency. |
| `index.html` (~998-1022) | Add the URL line and the QR to "One shelf, under version control". Rewrite the `:1016` speaker note from "currently lives in a private repo; I am moving it" to present tense with the address spoken aloud. |
| `css/custom.css` | Add a `.qr` rule with a fixed-px cap, matching the px figure caps already used for iPad delivery. |

Watch: that slide already carries an `h3`, three bullets and a `.take` line. Adding a QR plus a URL
line is the overflow risk in this whole plan. Likely layout is the QR inline beside the take line at
roughly 160-180px rather than stacked below it.

Verify: overflow audit at 960x700 across all 49 leaves, not just the edited one; QR renders with
Wi-Fi off; no CDN or remote URL introduced; guidepost bar unchanged.

## Phase 4 — Artifacts and merge

Regenerate `2026-coding-with-ai-v2.pdf` (landscape, via the stdlib-only CDP client used last time)
and `2026-coding-with-ai-v2.pptx`. Commit, merge `claude/skills-portfolio-repo-15cf08` to `main`,
push. GitHub Pages serves from `presentations`.

## Phase 5 — Sync the WinterAtomics mirror

`WinterAtomics` (`www.winteratomics.ca`) carries a second copy of the deck at
`talks/2026-coding-with-ai-v2/`. Copy the edited `index.html`, `css/custom.css`,
`assets/qr-skills.svg`, and both rebuilt artifacts. Commit and push.

## Phase 6 — Pointer note in `ai-workflow-engineering`

One short note (a `docs/` entry, or an addition to `docs/sharing-with-group.md`) recording that five
Skills have hand-written public counterparts at `github.com/Kerrator/skills`, that the public copies
are rewrites rather than exports, and the snapshot date. This is R9's discoverability half.

---

## Done criteria

1. `github.com/Kerrator/skills` is public, has five Skills at root, a README, `LICENSE`, and
   `CREDITS.md` naming the MIT upstream.
2. No Skill file references anything outside its own folder, and none carries provenance metadata.
3. The private `handoff` Skill and its public counterpart state the same, corrected stance on
   compaction.
4. The deck's shelf slide shows the address and a locally generated QR; the private-repo speaker note
   is gone.
5. Zero slides overflow 960x700; the deck renders with Wi-Fi off.
6. PDF and PPTX rebuilt in both `presentations` and `WinterAtomics`, and both pushed.
7. FOUNDATION.md carries decision 122 for the slide change.

## Open items this plan does not cover

- `review-analysis-claims` stays private, so the talk's non-coding example is not in the repo
  (assumption 3).
- FOUNDATION decision 120's other half, whether `handoff` ever gets named on a slide, is untouched.
  Phase 0 fixes the file, not that decision.
