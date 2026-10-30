# Integrated `cardano-ledger` Prototyping

**Status — 30 October 2026:** In progress. Integrated candidate published;
upstream integration and complete validation remain open.

## Current checkpoint

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) contains the
DepositStore implementation at `7b9b274800e213a33bb2f55b1210e901d91034dc`.
It replaces closed PR #2 and targets `leios-prototype-snapshot-30-10`.
Ten conflicts with the newer upstream snapshot remain unresolved.

- [x] Publish integrated output variants, declarations, historical allocation storage,
  transaction rules, Store-specific collateral and ledger-effect tests.
- [x] Run all 209 DepositStore examples and 13 metadata/codec examples successfully
  at the published head; pass all four CI compiler builds.
- [ ] Review the candidate model against the M3 specification (#26).
- [ ] Review upstream conflict resolutions and validate the resulting revision (#27).
- [ ] Complete the remaining pricing, distribution, Plutus and shared collateral
  coverage (#28).
- [ ] Complete full validation and account for CI failures (#29). The current
  conformance run has 27 failing Dijkstra SubTx script examples; their cause has
  not been attributed by this backlog review.

[Specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
· [Verification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md)
· [Live CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763).

The model is a working candidate, not a formally adopted protocol. The three-level
exploration in #39 feeds design review into this milestone; its tasks do not replace
the implementation and validation acceptance criteria below.

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
