# Integrate the DepositStore prototype with the newer Ledger snapshot

**Milestone:** [M4 — Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Open — conflict review and integration outstanding

## Scope and starting evidence — 30 October 2026

This task receives the upstream integration requirement from #26–28. The delivered
prototype is [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3),
head `v2-minutxo` at `7b9b274800e213a33bb2f55b1210e901d91034dc`, incorporating
upstream through `8a15ddc07`. Its base is `leios-prototype-snapshot-30-10` at
`9df9f98cce86c5f2195142b2c02dd9b39dd9dc7c`; ten conflicts remain unresolved.

[CI run 41019013763](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763)
tested the earlier published head, not an integration with the newer snapshot.
All four compiler builds passed; 24/26 package jobs passed and Dijkstra/conformance
failed. [Validation #29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29)
records the precise failure evidence without attributing its cause.

## Completion criteria

- [ ] Inventory all ten conflicts with exact base/head commits and source locations;
  distinguish upstream changes, prototype changes and unresolved semantic choices.
- [ ] Present the proposed resolutions and affected behavior for Nicolas's review
  **before code changes**. Route architecture, compatibility and economic choices to
  [#19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19),
  [#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23)
  and [#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40)/[#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41)/[#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42).
- [ ] Apply reviewed resolutions, preserve the agreed Store and earlier-era
  contracts, and record the resulting integration commit and upstream ancestry.
- [ ] Build the supported compiler matrix and rerun relevant DepositStore,
  metadata/codec, legacy, binary, Dijkstra and conformance regressions at that exact
  commit. Retain commands, compiler versions, seeds, logs and final CI links.
- [ ] Compare failures with appropriate pinned baselines; review any corrections
  before implementing them. Complete integration only with the required checks
  passing, and transfer the evidence to #29 for the full feasibility assessment.

The [remaining coverage task](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58)
owns new or extended behavioral tests. This task does not select deferred Plutus
projection, repricing or stronger local-settlement policy, and successful integration
does not establish formal design adoption.
