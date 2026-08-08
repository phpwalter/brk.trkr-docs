---
title: "Owned Assets"
lang: en
translation_key: "architecture.domains.owned-assets"
status: authoritative
---

# Owned Assets

The Owned Assets domain represents specific physical things owned or controlled by a user or organization.

## 1. Purpose and boundaries

An owned asset is an **instance**, not a catalog definition. Two users may own the same catalog set, and one user may own several physical copies; each owned instance has its own identity, condition, completeness, provenance, storage relationship, and financial history.

Loose fungible quantities are generally better modeled by [Inventory](./04-inventory.md), although inventory and owned assets may reference each other where a physical item is decomposed or assembled.

## 2. Identity

Every owned asset needs a stable internal identifier. Asset identity must survive location changes, collection reorganization, valuation updates, and normal lifecycle transitions.

The source archive proposed certificate-like identity and deterministic partitioning for bulk cases. Those are design ideas, not mandatory mechanisms. The authoritative requirement is stable instance identity and traceable transformations.

## 3. Condition and completeness

Condition and completeness are separate dimensions. A set can be in excellent physical condition while missing parts; another can be complete but heavily used.

Condition vocabularies should be explicit and consistent across UI, API, persistence, valuation, and reporting. Completeness should be derivable or recorded according to the type of asset and the available BOM/reference data.

## 4. Ownership lifecycle

Acquisition creates or establishes owned state. Disposal removes ownership while preserving provenance and financial history. Transfers between organization/user contexts must define whether identity moves, whether private history is sanitized, and which records remain visible to each party.

Transaction processing belongs primarily in [Acquisition & Disposal](./07-acquisition-disposal.md); this domain consumes the resulting ownership state.

## 5. Storage and provenance

Owned assets may be associated with a physical [Storage & Location](./08-storage-location.md) node. Moving an asset changes its placement, not its identity.

Provenance may include acquisition source, previous ownership information when legitimately retained, documentation, certificates, receipts, images, and relevant transaction references.

## 6. Composite assets and decomposition

Some owned assets contain other meaningful components. Decomposition must not silently duplicate ownership. If an owned set is parted out into inventory, the system needs an explicit transformation that preserves the relationship between source asset and resulting inventory movements.

## 7. Valuation boundary

Cost basis is historical transaction information; market value is derived information. Owned Assets references both but should not conflate them. Current market calculations belong in [Valuation & Market Intelligence](./06-valuation.md).

## 8. Engineering invariants

- **ASSET-001** — Every physical owned instance MUST have stable identity.
- **ASSET-002** — Owned asset identity MUST remain distinct from catalog identity.
- **ASSET-003** — Condition and completeness MUST be modeled as separate concepts.
- **ASSET-004** — Location changes MUST NOT change asset identity.
- **ASSET-005** — Disposal MUST preserve required provenance and historical financial references.
- **ASSET-006** — Decomposition into inventory MUST be explicit and auditable.
- **ASSET-007** — Market value MUST NOT overwrite historical acquisition cost.

## 9. Source consolidation

This chapter consolidates the Owned Asset Domain Specification, Tier 1 owned-asset context, relational schema draft, and runtime API draft. Draft implementation details remain validation candidates for the current API and database repositories.

## Related documentation

- [Global Catalog](./02-global-catalog.md)
- [Inventory](./04-inventory.md)
- [Acquisition & Disposal](./07-acquisition-disposal.md)
- [Storage & Location](./08-storage-location.md)
- [Valuation & Market Intelligence](./06-valuation.md)
