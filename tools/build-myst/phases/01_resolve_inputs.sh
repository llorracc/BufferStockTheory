#!/usr/bin/env bash
# Phase 01: Resolve \input{} and \subfile{} chains by recursive in-house
# expansion (latexpand cannot follow econark path macros like \ApndxDir
# through nested levels), then append a freshly-generated .bbl so the
# bibliography is visible to Phase 5.
#
# .bbl provenance:
#   This phase regenerates BufferStockTheory.bbl from current sources by
#   running pdflatex + bibtex into _build/myst/bbl-gen/. We do NOT rely
#   on docs/BufferStockTheory.bbl: that file is gitignored and kept in
#   sync only by manual intervention, which led to silent staleness
#   (e.g. the harmenbergAggregating cite-key incident — the .bbl was
#   ~18 months out of date and Phase 05 emitted broken citations until
#   noticed by a human). Self-regeneration makes the pipeline robust
#   against that class of bug.
#
#   The .bbl regen is cached: it only re-runs when a source .tex or
#   .bib file is newer than the existing .bbl. Steady-state cost is a
#   stat-loop; cold cost is one pdflatex pass + one bibtex.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

BUILD_DIR="_build/myst"
BBL_DIR="$BUILD_DIR/bbl-gen"
mkdir -p "$BUILD_DIR" "$BBL_DIR"

MASTER_TEX="BufferStockTheory.tex"
MASTER_STEM="BufferStockTheory"
BBL="$BBL_DIR/${MASTER_STEM}.bbl"
FLAT="$BUILD_DIR/01_flat.tex"

if [ ! -f "$MASTER_TEX" ]; then
  echo "Phase 01 ERROR: master TeX not found: $MASTER_TEX" >&2
  exit 1
fi

# --- .bbl freshness check --------------------------------------------------
# Regenerate if .bbl missing or any tracked .tex / .bib file is newer.
needs_regen=false
if [ ! -f "$BBL" ]; then
  needs_regen=true
  reason="missing"
else
  # Use git-tracked files only — avoids spurious staleness from build
  # artifacts in subdirectories. Faster than `find` and excludes
  # ignored content.
  if newer="$(git ls-files -- '*.tex' '*.bib' \
              | xargs -I{} stat -f '%m {}' 2>/dev/null \
              | awk -v t="$(stat -f '%m' "$BBL")" '$1 > t {print $2; exit}')"; then
    if [ -n "$newer" ]; then
      needs_regen=true
      reason="$newer is newer than $BBL"
    fi
  fi
fi

if [ "$needs_regen" = true ]; then
  echo "  regenerating .bbl ($reason) ..."
  PDFLATEX_LOG="$BBL_DIR/pdflatex-pass1.log"
  BIBTEX_LOG="$BBL_DIR/bibtex.log"

  # The master uses \begin{verbatimwrite}{\EqDir/X}...\end{verbatimwrite}
  # which writes to ./Equations/X.tex relative to cwd. With
  # -output-directory, those writes are redirected into BBL_DIR — the
  # subdirs must exist first or pdflatex fails with "I can't write on
  # file `./Equations/X.tex'".
  mkdir -p "$BBL_DIR/Equations" "$BBL_DIR/Tables"

  # Pass 1: produce .aux with cite keys. -draftmode skips PDF output;
  # -interaction=batchmode + -halt-on-error make non-interactive runs
  # surface their failure clearly. Errors here are fatal — the rest of
  # the pipeline depends on a working .aux.
  if ! pdflatex \
        -draftmode \
        -interaction=batchmode \
        -halt-on-error \
        -output-directory="$BBL_DIR" \
        "$MASTER_TEX" \
        >"$PDFLATEX_LOG" 2>&1; then
    echo "Phase 01 ERROR: pdflatex pass 1 failed during .bbl generation" >&2
    echo "  see $PDFLATEX_LOG and $BBL_DIR/${MASTER_STEM}.log (last 20 lines below):" >&2
    tail -20 "$BBL_DIR/${MASTER_STEM}.log" 2>/dev/null >&2 || tail -20 "$PDFLATEX_LOG" >&2
    exit 1
  fi

  if [ ! -f "$BBL_DIR/${MASTER_STEM}.aux" ]; then
    echo "Phase 01 ERROR: pdflatex produced no .aux at $BBL_DIR/${MASTER_STEM}.aux" >&2
    exit 1
  fi

  # bibtex: read .aux, write .bbl. The .aux references .bib files via
  # paths relative to repo root (e.g. ./BufferStockTheory.bib), so set
  # BIBINPUTS to include repo root for resolution.
  #
  # bibtex returns 2 on per-entry warnings ("Repeated entry", "Missing
  # field", etc.). Those are tolerated: real silent breakage is caught
  # downstream by Phase 05 (unresolved cite key) and Phase 11 (broken
  # cross-ref). Exit 1 = config error (.bib not found at all) — fatal.
  set +e
  BIBINPUTS="$REPO_ROOT:" bibtex "$BBL_DIR/${MASTER_STEM}" >"$BIBTEX_LOG" 2>&1
  bibtex_rc=$?
  set -e
  if [ $bibtex_rc -ne 0 ] && [ $bibtex_rc -ne 2 ]; then
    echo "Phase 01 ERROR: bibtex exited $bibtex_rc during .bbl generation" >&2
    echo "  see $BIBTEX_LOG (last 10 lines below):" >&2
    tail -10 "$BIBTEX_LOG" >&2
    exit 1
  fi

  if [ ! -f "$BBL" ]; then
    echo "Phase 01 ERROR: bibtex did not produce $BBL" >&2
    cat "$BIBTEX_LOG" >&2
    exit 1
  fi

  bbl_lines="$(wc -l < "$BBL")"
  bbl_entries="$(grep -c '^\\harvarditem' "$BBL" || true)"
  echo "  fresh .bbl: $BBL  (${bbl_lines} lines, ${bbl_entries} entries)"
else
  bbl_lines="$(wc -l < "$BBL")"
  bbl_entries="$(grep -c '^\\harvarditem' "$BBL" || true)"
  echo "  cached .bbl (sources unchanged): $BBL  (${bbl_lines} lines, ${bbl_entries} entries)"
fi

# --- recursive \input expansion -------------------------------------------
PYTHONPATH="tools/build-myst" \
python3 tools/build-myst/phases/_01_expand_inputs.py \
  --master "$MASTER_TEX" \
  --bbl    "$BBL" \
  --output "$FLAT" \
  --log    "$BUILD_DIR/01_expand.log"

LINES="$(wc -l < "$FLAT")"
WARN="$(grep -c -E 'WARN' "$BUILD_DIR/01_expand.log" || true)"
echo "  flat tex written: $FLAT (${LINES} lines, ${WARN} unresolved \\input warnings)"
