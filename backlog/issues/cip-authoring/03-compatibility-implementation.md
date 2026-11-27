# 03 — Document compatibility, transition, and implementation path

## Outcome

Complete CIP sections for ecosystem impact, migration, activation, and implementation.

## Acceptance criteria

- Backward compatibility and era transition are explicit.
- Plutus, wallet, builder, node, and governance impacts are covered.
- Path to Active and implementation sequencing are reviewable.

## Decisions to bring back to the CIP

- **Plutus contexts.** Specify which parts of the output value, its backing and the signed net each language version exposes. Decide how V1–V3 handle deposit-backed outputs, including contracts that compare exact ADA amounts. [Current support by version](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/verification.md#plutus-context-status)
- **Pricing at the deposit fork.** Record the companion CIP’s assigned number and activating protocol version once available. If its formula has evolved by the deposit fork, select the baseline for imported outputs and the initial price for new outputs. The prototype starts both with the same rule. Check that the calibration covers the allocation metadata and pricing history introduced by the deposit model. [Submitted formula](https://github.com/cardano-foundation/CIPs/pull/1328)
- **Stake and voting.** Compare the effect on a wallet’s capital when a live external deposit loses its staking weight or is attributed to the output’s staking credential. Record the chosen policy for each distribution. [Distribution policies](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/derived-distributions.md)
- **Off-node queries.** Specify how independent wallets and indexers retrieve and interpret allocation origins and formula history at the same chain point. Publish the interoperable snapshot format and link the [verification work](../prototype/PROTO-03-tests.md#deposit-integration-cases) from the implementation plan.
