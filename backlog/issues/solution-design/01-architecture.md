# Publish the candidate architecture

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Status:** Done — candidate publication. Architecture acceptance and protocol adoption remain open.

## Delivered artifact

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc) publishes the architecture in the
[domain model](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#L680), [ledger-effect responsibilities](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#L5963),
[state representation](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-state-representation) and
[implementation map](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#L6948).

- [x] Define implicit and Store-backed output roles, the owning Store and historical metadata.
- [x] Define TopTx/SubTx responsibilities and the boundary between declarations,
  validation and applied ordinary/collateral effects.
- [x] Identify the current legacy-translation boundary and unresolved design choices.

This closes publication of the implemented candidate, not the original broader
promise of a complete architecture derived from an approved recommendation.

## Transferred acceptance work

| Original obligation | Open owner |
|---|---|
| Accept capacity, representation, settlement and transition architecture | [Output representation review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40), [Transaction netting review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41), [Deposit settlement review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) and [Compatibility review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23) |
| Review components, authority and trust boundaries | [#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40), [#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) and [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) |
| Assign unresolved decisions and relate the architecture to the recommendation | [Design rationale and adoption record](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24), using [Architecture Decision](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14) |

Each review retains its decision or blocker. A published component map does not
establish formal adoption or migration approval.
