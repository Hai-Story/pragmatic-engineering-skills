---
name: pragmatic-planning
description: Convert clear software requirements and a chosen approach into executable implementation tasks with dependencies, target areas, ownership, and verification. Use for cross-module features, migrations, integrations, or complex refactors. Skip a separate plan document for a small, obvious change.
---

# Pragmatic Planning

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md). A useful plan lets another engineer execute the work without rediscovering critical decisions.

## Workflow

1. **Confirm inputs.** Capture the outcome, acceptance criteria, constraints, chosen approach, and remaining unknowns. Do not silently repair a product decision inside the plan.
2. **Inspect change surfaces.** Identify current files, components, interfaces, tests, migrations, docs, and operational paths. Mark proposed paths as proposed.
3. **Expose contracts first.** Put unresolved schemas, API behavior, state transitions, and shared types before tasks that depend on them.
4. **Slice by observable behavior.** Prefer coherent vertical increments. Each task should have one outcome, concrete inputs and outputs, affected areas, and a check.
5. **Order dependencies.** Mark tasks as sequential, parallel after a contract, or independent. Include migration, rollback, feature flags, and compatibility steps when relevant.
6. **Map acceptance to verification.** Every acceptance criterion needs a planned check. Add integration or end-to-end checks at boundaries that unit tests cannot prove.
7. **Review scope.** Remove speculative abstractions, unrelated cleanup, duplicate checks, and tasks that only restate a phase name.

## Task format

```markdown
### <task>: <observable result>
- Depends on:
- Target areas:
- Change:
- Acceptance covered:
- Verification:
- Risks or rollback:
```

Call out user decisions separately from engineering tasks. Planning collaboration does not authorize starting agents, creating tickets, changing Git history, or sending messages. When implementation was requested, proceed into [pragmatic-implementation](../pragmatic-implementation/SKILL.md) after the plan is sufficient.
