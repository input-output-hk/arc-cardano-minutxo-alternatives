# Protocol Specification

**Status:** In progress · **Deliverable:** reviewed implementation contract.

**Question:** what state, transaction rules and transitions define the candidate mechanism?

The [candidate specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
is published. Publication and implementation do not constitute design approval.

## Deliverables and reviews

| Deliverable | Publication | Remaining review |
|---|---|---|
| Candidate architecture | [#20](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/20) | [Output representation #40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40). |
| Candidate state and transaction rules | [#21](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/21) | [Transaction netting #41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41). |
| Candidate accounting and settlement | [#22](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/22) | [Deposit settlement #42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42). |
| Transition and ecosystem contracts | — | [Compatibility #23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23). |
| Decision rationale | — | [Design rationale #24](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24), informed by Architecture Decision. |

## Done when

- [ ] State, validation, funding, settlement and historical refunds are unambiguous.
- [ ] Output, transaction and Store contracts agree; material open decisions are resolved.
- [ ] Legacy migration, codecs, Plutus, builders, staking and governance impacts have
  explicit contracts and review conclusions.
- [ ] The rationale links to the reviewed architecture choice and records limitations.
- [ ] The reviewed specification is consistent with the prototype and its test results.

The reviews previously grouped under #39 now belong directly here. Their original
acceptance criteria and ownership are retained. Ledger implementation work remains
under [Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25).
