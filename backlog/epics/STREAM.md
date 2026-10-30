# [ARC-09] [TV-15] MinUTxO alternatives

**Programme** · Target: 10 January 2027 · Start date: not recorded.

**Purpose:** remove the need to embed minimum ADA in every application output while
preserving protection against adversarial growth of persistent Ledger state.

This is the programme, not a sixth deliverable epic. The previous “Phase 2” label
has been removed because it described a period rather than an outcome.

## Deliverables

| Epic | Question it answers | Status on 30 October 2026 |
|---|---|---|
| [Problem Definition](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/7) | What problem must an alternative solve? | Done: CPS-0037 published. |
| [Architecture Decision](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14) | Which complete mechanism should we choose, and why? | In progress: comparison and recommendation remain open. |
| [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19) | What are the exact rules of the candidate mechanism? | In progress: candidate contracts published; review and decisions remain. |
| [Ledger Prototype](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/25) | Can the Ledger implement those rules correctly? | In progress: implementation and focused tests published; integration and full validation remain. |
| [CIP](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/30) | What proposal can implementers review and adopt? | Todo: requires reviewed specification and prototype findings. |

Research, specification and prototyping inform each other. Publishing a prototype
neither selects the architecture formally nor completes compatibility review.

## Programme completion

- [ ] Compare at least two complete alternatives against the CPS requirements.
- [ ] Record the reviewed recommendation, trade-offs and evidence limitations.
- [ ] Review state, accounting, validation, transition and ecosystem contracts.
- [ ] Validate the integrated Ledger prototype against those contracts.
- [ ] Prepare an author-approved, submission-ready CIP.

Quantitative claims must have reproducible evidence or explicit limitations.
Separate follow-ups track [mainnet analysis](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/10) and
[application evidence](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/56); they are not unfinished CPS publication tasks.

## History

[Initial exploration](https://github.com/input-output-hk/ARC-operating-model/issues/63)
retains the original ARC mandate. [Bootstrap](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/3) is completed setup work.
Neither is a peer of the five deliverable epics in the default EPICS view.
