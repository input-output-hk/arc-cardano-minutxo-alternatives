# 03 — Implement invariant and compatibility tests

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Proposed

## Outcome

Executable evidence that the integrated implementation preserves the required invariants.

## Acceptance criteria

- QuickCheck covers conservation, solvency, capacity, unique release, and determinism.
- Integration tests cover creation, consumption, repricing, and migration paths.
- Serialization and compatibility round trips are tested.
- Adversarial and boundary cases are included.
- Relevant existing Ledger tests remain green.
