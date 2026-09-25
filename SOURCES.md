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

- [Backlog](backlog/README.md) and [GitHub milestones](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/milestones): milestone scope, issue status and completion dates, checked on 25 September.
- [ARC PR #38](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/38): focused CPS publication.
- [ARC PR #44](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/44): three-level Ledger exploration.
- [ARC PR #45](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/45): CPS review and withdrawal of the historical stock chart.
- [CIPs PR #1268](https://github.com/cardano-foundation/CIPs/pull/1268): official CPS submission on 11 September. Nicolas confirmed CPS-0037 numbering and ongoing review on 22 September; numbering does not establish acceptance.
- [Direct output split](https://github.com/nhenin/cardano-ledger-specs/commit/3843077adc0ecf1d4ce92d92df00a0fe1586480b), dated 27 August, and [forging checkpoint](https://github.com/nhenin/cardano-ledger-specs/commit/a0d67967bffb0667bf9665db0e74422dc70bba10), dated 3 September: early implementation and accounting-interface experiments.
- [Output-allocation checkpoint](https://github.com/nhenin/cardano-ledger-specs/commit/3c0614f26767ebe222d350b1b3f5f8688169175d), dated 21 September: separate storage, migration and initial allocation. The implementation attempt was subsequently parked and a fresh branch started from Ledger master; its findings remain useful.
- [Will's 23 September assessment](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/41#issuecomment-5796435821) and [annotated branch](https://github.com/willjgould/cardano-ledger/commit/29586b32e2c4d663a2e4374410a808a07bcff521): effects on ordinary balancing, validation and builders. An assessment and code annotations do not establish a working netting implementation.
