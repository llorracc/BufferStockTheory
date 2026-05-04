#!/bin/bash
# Install the canonical git hooks for this repo by pointing
# core.hooksPath at tools/git-hooks/.
#
# Run once per fresh clone:
#     bash tools/git-hooks/install.sh
#
# Notes:
#   - core.hooksPath is a per-clone (.git/config) setting. It is NOT
#     tracked, so each contributor must run this once.
#   - After installation, .git/hooks/* are bypassed in favour of
#     tools/git-hooks/*.

set -euo pipefail

repo_root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "ERROR: not inside a git repo" >&2
    exit 1
}

cd "$repo_root"

if [ ! -d tools/git-hooks ]; then
    echo "ERROR: tools/git-hooks not found in $repo_root" >&2
    exit 1
fi

chmod +x tools/git-hooks/pre-commit \
         tools/git-hooks/post-commit \
         tools/git-hooks/lint-no-inline-defs.sh
git config core.hooksPath tools/git-hooks

echo "Installed: core.hooksPath -> tools/git-hooks"
echo "  pre-commit:                $(ls -l tools/git-hooks/pre-commit            | awk '{print $1}')"
echo "  post-commit:               $(ls -l tools/git-hooks/post-commit           | awk '{print $1}')"
echo "  lint-no-inline-defs.sh:    $(ls -l tools/git-hooks/lint-no-inline-defs.sh | awk '{print $1}')"
