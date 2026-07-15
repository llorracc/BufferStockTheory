#!/usr/bin/env bash
# check-no-absolute-paths.sh — Phase-7 guard for the remove-absolute-paths plan.
#
# Rejects machine-specific absolute paths in tracked source so the repo stays
# portable (and a clean QE replication package), and routes each hit to the
# correct tool. Install in BufferStockTheory-Latest as tools/check-no-absolute-
# paths.sh, then:
#   * pre-commit: call it with --staged from .git/hooks/pre-commit (chain it
#     after the existing hook), and
#   * CI: run `bash tools/check-no-absolute-paths.sh --all`.
#
# Usage:
#   check-no-absolute-paths.sh --staged       # scan staged adds (pre-commit)
#   check-no-absolute-paths.sh --all          # scan all tracked files (CI)
#   check-no-absolute-paths.sh --range A..B   # scan files changed in a range
#
# Bypass intentionally: ALLOW_ABS_PATHS=1 ./check-…  (or git commit --no-verify).

set -uo pipefail

if [ "${ALLOW_ABS_PATHS:-}" = "1" ]; then
    echo "check-no-absolute-paths: skipped (ALLOW_ABS_PATHS=1)"
    exit 0
fi

mode="${1:---staged}"

# Machine-specific absolute roots that do not survive a clone / CI runner.
PAT='(/Volumes/|/Users/[A-Za-z0-9._-]+/|/usr/local/)'

# Skip generated mirror, vendored-upstream tree, dev notes, binaries, self.
# (@resources is vendored from econ-ark-tools — fix it upstream, not here;
#  docs/ is a generated mirror of fixed source.)
is_allowed() {
    case "$1" in
        docs/*|@resources/*|*/@resources/*|plans_private/*)   return 0 ;;
        .gitignore|*check-no-absolute-paths.sh)               return 0 ;;
        *.pdf|*.png|*.jpg|*.jpeg|*.gif|*.svg|*.xbb|*.eps)     return 0 ;;
    esac
    return 1
}

# Tool to route a contributor to, by file type.
route() {
    case "$1" in
        *.tex|*.sty|*.cls)  echo 'use \econtexRoot / \FigDir … (@local/dir-paths)' ;;
        *.bib)              echo "strip via bibtool 'delete.field{file}' (refresh-bib.sh)" ;;
        *.ipynb)            echo "clear outputs / install the nbstripout filter" ;;
        *.sh|*.py|*.pl|Makefile|*.mk|*latexmkrc*)
                            echo "source paths.sh (\$LATEST_ROOT …); tool binaries via PATH / command -v / env" ;;
        *)                  echo "make it relative or route through the repo path tooling" ;;
    esac
}

case "$mode" in
    --staged) files=$(git diff --cached --name-only --diff-filter=ACM) ;;
    --all)    files=$(git ls-files) ;;
    --range)  files=$(git diff --name-only --diff-filter=ACM "${2:?--range needs A..B}") ;;
    *) echo "usage: $0 [--staged|--all|--range A..B]" >&2; exit 2 ;;
esac

# Read content from the staged blob (pre-commit) or the working tree (CI).
content() {
    if [ "$mode" = "--staged" ]; then git show ":$1" 2>/dev/null; else cat "$1" 2>/dev/null; fi
}

hits=0
while IFS= read -r f; do
    [ -z "$f" ] && continue
    is_allowed "$f" && continue
    while IFS= read -r m; do
        [ -z "$m" ] && continue
        [ "$hits" -eq 0 ] && echo "❌ absolute paths in tracked source (machine-specific; won't survive a clone):" >&2
        hits=$((hits + 1))
        echo "  $f:$m" >&2
        echo "      → $(route "$f")" >&2
    done < <(content "$f" | grep -nIE "$PAT" 2>/dev/null)
done <<< "$files"

if [ "$hits" -gt 0 ]; then
    {
        echo ""
        echo "Blocked: $hits absolute-path occurrence(s). Fix per the hint, or bypass"
        echo "intentionally with ALLOW_ABS_PATHS=1 (or git commit --no-verify)."
    } >&2
    exit 1
fi

echo "check-no-absolute-paths: clean ($mode)"
exit 0
