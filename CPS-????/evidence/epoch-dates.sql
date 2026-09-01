\set ON_ERROR_STOP on

COPY (
  SELECT
    epoch_no,
    min(time) AS start_time,
    max(time) AS end_time
  FROM block
  WHERE epoch_no BETWEEN 0 AND 648
  GROUP BY epoch_no
  ORDER BY epoch_no
) TO STDOUT WITH (FORMAT csv, HEADER true);
