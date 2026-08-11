# Project memory — ARC min-UTxO stream

Last updated: 2026-08-11
Owner: Nicolas Henin
Purpose: durable human and AI handoff, decision record, and biweekly-report source

## Instructions for future Codex or Claude sessions

Read this file before making material changes to the CPS, CIP, report, diagrams, or
ledger prototype. Then read the referenced source documents relevant to the task.

After material work, update:

1. **Current state** — what is true now;
2. **Decision record** — decisions and their rationale;
3. **Work log** — dated accomplishments and artifacts;
4. **Open questions and blockers**; and
5. **Next actions**.

Do not rely on chat history as project memory. Repository documents are the source of
truth. All public artifacts must be written in English. Slack attribution belongs in
private working notes, not in the public CPS or CIP.

## 1. Mission and deliverables

The ARC stream investigates Cardano's minimum-UTxO mechanism and alternatives that
preserve an adversarial bound on persistent ledger state while improving the
application and transaction-builder abstraction.

The working strategy is:

1. describe the current mechanism and problem accurately in a CPS;
2. identify the operational logic independently of its current representation;
3. evaluate whether proposed ledger mechanisms solve the problem;
4. compare alternatives and their trade-offs;
5. prototype the selected accounting model in `cardano-ledger`.

Official deliverable D3.1 is the minUTXO Problem Definition & Alternatives Report,
Trade-off Analysis, and Policy Recommendations, comprising a CPS, report, and CIP.

Primary artifacts:

- `CPS-????/README.md` — public problem statement;
- `CIP-????/README.md` — early solution and alternatives specification;
- `NOTES.md` — verification items and non-public provenance notes;
- `PROJECT_MEMORY.md` — canonical cross-session memory;
- `docs/cps-reasoning-log.md` — detailed local reasoning log; note that `docs/` is
  currently gitignored;
- `docs/slack-findings.md` — private Slack digest and proposal provenance;
- `cardano-ledger/` — local, gitignored prototype clone.

## 2. Current repository checkpoint

```text
branch: codex/cps-capacity-narrative
commit: 7ffd87d — Reframe UTxO capacity accounting
remote branch: origin/codex/cps-capacity-narrative
```

The checkpoint includes the current CPS capacity reasoning and revised diagrams. The
top-level `HANDOFF.md` predates this update and remains untracked; use this file as the
new canonical memory once committed.

Current uncommitted work after that checkpoint reorganizes the CPS narrative into:

```text
current mechanism
→ operational nature of UTxO capacity
→ theoretical bounds and calibration
→ abstraction mismatch and consequences
→ accounting implications for alternatives
→ use cases and required outcomes
```

## 3. Current conceptual position

### 3.1 Essential problem

The live UTxO set consumes finite node resources. A safe design must preserve a
defensible bound under adversarial conditions. The project does not argue that state
should be free or unbounded.

### 3.2 Current implementation

Cardano requires every created output to satisfy:

```math
\operatorname{coin}(o) \geq M(o,p)
```

The finite ada supply creates an indirect theoretical bound. The ada satisfying the
rule remains ordinary `TxOut.Value`; the ledger does not record a separate operational
deposit, depositor, release condition, or refund claim.

### 3.3 Abstraction leak

The current representation blends:

- **application value** — assets and state controlled by applications; and
- **operational funding** — the economic condition used to protect persistent state.

This produces two related leaks:

- **value leak:** operational funding is represented inside application value;
- **accounting leak:** builders and applications implement its allocation and
  lifecycle instead of merely funding a ledger-owned obligation.

### 3.4 Operational resource model

A live UTxO has at least two resource dimensions:

```math
c(o)=(1,s(o))
```

- `1` is the fixed UTxO-set entry — the box;
- `s(o)` is the variable serialized object inside the box.

These dimensions correspond to different performance concerns. Entry count is a
proxy for per-entry indexing, lookup, database-row, cache, and bookkeeping costs.
Serialized size is a proxy for disk footprint, bandwidth, serialization, snapshot,
and synchronization costs. A fixed-overhead-plus-bytes formula converts the first
into the second using an assumed exchange rate; one shared price parameter assumes
that relationship remains appropriate as node architecture changes.

