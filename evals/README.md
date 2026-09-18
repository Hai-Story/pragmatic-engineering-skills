# Behavioral evaluations

`cases.json` is a catalog of representative requests, expected behaviors, and forbidden behaviors. It is grader input, not an automated claim that every scenario passed.

## Running a scenario

1. Copy the fixture to a clean isolated directory when the case provides one.
2. Start a fresh agent conversation with only the documented skill availability and prompt.
3. Preserve the complete output and file changes.
4. Grade every `checks` and `must_not` item with concrete evidence.
5. Record the host, model, settings, fixture revision, and limitations.
6. Update `results.json` only after an independent reviewer verifies the artifacts.

Do not reuse a modified fixture as a new baseline. Do not turn a single passing run into a success-rate claim.
