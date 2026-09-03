# Explore the Ledger across output splitting, transaction netting, and protocol settlement

**Status:** Planned — specification, design and exploration.

## Purpose

Produce a precise specification and a concrete implementation design for the
workstream's three-level minUTxO direction, grounded in active exploration of the
current `cardano-ledger` codebase.

The direction is already preferred and informally adopted as a working architecture.
Exploration must expose its constraints, costs, counterexamples and remaining choices.
It is not presented as an unbiased search or as a completed comparison of alternatives.
The existing alternatives work still needs to make the reasoning and trade-offs
explicit, reviewable and evidence-backed before a formal recommendation.

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
