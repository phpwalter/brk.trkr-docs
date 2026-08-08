#!/usr/bin/env python3
"""Validate localization identity and mirrored documentation structure."""

from __future__ import annotations

import sys

from docs_common import I18N_ROOT, language_directories, load_config, markdown_files, parse_frontmatter, relative


def collect(language: str) -> tuple[dict[str, str], dict[str, str], list[str]]:
    by_key: dict[str, str] = {}
    by_path: dict[str, str] = {}
    errors: list[str] = []
    language_root = I18N_ROOT / language

    for path in markdown_files(language):
        data, _ = parse_frontmatter(path)
        key = data.get("translation_key")
        rel = path.relative_to(language_root).as_posix()
        if not isinstance(key, str) or not key.strip():
            continue
        if key in by_key:
            errors.append(
                f"{relative(path)}: duplicate translation_key {key!r}; also used by {by_key[key]}"
            )
        by_key[key] = relative(path)
        by_path[rel] = key
    return by_key, by_path, errors


def main() -> int:
    config = load_config()
    canonical = config["canonical_language"]
    require_mirrored = bool(config["translation"].get("require_mirrored_paths", True))
    errors: list[str] = []

    languages = [path.name for path in language_directories()]
    if canonical not in languages:
        errors.append(f"canonical language directory docs/i18n/{canonical}/ is missing")
        canonical_keys: dict[str, str] = {}
        canonical_paths: dict[str, str] = {}
    else:
        canonical_keys, canonical_paths, canonical_errors = collect(canonical)
        errors.extend(canonical_errors)

    for language in languages:
        keys, paths, language_errors = collect(language)
        errors.extend(language_errors)

        if config["translation"].get("require_language_readme", True):
            readme = I18N_ROOT / language / "README.md"
            if not readme.exists():
                errors.append(f"{relative(readme)}: required language README is missing")

        if language == canonical:
            continue

        for key, source_path in keys.items():
            if key not in canonical_keys:
                errors.append(
                    f"{source_path}: translation_key {key!r} does not exist in canonical language {canonical!r}"
                )

        if require_mirrored:
            for rel_path, key in paths.items():
                expected_key = canonical_paths.get(rel_path)
                if expected_key is None:
                    errors.append(
                        f"docs/i18n/{language}/{rel_path}: no canonical document exists at mirrored path docs/i18n/{canonical}/{rel_path}"
                    )
                elif expected_key != key:
                    errors.append(
                        f"docs/i18n/{language}/{rel_path}: translation_key {key!r} does not match canonical key {expected_key!r}"
                    )

        translated = len(set(keys) & set(canonical_keys))
        total = len(canonical_keys)
        percent = (translated / total * 100.0) if total else 100.0
        print(f"{language}: {translated}/{total} canonical documents translated ({percent:.1f}%)")

    if errors:
        print("i18n validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("i18n validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
