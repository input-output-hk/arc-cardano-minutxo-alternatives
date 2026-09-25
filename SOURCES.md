# Sources and reconstruction method

## Source repository

- Repository: [`input-output-hk/arc-cardano-minutxo-alternatives`](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives)
- Report update prepared: 25 September 2026
- Evidence through 21 September for local Ledger implementation and 24 September
  for workstream discussions and weekly-meeting outcomes

The reports combine dated Git history, published issues and assessments, retained
validation results, and workstream discussions reviewed with Nicolas. Completed
work is distinguished from proposals, open decisions and incomplete integration.
The 22 September–5 October report is an interim draft as of 25 September.

## Format references

- [PubSub bi-weekly report template](https://github.com/input-output-hk/pubsub/blob/main/biweekly-reports/TEMPLATE.md)
- [PubSub report examples](https://github.com/input-output-hk/pubsub/tree/main/biweekly-reports)
- [PubSub epic example](https://github.com/input-output-hk/pubsub/issues/46)

## Published evidence

- [ARC PR #38](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/38): focused CPS publication.
- [ARC PR #44](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/44): three-level Ledger exploration.
- [ARC PR #45](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/45): CPS review and withdrawal of the historical stock chart.
- [CIPs PR #1268](https://github.com/cardano-foundation/CIPs/pull/1268): official CPS submission on 11 September. Nicolas confirmed CPS-0037 numbering and ongoing review on 22 September; numbering does not establish acceptance.
- [Direct output split](https://github.com/nhenin/cardano-ledger/commit/3843077adc0ecf1d4ce92d92df00a0fe1586480b), dated 27 August, and [forging checkpoint](https://github.com/nhenin/cardano-ledger/commit/a0d67967bffb0667bf9665db0e74422dc70bba10), dated 3 September: early implementation and accounting-interface experiments.
- [Output-allocation checkpoint](https://github.com/nhenin/cardano-ledger/commit/3c0614f26767ebe222d350b1b3f5f8688169175d), dated 21 September: separate storage, migration and initial allocation. The implementation attempt was subsequently parked and a fresh branch started from Ledger master; its findings remain useful.
- [Will's 23 September assessment](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41#issuecomment-5796435821) and [annotated branch](https://github.com/willjgould/cardano-ledger/commit/29586b32e2c4d663a2e4374410a808a07bcff521): effects on ordinary balancing, validation and builders. An assessment and code annotations do not establish a working netting implementation.

## Discussion and meeting evidence

Workstream discussions supplied the context for the split/netting work allocation,
developer feedback and open accounting questions. Nicolas provided the outcomes of
the 24 September weekly meeting: the broad impact map, the fixed-point requirement
for precise release accounting in the proposed dust account, and Polina's ownership
of nested-transaction exploration. These are recorded meeting outcomes, not claims
that a final mechanism or complete implementation has been approved.

Nicolas also reported a discussion with the Dingo node team. The professional
calendar confirms a meeting with Chris Gianelloni of Blink Labs on 24 September.
No specific technical conclusion is inferred from the calendar entry.

The current report draws on earlier experimental attempts without counting them as
new implementation work during 22–25 September. Git preserves several successive
variants; the linked checkpoints identify concrete evidence without claiming that
they uniquely define the boundaries between attempts.

## Validation and limitations

- Historical stock reconstruction omitted genesis outputs while including later
  spends. Its absolute-count claim was withdrawn on 7 September. Correction and
  independent validation remain open; no corrected count is established.
- The deterministic 1-in-500 DB-Sync sample still requires independent reproduction
  and ledger-native era-sizing review.
- Retained local results recorded 402 passing examples across seven focused groups.
  Compatibility and standard Dijkstra/API suites remained blocked at compilation;
  the published checkpoint's CI was not green. Focused checks do not establish
  integrated readiness. No Ledger tests were rerun for this documentation update.
- Internal working notes and discussions provide provenance, not public CPS/CIP
  citations. Statements about reviews and decisions retain their recorded dates.
- The ARC workstream repository is public. Official CPS submission and Ledger
  integration remain separate deliverables.
