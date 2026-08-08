---
title: "Acquisition & Disposal"
lang: en
translation_key: "architecture.domains.acquisition-disposal"
status: authoritative
---

# Acquisition & Disposal

This domain records transactions that bring owned items into Brk-Trkr, remove them, transfer them, or otherwise change their financial/provenance history.

## 1. Purpose and boundaries

Transaction state and ownership state are distinct. A purchase may be ordered but not received; a sale may be agreed but not shipped or completed. Ownership changes must therefore occur at explicit lifecycle points rather than whenever a transaction record is created.

## 2. Transaction identity and types

Every transaction needs stable identity and a clear type: acquisition/purchase, disposal/sale, trade, transfer, gift, loss, or another product-defined category. A transaction may contain multiple line items and may affect owned assets, inventory, or both.

## 3. Lifecycle

A transaction should move through defined states appropriate to its type. Lifecycle changes must be auditable, and reversal/cancellation behavior must be explicit. Completed financial history should not be silently rewritten to simulate corrections.

## 4. Cost basis

Acquisition cost includes the amounts necessary to represent the user's intended accounting view: item price plus allocated shipping, taxes, fees, discounts, and other landed-cost components where applicable.

Allocation of order-level overhead to line items must use a deterministic rule. The archived proportional-allocation proposal is reasonable but should become an ADR if adopted as policy.

## 5. Currency

Transactions in foreign currency must preserve original amount/currency. If Brk-Trkr stores normalized base-currency cost, the exchange rate and effective timestamp/source used for conversion should also be retained.

## 6. Counterparties and privacy

Counterparty information should be minimal and purpose-specific. Marketplace identifiers, seller/buyer handles, or contact details may be useful for provenance but must respect privacy and retention requirements.

## 7. Ownership and inventory effects

A completed acquisition can instantiate an [Owned Asset](./03-owned-assets.md) or increase [Inventory](./04-inventory.md). A completed disposal can retire/transfer an owned asset or decrease inventory. These effects should be performed through domain operations so stock and ownership invariants remain intact.

## 8. Provenance

Transactions are important provenance anchors. Disposal should not erase acquisition history required for reporting, valuation, or audit. When ownership transfers to another user/tenant, private information must not leak merely because an item identity continues to exist.

## 9. Engineering invariants

- **TXN-001** — Transaction identity MUST be stable and lifecycle changes auditable.
- **TXN-002** — Transaction state MUST remain distinct from ownership state.
- **TXN-003** — Completed cost-basis history MUST NOT be silently overwritten.
- **TXN-004** — Original currency and amount MUST be retained for foreign-currency transactions.
- **TXN-005** — Order-level costs allocated to lines MUST use a deterministic method.
- **TXN-006** — Ownership/inventory changes MUST occur through their respective domain operations.
- **TXN-007** — Cross-tenant transfers MUST NOT expose private counterparty/history data without authorization.

## 10. Source consolidation

This chapter consolidates the Acquisition, Disposal, and Transaction Domain Specification with the later acquisition/disposal architecture chapter. Shipping pipelines, marketplace orchestration, cross-border logistics, and provenance-ledger proposals remain research topics until product requirements justify them.

## Related documentation

- [Owned Assets](./03-owned-assets.md)
- [Inventory](./04-inventory.md)
- [Valuation & Market Intelligence](./06-valuation.md)
- [Storage & Location](./08-storage-location.md)
