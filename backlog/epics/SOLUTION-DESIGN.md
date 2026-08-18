# Adopted Solution Design & Specification

## Context

The policy recommendation selects a direction, but it is not yet an implementation
contract. The selected implementation must be made precise before changes are made to
Ledger state, transaction validation, serialization, accounting, or migration behavior.

## Goal

Turn the approved policy recommendation into a complete and internally consistent
technical specification that can be implemented in `cardano-ledger`.

## Approach

1. Define the adopted solution architecture.
2. Specify Ledger state and validation rules.
3. Specify economic settlement and accounting.
4. Specify transition and ecosystem compatibility.
5. Document the rationale for the selected internal design choices.

## Outcome

A reviewed implementation contract covering architecture, state, validation,
accounting, transition, compatibility, and rationale, ready to be tested through the
integrated prototype.
