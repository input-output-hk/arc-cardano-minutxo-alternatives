# 02 — Integrate DepositStore ledger rules

**Milestone:** [M4 — Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Completed — prototype rule integration at the pinned revision

## Delivered scope and evidence — 30 October 2026

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) publishes
`7b9b274800e213a33bb2f55b1210e901d91034dc`. Closed PR #2 is historical.
The [specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
and [verification record](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md)
define the implemented behavior and tested scope.

## Completion criteria

- [x] Integrate declarations, exact net accounting, balance, authorization,
  settlement, minimum coin, Store-specific collateral and ledger effects.
- [x] Implement required state, types, transaction fields and serialization;
  store outputs with historical allocations and adapt shared-state readers.
- [x] Preserve legacy codecs and implement the documented era translation:
  Conway outputs become legacy allocations without moving ADA between pots.
  Unsupported older experimental Dijkstra snapshots are rejected.
- [x] Build this feature with GHC 9.6.7, 9.10.3, 9.12.4 and 9.14.1 in
  [CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763),
  with focused DepositStore and metadata/codec execution recorded in #28.

This closes prototype rule integration at this revision, incorporating upstream
through `8a15ddc07`. Ten conflicts with the newer `9df9f98cc` snapshot remain.
Later unpushed Store/API cleanup is outside this checkpoint.

## Original acceptance requirements retained elsewhere

This issue was previously **Integrate the mechanism into cardano-ledger rules**.
The broader validation, settlement, migration and compatibility scope remains:

| Original requirement or remaining work | Continuing owner |
|---|---|
| Integrate the newer Ledger snapshot, review ten conflicts and validate the resulting revision. | [Upstream integration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57), then [full validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29). |
| Era boundaries, migration and backward compatibility follow the adopted specification; review shared interfaces affecting earlier eras. | [M3 design review #19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19), [compatibility #23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23), [output #40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40) and [economic settlement #42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42). |
| Complete Store-backed Plutus contexts and review remaining settlement/transition contracts. | #23 and [netting #41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41)/#42 for design; [remaining test coverage](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58) for agreed regressions. |
| All relevant packages and existing Ledger tests pass at the integrated revision. | #29; four passing builds do not establish full CI success or formal design adoption. |
