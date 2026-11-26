---
CIP: "?"
Title: UTxO Deposit versus UTxO Minimum ADA
Category: Ledger
Status: Proposed
Authors:
    - Nicolas Henin <nicolas.henin@iohk.io>
    - Will Gould <will.gould@iohk.io>
    - Polina Vinogradova <polina.vinogradova@iohk.io>
Implementors: []
Discussions:
    - "CIP discussion: https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/61"
    - "Motivation refinements: https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/62"
    - "Formula separation: https://github.com/input-output-hk/arc-cardano-minutxo-alternatives/pull/63"
    - "CPS review: https://github.com/cardano-foundation/CIPs/pull/1268"
    - "Ledger prototype: https://github.com/nhenin/cardano-ledger-specs/pull/3"
Solution To:
    - "CPS-0037: https://github.com/cardano-foundation/CIPs/tree/master/CPS-0037"
Created: 2026-08-03
License: CC-BY-4.0
---

**Table of contents**

- [Abstract](#abstract)
- [Motivation: Why is this CIP necessary?](#motivation-why-is-this-cip-necessary)
  - [1 Preliminaries — the live UTxO set and its economic deterrent](#1-preliminaries--the-live-utxo-set-and-its-economic-deterrent)
  - [2 From straightforward payments to hidden application intent](#2-from-straightforward-payments-to-hidden-application-intent)
    - [2.1 An ADA payment already covers the minimum](#21-an-ada-payment-already-covers-the-minimum)
    - [2.2 A token-only transfer introduces ADA funding](#22-a-token-only-transfer-introduces-ada-funding)
    - [2.3 The recorded value obscures the intended payment](#23-the-recorded-value-obscures-the-intended-payment)
  - [3 Composition multiplies the funding work](#3-composition-multiplies-the-funding-work)
  - [4 Explicit deposits with a choice of output form](#4-explicit-deposits-with-a-choice-of-output-form)
- [Specification](#specification)
  - [1 Application value and resource backing](#1-application-value-and-resource-backing)
    - [1.1 The banknote analogy](#11-the-banknote-analogy)
    - [1.2 Minimum-ADA vs deposit-backed outputs](#12-minimum-ada-vs-deposit-backed-outputs)
    - [1.3 Calculating the deposit for one output](#13-calculating-the-deposit-for-one-output)
    - [1.4 From individual deposits to transaction netting](#14-from-individual-deposits-to-transaction-netting)
  - [2 Transaction-building experience](#2-transaction-building-experience)
    - [2.1 Build the application. Review the net.](#21-build-the-application-review-the-net)
    - [2.2 Describing the application flow](#22-describing-the-application-flow)
    - [2.3 Choosing funding and refund policies](#23-choosing-funding-and-refund-policies)
    - [2.4 Computing and reviewing the net](#24-computing-and-reviewing-the-net)
    - [2.5 Composing SubTxs and delegating to TopTx](#25-composing-subtxs-and-delegating-to-toptx)
      - [2.5.1 Building a token-only SubTx](#251-building-a-token-only-subtx)
      - [2.5.2 Netting across SubTxs](#252-netting-across-subtxs)
    - [2.6 Mixing minimum-ADA and deposit-backed outputs](#26-mixing-minimum-ada-and-deposit-backed-outputs)
      - [2.6.1 Choosing the form of each payment](#261-choosing-the-form-of-each-payment)
      - [2.6.2 Spending an input below the minimum](#262-spending-an-input-below-the-minimum)
  - [3 The ledger’s transaction interface](#3-the-ledgers-transaction-interface)
    - [3.1 TxOut forms and encoding](#31-txout-forms-and-encoding)
    - [3.2 How the ledger recovers an input’s reserve from `Unspent`](#32-how-the-ledger-recovers-an-inputs-reserve-from-unspent)
    - [3.3 TxBody deposit declarations and encoding](#33-txbody-deposit-declarations-and-encoding)
      - [3.3.1 TopTx deposit declaration](#331-toptx-deposit-declaration)
      - [3.3.2 SubTx deposit declaration](#332-subtx-deposit-declaration)
    - [3.4 Building transactions outside the node](#34-building-transactions-outside-the-node)
  - [4 From submission to the recorded outcome](#4-from-submission-to-the-recorded-outcome)
    - [4.1 What the ledger checks at inclusion](#41-what-the-ledger-checks-at-inclusion)
    - [4.2 How execution changes the live UTxO set](#42-how-execution-changes-the-live-utxo-set)
      - [4.2.1 Ordinary success](#421-ordinary-success)
      - [4.2.2 Accepted phase-2 failure](#422-accepted-phase-2-failure)
  - [5 Tracking UTxO reserves across blocks](#5-tracking-utxo-reserves-across-blocks)
    - [5.1 What the accounting state stores](#51-what-the-accounting-state-stores)
    - [5.2 From one input’s reserve to total UTxO backing](#52-from-one-inputs-reserve-to-total-utxo-backing)
    - [5.3 Restoring a consistent view after rollback](#53-restoring-a-consistent-view-after-rollback)
  - [6 New Formula Activation](#6-new-formula-activation)
    - [6.1 When the new price takes effect](#61-when-the-new-price-takes-effect)
    - [6.2 Transactions signed before activation](#62-transactions-signed-before-activation)
  - [7 Compatibility](#7-compatibility)
    - [7.1 Spending outputs imported at the hard fork](#71-spending-outputs-imported-at-the-hard-fork)
    - [7.2 Script contexts and existing contracts](#72-script-contexts-and-existing-contracts)
    - [7.3 Stake and voting weight](#73-stake-and-voting-weight)
- [Rationale: How does this CIP achieve its goals?](#rationale-how-does-this-cip-achieve-its-goals)
  - [1 Application value and funding](#1-application-value-and-funding)
  - [2 Evaluation against the CPS use cases](#2-evaluation-against-the-cps-use-cases)
  - [3 Responses to the CPS questions](#3-responses-to-the-cps-questions)
  - [4 Alternatives considered](#4-alternatives-considered)
  - [5 Resource protection and implementation costs](#5-resource-protection-and-implementation-costs)
  - [6 Author TODOs](#6-author-todos)
    - [6.1 Plutus compatibility](#61-plutus-compatibility)
    - [6.2 Pricing and activation](#62-pricing-and-activation)
    - [6.3 Declarations](#63-declarations)
    - [6.4 Stake and voting](#64-stake-and-voting)
    - [6.5 Integration and validation](#65-integration-and-validation)
- [Path to Active](#path-to-active)
  - [1 Acceptance Criteria](#1-acceptance-criteria)
  - [2 Implementation Plan](#2-implementation-plan)
  - [3 Reference transaction-construction API](#3-reference-transaction-construction-api)
- [References](#references)
- [Copyright](#copyright)

<a id="1-abstract"></a>

## Abstract

This CIP continues the community work on minUTxO, including discussions at
BuidlerFest in Argentina. We thank the community contributors whose ideas and
discussions made this proposal possible.
[CPS-0037 acknowledgements](../CPS-0037/README.md#acknowledgements) · [@Crypto2099](https://github.com/Crypto2099) · [@lehins](https://github.com/lehins) · [@ch1bo](https://github.com/ch1bo) · [@matteocoppola](https://github.com/matteocoppola) · [@padierfind](https://github.com/padierfind)

*And to everyone who has ever sighed at yet another minUTxO top-up, this one's for
you. We're working to make your life a little easier from here on.*

This proposal introduces deposit-backed TxOuts alongside the current minimum-ADA
TxOuts. A deposit-backed output records application assets, including zero ADA,
while the ledger accounts for its full storage deposit separately. Spending the
output releases its original deposit under the output's spending authority.

The proposed declaration counts the storage reserve on both sides of a
transaction. Both minimum-ADA and deposit-backed outputs contribute. The ledger
also tracks how much ADA moves into or out of its external deposit store.
SubTxs can account for their contribution locally or delegate it to TopTx,
enabling token-only operations whose fees and deposit funding are coordinated
by the enclosing transaction.

This CIP depends on UTxO Storage Cost Formula for pricing. It introduces allocation
origins and shared formula history at the hard fork, allowing the ledger and
external tools to recover each original deposit across subsequent formula and
parameter changes. [UTxO Storage Cost Formula](../CIP-????-utxo-cost-formula/README.md)

<a id="2-motivation-why-is-this-cip-necessary"></a>

## Motivation: Why is this CIP necessary?

CPS-0037 collects the community's experience with minimum ADA. This proposal
addresses the **funding and accounting work** that arises when the ADA backing
ledger state becomes part of the **application's transfers**.
[CPS-0037](../CPS-0037/README.md)

<a id="21-preliminaries--the-live-utxo-set-and-its-economic-deterrent"></a>

### 1 Preliminaries — the live UTxO set and its economic deterrent

Each node maintains the **live UTxO set**, a map from input references to unspent
outputs. In ordinary successful execution, a transaction removes the outputs it
spends and adds those it creates. The resource grows through **more entries** or
**more bytes per entry**, including larger **inline datums** and **reference
scripts**. [Inline datums](https://cips.cardano.org/cip/CIP-0032) · [Reference scripts](https://cips.cardano.org/cip/CIP-0033)

The **minimum-ADA requirement** makes every new output carry enough ADA for its
resource footprint. Keeping more or larger outputs live therefore requires more
**ADA to remain committed**. Spending an output makes its ADA available to the
transaction, subject to the requirements of the outputs it creates.
[CPS-0037 — the current rule](../CPS-0037/README.md#the-current-minutxo-rule)

![More unspent outputs increase the number of map entries, while larger payloads increase bytes per entry. Both require more ADA to remain committed.](images/motivation-resource-backing.png?v=9c1d5cce)

That commitment is the **economic deterrent** this proposal preserves. It is the
**necessary resource friction**. Mixing that funding into application payments
also creates **accidental friction**, as the following examples show.
[CPS-0037 — necessary and accidental friction](../CPS-0037/README.md#necessary-resource-friction-and-accidental-implementation-friction)

<a id="21-resource-costs-and-accidental-friction"></a>
<a id="21-application-value-independent-of-resource-funding"></a>
<a id="22-from-ada-payments-to-application-workflows"></a>
<a id="23-explicit-accounting-and-readable-history"></a>
<a id="21-when-resource-funding-obscures-an-application-payment"></a>

<a id="22-from-straightforward-payments-to-hidden-application-intent"></a>

### 2 From straightforward payments to hidden application intent

The same rule affects these **3 application flows** differently. The examples use
illustrative minima for outputs with different contents.

![Three application flows show increasing friction. A 100 ADA payment covers its minimum. A token-only transfer requires 1.6 ADA. A 20 ADA payment with tokens requires a 12 ADA top-up, obscuring the intended payment in the recorded 32 ADA Value.](images/motivation-application-payments.png?v=b6148519)

<a id="221-an-ada-payment-already-covers-the-minimum"></a>

#### 2.1 An ADA payment already covers the minimum

An application sends **100 ADA** to a script output with a large datum and a
reference script. Its minimum is approximately **52 ADA**. The payment already
covers the requirement, so this output needs **no additional funding**. The
intended payment can be recorded directly in `Value`.

<a id="222-a-token-only-transfer-introduces-ada-funding"></a>

#### 2.2 A token-only transfer introduces ADA funding

The intended payment is **1 token and zero ADA**. With a **1.6 ADA minimum**, the
output must also carry that ADA. Sending tokens to **3 recipients** through
3 such outputs requires **4.8 ADA** alongside the tokens. The application now
has **ADA funding** to manage, and each recipient's spending conditions control
that ADA. [CPS-0037 — token transfers and funding control](../CPS-0037/README.md#use-case-fund-for-someone-else)

<a id="223-the-recorded-value-obscures-the-intended-payment"></a>

#### 2.3 The recorded value obscures the intended payment

An application sends **1,000 tokens and 20 ADA** to a script output with a
**32 ADA minimum**. A **12 ADA top-up** brings its recorded `Value` to
**1,000 tokens and 32 ADA**.

A **token-only transfer** could produce the same `Value`, with all 32 ADA supplied
for resource backing. `Value` alone cannot recover the intended **0 ADA or 20 ADA
payment**. Applications must preserve that **application context** through a
datum, metadata or their own records, and consult it when interpreting subsequent
transfers and transaction history. [CPS-0037 — application value and resource backing](../CPS-0037/README.md#applicative-value-and-operational-backing)

<a id="22-transaction-level-netting"></a>
<a id="23-ada-free-subtxs"></a>
<a id="24-transaction-level-netting"></a>
<a id="25-ada-free-subtxs"></a>
<a id="22-composition-multiplies-the-funding-work"></a>

<a id="23-composition-multiplies-the-funding-work"></a>

### 3 Composition multiplies the funding work

Applications must repeat this accounting across **recipient outputs** and
**successive state updates**. If an output holds 32 ADA and its successor needs
40 ADA after a pricing change, that successor has an **8 ADA funding
shortfall**. Consolidating outputs can instead free ADA for other uses.
Each step combines the application's asset movements with **top-ups and refunds**.
[CPS-0037 — successor-output funding](../CPS-0037/README.md#use-case-continuing-output)

**Nested transactions** amplify that work across independently authored
**SubTxs** assembled into a **TopTx**. Token-only operations can require ADA
funding and refund decisions across the batch, while their intended payment
amounts still need separate bookkeeping. Transaction-level accounting provides a
place to coordinate those resource-funding movements.
[Nested transactions](https://cips.cardano.org/cip/CIP-0118)

<a id="24-asset-free-txouts"></a>
<a id="25-a-predictable-deposit-calculation"></a>
<a id="26-asset-free-txouts"></a>
<a id="26-pricing-evolution-and-compatibility"></a>
<a id="27-simple-calculation-and-historical-recovery"></a>
<a id="23-explicit-deposits-with-a-choice-of-output-form"></a>

<a id="24-explicit-deposits-with-a-choice-of-output-form"></a>

### 4 Explicit deposits with a choice of output form

The goal is to preserve the **economic deterrent** while making **application
amounts explicit** and resource funding easier to coordinate. **Deposit-backed
outputs** account separately for application assets and their full storage
deposit. The current **minimum-ADA form** remains available for workflows in
which the same ADA serves both as payment and as resource backing.

The proposal gives transaction builders 3 capabilities.

1. Express application inputs and outputs with their **intended assets**.
2. Account for deposits through a **net change at transaction level**, with
   reusable funding and refund policies.
3. Let a SubTx handle its change locally or **delegate to TopTx**, which can
   coordinate deposit funding alongside fees.

The **UTxO Storage Cost Formula** proposal supplies the calculation. This CIP
adds the accounting and history needed to recover each **original deposit** when
its output is spent, including after pricing changes.
[UTxO Storage Cost Formula](../CIP-????-utxo-cost-formula/README.md)

<a id="317-scope-and-terminology"></a>

<a id="3-specification"></a>

## Specification

This CIP starts with the choice between **minimum-ADA and deposit-backed
outputs**. It follows that choice through transaction construction, from
calculating the net and choosing who funds or receives it to signing a
standalone transaction or a batch of SubTxs.

The **ledger’s transaction interface** sets out what a builder signs and which
data a wallet or SDK needs to reproduce the calculation. A payment example then
follows the deposit into the live UTxO set. **New Formula Activation** explains
which price applies to a transaction signed before a change takes effect.
**Compatibility** covers existing outputs, script-visible values and stake and
voting weight.

> **Ledger specification.** The companion document in `cardano-ledger` defines
> the validation rules, state transitions and accounting invariants for this
> feature. It lives alongside the Dijkstra prototype. Links throughout this CIP
> point to the rule or implementation behind each behaviour.
> [Ledger specification for minimum-ADA and deposit-backed outputs](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/README.md)

<a id="31-application-value-and-resource-backing"></a>

### 1 Application value and resource backing

Two amounts are involved when an application creates an output. The application
chooses the value it intends to transfer. The storage cost formula determines
the ADA backing required for the output to occupy the live UTxO set. This proposal
introduces a deposit-backed output that accounts for each amount separately.

<a id="311-the-banknote-analogy"></a>

#### 1.1 The banknote analogy

A **20-euro banknote** gives its holder 20 euros of spending power. Producing the
note also requires paper, ink and printing. Its face value expresses what it can
buy. Its production cost expresses the resources needed to create the physical
object used for that payment.

A deposit-backed output gives application value and resource backing similarly
distinct roles. The output records the assets the application transfers. Its
associated ADA deposit backs the resources it occupies in the live UTxO set.

![A banknote distinguishes face value from production cost, and a deposit-backed output distinguishes application value from resource backing](images/01-application-value-and-deposit.png?v=b2dfef87)

In the example, the application transfers **1,000 tokens and 20 ADA**. An
illustrative **32 ADA deposit** gives **52 ADA committed for this output**,
alongside the tokens. The deposit is held while the output is unspent. Spending
the output releases that deposit through the transaction balance.

<a id="311-choosing-each-output-form"></a>

<a id="312-minimum-ada-and-deposit-backed-outputs"></a>

<a id="312-minimum-ada-vs-deposit-backed-outputs"></a>

#### 1.2 Minimum-ADA vs deposit-backed outputs

The transaction builder chooses the form of each new ordinary output. In a **minimum-ADA
output**, the ADA in `Value` also satisfies the resource requirement. In a
**deposit-backed output**, `Value` records the application assets and the full
storage deposit is accounted for outside the `TxOut`.

Consider the intended transfer of **1,000 tokens and 20 ADA**, with an illustrative
resource requirement of **32 ADA**. A minimum-ADA output must carry 32 ADA,
including a **12 ADA top-up**. Its `Value` would be identical for a **token-only
transfer**, where all 32 ADA were supplied to meet the minimum. Reading `Value`
alone cannot distinguish those application payments.

A deposit-backed output records the **20 ADA payment** alongside the tokens and
accounts for the **32 ADA deposit** separately, giving **52 ADA committed** for
this output.

![A 20 ADA and 1,000 token payment commits 32 ADA with a minimum-ADA output or 52 ADA with a deposit-backed output](images/01a-output-forms-below-minimum.png?v=1cfe316c)

For the token-only transfer, the deposit-backed output instead records **1,000
tokens and zero ADA** in `Value`, with the same **32 ADA external deposit**. The
intended application ADA amount is explicit in each case.

When the payment already covers the minimum, the minimum-ADA form lets the same
ADA serve both purposes. A **5 ADA payment** with a **2 ADA resource requirement**
commits **5 ADA** in that form. A deposit-backed output records the 5 ADA payment
and a separate 2 ADA deposit, committing **7 ADA**.

![A 5 ADA payment with a 2 ADA storage requirement commits 5 ADA with a minimum-ADA output or 7 ADA with a deposit-backed output](images/01b-output-forms-above-minimum.png?v=0fa76cab)

**Deposit-backed outputs make the distinction explicit when resource funding
would otherwise obscure the application's intended ADA amount.** This supports
token-only transfers, exact ADA payments below the minimum, and application state
with zero application assets. Minimum-ADA outputs remain available for workflows
that use the same ADA as payment and resource backing. The choice is made for
each output, and both forms can appear in one transaction.

When a minimum-ADA output is spent, its full value enters the transaction balance.
Spending a deposit-backed output contributes its application value and releases
its historical external deposit into that balance.

<a id="313-calculating-the-deposit-for-one-output"></a>

#### 1.3 Calculating the deposit for one output

**When creating an output**, apply the active storage cost formula to its
contents. Take the deposit-backed output above that pays **5 ADA**. Suppose
the formula assigns this output **400 pricing units**.
At an illustrative **5,000 lovelace per unit**, its deposit is
`400 × 5,000 = 2,000,000 lovelace`, or **2 ADA**. The companion CIP defines
how to measure an output in pricing units. [UTxO Storage Cost Formula](../CIP-%3F%3F%3F%3F-utxo-cost-formula/README.md)

**When spending that output**, recover the **2 ADA** allocated when it entered
the live UTxO set. For a newly created output, the ledger pairs the `TxOut`
with the slot of the block that created it. Together they form an
**`Unspent` entry**. A builder looks up the formula version and parameters
active at that slot and applies them to the output.

![At slot 100 the output requires a 2 ADA deposit. A rate increase at slot 200 leaves that deposit at 2 ADA. At slot 210 spending it credits 2 ADA and an identical successor requires 2.4 ADA.](images/output-deposit-at-two-prices.svg?v=3c58f42d)

The new rate makes an identical successor cost **2.4 ADA**. If the other
inputs and outputs have matching reserves, the transaction needs **0.4 ADA**
in additional backing. The same rule applies when the formula itself changes.

For a **minimum-ADA input**, the historical requirement measures the reserve
already included in its value. The transaction can credit at most the ADA the
input actually holds. For a **deposit-backed input**, it credits the full
external deposit, even when the application value contains zero ADA.

<a id="313-from-individual-deposits-to-transaction-netting"></a>

<a id="314-from-individual-deposits-to-transaction-netting"></a>

#### 1.4 From individual deposits to transaction netting

The builder also chooses how many outputs carry a payment. Just as
**20 coins of 1 euro** can be exchanged for **1 banknote of 20 euros**,
a transaction can group the same assets into fewer outputs. Each output
has its own reserve.

Across both output forms, **input reserves can fund output reserves**. Add the
reserves required by the new outputs and subtract the backing recovered from
the inputs.

The transaction builder can therefore design the **application flow** and review
its resource-funding effect as **one net amount**. The following section shows how
this works in practice, with a **funding input** for top-ups, a **refund output**
for released ADA, and a calculation that prepares the net declaration for review.

<a id="31-moving-minutxo-accounting-from-txouts-to-transactions"></a>
<a id="31-transaction-builder-experience"></a>
<a id="31-transaction-building-dsl"></a>

<a id="32-transaction-building-dsl"></a>

<a id="32-transaction-building-experience"></a>

### 2 Transaction-building experience

<a id="321-build-the-application-review-the-net"></a>

#### 2.1 Build the application. Review the net.

Transaction builders describe the **application flow**, choose **funding and
refund policies**, and review the **net deposit change**. For the final set of
inputs and outputs, the construction API recovers each spent input’s original
reserve and prices each new output. It uses the difference to prepare the
declaration for a standalone transaction or a TopTx/SubTx batch.

![Transaction-building overview showing an application flow from 3 tokens to 3 separate outputs, with funding and refund choices used to calculate one net deposit declaration](images/02-builder-experience-overview.png?v=d7bbca05)

This workflow runs in transaction-construction software. The ledger validates its
**signed result** and records individual deposit allocations when applying it.

<a id="321-describing-the-application-flow"></a>

<a id="322-describing-the-application-flow"></a>

#### 2.2 Describing the application flow

An application wants to consolidate **3 units of token C in a single output**.
The transaction builder selects 3 deposit-backed inputs, each with 1 token and
zero ADA in its `Value`. The inputs retain their recorded form. For each new
ordinary output, the builder chooses between the **minimum-ADA** and **deposit-backed**
forms. Here, the builder chooses a deposit-backed output for the application
transfer so that **output 1** carries all 3 tokens and zero ADA.

![Three inputs holding 1 unit of token C each are consolidated into output 1. The transaction declares a 1.6 ADA net deposit release to refund output 0.](images/03-dsl-net-declaration.png?v=f2ad7948)

The builder designates **output 0** for the refund and also chooses the
deposit-backed form for it. Assume each of the 3 spent outputs releases a
**1.6 ADA** deposit and each of the 2 new outputs requires the same amount.
Of the 4.8 ADA released, 3.2 ADA backs the new outputs, including the refund
output itself. The remaining **1.6 ADA** goes into output 0 as spendable value.
The funding candidate `reserve#0` stays unspent. Assume the minimum-ADA input
for fees and the change output have equal embedded reserves. Their contributions
cancel in the net and are omitted from the breakdown below.

> **Viewing individual deposits.** The application view can hide the per-output
> deposits and show just the net release. When the ledger applies this transaction,
> it releases the spent inputs’ deposits and allocates a separate deposit to each
> new deposit-backed output. When a later transaction spends one of those outputs,
> its deposit appears on the input side of that transaction’s breakdown.

<details>
<summary>Show the deposit breakdown for this transaction</summary>

| Entry | Deposit released | Deposit allocated |
| --- | ---: | ---: |
| 3 spent token inputs | 1.6 ADA each | — |
| Output 1 · Token consolidation | — | 1.6 ADA |
| Output 0 · Refund | — | 1.6 ADA |
| **Total** | **4.8 ADA** | **3.2 ADA** |

</details>

<a id="313-funding-and-refund-policies"></a>

<a id="323-funding-and-refund-policies"></a>

<a id="322-choosing-funding-and-refund-policies"></a>

<a id="323-choosing-funding-and-refund-policies"></a>

#### 2.3 Choosing funding and refund policies

The builder chooses **where a top-up comes from** and **where a refund goes**.
An application can reuse these choices across transfers. In the consolidation
above, the policy offers `reserve#0` for funding and names output 0 for refunds.
The transaction releases **1.6 ADA**, so output 0 receives it and the reserve
stays unspent.

![Funding can use inputs already in the body or a named reserve input. Refunds can go to an existing output or to a new output supplied by the builder.](images/03a-reserve-policy.png?v=8fb677f2)

For a **top-up**, the builder can use funds already in the transaction or name
a reserve input to add when the body has an allocation to fund. If selected, the
reserve becomes an ordinary spending input. Its historical backing counts
towards the final net, including any minimum ADA already in its value.

For a **refund**, the builder can select an existing output by index or supply a
new output. Either form of new refund output contributes its active reserve to
the net. A minimum-ADA output carries that backing in its value. A deposit-backed
output requires a separate deposit. If the new reserve consumes the entire
release, the builder must choose another refund destination.

The builder can **preview the declaration** before applying the policy to the
transaction body. For the consolidation above, the pseudocode gives the following results.

```text
policy = { funding: candidate("reserve#0"), refund: existingOutput(0) }

previewDepositChange(draft, policy, ledgerContext)
    → Release(1.6 ADA, output 0)

applyDepositPolicy(draft, policy, ledgerContext)
    → draft with deposit declaration Release(1.6 ADA, output 0)
```

The preview accounts for any input or output the policy would add. Applying the
policy to the same draft and ledger context includes those additions and writes
the same declaration. Here, output 0 is already in the draft and the reserve
stays unspent. The builder sets the refund output’s value and balances assets,
change and fees before signing.

For a Haskell implementation, see the [reference transaction-construction API](#3-reference-transaction-construction-api).

<a id="311-builder-experience-consolidating-token-outputs"></a>
<a id="312-consolidation-and-the-net-declaration"></a>
<a id="312-computing-and-reviewing-the-net"></a>

<a id="322-computing-and-reviewing-the-net"></a>

<a id="323-computing-and-reviewing-the-net"></a>

<a id="324-computing-and-reviewing-the-net"></a>

#### 2.4 Computing and reviewing the net

With the inputs, outputs and reserve policy chosen, the builder can see **how
much ADA this transaction needs to commit or can recover**. For a standalone
transaction, price **every new output** under the active rules and recover the
**original reserve of every spent input**. For a minimum-ADA input the reserve
is capped at the ADA it contains. Include any funding input, change output or
refund output selected by the policy.

```math
\text{Net reserve change} = \text{Reserves on new outputs} - \text{Reserves on spent inputs}
```

The sign determines the declaration. **Release** returns the surplus when the
net is negative. **Allocate** identifies the additional backing when the net is positive.
Equal amounts give **No deposit change**, an explicit zero.

Consolidating or splitting outputs can change the net. So can changing the
contents of a single output. Consider 3 drafts that spend **the same inputs**
and create **the same number of outputs**. Each spends a script output with a
historical deposit of **3.2 ADA** and creates one deposit-backed successor with
the same address and application assets. Each also includes the same minimum-ADA
reserve input and a minimum-ADA change output at index 0, which can receive a
refund. Assume the reserve on the change output equals the embedded reserve on
the funding input, so their contributions cancel.

Assume the pricing rules stay fixed at an illustrative **4,000 lovelace per
byte**. The comparison varies the encoded sizes of the successor’s **inline
datum** and **reference script**. A difference of 400 bytes changes the required
deposit by **1.6 ADA**.

![Three outcomes for the same inputs and output count. A smaller inline datum releases 1.6 ADA. Adding 200 bytes each to the inline datum and reference script allocates 1.6 ADA. The same priced size gives zero net deposit change.](images/04-dsl-funding-refund.png?v=108045f5)

The builder can use this preview to compare valid representations of the same
application state, then review the declaration for the chosen draft before signing.

<a id="32-subtx-composition-and-delegation"></a>
<a id="33-subtx-composition-and-delegation"></a>
<a id="321-local-accounting-or-delegation-to-toptx"></a>
<a id="331-local-accounting-or-delegation-to-toptx"></a>

<a id="324-subtx-accounting-and-delegation-to-toptx"></a>

<a id="324-composing-subtxs-and-delegating-to-toptx"></a>

<a id="325-composing-subtxs-and-delegating-to-toptx"></a>

#### 2.5 Composing SubTxs and delegating to TopTx

In a nested transaction, the enclosing **TopTx** brings together **SubTxs** that
can have different authors. Each author calculates the net deposit change for
their SubTx’s inputs and outputs, just as they would for a standalone transaction.
They also choose **who funds a shortfall or receives a surplus**.

- **Handle it locally.** For **Allocate**, the author funds the shortfall within
  the SubTx, selecting a reserve input if needed. For **Release**, they choose one of the
  SubTx’s ordinary outputs to receive the refund. Its value must include at
  least the refund amount. Any external deposit on that output is accounted for
  separately.
- **Delegate to TopTx.** The SubTx still declares its own amount. For **Allocate**,
  it requests funding from TopTx. For **Release**, it lets TopTx account for the
  surplus alongside the other contributions. The author can build the SubTx
  without a deposit funding input or refund destination of its own.

![For Allocate or Release, the SubTx can arrange its own funding or refund, or declare the amount and delegate it to TopTx.](images/05-dsl-subtx-delegation.png?v=338a5eb4)

When the new outputs require exactly the reserve recovered from the inputs, a
SubTx that declares its net signs **No deposit change**. There is no top-up or
refund to delegate.

<a id="315-an-ada-free-subtx-under-formula-v1"></a>
<a id="323-an-ada-free-subtx-under-formula-v1"></a>
<a id="323-an-ada-free-subtx-using-the-storage-cost-formula"></a>
<a id="333-an-ada-free-subtx-using-the-storage-cost-formula"></a>

<a id="326-an-ada-free-subtx-example"></a>

<a id="3242-an-ada-free-subtx-example"></a>

<a id="3252-an-ada-free-subtx-example"></a>

<a id="3251-building-a-token-only-subtx"></a>

##### 2.5.1 Building a token-only SubTx

Alice holds tokens B and C in a single deposit-backed output. She sends **B to
Bob** and **C to Carol**. Each recipient’s deposit-backed output holds one token
and **zero ADA** in its `Value`.

![Alice spends B and C together and sends B to Bob and C to Carol. Her SubTx declares Allocate for the deposit shortfall of 1.0775 ADA and delegates funding to TopTx.](images/05a-token-only-subtx.png?v=918e5df3)

Spending Alice’s input releases its deposit, which covers part of the deposits
on the 2 new outputs. Alice’s SubTx declares **Allocate** and asks TopTx to
fund the remaining **1.0775 ADA**. The operator supplies the top-up from its
reserve and pays the batch fee. Alice can build her transfer using just the
input that holds her tokens.

<details>
<summary>How the deposit shortfall is calculated</summary>

Assume 57-byte base addresses, no datum or reference script, and the same
pricing rules for all 3 outputs. At 4,310 lovelace per byte, Alice’s two-asset
output releases **1.71538 ADA**. Bob’s and Carol’s one-asset outputs each
require **1.39644 ADA**. [UTxO Storage Cost Formula](../CIP-%3F%3F%3F%3F-utxo-cost-formula/README.md)

```math
2 \times 1.39644 - 1.71538 = 1.0775\ \text{ADA}
```

In this example, Alice supplies the only SubTx. The operator uses a minimum-ADA
reserve input and a minimum-ADA change output with equal embedded reserves.
Its own reserve change is zero. The TopTx declaration equals Alice’s contribution, and the
batch funds the allocation once.

</details>

<a id="322-netting-across-subtxs"></a>
<a id="332-netting-across-subtxs"></a>

<a id="325-netting-across-subtxs"></a>

<a id="3241-netting-across-subtxs"></a>

<a id="3251-netting-across-subtxs"></a>

<a id="3252-netting-across-subtxs"></a>

##### 2.5.2 Netting across SubTxs

The TopTx builder reviews **two amounts**.

- **The batch net** is the amount TopTx declares. It includes TopTx’s own reserve
  change and every SubTx’s reserve change, counted once.
- **TopTx’s share** is what remains after subtracting the changes that SubTxs
  fund or refund locally. It includes TopTx’s own change and any change delegated to it.
  A SubTx that spends and creates only minimum-ADA outputs may omit its
  declaration. In that case, its change in embedded reserve counts in full
  towards TopTx’s share. [Ledger attribution rule](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-accounting-attribution)

Consider 2 SubTxs spending distinct token inputs. Assume every token output in
this example, whether spent or created, carries zero application ADA and has an
external deposit of **1.6 ADA**. SubTx A consolidates 3 token inputs into 1
output and delegates **Release 3.2 ADA**.
SubTx B spends 1 token input, creates 3 outputs and delegates **Allocate
3.2 ADA**. TopTx’s fee-funding input and change output carry equal embedded
reserves, so its own reserve change is zero.

![SubTx A delegates Release of 3.2 ADA and SubTx B delegates Allocate of 3.2 ADA. TopTx’s own deposit change is zero, so the batch declares No deposit change.](images/06-dsl-batch-netting.png?v=34c42af7)

A’s release covers B’s allocation. **TopTx declares No deposit change**, and no
deposit top-up or refund output is needed. The token operations still have their
own declarations, and the operator still funds the fee.

Now suppose A chooses **local release** and puts the 3.2 ADA refund in its own
token output. With the same deposit costs, the batch net is still zero. This
time the TopTx builder must arrange **3.2 ADA for B** because A has directed
its refund to its own output. This is why the builder prepares each SubTx’s
declaration first and reviews the enclosing transaction again whenever a child’s
inputs, outputs or delegation choice changes.

<a id="326-mixing-minimum-ada-and-deposit-backed-outputs"></a>

#### 2.6 Mixing minimum-ADA and deposit-backed outputs

At the hard fork, all existing UTxOs have the minimum-ADA form. When spending
them, a builder can introduce deposit backing **one output at a time**. Reserves
from all spent inputs can fund any new output. The builder reviews a single
[transaction net](#24-computing-and-reviewing-the-net) across both forms.

<a id="3261-one-input-two-output-forms"></a>

<a id="3261-choosing-the-form-of-each-payment"></a>

##### 2.6.1 Choosing the form of each payment

Keep a **minimum-ADA output** when a contract expects the backing ADA in its
value. Choose a **deposit-backed output** when the recipient should see exactly
the assets the application intends to send. Both choices can appear in the same
transaction.

![Alice’s 1.6 ADA reserve and a 0.4 ADA top-up fund Carol’s deposit.](images/06a-mixed-output-forms.png?v=206adcf6)

Splitting the payment creates another output to back. Its embedded minimum
counts towards the net even when the external deposit for the token stays the same.

![Bob’s payment includes 1.6 ADA of reserve. Carol’s token needs a separate 2 ADA deposit.](images/06a2-split-payment.png?v=6b19649a)

<a id="3262-spending-an-input-below-the-minimum"></a>

##### 2.6.2 Spending an input below the minimum

A pre-fork output can hold less ADA than the minimum calculated at migration.
In that case **all the ADA it holds counts as reserve**. The builder
can pool it with reserves from other inputs and fund any remaining shortfall.
This works for either form of successor. [Migration rule](#71-spending-outputs-imported-at-the-hard-fork)

![The 100 tokens go to a deposit-backed output. The old input supplies 2 ADA of its deposit and other funds supply 1 ADA.](images/06b-underfunded-input.png?v=3c5f1f76)

<a id="33-ledger-interface-and-validation"></a>

<a id="33-ledger"></a>

<a id="33-ledger-specification"></a>
<a id="331-signed-transaction-interface"></a>
<a id="331-from-txouts-to-the-signed-deposit-declaration"></a>

<a id="331-the-ledgers-transaction-interface"></a>

<a id="33-the-ledgers-transaction-interface"></a>

### 3 The ledger’s transaction interface

The [transaction-building experience](#2-transaction-building-experience)
gives the builder two choices to express in the **signed transaction**:
which form to use for each new ordinary `TxOut`, and how to fund or settle the net
reserve change declared in the `TxBody`.

On the input side, the builder signs a `TxIn` reference. To check the
declaration, the ledger follows that reference to an **`Unspent` entry in its
own state** and recovers the reserve credited on spend. The ledger compares the
reserves required by the new outputs with the reserves recovered from spending
inputs to check the signed net. [Allocation records and reserve recovery](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/domain-model.md#section-1-1) · [Net-change rule](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-accounting-net-change)

<a id="322-output-representation"></a>
<a id="351-the-two-txout-forms"></a>
<a id="361-the-two-txout-forms"></a>

<a id="3312-txout-forms-and-encoding"></a>

<a id="3311-txout-forms-and-encoding"></a>

<a id="331-txout-forms-and-encoding"></a>

#### 3.1 TxOut forms and encoding

The builder chooses a form **for each ordinary output** in the signed `TxBody`. In the
split payment below, the same transaction pays Bob in ADA and sends Carol a
token. [Choosing the form of each payment](#261-choosing-the-form-of-each-payment)

![One TxBody creates Bob’s minimum-ADA output 0 with 5 ADA, including its 1.6 ADA minimum, and Carol’s deposit-backed output 1 with 1 token B and zero ADA. A separate 2 ADA deposit backs output 1 while it is unspent.](images/txout-forms-in-one-body.svg?v=1e0cb02b)

- **Minimum-ADA output.** Its value must contain at least the active minimum.
- **Deposit-backed output.** Its value holds the application assets and can
  contain zero ADA and zero native assets. The full deposit is funded
  separately, even when the application ADA exceeds the required deposit.

When either output is spent, the `TxIn` identifies it by transaction ID and
output index. The ledger reads its form from that live entry. A collateral
return follows a fixed rule for its output form. [Collateral returns on accepted phase-2 failure](#422-accepted-phase-2-failure)

**How the ledger recognises the form.** In a CBOR output map, exactly one
value key is present. Key `1` identifies the minimum-ADA form and key `4`
identifies the deposit-backed form. Both encode the same `value` type.
The existing Alonzo list form also decodes as a minimum-ADA output.

![The two TxOut maps share the address at key 0, optional datum at 2 and optional reference script at 3. Minimum-ADA outputs carry the full value at key 1. Deposit-backed outputs carry the application assets at key 4 and account for the deposit outside that value.](images/txout-forms-encoding.svg?v=9951101a)

The deposit amount and allocation slot are outside the serialized output.
The ledger derives the reserve for each output occurrence, including identical
outputs at distinct indices and zero-priced outputs.

<details>
<summary>Annotated Haskell · <strong>TxOut</strong> forms and their CBOR encoding</summary>

Each era defines the payload type for each constructor.
[Shared output type](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-core/src/Cardano/Ledger/TxOut.hs#L79-L81)

```haskell
data TxOut era
  -- The ADA that covers the minimum is part of the output's value.
  = MinAdaTxOut !(MinAdaTxOut era)
  -- The output carries the application's assets. Its deposit is accounted for separately.
  | DepositBackedTxOut !(DepositBackedTxOut era)

-- Dijkstra keeps the Babbage payload for minimum ADA and adds a second payload.
instance EraTxOut DijkstraEra where
  type MinAdaTxOut DijkstraEra = BabbageTxOut DijkstraEra
  type DepositBackedTxOut DijkstraEra = DijkstraDepositBackedTxOut
```

**Minimum-ADA payload.** Dijkstra reuses the Babbage output. Its public
pattern exposes four fields, including the full `Value` that covers the minimum.
[Dijkstra output types](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/TxOut.hs#L217-L219) · [Babbage output pattern](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/babbage/impl/src/Cardano/Ledger/Babbage/TxOut.hs#L479-L489)

```haskell
pattern BabbageTxOut ::
  (Era era, Val (Value era), HasCallStack) =>
  Addr ->                      -- Destination and spending conditions.
  Value era ->                 -- The minimum ADA is already part of this value.
  Datum era ->                 -- No datum, a datum hash, or an inline datum.
  StrictMaybe (Script era) ->  -- Optional script available by reference.
  BabbageTxOut era
```

**Deposit-backed payload.** `ApplicationAssets` wraps the `Value` transferred
by the application. The deposit backs the corresponding unspent entry.
[Deposit-backed fields](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/TxOut.hs#L92-L97)

```haskell
-- The prototype prefixes these field names with depositBacked.
-- Address, datum and reference script play the same roles as in the Babbage output.
data DijkstraDepositBackedTxOut = DijkstraDepositBackedTxOut
  { address :: !Addr
    -- Only the assets the application transfers. The ADA amount can be zero.
  , applicationAssets :: !(ApplicationAssets DijkstraEra)
  , datum :: !(Datum DijkstraEra)
  , referenceScript :: !(StrictMaybe (Script DijkstraEra))
  }
```

**CBOR encoding.** The Dijkstra schema names the deposit-backed form
`store_backed_transaction_output`. [Output decoder](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/TxOut.hs#L310-L368)

```cddl
transaction_output =
    alonzo_transaction_output
  / babbage_transaction_output
  / store_backed_transaction_output

store_backed_transaction_output =
  { 0 : address
  , 4 : application_assets
  , ? 2 : datum_option
  , ? 3 : script_ref
  }

application_assets = value
```

</details>

<a id="321-the-live-utxo-resource"></a>
<a id="352-unspent-entries-and-allocation-origins"></a>
<a id="362-unspent-entries-and-allocation-origins"></a>
<a id="341-unspent-entries-and-allocation-origins"></a>

<a id="3331-unspent-entries-and-allocation-origins"></a>
<a id="334-historical-deposits-and-pricing-changes"></a>
<a id="3341-storage-cost-formula-and-allocation-history"></a>
<a id="342-storage-cost-formula-and-allocation-history"></a>
<a id="323-dependency-on-utxo-storage-cost-formula"></a>
<a id="361-dependency-on-utxo-storage-cost-formula"></a>
<a id="371-dependency-on-utxo-storage-cost-formula"></a>

<a id="3312-recovering-the-original-deposit-from-an-unspent-entry"></a>
<a id="3312-historical-reserves-for-minimum-ada-and-deposit-backed-outputs"></a>
<a id="3312-the-unspent-type-and-deposit-calculation"></a>

<a id="3312-how-the-ledger-recovers-an-inputs-reserve-from-unspent"></a>

<a id="332-how-the-ledger-recovers-an-inputs-reserve-from-unspent"></a>

#### 3.2 How the ledger recovers an input’s reserve from `Unspent`

**What the ledger records.**\
Suppose the transaction paying Bob and Carol is included at slot 100.\
The ledger creates an **`Unspent (TxOut era)`** entry for each output, keyed by its `TxIn`. Each entry has two fields.

- **`output`** comes from the signed transaction.
- **`allocatedAt`** comes from the ledger and is `AtSlot 100` for both outputs.

The deposit amount can be derived from those fields and the shared pricing history.

![Bob and Carol’s outputs are recorded at slot 100. Spending Bob’s minimum-ADA output credits 1.6 ADA already included in its 5 ADA value. Spending Carol’s token-only output credits its separate 2 ADA deposit.](images/historical-reserve-by-output-form.svg?v=0c6d206e)

**What the ledger calculates on spend.**\
A spending `TxIn` retrieves one of those entries.\
`computeDeposit history entry` uses its allocation origin to select the formula and parameters.

- For `AtSlot s`, it takes the last change effective at or before `s`, or the initial rules if none had taken effect.
- For a minimum-ADA output imported at the fork, `AtStoreMigration` selects the fork’s baseline.

Applying those rules to the recorded output gives its **historical requirement**.\
The output form determines how much of that requirement the input contributes to the **net reserve change**.

- A **minimum-ADA output** contributes the requirement up to the ADA in its `Value`.\
  If the migration baseline prices an output at 2 ADA and it holds only 1.5 ADA, the reserve is **1.5 ADA**.\
  That ADA enters the transaction balance once, through the input’s value.
- A **deposit-backed output** contributes the **full requirement**.\
  Its deposit was funded separately and can be recovered even when its value holds only tokens.

To check the signed declaration, the ledger subtracts these input reserves from the reserves required by the new outputs, priced at inclusion.

<details>
<summary>Annotated Haskell · <strong>Unspent</strong> and <strong>computeDeposit</strong></summary>

```haskell
-- A spending reference looks up one live entry.
newtype IndexedUTxOs era = IndexedUTxOs
  { unIndexedUTxOs :: Map TxIn (Unspent (TxOut era))
  }

data Unspent output = Unspent
  { output :: !output              -- The accepted TxOut, including its form and value.
  , allocatedAt :: !AllocatedAt    -- Set by the ledger when the entry joins the live set.
  }

data AllocatedAt
  = AtStoreMigration               -- Imported at the fork. Use the migration baseline.
  | AtSlot !SlotNo                 -- Created in this block slot. Use the rules then in force.
```

[Allocation map](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-core/src/Cardano/Ledger/State/Accounting/UTxOs/IndexedUTxOs.hs#L89-L92) · [Unspent entry](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-core/src/Cardano/Ledger/State/Accounting/UTxOs/Unspent.hs#L52-L71)

```haskell
-- Recover the reserve for one input, in lovelace. Types shown for Dijkstra.
computeDeposit ::
  DepositFormulaHistory ->
  Unspent (TxOut DijkstraEra) ->
  DepositAmount
computeDeposit history (Unspent output origin) =
  -- Look up the allocation-time rules, then price the recorded output.
  Formula.computeDeposit (allocationFormula history origin) output
    -- Pass that requirement to the rule for this output form.
    & capMinAdaDeposit output

capMinAdaDeposit :: TxOut DijkstraEra -> DepositAmount -> DepositAmount
capMinAdaDeposit output deposit
  -- coinTxOutL reads the ADA in Value. This is the upper bound on embedded reserve.
  | MinAdaTxOut _ <- output = min deposit (DepositAmount $ output ^. coinTxOutL)
  -- The full deposit was set aside separately for a deposit-backed output.
  | otherwise = deposit

allocationFormula :: DepositFormulaHistory -> AllocatedAt -> DepositFormula
allocationFormula history origin = case origin of
  AtStoreMigration -> initialFormula history
  -- formulaAt includes changes activated at this slot and falls back to the baseline.
  AtSlot slot -> formulaAt slot history
```

[Allocation lookup](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-core/src/Cardano/Ledger/State/Accounting/UTxOs/Unspent.hs#L85-L89) · [Pricing history](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-core/src/Cardano/Ledger/State/Accounting/UTxOs/Deposit.hs#L141-L145) · [Output pricing function](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/UTxOs/Deposit/Formula.hs#L42-L50)

The prototype also exposes `computeExternalDeposit` for value conservation.
It returns zero for a minimum-ADA output whose reserve is already in its
`Value`, and the full deposit for a deposit-backed output. [Reserve calculation](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/UTxOs/Unspent.hs#L26-L42) · [External deposit query](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-core/src/Cardano/Ledger/State/Accounting/UTxOs/Unspent.hs#L76-L83)

</details>

<a id="312-txbody-deposit-declarations"></a>
<a id="33-txbody-declarations-and-encoding"></a>
<a id="33-ledger-interface-and-txbody-declarations"></a>
<a id="34-ledger-interface-and-txbody-declarations"></a>
<a id="332-txbody-deposit-declarations-and-encoding"></a>

<a id="3311-txbody-deposit-declarations-and-encoding"></a>

<a id="3312-txbody-deposit-declarations-and-encoding"></a>

<a id="3313-txbody-deposit-declarations-and-encoding"></a>

<a id="333-txbody-deposit-declarations-and-encoding"></a>

#### 3.3 TxBody deposit declarations and encoding

Spending inputs and outputs occupy keys `0` and `1` in the signed body.
The proposal adds **key `28`** alongside them for the **net deposit declaration**.

- The [TopTx declaration](#331-toptx-deposit-declaration) covers the **whole batch**.
- The [SubTx declaration](#332-subtx-deposit-declaration) covers **that SubTx’s contribution** and records who handles it.

![Selected CBOR fields in the signed body. TopTx key 23 contains the SubTxs. The new key 28 carries the batch net in TopTx and the individual net and any delegation in a SubTx.](images/txbody-declaration-field.svg?v=fc428033)

**Preparing a TopTx.**\
The prototype exposes two Haskell functions for the
[preview and update steps](#23-choosing-funding-and-refund-policies).

**Review the declaration.**\
`computeNetBalance history utxos strategy body`\
returns **`Right declaration`**, including the effect of any funding input or refund output the strategy would add.

**Prepare the body.**\
`updateTxBodyWithNetBalance history utxos strategy body`\
returns **`Right preparedBody`** with those additions and the declaration in field `28`.

If a selected funding input cannot be resolved, **either call** returns `Left (UnresolvedTopUpInput reserveInput)`.

Both calls take the same **four arguments**, in this order.

| Argument | Role |
| :--- | :--- |
| **1. `history`**<br>(`DepositFormulaHistory`) | Supplies the allocation-time prices for spent inputs and the active price for new outputs. |
| **2. `utxos`**<br>(`IndexedUTxOs DijkstraEra`) | Resolves each spending `TxIn` to its live entry, including a reserve input if selected. Supply it and `history` from the **same ledger snapshot**. |
| **3. `strategy`**<br>(`UTxODepositStrategy (TopTxDepositSettlement DijkstraEra)`) | Specifies the funding and refund choices. `TopUpFromInput reserveInput` offers a `TxIn` for funding. A refund can go to an existing output by `TxIx` or to a new `TxOut` supplied by the builder. |
| **4. `body`**<br>(`TxBody TopTx DijkstraEra`) | The unsigned draft, including its SubTxs. TopTx uses each child’s declaration when present. For a minimum-ADA-only child that omits it, TopTx derives the contribution from its inputs and outputs. |

<details>
<summary>Annotated Haskell · <strong>TopTx function signatures</strong></summary>

```haskell
-- Preview the declaration that the update function would write for the same arguments.
computeNetBalance ::
  DepositFormulaHistory ->
  IndexedUTxOs DijkstraEra ->
  UTxODepositStrategy (TopTxDepositSettlement DijkstraEra) ->
  TxBody TopTx DijkstraEra ->
  Either NetBalanceError TopTx.NetUTxODepositChange

-- Apply the funding and settlement choices and write that declaration into the body.
updateTxBodyWithNetBalance ::
  DepositFormulaHistory ->
  IndexedUTxOs DijkstraEra ->
  UTxODepositStrategy (TopTxDepositSettlement DijkstraEra) ->
  TxBody TopTx DijkstraEra ->
  Either NetBalanceError (TxBody TopTx DijkstraEra)
```

[`computeNetBalance` implementation](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance.hs#L37-L66) · [`updateTxBodyWithNetBalance` implementation](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance.hs#L68-L77) · [Strategy constructors](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance/Strategy.hs#L19-L41)

</details>

![The builder calls updateTxBodyWithNetBalance with history, utxos, strategy and body. On success the prepared body includes the selected funding input or refund output and the resulting declaration.](images/txbody-release-settlement.svg?v=08950de5)

The builder supplies the ADA in any refund output and completes fee and change
balancing. If the final inputs, outputs or refund index change, **recompute the
declaration before signing**.

The declaration includes the historical backing of every selected input and
the active backing of every new output, including funding inputs and refund
outputs. [What the ledger checks at inclusion](#41-what-the-ledger-checks-at-inclusion)

For a **SubTx**, the corresponding calls are `computeSubTxNetBalance` and
`updateSubTxBodyWithNetBalance`.\
They take the same history and UTxO index,
a strategy with `SubTxDepositSettlement DijkstraEra`, and a `TxBody SubTx DijkstraEra`.
The declaration covers that SubTx’s own net and can delegate funding or settlement
to TopTx. [SubTx functions](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance.hs#L79-L110)

**Reading the examples.**

- `Allocate(1.6 ADA)` declares the size of a top-up. Its funding input appears among the ordinary spending inputs as a `TxIn`.
- In `Release(1.6 ADA, output 1)`, the index selects the **second ordinary output of the declaring body**. Its value already includes the refund.
- An explicit **No deposit change** declares that input and output reserves balance. Omitting key `28` makes no declaration. [When a declaration is required](#41-what-the-ledger-checks-at-inclusion)

<a id="33121-toptx-deposit-declaration"></a>

<a id="33131-toptx-deposit-declaration"></a>

<a id="3331-toptx-deposit-declaration"></a>

##### 3.3.1 TopTx deposit declaration

TopTx signs the **net reserve change for the whole batch**. Each SubTx
contributes once, including those that handle their funding or refund locally.
On **Release**, the amount is the batch total. The settlement identifies
which TopTx output receives **TopTx’s share**, if any. That share is the
signed batch net less the signed changes handled locally by SubTxs.

![Example TopTx declarations in pseudocode. Allocate 1.6 ADA, release 1.6 ADA with a refund in TopTx output 1 or with no TopTx refund, or declare no deposit change.](images/toptx-deposit-declaration.svg?v=9cd0bca7)

In each example, the rest of the batch has zero net reserve change.

- **`Allocate(1.6 ADA)`** — Alice’s SubTx needs a 1.6 ADA top-up. If she
  requests funding from TopTx, the operator supplies it. If she funds it
  locally, TopTx still declares 1.6 ADA for the batch. The top-up is paid once.
- **`Release(1.6 ADA, output 1)`** — Alice and Bob each release 0.8 ADA in
  their SubTxs. Alice refunds her share locally. Bob delegates his to TopTx.
  TopTx declares the full **1.6 ADA** and includes **0.8 ADA** in its own output 1.
- **`Release(1.6 ADA, no TopTx refund)`** — Alice’s SubTx releases 1.6 ADA
  and puts the full refund in **its own output 1**. TopTx records the 1.6 ADA
  batch release. Alice’s output already accounts for the entire refund.
- **`No deposit change`** — Alice delegates a 1.6 ADA release to TopTx and
  Bob asks TopTx to fund a 1.6 ADA allocation. Alice’s release covers Bob’s
  top-up, so TopTx declares zero even though both SubTxs declare a change.

<a id="332-haskell-representation"></a>
<a id="342-haskell-representation"></a>

<a id="333-cbor-encoding"></a>
<a id="343-cbor-encoding"></a>

<details>
<summary>Annotated Haskell · <strong>TopTx</strong> declaration and CBOR encoding</summary>

The body field `dtbrNetUTxODepositChange` wraps the optional payload in
`StrictMaybe`. [TopTx body field](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/TxBody.hs#L226) · [TopTx declaration types](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/UTxOs/Deposit/TopTx.hs#L93-L143)

```haskell
-- The amount covers the entire batch, including SubTxs that settle locally.
data NetUTxODepositChange
  = NoUTxODepositChange  -- Explicit zero. Omitting the body field makes no declaration.
  -- How much more the new outputs require than the spent inputs release.
  | AllocateUTxODeposit !StrictlyPositiveCoin
  -- The batch surplus and the settlement choice for TopTx's own share.
  | ReleaseUTxODeposit !StrictlyPositiveCoin !TopTxReleaseSettlement

data TopTxReleaseSettlement
  -- TopTx has no refund to receive. A SubTx may have settled its release locally.
  = NoTopTxSettlement
  -- Zero-based index in TopTx's ordinary outputs. Its value includes TopTx's refund.
  | TopTxSettlementOutput !TxIx
```

```cddl
top_tx_deposit_field = (? 28 : net_utxo_deposit_change)

positive_coin = 1 .. 18446744073709551615
output_index = uint .size 2

net_utxo_deposit_change =
    [0, amount : positive_coin]  ; allocate
  / [1, amount : positive_coin, settlement : top_tx_release_settlement]  ; release
  / [2]  ; zero

top_tx_release_settlement =
    [0]  ; no TopTx settlement
  / [1, output_index]
```

Both decoders reject unknown tags, incorrect array lengths and out-of-range
values. Validation checks that an index selects an existing ordinary output.
[TopTx CDDL](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/cddl/data/dijkstra.cddl#L978-L999) · [TopTx body encoder](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/TxBody.hs#L568)

</details>

<a id="33122-subtx-deposit-declaration"></a>

<a id="33132-subtx-deposit-declaration"></a>

<a id="3332-subtx-deposit-declaration"></a>

##### 3.3.2 SubTx deposit declaration

A SubTx signs **its own net reserve change**. It can fund an allocation
locally or ask TopTx to fund it. For a release, it can name a refund output
of its own or ask TopTx to handle the refund. Even when it **delegates**,
its declaration must specify the full amount.

![Example SubTx declarations in pseudocode. For a 1.6 ADA allocation, fund it locally or request funding from TopTx. For a 1.6 ADA release, select SubTx output 1 or delegate to TopTx. Equal reserves give No deposit change.](images/subtx-deposit-declaration.svg?v=5e11387a)

- **`Allocate(1.6 ADA)`** — Alice’s new outputs require 1.6 ADA more reserve
  than her inputs release. She covers the difference from the spending inputs
  in her SubTx, drawing on her reserve input if needed.
- **`Allocate(1.6 ADA, funding = TopTx)`** — For the same shortfall, Alice
  asks TopTx to supply the 1.6 ADA. Her SubTx can carry just the tokens she
  wants to send. The operator can fund the top-up from its reserve or from
  another SubTx’s delegated release.
- **`Release(1.6 ADA, output 1)`** — Alice’s inputs release 1.6 ADA more
  reserve than her new outputs require. Alice selects **her SubTx’s output 1**
  and signs its final value. That output must contain at least 1.6 ADA.
- **`Release(1.6 ADA, delegate to TopTx)`** — Alice hands the same surplus
  to TopTx for settlement. Her SubTx names no refund output. The operator can
  use the release to cover another SubTx’s top-up or put the remaining refund
  in a TopTx output.
- **`No deposit change`** — Alice spends an output backed by 1.6 ADA and
  creates a successor requiring 1.6 ADA. The released reserve covers the new
  requirement exactly, so she declares zero and has nothing to delegate.

<details>
<summary>Annotated Haskell · <strong>SubTx</strong> declaration and CBOR encoding</summary>

The body field `dstbrNetUTxODepositChange` wraps the optional payload in
`StrictMaybe`. [SubTx body field](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/TxBody.hs#L248) · [SubTx declaration types](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/UTxOs/Deposit/SubTx.hs#L102-L148)

```haskell
-- Each amount is this SubTx's own net. Delegation assigns responsibility for it.
data SubTxNetUTxODepositChange
  = SubTxNoUTxODepositChange  -- Explicit zero, with nothing to fund or settle.
  -- This SubTx funds the shortfall from its own inputs.
  | SubTxAllocateUTxODeposit !StrictlyPositiveCoin
  -- This SubTx declares the shortfall and asks TopTx to fund it.
  | SubTxRequestUTxODepositFromTopTx !StrictlyPositiveCoin
  -- The surplus is known here. The target determines who settles it.
  | SubTxReleaseUTxODeposit !StrictlyPositiveCoin !SubTxReleaseTarget

data SubTxReleaseTarget
  -- Zero-based index in this SubTx's ordinary outputs. Its value includes the refund.
  = SubTxSettlementOutput !TxIx
  -- TopTx accounts for this release together with the other delegated changes.
  | DelegateToTopTx
```

```cddl
sub_tx_deposit_field = (? 28 : sub_tx_net_utxo_deposit_change)

positive_coin = 1 .. 18446744073709551615
output_index = uint .size 2

sub_tx_net_utxo_deposit_change =
    [0, amount : positive_coin]  ; allocate locally
  / [1, amount : positive_coin, target : sub_tx_release_target]  ; release
  / [2, amount : positive_coin]  ; request funding from TopTx
  / [3]  ; zero

sub_tx_release_target =
    [0, output_index]
  / [1]  ; delegate to TopTx
```

[SubTx CDDL](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/cddl/data/dijkstra.cddl#L875-L901) · [SubTx body encoder](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/TxBody.hs#L596)

</details>

<a id="363-recovering-deposits-outside-the-node"></a>
<a id="373-recovering-deposits-outside-the-node"></a>
<a id="345-recovering-deposits-outside-the-node"></a>
<a id="3343-recovering-deposits-outside-the-node"></a>
<a id="341-ledger-data-for-a-draft-transaction"></a>
<a id="342-from-a-local-calculation-to-a-signed-declaration"></a>

<a id="3314-building-transactions-outside-the-node"></a>

<a id="334-building-transactions-outside-the-node"></a>

#### 3.4 Building transactions outside the node

A wallet must calculate a payment’s top-up or refund **before it asks for a
signature**. A service assembling SubTxs needs the batch net to finish its
TopTx. The same requirement applies to any off-chain code that builds a
transaction, including a one-off script.

![Transaction-building software calculates the net before signing. On submission, the node independently checks the declaration against the resolved inputs and the pricing rules at inclusion.](images/off-node-transaction-construction.svg?v=d8561ab8)

`Unspent` is the ledger’s internal representation. A wallet or SDK can use
its own types if it can obtain **two things from the same chain point**,
through a node query or an indexer.

- **For each spending input**, start with the `TxOut` the builder already
  resolves, including the payload data its pricing formula measures. The only
  extra field per input is its **allocation origin** (creation slot or
  migration marker). [How the ledger recovers an input’s reserve](#32-how-the-ledger-recovers-an-inputs-reserve-from-unspent)
- **For all inputs and outputs**, the shared **pricing history**. The baseline
  and dated changes give the formula version and parameters at each input’s
  origin and at the intended inclusion slot for new outputs.

Once both are available, **the entire deposit calculation can be reimplemented
in any language or runtime**. A TypeScript wallet or a Rust service can recover
each input’s reserve, price the new outputs and construct the declaration
locally. Clients need a **common query format** to interpret allocation
origins and pricing history consistently across providers. With the same
draft and funding and refund choices, they must derive the same net, down to
the lovelace, including any funding input or refund output the policy selects.
[Funding and refund policies](#23-choosing-funding-and-refund-policies)

This is why the deposit calculation depends on the **UTxO Storage Cost
Formula**. Today’s minimum-ADA calculation requires the exact CBOR size of
the entire `TxOut`. The companion formula uses fixed allowances, counts
distinct native assets and measures specific fields, including the datum and
reference script. An SDK can therefore implement pricing without reproducing
every detail of the ledger’s output encoding. [UTxO Storage Cost Formula](../CIP-%3F%3F%3F%3F-utxo-cost-formula/README.md)

The signed body carries the declaration and any settlement choice. The input
origins and pricing history stay outside it.

<a id="332-validation-rules"></a>

<a id="332-applying-a-transaction-to-the-ledger-state"></a>

<a id="34-applying-a-transaction-to-the-ledger-state"></a>
<a id="4-applying-a-transaction-to-the-ledger-state"></a>

### 4 From submission to the recorded outcome

A wallet submits a payment of **5 ADA and 1 token B** in a deposit-backed
output. It spends a minimum-ADA input holding the token and 7.2 ADA, of
which 1.6 ADA already backs the input. The new output requires a **2 ADA external
deposit**, so the wallet signs **Allocate 0.4 ADA**. At inclusion, the ledger
checks both amounts. The declaration must match the change in backing, and
the input must fund the payment, the full external deposit and the 0.2 ADA fee.

![The declaration is Allocate 0.4 ADA because 2 ADA of new backing replaces 1.6 ADA of embedded backing. The 7.2 ADA input funds the 5 ADA output value, the full 2 ADA external deposit and the 0.2 ADA fee.](images/ledger-reserve-and-store.svg)

<a id="331-declaration-meaning-and-presence"></a>
<a id="341-declaration-meaning-and-presence"></a>
<a id="3321-declaration-presence-and-exactness"></a>

<a id="3321-checking-the-transaction-against-the-current-state"></a>

<a id="341-checking-the-transaction-against-the-current-state"></a>
<a id="41-checking-the-transaction-against-the-current-state"></a>

#### 4.1 What the ledger checks at inclusion

If the wallet signed **Allocate 2 ADA**, the payment would still balance, but
the ledger would reject it. To check the declaration, the ledger resolves the
ordinary spending inputs against the **UTxO set before the batch**. Each input
contributes its historical reserve, capped at the ADA in its value for a
minimum-ADA input. Each new ordinary output contributes the reserve required
**at inclusion**. Reference-only and collateral-only inputs contribute nothing
to this calculation.

<a id="34-transaction-accounting-and-validation"></a>
<a id="35-transaction-accounting-and-validation"></a>
<a id="313-netting-and-the-transaction-balance"></a>
<a id="341-netting-and-the-transaction-balance"></a>
<a id="351-netting-and-the-transaction-balance"></a>
<a id="333-netting-and-the-transaction-balance"></a>
<a id="3322-netting-and-the-transaction-balance"></a>
<a id="314-release-authority-and-settlement"></a>
<a id="342-release-authority-and-settlement"></a>
<a id="352-release-authority-and-settlement"></a>
<a id="334-release-authority-and-settlement"></a>
<a id="3323-release-authority-and-settlement"></a>

<a id="462-local-release-guarantees"></a>
<a id="62-local-release-guarantees"></a>

- **What must be signed?** Spending or creating a deposit-backed output on the
  ordinary path requires a declaration, even when the net is zero. A body using
  only minimum-ADA outputs may omit it, except that TopTx must declare whenever
  any SubTx declares. Each declaring SubTx signs its own exact net. TopTx signs
  the exact batch net. Two incorrect SubTx declarations still fail if their
  errors cancel. [Declaration rules](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-declarations)
- **Who can recover the reserve?** The input’s spending conditions authorise
  recovery, including when someone else funded the deposit. If a body names a
  refund output, the index must select one of its own ordinary outputs and its
  signed value must contain enough ADA for the assigned refund. A SubTx can
  delegate settlement to TopTx. [Settlement rules](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-settlement)
- **What must be funded?** A minimum-ADA output carries its minimum in its
  value. A deposit-backed output requires its full external deposit even when
  its value contains ADA. On ordinary success, the batch must balance in ADA
  and each native asset. Embedded backing already counts in the values. Only
  the change in external deposits enters the balance separately. [Transaction accounting](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-accounting)

The ledger checks declarations, settlement and output minimums on either script
outcome. When any body supplies a redeemer, collateral must also meet its own
funding and eligibility rules, match any declared total and preserve the native
assets in the return. [Ledger specification — checks by execution path](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx)

<a id="316-script-outcomes-and-collateral"></a>
<a id="343-script-outcomes-and-collateral"></a>
<a id="353-script-outcomes-and-collateral"></a>
<a id="335-script-outcomes-and-collateral"></a>
<a id="3324-script-outcomes-and-collateral"></a>
<a id="353-applying-the-transaction"></a>
<a id="363-applying-the-transaction"></a>

<a id="3322-applying-the-outcome"></a>

<a id="342-applying-the-outcome"></a>
<a id="42-applying-the-outcome"></a>
<a id="42-what-appears-on-chain"></a>

#### 4.2 How execution changes the live UTxO set

The resource the deposit protects is the **live UTxO set**. Every node must
keep each unspent output available for future transactions, including any
inline datum or reference script it carries. Creating more outputs or giving
them larger payloads can tie up more ADA for as long as the node must retain
them. In the prototype, both output forms share one map,
`TxIn → Unspent (TxOut era)`. Each entry records the output and its allocation
origin so the node can recover its original backing on spend.
[Ledger specification — where the node keeps an output](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#state-layout)

An accepted transaction removes the entries it actually spends and inserts
the outputs it actually creates, recording the inclusion slot for each new
entry. These same entries determine the change in **total external deposits**.
The distinction matters for a script payment because its body can describe
both a payment and a collateral return. Suppose `old#0` in the example above
is locked by a Plutus validator and the wallet pledges a separate input,
`col#0`, as collateral. Starting with those two live inputs in the centre,
follow the left branch for success or the right branch for an accepted failure.

![The same two live inputs have two possible outcomes. On success old#0 is spent to create tx#0 and col#0 stays live. On accepted script failure old#0 stays live and col#0 is spent to create the return at tx#1.](images/applied-mixed-output-transaction.svg?v=fa20685c)

<a id="3421-ordinary-success"></a>

##### 4.2.1 Ordinary success

When the validator accepts the spend, the node removes **`old#0`** and
inserts **`tx#0`** at slot 120. The recipient can now spend its **5 ADA and
1 token B**. The collateral input `col#0` stays live with its original deposit.

Replacing one entry with another leaves the **number of live outputs**
unchanged. The old entry carried 1.6 ADA of backing inside its value. Its
replacement requires an external deposit of 2 ADA. The wallet therefore signs
**Allocate 0.4 ADA**, while the node adds the full **2 ADA** to the external
deposit balance and credits **0.2 ADA** to fees.

In a batch, the node applies the ordinary inputs and outputs of each SubTx
and then those of TopTx. Each new output takes its own body’s transaction ID
and output index. Any refund is already in its signed value. A reference input
used only to read an output leaves that entry and its backing in place.
[Ledger specification — applying the selected entries](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#applied-inputs-and-outputs)

<a id="3422-accepted-phase-2-failure"></a>

##### 4.2.2 Accepted phase-2 failure

**How can a balanced payment fail?** Phase 2 runs the Plutus validators.
Suppose the datum on `old#0` identifies order 17 and its validator requires
the redeemer to identify the same order. A redeemer for order 18 fails that
check even though the payment balances and its deposit declaration is exact.
The ledger can accept this outcome when the transaction is marked
**phase-2 invalid** and all other applicable checks pass. A mismatch between
the validity tag and script execution, or a wrong deposit declaration in
phase 1, rejects the transaction entirely. Both inputs then stay live and no
fee or collateral is collected. [Ledger specification — a balanced payment with a failing script](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-accounting-balance-n08)

**Which entries change on an accepted failure?** The node consumes
**`col#0`**. The token and the 1.6 ADA embedded reserve stay in **`old#0`**, and the
proposed payment `tx#0` never enters the map. The optional collateral return
is indexed immediately after TopTx’s ordinary outputs, so **`tx#1`** is the
only new entry here. Without a return, the node would insert no entry. A
failure in a batch selects the shared collateral for the whole batch. None
of its ordinary SubTx outputs is created, and an input used in both spending
roles is consumed once. [Ledger specification — collateral and the live UTxO set](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-utxo-n03)

**One form for every collateral return.** The protocol fixes the form once
for all collateral returns. The prototype design uses a **deposit-backed
output** whenever TopTx includes a return. Transaction-building software
applies that rule automatically when preparing the body for signing. The
caller has no return-form setting.

Here `col#0` holds **5 ADA** in its value and releases a **2 ADA external
deposit**. On accepted failure, **4 ADA** goes into the value of `tx#1` and
**1 ADA** covers the collateral fee. The new return also requires a **2 ADA
deposit** at the active price, which the released deposit covers exactly.

**Design alternative.** The protocol could instead require **every collateral
return to be a minimum-ADA output**. If 4 ADA covers the active minimum,
the same return would tie up **4 ADA** in total instead of **6 ADA**. The
trade-off in this example is what happens to the released deposit. All **2 ADA**
would go to fees, bringing the fee credit to **3 ADA**. Under the prototype’s
rule, those 2 ADA remain recoverable when `tx#1` is spent.
[Ledger specification — collateral funding](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-collateral-funding) · [Fee credit on failure](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-fees-p02)

![Comparison of two fixed protocol rules for a 4 ADA return. The prototype design always creates a deposit-backed return: 2 ADA backs the return and fees total 1 ADA. Requiring minimum-ADA returns instead would direct the released 2 ADA to fees, for a total of 3 ADA in this example.](images/applied-collateral-outcome.svg?v=00176c2e)

<a id="32-deposit-model"></a>
<a id="35-output-representation-and-ledger-application"></a>
<a id="36-output-representation-and-ledger-application"></a>
<a id="36-deterministic-deposit-recovery"></a>
<a id="37-deterministic-deposit-recovery"></a>
<a id="34-ledger-state-and-deposit-lifecycle"></a>
<a id="333-ledger-state-and-transaction-application"></a>

<a id="333-deposit-accounting-across-blocks"></a>

<a id="35-deposit-accounting-across-blocks"></a>

<a id="5-deposit-accounting-across-blocks"></a>
<a id="5-tracking-a-deposit-across-blocks"></a>

### 5 Tracking UTxO reserves across blocks

After the payment succeeds at slot 120, a wallet sees **5 ADA and 1 token B**
in `tx#0`. When it selects that output as an input, its **`Unspent` entry**
and the shared pricing history tell it how much backing the spend releases
and how much ADA is available for the application. A wallet can total those
amounts for its selected inputs, and an indexer can do so for every entry
in the live UTxO set.

<a id="324-allocation-history-and-the-store-invariant"></a>
<a id="362-formula-history-and-the-store-invariant"></a>
<a id="372-formula-history-and-the-store-invariant"></a>
<a id="3332-utxostore-and-deposit-accounting"></a>
<a id="3331-utxostore-and-deposit-accounting"></a>
<a id="343-applying-transactions-and-maintaining-the-store-invariant"></a>
<a id="3333-applying-transactions-and-maintaining-the-store-invariant"></a>

<a id="3331-the-external-deposit-balance"></a>

<a id="351-the-external-deposit-balance"></a>

<a id="51-the-external-deposit-balance"></a>
<a id="51-reading-a-live-output-and-its-deposit"></a>

#### 5.1 What the accounting state stores

In the Dijkstra prototype, `LedgerState` contains an **`AccountingState`**.
Its `UTxOStore` holds the live outputs and their backing. Fees, certificate
and governance deposits, instant stake and donations sit alongside the Store
in the accounting state. [Ledger specification — state layout](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#state-layout)

![AccountingState contains a UTxOStore with a live allocation map, shared pricing history and total external deposits. Fees, certificate and governance deposits, instant stake and donations are separate fields.](images/utxo-accounting-state.svg?v=b2e6b6b5)

A Dijkstra snapshot persists three things in the Store.

- **`allocations`** maps each live `TxIn` to its accepted output and allocation
  origin. For `tx#0` the origin is slot 120. An output imported at the hard
  fork carries a migration marker.
- **`depositFormulaHistory`** records the baseline formula version and
  parameters, then each change with its effective slot. All entries share this
  history. The migration marker selects the baseline. A creation slot selects
  the rules in force at that slot.
- **`totalDepositAmount`** records the **total ADA held in external deposits**
  across the live set. The node adds external deposits when it
  creates entries and subtracts their original amounts when it spends them.
  This gives the node the external balance directly at each chain point.

Looking up `tx#0` gives the wallet the accepted output and its allocation
slot, 120. Applying the pricing rules for that slot to the output recovers
its **2 ADA external deposit**. The output’s spending conditions govern who
can release it. [Ledger specification — Store and per-input queries](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/domain-model.md#section-1-1)

#### 5.2 From one input’s reserve to total UTxO backing

**What can a wallet learn from one input?** For a **minimum-ADA output**
holding 5 ADA with a historical minimum of 1.6 ADA, the wallet can identify
both the **1.6 ADA embedded reserve** and the **3.4 ADA above the minimum**.
If an imported output holds less than its fork-baseline requirement, all
its ADA counts as reserve and its application ADA is zero.

For a **deposit-backed output**, the entire signed value is available to the
application. Spending `tx#0` supplies its **5 ADA and 1 token B** and also
releases its **2 ADA deposit**. In the prototype, `computeDeposit` gives the
reserve credited on spend and `computeApplicationAssets` gives the application
ADA and native assets for the same entry. [Per-input calculations](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/UTxOs/Unspent.hs#L26-L55)

Suppose the wallet selects these **three live inputs** at the same chain
point. The table shows only their ADA.

| Live entry | ADA in `Value` | Requirement at origin | Embedded reserve | External deposit | Application ADA |
| --- | ---: | ---: | ---: | ---: | ---: |
| `tx#0` · deposit-backed | 5 | 2 | 0 | 2 | 5 |
| `wallet#1` · minimum-ADA | 5 | 1.6 | 1.6 | 0 | 3.4 |
| `legacy#0` · imported minimum-ADA | 1.5 | 2 | 1.5 | 0 | 0 |
| **Selected totals** | **11.5** | | **3.1** | **2** | **8.4** |

Together these entries account for **13.5 ADA**. Of that, **8.4 ADA** is
application ADA and **5.1 ADA** is backing (3.1 embedded + 2 external).

**How much deposit is left to refund?** That depends on the outputs the
transaction creates. If all its new outputs, including any refund output,
require **4.1 ADA** of backing, the **5.1 ADA** credited by these inputs
leaves a **1 ADA surplus**. The transaction declares **Release 1 ADA**.

An indexer can apply the same calculation to **the full live UTxO set**.
It sums the historical reserves of the live minimum-ADA entries and adds
`totalDepositAmount` from the same chain point. Of these two subtotals, only
the external one is stored. For a smaller selection, both subtotals must
cover only those references. [Ledger specification — external balance invariant](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-balance-n02) · [How the ledger sums selected input reserves](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/Rules/DepositStore/Accounting.hs#L175-L192)

<a id="333-encoding-validation-and-versioning"></a>
<a id="375-encoding-validation-and-persistence"></a>
<a id="385-encoding-validation-and-persistence"></a>
<a id="346-persistence-rollback-and-replay"></a>

<a id="3334-persistence-rollback-and-replay"></a>

<a id="3333-persistence-rollback-and-replay"></a>

<a id="353-persistence-rollback-and-replay"></a>

<a id="53-persistence-rollback-and-replay"></a>
<a id="54-restoring-a-consistent-view-after-rollback"></a>

#### 5.3 Restoring a consistent view after rollback

Suppose a rollback undoes the payment at slot 120. The indexer removes
`tx#0`, subtracts its **2 ADA external deposit** from the total and restores
`old#0` with its original **1.6 ADA embedded reserve**. If the rollback also
undoes a price change, the indexer restores the pricing history at the target
chain point.

A snapshot must restore the **live entries, pricing history and external
balance at the same chain point**. The prototype decoder recomputes external
deposits from the restored entries and history and rejects a snapshot if
their sum differs from the persisted total. The same entries and history
also reproduce each embedded reserve. [Store snapshot decoder](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-core/src/Cardano/Ledger/State/Accounting/UTxOs/Store/Internals.hs#L253-L269)

Replaying the same blocks must reproduce the same balances on both the
ordinary and collateral paths. [Ledger specification — snapshot restoration tests](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-recovery) · [Consensus rollback and replay requirement](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-recovery-n02)

<a id="373-formula-and-parameter-changes"></a>
<a id="383-formula-and-parameter-changes"></a>
<a id="344-formula-and-parameter-changes"></a>

<a id="3342-formula-and-parameter-changes"></a>

<a id="3332-activating-a-pricing-change"></a>

<a id="352-activating-a-pricing-change"></a>

<a id="52-activating-a-pricing-change"></a>
<a id="52-spending-an-output-after-a-price-change"></a>
<a id="53-spending-an-output-after-a-price-change"></a>

<a id="53-querying-and-spending-an-output-across-a-price-change"></a>

### 6 New Formula Activation

#### 6.1 When the new price takes effect

The hard fork establishes the **initial pricing baseline**. The prototype
uses that formula and byte price for both imported outputs and the first new
allocations. Each subsequent change records an **effective slot**, a formula
version and its parameters. A protocol byte-price update takes effect at the
first slot of the new epoch and keeps the current formula version. A new
formula version can also take effect with the same byte price.
[Ledger specification — historical pricing](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/domain-model.md#ds-pricing-history)

Suppose the change raises the deposit for an output like `tx#0` from **2 ADA
to 2.4 ADA**. Querying `tx#0` after activation still gives **2 ADA** because
its allocation slot selects its original price. Activation alone changes
neither the reserves on live outputs nor the total external deposits. The
**2.4 ADA** price applies to an identical output created from the effective
slot onward.

#### 6.2 Transactions signed before activation

A wallet plans to spend `tx#0` and recreate its **5 ADA and 1 token B** in an
identical successor. Assume its fee input and change contribute zero net reserve.

| Inclusion slot | Released by `tx#0` | Required for the successor | Required declaration |
| --- | ---: | ---: | --- |
| Before activation | 2 ADA | 2 ADA | **No deposit change** |
| From activation onward | 2 ADA | 2.4 ADA | **Allocate 0.4 ADA** |

If the wallet signed **No deposit change** and the transaction reaches
validation after activation, the ledger rejects it and `tx#0` remains unspent.
The declaration must match the net reserve change **at inclusion**. To make
the same payment, the wallet funds the extra **0.4 ADA**, updates the
declaration and signs the revised body. [Ledger specification — exact TopTx declaration](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-exactness-toptx)

Wallets already handle this timing issue for **transaction fees**. A fee that
met the minimum at signing can fall below it when fee parameters change.
For a known activation slot, a wallet can set the old-price transaction to
expire at that slot. If the payment is still pending, it can rebuild using
the new rules and collect fresh signatures. [Ledger validity interval and minimum fee checks](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/Rules/Utxo.hs#L365-L390)

<a id="33-lifecycle-and-compatibility"></a>
<a id="37-migration-and-compatibility"></a>
<a id="38-migration-and-compatibility"></a>

<a id="35-activation-and-compatibility"></a>

<a id="34-activation-and-compatibility"></a>

<a id="36-activation-and-compatibility"></a>

<a id="6-activation-and-compatibility"></a>

### 7 Compatibility

<a id="331-parameter-changes-and-migration"></a>
<a id="371-activation-and-the-migration-baseline"></a>
<a id="381-activation-and-the-migration-baseline"></a>

<a id="351-activation-and-the-migration-baseline"></a>

<a id="341-activation-and-the-migration-baseline"></a>

<a id="361-activation-and-the-migration-baseline"></a>

<a id="372-legacy-outputs-below-the-new-minimum"></a>
<a id="382-legacy-outputs-below-the-new-minimum"></a>

<a id="352-legacy-outputs-below-the-new-minimum"></a>

<a id="342-legacy-outputs-below-the-new-minimum"></a>

<a id="362-legacy-outputs-below-the-new-minimum"></a>

<a id="61-activation-and-the-migration-baseline"></a>
<a id="62-legacy-outputs-below-the-new-minimum"></a>

#### 7.1 Spending outputs imported at the hard fork

A wallet can still spend a pre-fork output using the **same input
reference**. The ledger preserves its address, value, datum and reference
script. The `AtStoreMigration` marker selects the fork baseline whenever
that input is spent. All imported ADA stays in output values, so the external
deposit total starts at zero. A builder
can spend that input alongside deposit-backed inputs and choose either form
for each new ordinary output. [Ledger specification — hard-fork translation](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-translation)

**An output below the baseline minimum remains spendable.** The embedded
reserve is capped at the ADA it holds. Its full value enters the transaction
balance once. A successor must meet its own requirement at inclusion.
[Worked example — funding the shortfall](#262-spending-an-input-below-the-minimum)

<a id="376-script-contexts-and-legacy-plutus-mode"></a>
<a id="386-script-contexts-and-legacy-plutus-mode"></a>

<a id="353-script-contexts-and-existing-contracts"></a>

<a id="343-script-contexts-and-existing-contracts"></a>

<a id="363-script-contexts-and-existing-contracts"></a>

<a id="63-script-contexts-and-existing-contracts"></a>

#### 7.2 Script contexts and existing contracts

A contract that checks the exact ADA in a minimum-ADA output sees its
**full value**, including embedded backing. For a deposit-backed output,
the prototype exposes **application value** to Plutus V4. Support for that
output form in V1–V3 script contexts remains open.
[Script-visible output value](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/domain-model.md#script-visible-output-value)

In legacy Plutus mode, TopTx must also balance on its own. This check includes
the change in its own external deposits and the signed amounts delegated by
SubTxs. Each body already accounts for embedded ADA through its own inputs
and outputs.

<a id="332-stake-voting-and-monetary-conservation"></a>
<a id="374-stake-voting-and-monetary-conservation"></a>
<a id="384-stake-voting-and-monetary-conservation"></a>

<a id="354-stake-voting-and-monetary-conservation"></a>

<a id="344-stake-voting-and-monetary-conservation"></a>

<a id="364-stake-voting-and-monetary-conservation"></a>

<a id="64-stake-voting-and-monetary-conservation"></a>

#### 7.3 Stake and voting weight

**The prototype excludes external deposits from stake and voting weight.** It applies existing eligibility and delegation rules to the ADA in an output’s value. For example, an eligible minimum-ADA output carrying 10 ADA contributes 10 ADA. An eligible deposit-backed output carrying 8 ADA with a separate 2 ADA deposit contributes 8 ADA. [Stake contribution by output form](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/derived-distributions.md#ds-stake) · [Voting weight](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/derived-distributions.md#ds-voting)

The protocol could instead attribute each live external deposit to its output’s staking credential for either distribution. All nodes must apply the same policy for each distribution. Under either policy, the ledger counts the ADA held in external deposits exactly once in the monetary supply. [ADA conservation](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-conservation)

<a id="4-rationale-how-does-this-cip-achieve-its-goals"></a>

## Rationale: How does this CIP achieve its goals?

<a id="41-application-value-and-funding"></a>

### 1 Application value and funding

The two output forms offer different accounting and capital trade-offs. For a
payment of `C` application ADA and requirement `F`, a deposit-backed output commits
`C + F`. A minimum-ADA output commits at least `max(C, F)`, allowing the same ADA
to satisfy both purposes. Builders can choose the form appropriate to each ordinary output.

The full external deposit makes application value explicit, including token-only
and asset-free outputs. The existing value representation supports applications
that rely on ADA inside their outputs.

Netting follows the transaction's atomic update of the live UTxO set. The ledger
can settle one aggregate funding change while preserving an individual allocation
and spending authority for each output. Delegation extends that funding
coordination to independently authored SubTxs. The complete balance still includes
fees, change and all other applicable ledger effects.

<a id="42-evaluation-against-the-cps-use-cases"></a>

### 2 Evaluation against the CPS use cases

| CPS use case | Effect of the proposal | Remaining burden or trade-off |
| --- | --- | --- |
| Frozen wallet | Released backing can fund replacement deposits. TopTx can sponsor a SubTx's fee and additional deposit funding. | An equally priced replacement frees no spare ADA for the fee. A sponsor or another ADA source is still needed. |
| Payment below minUTxO | A `DepositBackedTxOut` can contain an exact small ADA payment or tokens with zero application ADA. | The full external deposit and transaction fees require funding. |
| Funding recipient-controlled ADA | Funding may be consolidated or delegated to TopTx. The deposit is held outside the application's value. | Release authority still follows the output. The original funder gains no separate claim. |
| Non-staking application state | Application value is represented independently of backing. | Under the prototype policy, ADA moved from an eligible output value into an external deposit ceases to carry stake or voting weight while held there. |
| Construction and change balancing | The formula CIP removes the dependency on the output’s ADA amount. The builder reviews one net change in backing for the batch. | Funding inputs and change outputs can affect that net. Builders also balance fees and the ADA moving into or out of the external Store. |
| High fan-out distribution | The batch funds the net sum, with optional sponsorship. | Each new output still incurs its full requirement. More outputs can require more capital. |
| Successor-output top-up | The old historical deposit is available toward the new active-price requirement. | Any shortfall needs funding. A decrease releases value through the spending transaction's settlement rules. |

A quantitative comparison uses representative transactions and wallet workflows.
It must count application ADA, external deposits and fees without double counting
ADA that serves both roles in a min-ADA output. [CPS evaluation requirements](../CPS-0037/README.md#evaluation-requirements)

<a id="43-responses-to-the-cps-questions"></a>

### 3 Responses to the CPS questions

1. **Parameter changes and beneficiaries.** Existing deposits retain their original
   amount. A successor pays the current requirement. The transaction funds an
   increase and disposes of a release under its spending and settlement rules.
   Historical funding creates no independent entitlement.
2. **Existing validators.** **TODO:** Specify the script-context projection for
   each supported Plutus version and its effect on validators that check exact
   ADA amounts. See [the author TODO](#61-plutus-compatibility).
3. **Uneconomic cleanup.** Spending releases the historical backing. The proposal
   adds no expiry or extra cleanup reward. An output can remain indefinitely when
   consumption costs exceed the value its controller can recover.
4. **Deposit organisation.** The ledger maintains an individual allocation per
   output and an exact aggregate total. Transaction-level funding can be shared,
   while output spending authority remains individual.
5. **Exact allocation and encoding boundaries.** The required formula CIP calculates
   the full requirement independently of application ADA and the outer output encoding.
   The Store holds the exact sum of the external deposits. A minimum-ADA
   output’s embedded backing counts toward the signed change in backing and
   enters ordinary ADA conservation once, through its value.

<a id="44-alternatives-considered"></a>

### 4 Alternatives considered

| Alternative | Reason for evaluating it | Trade-off motivating the proposal |
| --- | --- | --- |
| Adopt UTxO Storage Cost Formula alone | Simplify the minimum calculation while retaining minimum-ADA TxOuts | This CIP builds on that calculation to add deposit-backed values and explicit netting. |
| Application/deposit split inside each output | Make the two roles explicit within the transferred output | A size formula over that same encoded split can create a fixed-point allocation problem. Deposit representation and pricing must be evaluated together. |
| External deposit for only the shortfall `max(0, requirement − applicationADA)` | Preserve overlap between intended ADA and backing, as an alternative representation | Application ADA affects the external amount and requires its own lifecycle and compatibility analysis. The proposal uses a full external deposit for the new form. |
| Funder-controlled account obligation | Give the funder a continuing claim while state occupies capacity | Account ownership, authorisation, shared obligations and independently spendable outputs require additional rules. |
| Redistribute backing across outputs | Relax each output's minimum while retaining ADA in output values | Allocation and recovery rights still need definition, and backing continues to participate in the transferred values. |

The full external deposit separates the backing requirement from application ADA.
This gives each new output an exact, individual allocation while
allowing transactions to net their funding. The capital and implementation costs
of this choice are described below.

<a id="45-resource-protection-and-implementation-costs"></a>

### 5 Resource protection and implementation costs

The Store invariant ensures that the recorded external obligations have exactly
matching ADA backing. Economic protection additionally depends on the rate and
coefficients specified by [UTxO Storage Cost Formula](../CIP-????-utxo-cost-formula/README.md).
Calibration belongs to that proposal. Integrating deposit-backed outputs must also
account for the resources introduced here: allocation metadata, indexes and
historical-price lookup and storage. A passing accounting test does not establish
that the selected pricing covers those costs.

The protocol can represent a zero rate. Zero-priced outputs still require
allocation records and explicit declarations where applicable. Such a rate must
be assessed against the intended economic protection.

Each live output retains an allocation origin, while common formula versions
and parameters are recorded once per history interval. Recovering an amount
requires both the corresponding formula implementation and its input measurements.
Implementers must assess state size, lookups, snapshot costs and retention of
obsolete formula intervals. Any history compaction must preserve every live
allocation's exact historical amount.

Conservation includes the Store once. Ordinary and collateral effects must use the
selected execution path, and all consumers of ledger state must agree on the two
output forms. Release authority, price changes and migration are therefore part
of the validation and compatibility contract.

<a id="46-author-todos"></a>

### 6 Author TODOs

> **TODO — Editorial:** Resolve the items below, incorporate the resulting rules
> and rationale into the appropriate sections, and remove this author checklist
> before publication.

<a id="461-plutus-compatibility"></a>

#### 6.1 Plutus compatibility

> **TODO:** Specify the context projection for each supported Plutus version,
> including application value, backing, transaction-level deposit information and
> validators that check exact ADA amounts. Complete the `DepositBackedTxOut`
> translations for V1–V3 and verify the agreed contract for each version.
>
> [Plutus support by version](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/verification.md#plutus-context-status) · [V4 integration fixture](https://github.com/willjgould/cardano-minutxo-integration/commit/d2300267436d4cc6a4cb2dbc7898b9f98787192b)

<a id="463-pricing-and-activation"></a>

<a id="63-pricing-and-activation"></a>

#### 6.2 Pricing and activation

> **TODO:** Record the assigned number of the required UTxO Storage Cost Formula CIP and
> coordinate the two proposals' activation versions. Confirm that its calibration
> covers the allocation metadata and storage introduced here. Select the initial
> history baseline if the formula has evolved before the deposit fork. The
> prototype uses one initial formula for imported entries and the first new
> allocations. A separate migration pricing policy would require its own rule.
>
> **TODO — Formula integration:** Update the prototype's fixed 250-byte
> allowance to use the companion proposal's 193-byte allowance plus measured
> address bytes. Add the address measurement to the shared formula inputs and
> verify both output forms and historical recovery with those measurements.
>
> **TODO:** Verify the pricing-boundary workflow for batches of independently
> signed SubTxs. Document which bodies need fresh signatures when repricing
> changes a delegated amount or its settlement.

<a id="464-declarations"></a>

<a id="64-declarations"></a>

#### 6.3 Declarations

> **TODO:** Document why the builder signs the numeric net alongside its funding
> or refund choice. The ledger rules specify when a body may omit key `28` and
> how the batch accounts for an undeclared SubTx. [Declaration requirements](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-declarations-requirements) · [Attribution to TopTx](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-accounting-attribution)

<a id="465-stake-and-voting"></a>

<a id="65-stake-and-voting"></a>

#### 6.4 Stake and voting

> **TODO:** Compare the effect on a wallet’s capital efficiency when an external deposit is excluded from stake or attributed to its output’s staking credential.

<a id="466-integration-and-validation"></a>

<a id="66-integration-and-validation"></a>

#### 6.5 Integration and validation

- [ ] Verify mixed-form declaration and settlement checks on accepted phase-2
      failure against the independent collateral balance.

> **TODO:** Incorporate evidence for wallet/indexer handling, private-network flows
> and rollback/replay. Check that persisted-history validation enforces the same
> contract as formula activation, including version-downgrade rejection. Cover
> shared-collateral cases and document the interoperable snapshot format. Specify
> the common query representation for allocation origins and formula history so
> independent implementations can reproduce the historical deposit calculation.
>
> [Existing ledger test coverage](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/verification.md#current-implementation-status) · [Consensus rollback coverage gap](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/ledger-effects.md#ds-state-recovery-n02)

<a id="5-path-to-active"></a>

## Path to Active

<a id="51-acceptance-criteria"></a>

### 1 Acceptance Criteria

- [x] Publish the motivating problem statement as CPS-0037 and link it from the CIP.
- [ ] Complete author and domain review of the rules, alternatives, local settlement
      guarantee, Plutus projections, transaction encoding and activation policy.
- [ ] Adopt the required [UTxO Storage Cost Formula](../CIP-????-utxo-cost-formula/README.md)
      before or with this proposal, including its resource-pricing validation.
- [ ] Establish the conservation, exact-backing and historical-release properties
      in the formal specification and assess the additional allocation and history
      costs against the pricing supplied by the formula CIP.
- [ ] Demonstrate interoperable encoding, validation, migration, snapshots and
      rollback/replay against independent expectations.
- [ ] Verify the adopted treatment of external deposits for stake and voting after
      ordinary execution, collateral processing and at snapshot boundaries. Check
      that eligible ADA receives its weight once. Record results against the final implementation
      revision. [Distribution rules](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/derived-distributions.md) · [Verification record](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/verification.md#current-implementation-status)
- [ ] Complete the dedicated collateral verification against the final implementation revision.
- [ ] Demonstrate native-token transfers, small ADA payments, continuing-script
      transitions and sponsored SubTxs across the wallet, builder and node stack
      on a private network, including accepted script failure and transactions
      constructed across formula or parameter activation boundaries.
- [ ] Document the operational impact on node implementations, cardano-api,
      wallets, hardware wallets, indexers and explorers.
- [ ] Deploy compatible node and downstream implementations and activate the
      proposal through the agreed protocol transition.

<a id="52-implementation-plan"></a>

### 2 Implementation Plan

The Haskell Ledger implementation in PR #3 provides executable rules for output
forms, declarations, external deposit accounting, authority, settlement, collateral,
historical deposits and state transitions. Its transaction-construction API
provides funding and settlement strategies and transaction-body update functions.
Links to the ledger rules, source code and API signatures follow the latest commit
on the prototype’s `v2-minutxo` branch. Its pricing formula uses a fixed base. Integrating the companion formula also requires
its address-size term.
[Ledger implementation](https://github.com/nhenin/cardano-ledger-specs/pull/3)

Deployment requires support across the Ledger, node, cardano-api, transaction
builders, wallets and indexers. Integrated validation must cover native-token
transfers, small ADA payments, continuing-script transitions and sponsored SubTxs,
including accepted script failure, parameter changes, snapshots and rollback.
Results must identify the implementation revision and protocol parameters used.

Activation follows the acceptance criteria above and the supporting era's
protocol transition, with UTxO Storage Cost Formula active no later than this proposal.
Nodes and downstream tools must agree on the output forms,
deposit declarations, state representation and script-context contract before
activation.

<a id="53-reference-transaction-construction-api"></a>

### 3 Reference transaction-construction API

<a id="38-reference-transaction-construction-api"></a>
<a id="381-funding-and-settlement-strategies"></a>
<a id="382-preparing-transaction-bodies"></a>
<a id="383-constructing-declarations"></a>

The reference API takes the builder’s funding and refund choices and returns
the signed change in reserve across minimum-ADA and deposit-backed outputs.

| Choice | Reference API |
| --- | --- |
| Use funding already included in the body | `TopUpAlreadyIncluded` |
| Offer an ordinary input for additional funding | `TopUpFromInput TxIn` |
| Select a TopTx refund output | `TopTxRefundToExistingOutput TxIx` or `TopTxRefundToNewOutput TxOut` |
| Select a SubTx refund output | `SubTxRefundToExistingOutput TxIx` or `SubTxRefundToNewOutput TxOut` |
| Delegate a SubTx's allocation or release | `DelegateDepositToTopTx` |

The update functions take input entries and formula history from the same ledger
snapshot, apply the strategy, and return a body with its declaration.

<details>
<summary>Annotated Haskell · <strong>TopTx and SubTx construction functions</strong></summary>

```haskell
-- Prepare the batch declaration, including the backing of every SubTx.
updateTxBodyWithNetBalance ::
  DepositFormulaHistory ->    -- Historical prices for inputs and active prices for outputs.
  IndexedUTxOs DijkstraEra -> -- Resolves spending inputs and candidate funding inputs.
  -- Choose how TopTx funds a shortfall or settles its share of a release.
  UTxODepositStrategy (TopTxDepositSettlement DijkstraEra) ->
  TxBody TopTx DijkstraEra -> -- Draft containing the prepared SubTxs.
  -- An error, or the updated body to finish balancing before signing.
  Either NetBalanceError (TxBody TopTx DijkstraEra)

-- Prepare this SubTx before passing it to the TopTx builder.
updateSubTxBodyWithNetBalance ::
  DepositFormulaHistory ->
  IndexedUTxOs DijkstraEra ->
  -- Fund or settle locally, or delegate that responsibility to TopTx.
  UTxODepositStrategy (SubTxDepositSettlement DijkstraEra) ->
  TxBody SubTx DijkstraEra ->
  -- On success, the body carries this SubTx's amount and its local or delegated choice.
  Either NetBalanceError (TxBody SubTx DijkstraEra)
```

</details>

[`computeNetBalance`](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance.hs#L37-L66) and `computeSubTxNetBalance` take the corresponding inputs and
return the declaration payload. Their calculations include any input or output
additions selected by the strategy. [`updateTxBodyWithNetBalance`](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance.hs#L68-L77) and
`updateSubTxBodyWithNetBalance` also apply those additions and write the declaration
into the returned body.

Prepare the SubTxs before TopTx. `computeNetBalance` combines TopTx’s own
contribution with each SubTx’s signed change. For a minimum-ADA-only SubTx
that omits the declaration, it derives the contribution from the child’s inputs
and outputs. That amount still counts in the batch net and in TopTx’s share.
The ledger independently recalculates each contribution at inclusion.

Refund outputs are inserted with the ADA values supplied by the transaction
builder. The active backing of a new refund output of either form enters the
net. Adding a TopTx refund output must leave both the batch and TopTx’s share
in release. Adding a local SubTx refund output must leave that SubTx’s own
contribution in release. Rebalancing a body that already contains the refund
uses the existing-output strategy.

The transaction builder sets the selected output's serialized ADA to cover the
body's local release amount and completes change and fee balancing. For TopTx, that amount
is its attributed release. For a SubTx, it is its own release. Subsequent changes
to the body can require another calculation.
[Builder API](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance.hs) · [Strategy types and behavior](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/libs/cardano-ledger-api/src/Cardano/Ledger/Api/Tx/Body/DepositBalance/Strategy.hs)

<a id="6-references"></a>

## References

- [CIP-0001 and the CIP process](https://cips.cardano.org/cip/CIP-0001)
- [CPS-0037 and its cited prior work](https://github.com/cardano-foundation/CIPs/tree/master/CPS-0037)
- [UTxO Storage Cost Formula — required companion CIP](../CIP-????-utxo-cost-formula/README.md)
- [Ledger specification for minimum-ADA and deposit-backed outputs](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/README.md)
- [TopTx and SubTx deposit declarations](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/chapters/transaction-rules.md#ds-tx-declarations)
- [Verification record for the Dijkstra UTxO deposit rules](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/docs/dijkstra-utxo-deposit-rules/verification.md)
- [Formula implementation](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/UTxOs/Deposit/Formula.hs)
- [Dijkstra transaction accounting](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/src/Cardano/Ledger/Dijkstra/Rules/DepositStore/Accounting.hs)
- [Dijkstra transaction CDDL](https://github.com/nhenin/cardano-ledger-specs/blob/v2-minutxo/eras/dijkstra/impl/cddl/data/dijkstra.cddl)

<a id="7-copyright"></a>

## Copyright

This CIP is licensed under
[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode).
