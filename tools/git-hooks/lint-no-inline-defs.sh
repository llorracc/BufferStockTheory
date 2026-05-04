#!/bin/bash
# Lint: discourage NEW inline macro definitions in the body files of the
# published paper. Paper-local macros belong in @local/bst-macros.sty
# (general) or @local/bst-theorems.sty (theorem environments).
#
# Modes:
#   --staged   only inspect lines added in the staged diff (used by
#              pre-commit; default). Existing inline defs are tolerated;
#              this only fires on NEW regressions.
#   --all      report every in-scope body-level def in the working tree
#              (advisory; never blocks). Used by `make latex-source-lint`.
#
# Scope (only files included in the published BufferStockTheory.pdf):
#   Introduction.tex
#   BufferStockTheory-NoAppendix.tex (the wrapper)
#   sections/<the 5 body sections>.tex
#   Appendices/<the 6 referenced appendices>.tex
#
# Allowed patterns (not flagged even when newly added):
#   - \newcommand{\subname}{...}              per-file identity for \bibfilesfind
#   - \(provide|new|renew)command{\figName}   per-figure scratch
#   - \(provide|new|renew)command{\figFile}   per-figure scratch
#   - \renewcommand{\versn|\rootFromOut|\contentsname|\LtxDir}{...}
#                                             internal-LaTeX state toggles
#   - lines starting with \notinsubfile{...}
#   - lines starting with \compilingasstandalone{...}
#   - any line ending with "% allowed-inline: <reason>"
#
# See plans_private/20260428-2300h_streamline-tex-source-for-myst.md §A4.

set -euo pipefail
MODE="${1:---staged}"

# Exact in-scope files (avoids false positives on docs/, debug variants,
# Apndx files not referenced by the published paper, etc.).
SCOPE_FILES=(
    "Introduction.tex"
    "BufferStockTheory-NoAppendix.tex"
    "sections/TheoreticalFoundations.tex"
    "sections/IndividualBufferStockStability.tex"
    "sections/AggregateInvariantRelationships.tex"
    "sections/ConsumerPatienceAndLimitingConsumption.tex"
    "sections/Conclusions.tex"
    "Appendices/ApndxConcaveCFunc.tex"
    "Appendices/ApndxMTargetIsStable.tex"
    "Appendices/ApndxBalancedGrowthcNrmAndCov.tex"
    "Appendices/ApndxLiqConstr.tex"
    "Appendices/ApndxConditionDiagrams.tex"
    "Appendices/ApndxSupportingAnalysis.tex"
)

is_in_scope() {
    local f="$1"
    for s in "${SCOPE_FILES[@]}"; do
        [ "$f" = "$s" ] && return 0
    done
    return 1
}

# Returns 0 if the line content is an allowed pattern, 1 otherwise.
is_allowed() {
    local content="$1"
    # Comments
    [[ "$content" =~ ^[[:space:]]*% ]] && return 0
    # Opt-out marker
    [[ "$content" =~ %[[:space:]]*allowed-inline ]] && return 0
    # Per-file identity / scratch / internal-state toggles
    [[ "$content" =~ \\(provide|new)command\{\\subname\} ]] && return 0
    [[ "$content" =~ \\(provide|new|renew)command\{\\fig(Name|File)\} ]] && return 0
    [[ "$content" =~ \\renewcommand\{\\(versn|rootFromOut|contentsname|LtxDir)\} ]] && return 0
    # Standalone-mode wrappers — the inner \renewcommand only fires when
    # the file is compiled standalone, not when included by the master.
    [[ "$content" =~ ^[[:space:]]*\\(notinsubfile|compilingasstandalone)\{ ]] && return 0
    return 1
}

contains_inline_def() {
    [[ "$1" =~ \\(provide|new|renew)command ]]
}

EXIT=0

if [ "$MODE" = "--staged" ]; then
    current_file=""
    in_scope=0
    while IFS= read -r line; do
        if [[ "$line" == "diff --git "* ]]; then
            in_scope=0
            current_file=""
            continue
        fi
        if [[ "$line" == "+++ b/"* ]]; then
            current_file="${line#+++ b/}"
            if is_in_scope "$current_file"; then
                in_scope=1
            else
                in_scope=0
            fi
            continue
        fi
        [ "$in_scope" -eq 1 ] || continue
        # Added lines (but not the "+++" header)
        if [[ "$line" == +* && "$line" != "+++ "* ]]; then
            content="${line:1}"
            if contains_inline_def "$content" && ! is_allowed "$content"; then
                if [ $EXIT -eq 0 ]; then
                    echo "ERROR: new inline macro definition(s) in body file(s):" >&2
                fi
                echo "  $current_file: $content" >&2
                EXIT=1
            fi
        fi
    done < <(git diff --cached)
elif [ "$MODE" = "--all" ]; then
    echo "Scanning ${#SCOPE_FILES[@]} in-scope body files for inline macro defs..."
    found=0
    for f in "${SCOPE_FILES[@]}"; do
        [ -f "$f" ] || continue
        while IFS=: read -r linenum content; do
            if contains_inline_def "$content" && ! is_allowed "$content"; then
                echo "  $f:$linenum: $content"
                found=$((found + 1))
            fi
        done < <(grep -nE '\\(provide|new|renew)command' "$f" 2>/dev/null || true)
    done
    if [ "$found" -eq 0 ]; then
        echo "No body-level macro defs found (lint clean)."
    else
        echo
        echo "Found $found inline macro def(s). Consider moving to @local/bst-macros.sty."
        echo "(--all mode is advisory; this does not block commits.)"
    fi
else
    echo "usage: $0 [--staged|--all]" >&2
    exit 64
fi

if [ "$EXIT" -ne 0 ]; then
    cat >&2 <<'MSG'

Move new defs to @local/bst-macros.sty (general macros) or
@local/bst-theorems.sty (theorem environments). If the inline form is
genuinely necessary in this case, append "% allowed-inline: <reason>"
to the line.

See plan §A4 in plans_private/20260428-2300h_streamline-tex-source-for-myst.md.
MSG
fi

exit "$EXIT"
