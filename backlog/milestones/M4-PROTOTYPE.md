# Milestone M4 — Ledger Prototype

**State:** In progress · **Deliverable:** integrated, validated Ledger prototype.

The 30 October Leios snapshot (`9df9f98cc`, 63 upstream commits) is integrated
in [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3). The [2 November integration run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41433981296) passed.
The [8 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) at `b77257163` passed all four compiler builds and the
package tests, including Dijkstra and conformance. The 27 SubTx cases that failed
on 30 October also passed locally after integration.

The published head [`2298a0085`](https://github.com/nhenin/cardano-ledger-specs/commit/2298a008589d5a0a5ea70bd1ec87d8477e989422) adds the legacy deposit cap clarification and a check
rejecting formula-version downgrades. Its [9 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42592236836) was in progress at review.

## Completed implementation slices

- [Model #26](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/26): output variants, declarations and historical allocation storage.
- [Ledger rules #27](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/27): transaction rules, Store-specific collateral and state effects.
- [Business suite #28](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/28): 209 examples plus 13 metadata/codec examples pass locally.
- Four CI builds pass: GHC 9.6.7, 9.10.3, 9.12.4 and 9.14.1.

## Remaining work

| Task | Completion evidence |
|---|---|
| [Upstream integration #57](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57) | Reference integrated and tested; document conflict review and sign-off. |
| [Coverage gaps #58](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58) | Pricing, distributions, Plutus and shared collateral cases accounted for. |
| [Interface migration #43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) | Reviewed residual consumers, invariants and compatibility evidence. |
| [Regression validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) | Relevant suites pass at the integrated head; limitations and costs documented. |

Record full validation at the final implementation revision in #29, alongside
coverage exclusions, memory/runtime costs and remaining protocol decisions.

## Completion criteria

- [ ] Integrated behavior matches the reviewed specification.
- [ ] Required type, serialization, transition and interface changes are complete.
- [ ] Relevant property, integration, compatibility and regression tests pass.
- [ ] Findings, limitations and remaining production work feed back into the CIP.

Local unpublished changes are excluded. Formal architecture approval and protocol
review remain under M2/M3; completed implementation slices do not complete M4.
