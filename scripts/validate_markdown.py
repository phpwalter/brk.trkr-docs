#!/usr/bin/env python3
"""Apply deterministic Markdown hygiene checks without a renderer dependency."""

from __future__ import annotations

import sys

from docs_common import DOCS_ROOT, relative


def main() -> int:
    errors: list[str] = []
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if text and not text.endswith("\n"):
            errors.append(f"{relative(path)}: file must end with a newline")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip(" \t") != line:
                errors.append(f"{relative(path)}:{line_number}: trailing whitespace")
            if "\t" in line:
                errors.append(f"{relative(path)}:{line_number}: tab character; use spaces")

    if errors:
        print("Markdown style validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Markdown style validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
