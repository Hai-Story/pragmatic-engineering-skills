# Source review and design decisions

This document records the external material used to design Pragmatic Engineering Skills. It separates inspiration from copied content and explains where the suite intentionally differs.

Repository snapshots, revisions, licenses, inspected files, and hashes are recorded in [`sources.json`](sources.json). Star counts are discovery context captured at retrieval time, not a quality guarantee.

## Nature Skills

Inspected the shared entry point, reader workflow, and experiment log from [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills).

Adopted: a small shared core, specialist skills that can work independently, durable evidence records, and references loaded only when needed.

Changed: the suite does not use research-specific directory conventions, paper workflows, or external platform integrations. No Nature Skills file is bundled.

## Superpowers

Inspected brainstorming, plan writing, systematic debugging, verification, parallel-agent, and test-driven-development workflows from [obra/superpowers](https://github.com/obra/superpowers).

Adopted: explicit deliverables, hypothesis-driven debugging, verification tied to completion, and integration checks for parallel work.

Changed: small authorized changes do not require a full lifecycle or repeated approval. TDD is a useful regression technique rather than a universal reason to delete existing code and restart. Parallel agents are not started solely because a task is large.

## GitHub Spec Kit

Inspected specification, plan, and task templates from [github/spec-kit](https://github.com/github/spec-kit).

Adopted: traceability from outcome to acceptance, tasks that name dependencies and interfaces, and explicit unknowns.

Changed: the suite does not require Spec Kit's branch, command, or artifact structure. Small changes can remain lightweight, and test selection follows risk rather than a single template rule.

## Anthropic Skills

Inspected the web application testing workflow and skill-creation evaluation guidance from [anthropics/skills](https://github.com/anthropics/skills).

Adopted: observe the system before acting, evaluate skills on concrete scenarios, and separate output quality from format validation.

Changed: readiness conditions come from the application rather than a fixed waiting recipe. The current smoke trials have no baseline comparison, so the project does not claim measured improvement.

## OpenAI Skills and official authoring guidance

Inspected the focused GitHub review skill from [openai/skills](https://github.com/openai/skills) and the official [skill](https://learn.chatgpt.com/docs/build-skills) and [plugin](https://learn.chatgpt.com/docs/build-plugins) authoring documentation.

Adopted: narrow triggers, explicit deliverables, `SKILL.md` portability, repository-local discovery, optional `agents/openai.yaml` metadata, canonical `skills/` packaging, and plugin manifests for multi-skill distribution.

Changed: review feedback is verified rather than accepted automatically. The repository provides both a portable root manifest and the Codex-compatible `.codex-plugin/plugin.json` format.

## Vercel Agent Skills

Inspected the React best-practices skill from [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills).

Adopted: organize rules around concrete problem types and load detailed guidance on demand.

Changed: framework-specific advice is not placed in a technology-neutral workflow. Such references should be added only with a real supported-version use case.

## Addy Osmani's Agent Skills

Inspected the repository entry point, skill anatomy guide, and meta-router from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills).

Adopted: public-facing English documentation, phase-oriented discovery, contribution standards, negative trigger clarity, progressive disclosure, scenario-based evaluation, and the rule that procedures should describe capabilities instead of model-specific workarounds.

Changed: this suite deliberately remains smaller. Its differentiation is context-sensitive practice selection and explicit advice for existing nonconforming code, rather than a broad catalog of personas, commands, and technology workflows.

## Software Development Best Practices

Inspected the fixed-revision README from [dronezzzko/software-development-best-practices](https://github.com/dronezzzko/software-development-best-practices).

Adopted: its taxonomy is useful as a discovery index for candidate sources across design, APIs, security, languages, containers, data, and testing.

Changed: inclusion in a link collection is not treated as authority. A candidate practice still requires maintained primary documentation, project applicability, and license review. No indexed content was copied.

## Git Best Practices

Inspected [Seth Robertson's Git Best Practices](https://sethrobertson.github.io/GitBestPractices/), including its context warning and license.

Adopted: distinguish private checkpoints, reviewable history, and published history; write messages for later readers; protect current work before recovery; and keep published history stable by default.

Changed: no single branch model, merge flag, generated-file rule, or history-cleaning schedule is universal. Repository policy and collaboration state decide those choices.

## Conventional Commits 1.0.0

Inspected the complete [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) specification.

Adopted: the message grammar, `feat` and `fix` meaning, breaking-change markers, optional body and footer, and the distinction between the convention and semantic versioning.

Changed: the convention is enforced only when repository documentation or automation adopts it. Types and scopes come from project policy. In squash workflows, the final merge artifact may be the only message that must conform.

## Wikipedia software development philosophies index

Inspected the pinned 10 September 2026 revision of Wikipedia's [List of software development philosophies](https://en.wikipedia.org/w/index.php?title=List_of_software_development_philosophies&oldid=1374272361), including its groupings for large-scale styles, specification paradigms, comprehensive methodologies, rules of thumb, programming paradigms, development methodologies, and processes.

Adopted: the breadth of the index revealed that engineering advice operates at different levels. The suite now separates lifecycle and feedback models, product and behavior practices, domain and structural design, implementation heuristics, verification and failure handling, runtime and deployment models, and team organization. It also records common tensions such as DRY versus loose coupling, fail-fast versus graceful degradation, and release speed versus assurance.

Changed: Wikipedia is used only as a discovery index. The page itself warns that entries vary by domain, age, and current use, and it mixes methods, paradigms, processes, principles, and laws. The suite therefore does not copy the catalog, rank philosophies, or make every entry a rule. Material recommendations still require a primary maintained source and evidence that its assumptions fit the project.

The synthesis cross-checked three representative primary sources: the [Agile principles](https://agilemanifesto.org/principles.html) for the relationship between feedback, technical excellence, sustainability, simplicity, and reflection; the [Twelve-Factor App](https://12factor.net/) for its software-as-a-service scope; and the [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) for technology-specific, gradually adopted, tool-supported guidance. These checks support the rule that a philosophy must retain its original scope and assumptions.

## Original synthesis

The resulting design uses one router, ten specialist skills, and five shared references. Specialist skills do not call the router, which avoids circular routing. The classification of nonconforming code into defect, project-rule violation, contextual risk, and optional improvement, combined with explicit counter-pressures between philosophies, is the suite's central original synthesis.

Only workflow ideas are attributed here. Third-party scripts, templates, and skills are not redistributed. A repository-level license does not always govern every subdirectory, so any future direct reuse must verify the exact file, revision, and license obligations.
