# MinUTxO alternatives backlog

**Purpose:** remove the need to embed minimum ADA in every application output while
preserving protection against adversarial Ledger-state growth.

[Programme #1](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/1) · [Project board](https://github.com/orgs/input-output-hk/projects/261)

## Deliverables

| Epic | Question | State | Done when |
|---|---|---|---|
| [Problem Definition #7](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/7) | What must an alternative solve? | **Done** | CPS-0037 published; merged 27 October. |
| [Architecture Decision #14](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14) | Which mechanism should we choose? | In progress | Alternatives compared; recommendation reviewed. |
| [Protocol Specification #19](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19) | What are its exact rules? | In progress | Candidate contracts reviewed; material decisions resolved. |
| [Ledger Prototype #25](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25) | Does the Ledger implement those rules correctly? | Nearly complete | Nicolas completes his detailed implementation review. |
| [CIP #30](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/30) | What proposal can implementers review? | Todo | Author-approved submission package. |

These are deliverables, not sequential time periods. Research, specification and
implementation inform each other. “Phase 1” and “Phase 2” are no longer used to
explain the delivery structure.

The default **EPICS** view contains only these five peers. The programme and
historical bootstrap are tracked separately. [Exploration #39](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39) is superseded:
its review tasks now belong directly to Protocol Specification or Ledger Prototype.

## Published checkpoint — 9 November 2026

The Ledger prototype is nearly complete. Nicolas's remaining task is to check the implementation
details. The latest completed [full CI run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) passed on the integrated prototype, including all four
compiler builds, Dijkstra and conformance. [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) includes the Leios reference and the versioned deposit calculation.

After that review, assess how the prototype fits into Plutus, then run a private network
test. Will's [V4 integration experiments](https://github.com/willjgould/cardano-minutxo-integration/commit/d2300267436d4cc6a4cb2dbc7898b9f98787192b) provide a starting point for the assessment.

## Problem Definition

**[M1](milestones/M1-CPS.md)** — [CPS-0037 publication](https://github.com/cardano-foundation/CIPs/pull/1268).

| Completed task | Evidence |
|---|---|
| [Mechanism #8](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/8) | [Provenance](issues/cps/current-mechanism-provenance.md) |
| [Problem model #9](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/9) | [Formal model](issues/cps/problem-formal-model.md) |
| [Use cases #11](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/11) | [Published cases and requirements](issues/cps/use-cases-outcomes.md) |
| [Draft #12](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/12) | [Assembly and review](issues/cps/assemble-review-draft.md) |
| [Submission #13](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/13) | [Domain review](issues/cps/domain-review-submission.md) |

Mainnet analysis and empirical application validation remain open under Architecture
Decision. CPS publication does not complete that research.

## Architecture Decision

**[M2](milestones/M2-ALTERNATIVES-REPORT.md)** — one reviewed recommendation.

| Task | Deliverable |
|---|---|
| [Framework #15](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/15) | [Common criteria and invariants](issues/alternatives/ALT-01-evaluation-framework.md) |
| [Candidates #16](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/16) | [At least two complete architectures](issues/alternatives/ALT-02-candidate-architectures.md) |
| [Comparison #17](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/17) | [Evidence and trade-offs](issues/alternatives/ALT-03-tradeoff-analysis.md) |
| [Recommendation #18](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/18) | [Reviewed choice](issues/alternatives/ALT-04-policy-report.md) |
| [Mainnet evidence #10](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/10) | [Reproducible analysis](issues/alternatives/mainnet-evidence.md), deferred |
| [Application evidence #56](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/56) | [Named examples and transaction traces](issues/alternatives/application-evidence.md) |

## Protocol Specification

**[M3](milestones/M3-SOLUTION-DESIGN.md)** — candidate publication is separate from review.

| Published candidate deliverable | Remaining review |
|---|---|
| [Architecture #20](issues/solution-design/01-architecture.md) | [Output representation #40](issues/exploration/01-output-role-split.md) |
| [State and rules #21](issues/solution-design/02-ledger-rules.md) | [Transaction netting #41](issues/exploration/02-transaction-deposit-netting.md) |
| [Accounting #22](issues/solution-design/03-settlement-accounting.md) | [Deposit settlement #42](issues/exploration/03-protocol-dust-account.md) |
| — | [Plutus integration and transition compatibility #23](issues/solution-design/04-transition-compatibility.md) |
| — | [Private network test #60](issues/solution-design/private-network-test.md), after the Plutus assessment |
| — | [Design rationale #24](issues/solution-design/05-rationale.md) |

## Ledger Prototype

**[M4](milestones/M4-PROTOTYPE.md)** — the [model](issues/prototype/PROTO-01-domain-model.md), [Ledger rules](issues/prototype/PROTO-02-ledger-integration.md), [business suite](issues/prototype/PROTO-03-tests.md) and [upstream integration](issues/prototype/upstream-integration.md) are delivered.

[Review deposit rules and implementation #29](issues/prototype/PROTO-04-validation.md) tracks Nicolas's verification.
[Plutus assessment #23](issues/solution-design/04-transition-compatibility.md) and the [private network test #60](issues/solution-design/private-network-test.md) follow.
The [broader interface migration #43](issues/prototype/accounting-refactor.md) and [extended coverage #58](issues/prototype/remaining-test-coverage.md) were closed as not planned for this prototype. Their tickets retain the ideas for later work.

## CIP

**[M5](milestones/M5-CIP-AUTHORING.md)** — draft and review the public proposal.

- [Specification #31](issues/cip-authoring/01-draft-specification.md)
- [Rationale #32](issues/cip-authoring/02-rationale-alternatives.md)
- [Compatibility #33](issues/cip-authoring/03-compatibility-implementation.md)
- [Review #34](issues/cip-authoring/04-review.md)
- [Submission #35](issues/cip-authoring/05-submission.md)

## History and tracking rules

[Initial ARC mandate](https://github.com/input-output-hk/ARC-operating-model/issues/63)
· [Bootstrap #3](epics/BOOTSTRAP.md)
· [Consolidated exploration #39](issues/exploration/ledger-design-exploration.md).

- Programme → deliverable epic → work item. Dependencies are links, not extra epics.
- Close a delivered scope only when its evidence is linked. Transfer remaining
  criteria to named open tasks before closing the original item.
- “Superseded” containers do not count as delivered work.
- Prototype implementation, formal design approval and full validation are separate outcomes.
- Board percentages count closed child issues; they do not estimate engineering effort.
- Structural changes are reviewed with Nicolas; this split was approved on 30 October 2026.
