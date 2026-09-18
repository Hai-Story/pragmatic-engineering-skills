---
name: pragmatic-feasibility
description: Evaluate whether a software requirement or technical approach is viable, compare implementation paths, and test the highest-risk assumptions. Use for architecture choices, dependency evaluation, compatibility questions, cost or operational constraints, and proof-of-concept work. Do not turn advisory analysis into a full product implementation.
---

# Pragmatic Feasibility

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md). Base conclusions on the actual repository, versioned documentation, measurements, or a bounded experiment.

## Workflow

1. **Define the decision.** State the outcome, hard constraints, decision deadline, and what evidence would change the choice.
2. **Inspect the baseline.** Map current architecture, supported versions, deployment model, team skills, existing dependencies, and operational limits.
3. **Identify the risky unknowns.** Prioritize constraints that could invalidate an option: offline operation, data residency, latency, migration, licensing, rate limits, authentication, or platform support.
4. **Compare realistic options.** Include the current approach when it is viable. Compare only dimensions that affect the decision.
5. **Probe before debating.** Use the smallest experiment that can resolve the highest-risk unknown. Keep prototypes isolated and state what they do not prove.
6. **Recommend conditionally.** Name the preferred option, evidence, tradeoffs, prerequisites, exit criteria, and fallback.

## Decision table

| Option | Fits constraints | Evidence | Delivery cost | Operating cost | Risks | Reversibility |
| --- | --- | --- | --- | --- | --- | --- |

Distinguish verified facts, reasonable inferences, and unavailable information. Do not fabricate service pricing, benchmark results, account access, or compatibility. If no option is currently viable, say which constraint blocks each one and propose the next cheapest evidence-gathering step.

Hand an accepted direction to [pragmatic-planning](../pragmatic-planning/SKILL.md). A prototype is evidence, not automatically production code.
