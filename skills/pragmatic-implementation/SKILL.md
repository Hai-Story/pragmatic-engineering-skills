---
name: pragmatic-implementation
description: Implement a clear software change or behavior-preserving refactor in an existing repository while following local conventions and performing proportionate verification. Use when the requested behavior is known. Route unexplained failures to pragmatic-debugging, read-only assessment to pragmatic-review, and Git commits to pragmatic-commits.
---

# Pragmatic Implementation

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md). Deliver the requested behavior with the smallest coherent change that fits the codebase.

## Workflow

1. **Inspect before editing.** Read repository instructions, relevant implementation, neighboring patterns, tests, and current Git state. Identify changes you do not own.
2. **Confirm the contract.** Restate the behavior and acceptance criteria internally. Resolve only the unknowns that affect correctness.
3. **Choose a narrow design.** Reuse an established pattern when it fits. Add abstraction when it reduces demonstrated duplication or isolates a real boundary.
4. **Change one coherent path.** Keep edits tied to the requested behavior. Preserve compatible interfaces unless the requirement explicitly changes them.
5. **Handle boundaries.** Validate input, failure behavior, authorization, data changes, and cleanup where the feature crosses those boundaries.
6. **Add meaningful tests.** Cover changed behavior and credible regression risk. Do not add tests that merely repeat implementation or test framework behavior.
7. **Run focused checks.** Start with the closest tests or static checks, then broaden when the change surface or repository policy justifies it.
8. **Review the final diff.** Remove accidental edits, debug output, stale comments, secrets, generated noise, and unrequested formatting.

If a check fails for an unknown reason, stop speculative edits and use [pragmatic-debugging](../pragmatic-debugging/SKILL.md). If adjacent old code violates a practice, apply the classification in the working agreement: fix it only when it is necessary or already authorized; otherwise report a located recommendation.

Report the behavior changed, key files, verification and results, and remaining limits. Do not imply a commit, push, deployment, or production change unless it occurred.
