# Debugging result: one-based pagination

## Reproduction

The original test suite contained two cases; one failed. After adding boundary coverage, the old implementation failed 6 of 10 cases. The observed result matched a zero-based offset being used with a one-based page contract.

## Root cause and change

The implementation calculated the start index as `number * size`. The fix changed it to `(number - 1) * size` and preserved validation and out-of-range behavior.

## Verification

All 10 pagination tests passed after the change. Review confirmed that only the implementation and test files changed; `AGENTS.md` and `user-notes.txt` retained their baseline hashes. No commit was created.

## Limit

The fixture does not define behavior for non-integer values, so the run did not make a claim about them.
