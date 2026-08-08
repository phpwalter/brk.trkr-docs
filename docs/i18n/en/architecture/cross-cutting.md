---
title: "Cross-cutting Architecture"
lang: en
translation_key: "architecture.cross-cutting"
status: authoritative
---

# Cross-cutting Architecture

Cross-cutting concerns apply across multiple Brk-Trkr domains. The source archive contains extensive proposals in this area; this document preserves useful concerns without promoting unverified implementation claims.

## Tenancy and isolation

Tenant and organization boundaries MUST be enforced consistently in API authorization and database access. See [Core Foundations](./domains/01-core-foundations.md). Row-level security may be used as defense in depth, but documentation must not claim it is active until verified in `brk.trkr-db`.

## Identity federation

External identity providers may establish authentication identity. Authorization remains a Brk-Trkr responsibility and must map authenticated identity to user, organization, role, and entitlement context.

## Caching and synchronization

Caching is appropriate for read-heavy catalog and derived-value workloads. Every cache must have an explicit source of truth, invalidation strategy, and consistency expectation. A cache must not silently become an authoritative store.

## Events and background jobs

Asynchronous processing is appropriate for imports, catalog synchronization, valuation refreshes, image/vision processing, notifications, and other long-running work. Event brokerage, task queues, and event sourcing are separate patterns and must not be treated as interchangeable.

## Auditing

Security-sensitive and financially relevant state transitions should produce durable audit evidence. Examples include ownership changes, inventory adjustments, reservations, transaction changes, and administrative actions.

## API rate limiting

Rate limits should protect public or resource-intensive API surfaces and should be defined per identity or tenant context where appropriate. Limits and responses belong in the API contract rather than only at infrastructure level.

## Schema migrations

Database evolution requires ordered, repeatable migrations. Destructive changes should provide explicit migration and forward-recovery strategies. Current migration practice should be verified against `brk.trkr-db`.

## Search and semantic retrieval

Keyword/filter search is a baseline capability. Semantic search can be layered onto catalog metadata or user content when it provides demonstrated value; vector infrastructure is not a prerequisite for the core domain model.

## Computer vision

Computer vision is relevant to part/set recognition workflows. It should produce confidence-scored observations, not authoritative catalog or inventory state without validation.

## Related documentation

- [Future / Research Architecture](./future-architecture.md)
- [Architecture Decision Records](./adr/README.md)
- [System Overview](./system-overview.md)
