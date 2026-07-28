# Coding with AI — talk foundation

**Status:** ready for deck drafting  
**Last updated:** 2026-07-13  
**Talk length:** 20–30 minutes

> **Superseding copy.** Forked from `talks/2026-coding-with-ai/FOUNDATION.md` on 2026-07-13. This is
> the living decision record for the v2 deck in this folder; the original stays frozen with the
> first (Codex-built) draft. Update only this copy. The v2 scope decisions from the 2026-07-13
> design interview are recorded in the final section of this file.

This is the durable decision record for the new talk. Update it as each decision lands; do not wait
until the end of the interview. The presentation repository is public, so this file records only
material that is safe to publish. Private configuration, machine details, and unpublished project
information stay in their access-controlled sources.

## Authoritative deck-drafting brief

The design interview is sufficiently complete to draft the talk without inventing Stephen's
load-bearing decisions. Use the detailed record below as evidence and speaker-note source; use this
brief as the starting context for the first deck.

Target a roughly **24–25-minute core with about 19 leaf slides**:

1. **From chat to agentic coding — 3.5 minutes.** Car-wash hidden-purpose hook, then Stephen's
   practical definition: an LLM working inside the codebase and finding relevant files for itself,
   whether the interface is a CLI or an app.
2. **Tokens and context — 4 minutes.** Stephen's node/object representation, strawberry as a
   representation-changing anecdote, then adaptable versus rigid context and “capacity, not a
   target.”
3. **How I code with an agent — 7 minutes.** Design interview → `FOUNDATION.md`; proportional path
   through `to-spec`, vertical slices, and handoff; reproduce a bug before fixing it; verify with an
   inner loop and an outer scientific gate.
4. **Skills as maintained assets — 4 minutes.** A repeated discipline worth preserving; contrast the
   relevant debugging Skill with the trusted but irrelevant textbook/read-aloud Skill; show curation
   and scoped exposure; close with the wild-west/adaptability message. Mention
   `review-analysis-claims` briefly as a non-coding reasoning example.
5. **Ownership and validation — 5.5 minutes.** MECH 479 “outer space” → dipole comparison reversal →
   pyKMC HTST units error; land on staying inside the epistemic loop and delegating labour rather
   than scientific judgement.

Keep product-mode taxonomy, full tokenizer details, worktrees, the invocation matrix, formal Skill
evaluation, multi-machine synchronization, specialist agents, the full HTST equation, and detailed
repository evidence in vertical drill-downs or speaker notes. The first rendered draft—not more
abstract interrogation—should expose any remaining choices.

## Purpose and north star

Introduce materials-science and engineering group members to agentic coding through Stephen's
actual Claude-centred practice. The audience should understand what agentic coding is, how context
shapes an LLM's work, how reusable Skills support a coding workflow, and why the researcher retains
ownership of meaning and validation.

The talk explains a practice; it does not require the audience to complete an exercise during or
immediately after the session.

## Audience and format

- Materials-science and engineering research-group members.
- Medium Python experience.
- Some general LLM experience.
- New to agentic coding.
- Claude-centred because Claude has recently been rolled out to the group; portable concepts should
  be identified where useful.
- Target delivery: 20–30 minutes.

## Priority of ideas

1. Managing an agentic coding workflow.
2. Managing context within that workflow.
3. Retaining human ownership of the work and its scientific meaning.

## Working glossary

### Agentic coding

Stephen's practical definition is an LLM working inside a codebase, able to discover relevant files
and relationships for itself rather than being limited to the fragments a user uploads to a web
chat. The interface may be a CLI or an app. Access remains bounded by the surrounding system and its
permissions.

Inspect → act → observe → adapt is a common supporting behaviour once the agent is working in that
environment; it is not the talk's definitional test.

### Token ID

The fixed integer identifier produced by tokenization. The token ID itself is not repeatedly changed
by the transformer.

### Initial token representation

The vector representation created for a token at a sequence position before contextual processing.

### Contextual representation

The hidden representation carried at a sequence position after transformer layers have mixed in
information from other permitted token positions. Two occurrences of the same token ID can therefore
develop different contextual representations.

### Context window

The model's finite working set for the current generation. The practical goal is not to fill it, but
to select the current information that should shape the next answer.

### Skill

A packaged reusable procedure or prompt with an invocation mechanism. In this talk, “Skill” refers
to the Claude/agentic-coding mechanism, not a general human competency, unless explicitly qualified.

### Trigger surface

The set of installed descriptions, rules, hooks, and integrations that can cause agent behaviour to
activate. A larger collection is not free: broad or overlapping triggers can consume context,
conflict, invoke unnecessary procedures, or generate avoidable tool activity. Manual-only Skills
have a different cost from automatically triggered Skills; do not imply that every installed Skill
fires in every session.

### Invocation mode

Whether a Skill runs only when the user deliberately invokes it or may be selected automatically by
the agent from its description. This is separate from where the Skill is installed.

### Installation scope

Where a Skill is available: for one project or across the user's projects and machines. In Stephen's
workflow, “global” names this availability scope; it does not necessarily mean automatically invoked,
shared with the whole research group, or active in every turn.

### Design foundation

A durable Markdown distillation of the shared understanding reached during a design interview: the
goal, terminology, consequential decisions and their reasons, assumptions, invariants, bounded scope,
evidence requirements, definition of done, and unresolved questions. It is not a saved copy of the
entire context window. It is a deliberately curated **context start** that a future session can load.

### Vertical slice

A narrow but complete capability that crosses every relevant integration layer and produces an
observable result that can be verified independently. A file, module, or technical layer by itself
is a horizontal task, not a vertical slice.

### Red-capable reproducer

One named, agent-runnable command that exercises the actual bug path and can fail on the exact
reported symptom before the fix, then pass after it. It may be a test, CLI invocation, replay,
differential comparison, or other executable feedback loop—not necessarily a unit test.

### Inner loop / outer validation gate

The **inner loop** is the smallest practical, repeatable check used while changing code—usually a
fixture or reduced system that runs locally. An **outer validation gate** re-runs a representative
example, the original failing system, or the intended cluster environment before the work is accepted.

### Intentional compaction

An explicit, inspectable selection of what another context needs for a chosen direction of work. It
may draw from goals, decisions, evidence, pointers, current state, or next steps; the useful contents
vary with the direction. Unlike automatic compaction, the human deliberately chooses what survives.
It may continue the same task in a fresh chat or dispatch a separate bounded task.

### Worktree

An isolated checkout with its own branch and working-tree state. A worktree separates code state;
it does not by itself provide a clean conversational context or a useful task brief. Pair it with a
handoff when independent work needs both kinds of isolation.

## Accepted decisions

1. **Build a new talk from scratch.** The existing *Coding with Claude Code* deck is source material,
   not the structure to trim in place.
2. **Use the title _Coding with AI_.** Claude is the primary implementation discussed, while the
   central ideas should remain intelligible as agentic-coding concepts.
3. **Keep the live spine short.** Aim for roughly five horizontal sections and a 20–30-minute core;
   optional detail can live in vertical drill-downs.
4. **No mandatory immediate exercise.** A small-repository starter exercise is a useful future-course
   idea, not a required outcome of this talk.
5. **Use an operational agentic-coding definition.** This early loop-based wording is superseded by
   decision 74: the live definition is an LLM working inside the codebase and discovering relevant
   context for itself. Inspect → act → observe → adapt remains a useful description of behaviour,
   not the boundary the audience must accept.
6. **Teach token IDs and contextual representations separately.** A token ID is fixed; the hidden
   representation at its sequence position changes through the transformer layers as context is
   incorporated.
7. **Make contextual representation the primary token takeaway.** The context window is not merely
   storage: its contents help shape the contextual representation at each position and the next-token
   prediction.
8. **Keep tokenization mismatch as a secondary idea.** “Strawberry” and “pencil/pencils” illustrate
   tokenization and character/subword reasoning. They do not, by themselves, demonstrate contextual
   representation.
9. **Preserve Stephen's personal metaphors in speaker notes.** Use **node** when emphasizing a
   token-position's relationships inside a network. Use **object** when making token chunks concrete,
   especially in the strawberry and pencil/pencils examples. These are teaching metaphors, not literal
   technical definitions.
10. **Separate public and private workflow layers.** The deck may explain the principles of creating,
    evaluating, promoting, and synchronizing Skills, but it must not expose private machine layouts,
    personal paths, credentials, unpublished project state, or other private configuration.
11. **Lead the context-window topic with selection, not capacity.** More available space is useful,
    but the working objective is the current, task-relevant context—not the largest possible prompt.
    Use **adaptable/rigid** as the memorable binary contrast. An adaptable chat is focused and easy
    to steer as evidence changes; a rigid chat is crowded with abandoned ideas, stale assumptions,
    irrelevant tool output, and old directions until it becomes set in its ways. The visible advice
    is **“Keep context small and relevant.”**
12. **Use strawberry as a problem-representation anecdote, not a claim of inability.** If direct
    letter counting is unreliable, first ask the model to spell the word one character at a time,
    then count the explicit characters. The general lesson is to change the representation, expose
    intermediate state, or provide a suitable tool instead of merely repeating a failing question.
13. **Keep pencil/pencils in the speaker notes only.** It is a tokenizer-dependent illustration
    that a small textual addition can produce a large semantic change. It does not need its own
    slide and must not be presented as a guaranteed token split.
14. **Use the car-wash anecdote to expose hidden intent.** It illustrates how a fluent answer can
    optimize the surface wording while dropping the purpose that made the question meaningful. Its
    coding bridge is an underspecified implementation request: the agent may produce plausible code
    while silently inventing the missing design constraints. Present this as a possible or recorded
    failure, not a guaranteed response from every current model.
15. **Use the design interview to preserve human ownership of decisions.** The agent should expose
    the choices it would otherwise make implicitly, recommend an option, and interrogate Stephen one
    decision at a time. A decision becomes part of the design only when Stephen explicitly locks it
    in. The goal is shared understanding before implementation, not simply a longer prompt.
16. **Ground workflow ideas in public pyKMC evidence wherever possible.** Prefer a link to a concrete
    implementation, invariant, regression test, issue, pull request, or commit over an abstract claim.
    Verify each link and its public-safety before adding it to this world-readable talk.
17. **Use an explicit stop condition for shared understanding.** Implementation begins only when the
    goal, consequential decisions, assumptions, evidence requirements, bounded scope, and definition
    of done are explicit; Stephen can explain the agent's proposed path and trade-offs; the agent can
    restate Stephen's intent; and every load-bearing decision is visibly one Stephen made.
18. **Persist the interview's distillation as a Markdown foundation.** The scoping work should not
    remain trapped in one transient conversation or depend on automatic compaction. Save and, when
    appropriate, version the agreed north star so a new session can load a concise authoritative
    starting context. The file must remain current and must respect the project's public/private
    boundary.
19. **Treat design interviewing as a reusable reasoning pattern, not only a coding front end.** The
    same one-question-at-a-time procedure can be adapted into a teaching Skill that interrogates a
    learner's understanding and does not move on merely because the learner can repeat fluent words.
20. **Gate progress in the teaching adaptation on demonstrated understanding.** Before moving on, the
    learner must explain the idea in their own words, apply it to an unfamiliar example, identify its
    assumptions or failure conditions, and correct a plausible misconception. Repeating the model's
    wording is insufficient.
21. **Make `FOUNDATION.md` the central visible workflow artifact.** It should not be hidden in speaker
    notes as an implementation detail. Use it to connect the design interview, explicit human-owned
    decisions, durable context, fresh sessions, planning, and iterative implementation in one visual.
22. **Scale the workflow to the size of the work.** For a small, bounded change, proceed from the
    foundation directly into an iterative agent loop. For larger, multi-step work, synthesize a
    specification, divide it into independently verifiable vertical slices, and run one bounded
    implementation loop per slice. The additional artifacts are proportional control, not mandatory
    ceremony for every change.
23. **Call the post-foundation artifact an implementation specification in the talk.** Its role is
    to translate human-owned decisions from `FOUNDATION.md` into an explicit, testable end state for
    execution without reopening the design interview. Use **study/method specification** when the
    deliverable is a simulation campaign rather than a code change.
24. **Rename the underlying `to-prd` Skill to `to-spec`.** “PRD” carries product vocabulary that no
    longer matches Stephen's intended general use; `to-spec` is the locked concise name for this
    synthesis step. Describe the generated artifact precisely as an implementation specification or
    study/method specification according to the work. Preserve `to-prd` temporarily as a compatibility
    alias if the private library is later migrated; this talk decision does not itself authorize that
    repository change.
25. **Define vertical slices by independently verifiable capability.** Do not divide a feature into
    files or technical layers. Divide it into narrow, end-to-end paths that each produce observable
    evidence and can occupy one bounded agent loop. Candidate MSE examples include adding one data-
    analysis model and adding coordination-number support to the event-search path.
26. **Do not ask an agent to “fix” a bug before it can reproduce it.** First build and run a
    red-capable reproducer for the user's exact symptom, minimise it, and promote it to a regression
    test at the correct seam when one exists. Only then implement the smallest fix, observe red →
    green, and re-run the original scenario. The agent should not form a confident theory before it
    has executable evidence.
27. **Use a four-stage verification ladder for scientific software.** Run a tight local reproducer on
    every iteration; run a representative reduced integration case before handoff or commit; rerun the
    original failing system or a canonical example at the phase boundary; and validate on the cluster
    whenever MPI scale, hardware, scheduler, memory, or environment can change the result. Do not
    mistake a local-machine limitation for a production scientific constraint.
28. **Describe handoff broadly as compaction with intention.** A handoff is not limited to moving a
    different task. When a useful conversation has become too large or carries stale reasoning, use
    a curated handoff to continue the same work in a cleared or new context. Preserve what is
    relevant to continuing—goal, decisions, evidence, pointers, current state, and next step—rather
    than either copying the whole transcript or surrendering that choice to automatic compaction.
29. **Pair handoffs with worktrees for independent coding tasks.** The handoff isolates and scopes
    the receiving context; the worktree isolates its branch and filesystem state. Use both when work
    can proceed independently. A new chat without a worktree may still edit the same code state, and
    a worktree without a handoff may still begin with an ambiguous or polluted brief.
