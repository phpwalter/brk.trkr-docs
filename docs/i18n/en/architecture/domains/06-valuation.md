---
title: "Valuation & Market Intelligence"
lang: en
translation_key: "architecture.domains.valuation"
status: authoritative
---

# Valuation & Market Intelligence

This domain ingests market observations and derives values for catalog entities, owned assets, inventory, and collections without replacing historical accounting data.

## 1. Purpose and boundaries

**Market value is not cost basis.** Acquisition cost is historical transaction data; valuation is a derived estimate that may change whenever market observations, condition, completeness, currency, or valuation methodology changes.

The valuation domain should therefore behave primarily as a read/derived model over catalog, ownership, inventory, and transaction data.

## 2. Market observations

Price observations require source, timestamp, currency, item identity, condition/context, and enough metadata to judge comparability. Raw observations should remain distinguishable from normalized or aggregated values.

Outlier handling may use statistical techniques, but the method must be documented and reproducible. The archive proposes IQR/Winsorization and other algorithms; those are candidate implementations rather than universal requirements.

## 3. Currency normalization

Historical market observations should retain original currency/value and the exchange-rate context used for normalized reporting. Recomputing old prices with today's exchange rate changes meaning and should be an explicit analytical operation, not a silent mutation.

## 4. Condition and completeness

Owned-asset valuations may depend on condition, completeness, sealed/open state, packaging, minifigure inclusion, or other product-specific attributes. These adjustments must be transparent enough to explain why two copies of the same catalog entity have different estimates.

## 5. Portfolio valuation

Collection/portfolio totals aggregate lower-level valuations. Aggregation must avoid double counting where collections overlap or hierarchies include the same underlying asset through multiple views.

## 6. Appraisals and snapshots

An appraisal or valuation snapshot should record methodology/version, source data cutoff, timestamp, currency, and the resulting value. Historical snapshots must remain reproducible enough for insurance/reporting scenarios.

## 7. Forecasting

Forecasts and predictive market intelligence are optional derived capabilities. They must be labeled as estimates and must not overwrite observed market history. Model confidence and training/data window should be retained when machine learning is used.

## 8. Engineering invariants

- **VAL-001** — Market value MUST NOT overwrite acquisition cost or other historical transaction values.
- **VAL-002** — Raw market observations MUST retain source and timestamp.
- **VAL-003** — Currency normalization MUST retain original monetary context.
- **VAL-004** — Valuation methodology/version SHOULD be identifiable for durable appraisal snapshots.
- **VAL-005** — Portfolio aggregation MUST prevent double counting.
- **VAL-006** — Forecasts MUST be distinguishable from observed prices and current appraisals.
- **VAL-007** — Derived caches MUST remain rebuildable from authoritative source data.

## 9. Source consolidation

This chapter merges the Valuation & Market Intelligence Domain Specification, Tier 1 valuation chapter, market schema draft, and valuation API draft. Predictive ML, BI, and forecasting chapters remain research inputs unless validated as active product requirements.

## Related documentation

- [Owned Assets](./03-owned-assets.md)
- [Acquisition & Disposal](./07-acquisition-disposal.md)
- [Global Catalog](./02-global-catalog.md)
- [Cross-cutting Architecture](../cross-cutting.md)
