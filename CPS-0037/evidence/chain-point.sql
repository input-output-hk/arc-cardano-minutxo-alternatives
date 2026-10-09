\set ON_ERROR_STOP on

COPY (
  SELECT
    encode(hash, 'hex') AS block_hash,
    epoch_no,
    block_no,
    slot_no,
    time AS block_time
  FROM block
  WHERE epoch_no = 648
  ORDER BY slot_no DESC
  LIMIT 1
) TO STDOUT WITH (FORMAT csv, HEADER true);