30. **Keep worktrees as an optional handoff drill-down.** Handoff remains on the core path because it
    teaches intentional context control. Worktrees are useful but non-critical detail for this
    20–30-minute introduction. Briefly allude to the extension: derive several independent one-task
    handoffs from a larger specification, execute them in separate worktrees, then integrate, merge,
    and validate the results. Do not imply that isolation makes later integration automatic.
31. **Make intentional compaction and bounded scope one joint handoff takeaway.** Neither half is an
    optional qualification. A handoff deliberately selects what survives into the next context, and
    that selected context is shaped around one bounded direction of work. The locked concise
    slide language is: **“Handoff is compaction with intention: one bounded task, only the context
    needed to complete it.”** “One bounded task” expresses the direction and scope of the transfer;
    it does not impose a universal document schema.
32. **Do not turn handoff into an authoritative checklist.** Handoffs are deliberately versatile.
    Their contents depend on whether the receiving context is continuing work, breaking in a new
    direction, executing one specification slice, investigating a defect, or operating in a separate
    worktree. Show possible ingredients through examples, not a mandatory minimum contract. The
    stable criterion is that the receiver gets the context relevant to its direction without being
    burdened by the whole parent conversation or idea.
33. **Lead handoff with the diverged pyKMC bug story.** This is the primary concrete example because
    it shows a fresh context carrying the problem, evidence, and useful insight into a different code
    shape without carrying an obsolete implementation path. Mention same-chat continuation briefly
    as a second use of intentional compaction. Public repository history can verify the two native
    fixes, regression, and merge; the disposable handoff connecting them remains Stephen's account
    and must be labelled accordingly.
34. **Keep `review-analysis-claims` specific to paper writing.** It is a custom adversarial review of
    statistical claims and interpretation before prose is drafted. Its purpose is to make the author
    confront what the analysis actually licenses so the final interpretation is accurate, bounded,
    and clear. Do not broaden it into a generic code, methods, or units-review Skill. It is evidence
    that a Skill can encode a repeatable way of thinking, not merely store a canned prompt.
35. **Stop the claim review at shared interpretive ownership.** The Skill has done its job when, for
    each result, Stephen can explain how it was produced, its key assumptions and uncertainty, what
    it means in substantive terms, and the strongest claim the evidence supports. Only then should
    prose drafting begin.
36. **Give `review-analysis-claims` brief live visibility and optional depth.** Mention it on the main
    Skills slide as an example of a reusable reasoning discipline beyond coding. Put its full
    statistical tree and paper-writing example in a vertical drill-down so the 20–30-minute core
    remains centred on agentic coding.
37. **Make `review-workflow-candidate` a security and trigger-surface gate.** Its importance is not
    limited to separating good ideas from hype. Third-party Skills are instructions entering the
    agent's trust boundary and may also ship scripts, hooks, network access, or credential-sensitive
    behaviour; inspect them for prompt-injection-like instructions and executable risk before
    enabling them. Indiscriminately installing a large Skill pack can also create broad, overlapping
    triggers that inflate context and tool activity. Teach deliberate adoption, least footprint, and
    sandboxed inspection—not “download every useful-looking Skill.”
38. **Lock the Skill-intake headline.** Use **“Installing a Skill expands what the agent may trust,
    trigger, and run.”** Support it with **“Inspect before you adopt; keep the active set small.”**
    This deliberately joins prompt-injection/executable risk with the context and tool-activity cost
    of an oversized trigger surface.
39. **Use Skill intake to introduce a two-axis deployment choice.** Do not present “user-invoked” and
    “global” as opposites. Invocation mode is deliberate user invocation versus automatic selection;
    installation scope is project-local versus globally available to Stephen across projects and
    machines. A Skill can occupy any combination. This distinction explains why broad automatic
    Skills consume more contextual attention while a deliberate command can be widely available with
    little always-on trigger cost.
40. **Treat trust as a prerequisite, not a global-scope threshold.** An untrusted Skill should not be
    installed at any scope. After security and provenance clear that gate, the real placement question
    is contextual relevance: should this kind of chat know the Skill exists, and is its likely value
    worth the context and trigger surface it adds?
41. **Use the eager-intern and Neuralyzer analogy for chat context.** Stephen pictures one chat as a
    very eager intern who wants to help and lasts for only that chat. Showing the intern many tools or
    Skills invites attention and possible action across all of them, so expose only what is relevant
    to today's work. Starting a new chat is like a *Men in Black* Neuralyzer flash: the previous
    conversational path is gone unless useful state was carried into durable artifacts or a handoff.
    Preserve this as Stephen's personal speaking metaphor, not a literal claim about deterministic
    tool use or total system amnesia.
42. **Let repeated prompts become context-specific Skills.** A prompt that Stephen has refined and
    expects to reuse can become a Skill, but that does not make it relevant everywhere. Use the
    textbook read-aloud example: preserving the spoken text, omitting figures, and expanding acronyms
    may be valuable in a study workflow yet distracting in a coding repository. Surface Skills where
    the corresponding prompt is repeatedly useful.
43. **Use bug diagnosis as the positive coding contrast.** A coding project benefits from knowing the
    debugging discipline relevant to recurring bug work: do not rush to repair; first create and run
    a failure case that reproduces the exact symptom. The Skill turns that repeated prompt into a
    reusable procedure. Keep the distinction between making the procedure available and actually
    invoking it for a particular bug.
44. **Park the `diagnosing-bugs` invocation mismatch.** The current Skill is manual-only, while
    Stephen's conceptual example describes a coding chat that knows the discipline and applies it
    only when a real bug appears. This implementation detail does not need resolution in the talk.
    Preserve it as a private maintenance follow-up and avoid claiming that the current Skill
    automatically invokes.
45. **Use contextual Skill selection as the audience-facing example.** Contrast two trusted, useful
    Skills: textbook read-aloud support is valuable but irrelevant to a coding chat; reproducible-
    failure-first bug discipline is relevant to a coding repository. The lesson is not “good Skill
    versus bad Skill,” but “context this intern should see versus context it should not see today.”
46. **Require a stable reusable shape before a prompt becomes a Skill.** Repeated usefulness is
    necessary but not sufficient. The need must recur, the trigger must be recognizable, the
    procedure must be reusable, and success or failure must be observable. This keeps one-off advice
    and vague preferences from expanding the Skill surface merely because they have been written as
    prompts more than once.
47. **Do not prescribe formal A/B testing to this audience.** Stephen's managed library may use
    baselines, fixtures, rubrics, and regression checks, but graduate researchers do not need to build
    an evaluation laboratory before using a local Skill. Teach proportional observation: notice what
    behaviour changes, whether the workflow becomes more consistent, and whether the Skill creates
    new friction; revise, narrow, or remove it accordingly.
48. **Name agentic-coding practice as unsettled.** “Wild west” is Stephen's framing: teams and even
    departments inside large organizations use different Skill sets, project instructions, and
    Claude-file conventions, and those arrangements can produce different results. Present this as
    an observed and personally reported lack of consensus, not as a verified claim about any named
    company's official practice.
49. **Teach a way of thinking, not a canonical setup.** The exact Skill format, model behaviour,
    configuration layout, and preferred workflow will change. The durable value is learning to choose
    context deliberately, expose only relevant capabilities, preserve useful decisions, demand
    evidence, and retain ownership. These principles should help the audience adapt to the next
    generation of tools rather than freeze Stephen's 2026 configuration as doctrine.
50. **Make adaptability the payoff of Skill curation.** Stephen's system is one current working
    example, not the end state of agentic coding. The audience should borrow the questions used to
    build and prune it, then evolve their own setup as their projects and the tools change.
51. **Close the Skills section with the wild-west message.** Show Stephen's concrete Skill examples
    and curation choices first, then make the lack of settled practice explicit. End the section with
    **“Do not copy my configuration. Copy the habit of deciding what belongs in context—and change it
    as the tools change.”** Use that sentence to transition into the final ownership section.
52. **Keep multi-machine Skill management non-critical.** Briefly mention that Stephen versions his
    maintained Skills in a source of truth and selectively exposes the relevant subset across his
    computers, projects, chats, and worktrees. The purpose is to show how he personally keeps the
    practice coherent, not to teach paths, symlinks, manifests, hooks, or a prescribed deployment
    architecture. Put operational mechanics in notes or an optional drill-down.
53. **Keep `curate-rate-catalogue` as optional specialist context.** Do not introduce the
    Skill-versus-subagent distinction on the core spine. In speaker notes or a vertical drill-down,
    accurately describe `curate-rate-catalogue` as a manually dispatched, domain-specific pylatkmc
    agent with no always-on trigger surface. Its teaching job is to show that some valuable reusable
    context should be loaded only for specialist work rather than shown to every coding chat.
54. **Use “Stay inside the epistemic loop” as the visible ownership heading.** Preserve “outer
    space” as Stephen's spoken metaphor for the point where enough intermediate judgement has been
    delegated that the human can no longer audit, explain, or defend the result. This keeps the slide
    legible for a graduate audience while retaining Stephen's personal language.
55. **Ground “outer space” in Stephen's MECH 479 nanomaterials teaching.** The story should come from
    his interactions with students in that course, not be attributed to MECH 203 or presented as an
    abstract composite without explanation. Keep students unidentifiable and focus on loss of
    evaluative ownership rather than alleging misconduct.
56. **Tell the MECH 479 story as a progression across course offerings.** In an earlier year, Stephen
    used AI as bounded help: orient a student who had not found an entry into a paper, or critique and
    polish writing the student had already produced, while warning that clearer prose can distort the
    science. In the more recent offering, improved AI made it easy for some students to delegate the
    whole chain—finding papers, processing them, and producing a rubric-shaped report—so quickly that
    they could not answer substantive questions about the sources or judge which parts were correct.
    That accumulated loss of design decisions is the observed meaning of “outer space.”
57. **Make course redesign a consequence, not a complaint.** The lesson is not that students were
    dishonest or that AI use itself was wrong. The assignment no longer guaranteed that a polished
    deliverable reflected student understanding, so Stephen needs to rethink the checkpoints and
    evidence of ownership built into the course. Bridge this directly to coding: a finished program
    is not evidence that the researcher understands or owns the chain of decisions that produced it.
58. **Keep the dipole-edit anecdote at the verified level of detail.** The AI improved the paragraph's
    structure but reversed a scientific comparison—effectively changing a greater-than relationship
    into a less-than relationship—so the sentence became incorrect. Stephen repaired the comparison
    while retaining the useful structural revision. Do not invent the quantities or reproduce a
    before/after sentence unless the original text is recovered.
59. **Build the ownership climax in three escalating steps.** First, the MECH 479 story shows a
    polished artifact without understanding. Second, the dipole paragraph shows that greater fluency
    can reverse one scientific relationship. Third, the pyKMC HTST units case shows working code and
    green tests agreeing on a result that is wrong by `10^12`. This escalation makes the units case
    the primary coding demonstration of why the researcher must stay inside the epistemic loop.
60. **Keep the live HTST physics compact.** Use **“Green tests can agree on the wrong physics”** as
    the visible headline and show the single conversion `5 × 10^12 Hz = 5 ps^-1`. Explain that the
    unconverted value was consumed as `5 × 10^12 ps^-1`, making finite HTST/RPA rates `10^12` too
    large and simulated time `10^12` too short. Put the full Vineyard expression and implementation
    details in a vertical drill-down.
61. **Make the human catch an external scientific sanity check, and keep the reference generic.**
    Stephen first distrusted the HTST output because it disagreed with a known or expected reference
    value. Investigating that discrepancy exposed the Hz-versus-`ps^-1` boundary error. Do not imply
    that a unit test or the AI independently found the problem. Stephen has deliberately chosen not
    to identify the exact comparison value or source in this talk.
62. **Use pyKMC's coordination-number feature as a real, retrospective workflow example.** The
    feature was implemented in pyKMC before Stephen had the `to-spec` Skill. Present the finished
    feature as a concrete case that can be mapped onto the workflow he would use now: design
    interview → durable foundation → `to-spec` → vertical slices → bounded implementation and
    scientific validation. Never imply that `to-spec` produced the historical implementation.
63. **Ground the coordination-number feature in its surface-science purpose and actual mechanism.**
    Stephen wanted event work on a surface system to focus on the surface environments that mattered,
    rather than treating the rest of the bulk-like system as equally relevant. Coordination number
    controlled which atomic environments were classified as noncrystalline and therefore eligible
    for new event searches; it did not change the event-search algorithm or the event-storage key.
64. **Use threshold 8 as a system-specific selection example, not a universal surface law.** The
    implementation classifies atoms with at least the configured number of neighbours as `crystal`;
    with `coordination_threshold = 8`, atoms with fewer than eight neighbours are `noncrystal`. In
    Stephen's surface case, that restricted event finding to environments near surface defects.
65. **Make the threshold a visible scientific decision owned by the researcher.** Eight was selected
    from Stephen's understanding of the physical system, not derived by the coding agent or by a
    software concern. The agent's job is to surface the choice, make it configurable, wire it through
    the complete feature, and help test the behaviour. Stephen's job is to decide and defend what
    coordination distinguishes the scientifically relevant environments.
66. **Explain the scientific threshold as an FCC(100) coordination ladder.** An FCC bulk atom has 12
    nearest neighbours; an ordinary atom on an FCC(100) surface has eight; an atom adjacent to a
    surface vacancy has seven. With `coordination_threshold = 8`, the ordinary surface remains
    `crystal` while the vacancy-adjacent environments fall below the threshold and receive new event
    searches. Do not generalize “surface coordination is eight” to every FCC facet.
67. **Lock the coordination-number example's governing takeaway.** **“A specification does not make
    the scientific decision. It preserves that decision and turns it into explicit, testable software
    behaviour.”** Use the FCC(100) threshold to show the distinction: Stephen supplies and defends the
    `12 → 8 → 7` physical reasoning; the agent helps encode, propagate, and verify it.
68. **Stop the live coordination-number story at the governing takeaway.** The exact acceptance-test
    ladder and real-slab comparison are useful evidence for speaker notes or Q&A, but are not critical
    to the 20–30-minute path. Do not let this example become a detailed pyKMC case study after it has
    shown a researcher-owned decision becoming explicit, configurable, and testable.
69. **Keep a memorable binary label for context quality.** Stephen does not want the context-window
    slide reduced to neutral technical language. The chosen pair is **adaptable/rigid**: it describes
    session behaviour rather than implying that the model's underlying intelligence has changed, and
    it is Stephen's own framing rather than inherited “smart zone / dumb zone” wording.
