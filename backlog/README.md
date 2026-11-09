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
| [Ledger Prototype #25](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25) | Does the Ledger implement those rules correctly? | In progress | Reference integrated; agreed coverage and regressions pass. |
| [CIP #30](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/30) | What proposal can implementers review? | Todo | Author-approved submission package. |

These are deliverables, not sequential time periods. Research, specification and
implementation inform each other. “Phase 1” and “Phase 2” are no longer used to
explain the delivery structure.

The default **EPICS** view contains only these five peers. The programme and
historical bootstrap are tracked separately. [Exploration #39](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39) is superseded:
its review tasks now belong directly to Protocol Specification or Ledger Prototype.

## Published checkpoint — 9 November 2026

The 30 October Leios snapshot (`9df9f98cc`, 63 upstream commits) is integrated
in [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3). The [2 November integration run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41433981296) passed.
The [8 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42479739616) at `b77257163` passed all four compiler builds and the
package tests, including Dijkstra and conformance. The 27 SubTx cases that failed
on 30 October also passed locally after integration.

The published head [`2298a0085`](https://github.com/nhenin/cardano-ledger-specs/commit/2298a008589d5a0a5ea70bd1ec87d8477e989422) adds the legacy deposit cap clarification and a check
rejecting formula-version downgrades. Its [9 November CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/42592236836) was in progress at review.

Remaining work includes review of the integrated changes, coverage of the current
pricing contract, stake, voting, shared collateral and Plutus, and a feasibility
assessment with costs and compatibility limits.

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
| — | [Transition and ecosystem compatibility #23](issues/solution-design/04-transition-compatibility.md) |
| — | [Design rationale #24](issues/solution-design/05-rationale.md) |

## Ledger Prototype

**[M4](milestones/M4-PROTOTYPE.md)** — implementation delivered; integration and validation open.

| Completed at the published checkpoint | Remaining work |
|---|---|
| [Model #26](issues/prototype/PROTO-01-domain-model.md) | [Upstream integration #57](issues/prototype/upstream-integration.md) |
| [Ledger rules #27](issues/prototype/PROTO-02-ledger-integration.md) | [Coverage gaps #58](issues/prototype/remaining-test-coverage.md) |
| [Business suite #28](issues/prototype/PROTO-03-tests.md) | [Interface migration #43](issues/prototype/accounting-refactor.md) |
| — | [Regression validation #29](issues/prototype/PROTO-04-validation.md) |

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
