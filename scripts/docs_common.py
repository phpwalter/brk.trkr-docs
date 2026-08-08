#!/usr/bin/env python3
"""Shared helpers for Brk-Trkr documentation validation."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "docs"
I18N_ROOT = DOCS_ROOT / "i18n"
CONFIG_PATH = ROOT / "config" / "docs-schema.yaml"


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def markdown_files(language: str | None = None) -> list[Path]:
    base = I18N_ROOT / language if language else I18N_ROOT
    if not base.exists():
        return []
    return sorted(path for path in base.rglob("*.md") if path.is_file())


def language_directories() -> list[Path]:
    if not I18N_ROOT.exists():
        return []
    return sorted(
        path
        for path in I18N_ROOT.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{relative(path)}: unterminated YAML front matter")

    raw = text[4:end]
    body = text[end + 5 :]
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{relative(path)}: front matter must be a mapping")
    return data, body


def relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def github_anchor(heading: str) -> str:
    value = heading.strip().lower()
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    value = value.replace(" ", "-")
    value = re.sub(r"-+", "-", value)
    return value.strip("-")


def heading_anchors(path: Path) -> set[str]:
    _, body = parse_frontmatter(path)
    anchors: set[str] = set()
    seen: dict[str, int] = {}

    in_fence = False
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        base = github_anchor(match.group(1))
        count = seen.get(base, 0)
        seen[base] = count + 1
        anchor = base if count == 0 else f"{base}-{count}"
        anchors.add(anchor)
    return anchors
