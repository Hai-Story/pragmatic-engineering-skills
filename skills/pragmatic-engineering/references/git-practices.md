# Pragmatic Git Practices

Git practices depend on whether history is private, under review, or already shared. Inspect repository policy and the current state before choosing a command.

## Start with state and ownership

Inspect the worktree, index, branch, upstream, and relevant diffs. Determine which changes belong to the current task and which belong to the user or another workstream. Preserve existing staged intent; never assume every modified file belongs in one commit.

## Match history to its audience

- **Private checkpoint:** optimize for recoverability. A temporary commit may be rough if it is unpushed and clearly private.
- **Reviewable branch:** make each commit understandable and, where practical, independently buildable and testable. Separate changes by intent rather than file type.
- **Published history:** optimize for stability and collaboration. Prefer additive corrections; rewrite only when team policy and targeted authorization support it.

Small commits are useful when they preserve one coherent intent. Fragmentation that obscures a single behavior change is not an improvement.

## Stage deliberately

1. Review unstaged and staged diffs separately.
2. Select only files or hunks owned by the task.
3. Re-read the staged diff as the proposed commit.
4. Check generated files, migrations, lockfiles, and tests as a connected change.
5. Run checks that cover the staged behavior or explain why a check cannot run.

Avoid blanket staging in a mixed worktree. Do not use reset, stash, clean, or checkout as a convenience when they may disturb work you do not own.

## Write useful messages

A message should explain the intent and material effect. Use imperative, specific language and add a body when motivation, migration, or risk is not obvious from the diff.

Use Conventional Commits only when the repository has adopted it through documentation or automation. Version 1.0.0 follows:

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

`feat` represents a new feature and `fix` a bug fix. Mark breaking changes with `!` before the colon or a `BREAKING CHANGE:` footer. Other types and scopes come from project policy; they carry no universal semantic-version meaning. In squash workflows, the final PR title or merge message may be the enforced artifact.

## Treat risky operations explicitly

A commit does not authorize a push. A push does not authorize a force push, merge, release, tag move, or deployment. Before rewriting shared history, establish who may depend on it, what the repository permits, and how recovery will work.

Before recovery or cleanup, protect current work and inspect reflogs or recoverable objects. Prefer the least destructive command that reaches the intended state.

## Report the result

State the commit boundary, checks run, commit identifier if created, and whether it remains local. If no commit was authorized, provide the proposed split and messages without changing the index or history.

Sources that informed this guide: [Git Best Practices](https://sethrobertson.github.io/GitBestPractices/) and [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). Their guidance remains subordinate to the repository's actual workflow and constraints.
