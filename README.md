# Pragmatic Engineering Skills

**Evidence-driven software engineering workflows for AI coding agents.**

Pragmatic Engineering Skills helps an agent move from an ambiguous request to a verified change without forcing every task through the same ceremony. The suite covers requirements, feasibility, planning, implementation, testing, debugging, review, Git commits, collaboration, and retrospectives.

Its defining rule is simple: apply a practice because the project evidence supports it, not because a generic checklist says so.

## Why this project

Coding agents often fail in two opposite ways. They rush into code without establishing the contract, or they impose a heavyweight process on a small change. This suite teaches an agent to choose the smallest useful workflow, respect local conventions, preserve existing work, and make completion claims only when current evidence supports them.

When existing code differs from a recommended practice, the agent classifies the issue before suggesting a change:

- **Defect:** observable incorrect behavior, exposure, data loss, or broken acceptance.
- **Project-rule violation:** conflict with documented or automated repository policy.
- **Contextual risk:** a concrete risk under stated project conditions.
- **Optional improvement:** a preference or cleanup with limited demonstrated impact.

Every actionable recommendation should include a location, impact, evidence, smallest useful change, and verification method.

The suite also provides a [development philosophy map](skills/pragmatic-engineering/references/development-philosophies.md). It helps agents choose among approaches such as iterative delivery, formal methods, DDD, TDD, DRY, KISS, YAGNI, SOLID, secure by design, and Twelve-Factor without combining them into a contradictory checklist.

## Skill catalog

| Skill | Use it for |
| --- | --- |
| [`pragmatic-engineering`](skills/pragmatic-engineering/SKILL.md) | Route an end-to-end or multi-stage development task |
| [`pragmatic-requirements`](skills/pragmatic-requirements/SKILL.md) | Turn an ambiguous request into testable requirements |
| [`pragmatic-feasibility`](skills/pragmatic-feasibility/SKILL.md) | Compare technical paths and test risky assumptions |
| [`pragmatic-planning`](skills/pragmatic-planning/SKILL.md) | Build an executable plan with dependencies and checks |
| [`pragmatic-implementation`](skills/pragmatic-implementation/SKILL.md) | Implement a focused feature, fix, or refactor |
| [`pragmatic-testing`](skills/pragmatic-testing/SKILL.md) | Design and run risk-based verification |
| [`pragmatic-debugging`](skills/pragmatic-debugging/SKILL.md) | Reproduce, diagnose, and fix unexpected behavior |
| [`pragmatic-review`](skills/pragmatic-review/SKILL.md) | Review code or feedback for material, located risks |
| [`pragmatic-commits`](skills/pragmatic-commits/SKILL.md) | Prepare or create coherent Git commits safely |
| [`pragmatic-collaboration`](skills/pragmatic-collaboration/SKILL.md) | Partition parallel work and define integration gates |
| [`pragmatic-retrospective`](skills/pragmatic-retrospective/SKILL.md) | Turn real project evidence into bounded improvements |

## Quick start

Clone or download the repository and open its root. The checked-in `.agents/skills` link exposes the canonical `skills/` directory to Codex without duplicating files.

To use the skills in another repository, copy the complete suite so specialist skills retain their shared references:

```bash
mkdir -p /path/to/your-project/.agents/skills
cp -R /path/to/pragmatic-engineering-skills/skills/. /path/to/your-project/.agents/skills/
```

Then ask naturally or invoke a skill explicitly:

```text
Use $pragmatic-engineering to implement order export and verify the result.

Use $pragmatic-review to review the current diff. Report findings only; do not edit code.

Use $pragmatic-commits to propose commit boundaries and messages. Do not commit yet.
```

The repository includes both a portable [`plugin.json`](plugin.json) and the Codex-compatible [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json). This makes the suite ready for local plugin testing and later public plugin submission. See the official [skill authoring](https://learn.chatgpt.com/docs/build-skills) and [plugin packaging](https://learn.chatgpt.com/docs/build-plugins) documentation for current host behavior.

## Design principles

- **Proportional process.** Use only the stages that reduce real uncertainty or risk.
- **Local evidence first.** Repository rules, current code, tests, and versioned docs outrank generic advice.
- **Philosophies are lenses.** Select a principle for a demonstrated problem and state its counter-pressure.
- **Advice with impact.** Explain why a deviation matters before recommending a change.
- **Preserved user intent.** Do not discard unrelated edits or disturb a mixed Git index.
- **Fresh verification.** Tie completion claims to checks that cover the final relevant change set.
- **Portable instructions.** Core behavior lives in standard `SKILL.md` files with no external runtime dependency.

More detail is available in [Design](docs/design.md) and [Evaluation](docs/evaluation.md).

## Validation

The repository uses only the Python standard library for its own validation:

```bash
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -v
```

Validation checks skill metadata, shared dependencies, local links, UI metadata, plugin manifests, English-only public skill content, and evaluation case references. Behavioral fixtures provide review-only and debugging smoke tests; they are intentionally reported separately from structural validation.

## Sources and attribution

The workflow was informed by high-quality public skill repositories and established engineering references, including [Nature Skills](https://github.com/Yuan1z0825/nature-skills), [Superpowers](https://github.com/obra/superpowers), [Spec Kit](https://github.com/github/spec-kit), [Anthropic Skills](https://github.com/anthropics/skills), [OpenAI Skills](https://github.com/openai/skills), [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills), [Addy Osmani's Agent Skills](https://github.com/addyosmani/agent-skills), [Software Development Best Practices](https://github.com/dronezzzko/software-development-best-practices), the [software development philosophies index](https://en.wikipedia.org/w/index.php?title=List_of_software_development_philosophies&oldid=1374272361), [Git Best Practices](https://sethrobertson.github.io/GitBestPractices/), and [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

The project adopts workflow ideas and writes its own instructions. It does not bundle third-party skills. See [source review](research/source-review.md) for what was adopted, changed, or rejected.

## Contributing

Contributions are welcome when they improve observable agent behavior. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a skill or changing a workflow. New rules need a concrete failure mode, applicability conditions, exceptions, and a way to evaluate them.

## License

[MIT](LICENSE)
