# Refine asset, coin, and mint interfaces to support the three-level exploration

**Status:** In Progress — interface slices published; residual-consumer and compatibility review outstanding.

**Parent:** [Three-level Ledger exploration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39).

## Current progress and remaining work — 30 October 2026

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc) is the current published implementation evidence.
[State representation and interfaces](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-state-representation) and the
[verification record](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md) describe the completed slices and their limits.

- [x] Separate output interfaces and collection queries in `Cardano.Ledger.TxOut`.
- [x] Store shared ledger outputs and historical metadata in `UTxOStore`; migrate
  accepted-input contracts, contexts and annotations to `Allocations`.
- [x] Remove the shared whole-Store projections and publish selected build/runtime
  evidence for the interface migrations.
- [ ] Complete the residual consumer inventory and reviewed compatibility/removal policy.
- [ ] Review stake output-delta contracts, `txouts` and allocation-construction
  interfaces; retire `LegacyUTxOMap` only after its remaining owners are resolved.
- [ ] Complete the mint-specific invariant, policy-index, exact-wire/hash and
  compact-path evidence required below, plus agreed cost checks.
- [ ] Investigate CI failures and finish broader validation; [full CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763)
  has a failed conformance job despite all four GHC build jobs passing.

These completed slices do not establish full `Value` retirement, Store-backed Plutus
compatibility or the complete mint-refactor contract. Later local stake/allocation
work is outside this published checkpoint.

## Purpose

Make the accounting responsibilities exposed by the three-level exploration explicit
in the Ledger interfaces. This is a transversal, behavior-preserving engineering
track; it does not itself implement capacity deposits, netting, or a dust account.

The first output-splitting spike exposed that `Value`/`Val` combine output holdings,
ADA projections, signed native-asset arithmetic, compact storage, sizing and codecs.
Classify consumers before selecting replacements. A global rename does not establish
domain granularity, and full removal of `Value` must not block design exploration.

## Historical starting evidence

- The September starting checkpoint was `nicolas/minutxo-accounting-refactor` at
  `6084525881`, five signed commits above `9714940b3f`. It was recorded as a
  private-fork baseline requiring reviewer access. Retain it as historical evidence;
  the current published checkpoint is linked above.
- At that checkpoint, typed mint concepts had reached selected accounting, policy,
  Plutus and upgrade consumers. Generic interfaces remained; that observation did
  not establish a finished refactor.
- Uncommitted experiments remain outside the published evidence and require separate
  review.

## Scope and contracts to review

- Inventory declarations, exports and consumers by role, era support, arithmetic,
  construction, read/write access, validity assumptions and representation exposure.
- `Assets` includes ADA and native assets. `CapacityDeposit` is a distinct ADA role
  for the later design. `OutputCoins` means an ADA-only view, not a whole-asset bundle.
- `MintDelta` carries signed native-asset changes, with no ADA. `MintedAssets` selects
  positive entries; `BurnedAssets` contains positive magnitudes of negative entries.
- Review actual guarantees of exported constructors, record fields and instances;
  positive projection functions alone do not establish an unforgeable positive type.
- Decide `MultiAsset`/`PolicyID`/`AssetName` ownership, concrete generic signatures,
  whether `OutputCoins` needs a type, and legacy API migration before changing them.
- Investigate whether conservation consumers can use separate ADA and native-asset
  operations. Record real aggregate requirements and counterexamples, not just names.

This track preserves ledger acceptance, state transitions, failure payloads and order,
encoding/decoding, equivalent-operation bytes/hashes, era upgrades and compact paths.
Keep exact Plutus representations: V1/V2 mint has the existing leading ADA-zero entry;
V3/V4 mint is native-only. External Plutus `Value` is not a Ledger rename target.

## Deliverables

1. A reviewed interface contract with concrete signatures, laws and compatibility policy.
2. A revision-pinned consumer inventory linking each replacement or exception to evidence.
3. Small justified implementation slices with targeted tests and fork diff links.
4. A residual-use audit identifying what each exploration level still requires.

## Acceptance criteria

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
- [ ] Builds/tests and agreed hot-path checks are reproducible, tied to exact commits,
  with exclusions visible. No filtered run is described as a complete green suite.
- [ ] The reviewed migration scope is complete, with explicit legacy boundary
  exceptions and a removal policy; completed slices have clean signed fork commits.

## Dependencies and exclusions

Work in parallel with [split](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40), [netting](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) and
[dust-account](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) design. Require an agreed interface only where an experiment
actually depends on it. Deposits, settlement, migration, staking and economic policy
changes belong to those design issues, not this behavior-preserving refactor.

Retain the five-commit baseline for comparison and review the current migration and
residual interfaces against this contract. Keep code experiments on the personal
Ledger fork. Any central Ledger pull request requires a separate review and decision.
