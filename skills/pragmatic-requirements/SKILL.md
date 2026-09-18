---
name: pragmatic-requirements
description: Turn a software idea, change request, or ambiguous task into bounded, testable requirements. Use when user outcomes, scope, actors, edge cases, acceptance criteria, or business decisions are unclear. Do not restart requirements analysis for a well-specified local fix or make technical architecture choices that belong in feasibility work.
---

# Pragmatic Requirements

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md). Produce enough clarity to make the next decision or start delivery; do not generate a large specification by default.

## Workflow

1. **Inspect existing truth.** Read the request, relevant product docs, current behavior, tests, interfaces, and terminology before asking questions.
2. **State the outcome.** Describe who needs what observable result and why. Separate the user outcome from a proposed implementation.
3. **Bound the scope.** List included behavior, excluded behavior, affected actors or systems, and compatibility expectations.
4. **Model behavior.** Cover the happy path, important alternatives, validation, permissions, empty states, failures, and data lifecycle where relevant.
5. **Write acceptance criteria.** Make each criterion observable and independently verifiable. Use examples when rules contain dates, money, ordering, pagination, or state transitions.
6. **Resolve unknowns intelligently.** Inspect the repository first. Ask only for business choices that cannot be inferred or tested. State a reversible assumption when it permits useful progress.
7. **Check readiness.** Requirements are ready when implementation and test planning can distinguish success from failure without inventing product behavior.

## Output

Use this compact structure unless the project already has a template:

```markdown
## Outcome
## Actors and context
## In scope
## Out of scope
## Behavior and rules
## Acceptance criteria
## Constraints
## Assumptions and open decisions
```

Flag conflicts between the requested behavior and the current product. Do not invent throughput, availability, retention, security, or compliance targets. Hand technical uncertainty to [pragmatic-feasibility](../pragmatic-feasibility/SKILL.md) and multi-step delivery to [pragmatic-planning](../pragmatic-planning/SKILL.md).
