# 03 — Produce and validate the mainnet evidence

## Outcome

A reproducible evidence package supporting the CPS quantitative claims.

## Work included

- [ ] Reconstruct UTxO creation, consumption, net change, and live counts by epoch.
- [ ] Estimate the era-specific historical minimum-ADA requirement.
- [ ] Validate Mary and Alonzo sizing against ledger-native logic.
- [ ] Reproduce material estimates with an independent sample.
- [ ] Publish the DB-Sync schema/version, frozen tip, SQL, scripts, and assumptions.
- [ ] Separate exact results, estimates, proxies, and their limitations.

## Acceptance criteria

- A reviewer can reproduce the analysis from a compatible DB-Sync database.
- Sampling and sizing uncertainty are documented independently.
- Headline CPS figures follow from the published method.
