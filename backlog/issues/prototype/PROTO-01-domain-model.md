# 01 — Implement the DepositStore model

**Milestone:** [M4 — Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Completed — prototype implementation at the pinned revision

## Delivered scope and evidence — 30 October 2026

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3), at
`7b9b274800e213a33bb2f55b1210e901d91034dc`, implements the candidate model in the
[executable specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md).

## Completion criteria

- [x] Separate legacy and Store-backed outputs and explicit TopTx/SubTx declarations.
- [x] Make allocation, release, conservation and exact Store backing explicit;
  the cached Store total equals the sum of allocation deposits.
- [x] Retain accepted output size and creation-time `DepositCalculation` in
  `UTxOStore`; refund historical deposits after restoration and parameter changes.
- [x] Record passing focused evidence: 13 metadata/codec examples and the 209-case
  DepositStore suite, with all four CI compiler builds passing. Commands, results
  and exclusions are in the [verification record](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md).

This closes the implemented model slice. Formal design adoption, newer upstream
integration and full validation remain open. The earlier `max(0,M-adaIn)` formula
remains a historical comparison. Production selects V1; V2 has provisional V1
formula parity. Explicit repricing and migration of older experimental snapshots
require separate policy decisions.

## Original acceptance requirements retained elsewhere

This issue was previously **Align the domain model with the adopted specification**.
Its broader requirements are transferred explicitly, rather than marked satisfied:

| Original requirement or unresolved decision | Continuing owner |
|---|---|
| Capacity, settlement, representation and transition match an adopted specification; reconcile #20–24 and the split/netting contract. | [M3 design review #19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19), [compatibility #23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23), and [output #40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40), [netting #41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41), [economic settlement #42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42). |
| Decide Plutus projection, stronger local settlement and calculation-version/repricing policy. | #23 and #40–42; agreed executable coverage belongs to [remaining test coverage](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58). |
| Establish complete domain/invariant tests under the repository warning policy. | Remaining test coverage and [full validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29). |
| Validate the model on the newer Ledger snapshot. | [Upstream integration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57), then #29. |
