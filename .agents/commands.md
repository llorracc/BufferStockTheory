# Commands

Build commands for the BufferStockTheory repo. This file is the single source of truth — `AGENTS.md` and `CLAUDE.md` link here rather than duplicating.

## LaTeX → PDF (canonical paper)

```bash
latexmk BufferStockTheory          # uses .latexmkrc → .latexmkrc_build-BST-only
./reproduce/document.sh --quiet    # full reproduction (figures, tables, all appendices, slides)
./reproduce.sh                     # full pipeline: install deps, run notebooks, then document.sh
./reproduce/computed.sh MIN        # MIN skips long-running notebooks; MAX runs them all (hours)
```

## LaTeX → MyST Markdown → HTML site (separate pipeline)

```bash
make myst              # tools/build-myst/build.sh → BufferStockTheory.md (~2 min warm)
make myst-clean
make myst-test         # pytest in tools/build-myst/tests/
make myst-validate     # re-run only phase 11 (validation)
make myst-site         # rm -rf _build/site && myst build --html (single-page site)
make myst-site-check   # asserts exactly one content page in _build/site/
```

## Prerequisites

The MyST pipeline needs `latexpand`, `pandoc`, `mystmd` (`npm i -g mystmd`), and a Python with `PyYAML`. It picks Python in this order: `$BST_MYST_PYTHON`, `/usr/bin/python3`, `python3`.
