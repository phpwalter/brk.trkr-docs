---
title: "Inventory"
lang: en
translation_key: "architecture.domains.inventory"
status: authoritative
---

# Inventory

The Inventory domain tracks operational quantities of parts and other stock: what is on hand, available, reserved, allocated, missing, quarantined, or otherwise unavailable for use.

## 1. Purpose and boundaries

Inventory describes **operational stock state**. Ownership establishes the legal/product ownership context; inventory answers how much usable stock exists and where it can be consumed.

A discrete collectible or identifiable physical instance may belong in [Owned Assets](./03-owned-assets.md). Fungible quantities and operational stock positions generally belong here.

## 2. Inventory identity and quantity

An inventory position is defined by the attributes necessary to make quantities safely interchangeable: catalog identity, color/variant, condition, ownership/tenant context, and other lot attributes required by the product.

Quantity fields should distinguish physical on-hand quantity from reservations, allocations, quarantine, or other non-available states. **Available** quantity should be derived from authoritative components rather than independently edited whenever possible.

## 3. Reservations and availability

Reservations protect stock for a project or other consumer without immediately destroying the underlying quantity. Reservation creation and release must be atomic with respect to availability checks.

Expired or abandoned reservations require deterministic cleanup. The system must prevent concurrent requests from reserving more than the available amount.

## 4. Consumption and allocation

Projects consume or allocate inventory through explicit movements. Allocation should record source inventory, quantity, consumer/project, and timing. Releasing an allocation should restore availability according to the lifecycle rules rather than creating an unrelated replacement row.

See [Build & Project Management](./05-build-projects.md) for the consumer side of this relationship.

## 5. Reconciliation and auditing

Physical counts may disagree with recorded quantities. The system should capture adjustment reason, before/after quantity, actor, and source where an inventory correction is made.

Cycle counts and audits must produce durable evidence rather than silently overwriting quantities. Missing, damaged, found, and correction scenarios should be distinguishable when they have different operational meaning.

## 6. Storage and movement

Inventory positions may be stored in bins or other [Storage & Location](./08-storage-location.md) nodes. Moving stock between locations is a movement, not a change in catalog identity.

Partial movement must preserve total quantity accounting. Quarantine or inaccessible locations may make stock physically present but unavailable.

## 7. Concurrency

Quantity changes are concurrency-sensitive. Reservation, allocation, consumption, and adjustment operations require transaction boundaries or equivalent concurrency control so invariant checks and writes cannot race.

The archived documents mention locks and other mechanisms; the exact implementation belongs to the database/API design and must be verified against current repositories.

## 8. Engineering invariants

- **INV-001** — Physical and available quantities MUST NOT become negative.
- **INV-002** — Reserved plus allocated quantities MUST NOT exceed the quantity eligible for those states.
- **INV-003** — Availability MUST be derived consistently from authoritative quantity states.
- **INV-004** — Quantity-changing operations MUST be auditable.
- **INV-005** — Reservation/allocation checks and writes MUST be concurrency-safe.
- **INV-006** — Location movement MUST preserve total quantity unless accompanied by an explicit adjustment/consumption.
- **INV-007** — Inventory MUST reference canonical catalog identity rather than duplicating catalog definitions.

## 9. Source consolidation

This chapter merges the Inventory Domain Specification, Tier 1 Inventory Matrix, inventory schema draft, runtime API draft, and useful concepts from the later inventory-auditing architecture chapter. Speculative distributed-locking/event-sourcing proposals are not treated as current requirements.

## Related documentation

- [Owned Assets](./03-owned-assets.md)
- [Build & Project Management](./05-build-projects.md)
- [Storage & Location](./08-storage-location.md)
- [Cross-cutting Architecture](../cross-cutting.md)
