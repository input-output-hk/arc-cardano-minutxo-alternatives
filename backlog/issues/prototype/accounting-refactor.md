# Complete Ledger interface migration

**Parent:** [Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25).

**Status:** In progress — published interface slices exist; residual migration remains open.

## Responsibility

Complete the consumer and compatibility audit for output, asset, coin and mint
interfaces, then implement the justified remaining slices. Review semantic choices
with [Output representation](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40), [Transaction netting](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) and
[Compatibility](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23); do not make protocol choices through accessor changes.

In [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc), `Cardano.Ledger.TxOut` owns output interfaces and collection
queries; shared state owns `UTxOStore`; accepted-input contracts and annotations
use `Allocations`; whole-Store projections are removed.
[The pinned representation](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-state-representation) records these completed
slices. Later local stake/allocation changes are outside this checkpoint.

## Remaining migration

- [ ] Inventory declarations, exports and consumers across core, eras, APIs,
  translations, tools and tests; explain every retained representation adapter.
- [ ] Review stake output-delta contracts, `txouts` and allocation construction;
  distinguish proposed outputs from historical allocations. Retire
  `LegacyUTxOMap` only after its remaining responsibilities have explicit owners.
- [ ] Complete mint decomposition and policy-index evidence, constructor/instance
  guarantees, ADA access/update, compact paths and exact encoding/hash equivalence.
- [ ] Preserve behavior, failure payloads/order and era upgrades in each justified
  slice; publish clean commits, targeted results and residual exceptions.
- [ ] Send validation findings to [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29). Its final CI result is four successful
  compiler builds and 24 of 26 package jobs passing; Dijkstra and conformance each
  report 27 failures whose origin remains unestablished. This issue owns interface
  correctness, not a duplicate full-CI gate.

## Contracts to preserve

`Assets` includes ADA and native assets. `OutputCoins` is an ADA-only role;
`CapacityDeposit` is a distinct role. `MintDelta` contains signed native assets
without ADA; `MintedAssets` selects positive entries and `BurnedAssets` contains
positive magnitudes. Review constructor guarantees separately from projections.

Keep exact Plutus representations: V1/V2 mint retains its leading ADA-zero entry;
V3/V4 mint is native-only. External Plutus `Value` is not a rename target.
Review `MultiAsset`/`PolicyID`/`AssetName` ownership, generic signatures and
legacy migration against consumers. Record aggregate requirements and counterexamples;
a global rename does not establish an appropriate interface.

## Acceptance criteria retained

- [ ] Domain, genericity, module ownership and compatibility decisions are reviewed;
  no new catch-all abstraction or silent read/write allocation rule is introduced.
- [ ] The inventory covers affected declarations/exports and consumers across core,
  supported eras, APIs, translations, tools and tests; each retained use is explained.
- [ ] Mint decomposition, disjoint support, zero/empty and signed boundary cases are
  tested. Public API invariants are checked separately from projection behavior.
- [ ] Policy selection and the policy-to-redeemer-index correspondence are unchanged,
  including burn-only and raw zero-entry cases supported by the baseline.
- [ ] ADA access/update and compact/unpacked contracts are preserved; native-asset
  conservation and all era-specific ADA accounting terms remain accounted for.
- [ ] Exact Plutus representation, serialization/hash equivalence, upgrades, failures
  and collateral paths have appropriate regression evidence; semantic equality of
  `MultiAsset` alone is not treated as evidence of identical maps or wire bytes.
- [ ] Migration-specific builds/tests and agreed hot-path checks are reproducible,
  tied to exact commits, with exclusions visible. Report broader package/CI results
  in #29; no filtered run is described as a complete green suite.
- [ ] The reviewed migration scope is complete, with explicit legacy boundary
  exceptions and a removal policy; completed slices have clean signed fork commits.

## Historical baseline

The September `nicolas/minutxo-accounting-refactor` checkpoint `6084525881`
contained five signed commits above `9714940b3f` and was recorded as private-fork
evidence. Selected mint consumers had been adapted; the migration was incomplete.
Keep it for comparison with the published head, not as the current delivery status.
Uncommitted experiments are excluded. A central Ledger PR remains a separate decision.
