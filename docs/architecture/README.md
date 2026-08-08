# Architecture Documentation

This section explains **how Brk-Trkr is designed and how its major technical concerns fit together**.

Authoritative architecture documentation should live here when its primary purpose is to describe system boundaries, technical structure, persistence, APIs, integrations, security, runtime behavior, or operational design.

## Planned structure

- `system-overview.md` — system context, major components, and repository boundaries.
- `domain-model.md` — technical domain boundaries and relationships.
- `data/` — persistence, tenancy, schemas, migrations, and data lifecycle.
- `api/` — API conventions, authentication, errors, and endpoint organization.
- `security/` — identity, authorization, tenancy, PII, and security controls.
- `integrations/` — external systems and integration patterns.
- `operations/` — deployment, observability, caching, background work, resilience, and recovery.
- `adr/` — Architecture Decision Records for significant technical decisions.

## Content rules

- Document the architecture Brk-Trkr actually uses or has explicitly committed to.
- Separate current-state architecture from future proposals and research.
- Avoid promoting speculative enterprise patterns into the authoritative architecture without a concrete requirement or decision.
- Prefer explicit invariants, constraints, and trade-offs over broad aspirational language.
