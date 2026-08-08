---
title: "Global Catalog"
lang: en
translation_key: "architecture.domains.global-catalog"
status: authoritative
---

# Global Catalog

The Global Catalog domain provides canonical definitions for LEGO-related entities independent of any user's ownership or inventory.

## 1. Purpose and boundaries

The catalog answers **what an entity is**. It does not answer whether a user owns it, where it is stored, what quantity is available, or what a particular owned instance cost.

This separation prevents duplicated catalog metadata across users and allows owned assets, inventory, projects, and valuations to reference stable catalog identities.

## 2. Canonical identity

Catalog entities require stable internal identifiers. External identifiers from LEGO, BrickLink, Rebrickable, LDraw, or other sources should be treated as namespace-scoped cross-references rather than as the sole internal primary key.

External identifiers may change, collide across namespaces, or disappear. Brk-Trkr therefore needs a durable internal identity plus source attribution.

## 3. Entity types

The catalog may model sets, parts/elements, minifigures, colors, themes, categories, instructions, inventories/BOMs, and other shared definitions. Entity-specific properties should remain distinguishable while common metadata uses shared structures where appropriate.

A catalog entity is not an owned asset. A set definition may be referenced by thousands of users while each physical copy is represented separately in [Owned Assets](./03-owned-assets.md).

## 4. Taxonomy and classification

Taxonomy provides navigational and analytical groupings such as theme, category, genre, family, or part category. Taxonomy relationships should be explicit and versionable where upstream sources can change classification over time.

Active/retired status belongs to catalog metadata when it describes the official or source-defined lifecycle of the catalog entity. UI filtering of that status is discussed in [Frontend Patterns](../../development/frontend-patterns.md#catalog-filtering).

## 5. Bill of materials and composition

Sets, minifigures, MOCs, and other composite entities may expose bills of materials. BOM revisions should be identifiable so projects or historical calculations can pin to the version used at the time instead of silently changing when upstream catalog data is corrected.

## 6. Source synchronization and provenance

Catalog ingestion must record source and synchronization metadata sufficiently to explain where data came from. Conflicting upstream values require deterministic precedence or review rules.

Synchronization should be idempotent where practical. A source refresh must not create duplicate canonical entities merely because an external record was re-imported.

## 7. API and persistence guidance

Catalog APIs should expose canonical identity and source cross-references without coupling clients to a specific upstream provider. Search/filter endpoints should treat taxonomy, status, identifiers, and text search as contract-level concepts.

The archived schema/OpenAPI drafts contain useful examples but also over-specify unverified RLS, replication, and synchronization mechanics. Those details require validation against `brk.trkr-db` and `brk.trkr-api`.

## 8. Engineering invariants

- **CAT-001** — Catalog entities MUST be independent of user ownership.
- **CAT-002** — Internal catalog identity MUST remain stable across external-source changes.
- **CAT-003** — External identifiers MUST be namespaced by source/system.
- **CAT-004** — Source attribution MUST be retained for synchronized data.
- **CAT-005** — BOM revisions MUST be distinguishable when downstream consumers depend on historical composition.
- **CAT-006** — Synchronization MUST avoid creating duplicate canonical entities for the same source identity.
- **CAT-007** — User-private ownership data MUST NOT be stored as catalog truth.

## 9. Source consolidation

This chapter merges the original Catalog Domain Specification, Tier 1 Global Catalog chapter, catalog schema draft, and catalog runtime/API draft. The two archived `schema`/`openapi` Chapter 2 files were effectively misclassified by directory; their subject matter has been consolidated here by domain rather than by folder name.

## Related documentation

- [Core Foundations](./01-core-foundations.md)
- [Owned Assets](./03-owned-assets.md)
- [Inventory](./04-inventory.md)
- [Build & Project Management](./05-build-projects.md)
- [System Overview](../system-overview.md)
