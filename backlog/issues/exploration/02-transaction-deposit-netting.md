# Review transaction netting

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Owner:** Will Gould.

**Status:** In progress — assessment available; reconciliation and joint review remain open.

## Responsibility

Reconcile [Will's Ledger and builder assessment](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41#issuecomment-5796435821)
with the candidate contracts published by [#21](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/21) and [#22](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/22).
Preserve its attribution and original assumptions: backing held in outputs,
recorded backing at least equal to required backing, and total-value getters
including application ADA plus backing.

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc) instead has external deposits, exact allocations and declarations,
TopTx/SubTx delegation and separate ordinary/collateral accounting.
[Netting](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-accounting-net-change) and
[balance](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-tx-accounting-balance) define that candidate; implementation
does not establish Will's agreement with it.

## Remaining review

- [ ] Pin the annotated Ledger and builder revisions; update the impact map for
  external deposits, exact allocation, explicit declarations and nested transactions.
- [ ] Compare existing balancing, the earlier in-output split and the current
  contract. Explain the semantics added by declarations and delegation.
- [ ] Review the full ADA equation and native-asset conservation across supported
  fees, refunds, certificates, withdrawals, mint, governance and donation terms.
  The focused Balance fixtures exclude several of these flows.
- [ ] Demonstrate builder selection, change, collateral-return, serialization and
  convergence implications, including the worked examples below.
- [ ] Review the shared output/netting contract with Nicolas; record remaining
  choices in [#24](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24). Settlement guarantees belong to [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42);
  activation and ecosystem compatibility belong to [#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23).

## Acceptance criteria retained

- [ ] The reviewed specification defines allocation, release and net amount without
  treating output minimum, recorded deposit and available application ADA as synonyms.
- [ ] The added semantics over existing implicit balancing are demonstrated concretely;
  a new transaction field is neither presumed necessary nor excluded without analysis.
- [ ] Positive, zero and negative net cases reconcile to the complete ADA equation;
  backing is counted once and native assets remain conserved independently.
- [ ] Release authorization, multi-party funding, unique consumption, reference inputs,
  successful execution and collateral/failure behavior are explicitly specified.
- [ ] Examples cover same-size replacement, fan-out, consolidation, deletion, mint/burn,
  changed parameters and underfunding; builder implications are demonstrated.
- [ ] Focused evidence is reproducible and distinguishes model checks, prototype tests
  and untested integration paths; compilation alone is not behavioral validation.
- [ ] The design states exactly which contracts protocol-account settlement must retain
  or intentionally change, and Nicolas reviews the remaining cross-level decisions.

The review owns the reconciled contract and builder implications. Code migration
belongs to [#43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) or a scoped task under [#25](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25); executed test results
and full validation belong to [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29). Will's original assessment remains
available in the linked comment.
