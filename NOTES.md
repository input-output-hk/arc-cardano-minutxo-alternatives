# Working notes — min-UTxO CPS

## Decisions needed from the team

**Scope.** The draft currently takes the narrow framing: the problem is that an
internal node constraint is exported to upper layers unmanaged, *not* that the UTxO
set shouldn't be bounded. Narrow is more defensible and harder to dismiss. The wider
framing ("is a per-output ada deposit the right bounding mechanism at all?") invites
a much longer fight. Confirm which one we're making.

**Authors.** ~~Who is on the preamble?~~ Decided 2026-08-06: Nicolas Henin, Will
Gould, Polina Vinogradova. Set on both the CPS and the CIP, Nicolas first as editor —
reorder if the team prefers otherwise.

Still open: Alexey Kuleshevich is the origin of the view the CIP specifies, and Polina
authored variants B and C. Both are credited inline, which is the usual treatment for
ideas contributed to a proposal someone else drafts. Confirm Alexey is content with an
in-text attribution rather than a preamble line before the CIP is circulated.

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

**Defect grid (added 2026-08-06).** CPS 2.3 now identifies five precise design
defects in two families — the deposit is **invisible** (D1 no identity, D2 no
attribution) and the requirement is **rigid** (D3 across the transaction, D4 across
time, D5 against real cost) — with triggers and a symptom-mapping table. A sixth candidate — no duration term in the price — was cut
as out of scope (Nicolas's call, 2026-08-06): the mechanism's goal is a bound on
UTxO entries, and a one-time deposit achieves that bound regardless of entry
lifetime; duration pricing is a different mechanism, kept only as a pricing-model
limit (CPS 2.2.6.3) and an open question (CPS 5.2). The stranding inequality moved
to use case 3.5, where it makes the dust quantification measurable. Follow-ups: the explainer and
`images/03-abstraction-gap.svg` still show the old three-box story and must be
regenerated to show the defect layer; the CIP's variant table (A/B/C) should state
which of D1–D6 each variant removes.

## Claims that must be verified before submission

| Claim | Status |
|---|---|
| `coinsPerUTxOByte` = 4,310 lovelace | Verified at mainnet epoch 647 using the pinned Koios epoch-parameter response |
| UTxO-HD has moved ledger state to disk | **Unverified — this is the strongest argument in the document. Do not draft around it until confirmed.** |
| SPO vote above 50% for `utxoCostPerByte` | Verified against the current constitutional guardrails |
| Highest assigned CPS number | Locally we have up to CPS-0029; check open PRs for claimed numbers |
| ~0.86 ADA ada-only, ~1.2 ADA with one NFT | Consistent with community figures of ~0.85 ADA undelegated and ~0.97 ADA delegated at `utxoCostPerByte = 4,310`; still recompute from the formula for the doc |
| Mary derivation gives 37,037 per unit, Alonzo genesis records 34,482 | **Unreconciled.** Also unresolved: the Mary document states `adaOnlyUTxOSize = 27` in bytes, but `⌊1,000,000 / 27⌋ = 37,037` only makes sense per word. Flagged inline in CPS 2.2.3 |
| 1 ada chosen from a transaction-impact analysis, not a resource measurement | Sourced from the 2020 origin thread; see the provenance section below |

## Missing evidence

CIP-9999 will not merge a CPS without use cases. Every entry in the Use Cases section
needs at least one concrete, citable instance:

- A real airdrop with recipient count and total ada immobilised
- The live CIP-68 discussion mentioning cost as an operational friction point
- A count of outputs currently below the economic-consolidation threshold
- Total ada committed to minimum-ada floors, split by output type

The dust and total-immobilised figures need a chain query. Worth asking whether
anyone has already run this.

## Where the parameter came from (answered 2026-08-05)

Asked in the `#ledger` channel. The answers close the "why 1 ada" question and are
now reflected in CPS sections 2.2.2, 2.2.3, and 2.2.6.4.

- **Brian Bush:** a simple worst-case computation of how many UTxOs the ledger could
  support; Jared Corduan likely involved. Pointed to the Mary-era derivation now cited
  as reference [5].
- **Samuel Leathers:** Jared Corduan and Duncan Coutts identified the issue during the
  Shelley rollout; dust was a Byron problem and this was the fix. Notes the value was
  discussed for reduction when ada was above one dollar.
- **The 2020 origin thread:** Duncan Coutts states the analysis was run for several
  candidate minimums, that roughly 99.9% of existing mainnet transactions would have
  been unaffected, and that the 1-ada figure was chosen from that analysis. The
  security concern named at the time is a dust attack, with Litecoin cited as
  precedent. Kevin Hammond flags revisiting it for micropayments or a higher ada price.

The underlying spreadsheet sits with Rhys Bartels-Waller and Alex Apeldoorn. Worth
requesting: it is the only quantified impact analysis anyone has produced for this
parameter, and section 2.2.6.4 argues no equivalent exists for the current value.

**Do not put the Slack attributions in the CPS.** The public document cites the
readthedocs derivation; the provenance above is context for us and for the Working
Group, not evidence a CIP editor can check.

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
