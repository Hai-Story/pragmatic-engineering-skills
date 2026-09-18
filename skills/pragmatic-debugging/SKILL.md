---
name: pragmatic-debugging
description: Diagnose and fix software defects, failing tests, build failures, unexpected behavior, and performance regressions through reproduction and hypothesis testing. Use when the cause is unknown. Do not substitute repeated speculative edits or broad refactoring for diagnosis.
---

# Pragmatic Debugging

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md). The goal is the smallest explanation that accounts for the evidence and a fix that removes the cause without unrelated change.

## Workflow

1. **Define expected and observed behavior.** Capture the exact input, environment, version, output, frequency, and impact. Separate symptoms from inferred causes.
2. **Reproduce safely.** Use the smallest reliable case. Preserve current work and avoid destructive experiments against production data.
3. **Inspect the path.** Follow data and control flow across the failing boundary. Read logs, tests, configuration, recent relevant changes, and dependency versions without exposing secrets.
4. **Form ranked hypotheses.** Each hypothesis must explain the observations and have a discriminating check. Start with the cheapest high-information experiment.
5. **Change one variable.** Run the check, record the outcome, and update the hypothesis. Avoid accumulating guesses in the code.
6. **Identify the cause.** Show why the cause produces the symptom and why competing explanations do not fit the evidence.
7. **Fix narrowly.** Correct the responsible contract, state transition, calculation, or boundary. Avoid masking the symptom with retries, catches, or special cases unless those are the intended design.
8. **Verify the regression.** Demonstrate the original failure before the fix when practical, then run focused and relevant broader checks.
9. **Review collateral risk.** Check nearby paths that share the cause, and report limitations.

If reproduction is impossible, state what was attempted and add the least intrusive observation needed to distinguish hypotheses. Do not claim a root cause from correlation alone.

Report the symptom, reproduction, root cause, change, verification, and residual risk. Hand additional coverage to [pragmatic-testing](../pragmatic-testing/SKILL.md) when useful.
