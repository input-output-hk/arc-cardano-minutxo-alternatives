# ARC min-UTxO stream

## Context

Cardano's min-UTxO rule requires every output to contain a minimum amount of ADA. The
rule contributes to an adversarial bound on persistent UTxO state, but it also exposes
that operational requirement directly to applications and transaction builders. This
can constrain output construction, distribute ADA across application state, and make
some token, script, and high-output-count workflows harder to express or operate.

The stream investigates whether Cardano can preserve a defensible bound on persistent
ledger state while improving this abstraction. It considers the current mechanism's
history and mainnet incidence, changes in node state-management architecture, concrete
application use cases, alternative capacity-control and settlement mechanisms, and the
migration constraints of existing UTxOs.

## What are we trying to answer?

> What is the best trade-off for removing the requirement to embed a minimum amount
> of ADA in every UTxO, without compromising the security and operability of the chain?

Answering this requires separating two questions:

1. **What must remain protected?** Persistent UTxO state must remain within a
   defensible capacity envelope under adversarial behavior.
2. **How should that protection be implemented?** Capacity control, economic
   settlement, Ledger representation, and transition are design choices that should
   be evaluated independently before being combined into a complete solution.

## Scope

- Define the current min-UTxO mechanism, its provenance, and the problem experienced
  by applications and transaction builders.
- Establish a solution-neutral model for persistent UTxO capacity, allocation, and release.
- Quantify the current mechanism using reproducible Cardano mainnet evidence.
- Document concrete high-output-count, token/script, and economically stranded-output use cases.
- Construct and compare at least two complete implementations that remove the need
  for minimum ADA to remain embedded in each output.
- Evaluate security, solvency, liquidity, staking, compatibility, governance,
  parametrization, implementation cost, and user-experience trade-offs.
- Select and specify an adopted solution.
- Integrate the adopted design into `cardano-ledger` rules and validate its invariants.
- Produce a reviewed CIP based on the specification and prototype findings.

## Outcomes

1. **[Problem Statement Definition (CPS)](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/7)** — reviewed, evidence-backed definition of the problem and required outcomes.
2. **[Implementation Design Space Analysis & Policy Recommendation](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/89)** — comparison of complete implementations and final policy recommendation.
3. **[Adopted Solution Design & Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/100)** — implementation-ready technical design for the selected solution.
4. **[Integrated `cardano-ledger` Prototyping](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/101)** — integrated implementation and executable validation of the design.
5. **[CIP Authoring & Submission](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/117)** — reviewed CIP based on the specification and prototype findings.

## Success criteria

- The problem statement and quantitative claims are publicly reviewable and reproducible.
- At least two complete candidate implementations are documented and compared.
- The policy recommendation identifies one adopted solution and explains its trade-offs.
- The specification preserves the required security, conservation, solvency, and migration invariants.
- The prototype is integrated into `cardano-ledger` rules and the relevant tests pass.
- The final CIP is consistent with the reviewed specification and prototype findings.
