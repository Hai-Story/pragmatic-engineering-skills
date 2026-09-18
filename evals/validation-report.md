# Validation report

Date: 2026-09-18. Results apply to the current working tree following version 0.1.0; rerun affected checks after later changes.

## Structural validation

- All 11 skills passed the suite's metadata, naming, shared-reference, link, UI metadata, manifest, language, and evaluation-reference checks.
- The negative unit suite covers missing shared dependencies, missing skills, folder mismatch, escaped links, missing or duplicate metadata, non-English skill content, missing UI metadata, manifest drift, and unknown evaluation skills.
- The repository validator and unit tests use only the Python standard library.

## Behavioral smoke trials

Two scenarios were executed independently before the English packaging rewrite. Their prompts and acceptance criteria are preserved in English, and their fixtures remain in the repository. Four additional scenarios now cover conflicts between DRY and coupling, YAGNI and known contracts, tolerant parsing and security boundaries, and iterative work with formal assurance.

### Review-only account visibility

The run identified that an empty user ID returned every account, explained the impact and smallest correction, respected the fixture's camelCase rule, and did not edit any fixture file. See [result](runs/review-only/result.md).

### One-based pagination debugging

The run first reproduced the offset failure, changed the calculation to `(number - 1) * size`, expanded regression coverage, and passed 10 tests. Protected user notes and repository instructions remained unchanged. See [result](runs/debug-pagination/result.md).

## Limits

Twenty-two scenarios remain defined but not executed. Automatic skill selection, philosophy-conflict handling, mixed-index commits, shared-history operations, multi-person integration, different models, and repeated baseline comparisons have not been validated. The project therefore makes no numerical claim about quality, speed, or cost improvement.
