# Contributing to Brk-Trkr Documentation

Thank you for improving Brk-Trkr documentation.

## Scope

This repository contains project documentation, documentation governance, validation scripts, and CI used to keep the documentation coherent.

## Before you contribute

1. Read the [repository README](./README.md).
2. Review the [English documentation index](./docs/i18n/en/INDEX.md).
3. Follow the existing directory and front-matter conventions.
4. Prefer updating an authoritative document over creating a competing document for the same subject.

## Documentation conventions

Authoritative translated documentation lives under `docs/i18n/<language>/`.

English is the canonical source language:

```text
docs/i18n/en/
```

Translated documents should mirror the English path structure and preserve the same `translation_key`.

## Front matter

Authoritative documents require:

```yaml
---
title: "Document title"
lang: en
translation_key: "stable.logical.key"
status: authoritative
---
```

Allowed status values are defined in `config/docs-schema.yaml`.

## Cross-references

- Use relative Markdown links.
- Prefer links to authoritative documents.
- Do not link to superseded archive paths.
- Verify heading anchors when linking to document sections.
- Keep translated cross-reference topology equivalent to the English source wherever practical.

## Pull requests

A documentation pull request should:

- explain what changed and why;
- identify affected sections or domains;
- update indexes when authoritative documents are added or removed;
- preserve translation identity metadata;
- pass all blocking documentation CI checks.

## CI expectations

Blocking validation includes:

- Markdown hygiene;
- documentation structure and index coverage;
- front-matter validation;
- internal file and anchor links;
- i18n identity and mirrored paths.

Spell checking is advisory. External-link auditing runs separately because external services can fail transiently.

## Significant architecture decisions

Do not bury major architectural decisions in general prose. Use an Architecture Decision Record under:

```text
docs/i18n/en/architecture/adr/
```

See the ADR README for the expected structure.

## Historical material

Implementation notes, debugging records, and superseded designs should not be presented as current architecture. Consolidate durable guidance into the authoritative documentation and preserve history only when it remains useful.
