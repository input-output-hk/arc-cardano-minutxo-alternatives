# Implementation Design Space Analysis & Policy Recommendation

## Context

The CPS defines the problem and required outcomes, but it does not determine how the
Ledger should implement them. Individual ideas such as reserves, accounts, state
credits, or hard caps are not complete solutions until their capacity control,
settlement, representation, and transition behavior are specified together.

## Goal

Identify the implementation with the best overall trade-off for removing the
per-output minimum-ADA requirement while addressing the problem defined by the CPS.

## Approach

1. Define the common evaluation framework and required invariants.
2. Construct at least two complete candidate implementations.
3. Compare security, accounting, liquidity, staking, user-experience, ecosystem,
   parametrization, governance, and implementation trade-offs.
4. Produce the final policy recommendation and document why it was selected.

## Outcome

A reviewed design-space analysis that describes the viable implementations consistently,
records the evidence and trade-offs behind the decision, and selects the implementation
that proceeds to technical design.
