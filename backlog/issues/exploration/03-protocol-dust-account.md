# Review deposit settlement

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Status:** In progress — candidate accounting published; economic and settlement review remain open.

## Responsibility

Review the contract published by [#22](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/22), including refund rights, exact
backing, netting, parameter changes and the unresolved local-settlement guarantee.
Coordinate with [#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) and record Nicolas's cross-contract review in [#24](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24).
The former dust-account exploration is now this concrete review of DepositStore.

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc) retains accepted size and creation calculation, refunds historical
deposits after restoration/parameter changes, and maintains an exact cached total.
It has no unallocated Store surplus. These implemented facts are delivered evidence,
not open implementation tasks.

## Remaining review

- [ ] Compare historical-price and current-price release policies, their funding
  basis and repricing risk. Production selects V1; V2 has provisional V1 formula
  parity. Record the scope and consequences of deferred repricing/version selection.
- [ ] Decide what local settlement must guarantee beyond its destination bound
  while preserving valid SubTx exports to TopTx fees or other bodies. Do not silently
  introduce independent SubTx balance or an unsigned export allowance.
- [ ] Review payer/beneficiary authority, unique release, exact backing and
  conservation across ordinary and collateral outcomes, including boundary cases.
- [ ] Review stake/voting policy and any reward-policy consequences. Hand executable
  distribution/coverage work to [#25](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25) and cost measurements to [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29).
- [ ] Hand migration, signed-transaction, Plutus and node-recovery decisions to
  [#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23); record each dependency, blocker or agreed exclusion.
- [ ] Record the combined economic/consensus review with Nicolas in [#24](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24).

## Acceptance criteria retained

- [ ] Backing and obligations are defined separately; allocation, funding, release and
  surplus cannot be confused, and every promised release has an explicit funding basis.
- [ ] The design identifies the information needed for each UTxO and demonstrates how
  it survives parameter changes and is removed or updated exactly once on consumption.
- [ ] Historical-price and current-price release options are evaluated explicitly;
  refund rights and repricing risk are reviewed choices, not accidental consequences.
- [ ] Account and obligation equations reconcile with transaction netting and total ADA;
  native assets remain application holdings and are not deposited in the account.
- [ ] Examples cover creation, replacement, consolidation, fan-out, complete release,
  changed parameters, adversarial/double release, failure/collateral and migration.
- [ ] Missing-state and insolvency scenarios are either excluded by proved conditions
  or handled by explicit rules; no undocumented external historical oracle is required.
- [ ] Staking, collateral, old-output spendability, signed transactions and state-storage
  consequences have concrete designs or clearly identified implementation blockers.
- [ ] Evidence records revisions, methods, results and limitations; Nicolas reviews the
  combined three-level contract and all material economic/consensus decisions.

Boundary reviews may identify explicit blockers as the original criteria allow.
Their implementation and full-CI success are owned by [#25](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25) and [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29).

## Evidence

[Accounting and funding](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-accounting-balance) ·
[Historical pricing](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-pricing-history) ·
[Local settlement](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-settlement-refinement) ·
[State and translation](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-state-representation) ·
[Verification history](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md).
