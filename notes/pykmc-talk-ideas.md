# pyKMC talk ideas

Parked material for a future pyKMC-focused talk. Moved out of *Coding with AI v2* (section 3)
during the 2026-07-14 section interview because it is about pyKMC's design and verification, not
about coding with an agent.

## The inner loop and the outer gate (verification ladder)

Four rungs, cheap and constant on the left, rare and decisive on the right:

1. **Local reproducer**: every iteration, reduced system, small fixtures.
2. **Reduced integration case**: before handoff or commit.
3. **Original system re-run**: the failing case or a canonical example, at the phase boundary.
4. **Cluster validation**: when MPI scale, hardware, scheduler, memory, or environment matter.

Takeaway: my laptop's constraints are not the constraints of the machine where the science runs.

Terminology guard: an example-system re-run is a regression test only when it carries a pinned,
machine-checkable expectation; otherwise it is an end-to-end validation run. Both can be required;
they give different strengths of evidence.

Ready-made asset: `talks/2026-coding-with-ai-v2/assets/verification-ladder.svg` (Invisible
Variable style, four rungs with the gold outer-gate bracket).

## The HTST diagonalization story (Stephen's account)

While working on HTST, calculating a huge diagonalization failed because the laptop could not
handle the size of the system. That failure says nothing about whether the calculation fails at
scale: the same job can be fine on a cluster. The design lesson for pyKMC: if we design and test
pyKMC only within laptop constraints, we may miss what it could do on clusters. Bug fixing wants a
small sample system for the inner loop, but the outer gate has to run where the science actually
runs, at real size, with real MPI scale and memory.

This story motivates the ladder above from a real failure, and it argues that laptop-driven
development must not quietly become laptop-driven design.
