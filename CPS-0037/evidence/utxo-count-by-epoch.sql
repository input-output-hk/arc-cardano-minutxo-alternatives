\set ON_ERROR_STOP on

-- Frozen evidence boundary: last complete epoch 648.

COPY (
  WITH ordinary_created AS (
    SELECT b.epoch_no, count(*)::bigint AS n
    FROM tx_out o
    JOIN tx t ON t.id = o.tx_id
    JOIN block b ON b.id = t.block_id
    WHERE t.valid_contract
      AND b.epoch_no BETWEEN 0 AND 648
    GROUP BY b.epoch_no
  ),
  collateral_return_created AS (
    -- Collateral return exists in ledger state only when phase-2 validation fails.
    SELECT b.epoch_no, count(*)::bigint AS n
    FROM collateral_tx_out o
    JOIN tx t ON t.id = o.tx_id
    JOIN block b ON b.id = t.block_id
    WHERE NOT t.valid_contract
      AND b.epoch_no BETWEEN 0 AND 648
    GROUP BY b.epoch_no
  ),
  ordinary_consumed AS (
    -- Ordinary inputs are consumed only by phase-2-valid transactions.
    SELECT b.epoch_no, count(*)::bigint AS n
    FROM tx_in i
    JOIN tx spending_tx ON spending_tx.id = i.tx_in_id
    JOIN block b ON b.id = spending_tx.block_id
    WHERE spending_tx.valid_contract
      AND b.epoch_no BETWEEN 0 AND 648
    GROUP BY b.epoch_no
  ),
  collateral_consumed AS (
    -- Collateral inputs are consumed only by phase-2-invalid transactions.
    SELECT b.epoch_no, count(*)::bigint AS n
    FROM collateral_tx_in i
    JOIN tx spending_tx ON spending_tx.id = i.tx_in_id
    JOIN block b ON b.id = spending_tx.block_id
    WHERE NOT spending_tx.valid_contract
      AND b.epoch_no BETWEEN 0 AND 648
    GROUP BY b.epoch_no
  ),
  epoch_range AS (
    SELECT generate_series(0, 648)::integer AS epoch_no
  ),
  flows AS (
    SELECT
      e.epoch_no,
      coalesce(oc.n, 0) + coalesce(cr.n, 0) AS created,
      coalesce(oi.n, 0) + coalesce(ci.n, 0) AS consumed,
      coalesce(oc.n, 0) AS ordinary_created,
      coalesce(cr.n, 0) AS collateral_return_created,
      coalesce(oi.n, 0) AS ordinary_consumed,
      coalesce(ci.n, 0) AS collateral_consumed
    FROM epoch_range e
    LEFT JOIN ordinary_created oc USING (epoch_no)
    LEFT JOIN collateral_return_created cr USING (epoch_no)
    LEFT JOIN ordinary_consumed oi USING (epoch_no)
    LEFT JOIN collateral_consumed ci USING (epoch_no)
  )
  SELECT
    epoch_no,
    created,
    consumed,
    created - consumed AS net_change,
    sum(created - consumed) OVER (ORDER BY epoch_no) AS utxo_count_end,
    ordinary_created,
    collateral_return_created,
    ordinary_consumed,
    collateral_consumed
  FROM flows
  ORDER BY epoch_no
) TO STDOUT WITH (FORMAT csv, HEADER true);
