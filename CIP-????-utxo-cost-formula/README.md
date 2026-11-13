---
CIP: "?"
Title: UTxO Storage Cost Formula
Category: Ledger
Status: Proposed
Authors:
    - Nicolas Henin <nicolas.henin@iohk.io>
    - Will Gould <will.gould@iohk.io>
    - Polina Vinogradova <polina.vinogradova@iohk.io>
Implementors: []
Discussions:
    - "CPS review: https://github.com/cardano-foundation/CIPs/pull/1268"
Solution To:
    - "CPS-0037: https://github.com/cardano-foundation/CIPs/tree/master/CPS-0037"
Created: 2026-11-10
License: CC-BY-4.0
---

## 1. Abstract

On Cardano, every output must contain a certain minimum amount of ADA. This 
minimum is commonly called minutxo, and its calculation is currently based on 
the output.

The current minutxo formula is challenging to calculate and has been explicitly 
referenced as a pain point by community members; specifically, the 
recursive nature of the calculation. This CIP seeks to change the formula to 
simplify calculation.

## 2. Motivation: Why is this CIP necessary?

[CPS-0037](../CPS-0037/README.md) describes the problem in full, but here, we'll 
describe the core of the issue.

The current formula is:

`coinsPerUTxOByte * (160 + serializedOutputBytes)`

To calculate `serializedOutputBytes`, we serialise the output. Note that the 
output itself contains the total ADA value.

Let's assume an output with `n` ADA, where `n < minutxo` for that 
output. We serialise the output and plug it into the formula to get:

`coinsPerUTxOByte * (160 + so1) == result1`

So we add `result1 - n` to the ADA value of the output. We must now calculate a 
new `serializedOutputBytes`, since the ADA value has changed, meaning the size 
of the serialised output may differ. If it does differ, we must now recalculate 
minutxo.

This is the primary problem that we seek to simplify through this reformulation.

Additionally, doing so while minimising the dependence upon serialisation for 
simplicity's sake is ideal.

## 3. Specification

### 3.1 Formula

```
coinsPerUTxOByte × (250 + 74 × numberOfNativeAssets
                    + serializedDatumBytes
                    + serializedReferenceScriptBytes)
```

See the following for some examples, with `coinsPerUTxOByte = 4310` as it 
currently is on mainnet.

| Output measurements | Pricing units | Required lovelace | Current formula |
| --- | ---: | ---: | ---: |
| No native assets, datum or script | `250` | 1,077,500 | 969,750 |
| One native asset, no datum or script | `250 + 74` | 1,396,440 | 1,120,600–1,297,310 |
| Two native assets, no datum or script | `250 + 74 * 2` | 1,715,380 | 1,133,530–1,616,250 |
| Ten native assets, no datum or script | `250 + 74 * 10` | 4,266,900 | 1,236,970–4,167,770 |
| One native asset and a 32-byte datum hash | `250 + 74 + 32` | 1,534,360 | 1,267,140–1,443,850 |
| One native asset, a 100-byte serialised inline datum and a 200-byte serialised reference script | `250 + 74 + 100 + 200` | 2,689,440 | 2,491,180–2,667,890 |

### 3.2 Formula inputs

- `coinsPerUTxOByte`: the protocol parameter in effect for the transaction, in
  lovelace per byte.
- `numberOfNativeAssets`: the number of distinct pairs of policy ID and asset 
  name in the output, excluding ADA.
- `serializedDatumBytes`: the byte length of the datum hash or serialised
  inline datum; zero if absent.
- `serializedReferenceScriptBytes`: the byte length of the serialised
  reference script; zero if absent.

Datum and reference script lengths are measured on the bytes as they appear in 
the transaction, which is how the ledger stores and hashes them.

### 3.3 Enforcement and compatibility

The new formula will be enforced by the ledger for new outputs. Existing outputs 
are entirely unaffected.

### 3.4 Versioning

Any change to the formula's constants or inputs requires a new CIP that
supersedes this one.

## 4. Rationale: How does this CIP achieve its goals?

We achieve the primary goal of avoiding recursive calculation by omitting ADA 
quantity from the formula.

We achieve the secondary goal of decreasing the dependence upon serialisation
by omitting most of the output fields.

