# 03 — Analyze trade-offs and compare implementations

**Milestone:** [M2 — Implementation Design Space Analysis & Policy Recommendation](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/2) · **Status:** Proposed

## Outcome

A traceable comparison showing which candidates satisfy requirements and at what cost.

## Acceptance criteria

- All candidates use the [common evaluation framework](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/15) and the same evidence baseline.
- Security, solvency, liquidity, staking, transition, and implementation are analyzed.
- Sensitivity to `Nmax`, `Smax`, pricing, and mainnet incidence is explicit.
- Rejected candidates have evidence-backed rejection reasons.
- Material uncertainties and required experiments are recorded.

## Pricing evidence to review — 9 November 2026

The Ledger prototype now implements V1 and an experimental V2 with historical
refunds. For the pricing comparison, run each candidate on the same historical
UTxO sample and publish the baseline, sample provenance, excess ADA at the median
and 95th percentile, and any underpriced outputs. Record which output fields a
builder must encode or measure and whether changing the deposit requires another
size calculation. Keep the choice of formula open until reviewers can reproduce
the results. [Implemented formulas](https://github.com/nhenin/cardano-ledger-specs/commit/660d0d96c24613a42cd3131a38a653ab1e39c6cf)
