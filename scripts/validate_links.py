#!/usr/bin/env python3
"""Validate internal Markdown links and heading anchors."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

from docs_common import DOCS_ROOT, heading_anchors, load_config, markdown_files, relative

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def split_target(raw: str) -> tuple[str, str]:
    value = raw.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    # Strip an optional Markdown title after the URL/path.
    if " \"" in value:
        value = value.split(" \"", 1)[0]
    if "#" in value:
        path, anchor = value.split("#", 1)
        return unquote(path), unquote(anchor)
    return unquote(value), ""


def main() -> int:
    config = load_config()
    forbidden = config.get("links", {}).get("forbidden_internal_fragments", [])
    errors: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}

    for source in markdown_files():
        text = source.read_text(encoding="utf-8")
        in_fence = False
        for line_number, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            for match in LINK_RE.finditer(line):
                raw = match.group(1)
                path_part, anchor = split_target(raw)

                if path_part.startswith(("http://", "https://", "mailto:", "tel:")):
                    continue

                for fragment in forbidden:
                    if fragment in raw:
                        errors.append(
                            f"{relative(source)}:{line_number}: forbidden legacy/placeholder link fragment {fragment!r}"
                        )

                if path_part.startswith("/"):
                    errors.append(
                        f"{relative(source)}:{line_number}: internal link must be relative, not absolute: {raw}"
                    )
                    continue

                target = source if not path_part else (source.parent / path_part).resolve()
                try:
                    target.relative_to(DOCS_ROOT.resolve())
                except ValueError:
                    errors.append(
                        f"{relative(source)}:{line_number}: link escapes docs tree: {raw}"
                    )
                    continue

                if target.is_dir():
                    target = target / "README.md"

                if not target.exists():
                    errors.append(
                        f"{relative(source)}:{line_number}: missing internal target {raw}"
                    )
                    continue

                if anchor:
                    if target.suffix.lower() != ".md":
                        errors.append(
                            f"{relative(source)}:{line_number}: anchor used on non-Markdown target {raw}"
                        )
                        continue
                    anchors = anchor_cache.setdefault(target, heading_anchors(target))
                    if anchor not in anchors:
                        errors.append(
                            f"{relative(source)}:{line_number}: missing anchor #{anchor} in {relative(target)}"
                        )

    if errors:
        print("Internal link validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Internal link validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
