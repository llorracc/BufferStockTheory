# `tools/git-hooks/` — canonical, version-controlled git hooks

These are the source-of-truth git hooks for this repo. They live in the
working tree (so they can be reviewed, diffed, and updated like any other
file) instead of being copy-pasted into each clone's untracked `.git/hooks/`.

## Install

Run once per fresh clone:

```bash
bash tools/git-hooks/install.sh
```

This sets `core.hooksPath = tools/git-hooks` in `.git/config`. After that,
git will use the hooks here and ignore `.git/hooks/`.

`core.hooksPath` is a per-clone setting, so each contributor must run the
installer once on their own machine.

## What they do

| Hook | Platform | Behaviour |
|---|---|---|
| `pre-commit`  | Linux only (no-op on macOS) | Runs `reproduce/document.sh --quiet --debug --noninteractive` in the foreground; blocks the commit on failure. |
| `post-commit` | macOS only (no-op on Linux) | Runs the same reproduction in the **background**, with a desktop notification + spoken feedback when it finishes. |

The macOS hook intentionally runs in the background so successive commits
aren't blocked. To prevent two rapid commits from racing over shared LaTeX
intermediates (`BufferStockTheory.aux`, `.log`, `.out`, ...), the
`post-commit` hook supersedes any in-flight prior reproduction with a
single `pkill` line at the top of `run_reproduction`:

```bash
pkill -f 'reproduce/document.sh.*--quiet.*--debug.*--noninteractive' 2>/dev/null && sleep 1
```

Semantics: **latest commit wins.** The older reproduction is killed and
the newer one starts fresh. Reproductions are idempotent, so this is safe.

## Logs

Both hooks write to `.git/hooks/reproduction.log` (which is local to the
clone and not tracked). To follow live:

```bash
tail -f .git/hooks/reproduction.log
```

## Updating the hooks

Edit the files here, commit. After the commit, the hook is already in
effect (since `core.hooksPath` points at this directory).
