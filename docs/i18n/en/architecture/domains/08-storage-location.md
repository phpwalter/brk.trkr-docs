---
title: "Storage & Location"
lang: en
translation_key: "architecture.domains.storage-location"
status: authoritative
---

# Storage & Location

The Storage & Location domain answers a practical question: **where is a physical asset or inventory quantity located?**

## 1. Purpose and boundaries

Location is not ownership and is not inventory identity. Moving a part from one bin to another changes placement, not what the part is or who owns it.

The domain provides reusable physical/logical location nodes consumed by [Owned Assets](./03-owned-assets.md) and [Inventory](./04-inventory.md).

## 2. Location hierarchy

Locations may form a hierarchy such as site → room → cabinet → drawer → bin. Hierarchies must prevent cycles and should provide a deterministic human-readable path for retrieval.

A location node may represent physical or logical placement. Node type should make behavior explicit rather than requiring clients to infer semantics from labels.

## 3. Placement

Placement associates an owned asset or inventory position with a location. Quantity-based inventory may be split across multiple locations; if so, each placement must state the quantity at that location and total placement must reconcile with the authoritative inventory quantity model.

## 4. Capacity

Capacity may be modeled when it provides practical value. Capacity units must be explicit because a drawer's volume, weight limit, slot count, and item count are not interchangeable measures.

Capacity is advisory unless the product explicitly enforces it. An over-capacity state should be distinguishable from a data-integrity failure.

## 5. Movement

Relocation should be an explicit operation with source, destination, actor, time, and affected asset/quantity. Partial inventory moves must preserve total stock. Moving a parent physical container may imply descendant physical relocation, but whether descendant paths are materialized or derived is an implementation decision.

## 6. Retrieval

Stable paths, labels, barcodes/QR codes, and search may support retrieval workflows. Advanced route optimization or robotics is not required for the core location model.

## 7. Environmental metadata

Environmental properties such as temperature, humidity, light exposure, or protection class may be associated with storage locations if product requirements justify them. Sensor fusion and predictive maintenance are research topics, not current foundational requirements.

## 8. Engineering invariants

- **LOC-001** — Location hierarchies MUST NOT contain cycles.
- **LOC-002** — Physical placement MUST remain distinct from ownership and catalog identity.
- **LOC-003** — Quantity split across locations MUST reconcile with authoritative inventory totals.
- **LOC-004** — Movement MUST identify source and destination and preserve quantity unless accompanied by another explicit operation.
- **LOC-005** — Location paths SHOULD be deterministic and human-retrievable.
- **LOC-006** — Capacity units MUST be explicit when capacity is modeled.
- **LOC-007** — Moving a location MUST NOT silently create or destroy owned assets/inventory.

## 9. Source consolidation

This chapter consolidates the Storage & Location Management Domain Specification and later storage/location architecture chapter. Spatial trees, pathfinding acceleration, collision detection, AMR dispatch, IoT telemetry, and sensor-fusion proposals remain in the research backlog.

## Related documentation

- [Inventory](./04-inventory.md)
- [Owned Assets](./03-owned-assets.md)
- [Core Foundations](./01-core-foundations.md)
- [Future / Research Architecture](../future-architecture.md)
