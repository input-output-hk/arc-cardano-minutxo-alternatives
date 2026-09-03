# Explore transaction-level capacity-deposit netting

**Status:** Planned — specification, design and exploration.

**Parent:** [Three-level Ledger exploration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39).

**Input contract:** [Output-role split](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40).

**Next level:** [Protocol dust-account settlement](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42).

**Transversal work:** [Accounting interface refactor](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43).

## Objective

Specify how a transaction relates the capacity deposits released by consumed outputs
to the deposits allocated to created outputs, and design the Ledger/builder interfaces
needed to express that relationship. Establish what explicit netting adds to existing
ADA balancing rather than assuming that a new name or transaction field is necessary.
The result is a reviewed specification and implementation design with focused evidence,
not a completed settlement implementation or formal protocol adoption.

## Scope

- Derive the current and split-output transaction accounting from pinned Ledger code.
- Define the inputs, outputs, timing and authorization of allocation and release.
- Distinguish required new backing, actual new allocation and releasable old backing.
- Specify how any net charge or release affects balancing and transaction construction.
- Cover successful execution, invalid transactions, collateral and parameter changes.
- Provide the settlement contract that can later be implemented by a protocol account.

## Design questions

### What changes beyond existing balancing?

1. Show how ADA already flows between consumed and created outputs under the current
   rules, then derive the corresponding equation after the in-output split.
2. Start from the candidate identity
   `netCapacityCharge = depositsAllocatedToCreatedOutputs - depositsReleasedFromConsumedOutputs`.
   Define its terms precisely; positive, zero and negative results are distinct cases.
3. Which additional semantics are actually needed: explicit accounting terms, builder
   interfaces, constraints, transaction declarations, or changed ownership of refunds?
   Explain why an algebraic rearrangement alone does or does not meet the objective.
4. Does the Ledger derive the net amount, verify a declared amount, or need no new field?
   Compare options before deciding serialization or public-interface changes.

### Funding, release and authorization

5. Which recorded fact establishes the releasable amount? Specify whether historical
   allocation or current parameters determine it; do not recompute old backing silently.
6. Who may fund the new allocation and receive the release, including transactions
   combining multiple owners or scripts? What authorizes the resulting ADA allocation?
7. Show the full ADA equation with all supported era terms and separate native-asset
   conservation. Count capacity backing exactly once, not both inside `OutputCoins`
   and again as a net charge in the same equation.
8. Which outputs participate? Reference inputs cannot release backing; an input cannot
   release twice. Specify the effects of script failure and collateral-return creation.
9. How do parameter changes, validity intervals, mempool revalidation and era activation
   affect required funding, release entitlement and builder convergence?

## Deliverables

- A netting specification with state/transaction dependencies, signed equations,
  authorization, validation failures and parameter/activation behavior.
- A side-by-side account of current balancing, split-output balancing and the proposed
  explicit contract, identifying both unchanged behavior and the exact intended delta.
- A Ledger/builder implementation design: source locations, proposed signatures,
  construction flow, wire decisions, compatibility adapters and reviewable slices.
- A worked-example set plus an executable model or targeted prototype tests, and a
  decision register linking assumptions to the split and protocol-settlement designs.

## Acceptance criteria

- [ ] The reviewed specification defines allocation, release and net amount without
  treating output minimum, recorded deposit and available application ADA as synonyms.
- [ ] The added semantics over existing implicit balancing are demonstrated concretely;
  a new transaction field is neither presumed necessary nor excluded without analysis.
- [ ] Positive, zero and negative net cases reconcile to the complete ADA equation;
  backing is counted once and native assets remain conserved independently.
- [ ] Release authorization, multi-party funding, unique consumption, reference inputs,
  successful execution and collateral/failure behavior are explicitly specified.
- [ ] Examples cover same-size replacement, fan-out, consolidation, deletion, mint/burn,
  changed parameters and underfunding; builder implications are demonstrated.
- [ ] Focused evidence is reproducible and distinguishes model checks, prototype tests
  and untested integration paths; compilation alone is not behavioral validation.
- [ ] The design states exactly which contracts protocol-account settlement must retain
  or intentionally change, and Nicolas reviews the remaining cross-level decisions.

## Dependencies and review gates

Exploration can begin with explicit provisional split assumptions; it need not wait
for full split implementation or complete replacement of generic `Value` interfaces.
Review the final split/netting equations together before calling either contract stable.
Resolve material funding, release-rights and compatibility questions before describing
the design as implementation-ready; document an identified blocker rather than hiding it.

## Non-goals

No protocol-managed pot, historical-receipt storage implementation, generalized rent
policy or production builder migration is required for this exploration ticket.
Do not choose dust-account refund or staking rules here by implication.
Completion is a reviewed netting contract and design, not the integrated prototype
milestone, a full-suite certification or approval to publish a central Ledger PR.
