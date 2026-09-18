# Repository Guide for Coding Agents

This file governs work on the Pragmatic Engineering Skills repository itself. It is not part of the reusable workflow installed into other projects.

## Repository purpose

The public product is the set of portable skills under `skills/`. Each skill must improve observable software engineering behavior while remaining useful across languages and frameworks.

## Change rules

- Write all public repository content in English.
- Keep each skill name equal to its directory name and use lowercase kebab case.
- Put trigger conditions and exclusions in frontmatter descriptions.
- Keep the router thin. Put specialist instructions in the corresponding `pragmatic-*` skill.
- Reuse shared policy from `skills/pragmatic-engineering/references/` rather than duplicating it.
- Treat external practice guides as sources to evaluate, not rules to copy wholesale.
- Preserve source attribution in `research/` when a change draws on public work.
- Add or update an evaluation case when changing a trigger, permission boundary, completion claim, or material workflow decision.
- Do not add a dependency when a standard-library check is sufficient.

## Required validation

Run before declaring a repository change complete:

```bash
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -v
```

When behavior changes, run or add the smallest representative behavioral fixture and report its limits. Structural validation does not prove that an agent will follow the skill correctly.

## Pull request expectations

Explain the behavior problem, the resulting skill behavior, evidence used, and validation performed. Keep unrelated formatting or wording out of focused changes.
