---
title: "Core Foundations"
lang: en
translation_key: "architecture.domains.core-foundations"
status: authoritative
---

# Core Foundations

Core Foundations defines the identity, ownership, organizational, collection, visibility, and permission concepts upon which the rest of Brk-Trkr depends.

## 1. Purpose and boundaries

This domain establishes **who** owns or controls data and **how** owned information is organized. It does not define catalog identity, inventory accounting, transaction valuation, or physical storage mechanics; those belong to adjacent domains.

A central principle from the source specifications is that **ownership and organization are different concepts**. A user or organization may own an asset while collections provide one or more logical views over that owned state.

## 2. Collections

A collection is a logical organizational construct, not necessarily a physical container. Collections may represent a personal collection, a project-oriented grouping, a display grouping, an insurance/reporting view, or another product-defined perspective.

Collections may form hierarchies when the product requires nested organization. Hierarchy rules must prevent cycles and must define aggregation behavior so a descendant is not double-counted when totals are calculated across a tree.

### Lifecycle

A collection may move through states such as draft, active, archived, and deleted/retired. The exact persisted state model is implementation-specific, but transitions must preserve historical references when other records depend on the collection.

## 3. Ownership and membership

Ownership identifies the principal responsible for the collection or owned state. Membership associates assets or inventory positions with a collection view.

Membership must not create a second physical asset merely because the same owned entity appears in more than one logical view. Where multi-collection membership is supported, identity remains stable and aggregation rules must prevent accidental duplication.

## 4. Visibility and permissions

Visibility controls who may discover or view a collection. Permission controls what an authorized principal may do. These are related but distinct concerns.

Role or policy evaluation should be cumulative and explicit. A public collection must not implicitly expose private descendant information, personal data, acquisition history, addresses, or other sensitive attributes.

## 5. Tenancy and organizational boundaries

User identity, organization membership, and tenant boundaries must be represented explicitly. Authorization checks must use the active user/organization context rather than trusting client-supplied ownership identifiers.

Database-level row security may be used as defense in depth, but its existence and exact policies must be verified in `brk.trkr-db` before documentation claims implementation.

## 6. Events and auditability

Material changes to collection ownership, membership, visibility, permissions, and lifecycle should be auditable. Domain events may be emitted when they support integration or asynchronous processing, but event transport is a cross-cutting concern rather than part of collection identity.

## 7. Engineering invariants

- **FOUND-001** — Catalog identity MUST NOT be created by collection membership.
- **FOUND-002** — Ownership and logical organization MUST remain distinguishable concepts.
- **FOUND-003** — Collection hierarchies MUST NOT contain cycles.
- **FOUND-004** — Aggregation across nested collections MUST define and prevent double counting.
- **FOUND-005** — Authorization MUST be evaluated against authenticated user/organization context.
- **FOUND-006** — Visibility MUST NOT leak data from more restrictive descendants or related records.
- **FOUND-007** — Destructive lifecycle operations MUST preserve referenced historical data where required.

## 8. Source consolidation

This chapter consolidates the former collection/core domain specification, Tier 1 core-foundation notes, multi-tenancy schema draft, and core identity API draft. Draft SQL/OpenAPI details were not copied verbatim because they must be checked against the current database and API repositories.

## Related documentation

- [Global Catalog](./02-global-catalog.md)
- [Owned Assets](./03-owned-assets.md)
- [Inventory](./04-inventory.md)
- [Identity & User Management](../identity-user-management.md)
- [Cross-cutting Architecture](../cross-cutting.md)
- [Product Glossary](../../product/glossary.md)
