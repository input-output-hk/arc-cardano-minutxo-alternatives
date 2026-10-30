# Publish candidate deposit accounting

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Status:** Done — candidate publication. Economic and settlement review remain open.

## Delivered artifact

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc) publishes [deposit pricing](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-pricing),
[netting and attribution](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-accounting-net-change),
[transaction balance](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-accounting-balance),
[release authorization](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-authorization),
[settlement](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-settlement), [collateral](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-collateral)
and [Store balance](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-state-balance).

- [x] Define required new deposits and historical releases from retained accepted
  size and creation calculation; parameter changes affect new allocations.
- [x] Define funding, consuming-input authority, settlement designation and the
  ordinary/collateral timing of transfers.
- [x] Define signed netting, Store transfers counted once and exact cached backing;
  the candidate has no unallocated Store surplus.

The [historical-pricing decision](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-pricing-history) and
[local-settlement question](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-settlement-refinement) explicitly delimit
the published contract. Production selects V1; V2 has provisional V1 formula parity.

## Transferred acceptance work

| Original obligation | Open owner |
|---|---|
| Accept price basis, payer, beneficiary, timing and release rights | [Deposit settlement review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42), coordinated with [Transaction netting review](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) |
| Review whether the exact backing invariant establishes every promised credit | [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) |
| Review conservation across existing accounting terms and boundary cases | [#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) and [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42); additional execution evidence belongs to [Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25) |
| Decide explicit repricing, calculation-version evolution and any reward-policy scope | [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42); record rationale and deferrals in [#24](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24) |

Historical refunds are implemented. Publication does not approve a new repricing or
reward policy, resolve stronger local settlement, or certify all accounting paths.
