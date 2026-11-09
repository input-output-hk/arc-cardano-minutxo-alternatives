# Ledger Prototype

**Status:** In progress · **Deliverable:** validated Ledger implementation.

**Question:** can `cardano-ledger` execute the candidate's rules correctly while
preserving the required compatibility?

The 30 October Leios snapshot (`9df9f98cc`, 63 upstream commits) is integrated
in [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3). The [2 November integration run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41433981296) passed.
The [8 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) at `b77257163` passed all four compiler builds and the
package tests, including Dijkstra and conformance. The 27 SubTx cases that failed
on 30 October also passed locally after integration.

The published head [`2298a0085`](https://github.com/nhenin/cardano-ledger-specs/commit/2298a008589d5a0a5ea70bd1ec87d8477e989422) adds the legacy deposit cap clarification and a check
rejecting formula-version downgrades. Its [9 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42592236836) was in progress at review.

| Delivered | Remaining |
|---|---|
| [DepositStore model #26](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/26) | [Upstream integration #57](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57) |
| [Ledger rules #27](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/27) | [Coverage gaps #58](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58) |
| [209 business cases + 13 metadata/codec cases #28](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/28) | [Interface migration #43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) |
| Four GHC builds and the full package matrix passed on the rebased 8 November revision | [Full regression validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) |

The remaining integration task records the conflict review and sign-off.
Coverage, interface compatibility and feasibility are tracked separately below.

## Done when

- [ ] The reference snapshot is integrated with reviewed conflict resolutions.
- [ ] Remaining agreed coverage and interface contracts are implemented.
- [ ] Relevant regression suites pass at the integrated revision, with reproducible evidence.
- [ ] Deviations and compatibility limits are resolved with Protocol Specification;
  production work outside the prototype is explicitly recorded.

Completed implementation slices do not complete this epic or approve the protocol.
