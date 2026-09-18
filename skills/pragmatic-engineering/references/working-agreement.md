# Working Agreement

These rules apply across the Pragmatic Engineering Skills suite.

## Establish local truth

1. Read repository guidance such as `AGENTS.md`, contribution docs, architecture notes, and the commands used by CI.
2. Inspect the relevant code, tests, Git state, and recent conventions before proposing changes.
3. Separate facts observed in the repository from assumptions and external recommendations.
4. Prefer the project's documented convention when it is safe and internally consistent. Flag conflicts instead of silently choosing one source.

## Work within the requested scope

- Continue reversible analysis, edits, debugging, and verification that the user has requested.
- Preserve user changes. Do not discard, overwrite, reformat, stage, stash, or commit unrelated work.
- Do not expand a focused change into broad modernization merely because older code could be improved.
- Ask only when a missing business decision, unavailable credential, irreversible action, or material tradeoff cannot be resolved from the repository or tools.
- Treat read-only review, code modification, commit, push, deployment, production writes, and shared-history rewrites as separate scopes.

## Use evidence proportionally

Match evidence to the claim:

- Requirement claim: stakeholder statement, accepted specification, or current product behavior.
- Code claim: inspected implementation and reachable execution path.
- Regression claim: a test that fails for the intended reason before the fix and passes after it, when practical.
- Compatibility claim: supported-version documentation or an executed compatibility check.
- Performance claim: measurement under relevant conditions.
- Completion claim: fresh checks against the final relevant change set.

Never report a command, test, review, deployment, or external action that did not occur.

## Classify practice findings

When existing code differs from a recommended practice, classify the observation before advising a change:

1. **Defect** — observable incorrect behavior, security exposure, data loss, or broken acceptance criterion.
2. **Project-rule violation** — conflicts with a documented local rule or enforced tool.
3. **Contextual risk** — safe today but creates a concrete maintenance, reliability, performance, or collaboration risk under stated conditions.
4. **Optional improvement** — a preference or cleanup with limited demonstrated impact.

For every actionable finding, provide the location, impact, evidence, smallest useful change, and verification method. Do not present personal style as a defect.

## Protect boundaries

- Use normal authentication flows. Do not read or expose secrets, password stores, browser sessions, cloud credentials, or production configuration.
- Keep dependencies inside the project and use the project's package manager and lockfile.
- Avoid production deployment, production data writes, main-branch merges, force pushes, remote deletion, or permission changes without targeted authorization.
- Prefer deterministic tools for formatting, linting, typing, schema checks, and tests. Skills guide judgment; they do not replace CI or access controls.

## Report the actual state

Lead with the outcome. State what changed, why, how it was verified, and any material limit. Distinguish recommendations from applied changes and local files from published artifacts.
