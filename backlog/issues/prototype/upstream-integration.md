# Integrate the DepositStore prototype with the newer Ledger snapshot

**Milestone:** [M4 — Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** In progress — reference integrated and tested; conflict review and sign-off remain to be recorded

## Integration evidence — 9 November 2026

The 30 October Leios snapshot (`9df9f98cc`, 63 upstream commits) is integrated
in [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3). The [2 November integration run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41433981296) passed.
The [8 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) at `b77257163` passed all four compiler builds and the
package tests, including Dijkstra and conformance. The 27 SubTx cases that failed
on 30 October also passed locally after integration.

The published head [`2298a0085`](https://github.com/nhenin/cardano-ledger-specs/commit/2298a008589d5a0a5ea70bd1ec87d8477e989422) adds the legacy deposit cap clarification and a check
rejecting formula-version downgrades. Its [9 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42592236836) was in progress at review.

The initial attempt at `7b9b27480` had ten conflicts with the reference and failed
two CI suites. The rebase preserves batch SubTx script evaluation and execution
budgets, phase-2-independent checks, and updated Leios PoolReap and genesis behavior.

## Completion criteria

- [ ] Inventory all ten conflicts with exact base/head commits and source locations;
  distinguish upstream changes, prototype changes and unresolved semantic choices.
- [ ] Present the proposed resolutions and affected behavior for Nicolas's review
  **before code changes**. Record the review outcome and route architecture, compatibility and economic choices to
  [#19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19),
  [#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23)
  and [#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40)/[#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41)/[#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42).
- [x] Apply the resolutions and record the integrated reference and ancestry in Ledger PR #3.
- [ ] Record review of the resulting Store and earlier-era contracts.
- [x] Run the compiler and package matrix on the integrated branch; see the 2 and 8 November runs above.
- [ ] Link the commands, compiler versions, seeds, logs and final reviewed revision in #29.
- [ ] Compare failures with appropriate pinned baselines; review any corrections
  before implementing them. Complete integration only with the required checks
  passing, and transfer the evidence to #29 for the full feasibility assessment.

The [remaining coverage task](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58)
owns new or extended behavioral tests. This task does not select deferred Plutus
projection, repricing or stronger local-settlement policy, and successful integration
does not establish formal design adoption.
