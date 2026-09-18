---
name: pragmatic-review
description: Review existing code, diffs, pull requests, commits, or review feedback for correctness, requirement fit, and material engineering risk. Use for read-only assessment and for checking whether a proposed review comment is valid. Prioritize located, evidence-backed findings; do not treat personal style or unrelated debt as a required fix.
---

# Pragmatic Review

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md). Review is read-only unless the user also asks for fixes. For a best-practice audit or a claim based on DRY, SOLID, YAGNI, Agile, TDD, or another named philosophy, also read the [practice selection guide](../pragmatic-engineering/references/practices.md).

## Workflow

1. **Establish the review target.** Identify the diff or files, intended behavior, base revision, repository rules, and requested review dimensions.
2. **Understand the change.** Trace relevant execution paths, data contracts, state changes, authorization, failure handling, and tests. Do not review only filenames or isolated lines.
3. **Test risky claims.** Run focused checks or construct small examples when they materially improve confidence. Distinguish observed failures from plausible concerns.
4. **Classify deviations.** Use defect, project-rule violation, contextual risk, or optional improvement from the working agreement. Translate philosophy labels into a local objective and observable impact; the label alone is not a finding.
5. **Prioritize findings.** Rank by user impact and likelihood. Combine repeated symptoms that share one cause.
6. **Verify feedback before accepting it.** Check reviewer claims against code, requirements, measurements, and tradeoffs. Explain respectful disagreement with evidence.

## Finding format

Each actionable finding should include:

- **Location:** the tightest useful file and line range or component.
- **Impact:** the observable failure or concrete risk.
- **Evidence:** the code path, requirement, test, or measurement.
- **Recommendation:** the smallest change that addresses the cause.
- **Verification:** how to prove the correction.
- **Priority:** blocker, high, medium, or low based on impact and likelihood.

Do not invent the commit that introduced a problem. Do not require a new abstraction, cache, test, or rewrite without showing the risk it addresses. Follow the project's valid naming and style rules even when another convention is more common.

Lead with findings. If there are none, say so and state the reviewed scope and testing limits.
