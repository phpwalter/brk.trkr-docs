#!/usr/bin/env python3
"""Validate documentation front matter."""

from __future__ import annotations

import sys

from docs_common import language_directories, load_config, markdown_files, parse_frontmatter, relative


def main() -> int:
    config = load_config()
    required = set(config["frontmatter"]["required"])
    allowed_status = set(config["frontmatter"]["allowed_status"])
    errors: list[str] = []

    for language_dir in language_directories():
        language = language_dir.name
        for path in markdown_files(language):
            try:
                data, _ = parse_frontmatter(path)
            except ValueError as exc:
                errors.append(str(exc))
                continue

            if not data:
                errors.append(f"{relative(path)}: missing YAML front matter")
                continue

            missing = sorted(required - set(data))
            if missing:
                errors.append(f"{relative(path)}: missing front matter fields: {', '.join(missing)}")

            if data.get("lang") != language:
                errors.append(
                    f"{relative(path)}: lang={data.get('lang')!r} does not match directory {language!r}"
                )

            status = data.get("status")
            if status is not None and status not in allowed_status:
                errors.append(
                    f"{relative(path)}: unsupported status {status!r}; allowed: {', '.join(sorted(allowed_status))}"
                )

            for field in ("title", "translation_key", "status"):
                if field in data and (not isinstance(data[field], str) or not data[field].strip()):
                    errors.append(f"{relative(path)}: {field} must be a non-empty string")

    if errors:
        print("Front matter validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Front matter validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
