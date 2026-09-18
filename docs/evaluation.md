# Evaluation

Skill quality has three layers. Keep their claims separate.

## 1. Packaging validation

`scripts/validate_suite.py` checks metadata, names, links, shared dependencies, UI metadata, manifests, public-language policy, and evaluation references. Unit tests prove that common broken packages are rejected.

This layer can show that the repository is structurally coherent. It cannot show that an agent will choose or follow a skill correctly.

## 2. Behavioral scenarios

`evals/cases.json` defines positive triggers, negative triggers, expected behaviors, and forbidden behaviors. A useful scenario has a concrete request and a result that a reviewer can distinguish from plausible but incorrect behavior.

Run a scenario in a clean conversation or isolated workspace. Record:

- host, model, and relevant settings;
- exact skills made available or invoked;
- prompt and fixture revision;
- output and file changes;
- grader decision against every criterion;
- unexpected behavior and limitations.

## 3. Comparative evaluation

Claims that a skill improves quality require a baseline, repeated trials, equivalent starting state, and a documented grader. Track routing accuracy, task success, scope violations, unsupported claims, and unnecessary ceremony separately. Do not compress different failure types into one flattering score.

The current repository includes two independent smoke trials and a broader scenario catalog. It does not yet establish a statistically meaningful quality improvement over unskilled agents.
