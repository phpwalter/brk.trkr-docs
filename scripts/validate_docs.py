#!/usr/bin/env python3
"""Validate Brk-Trkr documentation structure and index coverage."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from docs_common import I18N_ROOT, ROOT, language_directories, load_config, markdown_files, parse_frontmatter, relative

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)#]+)(?:#[^)]+)?\)")


def linked_markdown(index_path: Path) -> set[Path]:
    linked: set[Path] = set()
    text = index_path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target_text = raw.strip().split(' "', 1)[0]
        if target_text.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        target = (index_path.parent / target_text).resolve()
        if target.is_dir():
            target = target / "README.md"
        if target.suffix.lower() == ".md":
            linked.add(target)
    return linked


def applicable_index(path: Path, language_root: Path) -> Path:
    current = path.parent
    while current != language_root.parent:
        candidate = current / "INDEX.md"
        if candidate.exists():
            return candidate
        if current == language_root:
            break
        current = current.parent
    return language_root / "INDEX.md"


def main() -> int:
    config = load_config()
    errors: list[str] = []

    for required in config.get("required_root_paths", []):
        target = ROOT / required
        if not target.exists():
            errors.append(f"missing required path: {required}")

    required_sections = config.get("required_sections", [])
    statuses_requiring_index = set(config["indexing"].get("statuses_requiring_index", []))
    exempt_filenames = set(config["indexing"].get("exempt_filenames", []))

    for language_dir in language_directories():
        for section in required_sections:
            section_dir = language_dir / section
            if not section_dir.is_dir():
                errors.append(f"{relative(section_dir)}: required section directory is missing")
            for filename in ("README.md", "INDEX.md"):
                required_file = section_dir / filename
                if not required_file.exists():
                    errors.append(f"{relative(required_file)}: required section index file is missing")

        index_cache: dict[Path, set[Path]] = {}
        for path in markdown_files(language_dir.name):
            if path.name in exempt_filenames:
                continue
            data, _ = parse_frontmatter(path)
            if data.get("status") not in statuses_requiring_index:
                continue

            index = applicable_index(path, language_dir)
            if not index.exists():
                errors.append(f"{relative(path)}: no applicable INDEX.md exists")
                continue

            links = index_cache.setdefault(index, linked_markdown(index))
            if path.resolve() not in links:
                errors.append(
                    f"{relative(path)}: authoritative document is not referenced by {relative(index)}"
                )

    if errors:
        print("Documentation structure validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Documentation structure and index coverage validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
