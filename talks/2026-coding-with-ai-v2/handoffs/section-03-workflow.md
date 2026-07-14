# Section 3 brief — How I code with an agent (~7 min)

Read `CONTRACT.md` first. Your block in `index.html` runs from the banner
`<!-- ============ 3 · HOW I CODE WITH AN AGENT ============ -->` to the section-4 banner.
This is the longest and most load-bearing section.

## Job of this section

Walk Stephen's actual workflow: design interview → FOUNDATION.md as a durable context start →
process scaled to the work (iterative loop vs to-spec → vertical slices → bounded loops) →
reproduce-before-fix → handoff as compaction with intention → inner loop and outer validation gate.

## Current draft slides

- **h6** "Expose the decisions" — interview bullets + gold "Surface the decisions the agent would
  otherwise guess." (stop condition in notes).
- **h7** "FOUNDATION.md: a context start" — distillation-not-transcript bullets + takeaway.
- **h8** "Scale the process to the work" — `assets/foundation-map.svg` (the central visual:
  interview ↔ FOUNDATION.md → two paths).
  - vertical: "Ralph: the blunt end of the loop" — bash loop code + "Autonomy is earned by the
    artifacts, not by the loop." (kept by explicit decision 79).
- **h9** "One slice, one owned decision" — `assets/coordination-ladder.svg` (FCC 12/8/7) + the
  locked specification takeaway.
- **h10** "Do not fix what you cannot reproduce" — reproducer-first bullets + gold line.
- **h11** "Handoff: compaction with intention" — locked line + diverged pyKMC bug story.
  - verticals: "Parallel work: handoffs + worktrees" (three mono route-lines);
    "What a handoff carries depends on where it is going" (4-row table, "examples, not required
    boxes").
- **h12** "An inner loop and an outer gate" — `assets/verification-ladder.svg` (four rungs, gold
  outer-gate bracket) + laptop-constraints takeaway.
  - vertical: "Vocabulary: the workflow" (6 terms).

## Binding foundation decisions (see FOUNDATION.md)

- Decisions 15, 17, 21, 22, 23, 24: interview exposes choices, Stephen locks them; explicit stop
  condition; FOUNDATION.md is the central visible artifact; process scales with the cost of getting
  lost; the synthesis Skill is called `to-spec` and its output an implementation specification (or
  study/method specification).
- Decisions 25, 62–68: vertical slices are independently verifiable capabilities; the
  coordination-number story is retrospective (never imply to-spec produced it); threshold 8 is
  Stephen's FCC(100) decision (12 bulk / 8 surface / 7 beside vacancy); stop the live story at the
  governing takeaway; PR 91 slice with PR 90 as the orthogonal companion; slab numbers only with
  the not-public caveat.
- Decisions 26, 27: red-capable reproducer before any fix; four-stage verification ladder;
  regression-vs-validation terminology guard.
- Decisions 28–33: handoff is compaction with intention (locked two-clause line); lead with the
  diverged pyKMC story (9dba577 branch fix; d493f8a native fix; 817524e regression; PR 86 merged;
  the handoff itself is Stephen's account); no authoritative handoff checklist, examples only;
  worktrees are an optional drill-down; pair handoff+worktree for independent work.
- Decision 79 (v2): Ralph stays as the h8 vertical, framed as the limiting case the artifacts earn.
- Speaker-language sources: FOUNDATION.md "Speaker-language capture" (shared understanding,
  foundation file, proportional workflow, specification, vertical slice, reproducer-first, layered
  verification, foundation-versus-handoff, handoff-and-worktree, versatile handoff).

## Known open questions to interview Stephen on

- Is seven core slides the right weight, or does he want to merge (e.g. h6+h7) or split anything?
- The central map (h8): does the two-branch topology match how he explains it aloud? Anything he
  would add or remove from the figure?
- Does he want the pyKMC handoff story told with more mechanics visible (the actual courier
  contents) or kept at the current three bullets?
- Ralph: does the bash snippet strike the right tone (honest, non-doctrinal), and is `claude -p`
  the invocation he wants shown?
- The deck itself was built with this workflow; does he want that made explicit on a slide (it is
  currently only in the h7 notes)?
