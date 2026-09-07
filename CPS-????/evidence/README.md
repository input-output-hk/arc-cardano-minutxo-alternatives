# Mainnet live-UTxO evidence

**Status: historical snapshot; absolute live counts require correction.** The live
stock figure has been removed from the active CPS. The original query, results, and
figure are retained here for investigation, not as validated ledger cardinalities.

The query reconstructs live stock by summing creations minus consumptions from epoch
0, without an initial stock. Its epoch filter excludes genesis creations, which
DB-Sync 13.7.2.1 records under a block with no epoch number, while later spending of
those outputs enters the consumption count. See the
[genesis insertion code](https://github.com/IntersectMBO/cardano-db-sync/blob/13.7.2.1/cardano-db-sync/src/Cardano/DbSync/Era/Byron/Genesis.hs#L93)
and [the historical query](./utxo-count-by-epoch.sql).

Before these absolute counts are reused, the reconstruction must account for the
initial state and ledger removals outside ordinary transactions, and agree with a
direct inventory of live outputs at the recorded chain point. No corrected count
has been established. A historical stock offset need not invalidate recent flow
totals or their difference, but those do not validate the absolute stock.

This dataset covers output counts. It does not measure application friction, builder
complexity, or the reasons outputs were created or consumed.

## Analysis boundary

- **Network:** Cardano mainnet
- **Last included epoch:** 648
- **Boundary block:** `786868fc343bc5d196e8cb03ead374365e368ce90d536d015772eb1d6788a7cb`
- **Block height:** 13,800,907
- **Absolute slot:** 195,004,781
- **Block time:** 2026-08-12 21:44:32 UTC
- **Historical `utxo_count_end` query result, awaiting correction:** 11,076,329

The DB-Sync environment was configured with
`ghcr.io/intersectmbo/cardano-db-sync:13.7.2.1` and the full insertion preset, so
historical `tx_in`, `tx_out`, `collateral_tx_in`, and `collateral_tx_out` rows were
retained. The immutable image digest and exact schema revision executed for the
original run were not recorded. No independent reproduction has yet been registered.
Those are provenance limits of this snapshot, not properties established by the
committed data.

## Counting method

For each epoch, the historical query counts:

- **created:** ordinary outputs from phase-2-valid transactions, plus collateral
  returns from phase-2-invalid transactions;
- **consumed:** ordinary inputs consumed by phase-2-valid transactions, plus
  collateral inputs consumed by phase-2-invalid transactions; and
- **`utxo_count_end`:** the cumulative sum of `created - consumed` from epoch 0,
  with the initial-state omission described above.

The query uses historical rows rather than a sample. That does not make its stock
reconstruction complete; the former description of the live count as exact is
withdrawn.

## Files

- [`utxo-count-by-epoch.sql`](./utxo-count-by-epoch.sql) is the historical query,
  frozen at epoch 648, whose stock calculation requires correction.
- [`utxo-count-by-epoch.csv`](./utxo-count-by-epoch.csv) is the committed query result.
- [`epoch-dates.sql`](./epoch-dates.sql) produces the first and last block time in
  each epoch.
- [`epoch-dates.csv`](./epoch-dates.csv) is the committed date result.
- [`chain-point.sql`](./chain-point.sql) selects the final block in epoch 648.
- [`chain-point.csv`](./chain-point.csv) is the committed chain-point result.
- [`build_live_utxo_evidence_svg.py`](./build_live_utxo_evidence_svg.py) regenerates
  [`../images/09-live-utxo-history.svg`](../images/09-live-utxo-history.svg) from the
  two CSV files using only the Python standard library.

## Reproducing the historical calculation

The following commands reproduce the original method, including its stock omission.
They are retained for diagnosis and do not constitute a corrected counting method.
Run them against a full-history mainnet DB-Sync PostgreSQL database:

```sh
cd 'CPS-????/evidence'
psql "$DBSYNC_DATABASE_URL" --no-psqlrc --quiet \
  --file=utxo-count-by-epoch.sql > utxo-count-by-epoch.csv
psql "$DBSYNC_DATABASE_URL" --no-psqlrc --quiet \
  --file=epoch-dates.sql > epoch-dates.csv
psql "$DBSYNC_DATABASE_URL" --no-psqlrc --quiet \
  --file=chain-point.sql > chain-point.csv
python3 build_live_utxo_evidence_svg.py
```

The published artifacts have these SHA-256 checksums:

```text
82bfc3da335cf9995e0fdd8493b04799b9eb9f766071fd79d6ade658d6422c93  09-live-utxo-history.svg
864e6b57c26b253502815e1cd22c53ffc72cb337228f3a4ddb0defbb053821e2  utxo-count-by-epoch.csv
98206ff68b3f103eae00d1f5e6f5081cdd522f8c0a018fb010967e27451e7a61  epoch-dates.csv
fa265bf938313fc4235fa666f687071d63d1f5425d0c97cca693963091ff893b  chain-point.csv
```

The generator is deterministic for the committed CSV inputs. Reproducing those
results verifies the historical calculation, not the correctness of the stock
estimate. Validation requires a corrected reconstruction and an independent inventory
at the same chain point.
