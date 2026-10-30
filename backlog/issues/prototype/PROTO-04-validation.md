# 04 — Validate and document prototype results

**Milestone:** [M4 — Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** In progress — targeted checks passed; full validation open

## Evidence — 30 October 2026

**Revision:** `7b9b274800e213a33bb2f55b1210e901d91034dc`, published in
[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3).
**Reference:** `leios-prototype-snapshot-30-10` at `9df9f98cc`; ten integration
conflicts remain. Results below do not validate a merge with that snapshot.

| Check | Result |
|---|---|
| Clean isolated Dijkstra test build | Passed; 720.1 s. |
| Local DepositStore suite | 209 examples, zero failures; 420.1 s. |
| Local historical metadata/codec suite | 13 examples, zero failures; 71.4 s. |
| CI compiler matrix | GHC 9.6.7, 9.10.3, 9.12.4 and 9.14.1 passed; doctests passed. |
| CI formatting and Nix checks | Passed. |
| Full package-test matrix | Not green; see the conformance failure below and the live run for other jobs. |

[Full CI run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763)
· [Specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
· [Verification history](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md).

### Conformance failure

[Job 123956169746](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763/job/123956169746)
reports **1,222 examples, 27 failures, 28 pending**, seed `234347344`.
The failures are Dijkstra SubTx script cases. One expects rejection for failed
SubTx phase-2 evaluation but observes acceptance; others report different predicate
failures. Their cause is not attributed here to upstream or to the prototype.
Keep the [failure artifact](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763/artifacts/12964468262)
with any baseline comparison and proposed correction.

## Next actions

- [ ] Account for every failed job using its exact revision, seed and failure output;
  compare with the corresponding upstream baseline before assigning the cause.
- [ ] Review any proposed correction before changing ledger behavior or test expectations.
- [ ] After #27's upstream integration, run and record the relevant suites again.
- [ ] Record remaining compatibility limits and meaningful memory/runtime measurements.
  Test durations are execution evidence, not production performance measurements.
- [ ] Complete the M3 design review before declaring the milestone delivered.

## Outcome

A reviewable feasibility result documenting implementation cost, behavior, and limitations.

## Acceptance criteria

- Build and test commands and results are reproducible.
- Performance and state-impact observations are recorded where meaningful.
- Deviations from the adopted specification are resolved or fed back into M3.
- Known limitations and production work not covered by the prototype are explicit.
- M4 is marked complete only after integration and the relevant test suite pass.