Cardano's current scalarization is:

```math
U(t)=160N(t)+S(t)
```

Each UTxO contributes 160 virtual accounting bytes plus its billable serialized size.
The model therefore sets `p_box = 160 × p_byte` and economically bounds the weighted
sum `160N + S`, rather than independently bounding `N` and `S`.

Notation must preserve this distinction: `Cmax = (Nmax, Smax)` is the desired
two-dimensional capacity envelope, while `Umax` is the ceiling on the current scalar
projection `U = (160,1) · C`. Do not use `Cmax` for the scalar bound.

Global live allocation:

```math
N(t)=|\mathrm{UTxO}(t)|
```

```math
S(t)=\sum_{o\in\mathrm{UTxO}(t)}s(o)
```

`Nmax` and `Smax` are currently analytical bounds, not claims about explicit current
ledger counters.

The operational security objective is the component-wise capacity-envelope invariant:

```math
C(t)=(N(t),S(t))
\preceq
C_{\max}=(N_{\max},S_{\max})
```

An explicit-capacity implementation could reject allocations that exceed this
envelope. Cardano instead obtains an indirect economic ceiling from positive minimum
ada and finite ada supply. The envelope is the required security property; deposits
and pricing are mechanisms for rationing access to it.

### 3.5 Transactions are the allocation boundary

Outputs determine the resources occupied. Transactions are the operations that change
the allocation:

```math
\Delta_N(tx)=|\mathrm{outputs}(tx)|-|\mathrm{inputs}(tx)|
```

```math
\Delta_S(tx)=
\sum_{o\in\mathrm{outputs}(tx)}s(o)
-
\sum_{i\in\mathrm{inputs}(tx)}s(i)
```

```math
\Delta_C(tx)=(\Delta_N(tx),\Delta_S(tx))
```

Key statement:

> Outputs are the persistent objects being retained. Transactions are the operations
> that allocate and release retention capacity.

### 3.6 Deposit and release model

Conceptual price vector:

```math
p(t)=(p_{\mathrm{box}}(t),p_{\mathrm{byte}}(t))
```

Allocation value:

```math
D(o,t)=p_{\mathrm{box}}(t)+s(o)p_{\mathrm{byte}}(t)
```

At fixed prices, transaction-level funding is:

```math
\Delta_D(tx)=
p_{\mathrm{box}}(t)\Delta_N(tx)
+
p_{\mathrm{byte}}(t)\Delta_S(tx)
```

- positive delta: the transaction adds net burden and funds it;
- negative delta: the transaction removes net burden and receives a release;
- zero delta: the transaction replaces equivalent capacity.

### 3.7 Common-resource settlement

UTxO capacity is treated as a common resource maintained by node operators. The base
mechanism does not necessarily need to remember the original payer.

Preferred neutral rule:

```text
increase net burden → allocating transaction funds the increase
keep allocation live → backing remains in the protocol mechanism
decrease net burden → releasing transaction receives the release value
```

The release is bearer-like and follows valid consumption. It is not necessarily the
return of property held for a named depositor.

The corrected CPS defect is therefore:

> Operational funding has no explicit settlement rule. Its control is determined
> indirectly by application-value ownership.

The protocol must define settlement precisely while remaining flexible about personal
identity. Scripts and higher-level applications may decide how released value is used.

### Conservation and payment guarantee

The UTxO model ensures that capacity can be released only by consuming a previously
allocated, currently live out-ref. Whole-output consumption prevents double release.

For live per-output claims `q(o)` and internal reserve `B`, the solvency invariant is:

```math
B(t)=\sum_{o\in\mathrm{UTxO}(t)}q_t(o)
```

A transaction subtracts the claims of consumed inputs and adds the claims of created
outputs. If the invariant holds beforehand and no unrelated channel can debit the
reserve, every valid release is payable and the invariant is preserved afterward.
Original-payer identity is unnecessary. A price change that revalues live claims must
atomically rebalance the reserve before the new price becomes active.

### 3.8 Price changes and revaluation

Changing either capacity price revalues every live allocation:

