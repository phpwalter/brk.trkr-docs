---
title: "Source Consolidation Map"
lang: en
translation_key: "source-map"
status: traceability
---

# Source Consolidation Map

This map records how the supplied 120-document archive was treated during consolidation. It is intentionally retained beside the new documentation so useful source material does not disappear without traceability.

## Disposition meanings

- **MERGE** — substantive material consolidated into an authoritative chapter.
- **EXTRACT** — durable concepts retained; duplicated, dated, or unverified implementation detail omitted.
- **FUTURE** — preserved as research/proposal material, not current architecture.
- **HISTORY** — implementation/debug milestone summarized under Development rather than treated as current specification.

## Core domain specifications — MERGE

| Source | Destination |
|---|---|
| `docs2/_old/01_BrixTrackr_Domain_Specification.md` | [Core Foundations](./architecture/domains/01-core-foundations.md) |
| `docs2/_old/02_Catalog_Domain_Specification.md` | [Global Catalog](./architecture/domains/02-global-catalog.md) |
| `docs2/_old/03_Owned_Asset_Domain_Specification.md` | [Owned Assets](./architecture/domains/03-owned-assets.md) |
| `docs2/_old/04_Inventory_Domain_Specification.md` | [Inventory](./architecture/domains/04-inventory.md) |
| `docs2/_old/05_Build_Project_Management_Domain_Specification.md` | [Build & Project Management](./architecture/domains/05-build-projects.md) |
| `docs2/_old/06_Valuation_Market_Intelligence_Domain_Specification.md` | [Valuation](./architecture/domains/06-valuation.md) |
| `docs2/_old/07_Acquisition_Disposal_Transaction_Domain_Specification.md` | [Acquisition & Disposal](./architecture/domains/07-acquisition-disposal.md) |
| `docs2/_old/08_Storage_Location_Management_Domain_Specification.md` | [Storage & Location](./architecture/domains/08-storage-location.md) |
| `docs2/_old/012_High_Performance_Caching.md` | [Cross-cutting Architecture](./architecture/cross-cutting.md#caching-and-synchronization) |

## Tier 1 architecture — MERGE

`docs2/arch/ch01_core_foundations.md` through `ch06_valuation_market_intelligence.md` were merged by domain into Chapters 01–06 under [Domain Architecture](./architecture/domains/README.md).

## Schema and OpenAPI drafts — MERGE / VALIDATE

All six files under `docs2/schema/` and all six under `docs2/openapi/` were classified by **subject**, not by their original directory. Their durable domain concepts were merged into Chapters 01–06. Draft SQL, RLS, replication, and endpoint definitions require validation against `brk.trkr-db` and `brk.trkr-api` before being documented as implemented contracts.

Notably, the archived Chapter 2 catalog files were effectively swapped by tier: `openapi/ch02_catalog_matrix_schema.md` describes a technical design/schema, while `schema/ch02_global_catalog.md` describes a runtime API specification.

## Later architecture chapters

### MERGE into domain chapters

- `ch07_acquisition_disposal.md` → [Acquisition & Disposal](./architecture/domains/07-acquisition-disposal.md)
- `ch08_storage_location.md` → [Storage & Location](./architecture/domains/08-storage-location.md)

### EXTRACT into cross-cutting architecture

The durable concerns from these files were extracted into [Cross-cutting Architecture](./architecture/cross-cutting.md):

- `ch12_caching_and_sync.md`
- `ch13_event_brokerage.md`
- `ch15_inventory_auditing.md`
- `ch29_semantic_search.md`
- `ch30_system_auditing.md`
- `ch33_tenant_isolation.md`
- `ch35_api_rate_limiting.md`
- `ch41_identity_federation.md`
- `ch44_task_queues.md`
- `ch55_schema_migrations.md`
- `ch60_computer_vision.md`

### FUTURE / research

The remaining `_architecture/chapters` files are retained as research topics in [Future / Research Architecture](./architecture/future-architecture.md), including:

- `ch09_marketplace_matrix.md`
- `ch10_shipping_pipelines.md`
- `ch11_team_topology.md`
- `ch14_predictive_ml.md`
- `ch16_custom_elements.md`
- `ch17_hardware_automation.md`
- `ch18_digital_guides.md`
- `ch19_marketplace_matrix.md`
- `ch20_digital_twin_iot.md`
- `ch21_regulatory_compliance.md`
- `ch22_disaster_recovery.md`
- `ch23_data_archival.md`
- `ch24_cache_optimization.md`
- `ch25_graphql_federation.md`
- `ch26_chaos_engineering.md`
- `ch27_business_intelligence.md`
- `ch28_zk_provenance.md`
- `ch31_data_sovereignty.md`
- `ch32_predictive_maintenance.md`
- `ch34_platform_lifecycle.md`
- `ch36_edge_mesh.md`
- `ch37_graph_topology.md`
- `ch38_event_sourcing.md`
- `ch39_distributed_locking.md`
- `ch40_distributed_transactions.md`
- `ch42_spatial_optimization.md`
- `ch43_telemetry_stream.md`
- `ch45_spatial_collision.md`
- `ch46_storage_sharding.md`
- `ch47_global_replication.md`
- `ch48_spatial_trees.md`
- `ch49_live_sync.md`
- `ch50_zero_trust.md`
- `ch51_pathfinding_acceleration.md`
- `ch52_sensor_fusion.md`
- `ch53_inference_pipelines.md`
- `ch54_mesh_simplification.md`
- `ch56_tenant_billing.md`
- `ch57_provenance_ledgers.md`
- `ch58_predictive_resupply.md`
- `ch59_amr_dispatch.md`
- `ch61_cross_border_logistics.md`
- `ch62_chaos_engineering.md`
- `ch63_monorepo_synthesis.md`

The duplicate subject pairs (`ch09`/`ch19` marketplace matrix and `ch26`/`ch62` chaos engineering) are intentionally not promoted as separate authoritative chapters.

## User, address, and subscription documents — MERGE

The following archive files were consolidated into [Identity & User Management](./architecture/identity-user-management.md):

- `docs/ADDRESS_BACKEND_API.md`
- `docs/ADDRESS_FRONTEND_IMPLEMENTATION.md`
- `docs/ADDRESS_HANDLING_ARCHITECTURE.md`
- `docs/ADDRESS_IMPLEMENTATION_SUMMARY.md`
- `docs/ADDRESS_MANAGEMENT.md`
- `docs/ADDRESS_QUICK_REFERENCE.md`
- `docs/README_ADDRESS_HANDLING.md`
- `docs/README_USER_MANAGEMENT.md`
- `docs/USER_MANAGEMENT_ARCHITECTURE.md`
- `docs/USER_MANAGEMENT_QUICK_REFERENCE.md`
- `docs/USER_MANAGEMENT_SUMMARY.md`
- `docs/USER_SCHEMA_COMPARISON.md`
- `docs/SUBSCRIPTION_FLOW_RECOMMENDATIONS.md`

## Product overview sources — EXTRACT

Stable product concepts were extracted from:

- `docs/DOCUMENTATION_INDEX.md`
- `docs/EXECUTIVE_SUMMARY.md`
- `docs/QUICK_REFERENCE.md`

Time-sensitive market-size, roadmap, status, and business claims were not promoted automatically into authoritative documentation.

## Development and implementation notes — HISTORY / EXTRACT

The following files are represented by [Frontend Patterns](./development/frontend-patterns.md), [Testing](./development/testing.md), or [Implementation History](./development/implementation-history.md):

- `ACTIVE_RETIRED_FILTER_ANALYSIS.md`
- `ACTIVE_RETIRED_FILTER_IMPLEMENTATION.md`
- `API_DEMO_PAGE_CREATED.md`
- `BREADCRUMB_FILTER_STYLING.md`
- `BREADCRUMB_FORMAT_UPDATE.md`
- `BREADCRUMB_METADATA_STRUCTURE.md`
- `BREADCRUMB_METADATA_SUMMARY.md`
- `BREADCRUMB_STYLING_SUMMARY.md`
- `CONSOLE_LOGS_CLEANUP.md`
- `DATA_MIGRATION_SUMMARY.md`
- `DEBUG_ACTIVE_RETIRED_FILTER.md`
- `DEBUG_LOGGING_SUMMARY.md`
- `IMPLEMENTATION-COMPLETE.md`
- `PHASE1-IMPLEMENTATION.md`
- `PRIMARY_GENRE_STATUS_UPDATE.md`
- `SETGRID_REFACTORING_COMPLETE.md`
- `SETSDISPLAY_API_ENDPOINT.md`
- `SETS_DISPLAY_IMPLEMENTATION.md`
- `TESTING_GUIDE.md`
- `WISHLIST_IMPLEMENTATION.md`

## Validation rule

Consolidation does **not** prove implementation. Technical claims inherited from design documents must be checked against the current `brk.trkr-fe`, `brk.trkr-api`, and `brk.trkr-db` repositories before being labeled implemented.
