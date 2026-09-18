# Selecting Engineering Practices

Use practices as context-sensitive decision aids. A popular checklist is a source of candidates, not automatic authority over a repository.

When a request names a development philosophy, compares methodologies, or asks for a broad best-practice audit, read [Selecting Development Philosophies](development-philosophies.md). It separates lifecycle methods, design principles, code heuristics, deployment models, and team practices so rules from different levels are not mixed accidentally.

## Source order

Prefer evidence in this order when sources conflict:

1. Current user requirement and explicit repository policy.
2. Enforced CI, formatter, linter, type checker, schema, or test behavior.
3. Maintained official documentation for the exact language, framework, or tool version.
4. Established project convention and relevant architecture decisions.
5. Well-supported industry guidance whose assumptions match the project.
6. Personal preference.

Record why a lower-ranked source should override a higher-ranked one when that is necessary for safety or correctness.

## Evaluate a proposed rule

Before recommending or adopting a practice, answer:

- What failure or cost does it prevent?
- Under which project conditions does that failure matter?
- What evidence shows the condition exists here?
- What is the migration and maintenance cost?
- Can a deterministic tool enforce the rule more reliably than prose?
- What exceptions are legitimate?
- How will the team know whether the change helped?

Prefer a narrow rule with an objective check over a broad slogan.

## Use principles as competing lenses

Most useful principles have a counter-pressure. DRY can increase coupling, fail-fast can reduce availability, reuse can transfer ownership risk, and release speed can conflict with assurance. Select the principle that addresses the demonstrated problem, state the counter-pressure, and explain why the tradeoff fits this project.

Do not use a philosophy label as evidence. Translate it into a local objective, an observed mismatch, a material impact, and a verifiable result.

## Advise on nonconforming code

Do not rewrite code solely because it differs from an external guide. Classify it using the [working agreement](working-agreement.md), then provide:

```text
Location: file and tight line range or component
Classification: defect | project-rule violation | contextual risk | optional improvement
Observed impact: what can happen and to whom
Evidence: code path, requirement, tool output, or measurement
Recommendation: smallest useful change
Verification: how to demonstrate the result
Applicability: conditions or exceptions
```

Group repeated instances under one root cause. Rank findings by user impact and likelihood, not by how easy they are to mention.

## Promote lessons carefully

Turn a lesson into shared guidance when it is supported by repeated incidents, a clear high-impact failure, or authoritative version-matched guidance. Add automation when the rule is objective and the maintenance cost is justified. Keep one-off observations in the review or retrospective until the evidence is stronger.
