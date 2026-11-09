# Publish candidate state and validation rules

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Status:** Done — candidate publication. Semantic review remains open.

## Delivered artifact

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc) publishes [state and transaction concepts](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#L709),
[transaction rules](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#transaction-rules), [ledger effects](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-state)
and [transaction-body fields](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#transaction-body-fields).

- [x] Define the Store, allocation metadata and TopTx/SubTx declaration fields.
- [x] State the candidate's allocation, release, declaration, accounting,
  authorization, settlement, minimum-coin and collateral validation contracts.
- [x] State observable ordinary/collateral transitions and locally checkable
  allocation and exact-cache invariants, with accepted and rejected cases.

The rules are normative for this candidate. This publication does not establish
that every protocol boundary is settled or that all relevant tests pass.

## Transferred acceptance work

| Original obligation | Open owner |
|---|---|
| Review state, construction/read/update laws and invariant boundaries | [Output representation review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40) |
| Accept declaration, netting and authorization semantics | [Transaction netting review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) |
| Resolve stronger local settlement and economic policy boundaries | [Deposit settlement review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) |
| Approve Plutus projection, activation and legacy compatibility | [Compatibility review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23) |
| Complete test coverage and full validation | [Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25); validation results belong to [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) |

Definitions and case links are delivered; review of their adequacy remains with
these tasks. Missing consensus choices are not silently selected by implementation.
