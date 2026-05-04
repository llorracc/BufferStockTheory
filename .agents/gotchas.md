# Gotchas

This file is the single source of truth — `AGENTS.md` and `CLAUDE.md` link here rather than duplicating.

- The active `.latexmkrc` is a symlink (`.latexmkrc → .latexmkrc_build-BST-only`). Switch to building all variants with `.latexmkrc_switch-to-build-all.sh`.
- `BufferStockTheory.bib`, `economics.bib`, `latexdefs.tex` are auto-generated/ignored — `latexmk` deletes them at startup. Don't commit them.
- `prompts/` and `HARK_ask-your-project/` at repo root are machine-local symlinks (gitignored).
- `Code/Python/HarKmenberg/` and `_build/templates/.../node_modules/` are large vendored trees — don't search them.
- The `Web` LaTeX boolean controls a stripped-down HTML-targeted variant; the MyST pipeline strips the `\ifthenelse{\boolean{Web}}{...}` blocks entirely (phase 02).
