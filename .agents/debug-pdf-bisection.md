# Debug PDF drift via subfile bisection

When an edit to BufferStockTheory's source (`.tex`, `.sty`, `.bib`, …) is *expected* to leave the generated PDF identical but in fact changes it, this procedure localizes the change to a specific `\subfile{}`.

This file is the **single source of truth** for the algorithm. Helper scripts in `tools/private/` are derived artifacts — if any are missing, recreate them from the spec in this file.

## When to use

You made an edit that should be cosmetic (whitespace, comment changes, refactoring a `\newcommand` to a definitionally-equivalent form, swapping a package for a behavioral equivalent, retiring an obsolete `.sty` import, …) but `BufferStockTheory.pdf` no longer matches the committed version. Use this to find which subfile(s) actually render differently and what changed inside them.

The repo's existing `reproduce/document.sh` already runs a `pdftotext`-based "is anything different" check; this tool answers "*where* is it different".

## Invocation

```bash
bash tools/private/bisect_pdf.sh <golden-branch>
```

`<golden-branch>` is the name of the clean reference branch (the "should be equivalent to" baseline). The current branch (HEAD) is the candidate.

The driver:

1. **Fails fast** if `git status --porcelain` is non-empty — the source must be a clean branch.
2. **Fails fast** if `<golden-branch>` doesn't exist or equals the current branch.
3. Creates a fresh branch `bisect-ref-YYYYMMDD-HHMMSS` from `<golden-branch>` (timestamp marks the bisection run for traceability).
4. Materializes two worktrees under `_build/bisect-ref-<ts>/`:
   - `ref/`  — at the new `bisect-ref-<ts>` branch
   - `cand/` — at the candidate's current branch
5. Runs the bisection (below).
6. Leaves all artifacts in place for inspection. The user removes the timestamped ref branch and worktrees when done (`git worktree remove _build/bisect-ref-<ts>/ref`, `git branch -D bisect-ref-<ts>`).

## Algorithm

### Two-stage equivalence test (`pdf_equiv.sh`)

For two PDFs A and B:

1. **Stage 1 — pdftotext.** Run `pdftotext -nopgbrk` on both (the `-nopgbrk` suppresses inter-page form-feed characters), pipe each through a `sed` filter that drops standalone ISO-date lines (`^\s*\d{4}-\d{2}-\d{2}\s*$`) so `\today` differences between calendar days don't trigger a false positive, then `diff` the outputs. If they differ, A and B are *not* equivalent (exit 1, print first 40 diff lines). The date filter only matches dates that occupy a whole line on their own, so dates appearing inline in body text are unaffected.
2. **Stage 2 — qpdf normalize + metadata strip.** Run `qpdf --qdf --object-streams=disable` on both, pipe through a sed filter that drops lines matching volatile metadata fields (`/CreationDate`, `/ModDate`, `/ID`, `/Producer`, `/Trapped`, `/Author`, `/Creator`, `/Title`, `/Subject`, `/Keywords`, and any PDF-date-format `(D:YYYYMMDD…)` strings). Diff the results. If they differ, A and B differ in typesetting only (exit 2).
3. If both stages pass, exit 0 — A and B are content-equivalent.

The two-stage design catches both textual drift (stage 1) and rare typeset-only drift such as font-subset reshuffling or sub-pixel figure placement that pdftotext flattens away (stage 2).

### Subfile bisection

Let `S = [s₁, s₂, …, sₙ]` be the list of `\subfile{…}` entries in `BufferStockTheory.tex`, in source order. (As of 2026-04-28: `Introduction`, `BufferStockTheory-NoAppendix`, `\ApndxDir/ApndxConcaveCFunc`, `\ApndxDir/ApndxMTargetIsStable`, `\ApndxDir/ApndxBalancedGrowthcNrmAndCov`, `\ApndxDir/ApndxLiqConstr`, `\ApndxDir/ApndxConditionDiagrams`, `\ApndxDir/ApndxSupportingAnalysis`.)

```
bisect(S):
    if |S| == 1:
        record S[0] as a culprit
        return
    A, B = halve(S)               # first ⌊n/2⌋ vs the rest
    build_masked(A) in ref-worktree  -> ref-A.pdf
    build_masked(A) in cand-worktree -> cand-A.pdf
    if not pdf_equiv(ref-A.pdf, cand-A.pdf):
        bisect(A)
    build_masked(B) in ref-worktree  -> ref-B.pdf
    build_masked(B) in cand-worktree -> cand-B.pdf
    if not pdf_equiv(ref-B.pdf, cand-B.pdf):
        bisect(B)
```

`build_masked(M)` rewrites `BufferStockTheory.tex` to comment out every `\subfile{X}` line whose target X isn't in M, runs `latexmk -silent BufferStockTheory`, copies the resulting PDF out, and restores the file with `git checkout -- BufferStockTheory.tex`.

The driver first runs `bisect(S)` after confirming the full build pair already differs. Both halves are tested at every level (rather than the classic single-pivot bisect) so that *multiple* drifting subfiles are all reported, not just one.

