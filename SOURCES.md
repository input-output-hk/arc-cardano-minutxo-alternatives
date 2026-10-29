# Sources and reconstruction method

## Source repository

- Repository: [`input-output-hk/arc-cardano-minutxo-alternatives`](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives)
- Report update prepared: 29 October 2026
- The 22 September–5 October report is finalized for that reporting period, using
  repository and supplied Slack evidence through 5 October. This refresh corrects
  the submission rename/acknowledgements status and a broken test-backlog link.
- The 6–19 October report now covers the full period, including implementation,
  validation, CPS review and downstream work after the previous 9 October cutoff.
- The 19–30 October report replaces the initially assumed 20 October–2 November
  window, following David's request supplied by Nicolas. It is an interim draft
  as of 29 October; no work after that date is counted as completed.

The reports combine dated Git history, published issues and assessments, retained
validation results, recorded weekly notes and workstream discussions reviewed with
Nicolas. Completed work is distinguished from proposals, open decisions and
incomplete integration.
Nicolas's implementation work is reconstructed primarily from the repository,
retained validation results and the design decisions made during the work. The
8 October generated meeting summary is supplementary and does not replace that
evidence. Historical source checks retain their original dates below. The
27 October review separately checked CPS PR #1268, ARC PR #53 and issues #13,
#40 and #41 on GitHub. Recorded tests were reviewed, not rerun; no current CI or
complete multi-era validation result is inferred from them.

## 29 October follow-up

