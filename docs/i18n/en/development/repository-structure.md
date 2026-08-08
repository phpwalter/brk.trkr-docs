---
title: "Repository Structure"
lang: en
translation_key: "development.repositories"
status: authoritative
---

# Repository Structure

Brk-Trkr is split across four canonical repositories.

| Repository | Responsibility |
|---|---|
| `phpwalter/brk.trkr-docs` | Product, architecture, and development documentation |
| `phpwalter/brk.trkr-fe` | User-facing frontend application and UI behavior |
| `phpwalter/brk.trkr-api` | Application API and backend/domain services |
| `phpwalter/brk.trkr-db` | Database schema, migrations, and database-specific behavior |

## Documentation source of truth

Documentation should describe behavior that can be traced to the appropriate code repository. When documentation and implementation disagree, investigate the discrepancy rather than silently treating either as correct.

## Cross-repository changes

Features that alter contracts across layers should update all affected repositories and relevant documentation in the same delivery cycle where practical.
