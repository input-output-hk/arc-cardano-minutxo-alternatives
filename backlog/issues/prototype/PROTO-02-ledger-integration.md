# 02 — Integrate the mechanism into `cardano-ledger` rules

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** In progress — ledger integration implemented; upstream merge outstanding

## Progress — 30 October 2026

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) publishes
`7b9b274800e213a33bb2f55b1210e901d91034dc`. Closed PR #2 is historical.

- [x] Integrate declarations, exact net accounting, balance, authorization,
  settlement, minimum coin, Store-specific collateral and ledger effects.
- [x] Store outputs and historical allocations together; adapt shared-state readers,
  legacy codecs and era translations.
- [x] Build the published feature with GHC 9.6.7, 9.10.3, 9.12.4 and 9.14.1 in CI.
- [ ] Review and resolve the ten conflicts against `leios-prototype-snapshot-30-10`
  (`9df9f98cce86c5f2195142b2c02dd9b39dd9dc7c`). The current feature integrates
  upstream only through `8a15ddc07`.
- [ ] Rebuild and rerun the relevant suites at the resulting integrated revision;
  #29 tracks failures and evidence.
- [ ] Complete Store-backed Plutus context compatibility and review unresolved
  transition/design boundaries with #23 and #42.

The shared interfaces affect earlier eras; their semantics and formats require
regression evidence. Later unpushed Store/API cleanup is not counted at this checkpoint.

## Outcome

The mechanism is executed by the appropriate ledger transition rules.

## Acceptance criteria

- Required state, types, transaction fields, and serialization changes are implemented.
- Validation, settlement, and migration run through ledger rules.
- Era boundaries and backward compatibility follow the adopted specification.
- The relevant `cardano-ledger` packages build successfully.
