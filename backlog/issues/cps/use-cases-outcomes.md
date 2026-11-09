# Document CPS use cases and required outcomes

**Status:** Done · **Parent:** [Problem Definition](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/7).

## Delivered

[CPS-0037](https://github.com/cardano-foundation/CIPs/blob/master/CPS-0037/README.md),
merged through [PR #1268](https://github.com/cardano-foundation/CIPs/pull/1268) on
27 October 2026, documents seven use cases: minimally funded transitions, small
payments, sender-funded outputs, non-staking state, balancing, high-fan-out
distribution and successor-output top-ups.

- [x] Explain each scenario, the current workaround and the remaining friction.
- [x] Define testable, solution-neutral outcomes and explicit non-goals.
- [x] Distinguish funding friction from protocol impossibility.
- [x] Publish the use cases with the CPS references and review record.

## Scope split

This closes **documentation of the use cases**, not empirical validation of deployed
applications. The original requirements for named examples, verified transaction
shapes and quantitative assumptions move to [application evidence](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/56).
That task retains the high-fan-out, token/CIP-68/script-state and stranded/unsolicited
output investigations. Parameter-change examples remain scenarios unless observations
establish an actual occurrence.
