# Ledger Prototype

**Status:** Nearly complete, 9 November 2026.

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) implements the DepositStore rules and integrates the Leios reference. Store-backed
outputs carry application value while their deposits are funded separately. The Store uses
the allocation's historical formula to determine the refund. The latest completed [full CI run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) passed.

Nicolas is checking the implementation details in [final verification #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29).
That is the remaining work on this prototype.

## After verification

1. Assess how to integrate the prototype with Plutus, starting with Will's V4 work. [Compatibility #23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23)
2. Run a private network test using the reviewed prototype and record what happens.
