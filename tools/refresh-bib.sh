#!/bin/bash
# Regenerate BufferStockTheory.bib from system.bib + BufferStockTheory-Add-Refs.bib
# via the bibtool-extract script in @resources/shell/.
#
# When to run: after editing system.bib (or BufferStockTheory-Add-Refs.bib) when
# you want the changes propagated into the tracked BufferStockTheory.bib.
# Inspect the resulting diff and commit deliberately.
#
# This replaces the old in-build auto-regenerate (.latexmkrc_build-all:21) with
# an explicit, maintainer-triggered step. The .bib is now a tracked artifact
# rather than a transient one.
#
# Requires: bibtool, kpsewhich, an existing BufferStockTheory.aux (so the script
# knows which keys are cited). If .aux is missing, run a build first.

set -euo pipefail
repo_root="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "ERROR: not inside a git repo" >&2
    exit 1
}
cd "$repo_root"

if [ ! -f BufferStockTheory.aux ]; then
    echo "ERROR: BufferStockTheory.aux not found." >&2
    echo "       Run ./reproduce.sh (or pdflatex BufferStockTheory) first so the" >&2
    echo "       extract script knows which citation keys are referenced." >&2
    exit 2
fi

bash @resources/shell/bibtool_extract-used-refs-from-system-bib-and-add-refs.sh . BufferStockTheory

# Strip reference-manager 'file = {...}' fields (local PDF paths like <local-path>,
# Dropbox) so they never reach the tracked/published bib. The extract script above
# is vendored from econ-ark-tools, so we post-process here to keep BST's bib clean
# without patching the vendored copy (ideal long-term: fix it upstream too).
if command -v bibtool >/dev/null 2>&1; then
    bibtool -- 'delete.field{file}' BufferStockTheory.bib -o BufferStockTheory.bib.tmp \
        && mv BufferStockTheory.bib.tmp BufferStockTheory.bib
fi

echo
echo "BufferStockTheory.bib refreshed. Inspect and commit if the diff is intentional:"
echo "    git diff BufferStockTheory.bib"
