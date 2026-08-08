---
title: "Frontend Patterns"
lang: en
translation_key: "development.frontend-patterns"
status: authoritative
---

# Frontend Patterns

This chapter consolidates recurring frontend lessons from the archive. Current implementation details must be checked against `phpwalter/brk.trkr-fe` before changing code.

## URL-driven state

Filter, sort, and pagination state that should survive refresh/navigation belongs in route/query state rather than isolated component state. Route synchronization should be debounced when high-frequency UI interaction would otherwise create excessive navigation updates.

## Catalog filtering

Archived active/retired work crossed catalog explorer, parent orchestration, and set display components. The durable pattern is to define one authoritative filter model and pass it through component boundaries without reinterpreting status semantics at each layer.

## Breadcrumb metadata

Breadcrumbs evolved from simple strings toward structured metadata carrying taxonomy/status context. Structured breadcrumb objects are preferable when rendering, filtering, and accessibility depend on more than display text.

## Component boundaries

Container/orchestrator components should own route coordination and data-flow composition; display components should focus on rendering and interaction. Avoid duplicating business filtering logic in multiple UI layers.

## Logging

Temporary diagnostic logging should be removed or gated before production. Durable observability belongs in deliberate logging/telemetry mechanisms rather than ad-hoc console output.

## Address UI

Address capture is a presentation concern that feeds a provider-neutral address domain model. Third-party UI components may assist with capture or validation but should not dictate persisted schema.

## Related documentation

- [Capability Map](../product/capabilities.md)
- [Identity & User Management](../architecture/identity-user-management.md)
- [Implementation History](./implementation-history.md)
