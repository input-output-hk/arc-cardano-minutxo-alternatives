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
    - "CIP discussion: https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/63"
    - "CPS review: https://github.com/cardano-foundation/CIPs/pull/1268"
    - "Ledger prototype: https://github.com/nhenin/cardano-ledger-specs/pull/3"
Solution To:
    - "CPS-0037: https://github.com/cardano-foundation/CIPs/tree/master/CPS-0037"
Created: 2026-11-10
License: CC-BY-4.0
---

**Table of contents**

- [1. Abstract](#1-abstract)
- [2. Motivation: Why is this CIP necessary?](#2-motivation-why-is-this-cip-necessary)
  - [2.1 Remove the funding fixed point](#21-remove-the-funding-fixed-point)
  - [2.2 Simplify output measurement](#22-simplify-output-measurement)
  - [2.3 Preserve the minimum-ADA model](#23-preserve-the-minimum-ada-model)
- [3. Specification](#3-specification)
  - [3.1 Scope and formula inputs](#31-scope-and-formula-inputs)
  - [3.2 Formula V1](#32-formula-v1)
  - [3.3 Minimum-ADA admission](#33-minimum-ada-admission)
  - [3.4 Calculation examples](#34-calculation-examples)
  - [3.5 Formula versioning and activation](#35-formula-versioning-and-activation)
- [4. Rationale: How does this CIP achieve its goals?](#4-rationale-how-does-this-cip-achieve-its-goals)
  - [4.1 Predictable calculation and pricing precision](#41-predictable-calculation-and-pricing-precision)
  - [4.2 Resource protection](#42-resource-protection)
  - [4.3 Compatibility and CPS scope](#43-compatibility-and-cps-scope)
  - [4.4 Alternatives considered](#44-alternatives-considered)
  - [4.5 Author TODOs](#45-author-todos)
- [5. Path to Active](#5-path-to-active)
  - [5.1 Acceptance Criteria](#51-acceptance-criteria)
  - [5.2 Implementation Plan](#52-implementation-plan)
- [6. References](#6-references)
- [7. Copyright](#7-copyright)

## 1. Abstract

This CIP specifies a UTxO storage cost formula based on a fixed per-output allowance,
the number of distinct native assets, and datum and reference-script payload
lengths. The calculated amount does not depend on the output's ADA amount or
the complete serialized output size. This removes the funding fixed point and
the need for byte-perfect sizing of the whole output when calculating its cost.

The formula determines the minimum ADA required in a transaction output. That ADA
remains part of the output's ordinary value and follows its spending conditions.
This CIP changes how the requirement is calculated while preserving the
minimum-ADA model, existing output encodings and the rule that newly created
outputs must contain sufficient ADA.

## 2. Motivation: Why is this CIP necessary?

[CPS-0037](../CPS-0037/README.md) describes how the current minimum-ADA rule couples
output construction to the backing needed for live UTxO capacity. Two distinct
calculation problems affect wallets, builders and applications.

### 2.1 Remove the funding fixed point

The current minimum depends on the serialized output size, including the ADA
amount being chosen. Adding ADA can increase its encoded width and therefore
raise the minimum again. Builders must account for this dependency while funding
and balancing the output.

V1 makes the requirement independent of the ADA amount. Once the native assets,
datum and reference script are fixed, adjusting ADA does not change the result.
The [CPS fixed-point examples](../CPS-0037/README.md#a-circular-dependency-between-funding-and-cost)
explain the construction problem this removes.

### 2.2 Simplify output measurement

Even without a funding fixed point, calculating the exact serialized output size
couples resource pricing to encoding details. Builders must reproduce those
details or use a serializer as part of the calculation.

V1 uses fixed base and per-asset allowances, plus the lengths of datum and script
payloads. It avoids measuring the whole output. Exact payload lengths still
matter, and transaction fees retain their own size-dependent rules.

### 2.3 Preserve the minimum-ADA model

The minimum-ADA rule protects persistent UTxO capacity by requiring ADA to remain
in each live output. The same ADA can serve both this resource-protection role
and the application's intended payment.

A simpler calculation improves transaction construction within that model.
Applications continue to fund outputs and control them through their existing
spending conditions. Builders gain a requirement they can compute before choosing
the final ADA amount, without changing how output value is represented.

## 3. Specification

### 3.1 Scope and formula inputs

For a valid output `o`, let `p` be the effective `coinsPerUTxOByte` parameter,
expressed in lovelace per pricing unit. V1 defines the following non-negative
integer measurements:

| Symbol | Measurement |
| --- | --- |
| `N(o)` | The number of distinct native-asset identities in the accepted value: each policy-ID and asset-name pair counts once. Quantities do not enter the formula. ADA contributes zero. |
| `D(o)` | No datum: zero. Datum hash: the length of its digest in bytes. Inline datum: the length of its accepted CBOR-encoded payload, excluding the outer tag 24 and byte-string envelope. |
| `R(o)` | No reference script: zero. Native script: its original CBOR bytes. Plutus script: its original serialized script bytes. Count their lengths, excluding the script-language and enclosing output wrappers. |

These measurements use the output's accepted contents. Existing asset-map,
quantity, datum, script and output-validity rules continue to apply; the formula
does not authorize additional representations or values.

For `D(o)` and `R(o)`, implementations must use the accepted payload bytes rather
than substitute a newly encoded payload. Re-encoding equivalent data can change
its length. The output's address, ADA amount, asset quantities, asset-name lengths
and outer CBOR fields add no separate term.

[Output measurement implementation](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/UTxOs/Deposit/Formula.hs)

### 3.2 Formula V1

```math
F_{1,p}(o) = p\left(250 + 74N(o) + D(o) + R(o)\right)
```

`250` and `74` are fixed pricing allowances. They are not measurements of the
output's exact encoded size. Multiple assets sharing a policy ID and shorter
asset names receive no reduction in the per-asset allowance. Changing quantities
while preserving the set of identities leaves `N(o)` unchanged.

The result is an exact non-negative integer amount in lovelace. Calculation must
not overflow or round; implementations must use sufficient precision for the
accepted inputs. Conversion into any bounded ledger representation remains
subject to that representation's existing limits and must not truncate the result.

The following illustrative Haskell function expresses V1 using the measurement
and coin types of the reference implementation. It is adapted to return the
minimum required `Coin` directly:

```haskell
utxoCostV1 ::
  CoinPerByte ->
  NativeAssetCount ->
  DatumBytes ->
  ReferenceScriptBytes ->
  Coin
utxoCostV1
  (CoinPerByte (CompactCoin rate))
  (NativeAssetCount assetCount)
  (DatumBytes datumLength)
  (ReferenceScriptBytes scriptLength) =
    Coin $
      toInteger rate * toInteger (250 + 74 * assetCount + datumLength + scriptLength)
```

The measurement wrappers use `Natural`; the coin calculation uses `Integer`.
[Formula and measurement types](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/libs/cardano-ledger-core/src/Cardano/Ledger/State/Accounting/UTxOs/Deposit.hs)

### 3.3 Minimum-ADA admission

In the era activating V1, every newly created output must satisfy:

```math
\mathrm{coin}(o) \geq F_{1,p}(o).
```

This bound also applies to a collateral return under the era's collateral
validation rules. The output's entire ADA remains part of its ordinary value
and follows its spending conditions.

The formula returns a requirement even when `N(o)`, `D(o)` and `R(o)` are all zero:
`250 × p`. An output with no native assets or payloads must therefore contain at
least that much ADA. A zero rate produces a zero result; other output-validity
rules still apply.

The calculation changes no transaction or output data structures. Existing
encodings remain applicable, so this CIP requires no new CDDL production.

### 3.4 Calculation examples

The following examples use `p = 4310` as an explicit illustrative input, not a
parameter fixed by this CIP. The amount of ADA carried by the output does not
affect these calculations.

| Output measurements | Pricing units | Required lovelace |
| --- | ---: | ---: |
| No native assets, datum or script | `250` | 1,077,500 |
| One native-asset identity, no datum or script | `250 + 74` | 1,396,440 |
| Two native-asset identities, no datum or script | `250 + 74 × 2` | 1,715,380 |
| One native-asset identity and a 32-byte datum hash | `250 + 74 + 32` | 1,534,360 |
| One native-asset identity, 100-byte datum payload and 200-byte reference-script payload | `250 + 74 + 100 + 200` | 2,689,440 |

For example, an output with one native-asset identity and no payloads must contain
at least 1,396,440 lovelace at this rate. An output carrying 1,396,439 lovelace fails
the minimum-ADA check. Adding ADA up to or beyond the minimum leaves the calculated
requirement at 1,396,440 lovelace.

### 3.5 Formula versioning and activation

V1 is the initial formula specified by this CIP. Its activation changes output
admission rules and requires an agreed protocol transition. Earlier eras keep
their existing rules. The activating era uses its effective
`coinsPerUTxOByte` parameter; subsequent parameter changes affect the cost of newly
created outputs when they take effect.

Changing a formula's coefficients or measurement rules defines a different
version. Implementations must select the formula version specified by the
validating era and evaluate it with the effective rate. Future formula versions
require their own specification and activation decision.

For testing formula evolution, the reference implementation includes this
experimental V2:

```math
F_{2,p}(o) = p\left(260 + 80N(o) + D(o) + R(o)\right)
```

It uses the same measurements as V1. At `p = 4310`, the two-asset example costs
1,810,200 lovelace under V2. This CIP does not activate V2.

Changing the formula or rate leaves existing output values and spending conditions
unchanged. Outputs created by later transactions, including successors to existing
outputs, must meet the requirement effective when those transactions are validated.

## 4. Rationale: How does this CIP achieve its goals?

### 4.1 Predictable calculation and pricing precision

V1 separates two improvements: independence from the ADA amount removes the
funding fixed point, while fixed base and per-asset allowances remove the need to
measure the complete serialized output. A change to the output's ADA alone
therefore leaves the result unchanged, including across CBOR integer-width
boundaries.

The trade-off is less byte-level pricing precision. Different addresses,
asset-name lengths or policy-sharing arrangements can receive the same charge.
Datum and reference-script payload lengths remain explicit terms because those
payloads vary independently of the native-asset count. The formula does not
eliminate serialization work for transaction fees or payload validation.

### 4.2 Resource protection

A cost formula supports resource protection only with suitable coefficients and
a suitable rate. The base and per-asset allowances must be evaluated against
actual node storage, supported address and asset-name sizes, datum and script
representations, and UTxO indexing overhead. The constants
are not a proof that every representation is conservatively priced.

The minimum-ADA rule provides the deterrence by requiring ADA to remain in each
live output. This CIP supplies its calculation. Zero pricing is representable but
does not provide the same economic deterrence as a positive requirement.

### 4.3 Compatibility and CPS scope

Existing outputs retain their value and spending conditions. An
application recreating an output after activation must meet the new requirement,
which can be higher or lower than the previous size-based minimum. Builders must
select the formula for the validating era instead of continuing to use the old
whole-output size rule.

For [CPS-0037](../CPS-0037/README.md), this proposal directly simplifies construction
and change balancing. It also makes the calculation for high fan-out distributions
and successor outputs more predictable. It does not remove the funding requirement
for those outputs, guarantee a lower total commitment, enable token-only outputs
at a positive rate, or change staking eligibility. Control over all output ADA
continues to follow the output's spending conditions.

### 4.4 Alternatives considered

| Alternative | Trade-off |
| --- | --- |
| Retain the complete serialized output size | Preserves byte-sensitive pricing, including the funding dependency and serializer coupling. |
| Exclude only the ADA encoding from the measured size | Removes the funding fixed point, while retaining the need to reproduce the remaining output serialization. |
| Charge a constant for every output | Simplifies calculation further, but gives no additional charge for native assets, datum payloads or reference scripts. |
| Use fixed allowances plus payload lengths | Gives a predictable calculation with explicit charges for the measured components, at the cost of less precise pricing for addresses and asset representations. |

### 4.5 Author TODOs

> **TODO — Calibration:** Confirm V1's coefficients against measured resource
> costs and document the calibration rationale, including adversarial outputs
> and UTxO indexing overhead.

> **TODO — Activation:** Assign the activating protocol version, confirm the
> effective rate and specify the mechanism selecting future formula versions.

## 5. Path to Active

### 5.1 Acceptance Criteria

- [ ] Complete review of the measurements, coefficients, activation rules and
      compatibility effects for minimum-ADA outputs.
- [ ] Validate the resource-cost calibration for supported representations and
      document the resulting economic assumptions.
- [ ] Demonstrate independent agreement on calculation vectors covering absent
      payloads, datum hashes, inline data, native and Plutus reference scripts,
      asset identities and preserved accepted payload bytes.
- [ ] Demonstrate that changing ADA alone, including across encoding-width
      boundaries, leaves the calculated requirement unchanged.
- [ ] Verify minimum-ADA admission and collateral returns at the exact bound and
      below it, with activation and protocol-parameter changes covered.
- [ ] Integrate the formula into node implementations and transaction-building
      interfaces, then activate it through the agreed protocol transition.

### 5.2 Implementation Plan

The Ledger reference implementation separates output measurement from pure formula
evaluation. Its shared formula and measurement types and its Dijkstra output
measurement adapter are linked below at revision
`2298a008589d5a0a5ea70bd1ec87d8477e989422`.

Implementers must integrate the calculation into the target era's minimum-ADA
validation and builder interfaces, including collateral-return construction.
Integration must preserve accepted datum and script payload lengths and use exact
integer arithmetic. Conformance checks must compare implementations with
independent vectors rather than duplicate one implementation's calculation.

## 6. References

- [CPS-0037: application and transaction friction in minUTxO implementation](../CPS-0037/README.md)
- [Shared formula and measurement types](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/libs/cardano-ledger-core/src/Cardano/Ledger/State/Accounting/UTxOs/Deposit.hs)
- [Output measurement adapter](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/UTxOs/Deposit/Formula.hs)
- [Pricing specification and executable cases](https://github.com/nhenin/cardano-ledger-specs/blob/2298a008589d5a0a5ea70bd1ec87d8477e989422/docs/dijkstra-deposit-store-rules.md#ds-pricing)
- [Ledger implementation discussion](https://github.com/nhenin/cardano-ledger-specs/pull/3)

## 7. Copyright

This CIP is licensed under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode).