```math
\Delta_P=
N(t)(p_{\mathrm{box},1}-p_{\mathrm{box},0})
+
S(t)(p_{\mathrm{byte},1}-p_{\mathrm{byte},0})
```

This is distinct from an application transaction's allocation delta. The current
implementation has no separate operational balance sheet on which to settle it.

Candidate reserve invariant:

```math
B(t)=N(t)p_{\mathrm{box}}(t)+S(t)p_{\mathrm{byte}}(t)
```

Candidate settlement:

- upward repricing: treasury transfers `ΔP` into the capacity reserve;
- downward repricing: reserve transfers `|ΔP|` into treasury.

This treasury mechanism is candidate CIP material. The CPS should require every
adaptive mechanism to identify a revaluation counterparty without prescribing this
specific answer.

## 4. CPS narrative planned for the next version

The next CPS iteration should be reorganized around this sequence:

1. **Necessity:** persistent state must remain bounded.
2. **Current implementation:** Cardano puts an ada floor in every output.
3. **Operational nature:** each UTxO occupies a box plus variable content space;
   transactions allocate and release this capacity.
4. **Quantification:** derive the theoretical ceilings using the formal model, then
   ask whether parameters and reachable states are calibrated to measured node limits.
5. **Representation mismatch:** operational accounting is implemented through
   application value.
6. **Temporal mismatch:** global repricing has no explicit settlement layer.
7. **Observable consequences:** token coupling, builder burden, liquidity
   fragmentation, historical top-ups, and application-state friction.
8. **Required properties:** preserve the bound while restoring the abstraction
   boundary and defining allocation, release, repricing, solvency, and migration.

The CPS must visibly separate:

```text
current implementation
        ↓
underlying resource semantics
        ↓
problem caused by their representation
        ↓
requirements for alternatives
```

The CPS should not present the reserve or treasury mechanism as if it were current
ledger logic.

## 5. Alternative landscape

Active shortlist:

- **A — ledger-held operational accounting.** Builder funds a transaction-level net
  delta; the ledger owns settlement. This is currently the primary focus.
- **D — credential-bound backing.** Backing has an explicit credential and an
  authorized release path.
- **E — simple default plus credential opt-in.** Common protocol path by default,
  credential attribution only when required.

Removed from the active shortlist:

- **B — account-held obligation.** Original form lacks sufficient output-to-account
  attribution for deterministic release.
- **C — output-spread allocation.** Token and funding lineages can diverge, while the
  builder must manage signed allocations across sibling outputs.

The common-resource settlement model may reduce the need for credential attribution
in the default mechanism. D remains relevant only where a use case requires a personal
or credential-bound claim.

## 6. Prototype status

The local `cardano-ledger` clone is gitignored and lives under `cardano-ledger/`.
Historical handoff state as of 2026-08-07:

- branch `nicolas/minutxo-deposit`;
- pure DDD modules under `Cardano.Ledger.MinUtxoDeposit`;
- settlement, deposit, solvency, and requirement domains implemented;
- seven QuickCheck properties, 100 cases each, previously green under `-Werror`;
- ledger-rule wiring intentionally postponed pending the variant decision.

The prototype reflects the earlier `max(0,M-adaIn)` model. It has not yet been adapted
to the two-dimensional box/content model, common-resource settlement, or dynamic
treasury revaluation.

## 7. Important artifacts produced

### CPS

- expanded mechanism history and theoretical bounds;
- abstraction-leak framing;
- five observable consequences;
- capacity-allocation reasoning;
- fixed-entry and variable-size dimensions;
- transaction-level capacity deltas;
- time-dependent revaluation reasoning;
- revised common-resource settlement framing;
- updated required outcomes and TOC.

### CPS visuals

- `01-utxo-state.svg` — transaction and UTxO-state growth;
- `02-bounding-chain.svg` — finite-ada bounding chain;
- `03-abstraction-gap.svg` — abstraction leak and consequences;
- `04-payer-beneficiary-flow.svg` — current control versus explicit settlement;
- `05-reserve-bound-trajectory.svg` — reserve and bound trajectory;
- `06-hidden-operational-cost.svg` — hidden obligation in input and outputs.

