# 02 — Integrate the mechanism into `cardano-ledger` rules

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Blocked by M3

## Outcome

The mechanism is executed by the appropriate ledger transition rules.

## Acceptance criteria

- Required state, types, transaction fields, and serialization changes are implemented.
- Validation, settlement, and migration run through ledger rules.
- Era boundaries and backward compatibility follow the adopted specification.
- The relevant `cardano-ledger` packages build successfully.

## Signed backing change for mixed output forms

At revision `1c22597b03`, the builder and validator sign the change in external
deposits. The existing SubTx test spends a minimum-ADA input, creates a
deposit-backed output and expects the entire new external deposit as the
allocation. [Builder calculation](https://github.com/nhenin/cardano-ledger-specs/blob/1c22597b03e950e14d86e1d5ad86284ee5d7c1f3/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance/Internals.hs#L214-L223) · [Ledger calculation](https://github.com/nhenin/cardano-ledger-specs/blob/1c22597b03e950e14d86e1d5ad86284ee5d7c1f3/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/Rules/DepositStore/Accounting.hs#L109-L136) · [Mixed-form fixture](https://github.com/nhenin/cardano-ledger-specs/blob/1c22597b03e950e14d86e1d5ad86284ee5d7c1f3/libs/cardano-ledger-api/test/Test/Cardano/Ledger/Api/Tx/Body/DepositBalance/Fixture.hs#L124-L136) · [Current expectation](https://github.com/nhenin/cardano-ledger-specs/blob/1c22597b03e950e14d86e1d5ad86284ee5d7c1f3/libs/cardano-ledger-api/test/Test/Cardano/Ledger/Api/Tx/Body/DepositBalance/Spec.hs#L47-L55)

- [ ] Align the builder API, TopTx and SubTx declaration validation, and
      settlement with the [CIP’s netting rule](../../../CIP-%3F%3F%3F%3F/README.md#3322-netting-and-the-transaction-balance).
      Count historical backing for every ordinary spending input and active
      backing for every new ordinary output. Cap a minimum-ADA input’s
      contribution at the ADA it holds. Keep the external Store movement
      separate when balancing serialized output values.

Verify these cases against both the builder and ledger:

- Replacing 1.6 ADA of embedded backing with a 2 ADA external deposit signs
  **Allocate 0.4 ADA**. The Store grows by **2 ADA**. A fee input and change
  output with equal backing cancel in the declaration.
- Spending an imported input with 2 ADA against a 3 ADA historical minimum
  credits 2 ADA. Creating a 3 ADA deposit-backed successor signs **Allocate
  1 ADA** and grows the Store by **3 ADA**, assuming other backing cancels.
- Switching from 2 ADA of external backing to 2 ADA of embedded backing
  declares **zero** while the Store releases **2 ADA**. Check ADA conservation
  for each case and rejection of a declaration with the wrong reserve net.
