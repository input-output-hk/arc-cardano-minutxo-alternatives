# Milestone M4 — Integrated `cardano-ledger` Prototyping

**Working artifact:** local `cardano-ledger` branch `nicolas/minutxo-deposit`

**State:** Exploratory checkpoint; blocked on stable CIP semantics

## Objective

Integrate the adopted solution into the appropriate `cardano-ledger` rules and provide
executable evidence that its semantics, invariants, and transition are feasible.

## Issues

1. [Align the domain model](../issues/prototype/PROTO-01-domain-model.md)
2. [Integrate Ledger rules](../issues/prototype/PROTO-02-ledger-integration.md)
3. [Implement invariant and compatibility tests](../issues/prototype/PROTO-03-tests.md)
4. [Validate and document prototype results](../issues/prototype/PROTO-04-validation.md)

## Acceptance criteria

- Domain and Ledger-rule semantics match the adopted solution specification.
- Required type and serialization changes are implemented.
- Validation and transition are integrated into `cardano-ledger` rules.
- QuickCheck, integration, compatibility, and relevant Ledger tests pass.
- Findings feed back into the CIP and delivery record.

The earlier `max(0,M-adaIn)` model and seven recorded QuickCheck properties are prior
exploration only; they do not complete this milestone.
