# 03 — Implement invariant and compatibility tests

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Proposed

## Outcome

Executable evidence that the integrated implementation preserves the required invariants.

## Acceptance criteria

- QuickCheck covers conservation, solvency, capacity, unique release, and determinism.
- Integration tests cover creation, consumption, repricing, and migration paths.
- Serialization and compatibility round trips are tested.
- Adversarial and boundary cases are included.
- Relevant existing Ledger tests remain green.

## Deposit integration cases

- **Plutus.** Implement the agreed V1–V3 handling of deposit-backed outputs and exercise exact-value validators for each supported version, alongside the existing [V4 fixture](https://github.com/willjgould/cardano-minutxo-integration/commit/d2300267436d4cc6a4cb2dbc7898b9f98787192b).
- **Storage-cost formula.** Integrate the submitted 193-byte base plus measured address size in place of the prototype’s fixed 250-byte base. Add address size to the shared calculation inputs and test new and historical reserves for both output forms. [Submitted formula revision](https://github.com/nhenin/CIPs/blob/ac37717c9820556db1b1bde2a25cfc6b85601e97/CIP-%3F%3F%3F%3F/README.md)
- **Signing across a price change.** Run a wallet-to-node payment on a private network with independently signed SubTxs. Cross a rate update and a formula change. For each, record which bodies require new signatures when repricing changes the delegated amount or its settlement.
- **Accepted phase-2 failure.** Check mixed-form declarations and settlement independently of the collateral balance. Include a batch in which only a SubTx supplies a redeemer and the batch’s shared collateral funds the failure. Check that an input used for both ordinary spending and collateral is consumed once on the applied path.
- **Persistence and replay.** Check that decoding rejects pricing histories that activation would reject, including a version downgrade. On a private network, compare wallet and indexer views of live inputs, reserves and totals before rollback and after replay. Record the implementation revision and reproducible results. [Existing coverage](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/verification.md#current-implementation-status) · [Consensus rollback requirement](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-recovery-n02)
