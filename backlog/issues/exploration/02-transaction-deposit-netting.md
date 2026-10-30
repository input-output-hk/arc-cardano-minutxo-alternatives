# Explore Ledger code impacts of transaction deposit netting

**Status:** In Progress — assessment available; reconciliation with the published Store/netting prototype and review outstanding.

**Owner:** Will Gould.

**Parent:** [Three-level Ledger exploration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39).

**Input contract:** [Output-role split](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40).

**Next level:** [Protocol dust-account settlement](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/42).

**Transversal work:** [Accounting interface refactor](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43).

## Current progress and remaining work — 30 October 2026

[Will's Ledger and builder assessment](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41#issuecomment-5796435821)
is available and remains attributed to Will. It assumes backing held in outputs,
recorded backing at least equal to required backing, and total-value getters that
include both application ADA and backing.

[Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3) at [`7b9b27480`](https://github.com/nhenin/cardano-ledger-specs/commit/7b9b274800e213a33bb2f55b1210e901d91034dc) now supplies an external-Store implementation with exact
TopTx/SubTx declarations, delegation, historical refunds and ordinary/collateral
accounting. Its [specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md) and [verification record](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md) are
evidence for the next review; they do not establish Will's agreement with that contract.

- [x] Record the existing Ledger/builder assessment and its assumptions.
- [x] Link published netting implementation and focused transaction-rule evidence.
- [ ] Pin Will's annotated Ledger and builder revisions and reconcile the assessment
  with external deposits, exact allocation, explicit declarations and nested transactions.
- [ ] Update builder input selection, change, collateral-return and serialization
  implications against that reconciled contract; demonstrate the remaining examples.
- [ ] Review the resulting split/netting contract with Nicolas, including local
  settlement, Plutus and activation dependencies.

The prototype's positive/zero/negative accounting checks and historical refunds are
implemented. The stronger local-release guarantee remains unresolved. Local results
include all 209 DepositStore contracts; [full CI](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763)
has a failed conformance job and broader validation remains outstanding.

## Objective

Specify how a transaction relates the capacity deposits released by consumed outputs
to the deposits allocated to created outputs, and design the Ledger/builder interfaces
needed to express that relationship. Establish what explicit netting adds to existing
ADA balancing rather than assuming that a new name or transaction field is necessary.
The result is a reviewed specification and implementation design with focused evidence,
not a completed settlement implementation or formal protocol adoption.

## Impact assessment and cross-level review

Will continues to own the netting investigation. His assessment is the starting
point for the remaining revision-pinned Ledger/builder impact work. Reconcile its
provisional assumptions with Nicolas's published split and Store implementation:

- [ ] Pin the Ledger and prototype revisions examined; map modules, functions,
  interfaces and consumers for transaction balancing, validation and deposit accounting.
- [ ] Trace existing ADA balancing and identify what explicit netting would change,
  what behavior must remain unchanged, and which interfaces may be affected.
- [ ] Record uncertainties and the focused experiments needed to resolve them;
  include reproducible commands and results for experiments performed.
- [ ] Link the shared, versioned provisional contract with #40; distinguish required
  new backing, actual allocation and releasable old backing, and identify the interfaces
  that supply or validate each quantity without double-counting it.
- [ ] Review the impact assessment with Nicolas and record the next specification/design
  steps, open dependencies and proposed implementation slices.

The remaining assessment and review establish the shared assumptions; implementation
evidence alone does not complete the specification, design or acceptance criteria.

## Scope

- Derive the current and split-output transaction accounting from pinned Ledger code.
- Define the inputs, outputs, timing and authorization of allocation and release.
- Distinguish required new backing, actual new allocation and releasable old backing.
- Specify how any net charge or release affects balancing and transaction construction.
- Cover successful execution, invalid transactions, collateral and parameter changes.
- Provide the settlement contract that can later be implemented by a protocol account.

## Design questions

The in-output split below is the earlier assessment baseline. Compare it explicitly
with the current external-Store contract when answering these questions.

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
