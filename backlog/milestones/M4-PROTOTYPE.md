# Milestone M4 — Ledger Prototype

**State:** In progress · **Deliverable:** integrated, validated Ledger prototype.

**Checkpoint:** [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3)
at `7b9b274800e213a33bb2f55b1210e901d91034dc`.
The reference is `leios-prototype-snapshot-30-10` at
`9df9f98cce86c5f2195142b2c02dd9b39dd9dc7c`; ten integration conflicts remain.

## Completed implementation slices

- [Model #26](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/26): output variants, declarations and historical allocation storage.
- [Ledger rules #27](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/27): transaction rules, Store-specific collateral and state effects.
- [Business suite #28](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/28): 209 examples plus 13 metadata/codec examples pass locally.
- Four CI builds pass: GHC 9.6.7, 9.10.3, 9.12.4 and 9.14.1.

## Remaining work

| Task | Completion evidence |
|---|---|
| [Upstream integration #57](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57) | Reviewed conflict resolutions; resulting head builds and is tested. |
| [Coverage gaps #58](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58) | Pricing, distributions, Plutus and shared collateral cases accounted for. |
| [Interface migration #43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) | Reviewed residual consumers, invariants and compatibility evidence. |
| [Regression validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) | Relevant suites pass at the integrated head; limitations and costs documented. |

[CI run 41019013763](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763)
finished with **24/26 package jobs passing**. Dijkstra and conformance each report
27 failing SubTx cases; the cause is not yet attributed. The aggregate gate also
fails because those suites failed. Test duration is not a production-performance measurement.

## Completion criteria

- [ ] Integrated behavior matches the reviewed specification.
- [ ] Required type, serialization, transition and interface changes are complete.
- [ ] Relevant property, integration, compatibility and regression tests pass.
- [ ] Findings, limitations and remaining production work feed back into the CIP.

Local unpublished changes are excluded. Formal architecture approval and protocol
review remain under M2/M3; completed implementation slices do not complete M4.
