---
title: "Identity & User Management"
lang: en
translation_key: "architecture.identity-user-management"
status: authoritative
---

# Identity & User Management

This chapter consolidates the archive's user-management, address-management, and subscription notes into one architectural entry point.

## Responsibilities

- User identity and profile lifecycle.
- Authentication identity association.
- User-owned addresses and default-address behavior.
- Soft deletion and auditability where historical references require retention.
- Subscription/account lifecycle integration.
- Separation between user identity and organization/tenant boundaries described in [Core Foundations](./domains/01-core-foundations.md).

## Address management

The archived designs converge on a `user_addresses` concept with operations to list, retrieve, create, update, remove/soft-delete, and establish a default address. Frontend address capture should use structured address fields and keep provider-specific UI concerns separate from the persisted domain model.

### Architectural rules

1. Address records belong to an authenticated user context.
2. A user may have multiple addresses.
3. Default-address selection must be deterministic; setting a new default clears the previous default within the same scope.
4. Deletion must preserve historical references when an address has been used by a transaction, billing record, or other immutable history.
5. Validation belongs at API/domain boundaries even when a third-party UI assists with client-side capture.

## Subscriptions

Subscription state is an account concern and must not be conflated with authentication. Authentication establishes identity; subscription state controls entitlement and product access.

The archived subscription recommendations remain design input rather than a final billing specification. Any payment-provider integration should be validated against current API/database implementations and captured in an ADR when it becomes architectural policy.

## Related documentation

- [Core Foundations](./domains/01-core-foundations.md)
- [Product Capability Map](../product/capabilities.md)
- [Implementation History](../development/implementation-history.md)
