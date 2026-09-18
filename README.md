# Pragmatic Engineering Skills

Software has become much easier to start building. With an AI coding agent, a founder, designer, researcher, or domain expert can turn an idea into a working application without first spending years as a software engineer.

That is a good change. It also creates a new problem: generating code is easier than knowing whether the code is ready to depend on.

Software teams have spent decades learning how to clarify requirements, test risky behavior, diagnose failures, review changes, preserve useful history, and work together without losing each other's work. Those lessons should not disappear just because the person directing the work is new to programming—or because an agent is writing the code.

Pragmatic Engineering Skills packages those lessons as a set of reusable skills for coding agents. The goal is not to turn every change into a formal process. It is to help the agent use the right amount of engineering discipline for the job in front of it.

## What changes when you use it

A coding agent can produce a plausible implementation quickly. This suite teaches it to pause where judgment matters:

- A vague feature request becomes a small set of testable outcomes before code is changed.
- A technical choice is checked against the project's actual constraints instead of justified with a fashionable pattern.
- A failure is reproduced and investigated before fixes are guessed.
- Existing code is not called “bad” merely because it differs from a general recommendation.
- Tests are chosen for the risks in the change, and completion claims are tied to checks that actually ran.
- Git commits are prepared around coherent changes while unrelated work is left alone.

When the codebase does differ from a recommended practice, the agent first decides what kind of issue it has found: a defect, a violation of a documented project rule, a risk that matters in this project, or an optional improvement. That distinction keeps style preferences from being reported as bugs.

The suite also includes a [development philosophy guide](skills/pragmatic-engineering/references/development-philosophies.md). It helps the agent use ideas such as DRY, KISS, YAGNI, SOLID, TDD, DDD, secure by design, iterative delivery, and Twelve-Factor in context. These ideas solve different problems and sometimes pull in different directions; they are more useful as lenses than as a single checklist.

## How it is organized

Start with `pragmatic-engineering` when a task may cross several stages. It acts as a small router and selects only the specialist skills the work needs. Each specialist can also be used on its own.

| Skill | What it helps with |
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
| [`pragmatic-collaboration`](skills/pragmatic-collaboration/SKILL.md) | Divide parallel work and define integration checks |
| [`pragmatic-retrospective`](skills/pragmatic-retrospective/SKILL.md) | Turn project evidence into practical improvements |

The skills share a small set of references for scope, evidence, engineering practices, development philosophies, Git history, and handoffs. Keeping that policy in one place prevents the same rule from drifting across several prompts.

## Try it in a project

Clone or download this repository, then copy the complete suite into the skills directory used by your coding agent. For a project that discovers skills from `.agents/skills`:

```bash
mkdir -p /path/to/your-project/.agents/skills
cp -R /path/to/pragmatic-engineering-skills/skills/. /path/to/your-project/.agents/skills/
```

Copying the whole `skills/` directory matters because the specialist skills use shared references from `pragmatic-engineering`.

You can ask for the router in ordinary language:

```text
Use $pragmatic-engineering to add order export and verify the result.
```

Or call a specialist when the task is already clear:

```text
Use $pragmatic-review to review the current diff. Report findings only; do not edit code.

Use $pragmatic-debugging to reproduce this intermittent test failure and find its cause.

Use $pragmatic-commits to propose commit boundaries and messages. Do not commit yet.
```

The repository includes a portable [`plugin.json`](plugin.json), host-specific [plugin metadata](.codex-plugin/plugin.json), and per-skill metadata under `agents/`. The skills themselves are plain Markdown and do not require a runtime dependency.

## The principles behind the suite

The repository favors evidence over ceremony. Local instructions, current code, tests, and versioned documentation come before generic advice. Process grows only when it reduces uncertainty or protects something that matters. Recommendations explain their impact and include a practical way to verify the change.

The suite also treats permission and history as part of engineering correctness. Editing code, creating a commit, pushing a branch, and deploying a release are separate actions. A useful agent should know the difference and report what actually happened.

For the architecture and the reasoning behind these boundaries, read [Design](docs/design.md). For the current evaluation approach and its limits, read [Evaluation](docs/evaluation.md).

## Validation

The repository has no third-party validation dependency. Run the same checks used in CI with Python 3.11 or newer:

```bash
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -v
```

These checks cover metadata, shared dependencies, links, manifests, English-only public skill content, and evaluation case references. Behavioral fixtures are reported separately because a valid package does not prove that an agent will follow its instructions well.

## Sources

This project was informed by public skill repositories and established engineering references, including [Nature Skills](https://github.com/Yuan1z0825/nature-skills), [Superpowers](https://github.com/obra/superpowers), [Spec Kit](https://github.com/github/spec-kit), [Anthropic Skills](https://github.com/anthropics/skills), [OpenAI Skills](https://github.com/openai/skills), [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills), [Addy Osmani's Agent Skills](https://github.com/addyosmani/agent-skills), [Software Development Best Practices](https://github.com/dronezzzko/software-development-best-practices), the [software development philosophies index](https://en.wikipedia.org/w/index.php?title=List_of_software_development_philosophies&oldid=1374272361), [Git Best Practices](https://sethrobertson.github.io/GitBestPractices/), and [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

Pinned revisions, licenses, and retrieval records are kept in [`research/sources.json`](research/sources.json). External work is used as evidence and inspiration; third-party skills and templates are not redistributed here.

## Contributing

Contributions are welcome when they improve observable behavior in real software projects. Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding a skill or changing a workflow. A new rule should name the problem it prevents, where it applies, where it does not, and how someone can tell whether it worked.

## License

[MIT](LICENSE)
