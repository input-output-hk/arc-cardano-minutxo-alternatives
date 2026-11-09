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

Nicolas and Will agreed on the simple V1 formula for the prototype. It can be
computed directly from the native asset count and the sizes of the datum and
reference script, without a deposit/encoding fixed point. Experimental V2
demonstrates a later change in formula while existing allocations retain their
historical price. The wider protocol comparison can use the distribution of
live UTxOs and a documented reference price to quantify the differences between
pricing options. [Implemented formulas](https://github.com/nhenin/cardano-ledger-specs/commit/660d0d96c24613a42cd3131a38a653ab1e39c6cf)
