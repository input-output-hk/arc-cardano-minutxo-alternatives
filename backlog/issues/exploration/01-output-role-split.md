# Review output representation

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Owner:** Nicolas Henin.

**Status:** In progress — candidate published; representation and cross-contract review remain open.

## Responsibility

Review the output contract published by [#20](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/20) and [#21](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/21). Accept or
revise its vocabulary, construction/read/update laws, allocation boundary and
consumer assumptions. Coordinate netting with Will in [#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41), settlement
with [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) and compatibility with [#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23).

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc) and its [domain model](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#L680) supply the current candidate.
Implicit outputs retain their existing in-output minimum; Store-backed output
projections contain application assets, while deposits are held externally.
Accepted size and creation calculation retain the historical refund basis.

## Remaining review

- [ ] Complete the revision-pinned impact map and distinguish preserved behavior,
  changed interfaces and unresolved assumptions across the output lifecycle.
- [ ] Review required versus allocated deposits, zero-price records and exact
  allocation; assess the earlier in-output split as an alternative, not the
  current Store-backed projection contract.
- [ ] Test the generic-aggregate hypothesis against real consumers; retain native-asset
  aggregation needs and justified adapters. Transfer code migration to [#43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43).
- [ ] Reconcile the shared split/netting contract with Will and record Nicolas's
  review, decisions and blockers in [#24](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24).
- [ ] Hand compatibility/activation obligations to [#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23) and the coverage
  matrix to [#25](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25). This review does not own their implementation or full CI.

## Acceptance criteria retained

- [ ] Vocabulary, supported eras and construction/read/update laws are reviewed;
  application ADA is not excluded from `Assets` or silently reclassified by an accessor.
- [ ] The specification states the allocation basis, amount recorded and release-facing
  contract, including parameter changes and any retained open dependency on netting.
- [ ] Every affected boundary above has an explicit design or a documented blocker;
  ADA and native-asset conservation, collateral and stake effects are covered.
- [ ] The generic-aggregate hypothesis is tested against an inventoried consumer set;
  findings include counterexamples and justified residual representation adapters.
- [ ] Examples cover ADA-only and multiasset outputs, boundary funding, creation and
  consumption, invalid transactions, legacy outputs and activation boundaries.
- [ ] Focused evidence records revisions, commands/results and exclusions; prototype
  test results are not presented as proof that the full Ledger implementation is ready.
- [ ] Nicolas has reviewed the spec, implementation map and cross-level assumptions;
  unresolved consensus/economic choices block implementation-ready status.

These criteria require a reviewed contract and explicitly owned blockers, not
completion of every related implementation. Executed evidence and CI limitations
are recorded by [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29).

## Historical evidence

The [21 September split checkpoint](https://github.com/nhenin/cardano-ledger-specs/commit/3c0614f26767ebe222d350b1b3f5f8688169175d)
and the [28 September interface update](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40#issuecomment-5866268906)
remain historical comparisons. The current implementation is pinned above.
