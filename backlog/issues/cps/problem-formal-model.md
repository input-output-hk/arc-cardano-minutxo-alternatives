# 02 — Define the min-UTxO problem and formal model

## Outcome

A solution-neutral statement of the security objective, capacity lifecycle, and
application-facing problem.

## Work included

- [ ] Define the persistent-state security objective.
- [ ] Define entry-count and serialized-size capacity dimensions.
- [ ] Explain the current scalar projection `U(t)=160N(t)+S(t)`.
- [ ] Define transaction-level capacity allocation and release.
- [ ] Distinguish reachable ledger states from relaxed analytical bounds.
- [ ] Describe representation, responsibility, and lifecycle mismatches.
- [ ] Separate root causes from observable application consequences.

## Acceptance criteria

- The model is internally consistent and reviewed by Ledger/domain experts.
- The CPS does not imply that persistent state should be free or unbounded.
- No candidate settlement or reserve design is presented as part of the problem definition.
