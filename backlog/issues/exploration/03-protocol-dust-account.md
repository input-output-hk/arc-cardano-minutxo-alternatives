# Explore protocol-managed capacity settlement through a dust account

**Status:** Planned — specification, design and exploration.

**Parent:** [Three-level Ledger exploration](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/39).

**Input contracts:** [Output-role split](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/40) and [transaction netting](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41).

**Transversal work:** [Accounting interface refactor](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/43).

## Objective

Determine how capacity backing can move out of application outputs into protocol-managed
accounting while preserving state protection, ADA conservation and solvent settlement.
Produce a precise specification and implementation design supported by focused evidence.
The dust account is a working architectural direction and name, not a settled choice
of refund policy, ownership, storage layout or formally approved protocol mechanism.

## Scope

- Define the aggregate backing and any records needed to associate obligations with UTxOs.
- Specify funding, allocation, consumption, release and any other permitted transfer.
- Connect the account to transaction netting, state totals, staking and collateral paths.
- Analyze historical allocations, changing parameters, migration and failure recovery.
- Measure the additional state and lookup costs rather than assuming aggregation is free.
- Compare concrete settlement/recording options within the working direction.

## Design questions

### Backing, obligations and historical information

1. What does the account hold, and what obligations does it owe? Define account balance,
   outstanding entitlements and any reserved or unallocated surplus separately.
2. What information identifies the obligation attached to a consumed UTxO: a recorded
   amount, a policy/version plus billed size, a sidecar/index, or another explicit design?
   An aggregate balance alone cannot identify arbitrary historical refund entitlements.
3. Where is that information stored, authenticated and removed? Evaluate per-output,
   shared and derived representations without silently choosing a receipt format.
4. Is release based on original allocation, a current rate or another rule? State who
   bears repricing gains/losses, when obligations change and how solvency is maintained.
5. Which facts can be recovered from live Ledger state alone? If a design needs historical
   transactions or parameters, specify the required availability and consensus state.

### State transitions and rights

6. Specify the payer, beneficiary, authorization and timing for each account transfer.
   Explain how consumed-input rights interact with multi-party transactions and netting.
7. Derive both the account balance transition and the outstanding-obligation transition.
   Show that the chosen relationship remains solvent, including boundary cases; do not
   assume that aggregate ADA conservation alone proves refund promises are backed.
8. How are duplicate release, reference-only access, missing or inconsistent records,
   overflow, invalid transactions and collateral-return allocation handled?
9. What changes in ADA-pot accounting, stake attribution and collateral availability when
   backing is no longer inside application outputs? Record economic choices explicitly.
10. How are existing outputs classified and initial backing/obligations established?
    Specify activation, legacy spendability, pending transactions, rollback and recovery.

## Deliverables

- A settlement specification covering state, rights, equations, validation, parameter
  changes, activation/migration and all permitted sources and destinations of ADA.
- A decision record comparing viable recording and release policies, their assumptions,
  economic consequences, storage cost and reasons for the selected or rejected options.
- A Ledger implementation design with pinned source references, proposed state/types,
  rule boundaries, interfaces, serialization, migration and stake/accounting integration.
- Worked traces plus a focused executable model or prototype validating conservation,
  obligation tracking, unique release and solvency across representative transitions.

## Acceptance criteria

- [ ] Backing and obligations are defined separately; allocation, funding, release and
  surplus cannot be confused, and every promised release has an explicit funding basis.
- [ ] The design identifies the information needed for each UTxO and demonstrates how
  it survives parameter changes and is removed or updated exactly once on consumption.
- [ ] Historical-price and current-price release options are evaluated explicitly;
  refund rights and repricing risk are reviewed choices, not accidental consequences.
- [ ] Account and obligation equations reconcile with transaction netting and total ADA;
  native assets remain application holdings and are not deposited in the account.
- [ ] Examples cover creation, replacement, consolidation, fan-out, complete release,
  changed parameters, adversarial/double release, failure/collateral and migration.
- [ ] Missing-state and insolvency scenarios are either excluded by proved conditions
  or handled by explicit rules; no undocumented external historical oracle is required.
- [ ] Staking, collateral, old-output spendability, signed transactions and state-storage
  consequences have concrete designs or clearly identified implementation blockers.
- [ ] Evidence records revisions, methods, results and limitations; Nicolas reviews the
  combined three-level contract and all material economic/consensus decisions.

## Dependencies and review gates

Investigate alongside split and netting using explicit assumptions; neither their full
implementation nor complete `Value` retirement is a prerequisite to this analysis.
Feed discoveries back into both contracts and the formal alternatives comparison.
A reviewed contract cannot be called implementation-ready while a material solvency,
ownership, historical-information or migration choice remains unresolved.

## Non-goals

No production account implementation, full integration certification, automatic protocol
adoption or central Ledger pull request is required. Broader rent, rewards or governance
redesign is not introduced implicitly; any necessary scope expansion requires review.
Exploration completion does not mark the integrated-prototype milestone complete.
