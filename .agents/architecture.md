# Architecture

This file is the single source of truth — `AGENTS.md` and `CLAUDE.md` link here rather than duplicating.

## Two independent build paths from one LaTeX source

**Critical contract:** `myst build --html` must produce *exactly* the content `pdflatex BufferStockTheory.tex` produces — no more, no less. This is enforced in `myst.yml` by both `project.toc` (single-page) and `project.exclude` (defence-in-depth against auto-discovery picking up `Code/`, `Appendices/`, slides, private notes, etc.). When LaTeX adds a new `\subfile{}`, the fix belongs in `tools/build-myst/`, not in `myst.yml`'s TOC.

## LaTeX layout

- `BufferStockTheory.tex` — root document; `\subfile`s `Introduction`, `BufferStockTheory-NoAppendix`, then individual appendices from `Appendices/`.
- `BufferStockTheory-NoAppendix.tex` — main body; compilable standalone via the `subfiles` package.
- `Appendices/*.tex` — each is a standalone subfile that can also be compiled on its own (some have local `.bib` files).
- `Figures/*_tikzMake.tex` — TikZ figures compiled by `pdflatex` (handled in `reproduce/document.sh`); other figures are produced by Python notebooks under `Code/Python/`.
- `Tables-All.tex`, `Figures-All.tex`, `Appendices-All-Referenced.tex` — debug-only collectors that the public site explicitly excludes.
- `@local/`, `@resources/` — machine-local path-config macros and shared TeX search paths; both are private and excluded from publication.
- `econark.sty` (in `@resources/texlive/...`) defines the macros (`\GIC`, `\PFGIC`, `\CRRA`, `\DiscFac`, `\PermGroFac`, `\Rfree`, `\Thorn`, etc.) used throughout. The paper sets `\renewcommand{\CRRA}{\gamma}`.
- **Paper-local macros and theorem environments** all live in `@local/local.sty` (paper-agnostic basename — same name in any paper using this skeleton). That file is the canonical home for paper-specific configuration: typography helpers (`\statement`, `\headmath`), economics-symbol overrides (`\CRRA`→γ, `\DiscGro`, `\GPFacMod`, `\Thorn`, `\boundFunc`), figure-inclusion scratchpads (`\figName`/`\figFile`), body-text vocabulary (`\difFunc`, `\GPFacRawName`), the custom `assumL`/`assumS`/`assumI` Assumption environments with their L.n/S.n/I.n counter formatters, and the ~45 `\hyperlink`-pattern named-condition macros. Material that is part of shared infrastructure (e.g. `econark-shortcuts.sty` in `@resources/`) is NOT moved here. New macros for this paper should be added to `@local/local.sty`, not inline in body `.tex` files. The pre-commit hook (`tools/git-hooks/lint-no-inline-defs.sh`) blocks new inline defs in the published body files; `make latex-source-lint` runs the same check in advisory mode against the whole tree.
- **`@local/` layout** (canonical 5-file skeleton, plus `auto/` cache and the `@resources` symlink): `local.sty` (paper-specific style — see prior bullet); `local-tikz.sty` (loaded by `Figures/*_tikzMake.tex` standalone tikz compilation; necessarily separate because tikz figures use `\documentclass{standalone}` and never load the master preamble); `dir-paths.tex` (path macros `\ApndxDir`/`\EqDir`/`\TableDir`, `\input`-ed before `\documentclass` so cannot be a `.sty`); `owner.sty` (per-clone `\owner` configuration — kept separate to allow per-machine override); `econtex_onlyinsubfile.tex` (subfile-mode boilerplate `\input`-ed by `Tables/*-subfile.tex` and `Figures-All.tex`).

## MyST pipeline (`tools/build-myst/`)

12 sequential phases driven by `build.sh`. Each writes a numbered intermediate to `_build/myst/` and is cached by sha256 of its input — re-running on unchanged source produces bit-identical output:

| Phase | Output | Role |
|---|---|---|
| 01 | `01_flat.tex` | `latexpand` flattens `\input{}` chain incl. `.bbl` |
| 02 | `02_stripped.tex` | drops `\ifthenelse{\boolean{Web}}`, `\begin{comment}`, frontmatter |
| 03 | `03_normalized.tex` | rewrites custom commands; emits `<<CITE:>>`, `<<ANCHOR:>>`, `<<XREF:>>`, `<<NAMED:>>` placeholders |
| 04 | `04_raw.md` | `pandoc` latex → markdown |
| 05 | `05_with_cites.md` | `<<CITE:>>` → `(Author, Year)`; appends `## References` |
| 06 | `06_with_xrefs.md` | placeholders + `\eqref` / `\Cref` → MyST refs |
| 07 | `07_with_theorems.md` | `\begin{theorem}` → `:::{prf:theorem}` |
| 08a/08b | `08a_polished.md`, `08b_glossed.md` | `\paragraph` → `###`; figure directives; first-occurrence English glosses for `\GIC`, `\PFGIC`, … |
| 09/10 | `09_clean.md`, `10_final.md` | strip residual `<div>`/TOC; prepend YAML frontmatter |
| 11 | (assertions) | `myst build` smoke test + privacy audit + grep probes |

Final `BufferStockTheory.md` at repo root is the committed deliverable. `_build/` and the older `build-myst/` are gitignored.

Configuration lives in `tools/build-myst/config/`:
- `pipeline.yml` — phase toggles & paths
- `named-conditions.yml` — `\GIC` → "growth impatience condition", etc.
- `theorem-mapping.yml` — `\begin{theorem}` → `prf:theorem`
- `econark-math-macros.tex` — `\newcommand` defs shipped to renderers via `_static/`
- `frontmatter-template.yml` — YAML skeleton

When phase 11 reports unresolved citations, see `_build/myst/05_unresolved_cites.txt` — keys cited but absent from `BufferStockTheory-Add-Refs.bib`. Either add them to the public bib or fix the cite key.

## Privacy boundary

`_private*`, `private_*`, `@local/`, `Private/`, `paperpile_private.bib`, `plans_private/` content **must not** reach published output. Three layers enforce this:

1. `.gitignore` — `*_pri`, `*private` excluded from version control (with explicit `!plans_private/` exception).
2. `.ragignore` — keeps the same patterns out of the RAG index.
3. `myst.yml` `exclude:` and the MyST pipeline's phase-11 privacy audit.

The MyST build's phase 11 will fail loudly if a stray local path or private content slips through. Don't bypass it — fix the offending source line.

## Reproduction script (`reproduce/document.sh`)

Compiles in this order: TikZ figures in `Figures/` → main paper → `BufferStockTheory-NoAppendix` → optional slides → `Figures-All`/`Tables-All` → each appendix as standalone. Each main document gets four `pdflatex` passes with one `bibtex` between passes 2 and 3. Appendices with local `.bib` files get a bibtex pass. Logs every command to `reproduce/document_commands.sh` for replay.

`check_and_restore_pdf_if_formatting_only` runs after compilation: if `pdftotext` of the new PDF matches `pdftotext` of the committed PDF, the script restores the committed binary so PDFs only get re-committed when content actually changed.

## plans_private workflow

When asked to make and later implement a plan, follow the workflow in `plans_private/buffer-stock-theory-plans-private-workflow.md`. Two timestamped files per plan: `YYYYMMDD-HHMMh_<why-slug>.md` and `YYYYMMDD-HHMM+1m_h_<what-slug>.md`. Always ask before writing them.
