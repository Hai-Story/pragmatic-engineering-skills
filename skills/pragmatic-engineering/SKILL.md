---
name: pragmatic-engineering
description: Route end-to-end software development work through the smallest useful set of requirements, feasibility, planning, implementation, testing, debugging, review, Git, collaboration, and retrospective workflows. Use for multi-stage engineering tasks, broad practice audits, or when the right specialist skill is unclear. Do not use for non-development work or force every stage onto a bounded task.
---

# Pragmatic Engineering

Apply engineering discipline in proportion to the task. Start by reading the [working agreement](references/working-agreement.md). Reuse it for the rest of the task unless it changes.

## Route the work

| Situation | Skill | Expected result |
| --- | --- | --- |
| Goal, scope, behavior, or acceptance is unclear | [pragmatic-requirements](../pragmatic-requirements/SKILL.md) | Testable requirements and open decisions |
| Technical path, dependency, compatibility, or cost is uncertain | [pragmatic-feasibility](../pragmatic-feasibility/SKILL.md) | Evidence-backed options and conditions |
| A multi-step change needs sequencing and ownership | [pragmatic-planning](../pragmatic-planning/SKILL.md) | Executable tasks with dependencies and checks |
| The requested behavior is clear enough to build | [pragmatic-implementation](../pragmatic-implementation/SKILL.md) | Focused code changes and verification |
| The task needs a test strategy, test code, or acceptance run | [pragmatic-testing](../pragmatic-testing/SKILL.md) | Risk-based coverage and observed results |
| Something fails or behaves unexpectedly | [pragmatic-debugging](../pragmatic-debugging/SKILL.md) | Reproduction, cause, fix, and regression evidence |
| Existing code, a diff, a PR, or review feedback needs assessment | [pragmatic-review](../pragmatic-review/SKILL.md) | Prioritized, located findings with rationale |
| Git changes need organizing, committing, or history guidance | [pragmatic-commits](../pragmatic-commits/SKILL.md) | Safe commit boundaries, messages, and status |
| People or authorized agents need parallel work boundaries | [pragmatic-collaboration](../pragmatic-collaboration/SKILL.md) | Ownership, interfaces, integration order, and handoffs |
| Real project evidence should improve the workflow | [pragmatic-retrospective](../pragmatic-retrospective/SKILL.md) | A bounded lesson with evidence and exceptions |

Choose only the stages that resolve the current uncertainty. A one-line copy fix may need implementation and a focused check. A new cross-service feature may need requirements, feasibility, planning, implementation, testing, and review. A read-only review does not need a specification first.

## Keep stages connected

- State the selected path in one sentence, then continue the work already authorized.
- Carry forward the objective, constraints, acceptance criteria, repository rules, decisions, and evidence. Use the [handoff record](references/handoff.md) for long or multi-session work.
- Move from implementation to debugging when observed behavior contradicts expectations.
- Record relevant out-of-scope problems as recommendations. Do not turn one task into an unrequested repository-wide cleanup.
- Treat a plan as a means to delivery. When the user requested implementation, continue past planning without asking them to repeat the instruction.
- Treat commit, push, deployment, production writes, and shared-history rewrites as distinct actions with distinct authorization.

## Judge completion

For each acceptance criterion, report one of: completed and verified, completed but not verified, pending a decision, or blocked. Tie claims to current evidence. A passing formatter does not prove behavior; an old test run does not cover code changed afterward.

Load the [practice selection guide](references/practices.md) only when judging a practice or proposing a new rule. Load [Git practices](references/git-practices.md) for commit or history work.
