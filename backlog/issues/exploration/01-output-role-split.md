# Explore the output-role split: Assets and CapacityDeposit

**Status:** Planned — specification, design and exploration.

**Parent:** [Three-level Ledger exploration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39).

**Next level:** [Transaction deposit netting](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41).

**Transversal work:** [Accounting interface refactor](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43).

## Objective

Produce a precise specification and implementation design for separating
application-controlled assets from the ADA backing an output's persistent-state cost.
Support the design with source-grounded analysis and focused executable evidence.
This is the first level of a preferred working direction, not a claim of formal
protocol adoption or a completed integrated implementation.

## Scope

- Define `Assets` as holdings including ADA and native assets, not native assets alone.
- Define `CapacityDeposit` as a distinct ADA-denominated operational role.
- Identify the supported eras and exact output construction, read and update contracts.
- Trace output creation, validation, storage, spending, collateral and era transition.
- Identify effects on conservation, staking, Plutus, builders, serialization and sizing.
- Use the earlier split prototype as evidence and a source of counterexamples.

## Design questions

### Meaning, allocation and access

1. What distinguishes the deposit required by the rule, the amount actually allocated,
   and the amount recorded for later release? Can an output carry surplus backing?
2. Which quantity does each getter expose: application ADA, capacity backing, or total
   output ADA? Which updates are legal, and which require an allocation decision?
3. For the in-output split, specify the relation
   `outputCoins(o) = ada(assets(o)) + capacityDepositCoins(o)`.
   `OutputCoins` is an ADA-only role; the name does not decide its Haskell representation.
4. Does any real domain operation require a generic `Assets <> CapacityDeposit` bundle,
   or can explicit ADA and native-asset operations satisfy its contract?
   Record counterexamples; the absence of such a requirement is a hypothesis to test.

### Ledger and external boundaries

5. How are native-asset and ADA conservation checked separately without losing any
   era-specific fees, refunds, deposits, withdrawals or other accounting terms?
6. What happens on successful spending and on phase-2 failure, including collateral
   return? How are the two ADA roles represented in state totals and stake attribution?
7. Which representation is visible to each Plutus language version and existing tools?
   Identify intentional changes separately from contracts that must remain unchanged.
8. What encoding, compact representation and sizing rule are proposed? If old bytes
   acquire a new interpretation, specify the activation and signed-transaction risks.
9. How are existing outputs and transactions crossing an era or parameter boundary
   handled? Do not silently choose implicit allocation, explicit allocation or a hybrid.

## Deliverables

- A versioned split specification: concepts, state, allocation and validation rules,
  invariants, observable behavior, compatibility boundaries and decision rationale.
- An implementation map with pinned source references, proposed interfaces, affected
  rules/modules, compact paths, migration points and independently reviewable slices.
- Worked examples and focused tests/models covering ordinary and adverse cases.
- A decision register distinguishing observations, design choices and unresolved items,
  plus explicit contracts passed to netting and [protocol settlement](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42).

## Acceptance criteria

- [ ] Vocabulary, supported eras and construction/read/update laws are reviewed;
  application ADA is not excluded from `Assets` or silently reclassified by an accessor.
- [ ] The specification states the allocation basis, amount recorded and release-facing
  contract, including parameter changes and any retained open dependency on netting.
- [ ] Every affected boundary above has an explicit design or a documented blocker;
  ADA and native-asset conservation, collateral and stake effects are covered.
- [ ] The generic-aggregate hypothesis is tested against an inventoried consumer set;
  findings include counterexamples and justified residual representation adapters.
- [ ] Examples cover ADA-only and multiasset outputs, boundary funding, creation and
  consumption, invalid transactions, legacy outputs and activation boundaries.
- [ ] Focused evidence records revisions, commands/results and exclusions; prototype
  test results are not presented as proof that the full Ledger implementation is ready.
- [ ] Nicolas has reviewed the spec, implementation map and cross-level assumptions;
  unresolved consensus/economic choices block implementation-ready status.

## Dependencies and review gates

Coordinate interface changes with the accounting refactor, but do not require its
complete retirement of `Value` before investigating this level or the next ones.
Review concrete public-interface and wire choices before implementing them.
Netting may be explored against a clearly stated provisional split contract; changes
to that contract must be propagated and reviewed across both levels.

## Non-goals

No full Ledger integration, central-repository pull request, dust-account implementation,
new economic pricing policy or automatic adoption of the earlier spike is required here.
Completion means reviewed specification/design evidence for this level, not completion
of the integrated-prototype milestone or formal architectural approval.
