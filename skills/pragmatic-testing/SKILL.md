---
name: pragmatic-testing
description: Design and execute risk-based verification for software changes, including regression, integration, contract, and end-to-end tests. Use when acceptance coverage, test implementation, or observed validation is needed. Do not add mechanical tests for behavior-free edits or treat a test infrastructure error as a meaningful red test.
---

# Pragmatic Testing

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md). Tests should provide decision-relevant evidence, not maximize counts.

## Workflow

1. **Identify the claim.** Map acceptance criteria and changed behavior to risks: wrong result, broken contract, lost data, permission leak, race, compatibility, or unusable UI.
2. **Inspect existing coverage.** Understand the framework, fixtures, test boundaries, naming, and CI commands before adding tests.
3. **Choose the lowest sufficient level.** Use unit tests for local rules, integration tests for boundaries, contract tests for shared interfaces, and end-to-end tests for critical user journeys.
4. **Create a valid failure signal.** For a regression test, confirm the old behavior fails because of the target defect. Import errors, missing fixtures, and broken setup show an invalid test environment.
5. **Implement stable assertions.** Assert observable behavior. Control nondeterminism at system boundaries and avoid overspecifying private implementation.
6. **Exercise important alternatives.** Include boundaries, empty states, failure paths, permissions, and migration behavior in proportion to risk.
7. **Run and interpret.** Record the command, result, relevant environment, and revision. Investigate flaky or unexpected failures rather than hiding them with retries.
8. **State the coverage limit.** Explain what the run proves and what remains untested.

For UI tests, wait on observable readiness or the expected result. Long polling or background traffic can make “network idle” permanently false. Derive selectors from the real UI and prefer accessible roles, labels, and stable test identifiers.

Re-run checks affected by later code changes. Do not reuse a stale passing result as evidence for a different revision.
