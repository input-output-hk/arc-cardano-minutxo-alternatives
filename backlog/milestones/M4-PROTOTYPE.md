# Milestone M4 — Integrated `cardano-ledger` Prototyping

**State — 30 October 2026:** In progress. An integrated candidate is published;
upstream integration, remaining coverage and design review are outstanding.

**Working artifact:** [Ledger PR #3](https://github.com/nhenin/cardano-ledger-specs/pull/3),
`v2-minutxo` at `7b9b274800e213a33bb2f55b1210e901d91034dc`.
PR #2 is closed. The reference branch is `leios-prototype-snapshot-30-10`, at
`9df9f98cce86c5f2195142b2c02dd9b39dd9dc7c`. Ten merge conflicts remain;
the prototype has not yet integrated this newer upstream snapshot.

## Delivered evidence

| Area | Published evidence |
|---|---|
| Domain and state | Explicit output variants, TopTx/SubTx declarations, one `UTxOStore`, retained accepted sizes and creation-time calculations. |
| Ledger rules | Declaration requirements, exact net accounting, balance, authorization, settlement, minimum coin, Store-specific collateral and ledger effects. |
| Local tests at this head | 209 DepositStore examples passed in 420.1 seconds; 13 metadata/codec examples passed in 71.4 seconds. |
| Build | Clean isolated Dijkstra build; CI builds passed with GHC 9.6.7, 9.10.3, 9.12.4 and 9.14.1. |
| Full CI | Not green: the conformance job reports 27 failures in Dijkstra SubTx script cases. Attribution and the complete result remain under review. |

[Executable specification](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-rules.md)
· [Verification record](https://github.com/nhenin/cardano-ledger-specs/blob/7b9b274800e213a33bb2f55b1210e901d91034dc/docs/dijkstra-deposit-store-verification.md)
· [CI run](https://github.com/nhenin/cardano-ledger-specs/actions/runs/41019013763).

These results apply to the published feature head, not a resolved merge with the
new snapshot. Later local Store/API work is not included in this checkpoint.

## Remaining work

| Work | Tracked by | Completion evidence |
|---|---|---|
| Review the candidate model against M3 | [#26](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/26) | Decisions and unresolved semantics recorded; no implicit claim of protocol adoption. |
| Integrate the upstream snapshot | [#27](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/27) | Ten conflict resolutions reviewed, then the resulting revision rebuilt and tested. |
| Close coverage gaps | [#28](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/28) | Pricing, stake/voting, Plutus and shared collateral coverage explicitly accounted for. |
| Complete validation | [#29](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/29) | CI failures explained or resolved with reproducible evidence; relevant suites pass at the integrated head. |

## Objective

Integrate the adopted solution into the appropriate `cardano-ledger` rules and provide
executable evidence that its semantics, invariants, and transition are feasible.

## Issues

1. [Align the domain model](../issues/prototype/PROTO-01-domain-model.md)
2. [Integrate Ledger rules](../issues/prototype/PROTO-02-ledger-integration.md)
3. [Implement invariant and compatibility tests](../issues/prototype/PROTO-03-tests.md)
4. [Validate and document prototype results](../issues/prototype/PROTO-04-validation.md)

## Acceptance criteria

- Domain and Ledger-rule semantics match the adopted solution specification.
- Required type and serialization changes are implemented.
- Validation and transition are integrated into `cardano-ledger` rules.
- QuickCheck, integration, compatibility, and relevant Ledger tests pass.
- Findings feed back into the CIP and delivery record.

The earlier `max(0,M-adaIn)` model and seven QuickCheck properties are historical
exploration. The integrated prototype supersedes that checkpoint, but its existence
does not establish M2 recommendation approval, M3 adoption or M4 completion.
