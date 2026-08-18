# 02 — Integrate the mechanism into `cardano-ledger` rules

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** Blocked by M3

## Outcome

The mechanism is executed by the appropriate ledger transition rules.

## Acceptance criteria

- Required state, types, transaction fields, and serialization changes are implemented.
- Validation, settlement, and migration run through ledger rules.
- Era boundaries and backward compatibility follow the adopted specification.
- The relevant `cardano-ledger` packages build successfully.
