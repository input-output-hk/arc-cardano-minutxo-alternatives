# Record design rationale and adoption decisions

**Parent:** [Protocol Specification](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/19).

**Status:** Todo — candidate choices exist; comparative rationale and review remain open.

## Responsibility

Connect the published candidate to [Architecture Decision](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14) and record
why material choices are selected, rejected or deferred. Maintain the decision
register and the cross-contract review; do not infer approval from implementation.

[Candidate architecture](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/20), [State and validation rules](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/21) and
[Deposit accounting](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/22) are published at `7b9b27480`. Their publication
closures transfer architecture acceptance and unresolved choices to this register,
[Output representation](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40), [Transaction netting](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41),
[Deposit settlement](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42) and [Compatibility](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/23).

## Remaining deliverables

- [ ] Link the comparison and recommendation, including evidence unfavorable to
  the preferred candidate; distinguish candidate choices from approved decisions.
- [ ] Record material alternatives, assumptions, trade-offs, risks and reasons for
  each selected or rejected internal design.
- [ ] Assign each unresolved decision and record its consequences and dependent
  implementation/tests; explicit deferral must state the supported contract.
- [ ] Record cross-contract review by Nicolas and the responsible contributors.
  Preserve Will's netting assessment and its reconciliation in [#41](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41).
- [ ] State the actual approval/adoption decision when made; maintain the unresolved
  gate until that evidence exists.

## Acceptance criteria retained

- Rationale links to the architecture comparison rather than duplicating it.
- Material design alternatives and rejected choices are recorded.
- Assumptions, trade-offs and remaining risks are explicit.

This consolidates the design-review obligations previously grouped under [#39](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39).
Validation findings from [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) feed the register; this task does not duplicate
the full-CI exit criterion.
