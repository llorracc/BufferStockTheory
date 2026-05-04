# AGENTS.md

Guidance for coding agents (Claude Code, Cursor, Codex, …) working in this repo.

## Repository purpose

Source for the academic paper *Theoretical Foundations of Buffer Stock Saving* (Carroll). The repo produces three artifacts from one shared LaTeX source:

1. **PDF** (`BufferStockTheory.pdf`) via `pdflatex` / `latexmk`.
2. **Single-page MyST web site** (`_build/site/`) via `mystmd`, fed by a generated `BufferStockTheory.md`.
3. **Computational figures** via Jupyter notebooks under `Code/Python/` that depend on `econ-ark/HARK`.

## Where to find what

The detailed guidance lives in `.agents/`. Each file is the **single source of truth** for its topic — read the relevant file directly rather than copying its content elsewhere.

- [`.agents/commands.md`](.agents/commands.md) — build, reproduce, and MyST-pipeline commands.
- [`.agents/architecture.md`](.agents/architecture.md) — the two build paths, LaTeX layout, MyST pipeline phases, privacy boundary, reproduction script, and `plans_private/` workflow.
- [`.agents/gotchas.md`](.agents/gotchas.md) — non-obvious traps (symlinked `.latexmkrc`, auto-generated bib files, vendored trees, the `Web` boolean).
- [`.agents/debug-pdf-bisection.md`](.agents/debug-pdf-bisection.md) — when a "should-be-cosmetic" source edit changes the PDF, bisect over `\subfile{}` entries to localize the drift. Driver: `tools/private/bisect_pdf.sh <golden-branch>`.

## Tool-specific notes

- `CLAUDE.md` — Claude Code-specific guidance only; everything tool-agnostic lives here or in `.agents/`.

## Editing rule

`.agents/*.md` is canonical. Don't duplicate its content into `AGENTS.md` or `CLAUDE.md` — link to it instead. This keeps the docs free of the propagation loops that mirrored content invites.
