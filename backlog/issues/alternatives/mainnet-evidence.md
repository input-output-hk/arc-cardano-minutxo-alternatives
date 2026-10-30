# Validate mainnet UTxO evidence

**Status:** Deferred / Todo · **Parent:** [Architecture Decision](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14).

**Outcome:** a reproducible evidence package for quantitative comparisons. This work
was separated from the completed [CPS publication](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/7); it is not complete.

## Known limitation

The earlier historical live-UTxO reconstruction omitted the initial genesis stock
while counting spends of genesis outputs. Its chart was removed from the CPS.
A corrected historical series has not been established. Reconcile initial state
and any non-transaction removals with an independent inventory before using it.

## Completion criteria

- [ ] Reconstruct creation, consumption, net change and live UTxO counts by epoch.
- [ ] Reconcile the historical stock with a directly observed inventory.
- [ ] Estimate historical minimum ADA using the appropriate rules for each era.
- [ ] Validate Mary and Alonzo sizing against Ledger-native logic.
- [ ] Reproduce material estimates with an independent sample.
- [ ] Publish DB-Sync schema/version, frozen tip, SQL, scripts and assumptions.
- [ ] Separate exact results, estimates and proxies; quantify sampling and sizing
  uncertainty. Every headline comparison must follow from the published method.

The [Architecture Decision](https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/issues/14) must identify which conclusions require this
analysis and which remain justified without it. Do not imply that deferral validates
the removed figures or removes the need to substantiate future quantitative claims.
