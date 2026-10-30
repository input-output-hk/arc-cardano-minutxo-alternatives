# Validate application evidence for the CPS use cases

**Status:** Todo · **Parent:** [Architecture Decision](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14).

**Outcome:** reproducible application examples for evaluating candidate mechanisms
against the published CPS. This is the empirical work separated from completed
[use-case documentation](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/11).

## Completion criteria

- [ ] Identify a named high-fan-out distribution flow with public evidence.
- [ ] Identify a named token, CIP-68 or script-state flow and its output requirements.
- [ ] Document a stranded or unsolicited-output example; distinguish observation
  from an economic scenario.
- [ ] For each example, publish the transaction/output shape or reproducible builder
  trace, sources, protocol parameters and assumptions.
- [ ] Compare intended transfers, fees, backing required and recoverable ADA without
  double-counting ADA that serves multiple roles; show the current workaround.
- [ ] State which application logic each candidate removes, retains or shifts to
  another participant. Feed the results into #17, with uncertainties explicit.

A CIP reference alone does not prove a deployed application's behavior. Do not
present hypothetical parameter changes as observed mainnet incidents.
