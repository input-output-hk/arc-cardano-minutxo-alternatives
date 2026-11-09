# Integrate the DepositStore prototype with the newer Ledger snapshot

**Status:** Complete.

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) incorporates all 63 previously missing commits from the 30 October Leios
snapshot (`9df9f98cc`). The integration combines the deposit Store with the updated
SubTx script evaluation, execution budgets, PoolReap and genesis behavior.

The [2 November integration run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41433981296) and the
[8 November compiler and package matrix](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) passed,
including Dijkstra and conformance. [Final prototype verification #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) tracks
Nicolas's remaining detailed review.