70. **Use plain human language to sell small, relevant coding contexts.** An adaptable chat is
    focused and easy to steer as evidence changes. A rigid chat has accumulated abandoned ideas,
    stale assumptions, irrelevant tool output, and old directions until it starts to get set in its
    ways. The visible advice is **“Keep context small and relevant.”** Treat a one-million-token
    context window as available capacity, not a target to fill; qualify the number as model-dependent
    and time-sensitive.
71. **Lock Stephen's spoken one-million-token line.** **“A million-token window is capacity, not a
    target. Just because Claude can hold that much does not mean I want every abandoned idea and
    stale decision following me through one coding chat.”** Preserve the conversational tone; keep
    the model-specific qualification in the notes or source record rather than interrupting the line.
72. **Open with the car-wash hidden-goal anecdote.** Put the audience inside a simple question where
    a locally sensible answer can miss the purpose of the task, then bridge immediately to coding:
    an agent can satisfy the visible request while guessing the architecture, constraints, and
    definition of done. Strawberry belongs later in the token/context section, not in the cold open.
73. **Make hidden purpose—not model comparison—the opening's primary lesson.** Show the single
    observed **ChatGPT 5.3 Instant** failure in the live path, let the audience identify that the car
    must reach the wash, and bridge directly to underspecified coding requests. Keep the correct
    **ChatGPT 5.4 Pro** response and the unidentified safeguard-like partial response as optional
    vertical depth. Do not infer the production mechanism from an output or present one run as stable
    model behaviour.
74. **Define agentic coding by situated access and self-directed context discovery, not by the user
    interface.** In Stephen's usage, an agentic coding system works inside the codebase and can search
    for the files and relationships relevant to the task instead of receiving only the fragments a
    user uploads to a web chat. A CLI and an app can both be agentic. Say “within the access it has
    been granted” rather than implying that every agent has unrestricted access to every file.
75. **Do not turn the practical agentic-coding definition into a product taxonomy.** Use Stephen's
    operational definition in the live talk and move on. Read-only modes, product labels, and edge
    cases belong only in Q&A if someone challenges the boundary; Stephen is comfortable handling
    that discussion live.
76. **Build the deck section by section using intentional agent handoffs.** The primary agent owns the
    full narrative, shared reveal.js files, visual system, integration, and verification. Section
    agents receive curated briefs rather than the entire foundation and return isolated drafts; they
    do not edit `index.html` or `custom.css` concurrently. Sections 1–3 form the first parallel wave;
    Sections 4–5 and an independent evidence audit form the second. The detailed execution contract
    lives in `BUILD_PLAN.md`.

## Locked live spine

1. **From chat to agentic coding** — situated codebase access and self-directed context discovery.
2. **Tokens and context** — fixed IDs, contextual representations, scoped working context, and model
   failure examples.
3. **How I code with an agent** — design interview, durable foundation, bounded slices,
   iterative implementation, feedback, and verification.
4. **Skills as maintained assets** — reusable prompts, invocation, project-specific Skills, curation,
   teaching adaptations, evaluation, promotion, and synchronization.
5. **Ownership and validation** — the human supplies scientific judgement and turns discovered
   invariants into better automated checks.

Each section has an explicit governing takeaway below. Optional depth hangs vertically from this
five-section spine rather than expanding the horizontal path.

## Locked section takeaways

### 1. From chat to agentic coding

Primary contrast:

> A web chat works from the context I give it. An agentic coding system works inside the codebase
> and can find the context it needs for the task.

Locked personal speaker language:

> Agentic coding is when I have an LLM working inside my codebase. It can look through the files and
> suss out where things are instead of only seeing what I upload to a web chat. It can be in a CLI or
> in an app—the interface is not what makes it agentic.

Supporting definition:

> The agent can choose what to inspect across the repository within the access it has been given.
> That does not mean every file is placed in the context window at once; it means the agent can go
> looking for relevant context rather than waiting for me to supply every file.

The inspect → act → observe → adapt loop can describe how a coding agent works after it has found
the relevant context, but it is not a definitional test the audience must accept.

