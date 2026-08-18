# Sources and reconstruction method

## Source repository

- Repository: [`input-output-hk/arc-minutxo`](https://github.com/input-output-hk/arc-minutxo)
- Audited branches: `main` and `codex/cps-capacity-narrative`
- Confirmed Git history: eight commits from 28 July to 11 August 2026
- Latest confirmed checkpoint: [`c1bd76e`](https://github.com/input-output-hk/arc-minutxo/commit/c1bd76e51ecbf6bbfa53934fdd2789d227118fc3)
- Working-state cutoff: 17 August 2026

Primary evidence reviewed: the root README, CPS and CIP drafts, `NOTES.md`,
`PROJECT_MEMORY.md`, `HANDOFF.md`, the weekly report, DB-Sync methodology and outputs,
and Git history/working-tree state.

## External format references

- [PubSub bi-weekly report template](https://github.com/input-output-hk/pubsub/blob/main/biweekly-reports/TEMPLATE.md)
- [PubSub report examples](https://github.com/input-output-hk/pubsub/tree/main/biweekly-reports)
- [PubSub epic example](https://github.com/input-output-hk/pubsub/issues/46)

## Evidence labels

- **Confirmed** — present in committed Git history.
- **In progress** — present in the 17 August working tree or project memory but not
  in the latest confirmed commit.
- **Proposed** — inferred from recorded next actions, blockers, or acceptance needs.
- **Blocked** — requires a decision, external evidence, or independent review.

No historical intent is invented. The first report's next steps come from dated plans.
The second report is a live draft with a 17 August evidence cutoff.

## Known limitations

- Git history begins on 28 July 2026.
- Gitignored prototype and private Slack material were not independently inspected;
  their status comes from project memory and handoff notes.
- The deterministic 1-in-500 DB-Sync sample requires independent reproduction and
  ledger-native era-sizing review.
- The planning backlog is published in this private repository. Reports link directly
  to the corresponding GitHub issues; publication to the official repository remains separate.
