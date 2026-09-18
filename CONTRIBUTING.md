# Contributing

Thank you for improving Pragmatic Engineering Skills. The project values changes that make agent behavior more reliable in real repositories.

## Before opening a change

Search existing skills and issues first. Extend an existing workflow when the new behavior shares the same trigger and outcome. Propose a new skill when it has a distinct trigger, workflow, and deliverable.

For a material workflow change, open an issue describing:

- the failure mode or missing capability;
- a representative user request;
- the expected observable behavior;
- cases where the rule should not apply;
- how the change can be evaluated.

Small wording corrections and clear bug fixes can go directly to a pull request.

## Development setup

No third-party runtime dependency is required. Use Python 3.11 or newer:

```bash
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -v
```

## Skill quality standard

A skill contribution should:

1. Use a lowercase kebab-case name that matches its directory.
2. Describe specific positive and negative trigger conditions in frontmatter.
3. Give an executable workflow, decision rules, and a clear deliverable.
4. Distinguish project evidence from external advice.
5. State permission or scope boundaries where the workflow can change code, Git, remote systems, or external communication.
6. Avoid universal claims that lack applicability conditions and exceptions.
7. Link supporting material instead of loading all references into every task.
8. Include `agents/openai.yaml` with a short description and a default prompt that names the skill.
9. Add or update evaluation cases for material behavior.

Keep `SKILL.md` focused. Deterministic formatting, schema checks, or repetitive transformations belong in scripts when they cannot be expressed reliably as instructions.

## Evaluation

Structural checks catch packaging errors. Behavioral evaluation checks whether an agent follows the workflow in a representative task. A behavioral claim needs the prompt, fixture or repository revision, result, grader criteria, and limitations. Do not report improvement percentages without a baseline, repeated trials, and a documented grading method.

See [docs/evaluation.md](docs/evaluation.md) and [`evals/`](evals/).

## Pull requests

Keep a pull request centered on one behavior or maintenance goal. The description should state:

- the problem and trigger;
- before and after behavior;
- source or project evidence;
- validation performed;
- compatibility or migration impact.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
