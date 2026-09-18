# Selecting Development Philosophies

Software development philosophies are lenses for different problems, not a stack of rules to apply simultaneously. The [Wikipedia index](https://en.wikipedia.org/w/index.php?title=List_of_software_development_philosophies&oldid=1374272361) mixes methodologies, processes, programming paradigms, design principles, laws, and individual practices. It also notes that relevance varies by domain and that some entries may be dated. Use the index for discovery, then verify important guidance against a primary, maintained source.

## Choose a lens from the problem

1. **Name the decision level.** Is the issue about lifecycle, product discovery, architecture, code design, verification, deployment, or team organization?
2. **Name the failure or cost.** Examples include slow feedback, ambiguous behavior, accidental coupling, unsafe change, duplicated decisions, weak traceability, or deployment drift.
3. **Identify hard constraints.** Consider safety, regulation, reversibility, release cost, latency, offline operation, team topology, and supported technology.
4. **Inspect local adoption.** Look for repository rules, architecture decisions, tests, CI, team workflow, and vocabulary that show which philosophy is already in use.
5. **Select the smallest useful lens.** Prefer one primary principle and one counter-pressure over a list of slogans.
6. **Define an observable result.** State what should improve and how the project can tell.

## Families and useful contexts

| Family | Examples from the index | Useful when | Guard against |
| --- | --- | --- | --- |
| Feedback and flow | Iterative and incremental development, Agile, Lean, Kanban, release early and often | Requirements change, feedback is valuable, and increments can be delivered safely | Treating speed or ceremony reduction as permission to skip design, security, or verification |
| Assurance, specification, and traceability | Waterfall, Unified Process, formal methods, model-based systems engineering | Contracts are stable, assurance evidence is required, or failures are very costly | Assuming the approach forbids prototypes, staged learning, or feedback |
| Product and behavior | User-centered design, value-driven design, BDD, ATDD, specification by example | The main risk is building the wrong behavior or sharing different meanings | Turning examples into exhaustive requirements or confusing activity with user value |
| Domain and structure | DDD, separation of concerns, loose coupling, Law of Demeter, GRASP, SOLID | Domain language, change boundaries, or dependency structure drive complexity | Applying object-oriented principles outside their context or adding layers without a change pressure |
| Simplicity and implementation | KISS, YAGNI, DRY, rule of least power, Unix philosophy, convention over configuration | Accidental complexity, speculative capability, duplicated decisions, or oversized tools slow change | Removing necessary flexibility, merging coincidental similarity, or hiding important configuration |
| Verification and failure | TDD, continuous TDD, fail-fast, secure by design, robustness principles | Feedback on correctness, invalid state, trust boundaries, or failure containment is central | Confusing test order with coverage quality, or accepting malformed input at a security boundary |
| Runtime and deployment | Twelve-Factor App, local-first, reactive programming | The product and operating model actually match the philosophy's assumptions | Applying service, cloud, or distributed-system rules to a different architecture |
| Team and organization | Egoless programming, pair or mob programming, Conway's law, Brooks's law | Review quality, knowledge flow, ownership, or communication structure is the bottleneck | Treating observations about organizations as deterministic laws or adding people without integration capacity |

The [Agile principles](https://agilemanifesto.org/principles.html) connect frequent delivery with technical excellence, sustainable pace, simplicity, collaboration, and reflection. Do not reduce Agile to short iterations. The [Twelve-Factor App](https://12factor.net/) describes software delivered as a service; its deployment assumptions are not a universal code standard. Language guides such as the [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) are living, technology-specific guidance and should be matched to the project's language and version.

## Resolve common tensions

| Tension | Decision question |
| --- | --- |
| DRY vs. loose coupling | Is the duplication one shared business decision, or merely similar code that may evolve independently? |
| KISS or YAGNI vs. known future constraints | Is the flexibility speculative, or required by an accepted contract, migration, security boundary, or near-term roadmap? |
| Fail-fast vs. graceful degradation | Does stopping prevent corruption and expose a programmer error, or does isolation preserve a service without hiding damage? |
| Robust input handling vs. strict validation | Is this a tolerant interoperability boundary, or a security, financial, schema, or authorization boundary where ambiguity is dangerous? |
| Single source of truth vs. distributed autonomy | Does central authority prevent conflicting decisions, or create an availability and coupling bottleneck that needs explicit replication semantics? |
| Reuse vs. ownership | Does reuse remove one maintained decision, or add a dependency whose lifecycle and failure modes the project cannot control? |
| Release early vs. assurance | Can the change be limited, observed, rolled back, and kept within regulatory or safety obligations? |
| Open-closed or SOLID vs. simplicity | Is variation already present and costly, or is an abstraction being built for hypothetical change? |
| Agile vs. formal or staged methods | Which parts need rapid learning, and which parts require stable baselines, traceability, or proof? A project may need both. |

## Review code without slogan findings

Do not report “violates DRY,” “not SOLID,” or “not Agile” as a complete finding. Translate the philosophy into project evidence:

```text
Candidate lens: the principle or methodology being considered
Local objective: the failure or cost it should reduce here
Observed mismatch: the specific code, workflow, or architecture condition
Impact: the behavior, change cost, or risk created by that condition
Counter-pressure: the principle or constraint arguing against the change
Recommendation: the smallest justified adjustment
Verification: the observable result or measure
```

If no material impact or project objective can be shown, classify the observation as an optional improvement or omit it. A philosophy name is never evidence by itself.
