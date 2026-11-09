# Review the Ledger prototype’s deposit rules and implementation

**Status:** Final detailed review by Nicolas. The prototype is nearly complete.

The integrated branch passed its latest completed [full CI run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) at `b77257163`,
including all four compiler builds and the Dijkstra and conformance package tests.
The newer `2298a0085` revision clarifies legacy deposit capping and rejects formula
version downgrades. [Current code](https://github.com/nhenin/cardano-ledger-specs/commit/2298a008589d5a0a5ea70bd1ec87d8477e989422) · [9 November run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42592236836)

**Remaining task.** Nicolas will check that the implementation behaves as intended
in the details. The new transaction DSL, formula mechanism and underlying state
logic are in place. Trace formula selection at allocation, extraction of the
output fields, and the deposit calculation itself. Check whether any superseded
minUTxO logic still runs on the new path, including the treatment of legacy
outputs. Record any concrete issue found during that review.
[Prototype rules](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/docs/dijkstra-deposit-store-rules.md) ·
[Verification record](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/docs/dijkstra-deposit-store-verification.md)

**After the prototype review.** Assess how the reviewed version would integrate with
Plutus in [Plutus assessment #23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23), then run the [private network test #60](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/60) and record the
tested revision and observed result.
