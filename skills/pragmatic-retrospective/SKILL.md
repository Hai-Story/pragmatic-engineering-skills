---
name: pragmatic-retrospective
description: Extract evidence-backed engineering lessons from real commits, pull requests, incidents, defects, and user feedback, then propose bounded improvements to code, process, or this skill suite. Use after meaningful delivery or failure. Do not invent project history or turn one anecdote into a universal rule.
---

# Pragmatic Retrospective

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md) and the [practice selection guide](../pragmatic-engineering/references/practices.md).

## Workflow

1. **Collect evidence.** Use actual diffs, tests, timelines, logs, review comments, incidents, and outcomes. Remove or redact secrets and personal data.
2. **Separate fact from interpretation.** State what happened, what is inferred, and what remains unknown.
3. **Find the mechanism.** Identify the condition and decision that allowed the outcome. Avoid blaming an individual or naming a tool without causal evidence.
4. **Assess recurrence and impact.** Determine whether this is a one-off, a repeated pattern, or a low-frequency high-impact risk.
5. **Propose the smallest improvement.** Choose among code change, test, automation, documentation, review checklist, training, or no systemic action.
6. **Define applicability.** State when the lesson applies, legitimate exceptions, maintenance cost, and how to evaluate it.
7. **Promote carefully.** Update shared guidance only when evidence justifies the broader rule and the current task authorizes that edit.

## Lesson format

```markdown
### Observation
### Evidence
### Contributing conditions
### Proposed change
### Applies when
### Exceptions
### Verification and review date
```

One timeout does not prove every write must become idempotent. One style disagreement does not justify a global lint rule. Prefer automation for objective repeated checks and prose for decisions that require context.
