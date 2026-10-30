# 03 — Implement the DepositStore business suite

**Milestone:** [M4 — Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Completed — business suite at the pinned revision

## Delivered scope and evidence — 30 October 2026

At [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) head
`7b9b274800e213a33bb2f55b1210e901d91034dc`:

| Executed locally | Examples | Failures | Time |
|---|---:|---:|---:|
| DepositStore business suite | 209 | 0 | 420.1 s |
| Historical metadata and codecs | 13 | 0 | 71.4 s |

## Completion criteria

- [x] Implement 178 transaction cases, seven Store-specific collateral cases and
  24 ledger-effect cases, following the executable business contracts.
- [x] Provide generators, fixtures and submission helpers supporting those cases;
  the suite contains no deliberate placeholders.
- [x] Record the passing 209-example execution and the separate 13-example
  historical metadata/codec checks with their commands and pinned revision.

[Case definitions and existing-test references](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
· [Recorded verification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md).
Source-line counts are not test counts. Completion covers this business suite;
full CI and broader invariant/compatibility completeness remain open.

## Original acceptance requirements retained elsewhere

This issue was previously **Implement invariant and compatibility tests**.

| Original criterion or remaining coverage | Continuing owner |
|---|---|
| QuickCheck covers conservation, exact backing, capacity, unique release and determinism; adversarial and boundary cases are included. | [Remaining test coverage](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58): map existing evidence and fill identified gaps. |
| Integration tests cover allocation, release, historical refunds after parameter changes, supported migration paths, serialization and compatibility round trips. | Remaining test coverage and [full validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29); explicit repricing/migration policy is reviewed in [#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23) and [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) first. |
| Complete seven pricing cases, eight stake cases, one voting case, agreed Plutus contexts and shared collateral regressions. | Remaining test coverage, using the specification's existing test ownership and references. |
| Relevant existing Ledger, legacy, binary and conformance tests remain green after integration. | [Upstream integration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57), then #29. |
| Tests establish agreement with the adopted design. | [M3 design review #19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19), #23 and [#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40)/[#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41)/#42; passing prototype examples do not establish adoption. |
