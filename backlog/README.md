# ARC min-UTxO backlog

## Current implementation — 30 October 2026

The integrated DepositStore candidate is published in
[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3), at
`7b9b2748`. PR #2 is closed. The new reference branch,
`leios-prototype-snapshot-30-10`, contains the upstream snapshot fetched today;
ten integration conflicts remain unresolved.

| Delivered at this checkpoint | Still open |
|---|---|
| Explicit output variants, declarations, exact accounting and historical allocation storage | Design review, Store-backed Plutus projection and remaining interface work |
| 209 DepositStore examples and 13 metadata/codec examples pass locally | Full pricing, stake/voting and shared collateral coverage |
| All four CI compiler builds pass | Full test validation: the conformance job has 27 failures; investigate before attributing the cause |

Use [M4](milestones/M4-PROTOTYPE.md) for the implementation checkpoint,
[#27](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/27)
for upstream integration and
[#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29)
for validation. The [project board](https://github.com/orgs/input-output-hk/projects/261)
tracks active work. Local unpublished changes are not counted as delivered here.

## Epic hierarchy

- [[ARC-09] [TV-15] IOR — MinUTxO alternatives — Phase 2](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/1) — `Epic`
  - [Stream Bootstrap & Initial Exploration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/3) — `Epic`, completed
  - [Problem Statement Definition (CPS)](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/7) — `Epic`
  - [Implementation Design Space Analysis & Policy Recommendation](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14) — `Epic`
  - [Adopted Solution Design & Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19) — `Epic`
  - [Integrated cardano-ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25) — `Epic`
  - [CIP Authoring & Submission](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/30) — `Epic`

Each deliverable epic is assigned to its milestone. Its work items are GitHub
sub-issues, following the structure used by the PubSub stream.

## Milestones

| Milestone | Deliverable | Current state | Exit condition |
|---|---|---|---|
| [M1 — Problem Statement Definition (CPS)](milestones/M1-CPS.md) | Cardano Problem Statement | In progress | Reviewed and submission-ready |
| [M2 — Implementation Design Space Analysis & Policy Recommendation](milestones/M2-ALTERNATIVES-REPORT.md) | Design-space analysis and final policy recommendation | In progress | Recommendation reviewed and approved |
| [M3 — Adopted Solution Design & Specification](milestones/M3-SOLUTION-DESIGN.md) | Complete technical solution specification | Candidate specification available; adoption awaits M2 and review | Reviewed implementation contract |
| [M4 — Integrated `cardano-ledger` Prototyping](milestones/M4-PROTOTYPE.md) | Integrated Ledger prototype | In progress: published implementation; integration and validation open | Adopted semantics integrated and tested |
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

Prototype findings feed corrections back into M3 before CIP authoring. M4 now has
an integrated candidate, but remains open until design review, upstream integration
and the relevant validation are complete.

These are deliverable completion gates, not a requirement to finish all comparison
work before exploring the codebase. The exploration below feeds evidence into M2 and
draft contracts into M3 while keeping M4's integrated-implementation criteria intact.

## Cross-level design review

[Issue #39](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39),
under the existing prototype epic #25, tracks the design and interface review across
output representation, transaction netting and protocol settlement. Published prototype
evidence now informs that review. Comparative analysis and the final recommendation
remain separate deliverables; implementation does not establish formal adoption.

| Work item | Issue | Current focus |
|---|---|---|
| Cross-level review | [#39](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39) | [Reconcile the implemented candidate and open decisions](issues/exploration/ledger-design-exploration.md). |
| Output representation | [#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40) | [Review implemented output variants and remaining compatibility](issues/exploration/01-output-role-split.md). |
| Transaction netting | [#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) | [Reconcile Will's assessment with the published Store/netting contract](issues/exploration/02-transaction-deposit-netting.md). |
| Protocol backing | [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) | [Review historical refunds, pricing evolution and settlement guarantees](issues/exploration/03-protocol-dust-account.md). |
| Accounting interfaces | [#43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) | [Audit remaining consumers, mint semantics and compatibility](issues/prototype/accounting-refactor.md). |

The three levels are cumulative; they are not three competing alternatives or three
pre-approved activations. The interface refactor supports the exploration and does
not have to be completed wholesale before netting or dust-account investigation.

## Sub-issues

### Stream Bootstrap & Initial Exploration — completed

The bootstrap work is retained as completed history and provides the ticket references
used by the first bi-weekly report.

1. [Establish the stream scope and working structure](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/4) — completed
2. [Review the current mechanism and initial source material](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/5) — completed
3. [Collect solution proposals and define the exploration plan](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/6) — completed

### M1 — Problem Statement Definition (CPS)

- [01 — Document the current mechanism and its provenance](issues/cps/current-mechanism-provenance.md) ([#8](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/8))
- [02 — Define the min-UTxO problem and formal model](issues/cps/problem-formal-model.md) ([#9](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/9))
- [03 — Produce and validate the mainnet evidence](issues/cps/mainnet-evidence.md) ([#10](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/10))
- [04 — Document use cases and required outcomes](issues/cps/use-cases-outcomes.md) ([#11](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/11))
- [05 — Assemble and review the CPS draft](issues/cps/assemble-review-draft.md) ([#12](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/12))
- [06 — Complete domain review and prepare submission](issues/cps/domain-review-submission.md) ([#13](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/13))

### M2 — Implementation Design Space Analysis & Policy Recommendation

| Issue | Status |
|---|---|
| [01 — Define the evaluation framework and invariants](issues/alternatives/ALT-01-evaluation-framework.md) | In progress |
| [02 — Construct complete candidate architectures](issues/alternatives/ALT-02-candidate-architectures.md) | In progress |
| [03 — Analyze trade-offs and compare implementations](issues/alternatives/ALT-03-tradeoff-analysis.md) | Proposed |
| [04 — Write the final policy recommendation](issues/alternatives/ALT-04-policy-report.md) | Proposed |

### M3 — Adopted Solution Design & Specification

1. [Define the adopted solution architecture](issues/solution-design/01-architecture.md) ([#20](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/20))
2. [Specify Ledger state and validation rules](issues/solution-design/02-ledger-rules.md) ([#21](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/21))
3. [Specify economic settlement and accounting](issues/solution-design/03-settlement-accounting.md) ([#22](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/22))
4. [Specify transition and ecosystem compatibility](issues/solution-design/04-transition-compatibility.md) ([#23](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23))
5. [Document the design rationale](issues/solution-design/05-rationale.md) ([#24](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/24))

### M4 — Integrated `cardano-ledger` Prototyping

All four tasks are in progress. Their delivered evidence and remaining acceptance
criteria are recorded separately; none is closed merely because the prototype builds.

1. [Align the domain model with the adopted specification](issues/prototype/PROTO-01-domain-model.md) ([#26](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/26))
2. [Integrate the mechanism into Ledger rules](issues/prototype/PROTO-02-ledger-integration.md) ([#27](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/27))
3. [Implement invariant and compatibility tests](issues/prototype/PROTO-03-tests.md) ([#28](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/28))
4. [Validate and document prototype results](issues/prototype/PROTO-04-validation.md) ([#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29))

### M5 — CIP Authoring & Submission

1. [Draft the CIP specification sections](issues/cip-authoring/01-draft-specification.md) ([#31](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/31))
2. [Write the rationale and alternatives-considered sections](issues/cip-authoring/02-rationale-alternatives.md) ([#32](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/32))
3. [Document compatibility, transition, and implementation path](issues/cip-authoring/03-compatibility-implementation.md) ([#33](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/33))
4. [Complete domain and editorial review](issues/cip-authoring/04-review.md) ([#34](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/34))
5. [Prepare the CIP submission](issues/cip-authoring/05-submission.md) ([#35](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/35))

## Rules

- Cross-deliverable dependencies are links, not milestones.
- “Done” means the issue acceptance criteria are met.
- Uncommitted source work is “in progress,” not completed delivery.
- Structural changes to milestones, epics, and sub-issues are reviewed with Nicolas.
