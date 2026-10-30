# Ledger Prototype

**Status:** In progress · **Deliverable:** validated Ledger implementation.

**Question:** can `cardano-ledger` execute the candidate's rules correctly while
preserving the required compatibility?

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3), head
`7b9b274800e213a33bb2f55b1210e901d91034dc`, publishes the implementation.

| Delivered | Remaining |
|---|---|
| [DepositStore model #26](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/26) | [Upstream integration #57](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57) |
| [Ledger rules #27](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/27) | [Coverage gaps #58](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58) |
| [209 business cases + 13 metadata/codec cases #28](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/28) | [Interface migration #43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) |
| Four GHC builds pass | [Full regression validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) |

Full CI is **not green**: 24 of 26 package jobs pass; Dijkstra and conformance each
report the same 27 SubTx cases failing. The cause is not yet attributed.
The newer `leios-prototype-snapshot-30-10` has ten unresolved integration conflicts.
Local unpublished changes are not counted in this checkpoint.

## Done when

- [ ] The reference snapshot is integrated with reviewed conflict resolutions.
- [ ] Remaining agreed coverage and interface contracts are implemented.
- [ ] Relevant regression suites pass at the integrated revision, with reproducible evidence.
- [ ] Deviations and compatibility limits are resolved with Protocol Specification;
  production work outside the prototype is explicitly recorded.

Completed implementation slices do not complete this epic or approve the protocol.
