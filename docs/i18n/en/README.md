---
title: "Brk-Trkr Documentation"
lang: en
translation_key: "root"
status: authoritative
---

# Brk-Trkr Documentation

This is the authoritative English documentation set for Brk-Trkr.

## Primary sections

1. [Product](./product/README.md) — what Brk-Trkr is, its terminology, capabilities, and user/domain behavior.
2. [Architecture](./architecture/README.md) — how Brk-Trkr is designed, including domains, data, APIs, security, and cross-cutting concerns.
3. [Development](./development/README.md) — how engineers work on Brk-Trkr, including repositories, testing, frontend conventions, and implementation history.

## Indexes

- [Master Index](./INDEX.md)
- [Source Consolidation Map](./SOURCE-MAP.md)
- [Product Index](./product/INDEX.md)
- [Architecture Index](./architecture/INDEX.md)
- [Development Index](./development/INDEX.md)

## Canonical repositories

| Concern | Repository |
|---|---|
| Documentation | `phpwalter/brk.trkr-docs` |
| Frontend | `phpwalter/brk.trkr-fe` |
| API | `phpwalter/brk.trkr-api` |
| Database | `phpwalter/brk.trkr-db` |

## Documentation rules

- Primary documentation describes the current intended system state.
- Significant architectural decisions should be recorded as ADRs.
- Implementation/debug history is preserved as historical evidence, not presented as current architecture.
- Speculative architecture is explicitly labeled as future/research material.
- Cross-references use relative paths so translated trees can preserve equivalent link topology.
