# Review transition and ecosystem compatibility

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Next step after prototype verification:** assess how the reviewed Ledger prototype
would integrate with Plutus. The review with Philip DiSarro, Will, Polina and Nicolas is planned for the
week of 16 November. Nicolas asked Will to lead it.
Start with Will's V4 results, including the values and
backing exposed to scripts, and identify what carries over to the reviewed revision.
One option to evaluate is a new script version that reads both legacy and new
inputs, exposes their backing and application value separately, and allows a
validator to inspect transaction-level deposit netting. Check the effect on
earlier script versions. A private network test follows this assessment. [Prototype verification #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29)

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

## Wider protocol compatibility work

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

## Evidence for review — 9 November 2026

Will's 4 November integration preserved total output value and exposed backing
and application value through both V4 libraries. Three live V4 spends passed.
A local Conway-to-Dijkstra chain replayed, loaded its migrated snapshot and
resumed after interruption. Earlier validator versions and mainnet replay costs
still require evidence. [Pinned downstream integration](https://github.com/willjgould/cardano-minutxo-integration/commit/d2300267436d4cc6a4cb2dbc7898b9f98787192b)

The Ledger prototype subsequently introduced allocation origins and formula
history. Imported entries use the initial formula. Later changes leave existing
allocations priced at their historical formula, and a V2 activation prevents a
return to V1. Verify the downstream fixture on matching revisions and review
these activation and refund semantics before adopting a compatibility contract.
[Formula history](https://github.com/nhenin/cardano-ledger-specs/commit/660d0d96c24613a42cd3131a38a653ab1e39c6cf) · [Activation guard](https://github.com/nhenin/cardano-ledger-specs/commit/2298a008589d5a0a5ea70bd1ec87d8477e989422)
