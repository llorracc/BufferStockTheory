#!/usr/bin/env python3
"""Shared helpers for the canonical-anchor tooling.

Root-relative and variant-agnostic by construction (per project policy):
NO hardcoded repo root, absolute path, or variant repo name anywhere.

  - the repo root is found by walking up to the nearest ancestor that holds
    the @local/ marker dir (@local/_projectname.ltx);
  - project/variant identity is read from the @local/ markers;
  - the paper's filename is derived from the project marker (never literal);
  - the canonical site URL is read from myst.yml's project.url.

So the same module works unchanged when run inside BufferStockTheory-Latest/,
-Public/, -dev/, or a future repo renamed to just BufferStockTheory/.
"""
from __future__ import annotations

import functools
import os
import re


@functools.lru_cache(maxsize=1)
def repo_root() -> str:
    """Nearest ancestor of cwd containing the @local/ marker dir."""
    d = os.getcwd()
    while True:
        if os.path.isfile(os.path.join(d, "@local", "_projectname.ltx")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            raise SystemExit(
                "anchor-lib: no @local/_projectname.ltx found in any ancestor of cwd; "
                "run from inside the project tree."
            )
        d = parent


def _marker(name: str) -> str:
    with open(os.path.join(repo_root(), "@local", name), encoding="utf-8") as fh:
        return fh.read().strip()


def project_name() -> str:
    """e.g. 'BufferStockTheory' — the variant-independent project name."""
    return _marker("_projectname.ltx")


def variant_name() -> str:
    """e.g. 'Latest' / 'Public' / 'dev'."""
    return _marker("_variantname.ltx")


def paper_md() -> str:
    """Absolute path to the built MyST paper, derived from the project marker."""
    return os.path.join(repo_root(), f"{project_name()}.md")


def paper_md_rel() -> str:
    """Repo-root-relative reference to the paper, e.g. 'BufferStockTheory.md'."""
    return f"{project_name()}.md"


@functools.lru_cache(maxsize=1)
def canonical_base() -> str:
    """project.url from myst.yml, '/'-terminated.

    This is the canonical, rename-proof published-site URL (the project-name URL,
    not any variant's GitHub-Pages URL) — read at runtime, never hardcoded.
    """
    with open(os.path.join(repo_root(), "myst.yml"), encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"\s*url:\s*(\S+)", line)
            if m:
                return m.group(1).rstrip("/") + "/"
    raise SystemExit("anchor-lib: project.url not found in myst.yml")


# --- anchor extraction from a built MyST .md -------------------------------
# Two MyST anchor syntaxes survive into the build (cf. tools/concepts_validate.py):
ANCHOR_RE = re.compile(r"^\((?P<id>[A-Za-z0-9_.\-]+)\)=\s*$", re.M)        # (id)=  target lines
LABEL_RE = re.compile(r"^:label:\s*(?P<id>[A-Za-z0-9_.\-]+)\s*$", re.M)    # directive :label:


def html_id(anchor: str) -> str:
    """The id mystmd emits into HTML (it lowercases)."""
    return anchor.lower()


def canonical_url(anchor: str) -> str:
    return canonical_base() + "#" + html_id(anchor)


def all_anchors(md_text: str) -> set:
    return set(ANCHOR_RE.findall(md_text)) | set(LABEL_RE.findall(md_text))
