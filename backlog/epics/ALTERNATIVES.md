# Architecture Decision

**Status:** In progress · **Deliverable:** reviewed recommendation.

**Question:** which complete mechanism best addresses the CPS without weakening
persistent-state protection or Ledger correctness?

The DepositStore prototype is a working candidate. Its existence does not replace a
comparison or establish approval of the architecture.

## Work

| Responsibility | Issue | Completion evidence |
|---|---|---|
| Evaluation framework | [#15](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/15) | Common requirements, invariants and comparison criteria. |
| Candidate mechanisms | [#16](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/16) | At least two complete architectures, including transition. |
| Trade-offs | [#17](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/17) | Comparable security, liquidity, staking, implementation and application results. |
| Recommendation | [#18](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/18) | Reviewed choice with rationale and rejected alternatives. |
| Mainnet evidence | [#10](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/10) | Reproducible stock/minimum-ADA analysis; currently deferred. |
| Application evidence | [#56](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/56) | Named examples and reproducible transaction or builder traces. |

## Done when

- [ ] At least two complete alternatives are evaluated against the same criteria.
- [ ] Claims have evidence; unresolved empirical dependencies and sensitivity are explicit.
- [ ] Review records the selected architecture, risks and reasons for rejecting alternatives.

Exact contracts belong to [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19); implementation and
regression evidence belong to [Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25).
