# Integrated `cardano-ledger` Prototyping

## Context

The adopted specification must be validated in the Ledger implementation rather than
only as a document or isolated model. Integration may expose type, serialization,
transition, accounting, or compatibility constraints that require the design to change.

## Goal

Implement the adopted specification in the appropriate `cardano-ledger` rules and
test whether its intended behavior and invariants hold in the integrated system.

## Approach

1. Align the domain model with the adopted specification.
2. Integrate the mechanism into Ledger rules and required state/serialization types.
3. Implement invariant, compatibility, and integration tests.
4. Validate the results and feed material findings back into the specification.

## Outcome

An integrated implementation with reproducible build and test results, documented
limitations, and enough evidence to confirm or revise the design before CIP authoring.
