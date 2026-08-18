# 01 — Align the domain model with the adopted specification

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Blocked by M3

## Outcome

A pure domain model matching the adopted solution specification rather than the earlier exploratory formula.

## Acceptance criteria

- Capacity, settlement, representation, and transition semantics match the adopted specification.
- Conservation, solvency, allocation, and release operations are explicit.
- Earlier `max(0,M-adaIn)` behavior is retained only as historical comparison.
- Domain-level tests pass under the repository warning policy.
