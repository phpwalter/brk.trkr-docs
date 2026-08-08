---
title: "Build & Project Management"
lang: en
translation_key: "architecture.domains.build-projects"
status: authoritative
---

# Build & Project Management

The Build & Project Management domain represents user intent: builds, restorations, MOCs, sorting efforts, or other projects that require parts, milestones, work sessions, and progress tracking.

## 1. Purpose and boundaries

Projects do not own inventory merely because they need it. They request or reserve stock from [Inventory](./04-inventory.md), track requirements, and record progress. This keeps project intent separate from the operational truth of what is physically available.

## 2. Project identity and type

Every project has stable identity, ownership/tenant context, type, lifecycle state, and relevant descriptive metadata. Project types may include builds, restorations, MOCs, part-outs, or other future workflows, but type-specific behavior should extend a common lifecycle rather than create unrelated systems.

## 3. Bill of materials

A project may reference a catalog BOM or define a custom BOM. When catalog BOMs can change, a project should pin the relevant revision or otherwise retain enough information to explain its historical requirements.

Required quantities, satisfied quantities, reserved quantities, missing quantities, and substitutions must have clear semantics.

## 4. Allocation workflow

Projects may reserve inventory before physical consumption. A typical lifecycle is:

1. determine requirement;
2. query eligible inventory;
3. reserve or allocate quantity;
4. physically consume/use quantity when appropriate;
5. release unused reservations;
6. reconcile differences.

Allocation must use the Inventory domain's concurrency rules rather than updating project and inventory quantities independently.

## 5. Progress and completion

Project progress should be derived from explicit milestones, BOM fulfillment, sessions, or other measurable states rather than from a single arbitrary percentage where richer information exists.

Completion does not necessarily imply that every reservation is consumed; closing a project must define how remaining reservations and temporary allocations are handled.

## 6. Build sessions and collaboration

Build sessions capture time-bounded activity and may support notes, progress, or consumed materials. Collaborative projects require explicit membership/permission rules from [Core Foundations](./01-core-foundations.md).

The archived proposal for token locks/optimistic collaboration is an implementation option, not an authoritative requirement.

## 7. Engineering invariants

- **PROJ-001** — Project identity MUST be stable across lifecycle transitions.
- **PROJ-002** — Project requirements MUST remain distinct from physical inventory quantities.
- **PROJ-003** — Inventory allocation MUST occur through concurrency-safe inventory operations.
- **PROJ-004** — BOM revisions used by a project MUST be historically explainable.
- **PROJ-005** — Closing/canceling a project MUST deterministically release or resolve outstanding reservations.
- **PROJ-006** — Progress metrics MUST be derived from defined project state, requirements, or milestones.
- **PROJ-007** — Collaborative access MUST use the platform's authorization model.

## 8. Source consolidation

This chapter consolidates the Build & Project Management Domain Specification, Tier 1 BPM chapter, project/reservation schema draft, and BPM runtime API draft. Advanced collaboration and distributed-locking ideas remain research until the product requires them.

## Related documentation

- [Inventory](./04-inventory.md)
- [Global Catalog](./02-global-catalog.md)
- [Core Foundations](./01-core-foundations.md)
- [Acquisition & Disposal](./07-acquisition-disposal.md)
