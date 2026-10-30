# Ledger exploration — consolidated

**Status:** Closed as superseded, not completed.

The extra exploration epic duplicated the Protocol Specification and Ledger Prototype
deliverables. Its remaining work is now tracked directly in those epics:

| Work | Continuing issue | Parent |
|---|---|---|
| Output representation review | [#40](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40) | Protocol Specification #19 |
| Transaction netting review | [#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) | Protocol Specification #19 |
| Deposit settlement review | [#42](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) | Protocol Specification #19 |
| Ledger interface migration | [#43](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) | Ledger Prototype #25 |

Ownership and substantive review criteria are retained. Closing this container does
not certify design adoption, full validation or completion of its former children.

<details>
<summary>Previous scope, retained for traceability</summary>

# Explore the Ledger across output splitting, transaction netting, and protocol settlement

**Status:** In Progress — published integrated prototype; cross-level review and full validation outstanding.

## Current progress and remaining work — 30 October 2026

The current evidence is [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc). The pinned
[specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md) and [verification record](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md) describe output variants,
transaction declarations/netting, collateral and Store effects, accepted-size and
creation-price retention, serialization and legacy translation.

- [x] Publish the prototype and its specification/verification evidence.
- [x] Implement historical deposit refunds from retained accepted size and calculation,
  including restoration and later parameter changes.
- [ ] Reconcile Will's earlier in-output assessment with the external-Store contract;
  record the shared review and remaining builder/interface work.
- [ ] Resolve Plutus context projection and stronger local-settlement semantics.
  Explicit repricing and calculation-version selection remain separate design work;
  V2 currently has provisional V1 formula parity.
- [ ] Complete the full pricing, stake and voting test matrices and remaining shared
  collateral regressions; investigate CI failures and complete broader validation.
- [ ] Complete the reviewed alternatives, cross-level design and milestone deliverables.

Local checks passed all 209 DepositStore contracts and 13 Store metadata/codec checks.
All four GHC CI build jobs passed. The [full CI run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763)
has a failed conformance job; the cause is not yet attributed. Full validation remains
outstanding. These results do not establish formal adoption or completion of M3/M4.

## Purpose

Produce a precise specification and a concrete implementation design for the
workstream's three-level minUTxO direction, grounded in active exploration of the
current `cardano-ledger` codebase.

The direction is already preferred and informally adopted as a working architecture.
Exploration must expose its constraints, costs, counterexamples and remaining choices.
It is not presented as an unbiased search or as a completed comparison of alternatives.
The existing alternatives work still needs to make the reasoning and trade-offs
explicit, reviewable and evidence-backed before a formal recommendation.

## Track progress and review

| Track | Owner | Current evidence and next step |
|---|---|---|
| [Value split (#40)](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40) | Nicolas Henin | Output/Store integration published; finish the impact assessment and cross-level review |
| [Transaction deposit netting (#41)](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) | Will Gould | Earlier Ledger/builder assessment available; reconcile its assumptions with the published prototype |
| [Protocol settlement (#42)](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) | Unassigned | DepositStore prototype available; review policy, compatibility, cost and coverage gaps |
| [Accounting interfaces (#43)](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) | Unassigned | Interface slices published; complete the residual-consumer and compatibility audit |

The original Phase 1 impact-assessment and shared-contract deliverables remain part
of these tracks. Record affected modules, functions, interfaces and consumers at
pinned revisions, distinguish preserved behavior from changes, and propagate revised
assumptions across split and netting. Published implementation evidence does not
replace the outstanding reviews or complete #42/#43.

## Three cumulative levels

| Level | Design question | Expected result |
|---|---|---|
| [1 — Output-role split](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40) | How can an output distinguish application-controlled assets, including ADA, from capacity backing? | Output contracts, invariants and an impact map covering representation, accounting and compatibility |
| [2 — Transaction-level deposit netting](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41) | How are deposits released and required balanced explicitly at the transaction boundary? | Funding/release rules, conservation equations and builder/validation interfaces |
| [3 — Protocol dust account](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) | What must the protocol retain and guarantee when backing leaves application outputs? | State, entitlement and solvency model, settlement interfaces and transition design |

These are cumulative exploration levels, not three competing alternatives and not a
commitment to three separate protocol activations. Each level records which contract
it inherits and which behavior it intentionally changes.

[Asset, coin, and mint interface refinement](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43) is a transversal engineering
track. Changes must be justified by observed consumers and the three-level design.
Completing the entire `Value` retirement is not a prerequisite for investigating the
netting or dust-account models.

## Deliverables

For each level, produce linked review artifacts:

1. **Specification:** terminology, state, inputs/outputs, preconditions, equations,
   validation rules, invariants, failure behavior and worked examples.
2. **Implementation design:** concrete Ledger interfaces/modules/rules, read/write
   contracts, generic era support, representation, compatibility, migration and cost.
3. **Evidence:** revision-pinned code observations, focused experiments or executable
   models, reproducible commands/results, counterexamples and explicit limitations.

A cross-level synthesis connects the three specifications, records design decisions
and their rationale, and gives an implementation/test plan. Separate what the current
code demonstrates, what an experiment demonstrates, and what is still a hypothesis.

## Relationship to the existing backlog

- Parent: [Integrated Ledger Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25), as an exploration track, not completion of integrated implementation.
- Feed constraints and comparative evidence into [alternatives and recommendation](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14), including criteria #15, candidates #16, comparison #17 and recommendation #18.
- Feed the reviewed contract into [solution design and specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19), covering architecture #20, rules #21, settlement #22, transition #23 and rationale #24.
- Enable the existing implementation work #26–#29; do not close those tickets based on exploratory models or documents alone.

M2/M3/M4 are deliverable completion gates, not a prohibition on concurrent discovery.
Exploration and draft design can advance while the comparative recommendation is
being documented. This issue does not change existing milestone completion criteria.

## Acceptance criteria

- [ ] Each level has a reviewed specification, implementation design and focused
  evidence, linked from its issue and consistent with the other two levels.
- [ ] The cross-level contract explains ownership, funding, release, conservation,
  solvency, parameter changes, staking, collateral, failure paths and migration.
- [ ] Interfaces distinguish application holdings, ADA accounting and signed mint
  where necessary; `Assets` includes ADA and `OutputCoins` is an ADA-only role.
- [ ] The hypothesis that capacity accounting does not need a generic
  `Assets <> CapacityDeposit` operation is tested against concrete consumers.
  Counterexamples and legitimate native-asset aggregation needs are documented.
- [ ] The design states which changes are behavior-preserving refactors and which
  require protocol, encoding, script-context, builder or ecosystem changes.
- [ ] Consensus/economic choices necessary for the scoped mechanism are resolved.
  Any deferred work is explicitly outside that contract, with its consequences named.
- [ ] The alternatives work receives explicit constraints and evidence, including
  findings unfavorable to the preferred direction; comparison is not declared done.
- [ ] The resulting design is specific enough to plan small implementation commits
  and a verification matrix without hidden choices at the boundaries.

Finding that a level needs revision is a useful exploration result, but it does not
complete the promised spec/design. Likewise, a green focused experiment does not
demonstrate an integrated, production-ready Ledger implementation.

## Working and publication policy

Review the scope and the findings of each level before committing to its implementation
choices. Use small, signed, reviewable code slices on the personal Ledger fork when
an experiment is justified; no central Ledger pull request is implied.

</details>
