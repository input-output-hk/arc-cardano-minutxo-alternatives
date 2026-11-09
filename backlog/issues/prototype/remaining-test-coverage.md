# Defer extended DepositStore test coverage

**Status:** Closed as not planned for this prototype. The existing test results and deferred coverage ideas are recorded below. [Final review #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) tracks the remaining detailed
verification of the prototype. This ticket retains broader test ideas for future work.

## 9 November evidence

The current [pricing contract](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/docs/dijkstra-deposit-store-rules.md#ds-pricing) prices assets, datum and script payloads using the formula
applicable at allocation. Focused tests cover typed measurements, historical
refunds, formula changes, zero pricing and minimum-coin admission of legacy outputs.
The [verification record](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/docs/dijkstra-deposit-store-verification.md#deposit-formula-history-on-6-november-2026) records 212 DepositStore-filter examples and 26 Store codec examples
passing at the 6 November checkpoint. The matrix below records cases for potential extension.

## Possible extensions to the existing suite

| Area | Cases to consider |
|---|---|
| Seven cases in the current [pricing contract](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/docs/dijkstra-deposit-store-rules.md#ds-pricing) | P01 and N01–N06: price each created output, count distinct assets, price applied collateral returns, measure datum/script payloads, vary the declaration independently, cross ADA encoding boundaries and retain the legacy reserve inside the output. Map focused tests against each case. |
| [Stake: eight cases](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-stake) | N01–N08: implicit full ADA; Store-backed application ADA; no global Store weight; applied allocations and releases; inactive collateral on success; applied collateral on failure; unchanged eligibility, delegation and snapshot timing. |
| [Voting: one case](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-voting) | N01: compare the complete distribution to an independent expectation, with positive eligible and ineligible/delegation controls, both execution outcomes and snapshot boundaries. Neither allocated deposits nor global Store balance adds weight. An all-zero result must fail positive controls. |
| [Plutus contexts](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-plutus-compatibility) | Test the agreed projection and translation for V1–V4, respecting each version's feature restrictions. Context design remains under #23/#40; resolve it before choosing expectations or changing the current `unexpected NewTxOut` paths. |
| [Shared collateral regressions, section 2.2](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-collateral-existing-rules) | Extend the existing Alonzo, Babbage and Dijkstra owners referenced there: TopTx/SubTx/both redeemer triggers; no-redeemer gated checks versus independent input/return/count checks; key-locked eligibility and collateral witnesses for both output forms/outcomes. Keep accepted controls and unrelated transaction fields valid. |

The shared collateral source references already cover input resolution, fee
percentage, witnesses, supplied totals and some return validation. They establish
ownership, not a fresh passing run. Reuse those suites and extend Store-backed
fixtures rather than duplicate their tests under DepositStore. Also extend the
existing [Minimum coin N03 control](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/eras/dijkstra/impl/test/Test/Cardano/Ledger/Dijkstra/Imp/DepositStore/TransactionRules/Tx/MinimumCoinSpec.hs#L75)
to assert empty redeemers and collateral explicitly. The inherited Babbage return
fixup currently rejects `NewTxOut`; implicit fixtures alone do not cover Store returns.

## Reference criteria for future test work

- [ ] Map every case above to its owning executable test, existing evidence or
  reviewed design dependency. Add meaningful cases for identified gaps; do not
  blindly add placeholders, duplicate inherited tests or count helpers as examples.
- [ ] Preserve the original #28 QuickCheck obligations: conservation, exact Store
  backing, capacity, unique release and determinism, with adversarial and boundary
  cases. Identify which existing tests establish each property and fill genuine gaps.
- [ ] Preserve allocation/release integration, historical refunds after parameter
  changes, supported migration paths, serialization and compatibility round trips.
  Review explicit repricing or new migration policy with #23/#42 before testing it
  as an agreed rule; rejection of unsupported experimental snapshots remains explicit.
- [ ] Implement and run the seven pricing, eight stake and one voting cases and
  the agreed Plutus/shared-collateral coverage. Use independent expected results
  and positive controls that detect missing effects or unintended acceptance.
- [ ] Record exact tested commits, commands, compiler/warning policy, seeds,
  example/failure/pending counts and logs. Rerun affected earlier-era, binary
  and conformance suites after [upstream integration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57).
- [ ] Deliver passing evidence and explicit exclusions to [validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29).
  The [8 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) passed both Dijkstra and conformance at `b77257163`.

Formal design agreement remains in [#19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19),
[#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23) and
[#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40)/[#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41)/[#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42).
Full CI and milestone completion remain in #29.
