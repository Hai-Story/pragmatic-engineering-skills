---
name: pragmatic-collaboration
description: Design and coordinate parallel software development across people or explicitly authorized agents using ownership, interfaces, isolated workspaces, handoffs, and integration checks. Use for team decomposition, development handoff, or conflict resolution. Do not start agents, send messages, or create remote work merely because the task is large.
---

# Pragmatic Collaboration

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md). Use collaboration only when independent work and reduced elapsed time outweigh coordination and integration cost.

## Workflow

1. **Define the shared outcome.** Align acceptance criteria, constraints, base revision, and integration owner.
2. **Map dependencies.** Identify shared schemas, APIs, generated files, migrations, configuration, and tests. A shared contract is a dependency even when implementation files differ.
3. **Partition by ownership.** Give each workstream a coherent result and explicit files or modules. Assign one owner to shared artifacts or define a merge order.
4. **Choose isolation.** Use separate branches or worktrees when concurrent edits would collide. Confirm that uncommitted changes are not automatically present in another worktree.
5. **Define handoffs.** Specify inputs, outputs, decisions, verification, and known limits using the shared [handoff record](../pragmatic-engineering/references/handoff.md).
6. **Set integration gates.** Agree on contract checks, merge order, conflict ownership, and final system verification.
7. **Reconcile evidence.** Integrate against the intended base, inspect combined behavior, and rerun checks affected by the combination.

## Workstream format

```markdown
### <workstream>
- Owner:
- Outcome:
- Owned areas:
- Shared contracts:
- Depends on / blocks:
- Verification:
- Handoff artifact:
```

Do not label tasks independent when both can change the same contract. Do not create parallel workstreams for tightly coupled edits that one person can complete faster and more safely. Planning collaboration does not itself authorize agent creation, external messages, commits, or remote changes.