### CIP

- Alternative A ledger-held deposit model;
- Alternatives B and C comparison;
- transaction-level `utxoDeposit` and `utxoRefund` accounting;
- open design decisions and prototype plan.

### Working visuals

Local, currently gitignored:

- `docs/visuals/builder-tx-chains.svg`;
- `docs/visuals/builder-tx-chains.png`;
- interactive transaction and capacity visualizations under the Codex visualization
  workspace.

## 8. Decision record

### 2026-08-03 to 2026-08-07

- Accepted that the CPS must preserve the adversarial UTxO-state bound.
- Narrowed the CPS to an abstraction-boundary problem rather than questioning whether
  persistent state should be priced at all.
- Documented Alexey's implicit-minUTxO proposal as Alternative A.
- Added Polina's account-held and output-spread proposals as B and C.
- Removed Robertino's dust account as a separate alternative; retained relevant
  compatibility criticism.
- Built and tested the initial ledger-domain prototype for Alternative A.
- Identified Polina's combined credential/anonymous proposal and the fee-like default
  synthesis as additional candidate directions.
- Kept state rent and duration pricing out of CPS scope.

### 2026-08-07 to 2026-08-11

- Reduced the active comparison to A, D, and E.
- Changed analysis from isolated output diagrams to complete transaction chains.
- Made token lineage and operational-funding lineage separate analytical objects.
- Established that every live UTxO, including a large-ada input, has a hidden
  operational role under the current representation.
- Identified transactions as the allocation/release boundary.
- Split capacity into the box and object-size dimensions.
- Added dynamic repricing and aggregate treasury/reserve settlement reasoning.
- Corrected the assumption that deposits must return to original funders.
- Reframed settlement as common-resource management: allocator funds, releaser is
  credited, and the base mechanism need not retain payer identity.
- Updated CPS text, TOC, required outcomes, and affected SVG diagrams.
- Committed and pushed checkpoint `7ffd87d` on
  `codex/cps-capacity-narrative`.

## 9. Biweekly report ledger

### Reporting period: 2026-07-28 to 2026-08-10

#### Objectives

- Establish the min-UTxO problem statement.
- Document why the existing bound exists and how it evolved.
- Collect and compare solution proposals.
- Begin a ledger-level feasibility prototype.

#### Completed

- Drafted the CPS and CIP repository structure.
- Added parameter provenance, historical analysis, theoretical UTxO bounds, and
  unresolved evidence flags.
- Defined the abstraction leak and its observable consequences.
- Documented Alternatives A, B, and C with diagrams and open decisions.
- Analysed the combined credential proposal and fee-like protocol-pot framing.
- Implemented the initial pure ledger-domain model and property tests.
- Recorded Slack findings, proposal provenance, and verification requirements.

#### Outcomes

- Established that the security bound is essential but its exposure through
  application value is an implementation choice.
- Identified ledger-held, account-held, and output-distributed accounting families.
- Deferred ledger-rule wiring until the accounting model is selected.

#### Risks and blockers

- Missing empirical use-case evidence.
- Unverified UTxO-HD assumptions.
- Unreconciled Mary/Alonzo parameter derivations.
- Unresolved deposit denomination and repricing semantics.

### Reporting period: 2026-08-11 to 2026-08-24 — in progress

#### Objectives

- Rebuild the CPS narrative around the operational nature of UTxO capacity.
- Model Alternative A through complete builder transaction chains.
- Clarify common-resource settlement and time-dependent pricing.
- Produce a reviewable next CPS version without losing the current checkpoint.

#### Completed as of 2026-08-11

- Added the hidden-operational-cost visual across consumed and created UTxOs.
- Defined box and variable-content capacity dimensions.
- Defined transaction-level allocation and release deltas.
- Added aggregate repricing and treasury/reserve reasoning.
- Reframed deposit ownership as a settlement-policy question.
- Revised the CPS and diagrams to remove original-payer refund as a universal
  requirement.
- Committed and pushed the current checkpoint.
- Created durable reasoning and reporting memory.
- Reorganized the CPS Problem section so the operational resource lifecycle is
  established before the abstraction leak is diagnosed.
