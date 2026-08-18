# ARC min-UTxO backlog

## Epic hierarchy

- [[ARC-09] [TV-15] IOR — MinUTxO alternatives — Phase 2](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/1) — `Epic`
  - [Stream Bootstrap & Initial Exploration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/3) — `Epic`, completed
  - [Problem Statement Definition (CPS)](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/7) — `Epic`
  - [Implementation Design Space Analysis & Policy Recommendation](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/89) — `Epic`
  - [Adopted Solution Design & Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/100) — `Epic`
  - [Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/101) — `Epic`
  - [CIP Authoring & Submission](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/117) — `Epic`

Each deliverable epic is assigned to its milestone. Its work items are GitHub
sub-issues, following the structure used by the PubSub stream.

## Milestones

| Milestone | Deliverable | Current state | Exit condition |
|---|---|---|---|
| [M1 — Problem Statement Definition (CPS)](milestones/M1-CPS.md) | Cardano Problem Statement | In progress | Reviewed and submission-ready |
| [M2 — Implementation Design Space Analysis & Policy Recommendation](milestones/M2-ALTERNATIVES-REPORT.md) | Design-space analysis and final policy recommendation | In progress | Recommendation reviewed and approved |
| [M3 — Adopted Solution Design & Specification](milestones/M3-SOLUTION-DESIGN.md) | Complete technical solution specification | Blocked by M2 recommendation | Reviewed implementation contract |
| [M4 — Integrated `cardano-ledger` Prototyping](milestones/M4-PROTOTYPE.md) | Integrated Ledger prototype | Exploratory checkpoint | Adopted semantics integrated and tested |
| [M5 — CIP Authoring & Submission](milestones/M5-CIP-AUTHORING.md) | Cardano Improvement Proposal | Blocked by stable M3/M4 results | Reviewed and submission-ready CIP |

## Delivery flow

```text
M1 — Problem Statement Definition (CPS): define and prove the problem
        ↓ requirements
M2 — Implementation Design Space Analysis & Policy Recommendation
Compare complete implementations and recommend policy
        ↓ selected architecture
M3 — Adopted Solution Design & Specification
Specify the selected mechanism completely
        ↓ implementation contract
M4 — Integrated cardano-ledger Prototyping
Integrate and validate the solution in Ledger rules
        ↓ validated design and findings
M5 — CIP Authoring & Submission
Write, review, and submit the CIP
```

Prototype findings may feed corrections back into M3 before CIP authoring, but M4 is not
complete until the mechanism is integrated into `cardano-ledger` rules.

## Sub-issues

### Stream Bootstrap & Initial Exploration — completed

The bootstrap work is retained as completed history and provides the ticket references
used by the first bi-weekly report.

1. [Establish the stream scope and working structure](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/4) — completed
2. [Review the current mechanism and initial source material](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/5) — completed
3. [Collect solution proposals and define the exploration plan](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/6) — completed

### M1 — Problem Statement Definition (CPS)

- [01 — Document the current mechanism and its provenance](issues/cps/current-mechanism-provenance.md) ([#1](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/8))
- [02 — Define the min-UTxO problem and formal model](issues/cps/problem-formal-model.md) ([#24](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/9))
- [03 — Produce and validate the mainnet evidence](issues/cps/mainnet-evidence.md) ([#2](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/10))
- [04 — Document use cases and required outcomes](issues/cps/use-cases-outcomes.md) ([#3](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/11))
- [05 — Assemble and review the CPS draft](issues/cps/assemble-review-draft.md) ([#35](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/115))
- [06 — Complete domain review and prepare submission](issues/cps/domain-review-submission.md) ([#4](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/13))

### M2 — Implementation Design Space Analysis & Policy Recommendation

| Issue | Status |
|---|---|
| [01 — Define the evaluation framework and invariants](issues/alternatives/ALT-01-evaluation-framework.md) | In progress |
| [02 — Construct complete candidate architectures](issues/alternatives/ALT-02-candidate-architectures.md) | In progress |
| [03 — Analyze trade-offs and compare implementations](issues/alternatives/ALT-03-tradeoff-analysis.md) | Proposed |
| [04 — Write the final policy recommendation](issues/alternatives/ALT-04-policy-report.md) | Proposed |

### M3 — Adopted Solution Design & Specification

1. [Define the adopted solution architecture](issues/solution-design/01-architecture.md) ([#38](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/118))
2. [Specify Ledger state and validation rules](issues/solution-design/02-ledger-rules.md) ([#9](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/21))
3. [Specify economic settlement and accounting](issues/solution-design/03-settlement-accounting.md) ([#10](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/80))
4. [Specify transition and ecosystem compatibility](issues/solution-design/04-transition-compatibility.md) ([#11](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/81))
5. [Document the design rationale](issues/solution-design/05-rationale.md) ([#39](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/119))

### M4 — Integrated `cardano-ledger` Prototyping

1. [Align the domain model with the adopted specification](issues/prototype/PROTO-01-domain-model.md) ([#13](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/83))
2. [Integrate the mechanism into Ledger rules](issues/prototype/PROTO-02-ledger-integration.md) ([#14](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/84))
3. [Implement invariant and compatibility tests](issues/prototype/PROTO-03-tests.md) ([#15](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/85))
4. [Validate and document prototype results](issues/prototype/PROTO-04-validation.md) ([#16](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/86))

### M5 — CIP Authoring & Submission

1. [Draft the CIP specification sections](issues/cip-authoring/01-draft-specification.md) ([#12](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/82))
2. [Write the rationale and alternatives-considered sections](issues/cip-authoring/02-rationale-alternatives.md) ([#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/130))
3. [Document compatibility, transition, and implementation path](issues/cip-authoring/03-compatibility-implementation.md) ([#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/131))
4. [Complete domain and editorial review](issues/cip-authoring/04-review.md) ([#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/132))
5. [Prepare the CIP submission](issues/cip-authoring/05-submission.md) ([#43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/133))

## Rules

- Cross-deliverable dependencies are links, not milestones.
- “Done” means the issue acceptance criteria are met.
- Uncommitted source work is “in progress,” not completed delivery.
- Structural changes to milestones, epics, and sub-issues are reviewed with Nicolas.
