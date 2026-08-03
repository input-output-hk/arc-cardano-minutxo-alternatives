# Working notes — min-UTxO CPS

## Decisions needed from the team

**Scope.** The draft currently takes the narrow framing: the problem is that an
internal node constraint is exported to upper layers unmanaged, *not* that the UTxO
set shouldn't be bounded. Narrow is more defensible and harder to dismiss. The wider
framing ("is a per-output ada deposit the right bounding mechanism at all?") invites
a much longer fight. Confirm which one we're making.

**Authors.** Real names and emails are required by CIP-9999. Who is on the preamble —
Polina, Will, Nicolas Biri?

**Analogies.** VAT and the bottle-deposit (*consigne*) analogies are both partially
apt and both breakable. Deliberately kept out of the document: reviewers argue with
the analogy instead of the substance. Fine for the Ledger Working Group presentation,
not for the CPS.

**Candidate solution direction.** The current design sketch keeps the state-deposit
calculation but moves the ada out of `TxOut.Value` into a ledger-controlled reserve.
The transaction funds or receives the net difference between deposits created and
deposits consumed. This is documented in `CIP-????/README.md`; it is not yet a team
decision or a formal proposed solution in the CPS preamble.

**Release beneficiary.** The sketch credits the transaction that consumes the UTxO.
Confirm whether cleanup incentive is sufficient, or whether the original funder must
remain attributable.

**CIP-0159 relationship.** Treat CIP-0159 as adjacent prior art unless the Ledger
Working Group confirms its account machinery can implement a system-controlled
reserve. Do not state that CIP-0159 already specifies the dust-account mechanism.

## Claims that must be verified before submission

| Claim | Status |
|---|---|
| `coinsPerUTxOByte` = 4,310 lovelace | Verified at mainnet epoch 647 using the pinned Koios epoch-parameter response |
| UTxO-HD has moved ledger state to disk | **Unverified — this is the strongest argument in the document. Do not draft around it until confirmed.** |
| SPO vote above 50% for `utxoCostPerByte` | Verified against the current constitutional guardrails |
| Highest assigned CPS number | Locally we have up to CPS-0029; check open PRs for claimed numbers |
| ~0.86 ADA ada-only, ~1.2 ADA with one NFT | Approximate — recompute from the formula for the doc |

## Missing evidence

CIP-9999 will not merge a CPS without use cases. Every entry in the Use Cases section
needs at least one concrete, citable instance:

- A real airdrop with recipient count and total ada immobilised
- The live CIP-68 discussion mentioning cost as an operational friction point
- A count of outputs currently below the economic-consolidation threshold
- Total ada committed to minimum-ada floors, split by output type

The dust and total-immobilised figures need a chain query. Worth asking whether
anyone has already run this.

## Prior art to check

- **CIP-55** — introduced `coinsPerUTxOByte` at Babbage. Read the rationale; it is
  the last time this was formally reasoned about.
- **CPS-0009** (Coin Selection Including Native Tokens), **CPS-0018**, **CPS-0022** —
  cross-reference, avoid restating their problems.
- **CIP-0165**, **CIP-0159** — solution-space adjacent, cite as context only.
- A 2022 forum thread proposed cutting `utxoCostPerWord` from 34,482 to 3,000. Never
  became a CIP. Worth finding out why — that reason is likely to resurface.

## Process

- Folder is `CPS-????/` until a number is assigned. There is no draft status: the
  unmerged PR *is* the draft.
- Category: Ledger. License: CC-BY-4.0.
- `Proposed Solutions: []` stays empty until a CIP exists.
