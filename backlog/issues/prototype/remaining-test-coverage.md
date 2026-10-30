# Complete the remaining DepositStore test coverage

**Milestone:** [M4 — Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Open — coverage requirements identified; implementation outstanding

## Scope and starting evidence — 30 October 2026

This task receives the broader invariant and compatibility acceptance criteria from
#26–28. At `7b9b274800e213a33bb2f55b1210e901d91034dc`, the delivered business suite
has 209 passing examples (178 transaction, seven Store collateral, 24 ledger effects),
plus 13 passing metadata/codec examples. See the [pinned specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
and [verification record](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md).
These results leave the following explicit coverage obligations.

## Required coverage

| Area | Required cases and evidence |
|---|---|
| [Pricing: seven cases](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-pricing) | P01 and N01–N06: accepted-byte retention; `coinsPerUTxOByte * (160 + acceptedSize)`; collateral-return pricing; included address/assets/datum/script bytes; excluded external deposit/declaration; CBOR coin-size boundaries; no Store obligation for implicit outputs. Existing historical size/rate checks cover only part of this matrix. |
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

## Completion criteria and original acceptance traceability

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
  The existing 27 Dijkstra/conformance failures require diagnosis and review there;
  their cause is not inferred from the coverage gaps.

Formal design agreement remains in [#19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19),
[#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23) and
[#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40)/[#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41)/[#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42).
Full CI and milestone completion remain in #29.