### Reporting

For each culprit:

- The subfile name (path and basename).
- A `pdftotext` diff between the ref and candidate solo build of that subfile (i.e. mask=`{culprit}` only).
- A note indicating whether the drift is textual (stage 1) or typeset-only (stage 2).

If the full build differed but no half does, the algorithm reports an interaction-effect inconclusive result and points the user to `_build/bisect-ref-<ts>/` for manual inspection.

## Helper scripts (canonical interfaces)

If any of the following is missing in `tools/private/`, regenerate it from the spec below. Scripts must use `set -euo pipefail`. The directory `tools/private/` is gitignored via the repo's `*private` pattern, so a fresh clone won't have them — that's expected.

### `tools/private/pdf_equiv.sh A.pdf B.pdf`

| Exit | Meaning |
|---|---|
| 0 | Equivalent (both stages match) |
| 1 | Stage 1 (pdftotext) differs; first 40 diff lines printed |
| 2 | Stage 1 matches but stage 2 (qpdf-normalized) differs |
| 64 | Usage error |
| 65 | One of the input files is missing |

Stage 1 uses `pdftotext -nopgbrk INPUT -` piped through `sed -E '/^[[:space:]]*[0-9]{4}-[0-9]{2}-[0-9]{2}[[:space:]]*$/d'` to strip `\today` lines. Stage 2 uses `qpdf --qdf --object-streams=disable INPUT -` piped through `sed -E -e '/\/(CreationDate|ModDate|ID|Producer|Trapped|Author|Creator|Title|Subject|Keywords)\b/d' -e '/\(D:[0-9]{14}/d'`.

### `tools/private/build_masked.sh <include-csv> <out.pdf>`

Runs in the current directory (must be a worktree root with `BufferStockTheory.tex` and `.latexmkrc` present). The include list is a comma-separated list of subfile names — each entry matches either the full string inside `\subfile{…}` (e.g. `\ApndxDir/ApndxConcaveCFunc`) or its basename (`ApndxConcaveCFunc`).

Steps:

1. `git checkout -- BufferStockTheory.tex` (idempotent restore).
2. For every line matching `^\s*\\subfile\{X\}`, if X (or its basename) is not in the include list, prepend `%BISECT-MASKED% ` to the line.
3. **Canonical 4-pass build for `BufferStockTheory.tex` specifically.** First clean stale state: `rm -f BufferStockTheory.{aux,bbl,blg,toc,log,out,fls,fdb_latexmk,synctex.gz}` and `BufferStockTheory.bib`, `economics.bib`, `latexdefs.tex` (the `.latexmkrc` deletes these at startup; we replicate that since we invoke pdflatex directly). Then run `pdflatex -halt-on-error -interaction=batchmode BufferStockTheory` twice, `bibtex BufferStockTheory` once, then `pdflatex` twice more — exactly the sequence `reproduce/document.sh` uses for the main paper. Bisection does not need the rest of `document.sh`'s work (TikZ figures, appendices-as-standalone, slides, Figures-All, Tables-All), and skipping it cuts per-iteration time from ~10 min to ~1 min. Tolerate non-zero exits from individual commands (bibtex returns 2 on duplicate-entry warnings); verify success by checking that `BufferStockTheory.pdf` exists. On absence, restore the file and exit 70.
4. `cp BufferStockTheory.pdf <out.pdf>`.
5. `git checkout -- BufferStockTheory.tex`.

Use Python (or sed with care) for step 2 — the subfile names contain backslashes (`\ApndxDir/...`) which complicate shell quoting.

### `tools/private/bisect_pdf.sh <golden-branch>`

Driver. Implements the algorithm above. Output discipline:

- Echoes each phase header (`─── Step 0: full build ───`, `─── bisect: split N → ⌊N/2⌋ | ⌈N/2⌉ ───`).
- Echoes worktree paths, ref branch name, and final culprit list with diffs.
- Exit 0 if equivalent at full build; 1 if culprits found; 2 if inconclusive.

## Limitations

- **Granularity** is one `\subfile{}` per bisection node. Drift inside `BufferStockTheory-NoAppendix` (the largest subfile) requires manual narrowing — typically by `\section{}` or `\input{}` boundaries.
- **`.sty` changes that affect every subfile equally** will be reported as "all subfiles drift". Interpret as a global change and trace through the macros each subfile uses.
- **Bibliography changes** (edits to `BufferStockTheory-Add-Refs.bib` that affect citations referenced from many subfiles) likewise present as broad drift.
- **Stage-2 metadata stripping is best-effort.** A rare false-positive is possible if a non-volatile field happens to match a stripped pattern. If observed, tighten the sed filter.

## Cleanup

After diagnosis:

```bash
git worktree remove _build/bisect-ref-<ts>/ref
git worktree remove _build/bisect-ref-<ts>/cand
git branch -D bisect-ref-<ts>
rm -rf _build/bisect-ref-<ts>
```

The driver does not auto-clean — leaving artifacts in place lets the user re-inspect diffs without re-running the full bisection.
