# 03 — Implement invariant and compatibility tests

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** In progress — business suite implemented; remaining coverage explicit

## Progress — 30 October 2026

At [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) head
`7b9b274800e213a33bb2f55b1210e901d91034dc`:

| Executed locally | Examples | Failures | Time |
|---|---:|---:|---:|
| DepositStore business suite | 209 | 0 | 420.1 s |
| Historical metadata and codecs | 13 | 0 | 71.4 s |

The business suite includes 178 transaction cases, seven Store-specific collateral
cases and 24 ledger-effect cases. It contains no deliberate placeholders. Generators,
fixtures and submission helpers support these examples; source-line counts are not
test counts. Full CI is tracked separately in #29 and is not green.

## Remaining coverage

- [ ] Complete the seven-case pricing matrix; historical size/rate regressions cover
  only part of it.
- [ ] Implement the eight documented stake cases and one voting case.
- [ ] Test Store-backed outputs across the supported Plutus versions once the
  context projection is agreed.
- [ ] Extend the existing shared collateral scope/authorization tests identified in
  specification section 2.2; do not duplicate them in DepositStore.
- [ ] Re-run legacy, binary and conformance regressions after upstream integration.

[Case definitions and existing-test references](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
· [Recorded verification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md).

## Outcome

Executable evidence that the integrated implementation preserves the required invariants.

## Acceptance criteria

- QuickCheck covers conservation, exact Store backing, capacity, unique release, and determinism.
- Integration tests cover allocation, release, historical refunds after parameter changes,
  and supported migration paths. Explicit repricing requires an agreed policy first.
- Serialization and compatibility round trips are tested.
- Adversarial and boundary cases are included.
- Relevant existing Ledger tests remain green.
