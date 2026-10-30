# Review transition and ecosystem compatibility

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Status:** Todo — candidate translation exists; compatibility decisions remain open.

## Responsibility

Own the protocol compatibility and activation contract. Review legacy output
spendability, signed transactions, era transitions, serialization, Plutus contexts,
wallets, builders, governance and node/state recovery. Implementation and runtime
validation are tracked by [Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25) and [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29).

The candidate [translation](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-state-translation) preserves Conway outputs
as legacy allocations with zero external deposits. Its
[representation and codecs](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md#ds-state-representation) reject earlier
experimental Dijkstra snapshots; imported legacy size/rate metadata is provisional.
These are implemented boundaries, not migration approval.

## Remaining deliverables

- [ ] Classify supported transitions and old outputs; prove or explicitly constrain
  the absence of duplicate/unfunded claims and preserve intended spendability.
- [ ] Specify activation, signed-transaction and mempool behavior, legacy bytes,
  experimental snapshot rejection/migration policy and node recovery boundaries.
- [ ] Define Store-backed projection for each supported Plutus version and its
  feature restrictions; identify the required implementation and test work.
- [ ] Record wallet, builder, governance and node impacts with owners and dependencies.
  Coordinate builder accounting with [#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) and output interfaces with [#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40).
- [ ] Record Nicolas's review and unresolved blockers; feed compatibility decisions
  into [Design rationale and adoption record](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24).

## Acceptance criteria retained

- Legacy state cannot acquire duplicate or unfunded claims.
- Era transition and serialization behavior are defined.
- Plutus, wallet, builder, governance and node impacts are documented.

A translated fixture or preserved legacy encoding is evidence for its stated scope;
neither establishes complete ecosystem compatibility.
