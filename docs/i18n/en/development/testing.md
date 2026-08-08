---
title: "Testing"
lang: en
translation_key: "development.testing"
status: authoritative
---

# Testing

The archive contains feature-level testing notes and manual verification procedures. This chapter consolidates them into durable guidance; repository-specific commands should be checked against the current project configuration before use.

## Testing layers

### Unit tests
Test pure domain logic, transformations, validation, utility code, and isolated component behavior.

### Integration tests
Test boundaries between API handlers/services, persistence, external-provider adapters, and frontend data clients.

### Contract tests
Validate assumptions shared between frontend, API, and database layers. API schema and error-shape changes should be tested as contracts, not only as implementation details.

### End-to-end tests
Cover critical user workflows such as authentication, catalog navigation, inventory updates, project allocation, address management, and other high-value flows.

## Regression testing

When a defect is fixed, prefer a test that reproduces the failure before the fix. Historical debugging notes in the archive are useful sources for regression scenarios, especially around active/retired catalog filtering and route-driven state.

## Test data

Fixtures should be deterministic, minimal, and explicit about ownership/tenant context. Avoid tests that depend on unstable external catalog services unless the purpose is explicitly an integration test.

## Related documentation

- [Repository Structure](./repository-structure.md)
- [Frontend Patterns](./frontend-patterns.md)
- [Architecture](../architecture/README.md)