- Added an explicit capacity-envelope invariant to connect the operational model back
  to the adversarial bound and distinguish the security property from its pricing
  mechanism.
- Split solution-neutral semantics from accounting implications: treasury-backed
  revaluation now appears only as an open mechanism-design question.
- Renumbered the CPS narrative and synchronized its TOC and cross-references.
- Moved the theoretical-bound hierarchy and parameter-calibration analysis after the
  formal capacity model, under “Quantifying the bound: is current protection
  sufficient?”.
- Completed an end-to-end coherence review of the revised Problem narrative.
- Corrected count-only descriptions of the current rule: finite ada directly bounds
  $U(t)=160N(t)+S(t)$; entry-count figures are projections of that scalar bound.
- Distinguished analytical safety limits $N_{\max},S_{\max}$ from supply-derived
  count projections $N_{\mathrm{ceiling}}$.
- Added the containment test
  $U_{\max}\leq\min(160N_{\max},S_{\max})$ to make calibration answer whether the
  current scalar reachable region fits inside the desired operational envelope.
- Renamed calibration headroom from byte-like $H_B$ to weighted-capacity $H_U$, and
  removed stale ordering references and notation collisions.
- Added the indirect per-output feasibility constraint
  $S(t)\leq N(t)s_{\max}^{\mathrm{out}}$, while distinguishing the complete-output
  ceiling induced by `maxTxSize` from the 5,000-byte `maxValueSize` limit.
- Refreshed quantitative examples to mainnet epoch 648: 36.550B ada resident in
  UTxOs, 8.480T priced units, a 53.002B box-only count projection, and 32.617B
  illustrative 100-byte outputs.
- Added ada-budget orders of magnitude and percentages of the 45B maximum supply.
- Compared the supply-derived ceilings with standard SPO hardware guidance and
  recorded only benchmark search ranges—not claims of measured limits—for
  `InMemory` ($10^7$–$10^8$ entries) and `OnDisk` ($10^8$–$10^9$ entries).
- Recorded the central evidence gap: hardware recommendations do not define
  $N_{\max}$ or $S_{\max}$; those require deadline-based node benchmarks.

#### Planned

- Produce the new CPS narrative version.
- Review whether the current five-defect grid remains the best explanatory structure.
- Move solution-specific treasury mechanics out of the problem narrative where
  necessary.
- Update the CIP and prototype only after the operational semantics are stable.

## 10. Open questions and blockers

1. Should the CPS call Section 2.4 “underlying operational logic” or more cautiously
   “a resource-allocation interpretation”?
2. Are entry count and serialized size sufficient resource dimensions?
3. Are capacity limits hard protocol limits, economic bounds, or analytical targets?
4. Should release use allocation-time price, current price, or another index?
5. What safeguards prevent treasury-funded repricing windfalls?
6. Must the capacity reserve be exactly backed or conservatively solvent?
7. Which use cases require credential-bound attribution after adopting a neutral
   common-resource release rule?
8. How should current embedded-value UTxOs migrate?
9. What empirical evidence is required before CPS submission?
10. How should the prototype evolve from `max(0,M-adaIn)` to the revised model?

## 11. Next actions

1. Obtain domain review of the new CPS narrative revision created after checkpoint
   `7ffd87d`, especially the analytical capacity envelope and calibration test.
2. Keep the opening factual: current mechanism, history, security objective, and
   evidence.
3. Introduce box/content operational semantics before enumerating the abstraction
   consequences.
4. State the mismatch between the semantics and `TxOut.Value` representation.
5. Keep treasury-backed repricing clearly labelled as candidate implementation.
6. Reassess A, D, and E against the revised common-resource model.
7. Update this file after each material reasoning or implementation session.

## 12. Biweekly report template

```markdown
## Reporting period: YYYY-MM-DD to YYYY-MM-DD

### Objectives
- ...

### Work completed
- ...

### Key decisions and rationale
- Decision — rationale.

### Artifacts produced or updated
- Path — purpose.

### Validation and evidence
- Tests, reviews, measurements, or references.

### Risks and blockers
- ...

### Next-period priorities
- ...
```