Q&A-only reference, verified 2026-07-13: product capability is a **system or mode configuration**,
not a distinct kind of base LLM. [Cursor Ask mode](https://docs.cursor.com/en/agent/modes) searches a
codebase read-only, while Cursor Agent enables edits and commands. GitHub's official
[Copilot IDE documentation](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide)
similarly separates Ask from Agent mode. Do not introduce this distinction in the live path unless
an audience question makes it useful.

### 2. Tokens and context

> A token ID is fixed, but the representation carried at that sequence position becomes contextual.

Context-window takeaway:

> The context window is the model's finite working set. The goal is not to fill it, but to select the
> current information that should shape the next answer.

Supporting bridge:

> The context window is not merely storage; its contents shape how token positions are represented
> and how the next token is predicted.

Problem-solving takeaway:

> When a model struggles, do not merely repeat the question. Change the representation, expose
> intermediate steps, or give it a suitable tool.

Hidden-intent bridge into the coding workflow:

> A fluent answer can satisfy the visible request while missing the goal behind it. Make the goal,
> constraints, assumptions, and definition of done explicit before implementation.

### 3. How I code with an agent

Design-interview takeaway:

> The first job is not to generate code. It is to expose the decisions the agent would otherwise
> guess.

Ownership principle:

> The agent may identify options and recommend one. I lock in the load-bearing decisions, so the
> resulting design remains mine and both of us work from the same understanding.

Stop condition:

> We start implementation only when I can explain the proposed path and its trade-offs, the agent can
> restate my goal and constraints, the evidence and definition of done are testable, and every
> load-bearing decision is one I knowingly made.

Durable-context takeaway:

> Do not preserve the whole conversation. Distil the agreed north star into a durable foundation file
> that a new session can load without reconstructing the design from a compacted chat.

Handoff takeaway:

> **Handoff is compaction with intention: one bounded task, only the context needed to complete it.**

The two clauses carry equal weight. “Compaction with intention” explains who controls what survives;
“one bounded task” explains what that selected context is for. This is a scoping principle, not a
fixed handoff template.

Central visual commitment:

> design interview ↔ `FOUNDATION.md` → small change: iterative implementation  
> design interview ↔ `FOUNDATION.md` → large change: specification → vertical slices → bounded loops

Context narrowing across the larger-work path:

> `FOUNDATION.md` holds the durable design → `to-spec` describes the complete agreed end state → a
> handoff intentionally compacts the exact context for one bounded task → one agent executes and
> verifies it.

Optional parallel extension:

> specification → independent one-task handoffs → separate worktrees → integrate, merge, and validate

Verified behaviour of the current `build-design-foundation` Skill:

- The interview and file are one pass: update the document when each decision lands, never as a
  write-up batched at the end.
- Re-run against an existing foundation to sharpen it; do not clobber it.
- Record purpose and north star, a canonical project glossary, load-bearing decisions and why,
  invariants and constraints, architecture and build/test seams, open branching questions, and
  explicit out-of-scope items.
- A logged design decision must be hard to reverse, surprising without context, and the result of a
  genuine trade-off; smaller operational facts belong elsewhere.
- Treat the document as a live constraint: resolve disagreement between the conversation, repository,
  and foundation as soon as it appears.

The private Skill currently named `to-prd` is a synthesis step, not another design interview: it
explores the current repository, uses the already-settled conversation and project vocabulary,
identifies test seams, produces a tracker artifact, and is expected not to reopen the interview. Its
inherited template is product-shaped (`Problem Statement`, `Solution`, extensive `User Stories`,
implementation and testing decisions). The audience-facing name is already locked as `to-spec`;
describe its output as an **implementation specification** or, for a simulation campaign, a
**study/method specification**.

The current `to-issues` Skill then proposes tracer-bullet vertical slices, checks their granularity
and dependency order with the user, and publishes only the approved breakdown. Each slice must cut
through every relevant integration layer and be independently demoable or verifiable; a layer or
file by itself is not a vertical slice.

The current `diagnosing-bugs` Skill makes the reproducer its first and load-bearing phase. Before any
hypothesis, it requires one command that has already been run and can catch the exact bug; it then
minimises the reproducer, ranks falsifiable hypotheses, instruments one prediction at a time, turns
the minimal case into a regression at the correct seam, applies the fix, and re-runs both the
regression and original scenario. A nearby failing test that demonstrates a different failure is not
acceptable evidence.

Stephen's intended `handoff` concept is **compaction with intention**: a disposable Markdown courier
that carries the selected context needed to continue the same work in a clean window or to dispatch
one independent task. Depending on that direction, it might include a goal or done condition,
authoritative pointers, pinned code state, measured evidence and its conditions, relevant constraints,
or a suggested receiving Skill. These are examples, not required fields. It should redact portable
sensitive information and be discarded after newly durable facts are promoted. For independent code
changes, it can be paired with a worktree so that conversational context and code state are both
isolated.

This is distinct from `FOUNDATION.md`: the foundation is the durable north star shared across future
work; a handoff is a temporary, deliberately selected route from the current state to one next
context. The current private `handoff` Skill says that continuous work should use automatic
compaction instead. That wording now conflicts with the broader governing definition accepted for
the talk and is flagged for later review; this talk decision does not itself authorize changing the
private Skill.

It is also narrower than `to-spec`. The specification packages the complete agreed end state and its
verification seams, potentially covering several vertical slices. A handoff packages only the
context needed for one receiving session to complete one bounded task. That task may be one slice
from the specification, a focused bug repair, or a continuation of work already in progress.

Naming audit:

- `to-foundation` would collide conceptually with `build-design-foundation`, which already creates
  and maintains `FOUNDATION.md`; it would make two distinct stages sound like the same operation.
- `to-doc` is too broad to communicate either the trigger or the output—all of these Skills produce
  or update documents.
- The current library already contains `to-paper-spec` and `to-figure-spec`. Stephen has selected the
  shorter general name `to-spec`; the invocation stays concise while the selected template and output
  make the kind of specification explicit.

### 4. Skills as maintained assets

> A Skill is not something to collect. It is a repeated prompt or procedure I deliberately preserve,
> expose only to the chats where it is relevant, observe in use, and revise or remove when it stops
> helping.

Audience-level evaluation takeaway:

> You do not need to run a formal A/B campaign for every personal Skill. Pay attention to what changes:
> does the agent follow the discipline more consistently, does the output become easier to verify,
> and what new friction or unwanted behaviour appears?

Durable section takeaway:

> Do not copy my configuration as if it were settled best practice. Copy the habit of deciding what
> belongs in context and changing the setup when the evidence or the tools change.

### 5. Ownership and validation

Visible heading:

> **Stay inside the epistemic loop.**

Speaker definition:

> I call it “outer space”: the point where I have delegated so many intermediate judgements that I
> can no longer audit, explain, or defend the result.

Operational takeaway:

> Delegate labour, not scientific judgement. I should still be able to explain the choices, trace the
> evidence, challenge the output, and say what observation would show that it is wrong.

Locked narrative escalation:

1. **MECH 479:** a polished artifact without understanding.
2. **Dipole paragraph:** clearer language reverses a scientific comparison.
3. **pyKMC HTST units:** working code and green tests preserve a `10^12` physical error.

Transition into the coding climax:

> The same failure can happen in software. The artifact can look more convincing at every step while
> I move farther away from the decisions that determine whether the science is true.

Live HTST slide commitment:

> **Green tests can agree on the wrong physics.**  
> `5 × 10^12 Hz = 5 ps^-1`

The main slide should not also carry the Vineyard equation. That equation, the primed saddle-mode
product, backend boundary, and affected/unaffected paths belong in a separate vertical drill-down.

Speaker emphasis:

> The tests did not tell me this was wrong. I compared the result with a value I already had reason
> to expect, and the discrepancy made me stop. Following that physical sanity check led us to the
> unit boundary.

> Automated checks prove the contracts they encode; an external scientific anchor can reveal that
> the encoded contract itself is wrong.

## Speaker-language capture

### Personal token representation

> I picture each token as a node carrying a vector. It begins with a general representation, but as
> it passes through the transformer layers, that representation is repeatedly reshaped by the other
> token positions it can attend to. The token ID remains fixed; the contextual state carried at that
> position changes. So context is not merely text surrounding a token—it helps give that particular
> occurrence its working meaning.

When discussing tokenization more concretely, Stephen may instead call a token an **object**: for
example, the chunks involved in “strawberry” or the possible separation of “pencil” and a plural
suffix. Qualify any exact split as tokenizer-dependent.

### Strawberry anecdote

> The point is not that the model is incapable of counting letters. A direct question may ask it to
> operate at an awkward representation level. If I first ask it to spell “strawberry” one letter at
> a time, the characters become explicit intermediate state; counting the R's is then much easier to
> perform and verify. When a model struggles with a problem, I need to think about how the task is
> represented and help it adopt a form that supports the reasoning I want.

Do not claim that “strawberry” is always one token or always produces a particular error. Exact
tokenization and behaviour depend on the tokenizer, model, prompt, and available tools.

### Pencil/pencils aside

Use this only as a brief concrete aside: a tokenizer may represent a word and a small plural suffix
separately, and that small addition changes one object into several. The exact split is not the
lesson and must be checked before showing token IDs; the lesson is that the model's textual units do
not map cleanly onto either individual characters or complete words.

### Adaptable-versus-rigid context language

Locked visible contrast:

> **Adaptable** — focused and easy to steer  
> **Rigid** — crowded and set in its ways

Locked visible instruction:

> **Keep context small and relevant.**

Locked personal speaker language:

> A fresh, focused coding chat is easier to steer. As the chat fills with abandoned ideas, stale
> assumptions, old tool output, and directions I no longer want, it can start to get set in its ways.
> That is what I mean by rigid. A million-token window is capacity, not a target. Just because Claude
> can hold that much does not mean I want every abandoned idea and stale decision following me
> through one coding chat.

Technical qualification: this is a practical heuristic, not a hard boundary or a claim that the
model's parameters change during the chat. Large, deliberately assembled contexts can be valuable
for reference work and synthesis. The recommendation is specifically to avoid accidental context
growth when a smaller, task-relevant coding context will do.

### Shared-understanding language

> I do not want the agent to make a chain of quiet design choices and hand me the endpoint. I want it
> to interrogate me about the consequential choices, explain what each option changes, and let me
> lock them in one at a time. Then the implementation follows decisions I can still explain and
> defend.

### Foundation-file language

> We have just done a great deal of valuable work scoping the problem. We have distilled a north star
> for an iterative coding agent: what it is trying to accomplish, the decisions I made, the boundaries,
> and the evidence that will tell us whether it worked. I do not want that value trapped in this one
> context window. I commit the distillation—not the transcript—to a Markdown file. That file becomes
> a context start: a new chat can load the agreed design directly instead of inheriting a lossy
> automatic compaction of the conversation that produced it.

Technical qualification for the spoken explanation: the file does not eliminate context limits or
compaction. It avoids **depending** on compaction for durable project knowledge. A future agent still
needs to load the file, and a stale foundation is not authoritative merely because it was committed.

### Proportional-workflow language

> I do not create a procession of documents for every code edit. If the work is small and bounded,
> the foundation is enough to begin an iterative loop. If the work has several independent outcomes,
> I translate the foundation into an execution specification and slice that into pieces that can each
> be built and verified. The amount of process should scale with the cost of getting lost.

### Specification-language capture

> I inherited the name `to-prd`, but I am not trying to produce product-management paperwork. This
> stage distils an agreed foundation into an implementation specification: the end state, its seams,
> and the evidence an execution agent must produce. The design decisions are already mine; this Skill
> packages them for execution.

Current invocation language after the locked rename:

> I invoke `to-spec` to package the agreed foundation for execution. The short Skill name stays
> general; the artifact says whether it is an implementation specification or a study/method
> specification.

### Vertical-slice language

Personal motivation:

> For a surface problem, I cared about the surface—not the rest of the material in the same way. I
> wanted the event workflow to focus on those surface environments, and coordination number gave me
> a direct way to distinguish them.

> With the threshold at eight, atoms with fewer than eight neighbours were the ones that received new
> event searches. In this system, that concentrated the work near the surface defects.

> Eight is not a coding number. It comes from my understanding of the surface. The coding workflow
> should make that decision explicit and testable, but it should not quietly make the scientific
> decision for me.

Candidate compact visual or spoken ladder:

> `12` — FCC bulk  
> `8` — ordinary FCC(100) surface atom  
> `7` — beside a surface vacancy → search here

Governing takeaway:

> A specification does not make the scientific decision. It preserves that decision and turns it
> into explicit, testable software behaviour.

> If I want to add a new data-analysis model, I do not make one issue for its data structure, another
> for its algorithm, and another for its tests. I find the thinnest complete path that accepts a real
> input, runs the model, exposes a result, and verifies that result. The same applies to adding
> coordination number to event searches: one narrow path through the scientific behaviour is more
> useful than a pile of disconnected layer tasks.

The coordination-number example is publicly verified in pyKMC pull request 91. It changes how pyKMC
classifies/selects atomic environments that receive event searches; it does not change the event-
search algorithm itself. The slice adds that capability end to end: configuration and validation, a
pure coordination-number classifier, `coordination` and `coordination/graph` dispatch, threshold
wiring through all five environment-construction sites, focused tests, documentation, and a real-
slab validation script. It deliberately leaves chemical colouring to the orthogonal companion pull
request 90—evidence of a meaningful slice boundary rather than an incomplete feature.

The pull request reports that, on a 9,679-atom Ni95Cr5 surface-vacancy slab, threshold 12 reproduced
CNA's 971 non-crystalline atoms with zero disagreement and threshold 8 selected a strict four-atom
subset. The exact slab input is not public, so do not claim this external validation is reproducible
from the repository; the public unit/integration checks are. The numbers are supporting evidence,
not the primary takeaway—the takeaway is the complete path from a user-selectable scientific mode to
an independently checked result.

The “new data-analysis model” example remains a hypothetical illustration. No public pyKMC or
pylatkmc artifact currently proves that complete slice, so do not present it as a second case study.

### Reproducer-first debugging language

> I do not begin by telling the LLM to fix the bug. First I make it prove that it can see the same bug
> I can see. We build a command or test that fails for the right reason, reduce it until the failure is
> clear, and keep that case as a regression test. Only then do we change the implementation and watch
> the same evidence go from red to green. Otherwise the agent can produce a plausible change without
> proving that it touched the problem I reported.

Feature slicing and bug diagnosis are related but not identical. A vertical slice bounds new work by
an independently verifiable capability. A red-capable reproducer bounds bug work by an executable
failure. Both prevent an agent from working against an unobservable goal.

### Layered scientific-verification language

> I want the inner loop to be cheap enough that the agent can run it repeatedly, so I reduce the
> system and use small fixtures locally. But that is not the finish line. At the end of the loop I run
> the representative examples again—or the exact system where I saw the problem. And if the behaviour
> depends on MPI scale or the cluster environment, I validate it there. My laptop's constraints are
> not automatically the constraints of the machine where the science will run.

Terminology guard: an example-system rerun is a **regression test** only when it contains a pinned,
machine-checkable expectation. Otherwise call it an end-to-end validation run or confirmation. Both
can be required; they provide different strength of evidence.

### Foundation-versus-handoff language

> `FOUNDATION.md` is durable: it records the design we want future sessions to share. A handoff is
> disposable: it is compaction with intention. I decide which goal, decisions, evidence, pointers,
> current state, and next step survive into a clean context. That clean context may continue the same
> task or take one independent task. When the work lands, I promote any newly durable fact and throw
> the courier away.

### Handoff-and-worktree language

> A new chat gives me clean conversational context; a worktree gives me separate code state. They
> solve different problems. If I am continuing one overloaded conversation, a curated handoff into a
> new window may be enough. If I am dispatching independent coding work, I pair that handoff with a
> worktree so the new agent has both a bounded brief and an isolated branch.

### Versatile-handoff language

> I do not want the handoff to carry the whole idea just because the previous chat needed it. I want
> it to carry what is relevant to the direction I am breaking off into. Sometimes that is a goal and
> a next action; sometimes it is a pointer to a specification, a failing test, a decision, or an
> observed result. Those are examples, not required boxes. The point is that I choose what the next
> context needs instead of dragging the entire reasoning history along with it.

Illustrative payloads for speaker notes or an optional example slide—not a universal contract:

- **Continue the same work:** current state, settled decision, useful evidence, next move.
- **Break in a new direction:** relevant premise, divergence point, local boundary, open question.
- **Execute a specification slice:** pointer to the larger spec, slice scope, starting state,
  verification target.
- **Use a separate worktree:** branch or checkout pointer, integration boundary, relevant checks.

Candidate visual:

> same task: large or stale context → curated handoff → fresh chat, same code state  
> one task from a specification: `to-spec` → bounded handoff → fresh chat → verified result  
> optional parallel work: independent handoffs → separate worktrees → merge + integration checks

The worktree branch is a vertical drill-down, not a required live-path slide. Keep its claim narrow:
a fresh session sheds the previous conversation's path-dependent state; a worktree isolates checkout
state. A handoff does not merge code, a worktree does not transfer understanding, and neither makes
integration conflicts or cross-slice regressions disappear.

### Teaching-Skill adaptation

> The design interview is really a reusable pattern for reaching shared understanding. I can point it
> at a feature I want to build, but I can also point it at something I am trying to learn. A teaching
> version can question me relentlessly, expose the parts I only think I understand, and refuse to move
> on until I can demonstrate the idea rather than repeat the model's explanation.

The accepted learning gate is demonstration across four modes:

1. Explain the idea in the learner's own words.
2. Apply it to an unfamiliar example.
3. Identify assumptions, limits, or a condition under which it would fail.
4. Diagnose and correct a plausible misconception.

### `review-analysis-claims` language

> Before I ask an AI to write the conclusion, I make it act adversarially toward my claims. It walks
> through how each result was estimated, the assumptions underneath it, what the magnitude means,
> uncertainty, causality, robustness, and finally the exact language the analysis licenses. The goal
> is not prettier prose. The goal is an interpretation that is accurate, bounded, and clear.

This is deliberately a **paper-writing** Skill. It reuses the one-question-at-a-time interaction
pattern from the design interview but walks a statistical interpretation tree instead of a software
design tree. The agent challenges the reasoning; the author retains ownership of the final claim.
Do not present the pyKMC units error as a historical success of this Skill, and do not claim that its
current evaluation proved it superior to an unskilled frontier model.

Stop condition:

> Before drafting prose, I can explain how each result was produced, its assumptions and uncertainty,
> what it substantively means, and the strongest claim the evidence actually supports.

### `review-workflow-candidate` language

> A Skill is not just a clever prompt I found online. It is a set of instructions I am inviting into
> the agent's working environment, and it may bring scripts, hooks, network access, or very broad
> triggers with it. I inspect the source before I install it: what can it instruct, what can it run,
> and when can it fire?

> There is another trap in downloading a pile of Skills: each one expands the trigger surface. If the
> descriptions overlap or hooks run automatically, I can fill the context with procedures I do not
> need and blow up the amount of tool activity. More installed Skills is not automatically a better
> workflow. I want the smallest set that earns its place.

Technical guardrails for the spoken version:

- Do not say that every installed Skill automatically executes or calls tools. Distinguish deliberate
  invocation from auto-triggered descriptions and always-on hooks.
- A plain Markdown Skill can still contain hostile or scope-exceeding instructions; bundled scripts
  and hooks add executable risk.
- The benefit of intake review is reduced and visible risk, not a guarantee that prompt injection or
  excessive invocation becomes impossible.
- “Install to try” is the wrong default for untrusted material: inspect in a non-discovered sandbox
  first, then test locally only after its instructions and executable surface have been reviewed.

### Invocation-versus-scope language

> There are two different decisions here. First: does this Skill run only when I ask for it, or can
> the model invoke it automatically? Second: is it available only inside this project, or is it part
> of my global working library? A manual Skill can be global. An automatic Skill can be project-only.
> Those are not opposites; they are two axes of the trigger surface.

Candidate two-axis visual:

| | **User-invoked** | **Automatically selected** |
|---|---|---|
| **Project-local** | Specialized command used only here | Project-specific behaviour that may fire |
| **Global availability** | Repeated command relevant across projects | Broad cross-project trigger; greatest context exposure |

The matrix teaches risk and reach, not a universal placement rule. “Global” must not be described as
equivalent to group-shared or always running.

### Eager-intern and Neuralyzer language

> I think of an LLM chat like a very eager intern who only lasts for one chat. It wants to do work for
> me. If I put ten tools on its desk, it may try to find reasons to use all ten, so I need to be careful
> what I let that intern see on a given day. More capability in view is not automatically better
> context.

> When I start a new chat, it is like the Neuralyzer in *Men in Black*: that intern no longer carries
> the path we took through the previous conversation. The next chat starts from the instructions,
> Skills, files, foundation, or handoff I deliberately put back in front of it.

Technical qualification: a fresh session is not literally empty. System instructions, project
instructions, available Skill metadata, durable files, and any product-provided memory may still be
loaded. The metaphor names loss of the prior chat's path-dependent conversational state. Likewise,
an agent is not guaranteed to try every visible tool; the point is that irrelevant capability expands
the context and opportunity for unnecessary selection.

### Repeated-prompt-to-Skill language

> One of my Skills started as a prompt I refined over time for turning textbook material into something
> easier to hear: preserve what was said, leave out the figures, and expand acronyms for read-aloud.
> That is useful enough to package and reuse, but I would never make it part of a coding repository's
> working context. The question is not only “is this a good Skill?” It is “does this intern need to
> know about it today?”

> In a coding repository, bug discipline is relevant. When the agent finds a bug, I want the available
> workflow to tell it not to leap straight into a fix. First make the exact failure reproducible; then
> diagnose and repair it against that evidence. That is a prompt I use repeatedly in coding, so it
> earns a place in that context.

Skill-creation threshold:

> I do not turn every prompt I reuse into a Skill. First I need to recognize the situation that should
> trigger it, know the procedure I want repeated, and be able to tell whether it did the job. Once
> that shape has stabilized, packaging the prompt means the next chat does not have to rediscover the
> procedure from scratch.

### Wild-west and adaptability language

> Coding with AI is still the wild west. People do not agree on the right set of Skills, the right
> project instructions, or even the right shape for a Claude file. Friends of mine at large technology
> companies tell me that the practice can differ from one department to another. People get better
> and worse results from different arrangements, and what works now probably will not be how we work
> a few years from now.

> I am showing you how I think about the problem, not handing you a canonical configuration. If you
> understand context, trigger surface, intentional handoffs, evidence, and ownership, you can change
> the tools without losing the reasoning that made the workflow useful.

Attribution guardrail: keep the slide generalized to “teams” or “large organizations.” If Stephen
mentions Apple aloud, frame it explicitly as a personal anecdote from friends, not an official or
comprehensive statement about Apple practice.

### Multi-machine Skill-management language

> I use several computers, but I do not want six slowly diverging copies of the same prompt. I keep
> the Skills I maintain under version control, then expose only the appropriate subset to each project
> and working context. That is how I keep a useful refinement made in one place available elsewhere
> without putting every Skill in front of every chat.

This is a personal-practice aside, not an installation tutorial. “Across six computers” may be used
as Stephen's own reported scale; do not claim that the public repository independently verifies every
machine. Do not publish machine names, private paths, branch topology, or local configuration details.

### Optional specialist-agent language

> Some reusable procedures are too specialized to sit on every intern's desk. My rate-catalogue
> workflow carries detailed pylatkmc context about event families, harmonic transition-state-theory
> prefactors, fallbacks, and provenance. It is valuable when I am curating that catalogue and noise
> almost everywhere else, so I dispatch a specialist only when I need it.

If this drill-down is used, connect it to ownership: the specialist can build a working pipeline and
produce a plausible prefactor, but Stephen still owns family definitions, representative-event
choices, fallback justification, zero-mode conventions, and physical plausibility. Passing code
checks alone does not validate the kinetics.

Accuracy notes:

- `curate-rate-catalogue` is a dispatched agent, not a Skill, and has no Skill eval.
- The sanitized library name is not yet consistently migrated in the private configuration layer;
  avoid implying otherwise.
- Any detailed rate or soft-mode numbers are Stephen's recorded observations unless a reproducible
  public artifact is supplied.

### MECH 479 “outer space” story

> In an earlier year, I would ask students where they were in the writing process, and many were quite
> honest. If they had not found an entry into a paper, I might suggest using AI to produce a summary
> they could start from. If they had written something but did not know how to progress, I might ask
> AI to polish the structure. That could be useful—but only if the student still checked the science.

> I had my own warning example: AI made a paragraph about dipoles much better structured, but reversed
> a comparison—effectively turning a greater-than relationship into a less-than relationship. The
> sentence became scientifically incorrect. I kept the better paragraph structure and repaired the
> relationship, which I could do only because I still knew what the science was supposed to say.

> In the more recent course, the models were more capable. Some students arrived having already used
> AI to find papers, process those papers, and build a report against the rubric. The submission could
> be ready very quickly, but when I asked questions about one of the cited papers, they could not give
> strong answers or judge which parts of the report were correct. They had delegated not one task but
> the chain of decisions that made the project theirs.

> That is what I call “outer space”: the report is present, but the student is disconnected from the
> decisions that produced it. It made me rethink the course and the assignment, because a polished
> artifact was no longer reliable evidence of understanding.

Candidate visual sequence:

> AI as orientation → AI as critic → AI as end-to-end author → **outer space**

Coding bridge:

> AI selects the design → writes the implementation → writes tests against its assumptions → explains
> its own output. If I cannot interrogate those steps, I can end with working software and still be
> outside the epistemic loop.

Privacy and attribution guardrails: describe an aggregate pattern across interactions, use no student
identifiers or report details, and do not imply a formal misconduct determination. Do not substitute
the separate MECH 203 teaching-assistant instructions example; that source illustrates constrained
tutoring, not the provenance Stephen has given for “outer space.”

Implementation audit: the current `diagnosing-bugs` Skill is marked user-invoked and cannot be
automatically selected by the model. Stephen's description of a project-aware agent invoking the
discipline only when it encounters a bug therefore names an intended context design or a project
instruction that routes to the Skill, not the current Skill's standalone invocation behaviour. Do
not state that the current Skill auto-invokes unless that configuration is deliberately changed and
verified.

## Stories

### Opening hook — car-wash hidden-goal anecdote

Prompt:

> I need to wash my car, the car wash is 10 m away should I walk or drive?

Observed failure pattern: a model recommends walking because the destination is close, overlooking
that the car must arrive at the car wash. The model answers a familiar distance/transport question
while dropping the implied purpose of the trip.

Coding bridge: “implement my new idea in this codebase” also invites a fluent, apparently working
answer while leaving the model to guess architecture, constraints, seams, and acceptance criteria.
This anecdote should lead directly into the design interview: hidden intent must be surfaced before
implementation.

Stephen supplied an exact response set on 2026-07-13. The screenshots all use the same `10 m` prompt:

- `codex-clipboard-7dec5779-6413-4dc5-ad07-132486576a4a.png`: the visible ChatGPT model is not
  identified. It first recommends walking, then adds an exception that recognizes the car must be
  brought to a drive-through or automated wash. Stephen describes this as a safeguard-like follow-on;
  the screenshot does not establish how that correction was produced.
- `codex-clipboard-22da6e34-627d-40b0-a5da-b0f95d6a258a.png`: **ChatGPT 5.3 Instant** recommends
  walking and never recovers the hidden goal.
- `codex-clipboard-0bce73a0-bc99-4293-90e1-f584b7da4e7c.png`: **ChatGPT 5.4 Medium** recommends
  walking and diverts into whether `m` meant minutes.
- `codex-clipboard-62ac6d4e-1b64-4141-9473-824ec4b43349.png`: **ChatGPT 5.4 Pro** recommends driving
  because the car must reach the wash. The `[Inference]` label reflects Stephen's personal ChatGPT
  instruction asking the model to identify the logic it used; do not present the label as a default
  product feature or proof of access to an internal reasoning trace.
- `codex-clipboard-4539a6b2-a504-4156-bb00-2fdeb1424d41.png`: an **Instant** ChatGPT response begins
  with walking for 10 metres, then recognizes that car-wash customers ordinarily arrive by car only
  in its separate 10-minutes branch. It is a partial catch, not a clean answer to the stated prompt.
- `codex-clipboard-62f415c2-2ed0-4929-af9d-e21fd3cecb1e.png`: **Claude Haiku 4.5** recommends
  walking.
- `codex-clipboard-6c4694f7-a237-49da-8aa3-bdc6a5f5a1c3.png`: **Claude Sonnet 5 Low** recommends
  walking.
- `codex-clipboard-0e231a05-4322-478c-a77d-39bd4de197ad.png`: **Claude Sonnet 5 Extra** recommends
  driving after a visible five-second thinking period.

Slide-asset note (2026-07-14): the section-1 “Walk… unless” slide uses Stephen's dark-mode
re-capture of the exception response (same response text verbatim as the 2026-07-13 light-theme
logged-out capture; `assets/carwash-exception.png`). Stephen identified this response's model as
**ChatGPT 5.5 Instant** (2026-07-14, from his account of the session; no model label is visible in
either capture). Slide caption and drill-down table credit it accordingly.

Added 2026-07-14 (section-1 interview): a ninth response, supplied by Stephen as a screenshot.
**ChatGPT 5.5 Instant**, dark theme; the prompt wording is identical except it ends with a period
rather than a question mark. The model answers "If it is literally 10 metres away, walk," then
lists the reasons one would drive (the wash requires the vehicle to enter under its own power; the
car must be moved onto the wash track) and gives the full practical sequence: walk to the car,
drive it the short distance into the wash, walk home only if leaving it there. It closes with a
10-minutes fallback. The trap's resolution arrives pre-packaged inside the exception structure.
Stephen's speculation, recorded as speculation and never slide text: famous trap patterns may get
special handling because a product that misses a simple question looks bad. The screenshot cannot
establish that; the no-mechanism-inference boundary below applies unchanged. Slide use: none.
Stephen decided (2026-07-14) the opening needs only two artifacts, the 5.3 Instant clean failure
(live hook) and the unidentified-model exception response (drill-down); the 5.5 response stays in
this record as evidence, without a slide.

Added 2026-07-14 (section-1 interview): the drill-down table also lists three Claude rows.
**Claude Haiku 4.5** (walk) and **Claude Sonnet 5 Low** (walk) are verified against the capture
set above. **Claude Opus Low** (drive) is included on Stephen's attestation from his own session
logs; no capture is held in this folder and Stephen explicitly waived verification to save tokens
(2026-07-14). The table slide's speaker notes disclose the logs-not-screenshot provenance. The
captured **Claude Sonnet 5 Extra** response (drive after visible thinking) is not in the table;
Stephen chose Opus Low as the Claude drive example.

Evidence boundary: the screenshots demonstrate different outputs across named model/mode/context
conditions. They do **not** reveal whether a correct or partial answer came from fresh inference,
post-training familiarity with a common puzzle, a system instruction, routing, or a curated
safeguard. That uncertainty is itself useful: one correct answer to a familiar trap is not evidence
that a model will recover the hidden purpose of a novel coding request.

Keep the “generated reasoning versus curated/safeguarded answer” question out of the live spine; it
is a legitimate but separate rabbit hole. If retained, it belongs in speaker notes or an optional
drill-down about why output alone does not reveal the production mechanism.

Locked image-selection decision:

- Use the clearly labelled **ChatGPT 5.3 Instant** failure as the live hook. It is a single observed
  response, not a claim that the model always fails.
- Reveal the missing purpose in Stephen's own words, then bridge directly to underspecified coding
  requests.
- Keep the **ChatGPT 5.4 Pro** correct response and the unidentified safeguard-like partial response
  in an optional vertical drill-down. They support “the same surface prompt can produce materially
  different answers,” while the notes preserve the uncertainty about why.
- Do not show all eight screenshots in the live path. That would be illegible at reveal.js scale,
  date the talk unnecessarily, and turn a hidden-intent lesson into a model leaderboard.
- If selected for the deck, copy each image into the talk's local `assets/` folder and crop UI clutter
  while retaining the exact prompt, response, and any model label used for attribution.

### Primary handoff story — diverged pyKMC implementations

The same first-step prune/log `KeyError` was first fixed on a substantially refactored basin-
hardening branch in [commit `9dba577`](https://github.com/hugomoison/pyKMC/commit/9dba57713c944e77bdeb79cbd0278b651ef48a32).
That implementation could not simply be transplanted into the less-refactored `develop` code path:
the two branches performed the migration at different seams. Stephen created a handoff for a fresh
session working against `develop` that carried:

- the narrowly stated bug;
- the requirement to produce a reproducible failing test first;
- clues from the refactored-branch solution;
- and the constraint that `develop` needed a small, native fix rather than the larger backend refactor.

The receiving session implemented the native fix in
[commit `d493f8a`](https://github.com/hugomoison/pyKMC/commit/d493f8aaa67e1f73acdd3995fb84543e9f742602),
added the focused regression in
[commit `817524e`](https://github.com/hugomoison/pyKMC/commit/817524ed328098bad152a96be0f51ee275b4b0ef),
and the change merged as [pull request 86](https://github.com/hugomoison/pyKMC/pull/86).
The locked story takeaway is:

> Carry the problem, evidence, and useful clues across a task boundary—not an obsolete solution.

Public history verifies the divergent native implementations, regression, and merge. It does not
record the temporary handoff that linked the work, so describe that mechanism as Stephen's account.
This story also does not prove that a long context made the model observably “rigid”; the clean
handoff was a preventive scoping choice.

Same-chat continuation remains the brief second example: when a useful conversation has become too
large or accumulated stale reasoning, create a curated handoff and continue in a new window with
only the context relevant to the next direction.

### HTST rate-units error

Repository history verifies the unit contract. The Vineyard calculation produced the attempt
frequency `nu0` in Hz (`s^-1`), while pyKMC's rate layer and KMC clock consumed the prefactor in
`ps^-1`. The initial HTST and RPA backends passed the numerical Hz value through without conversion.
In the implementation, the Vineyard expression is

> `nu0 = (1 / (2 * pi * hbar)) * product(hbar*omega_min) / product'(hbar*omega_saddle)`

where the primed saddle product omits the imaginary mode. Do not describe the product ratio as
dimensionless: the minimum has one more positive mode than the saddle, leaving one energy dimension
before division by `2*pi*hbar`. Because

> `k = nu0 * exp(-dE / (kB * T))`

uses the prefactor multiplicatively, this made every HTST rate `10^12` too large and simulated time
`10^12` too small. This statement applies to the finite-`nu0` HTST/RPA path; constant-style runs and
the `k0` fallback were unaffected. The code could run smoothly while the scientific result was wrong.

The history also verifies “green and wrong”: existing tests expected the raw Hz value as the resolved
prefactor, so they encoded the same mistaken unit contract. The regression commit corrected those
expectations and added an end-to-end boundary test using a committed Ni(100) surface-hop event
(`dE ~= 0.597 eV`) and a known 5 THz prefactor.

Teaching sequence:

1. An implementation choice was implicit rather than deliberately locked in.
2. The software and tests agreed with each other, but the physical rate was wrong.
3. Comparison with a known or expected value made Stephen distrust the result; investigating that
   external scientific mismatch exposed the unit inconsistency.
4. The recovered unit contract became an explicit boundary helper, backend documentation, corrected
   expectations, and a regression test, so the choice is no longer left to a person or agent to
   guess.

Verified public evidence:

- Historical HTST implementation context: [pyKMC pull request 71](https://github.com/hugomoison/pyKMC/pull/71).
  The closed draft reports 48 passing HTST tests and describes `k_prefactor == nu0`; that validation
  belonged to the pre-correction unit convention and should not be presented as the final unit proof.
- Boundary fix: [`d705932`](https://github.com/hugomoison/pyKMC/commit/d70593204290d7e8e978da1caa30f2e0733446a1),
  converting finite HTST/RPA `nu0` values from Hz to `ps^-1` once at the backend boundary.
- Physics regression: [`d6b921f`](https://github.com/hugomoison/pyKMC/commit/d6b921f4e461c0aa5d1ed265fe26931b25e0e92c),
  adding `tests/htst/test_rate_units_boundary.py` and correcting earlier expectations that encoded the
  `10^12` error.

The commits and links resolve publicly as of 2026-07-13. They verify the implementation and correction,
but not that a particular agent made the original choice or that the design-interview Skill was used
at the time. Unless further evidence appears, present this as the kind of hidden decision the current
workflow is designed to surface—not as proof that the Skill prevented the historical bug.

The named Skill is retrospective: the public HTST work and units fix predate the current Skill and no
matching design-interview artifact exists in the public repositories. Accurate speaker language:

> This work already followed parts of the practice—capturing decisions, blockers, fallbacks, and
> acceptance evidence. I later formalized that practice as a reusable design-interview Skill.

Do not transfer pyKMC's unit bug to pylatkmc. pylatkmc deliberately stores `prefactor_Hz`, evaluates
rates in `s^-1`, and advances its clock directly in seconds. Converting that prefactor to `ps^-1`
without changing its clock would introduce the same `10^12` error in the opposite codebase.

### “Outer space” teaching analogy

Stephen uses “outer space” for the point where every intermediate judgement has been delegated and a
student can no longer evaluate or defend the final result. The source notes give this typical chain:

1. AI selects the papers.
2. AI summarizes the papers.
3. AI chooses the points.
4. AI builds the outline.
5. AI writes the report.
6. The student submits text they have not read closely and cannot defend.

The problem is not that AI was used; the human has left the **epistemic loop**.

Coding bridge: if an agent silently accumulates consequential choices over many turns, the human may
be unable to reconstruct, explain, or defend the resulting implementation. Staying human-in-the-loop
means owning the decision chain, not merely approving the final diff. The coding analogue is an agent
choosing the physical model, numerical method, implementation, tests, and interpretation against its
own inherited assumptions until the researcher can no longer explain the model, units, test oracle,
or failure conditions.

Public-safe framing: present this as Stephen's informal name for a failure pattern or composite
teaching scenario, not as a claim about a particular student. The locked visible heading is **Stay
inside the epistemic loop**, with “outer space” retained in Stephen's speaker notes. The current
draft closing line is **Delegate labour, not scientific judgement.** Its final cadence may be refined
after rehearsing the first deck.

### QE energy-extraction story — “I was the agent for the LLM”

Stephen's account, from Lauren's computational materials course. Students (and Stephen) tried to use
ChatGPT on course tasks and it failed often until the question was asked the right way. The example
Stephen retells: processing Quantum ESPRESSO DFT output. The output files were huge, and ChatGPT at
the time had no reliable way to extract the total energy. Even told explicitly that the energy was
needed, it would at best grab a few energy values from somewhere in the pasted file. It produced the
right answer only when Stephen specified the method: grep for the energy lines only (or he ran the
grep himself), print that list, sort it, and verify the number of entries matched a direct grep
count. His summary: “At the time I guess I was the agent for the LLM,” and he could only steer it to
the right answer because he already knew how to get it. He then turned the working recipe into a
prompt and script that made his own data processing faster.

Lessons the story carries (in his words, paraphrased): models can recognize what kind of prompt they
are given and answer that recognized pattern, so prompt care matters; extraction from large
scientific outputs needs an explicit, verifiable method; and this is exactly what to think about
when writing prompts for agents or Skills that process data.

Placement (decision 85): NOT in section 1's live path. Candidate homes are section 3 (the human
supplies the method; verification step mirrors the grep-count check) or section 4 (repeated prompt
hardened into a script/Skill is the origin story of a Skill). The section 3 and 4 interviewers
should decide where it lands; it should appear exactly once.

## Public implementation evidence ledger

These links are candidates for slides or speaker notes. Inclusion in the ledger does not yet mean
every artifact belongs in the 20–30-minute live path.

- **Explicit physical boundary:** [pyKMC `d705932`](https://github.com/hugomoison/pyKMC/commit/d70593204290d7e8e978da1caa30f2e0733446a1)
  converts Hz to `ps^-1` exactly once at the backend boundary while retaining raw `nu0` in Hz for
  diagnostics.
- **Regression against a scientific contract:** [pyKMC `d6b921f`](https://github.com/hugomoison/pyKMC/commit/d6b921f4e461c0aa5d1ed265fe26931b25e0e92c)
  checks rate, residence time, and constant-versus-HTST equivalence at the same physical prefactor.
- **Reproduce before theorizing:** [pyKMC pull request 86](https://github.com/hugomoison/pyKMC/pull/86)
  adds a focused first-step failure regression, moves the smallest relevant seam, and verifies the
  change with both the suite and a short real MPI run. This pull request was merged.
- **Extract one bounded vertical slice:** [pyKMC pull request 90](https://github.com/hugomoison/pyKMC/pull/90)
  separates multi-element colouring from a much larger bundled change and threads that one capability
  through classification, symmetry, persistence, and tests. This pull request was merged.
- **Coordination-number feature as a complete slice:** [pyKMC pull request 91](https://github.com/hugomoison/pyKMC/pull/91)
  adds two user-selectable atomic-environment styles through configuration, classification, dispatch,
  all construction sites, tests, documentation, and real-slab validation while keeping colouring in
  the orthogonal pull request 90. This pull request was merged. The reported real-slab validation's
  exact input is not public, so only its public unit/integration checks are independently reproducible.
- **A different but explicit rate/clock contract:** [pylatkmc `e2296d7`](https://github.com/Kerrator/pylatkmc/commit/e2296d789a0c4eb0f33fe686dc233215af552e5b)
  stores `{prefactor_Hz, Ea_eV}` and evaluates the Arrhenius rate at runtime temperature in C. This is
  public branch history, not evidence that the feature is on the current public `main` branch.
- **Historical design record:** [pyKMC pull request 71](https://github.com/hugomoison/pyKMC/pull/71)
  records architecture, dependency, fallback, review, and validation decisions for the HTST backend.
  It is a closed, unmerged draft and must be labelled that way if shown.
- **Current long-context capability and curation warning:** Anthropic's
  [context-window documentation](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  lists one-million-token windows for several current Claude models, while explicitly warning that
  accuracy and recall can degrade as token count grows and that context still needs curation. This
  product fact was checked on 2026-07-13 and should be date-qualified if used.

## Course and workshop parking lot

- Starter exercise: open Claude Code in a small, non-critical Python repository; ask it to inspect
  the project, make one bounded change, run a named verification command, and show the diff and
  evidence. Valuable for a course, but not required in this talk.

## Remaining non-blocking authoring and release checks

- What are the exact prompts and observed responses for the strawberry and answer-shortcut examples?
  Which model and date produced each response? This is required only if a screenshot or model claim
  is added; the presenter-led strawberry anecdote does not depend on it. The car-wash evidence set is
  captured above.
- Worktrees need no concrete live example. Add one only if a public-safe optional drill-down improves
  the rendered deck.
- Authoring default for live Skill examples: debugging discipline, the trusted-but-irrelevant
  textbook/read-aloud contrast, Skill-intake curation, and a brief `review-analysis-claims` mention.
  Keep formal evaluation, synchronization, and specialist agents optional.
- Reconfirm that every selected scientific and teaching example remains suitable for a
  world-readable public deck during the final release review.
- Does later evidence support a claim that neutral naming reduced Fable interventions? The recorded
  naming pilot was inconclusive, so the first deck must not make that causal claim.
- Choose the final subtitle and rehearse the closing sentence after the first rendered draft exists.

## Private maintenance follow-ups — not talk blockers

- Reconcile the current manual-only `diagnosing-bugs` frontmatter with Stephen's preferred model of a
  coding chat that knows the discipline and uses it only when an actual bug is encountered. Do not
  change the private Skill until that behaviour is deliberately designed and authorized.
- Complete or deliberately abandon the private rename from `ingest-htst-bridge` to
  `curate-rate-catalogue`; the talk may use the sanitized conceptual label without claiming the
  migration is finished.

## Out of scope for the first draft

- Copying the old deck's seven-phase structure wholesale.
- Publishing private configuration-repository details.
- Treating product-specific names or current model tiers as durable general facts.
- Dense slides that combine multiple ideas or push notes onto the visible canvas.

## V2 scope decisions — 2026-07-13 design interview

These decisions govern the v2 deck in this folder. They were locked one at a time in a design
interview after the first (Codex-built) rendered draft was reviewed and rejected.

77. **Build v2 in a new folder, `talks/2026-coding-with-ai-v2/`.** The first draft's folder,
    `talks/2026-coding-with-ai/`, stays untouched as a frozen artifact (it is untracked in git and
    lives only in the main checkout). This foundation copy travels with the living deck.
78. **Treat the Codex draft as a content outline only.** Its execution was rejected on all four
    reviewed dimensions: visuals and design, wording and voice, narrative flow, and slide craft and
    density. V2 reuses its rendering nowhere. Evidence assets (e.g. the cropped ChatGPT 5.3 Instant
    car-wash screenshot) are screenshots, not designed visuals, and may be copied into v2's
    `assets/`.
79. **Keep exactly two beyond-foundation drill-downs from the old Claude deck.** The **Ralph loop**
    hangs as a vertical under Section 3, beneath the specification → slices → bounded-loops slide,
    as the autonomous-execution flavour of that path. The **vocabulary tables** are re-derived, one
    per spine section as its last vertical, from this file's working glossary; Dictionary of AI
    Coding terms are reframed, never quoted (no licence). Everything else beyond the foundation is
    cut: the Rosetta stone (tokens ↔ KMC isomorphism), the kit slide, the seven-phase pipeline, the
    kanban graph, and the smart/dumb-zone framing (superseded by adaptable/rigid).
80. **Use a fresh visual system: “The Invisible Variable.”** A dark scientific keynote in which the
    missing goal, context, or physical reference is revealed in gold. Palette from the concept
    exploration: deep blue `#002452`, gold `#FABD0F`, red `#B90E31`, white, near-black `#212121`.
    Nothing is ported from the old Claude deck's CSS or SVGs; all figures are redrawn to this one
    system. Avoid dashboards, grids of cards, and generic corporate styling.
81. **Build with a hybrid process.** One narrative owner (the primary agent) writes the full spine
    and every line of visible text in a single pass, so voice and flow have a single author. Agent
    handoffs are used only for bounded subtasks: SVG asset production to the Invisible Variable
    spec, and independent audits (overflow, offline, evidence links, notes/timing). This preserves
    decision 76's handoff discipline while fixing the stitched-voice failure of the first draft.
82. **Leave the landing page untouched until v2 passes the done criteria.** When v2 is verified
    (offline, no overflow, notes present, landscape PDF exported), repoint the existing
    “Coding with AI” entry on the root `index.html` to `talks/2026-coding-with-ai-v2/`. The frozen
    first draft becomes unlisted.
83. **Add nothing beyond the foundation.** No live demo, no group-rollout section. The first
    rendered v2 draft — not further scoping — exposes any remaining choices.
84. **Refine each section interactively, in its own fresh context.** (Amends the second half of
    decision 81.) After the single-owner first draft, each of the five sections is revisited in a
    NEW session that loads a curated handoff brief (`handoffs/CONTRACT.md` +
    `handoffs/section-0N-*.md`), interviews Stephen one question at a time about what the section's
    slides should contain, drafts options back and forth, and treats a slide as settled only when
    Stephen explicitly locks it. Sessions run one section at a time; each edits only its own
    section block of `index.html` and commits when the section is locked. The 2026-07-13 draft
    (evidence and language audits passed) is starting material, not a commitment. The PDF export
    and the landing-page repoint (decision 82) wait until all five section interviews are done.
85. **Section 1 stays the fast cold open; the QE energy-extraction story lands later in the talk.**
    (2026-07-13 section-1 interview.) Stephen's stated goal for the opening: models are getting
    better but can still fail silly cases, and that is still the case for science. Section 1 keeps
    the car-wash hook in place and fast, planting at most a one-line foreshadow that science
    examples follow later. His Quantum ESPRESSO energy-extraction story (see Stories → “QE
    energy-extraction story”) must not be dropped from the talk: the section 3 and 4 interviewers
    choose its single home (workflow verification vs. Skill origin).
86. **Section 5 meets hesitancy first and lands on encouragement.** (2026-07-14 section-5
    interview.) The caution is the handshake, not the destination: the three failure stories
    validate the audience's earned hesitancy about AI in scientific code, the epistemic loop
    answers it, and the section ends on what the discipline unlocks. Amends the emotional reading
    of decision 59's escalation without changing its content.
87. **Section 5 opens with the MECH 479 story; the definition beat follows.** (2026-07-14
    section-5 interview.) The story slide is retitled in Stephen's felt language ("Less connected
    to their own writing"); red "outer space" appears in the progression line one slide before
    "Stay inside the epistemic loop" defines it (example before abstraction). Decision 54's
    visible heading is retained, one slide later. The dipole slide now carries an on-slide
    epistemic caption ("the shape of the error, not the sentence"), and the HTST evidence table
    is trimmed to the three units-story receipts (fix commit, regression commit, closed design
    record).
88. **A builds-montage "unlock" slide sits between the HTST drill-downs and the close.**
    (2026-07-14 section-5 interview.) Headline: "Going from idea to implementation has never been
    easier." Content: the looping Blender clip of a pyKMC event (Claude driving Blender over MCP)
    plus four small app tiles: pylatkmc, to-do, Netrunner, lotusfield. The Netrunner glyph is
    drawn in-house (click-inspired); no third-party artwork enters this public repo. Speaker
    notes carry the five build stories.
89. **The closing cadence is rehearsed and recorded.** (2026-07-14 section-5 interview.)
    Stephen's spoken close uses the eager-interns metaphor and "stay connected to the work",
    deliberately echoing the section opener's disconnection language, and ends on learning along
    the way as tools change. No URL or contact pointer on the final slide.
90. **Section 4 leads with Skills keeping the human in the loop.** (2026-07-14 section-4
    interview.) Stephen's takeaway: a good Skill prompts reflection on direction, so each decision
    is understood and direction errors are caught while they are cheap. Spoken corollary, kept in
    notes: a clarifying question the researcher cannot answer is the signal to go read, or ask the
    group, before the code moves. The design interview is the flagship example.
91. **The HTST time-scale traceback is section 4's story.** New vertical under "A prompt earns its
    packaging": during the pyKMC HTST design interview one question settled the time scale;
    Stephen took the paper's convention and the spec recorded it; later a computed rate landed
    orders of magnitude off an accepted literature value; the external mismatch, not the Skill,
    triggered distrust, and the recorded decision made the "why" findable. Spoken as "orders of
    magnitude", never a number; the 10^12 factor and the green-tests lesson stay in section 5. The
    interview/spec provenance of the choice is Stephen's account.
92. **The claims-walk drill-down is replaced by "The Skill, as written".** (Amends the depth half
    of decision 36.) The slide renders the interview Skill's condensed core instruction
    ("Interrogate me about each decision that is not already settled in the code base or
    foundation..."); take line "It hunts the decisions not yet on the record."
    `review-analysis-claims` keeps brief live visibility via the opener bullet; its stop
    condition, the teaching adaptation, and the honesty guardrails move to speaker notes.
93. **Drift is the stated reason for maintenance.** Opener bullet: "Observed for drift; revised or
    removed when it stops helping." A Skill drifts from what performs best as models and practice
    change; observation is part of owning one.
94. **The intern's-desk contrast is three cards.** (Amends decision 45.) Study chat (textbook
    read-aloud) / Hobby chat (deliberately generic: the audience is not told the hobby) / Coding
    chat (debugging, the gold card). The relevance-not-quality takeaway is unchanged; the
    pyKMC-versus-paper-figures-versus-hobby "different desks" line lives in the notes.
95. **The `curate-rate-catalogue` specialist drill-down is cut.** (Exercises the optionality in
    decision 53.) Section 4 has no specialist slide; the ownership tie stays in section 5.
96. **The intake slide is framed eagerness-first.** Locked headline kept (decision 38). Lead:
    "Agents are eager: give one a tool and it will look for a reason to use it." Exposure includes
    every place a Skill is listed (CLAUDE.md and AGENTS.md standing files), read by every agent
    and subagent; "Inspect before you adopt. Keep the active set small." is now the take line.
    Decision 37's guardrails stay in the notes.
97. **The two-axis table is a quadrant figure.** `assets/skill-axes.svg`, Invisible Variable
    style; the global-and-automatic corner carries the slide's gold as "greatest context
    exposure". Take line unchanged.
98. **The maintained-Skills repo is a visible drill-down under the wild-west closer.** (Supersedes
    decision 52's one-sentence cap; its no-paths rule stands.) One version-controlled repo,
    per-project shelves; helps generate project-tailored Skills; tracks related Skills so an
    improvement disseminates to relatives. Being made public for the group; unnamed on the slide
    until it is public. Framing is an invitation: "a jumping-off point for a workflow of your own."
99. **The wild-west closing line is reworded to invite.** (Amends decision 51's close and the
    locked durable takeaway.) New goldline: "My configuration is a starting point, not a standard.
    Keep the habit: decide what belongs in context, and change it as the tools change."
100. **Section 4 vocabulary glosses are in spoken voice.** Terms unchanged; glosses reworded (e.g.
    trigger surface: "Everything a chat can see that can cause behaviour. Every place a Skill is
    listed makes it larger.").
101. **The QE energy-extraction story lands in section 4's opener notes.** (Closes decision 85's
    placement question; section 3 must not duplicate it.) Told as the origin story of packaging:
    Stephen supplied the extraction method, was "the agent for the LLM", then hardened the recipe
    into a prompt and script. Notes only; the opener's visible content is unchanged.
102. **The node metaphor is visible in section 2.** (Amends decision 9's notes-only scope.) A
    lead-in slide, "What is a token?", carries the chain of words: the smallest bit of information
    the model works with; a node connected to the other tokens in the window; its working meaning
    comes from those connections. The object variant and the not-literal-architecture hedge stay
    in the notes. The vocabulary table gains a matching "token" row.
103. **The token figure's second sentence is the lead nurse.** "the lead author checks the dose"
    becomes "the lead nurse checks the dose": both "lead" (metal versus role) and "dose"
    (radiation versus medication) flip meaning, and the figure marks the dose flip in soft blue
    with output labels "lead, the metal" / "lead, the role". Pb/lead convergence (different token
    IDs arriving at the same working meaning) is a notes-only aside. The strawberry slide keeps
    its single spaced reveal (confirms decision 12's presenter-led form).
104. **The context slide is a zone diagram with a growth progression.** The Adaptable/Rigid cards
    become one context-window figure with two overlapping zones (overlap = no sharp line),
    uniform token density, and captions "attention concentrated on what matters" versus
    "attention spread thin across the crowd". Three drill-downs show the window filling: the
    attention fan from the next-token position grows wide and faint. Visible labels stay the
    locked pair (decision 69); smart/dumb is spoken colour in the notes only. New locked speaker
    line: "A model's best work happens when the context is small and targeted." All stages carry
    the cartoon-not-mechanism hedge.
105. **Section 2 closes on practice: new chats and /btw.** A main-path slide, "Do not be afraid
    to start a new chat", pairs a fresh window against /btw side questions (mechanics verified
    against the Claude Code interactive-mode documentation on 2026-07-14: overlay answer, sees
    the conversation, no tools, never enters history) and bridges forward in gold: carrying the
    thread into the new chat is a handoff (section 3). A drill-down, "A workspace the agent can
    navigate", carries the small-modules and docs-link-to-docs discipline (one huge file versus
    navigable pieces). The vocabulary table gains a "/btw side question" row.
106. **Open handoff with context-window curation, not the example.** (Amends decision 33.) The
    handoff slide leads with a simplified two-window figure: one long session's crowded context
    (goal and decisions among abandoned ideas, stale assumptions, old tool output) versus a fresh
    session started from a handoff (the task, the decisions that matter, evidence and next move,
    room to work), reusing section 2's locked crowded/focused language. The first drill-down
    contrasts automatic compaction with handoff (both compress; only one is intentional). The
    diverged pyKMC bug story remains the primary concrete example but moves to the second
    drill-down, followed by the what-a-handoff-carries table and worktrees. Locked in the
    2026-07-14 section-3 interview.
107. **Park the verification ladder for a pyKMC talk.** (Amends decisions 27 and, for section 3,
    the vocabulary-placement half of 79.) The four-stage inner-loop/outer-gate ladder is pyKMC
    design and verification guidance, not agent-workflow guidance, so it leaves this talk. The
    ladder, the regression-versus-validation terminology guard, and the HTST diagonalization
    story that motivates it (a laptop failing to diagonalize a huge system says nothing about the
    cluster) are parked in `notes/pykmc-talk-ideas.md` at the repository root, with
    `assets/verification-ladder.svg` kept for reuse. Reproducer-first (decision 26) still carries
    the evidence discipline in section 3. The vocabulary table becomes section 3's closing
    horizontal slide, with **automatic compaction** added as a seventh term beside handoff.
    Locked in the 2026-07-14 section-3 interview.
108. **Frame section 3 as context management, opened by the manual-subagent story.** Stephen's
    declared takeaway for the section: how to manage context, with Skills doing repeatable things
    well planted here and harvested in section 4. A new opening slide, "I was the context
    manager," tells his grad-course story (an LLM could not parse a huge output file until he gave
    it a procedure: grep the lines that matter, write them to a small file, analyse that, report
    back), with the copy-paste era and the tidy-workspace lesson in its notes. Workflow stages
    that are named Skills carry a small mono **skill chip** top-right (`interview-design-decisions`,
    `build-design-foundation`, `to-spec`); chips mark named Skills only, so discipline slides
    (opener, reproducer-first) carry none. The FOUNDATION.md slide states visibly that this
    presentation was built this way, without showing a path. Section 4 should harvest the chip
    motif. Locked in the 2026-07-14 section-3 interview.
109. **Deliver from an unlisted Winter Atomics URL.** (2026-07-14, after all five section
    interviews locked.) The finished deck is hosted verbatim on Stephen's personal site repo
    (`Kerrator/WinterAtomics`, www.winteratomics.ca) at `talks/2026-coding-with-ai-v2/`, not
    linked from any navigation, matching how the previous talk was hosted. The delivery URL is
    the hosting outcome for this talk; the presentations-repo landing-page repoint in decision 82
    stays parked until Stephen asks for it. The talk folder carries its own PDF backup
    (54 pp landscape, fonts embedded) and a pixel-faithful PPTX (48 slides at the deck's true
    1060 × 740 pt visual box, speaker notes attached), both regenerated from the merged deck.
110. **Vendor the deck's declared fonts; note the tight-viewport caveat.** (2026-07-14.) The
    first-draft CSS declared Open Sans Var and Plex Mono from `css/fonts/` but the woff2 files
    were never copied in, so every section interview reviewed the deck in the system fallback
    font. Stephen chose to vendor the three files from the v1 talk; two table slides were
    re-tightened for the new metrics (six-model table image margin, workflow vocabulary table at
    0.53 em) and the full overflow audit re-passed. Known caveat, deliberately not "fixed":
    sections carry 10/20 px content-box padding outside reveal's 960 × 700 canvas, so a few long
    lines paint up to ~40 canvas px past the nominal edge. Harmless on wide displays and in the
    PDF/PPTX, but a near-4:3 fullscreen viewport (an iPad, some projectors) could clip those
    glyph tails. Changing the box model would re-wrap locked slides, so it needs Stephen's
    explicit decision; parked as a follow-up.
111. **Guideposts: an outline slide plus a section tracking bar.** (2026-07-15, Stephen's request;
    style locked by interview: labeled segments, outline directly after the title.) A new "The
    plan" slide (h = 1) maps the five sections, gold numbers echoing the kickers, one muted gloss
    phrase each. A fixed **guidepost bar** lives in the letterbox below the canvas on every slide
    except the title: five equal segments labeled "N · section name", the current section's label
    lit (gold number, white text) with a gold fill showing progress through that section's
    horizontal stacks; finished sections keep a dim filled track. Implementation derives the
    section map from the kickers already on each stack (no duplicate bookkeeping), replaces
    reveal's plain progress strip, and nudges the corner chrome up clear of the bar. The PDF
    export gets a static copy of the bar injected at the foot of every printed page, so the
    backup keeps the guideposts. Export note recorded with the decision: reveal 6's true print
    view emits exactly one page per leaf at the deck's own aspect (749 × 546 pt landscape); the
    earlier 792 × 612 letter export turned out to be the scroll-view fallback winning a race,
    which is also why per-page chrome could never appear in it. The PDF is now 49 pages, one per
    leaf, bars included; the PPTX captures include the bar pinned to the crop region.
112. **Reorder the spine: tokens and context becomes section 1; from chat to agentic coding becomes
    section 2.** (2026-07-27, after Stephen rehearsed the talk aloud several times.) This amends the
    "Locked live spine" block, the authoritative deck-drafting brief, and decisions 72, 73 and 85,
    all of which fixed agentic coding as the opener and the car-wash prompt as the cold open. His
    reason is delivery, not content: rehearsing it, the machinery has to be in the room before the
    agentic-coding definition means anything. Consequences carried out: the outline slide's rows and
    its spoken roadmap swap; eight kickers renumber in one pass; the title-slide notes now read the
    three takeaways "in the order we walk them" rather than in priority order, since the priority
    order (workflow first) no longer matches the running order recorded at "Priority of ideas".
    Decision 72's prohibition ("strawberry belongs later in the token/context section, not in the
    cold open") is knowingly overridden by this decision together with decision 113: strawberry now
    lands in the talk's first three minutes. Stephen accepted that in rehearsal; the hook is now the
    tokenization surprise rather than the car wash.
113. **Strawberry precedes the lead figure inside the token section.** (2026-07-27, rehearsal.) Pure
    position swap; the primary token takeaway (contextual representation, decisions 7 and 8) stays
    on the lead figure, which keeps its `take` line. Because "change the representation" is now
    spoken before "contextual representation" is defined, the strawberry notes gained an explicit
    gloss separating the two senses of the word, and the lead-figure notes gained a one-clause
    re-entry into the node picture.
114. **Handoff closes section 1 and is the first Skill named in the talk.** (2026-07-27, rehearsal;
    Stephen chose this placement over opening section 3 with it.) The whole handoff run (parent plus
    four drill-downs) moves out of section 3 to sit after "Do not be afraid to start a new chat",
    which already bridged into it in gold. That on-slide bridge loses its "Section 3." pointer and
    becomes an immediate lead-in. This amends decisions 105, 107 and the "Context narrowing" chain
    (FOUNDATION 612-621), where handoff was the LAST narrowing step, defined by contrast with
    FOUNDATION.md and to-spec. Since handoff now precedes both, its slides were rewritten to stand
    on their own: the FOUNDATION.md contrast became a forward pointer, the "same rule as the
    foundation file" echo became the first statement of the rule, and two on-screen forward
    references to artifacts not yet introduced were reworded ("Execute one spec slice" → "Execute
    one piece of a larger plan"; the mono line `one spec slice: to-spec → …` → `one planned piece:
    written plan → …`). Section 3's "Scale the process" notes now refer back to handoff instead of
    introducing it.
    **A `Skill: handoff` chip was added and then removed the same day; see decision 120.**
115. **Vocabulary tables follow the material.** (2026-07-27.) Section 1's table was promoted from a
    drill-down under "Keep context small" to its own closing horizontal stack, so the section still
    ends on its vocabulary, and gained **handoff**, **automatic compaction** and **worktree** from
    section 3's table. It runs at 0.45 em with three glosses shortened; the audit re-passed. Section
    3's table drops to four terms, all of them artifacts, and returns to the default size; its
    closing note no longer says "keep handoff" (which presumed handoff closed that section) and now
    points at vertical slice, with a pointer back to section 1 for the three moved rows. This amends
    decisions 79 and 107 on table membership, not the one-table-per-section rule.
116. **The two "I was the agent" tellings merge into one slide on section 2's spine.** (2026-07-27,
    rehearsal; Stephen chose "both, merged".) This resolves a real conflict in the record: decision
    101 filed the Quantum ESPRESSO story in section 4's opener notes and forbade section 3 from
    duplicating it, but decision 108 later created "I was the context manager" as section 3's opener
    telling the same grep-the-output-file episode. The story now appears **exactly once**, as
    required at FOUNDATION 1396: retitled "I was the agent", it is the last spine stack of section
    2, with both courses on the slide (the QE total energy and the grad-course analysis) and the
    shared procedure line beneath. The agentic-coding vocabulary moved to be its drill-down, so the
    section still closes on vocabulary. Section 4's opener notes keep only a one-line callback plus
    the life-cycle sentence, so nothing is told twice. The gold payoff, "I was doing a subagent's job
    by hand", now lands one slide after the sub-worker clause in decision 117 instead of 25 slides
    later, which also mitigates decision 53 (no Skill-versus-subagent distinction on the core spine):
    the word arrives with its story attached.
117. **Reword the agentic-coding gloss and the title subtitle.** (2026-07-27, rehearsal, Stephen's
    exact wording.) The vocabulary row becomes "An LLM working inside the codebase, having
    sub-workers find relevant context for itself." The co-located pair panel and `take` line on
    "Inside the codebase" were deliberately left alone: the definition gains its sub-worker clause in
    one authoritative place, and the story slide immediately after supplies the payoff. The title
    subtitle's gold span changes from "scientific ownership" to **"using AI in science"**, settling
    the wording FOUNDATION 1452 left open until after a rendered draft existed; the stale
    "(Subtitle is provisional…)" marker was deleted from the title notes. Section 5 keeps its name,
    "Ownership and validation".
118. **The design interview moves into section 4 as the flagship Skill.** (2026-07-27, rehearsal.)
    "Expose the decisions" leaves section 3 and becomes the first drill-down under "A prompt earns
    its packaging", ahead of the HTST payoff slide and "The Skill, as written" (which were already
    entirely about this Skill and previously had no antecedent). It is demoted to `h3`, its kicker
    stripped so it cannot hijack the parent stack's section number, and it keeps its
    `interview-design-decisions` chip. Its first bullet, an ordinal claim ("The first job is not to
    generate code"), became "The discipline: no code until the decisions are on the record", since
    the deck has by then already walked handoff, foundation and slices. This amends the locked
    section-3 takeaways (FOUNDATION 581-597), which filed the interview takeaway and stop condition
    under section 3; it is supported by decisions 90 and 92, which already named the interview
    section 4's flagship example. Section 3 now opens on FOUNDATION.md, whose notes previously began
    "We have just done valuable work scoping the problem" with no antecedent; they now introduce the
    interview in two spoken sentences and point forward to section 4. Section 3 retains five stacks
    (foundation, spec + Ralph, slices, reproducer, vocabulary); the outline gloss changed from
    "interview · foundation · slices · evidence" to "foundation · spec · slices · evidence".
119. **Deck geometry after the restructure.** (2026-07-27.) 28 horizontal stacks and 49 leaves, both
    unchanged; section stack counts are 7 / 4 / 5 / 4 / 6. Verified in the browser: zero leaves
    overflow the 960 × 700 canvas (worst 704, within the audit's tolerance and unchanged from the
    pre-edit deck), all 49 leaves carry speaker notes, all figures load, KaTeX renders, and the
    guidepost bar reports the five sections in the new order with correct fills. The content-box
    padding caveat in decision 110 is untouched and still parked. Two delivery notes: the persisted
    chalkboard key `2026-coding-with-ai-v2-chalkboard` must be cleared, because rehearsal ink is
    keyed to slide indices that have all moved, and every `#/h/v` deep link into this deck is now
    stale.
120. **No chip on handoff: it stays a discipline, and the private Skill's stance is rejected.**
    (2026-07-27, Stephen, same session as decision 114.) The `Skill: handoff` chip added earlier that
    day is removed, restoring decision 108's rule that chips mark named Skills only and returning the
    roster to three (`interview-design-decisions`, `build-design-foundation`, `to-spec`). His stated
    reason is substantive, not cosmetic: **"I do not think you should hit compaction often if ever."**
    The private `handoff` Skill file recorded at FOUNDATION 671 says the opposite, that continuous
    work should let automatic compaction run instead of writing a handoff. Rather than put that
    file's name on a public slide, the deck keeps the discipline unnamed and keeps its own line,
    "do not depend on automatic compaction for anything durable" (section 1's handoff run and the
    FOUNDATION.md take line in section 3), which matches what he actually practises. The caveat
    raised under decision 114 is therefore closed by removing the claim, not by editing the Skill;
    correcting the private `handoff` Skill remains open work outside this talk, and this decision
    does not authorize it. Two spoken lines that framed handoff as a Skill were also reverted: the
    new-chat bridge no longer promises "the first Skill I will show you", and the handoff notes now
    say "the first discipline in the talk that I run often enough to have packaged".
121. **Rotate the chalkboard storage key to orphan rehearsal ink.** (2026-07-27.) The persisted
    chalkboard key becomes `2026-coding-with-ai-v2-chalkboard-r2`. Ink is keyed to slide h/v/f
    indices, all of which moved in decisions 112-118, so the rehearsal drawings would have
    reattached to the wrong slides. Rotating the key in `index.html` clears it on every device he
    presents from, including the iPad, which no browser-side clearing from a desktop session could
    reach. Rotate it again after any future reorder.
122. **The public Skills repo goes on the shelf slide, and the private-repo line is retired.**
    (2026-07-27.) `github.com/Kerrator/skills` is live and public (five Skills, initial commit
    `d8760f2`), so the promise the deck was already making is now true. On "One shelf, under version
    control" (h21/v1, leaf 38): a locally generated QR (`assets/qr-skills.svg`, `qrencode -t SVG -m 4`,
    quiet zone to spec, generator comment stripped) sits to the **right of the bullets**, not below
    them, so it spends horizontal space the slide had spare; the URL is a full-width right-aligned
    line under it. A first attempt put the URL in a `<figcaption>` under the QR and it clipped
    mid-word at a 132px column, so it was moved out. The take line loses its future tense
    ("Being opened to the group" → "Open to the group"), and the speaker note that said "It currently
    lives in a private repo; I am moving it into a public one" now speaks the address and flags that
    three of the five are adapted from someone else's openly licensed set, matching the repo's own
    Origin column. No new slides, no spine reflow, no guidepost change.
    **Decision 110's parked caveat stopped being theoretical, and is now partly mitigated.** The
    first cut left the QR and URL 6px off the content edge, and the PPTX capture came back with the
    QR sliced and the URL reading "github.com/Kerrator/skil". Measured: the section box paints past
    the viewport by 59px at the 1060 × 740 capture aspect (its content box by 38px) and more at 4:3,
    and that near-flush content sat **32px outside at 1060 × 740 and 54 units outside at 4:3** while
    the widest bullet was 122px inside at 960 × 700. The right column therefore carries a **76px inset** (`.shelf-qr` / `.shelf-url`
    `margin-right`), chosen to clear the 4:3 worst case with room to spare: it now lands 39px inside
    at the capture aspect and 16px inside at 4:3. The inset is commented in `custom.css` as
    load-bearing so a future tidy-up does not remove it. This does **not** fix decision 110 in
    general (other slides' long lines still overhang); it keeps this slide's new content out of the
    unsafe zone, which also protects the iPad.
    Measured against `main` using each slide's rendered `scrollHeight`: one value moves, this slide,
    **489 → 596** against the 700 canvas (104px headroom). The deck's worst leaves are unchanged
    from `main` and **tie at 704** (684 of content plus the 20px content-box pad, 10 top and 10
    bottom): "Same token ID,
    different meaning" (h4) and "Same prompt, different answers" (h10/v2). That agrees with decision
    119's recorded worst of 704.
    *Correction, same day:* an earlier draft of this decision claimed a single 719px leaf and
    dismissed the second 704 as font-settling noise. Both claims were wrong. They came from
    measuring leaves force-flattened to `position: static`, which inflates the figure and does not
    reproduce against the rendered slide; the flattened pass was still valid for the
    branch-vs-`main` comparison, since both sides used it, but its absolute numbers were not, and it
    should not have been written into the record over decision 119. Offline verified by request log:
    every request localhost, no external host.
    **Artifacts rebuilt** from the corrected deck: PDF 49 pages at 749.04 × 546 pt (the true print
    box, not the letter-size scroll-view fallback), guidepost bar present on 48 of 49 pages (the
    title card carries none, as it should), QR URL
    extractable from the text layer; `pdftotext` diff against the previous PDF shows changes on the
    shelf page only. PPTX 49 slides at 13462000 × 9398000 EMU (1060 × 740 pt), 49 notes slides none
    empty, one full-bleed 2119 × 1479 PNG each. Both built with a stdlib-only CDP client that waits
    for reveal's `.pdf-page` wrappers before printing, because the `--print-to-pdf` CLI route races
    that layout and silently emits the letter-size fallback.

123. **Decision 122 was re-derived end to end by a session that did not build it; three of its numbers
    were wrong and are corrected above.** (2026-07-27.) An independent challenge review re-measured
    every claim from the artifacts rather than reading the record, under stated conditions: macOS
    25.5.0, headless Chrome over a stdlib CDP client, rendered slides via `Reveal.getCurrentSlide()`
    and never force-flattened, fonts and images awaited, reveal canvas 960 × 700.
    **Held on re-derivation.** The worst leaves still tie at **704** at h4 and h10/v2, agreeing with
    decision 119; the shelf slide measures **596**; the QR and URL land **38.8px inside** at
    1060 × 740 and **16.4px inside** at true 4:3, so the 76px inset does its job at every aspect
    tested. PDF: 49 pages, MediaBox `0 0 749.03998 546` on all 49 with no second value anywhere in the
    file. PPTX: 49 slides, 49 non-empty notes, 2119 × 1479 each, `sldSz` 13462000 × 9398000 EMU.
    Slide 39's notes carry the corrected "not the whole shelf" wording. The QR decodes to
    `https://github.com/Kerrator/skills` from the SVG source, from the rendered slide pixels, and
    from the PPTX raster, with no near-miss in scheme, owner, or trailing slash.
    **Corrected.** (a) The 704 decomposition was arithmetic nonsense: the leaves carry **684** of
    content plus a **20px** pad (10 top, 10 bottom), not 694 plus 10. Line 1665 of this file already
    said 10/20 correctly, so the document contradicted itself. (b) "The widest bullet was 112px
    inside" is not reproducible at any aspect: it is **122px** at 960 × 700, 130px at true 4:3, 152px
    at the capture box. (c) The guidepost bar is on **48** of 49 PDF pages, not 49; the title card
    has none, correctly. The `custom.css` comment was also rewritten: it attached 32 and 54 to "the
    right edge of the box", when those are the overhang of the *old* 6px-inset content, and it mixed
    px with reveal units. The invariant worth keeping is that the content box overhangs by exactly
    **60 units at every aspect at or below 1.371** and 37.8 units at 1.432.
    **New, and out of this change set's scope: the PPTX raster clips text.** The `.pptx` images are a
    viewport-width capture, so decision 110's overhang paints outside the frame and is cropped. On 19
    of the 49 images, ink runs terminate exactly at the final column; on several, words are sliced
    mid-glyph ("simulated time 10¹² to**o**" on slide 44; "Quantum ESPRESSO outpu**t**" and
    "→ analyse tha**t**" on slide 23). The PDF is unaffected and carries the full text at those pages,
    and the HTML deck is what gets presented, so nothing a room sees is wrong. This is pre-existing
    (the same crop geometry is in the two earlier builds), belongs to decision 110 rather than to the
    shelf slide, and wants a decision about the fix (widen the capture, or cure the overhang globally)
    before anyone rebuilds. **Do not treat the `.pptx` as a faithful export until then.**
    **Left alone, deliberately.** The QR stays at ECC **L**. Level M encodes the same 34-byte payload
    at the same version 3, 29 × 29, 3.57 units per module, so the upgrade would be free in geometry
    and would roughly double the correctable budget; it is a real improvement and a real rebuild of
    three artifacts across two public repos, so it is a decision, not a correction.
    **Still unverified, and honestly so.** No physical device has scanned the QR off a projector or
    the iPad, and repository visibility is not observable offline.
    *Superseded the same day by decision 124:* both items left alone above were acted on, and the
    PPTX crop turned out to be a symptom of a live-deck defect rather than an exporter bug.

124. **The deck was clipping sentences off the right edge on 22 of 49 leaves at 4:3, and the cause was
    one CSS rule.** (2026-07-27.) Chasing decision 123's PPTX crop upstream found it in the deck
    itself, not the exporter. Measuring the **rendered text extents** (`Range.getClientRects()` over
    every text node, not element boxes) against the viewport: **22 of 49 leaves at 1024 × 768 and at
    960 × 700, 15 of 49 at 1060 × 740, none at 1280 × 800 or wider**, worst case 59.6px of sentence
    outside the frame. So the deck was correct on the laptop it was written on and wrong on a 4:3
    projector and on the iPad. "Quantum ESPRESSO out|put" and "→ analyse t|hat" were being cut on
    leaf 23 alone.
    **Cause.** `custom.css` set `padding: 10px 20px` on `.reveal .slides section`, which matches the
    **stack** as well as the leaf. reveal makes every section `position: absolute`, so a nested
    section's `width: 100%` resolves against the *stack's padding box*: each leaf inherited the
    stack's padding as extra width, then added its own, and the box ran up to 100 units past the
    960-unit canvas. reveal's own print stylesheet zeroes exactly this
    (`html.reveal-print .reveal .slides section { padding: 0; box-sizing: border-box }`), which is why
    the PDF was always correct and only the screen and the PPTX were not.
    **Fix:** `.reveal .slides > section.stack { padding: 0 }`. A stack is a container, not a slide.
    Re-audited at ten aspects from iPad portrait 768 × 1024 through 900 × 760, 960 × 700, 1000 × 800,
    1024 × 768, 1060 × 740, 1280 × 800, 1366 × 768, 1920 × 1080 to 2560 × 1440: **0 clipped and 0 over
    the canvas at every one**. This closes decision 110, which decision 122 could only mitigate for a
    single slide.
    **Cost, paid honestly:** the leaves are now ~40 units wider, so line breaks move on 11 of 49. One
    leaf, "Same prompt, different answers" (h10/v2), went to **729**. Trimming its wordiest table cell
    ("the exception recognizing the car has to be brought in" → "the exception: the car has to be
    brought in") let the first column stop wrapping, which collapsed three two-line rows to one line
    each: **729 → 644**. No other wording changed.
    **The 76px inset is retired.** It only ever existed to hold the QR clear of the overhang; with the
    overhang gone it left the QR stranded 78px inside. Now **20px**, matching the section's own
    20-unit side padding, so the QR and URL line up with the right margin of the body text.
    **QR regenerated at ECC M.** Level M encodes the same 34-byte payload at the same **version 3,
    29 × 29 modules, 37 including the quiet zone**, so the extra error correction is free in geometry.
    Verified by an **independent decoder** (format bits → mask → zig-zag data region → byte mode),
    not by an encoder round-trip, from the SVG source *and* from actual rendered pixels: 1024 × 768 at
    3.68 px/module, 1920 × 1080 at 5.30, the PPTX 2× capture at 7.24. Payload
    `https://github.com/Kerrator/skills`, mask 3, every time. Level Q was rejected: it bumps the symbol
    to version 4 (33 × 33), which *shrinks* the modules at a fixed render size.
    **Artifacts rebuilt.** PDF: 49 pages, MediaBox `0 0 749.03998 546` on all 49, one distinct value in
    the file, guidepost bar on 48 of 49 (the title card correctly carries none). PPTX: 49 slides, 49
    notes none empty, slide 39's note still carries "not the whole shelf"; images are now **2120 ×
    1480**, an exact 2× of the 1060 × 740 box (was 2119 × 1479). The edge audit that found the crop
    now reads **0**: images with ink in the final pixel column went **20 → 0**, and the 19 with
    clipped glyph runs went to 0. The PPTX is a faithful export again. It also grew 8.7 → 12.3 MB,
    because these captures are lossless RGB PNGs; quantizing them to a 256-colour palette would take
    it to 5.3 MB but puts visible error on antialiased text, so the size was accepted rather than
    traded for quality in a correctness fix.

125. **The workspace drill-down names what a workspace is, and the montage's first tile is
    captioned "blender".** (2026-07-28, rehearsal follow-up; amends decisions 105 and 88.) The
    "A workspace the agent can navigate" leaf (h6/v1) gains a lead line, "Your workspace: a
    Project in the web app, or a codebase on disk", and its contrast panels now carry Stephen's
    textbook example: one huge file no window can hold, versus a file per chapter section that
    the agent parses and loads selectively. The small-modules and docs-link-to-docs discipline
    moved intact into the speaker notes; the goldline takeaway is unchanged. On the builds
    montage (h26/v0) the first tile's visible caption changed from "pylatkmc" to "blender" at
    Stephen's request; the lattice glyph, the asset filename, and the speaker-note description
    of the software behind it (pylatkmc) are unchanged. Artifacts rebuilt with the recipe of
    decision 124 (PDF 49 pp at 749.04 x 546 pt; PPTX 49 slides, 2120 x 1480 captures, notes on
    all 49); audits re-passed: 0 overflow at 960 x 700, offline-clean.
