# Governance

## Repository purpose

`phpwalter/brk.trkr-docs` is the canonical documentation repository for Brk-Trkr.

## Authority

The repository maintainer has final responsibility for repository structure, documentation policy, accepted architecture documentation, contributor access, and releases of the documentation set.

## Sources of truth

Documentation should distinguish between:

- **Product documentation** — intended user/domain behavior.
- **Architecture documentation** — accepted system design and technical constraints.
- **Development documentation** — contributor and engineering practices.
- **ADRs** — significant architectural decisions and their rationale.
- **Research/future architecture** — proposals that are not current implementation commitments.
- **Implementation repositories** — source of truth for code, schema, and runtime behavior when documentation conflicts with implementation.

## Change process

Routine editorial changes may be made through normal pull requests.

Changes that alter domain boundaries, architectural invariants, security assumptions, tenancy, persistence strategy, or other significant technical commitments should include or update an Architecture Decision Record when appropriate.

## Documentation ownership

The English documentation tree under `docs/i18n/en/` is canonical. Translations derive from it and should preserve stable `translation_key` identities.

## Indexing and cross-references

Authoritative documents must remain discoverable through the applicable indexes. Cross-references are part of the documentation contract and are validated by CI.

## Deprecation

When an authoritative document or architectural decision is replaced:

1. identify the replacement;
2. update inbound cross-references;
3. change status metadata where appropriate;
4. retain historical material only when it continues to provide useful context.