We achieve both of these in balance with keeping overestimates close "enough" 
to the current formula, and while keeping underestimates to a minimum.

The constant 250 consists of the existing 160, plus 90, approximating the 
additional components of a near-worst-case output. The constant 74 is made up 
of: 
- 30 for the policy ID (a 28-byte hash and a 2-byte header)
- 1 for the header of that policy's asset map
- 34 for the asset name (32 bytes and a 2-byte header)
- 9 for the quantity (8 bytes and a 1-byte header)

We tested this against the 229 million outputs created on mainnet from the
Babbage hard fork, which introduced the current formula, to 28 October 2026.
Each output is compared with what the current formula required:

| Formula (* `coinsPerUTxOByte`) | Outputs below the current requirement | Median excess | 95th-percentile excess | Mean requirement | Largest shortfall |
| --- | ---: | ---: | ---: | ---: | ---: |
| `160 + serializedOutputBytes` (current) | – | – | – | 1.49 ADA | – |
| `250 + 74 * numberOfNativeAssets + serializedDatumBytes + serializedReferenceScriptBytes` (this CIP) | 6,756 (0.003%) | 13.7% | 61.6% | 2.21 ADA | 2.36 ADA |
| `175 + serializedAddressFieldBytes + 12 * numberOfNativeAssets + 30 * numberOfMintingPolicies + totalAssetNameBytes + serializedDatumFieldBytes + serializedReferenceScriptFieldBytes` | 9,422 (0.004%) | 4.0% | 12.8% | 1.64 ADA | 3.00 ADA |
| `250 + 74 * numberOfNativeAssets + serializedDatumBytes` | 21,013 (0.009%) | 13.7% | 61.6% | 2.21 ADA | 69.33 ADA |
| `160 + serializedOutputBytes - serializedAdaAmountBytes + 9` | 0 | 1.5% | 2.0% | 1.51 ADA | none |

Method, full results and reproduction: [historical backtest](https://github.com/willjgould/cardano-minutxo-integration/blob/9b5a105905611ee8d56c0fbc483eb7e40f14df98/docs/minutxo-calibration/history-formulas.md).

### 4.1 Alternative formulae considered

| Alternative | Formula | Trade-off |
| --- | --- | --- |
| Asset and policy counts with address, asset-name, datum and script sizes | `coinsPerUTxOByte × (175 + serializedAddressFieldBytes + 12 × numberOfNativeAssets + 30 × numberOfMintingPolicies + totalAssetNameBytes + serializedDatumFieldBytes + serializedReferenceScriptFieldBytes)` | Close to the current formula results, but still a large amount of serialisation dependency |
| Token count and datum size only | `coinsPerUTxOByte × (250 + 74 × numberOfNativeAssets + serializedDatumBytes)` | Less serialisation dependency, but underestimates too much |
| Byte-based formula with a fixed ADA encoding allowance | `coinsPerUTxOByte × (160 + serializedOutputBytes - serializedAdaAmountBytes + 9)` | Very close to the current formula, but still dependent on serialising the whole output |

### 4.2 Alternative implementation considered

The same benefits could be obtained by simply disseminating one of the 
alternatives, which never underestimates, throughout tooling only, thus leaving 
the ledger-enforced formula as it is today. This would give users the choice, 
if they so desire, to optimise their minutxos by getting closer to the 
current formula than the overestimating function, while providing them with the 
means to more easily calculate a valid minutxo.

This alternative would require proving that any selected formula never 
underestimates.

## 5. Path to Active

### 5.1 Acceptance Criteria

- [ ] The specified minimum-ADA formula is implemented and activated on Cardano 
mainnet.

### 5.2 Implementation Plan

Implementation requires updating the ledger specification and minimum-ADA 
validation to use the new formula, and updating transaction-building tools to 
calculate the same requirement.

The changes must be implemented, tested and included in a node release. 
Activation requires a hard fork.

## 6. References

- [CPS-0037: application and transaction friction in minUTxO implementation](../CPS-0037/README.md)
- [CIP-0055: Protocol Parameters (Babbage Era)](https://github.com/cardano-foundation/CIPs/tree/master/CIP-0055), which defines the current formula

## 7. Copyright

This CIP is licensed under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode).
