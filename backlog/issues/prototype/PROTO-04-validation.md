# Validate the Ledger prototype

**Milestone:** [M4 — Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestone/4) · **Status:** In progress — targeted checks passed; full validation open

## Evidence — 30 October 2026

**Tested revision:** `7b9b274800e213a33bb2f55b1210e901d91034dc`, published in
[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3).
**Newer reference:** `leios-prototype-snapshot-30-10` at
`9df9f98cce86c5f2195142b2c02dd9b39dd9dc7c`; ten conflicts remain.
These results do not validate integration with that snapshot.

| Check | Result |
|---|---|
| Clean isolated Dijkstra test build | Passed; 720.1 s. |
| Local DepositStore suite | 209 examples, zero failures; 420.1 s. |
| Local historical metadata/codec suite | 13 examples, zero failures; 71.4 s. |
| CI compiler matrix | GHC 9.6.7, 9.10.3, 9.12.4 and 9.14.1 passed; doctests passed. |
| CI formatting and Nix checks | Passed. |
| Final package-test matrix | 24 of 26 passed; Dijkstra and conformance failed. |
| Final workflow | Failed at 09:53:01 UTC: 39 successful jobs, three failed and one skipped. The third failure is the aggregate `Tests completed` gate, reporting `Some tests failed`. |

[Completed CI run 41019013763](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763)
· [Specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
· [Verification history](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md).

### Failed suites

| Suite | Result | Seed | Log |
|---|---|---|---|
| Dijkstra | 1,384 examples, 27 failures, two pending; 5,554.1647 s | `1847871563` | [Job 123956169842](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763/job/123956169842) |
| Conformance | 1,222 examples, 27 failures, 28 pending; 2,565.8291 s | `234347344` | [Job 123956169746](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763/job/123956169746) |

Both logs name the same 27 Dijkstra SubTx script cases: two UTXOW phase-2/budget
checks report `Expected Left, got Right`, and 25 SUBUTXOW checks report unexpected
predicate failures. This identifies the observed failures, not their cause.
No attribution to upstream or the prototype is established. Retain logs, seeds and
the [conformance failure artifact](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763/artifacts/12964468262)
with the baseline comparison and any proposed correction.

## Remaining work and completion criteria

- [ ] Reproduce and account for every failed case against the corresponding pinned
  upstream baseline before assigning cause; record commands, revisions, seeds and output.
- [ ] Review proposed corrections before changing ledger behavior or test expectations.
- [ ] After [upstream integration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/57),
  rerun the compiler matrix and relevant existing, legacy, binary, conformance and
  DepositStore suites at the exact resulting commit. Record the final outcome.
- [ ] Incorporate [remaining test coverage](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/58)
  and make remaining exclusions explicit; a focused pass cannot stand in for the full suite.
- [ ] Record meaningful memory/runtime and state-impact observations with methods
  and workloads. Test durations above are not production performance measurements.
- [ ] Resolve deviations from the reviewed specification or feed them back into
  [M3 #19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19),
  [compatibility #23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23)
  and [#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40)/[#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41)/[#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42).
  Record formal design review separately from implemented prototype evidence.
- [ ] Publish a reproducible feasibility result covering implementation cost,
  behavior, compatibility limits and production work excluded from the prototype.
  Complete M4 only after upstream integration and the relevant suites pass, with
  remaining design decisions resolved or explicitly retained under their review owners.

The completed implementation slices #26–28 supply evidence for this validation;
their closure does not complete #29 or M4.