Nicolas supplied David Rosales Parral's Slack request to prepare a report for
19–30 October and his correction of a follow-up slot from the 26th to the 16th.
The surrounding sequence (the next week's holiday, then PubSub, then this slot)
places that corrected date on 16 November. This records the supplied scheduling
exchange; no calendar invitation or additional message was sent. The new report
uses David's requested window. Its 19 October boundary overlaps the prior report;
that day's implementation is identified as the starting checkpoint, not a second
delivery.

Live GitHub verification on 29 October confirms that
[CPS PR #1268](https://github.com/cardano-foundation/CIPs/pull/1268) was merged at
`2026-10-27T16:59:53Z` (18:59:53 in Cyprus), merge commit
[`9cebacf9`](https://github.com/cardano-foundation/CIPs/commit/9cebacf9dab2030dd0322219577cd2b24ed6e4f0).
The earlier 27 October read below occurred before the merge. The new report now
records CPS publication and carries solution-design work forward into the CIP.

The final 27 October prototype commit
[`1a903ab00`](https://github.com/nhenin/cardano-ledger-specs/commit/1a903ab0040f4f3723d9343a323a75b44ded5245)
was missing from the earlier snapshot. The local Ledger checkout is clean at that
commit, matching its recorded fork tracking ref; the development chat records its
push. It separates UTxO storage domains and pure deposit operations, introduces
provisional V2/V1 formula parity and extracts `Cardano.Ledger.TxOut` while keeping
Core exports compatible. The prototype's creation path still uses V1; migration and
parameter-driven version selection remain unimplemented.

The verification record reports 145 targeted checks after consolidating the
storage/deposit changes, followed by six successful build targets and 134 checks
(127 goldens plus seven collateral properties, 100 cases each) after TxOut
extraction. The full 209-business-check and full State Types suites were not rerun
for this final checkpoint. This supersedes the earlier statement that the changes
were still uncommitted and their combined build was pending.

A bounded review of the local Ledger history and verification record, plus the
latest turns of “Réévaluer la situation” and “Rédiger un message Slack à Pi”, found
no further 28–29 October implementation or validation results in those sources.
Slack was not independently searched again for this follow-up; the source for
David's new instructions is Nicolas's supplied transcript. Earlier chat and Slack
coverage retains its 27 October cutoff below.

## 27 October evidence review

### Source coverage and method

The update combines the relevant accessible project chats, local Ledger commits
and verification records, live GitHub reads and direct read-only inspection of
Slack. The selected chats cover prototype development, CPS review, refund/fee
accounting, stakeholder discussions and presentation preparation. Older project
chats were checked for continuity with the previously reconstructed reports.
This is a review of relevant sources, not an assertion that every historical chat,
archived conversation or Slack message has been exhaustively retrieved.

Slack review covered all 13 results in the workstream channel for 9–27 October,
all four pages of a bounded minUTxO search, the Pi/Simon/Philip group conversation
and relevant Will messages and threads. A focused calculation search and the
latest Will conversation supplied additional context. The previous 9 October
Slack evidence remains the source for the earlier part of the period. A private
evidence index is retained in `AI/docs/slack-stream-2026-10-27.md`, outside Git.
Personal remarks and restricted security-channel details are not report content.

Chat evidence was taken from user messages, final work summaries and retained
command results. Draft communications were not counted as sent without an actual
Slack message or GitHub comment. Presentation files and sharing establish
preparation and circulation, not delivery of the talk. The Dingo design draft
remains unconfirmed in the reviewed sources; silence is not evidence of delay.

### CPS publication and reporting corrections

- [ARC PR #53](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/53)
  is merged (`25472521b5f7f2373baf142cf9d19ede3e457c60`). It aligned the stream's
  CPS metadata and `CPS-0037` directory with the submission and published the
  previous report update. The current root checkout still contains older local
  working copies; those are not evidence that the upstream alignment is pending.
- [CPS PR #1268](https://github.com/cardano-foundation/CIPs/pull/1268) was open and
  unmerged on 27 October, at `d9361ed0b00931023b342cace3dc88bead51b2b5`.
  The [12 October review](https://github.com/cardano-foundation/CIPs/pull/1268#pullrequestreview-5494942709)
  requested attribution and earlier-alternative follow-up before approval/Last Check;
  [issue #1295](https://github.com/cardano-foundation/CIPs/issues/1295) tracks the
  associated history for the forthcoming CIP.
- The [16 October RFP comment](https://github.com/cardano-foundation/CIPs/pull/1268#issuecomment-6220997893)
  and Nicolas's [19 October response](https://github.com/cardano-foundation/CIPs/pull/1268#issuecomment-6261452304)
  are published. GitHub's comment API dates the latter to
  `2026-10-19T06:50:16Z`; it is not merely a chat draft. No causal connection between
  the RFP and the preceding stakeholder discussions has been established.
- Issues #13, #40 and #41 were open when read. The old official-repository links
  to #84 and #85 returned 404; the refreshed reports use existing goal issues and
  local prototype backlog files instead. Issue-body progress text can lag the
  implementation and does not override dated commit/test evidence.

### Ledger implementation and validation

The primary local record is
`cardano-ledger/docs/dijkstra-deposit-store-verification.md`, read together with
the corresponding commit messages and retained execution results.

| Date | Evidence and scope |
| --- | --- |
| 9 October | [Declaration enforcement](https://github.com/nhenin/cardano-ledger-specs/commit/e10164c57ff90fb0d668cbef1eceda7b07b68b32), extending the earlier nine-check checkpoint. |
| 13 October | [Persistent state and accounting](https://github.com/nhenin/cardano-ledger-specs/commit/995ed4a4712a0c3db8b2cd7baae0a881970eb5a0): initial run 62 passing checks and 174 intentional placeholders; 125 golden checks also passed. |
| 15–16 October | [Leios rebase](https://github.com/nhenin/cardano-ledger-specs/commit/e5da0be244308c217a9b0eecf221c797f4176f44): 68 implemented checks passed. A subsequent independent upstream comparison reproduced the same 27 broader failures; see qualification below. |
| 19 October | [Exact declarations](https://github.com/nhenin/cardano-ledger-specs/commit/b72b2bbc80570dc84c30b59b2498ceb80f6da5b7) and [balance](https://github.com/nhenin/cardano-ledger-specs/commit/1d2aa2e3ff62cd7e0fd60c403811287f98335773): 139 passing / 117 placeholders at the committed checkpoint; 144 passing / 111 placeholders after local attribution work that evening. |
| 20 October | [Settlement/authority](https://github.com/nhenin/cardano-ledger-specs/commit/ade9da28f33f3fe74dbeb5c281728dfc96ab2b33), [minimum coin](https://github.com/nhenin/cardano-ledger-specs/commit/a384c4333f8b276968702face92bb5b608f1425b) and [collateral](https://github.com/nhenin/cardano-ledger-specs/commit/75403c2a23b674416ef9a29549d4a6c795dc7242): 178 transaction checks and eight focused collateral contracts passed. |
| 23 October | [Ledger effects and accepted-size preservation](https://github.com/nhenin/cardano-ledger-specs/commit/88a68589d7385a159551241171efa33851f1f782): all 206 current business checks passed; three decoder regressions and five transaction round-trip properties passed. |
| 26 October | [Historical output storage](https://github.com/nhenin/cardano-ledger-specs/commit/04ae12ff5bc0a711e2857a43f5721bba1b6559e6): 209 business checks, 14 metadata/size properties and 127 goldens passed, plus bounded state and compatibility checks. |
| 27 October | [Generic stored outputs](https://github.com/nhenin/cardano-ledger-specs/commit/52d2c835e8f5a04c384b69dd651183bd6972f0df): 165 targeted checks plus a 100-case bounded UTxOState property passed. [Accessor rename](https://github.com/nhenin/cardano-ledger-specs/commit/f3533831bbab8c23b2ac7bd9f59bfb5db6f21dbe) compiled. |

The independent Leios comparison is recorded in the 16 October turn
`01a14391-df42-71e0-9e47-c0971d96c1a4` of “Réévaluer la situation”. Successful reads
of `pristine-regressions.log` and
`/private/tmp/leios-upstream-verification-20261016/comparison.json` report 265
examples, 238 passes and 27 failures on each branch, seed `739231514`, with identical
failure paths and ordering. This later run supersedes the earlier verification
note saying pristine upstream had not been executed. It does not make that suite
green.

At this refresh, the local Ledger HEAD is `f3533831b`, with additional uncommitted
module/deposit-calculation changes. Their combined build and fresh metadata
validation are pending. The 209-business-test result belongs to the 26 October
checkpoint; the later refactor has targeted coverage only. The full State Types
run was interrupted; only the bounded UTxOState property is counted as completed.
Pricing, staking, voting, some inherited collateral cases, complete Plutus
compatibility, migration policy and performance sign-off remain outside the
completed active suite. Consolidating or removing placeholders is not counted as
implementing those deferred requirements. A provisional second formula version
does not establish adoption of Pi's suggested alternative pricing rule.

### Stakeholder and downstream evidence

- [9 October, Will](https://input-output-rnd.slack.com/archives/D06FTPHMSNN/p1791551617427229):
  a fresh multi-repository workspace builds implicit and store-backed transactions
  and reaches the Ledger's then-intentional errors. This is partial integration,
  not successful final ledger acceptance.
- [19 October, Will](https://input-output-rnd.slack.com/archives/D06FTPHMSNN/p1792423176903689):
  the refund/fee example exposes the strict settlement-output constraint. The
  reviewed implementation's conservation equation alone does not resolve this
  policy choice; no fix is inferred from later tests passing the existing rule.
- [21 October, prototype explanation](https://input-output-rnd.slack.com/archives/C0CATC4PQ59/p1792590385758709),
  [22 October, Pi's formula feedback](https://input-output-rnd.slack.com/archives/C0CATC4PQ59/p1792653683972129)
  and [Nicolas's declaration response](https://input-output-rnd.slack.com/archives/C0CATC4PQ59/p1792656865480539):
  verified directly in Slack, including the distinction between numeric amounts
  and meaningful delegation/settlement choices.
- [22 October, Will relays Polina's formula-only alternative](https://input-output-rnd.slack.com/archives/D06FTPHMSNN/p1792682690827409)
  and [23–26 October, ADA-payment discussion](https://input-output-rnd.slack.com/archives/D06FTPHMSNN/p1792761312903689):
  unresolved design comparison, not an agreed abandonment or adoption of an architecture.
- [22 October, Pi's collateral workflow](https://input-output-rnd.slack.com/archives/C0CATC4PQ59/p1792654309751309):
  explicitly outside the current deposit scope.
- [22 October, Philip's response](https://input-output-rnd.slack.com/archives/C0CATC4PQ59/p1792658436310259):
  availability for advice confirmed; no completed technical review claimed.
- [22 October, presentation PDFs shared](https://input-output-rnd.slack.com/archives/D06FTPHMSNN/p1792661836760729):
  corroborates the local deck/speaker-note work and Google Slides update. No talk
  delivery evidence was established.
- [27 October, Nicolas relays Nicolas Biri's Plutus feedback](https://input-output-rnd.slack.com/archives/D06FTPHMSNN/p1793106526547019):
  total value, application assets and deposit should be available. Will's ensuing
  reply says he is still considering how to implement it; the report preserves
  that distinction between stakeholder feedback and a completed design.

## Historical evidence snapshots

The following sections describe the evidence available at their stated dates.
Their references to a stale local CPS, uncommitted declaration implementation or
pending work are historical and are superseded where the 27 October review above
records later delivery.

## Format references

- [PubSub bi-weekly report template](https://github.com/input-output-hk/pubsub/blob/main/biweekly-reports/TEMPLATE.md)
- [PubSub report examples](https://github.com/input-output-hk/pubsub/tree/main/biweekly-reports)
- [PubSub epic example](https://github.com/input-output-hk/pubsub/issues/46)

## Evidence references

- [Backlog](backlog/README.md) and [GitHub milestones](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestones): milestone scope, issue status and completion dates, checked on 25 September.
- [ARC PR #38](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/38): focused CPS publication.
- [ARC PR #44](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/44): three-level Ledger exploration.
- [ARC PR #45](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/45): CPS review and withdrawal of the historical stock chart.
- [CIPs PR #1268](https://github.com/cardano-foundation/CIPs/pull/1268): official CPS submission on 11 September. Nicolas confirmed CPS-0037 numbering and ongoing review on 22 September; numbering does not establish acceptance.
- [Direct output split](https://github.com/nhenin/cardano-ledger-specs/commit/3843077adc0ecf1d4ce92d92df00a0fe1586480b), dated 27 August, and [forging checkpoint](https://github.com/nhenin/cardano-ledger-specs/commit/a0d67967bffb0667bf9665db0e74422dc70bba10), dated 3 September: early implementation and accounting-interface experiments.
- [Output-allocation checkpoint](https://github.com/nhenin/cardano-ledger-specs/commit/3c0614f26767ebe222d350b1b3f5f8688169175d), dated 21 September: separate storage, migration and initial allocation. The implementation attempt was subsequently parked and a fresh branch started from Ledger master; its findings remain useful.
- [Will's 23 September assessment](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41#issuecomment-5796435821) and [annotated branch](https://github.com/willjgould/cardano-ledger/commit/29586b32e2c4d663a2e4374410a808a07bcff521): effects on ordinary balancing, validation and builders. An assessment and code annotations do not establish a working netting implementation.
- [24 September weekly notes](https://docs.google.com/document/d/1CnqVT571qKzxJBVOdAAxCWM6QQc97C4SzBKseQVY8hQ/edit?tab=t.lfddgi8lle8): Quick notes and Full notes covering deposit accounting, byte-based pricing, transaction-body and legacy interfaces, and the Dingo and Polina follow-ups.

## 9 October repository review

- [5 October CPS revision](https://github.com/nhenin/CIPs/commit/d9361ed0b00931023b342cace3dc88bead51b2b5): inspected in the official-submission checkout. The supplied Slack evidence identifies the added parameter-change accounting section and separately confirms the [posted 5 October reply](https://github.com/cardano-foundation/CIPs/pull/1268#issuecomment-5990405952). The root `CPS-????/README.md` remains behind the submission fork and is not evidence of the current PR text; reconciliation remains a TODO.
- Ledger commits from 28–29 September adapt Shelley through Conway to explicit output variants. Their commit records identify the individual build and test results, including pending cases and the incomplete Conway full-suite run at its checkpoint.
- [Dijkstra output implementation, 2 October](https://github.com/nhenin/cardano-ledger-specs/commit/39019ba5624d2429c210003f7e16d827fee19c88): storage, codecs and remaining consumers. The validation record distinguishes a passing full build and 24 passing suites from six CDDL failures and interrupted generic-Ledger/conformance runs.
- [Dijkstra output CDDL, 2 October](https://github.com/nhenin/cardano-ledger-specs/commit/00ede97526f48f91908a24c557f5e50c0da58300): eight targeted checks passed, resolving the six earlier failures; `application_assets` names the value grammar.
- [Transaction interfaces, 5 October](https://github.com/nhenin/cardano-ledger-specs/commit/ee56dc0467ba7dcd467a2b73166f1c7a270f9bba) and [positive amounts and settlement](https://github.com/nhenin/cardano-ledger-specs/commit/b5583790b8d22d883042a5bc3348d5a54de7f37d): interfaces and codecs precede Store state and ledger enforcement. The latter checkpoint records 109 passing focused examples; the retained API doctest log records 25 passing examples.
- [Accounting and lifecycle rules, 6 October](https://github.com/nhenin/cardano-ledger-specs/commit/2c1f6b369c395f431b273149120992cddc93c4bd): baseline for the current period. Local commit `7f0b5e5afbdf96e636ca2becb5292294c092ec7e`, dated 8 October, adds 21 domain-rule modules and 170 intentional placeholders. It is ahead of the locally recorded fork tracking ref; no live publication check was made.
- Current uncommitted Ledger code implements DS-TX-009 and separates TopTx/SubTx declaration types. The rule document and test registry describe 172 checks, with nine implemented and 163 intentional placeholders. Retained focused logs record nine examples passing, including a 100-sample property. Later fixture/naming changes compile; broader regression results are attributed to their earlier checkpoints.

Recorded validation was reviewed, not rerun for the report update. Relevant local
logs include `arc-subtx-positive-store-tests.log`, `cardano-api-doctest-verified.log`,
`arc-declaration-fixture-tests.log`, `arc-qualified-declarations-inventory.log` and
the declaration codec/round-trip logs in `/private/tmp`. The prototype's working
rule document is `cardano-ledger/docs/dijkstra-deposit-store-rules.md`.

## 8 October 2026 weekly notes

Source: user-supplied PDF, `ARC-MinUtxo Weekly - 2026_10_08 17_00 EEST - Notes by Gemini.pdf`,
received on 9 October. The two-page export contains Quick notes; substantive
meeting content is on page 1. It does not include the Full notes or a usable
link to their document.

Nicolas assessed this generated summary as a poor account of his work. It is used
only as supplementary context for team follow-ups, notably Agda terminology and
the transaction-reading comparison. His implementation and domain-model progress
are grounded in repository evidence and the actual design discussions instead.
Nicolas confirmed that “Agnes” and “AlchemyOS” mean **Agda** and **Ogmios**.

## 9 October Slack evidence update

The user supplied `AI/docs/slack-stream-2026-10-09.md` and explicitly requested its
reporting instructions be followed. It records dated CPS review, prototype,
netting and downstream-integration discussions. The reports retain the goal order
#13, #40 and #41 and distinguish published interfaces from local implementation
in progress.

New evidence confirms the posted 5 October CPS reply, the 5 October interface
announcement and handoff to Will, and the 6–8 October accounting questions and
downstream findings. The 6 October CI result is attributed to the historical
interface version reported in Slack, not the current working tree. The prior
claim that the 24 September discussion settled a replacement pricing policy has
been removed: the prototype's byte-based formula and the discussion of builder
estimates are kept distinct.

The Dingo draft has no delivery evidence in the supplied material. Nicolas changed
the target to 15 October in this conversation; both reports retain that target and
a TODO to confirm the draft's status and link. The separate TODO for the stale
local CPS remains unresolved. No missing status is inferred from silence.
