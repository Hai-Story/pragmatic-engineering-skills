# Design

Pragmatic Engineering Skills is a routed suite rather than one monolithic instruction file. The router selects the smallest useful set of specialist workflows, and each specialist loads shared policy through relative references.

## Architecture

```text
pragmatic-engineering (router)
├── requirements ── feasibility ── planning
├── implementation ── testing ── debugging
├── review ── commits ── collaboration
└── retrospective

shared references
├── working agreement
├── practice selection
├── development philosophies
├── Git practices
└── handoff record
```

The specialist skills can be invoked directly. They link to shared references instead of routing back through the entry point, which prevents circular invocation and duplicated policy.

## Product position

The suite focuses on context-sensitive engineering judgment. It does not attempt to be a language framework catalog, a rigid lifecycle, or a replacement for repository automation. A team should keep deterministic rules in formatters, linters, type checkers, tests, policy tools, and CI.

The workflow is differentiated by five behaviors:

1. It scales process to uncertainty and risk.
2. It ranks local project evidence above generic advice.
3. It treats development philosophies as competing lenses with explicit counter-pressures.
4. It classifies nonconforming code before recommending changes.
5. It treats authorization and verification as part of technical correctness.

## Adding scope

Add a shared rule when several workflows need the same decision policy. Add a specialist skill when the trigger, workflow, and deliverable are distinct. Add a technology-specific reference only after a real use case establishes the version and context it must support.

Avoid overlapping skills whose only difference is wording. Avoid rules that cannot name the failure they prevent, the conditions where they apply, and a way to evaluate them.
