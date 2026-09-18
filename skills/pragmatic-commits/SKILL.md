---
name: pragmatic-commits
description: Organize Git changes into coherent commits, propose or write commit messages, inspect staged content, and create local commits when explicitly requested. Use for commit preparation and commit execution. Preparation does not authorize committing, committing does not authorize pushing, and shared history is not rewritten by default.
---

# Pragmatic Commits

Read the shared [working agreement](../pragmatic-engineering/references/working-agreement.md) and [Git practices](../pragmatic-engineering/references/git-practices.md).

## Workflow

1. **Inspect policy and state.** Read contribution rules and message automation. Inspect branch, upstream, worktree, index, and staged and unstaged diffs separately.
2. **Determine ownership.** Separate current-task changes from user work, generated output, and other workstreams. Preserve existing staged intent.
3. **Choose commit boundaries.** Group changes by one coherent behavior or reason. Keep implementation, tests, migrations, lockfiles, and documentation together when they form one atomic change.
4. **Choose the message convention.** Follow repository evidence. Use Conventional Commits only when adopted; use only allowed types and scopes.
5. **Verify the candidate.** Review the exact staged diff and run checks relevant to that boundary. A conventional message does not prove a correct change.
6. **Act within authorization.** If asked only for preparation, provide the split and messages without changing the index. If asked to commit, stage only owned content and create the local commit.
7. **Report state.** Provide the resulting commit ID when created, checks run, omitted changes, and whether anything was pushed.

For mixed or ambiguous hunks, do not blanket-stage, reset, or stash. If safe separation is impossible, present the exact conflicting paths or hunks and ask only for the ownership decision.

For squash workflows, assess the artifact the repository validates, often the PR title or final merge message. For published history, prefer a follow-up correction unless repository policy and targeted authorization allow rewriting. Never treat a request to commit as permission to push, force-push, merge, tag, release, or deploy.
