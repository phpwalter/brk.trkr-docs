# Versioning Policy — Brk-Trkr Documentation

Brk-Trkr documentation follows [Semantic Versioning](https://semver.org/) using the form:

`MAJOR.MINOR.PATCH`

Documentation repository versions describe the evolution of this documentation corpus and its published documentation contracts. They do **not** automatically represent the version of the Brk-Trkr application, frontend, API, or database.

## MAJOR version

Increment the MAJOR version when a backward-incompatible documentation contract changes.

Examples include:

- The canonical documentation hierarchy changes incompatibly.
- Published document paths or stable identifiers are removed without compatibility handling.
- `translation_key` semantics or translation-path rules change incompatibly.
- A published API, data, architecture, or product specification is intentionally changed in a backward-incompatible way.
- Documentation governance or interpretation rules change in a way that invalidates existing consumers or translations.

## MINOR version

Increment the MINOR version for backward-compatible additions or substantial expansions.

Examples include:

- A new product or architecture domain is documented.
- A new major documentation section is introduced.
- A new translated language is added.
- New ADR categories or architecture specifications are added.
- New documentation validation, indexing, or publishing capabilities are introduced without breaking existing documentation contracts.

## PATCH version

Increment the PATCH version for backward-compatible corrections and maintenance.

Examples include:

- Typographical or grammatical corrections.
- Clarifications that do not change documented behavior.
- Broken-link or cross-reference fixes.
- Formatting and presentation improvements.
- Index corrections.
- Internal documentation-tooling refactors with no documentation-contract impact.

## Pre-releases

Pre-release versions use these forms:

- `vX.Y.Z-alpha.N`
- `vX.Y.Z-beta.N`
- `vX.Y.Z-rc.N`

Definitions:

- **Alpha** — experimental and unstable; substantial structural or content changes may still occur.
- **Beta** — intended scope is substantially complete and undergoing validation and refinement.
- **RC** — release candidate; no material new scope should be introduced except changes required to reach release quality.

## Canonical source and translations

English documentation under `docs/i18n/en/` is the canonical source language.

Translation updates do not normally require independent repository versions. A release version applies to the documentation corpus as a whole. Translation completeness may vary by language unless a language is explicitly designated as complete for that release.

Stable `translation_key` values are part of the documentation contract. Changing or removing them requires the same compatibility consideration as changing a public document path.

## Release authority

- The Project Owner is the final authority on version assignment.
- MAJOR releases must be explicitly documented in `CHANGELOG.md` and the corresponding GitHub Release notes.
- MINOR and PATCH releases should be recorded in `CHANGELOG.md`.
- Version tags should use the form `vX.Y.Z` or one of the pre-release forms above.

## Relationship to application releases

The documentation repository may be released independently of the Brk-Trkr application repositories.

When documentation describes a version-specific product, API, database, or frontend contract, that relationship should be stated explicitly in the affected documentation or release notes rather than inferred from the documentation repository version.
