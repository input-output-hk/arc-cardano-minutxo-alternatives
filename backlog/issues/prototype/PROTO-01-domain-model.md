# 01 — Align the domain model with the adopted specification

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** In progress — candidate implemented; design review outstanding

## Progress — 30 October 2026

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3), at
`7b9b274800e213a33bb2f55b1210e901d91034dc`, implements the candidate model.
The [executable specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
defines its vocabulary, equations and cases.

- [x] Separate legacy and Store-backed outputs and explicit TopTx/SubTx declarations.
- [x] Retain each accepted output's size and creation-time calculation in `UTxOStore`.
- [x] Maintain exact backing: cached Store total equals the sum of allocation deposits.
- [x] Refund historical deposits after restoration and parameter changes; the
  13 focused metadata/codec examples pass at this head.
- [ ] Review the candidate with #20–24 and reconcile the split/netting contracts
  in #40–42. An implementation is not evidence of formal design adoption.
- [ ] Decide the remaining Plutus projection, stronger local-settlement guarantee
  and calculation-version policy. V2 currently has provisional V1 formula parity.

Explicit repricing of existing allocations and migration of older experimental
snapshots are separate design choices, not missing implementations of agreed rules.

## Outcome

A pure domain model matching the adopted solution specification rather than the earlier exploratory formula.

## Acceptance criteria

- Capacity, settlement, representation, and transition semantics match the adopted specification.
- Conservation, exact Store backing, allocation, and release operations are explicit.
- Earlier `max(0,M-adaIn)` behavior is retained only as historical comparison.
- Domain-level tests pass under the repository warning policy.
