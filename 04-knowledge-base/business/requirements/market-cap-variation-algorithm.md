---
title: Market Cap Percentage Variation Algorithm
type: feature-specification
status: draft
priority: medium
created: 2025-04-17
date: 2025-10-20
updated: 2025-10-20
tags: [trading, algorithm, market-cap, automated-trading]
related:
  - "[[trading-methods]]"
  - "[[platform-vision-requirements]]"
---

# Market Cap Percentage Variation Algorithm

## Overview

As Cooking.gg evolves, it aims at implementing new algorithms that enable traders different mechanisms to generate profit. This feature focuses on leveraging the variation percentage on the market capitalization of a given token through time.

## Order Parameters

### Required Parameters

In order to open a position of this caliber, the user will define:

- **Side**: BUY or SELL
- **Order Size**: Amount to be executed per transaction
- **Total Amount**: Total amount to be executed until completion
- **Variation Percentage**: Percentage variation on market capitalization that triggers execution

### Optional Parameters

Along side these parameters, the user can choose to:

- Open the order with the execution of a transaction (BUY or SELL) at the current market cap or not
- Only execute when the market capitalization variation is positive, negative or either

## Order Management

It is expected for this order to have the ability to be:
- **Paused**: Temporarily stop execution
- **Resumed**: Continue execution after pause
- **Cancelled**: Permanently stop and close the order

## Lifecycle Examples

### Example 1: No Initial Execution, Absolute Variation

**Configuration**:
- Buy 0.2 SOL of ROOSTER token per purchase
- Trigger: Every 10% MC variation
- Total target: 1 SOL

**Timeline**:

**T0 - No initial execution, absolute variation**
- ROOSTER MC = $3,670 USD

**T1 - (+10%) MC variation**
- ROOSTER MC = $4,037 USD
- BUY = 49,474.335188 ROOSTER = 0.2 SOL

**T2 - (-10%) MC variation**
- ROOSTER MC = $3,633 USD
- BUY = 54,971.483542 ROOSTER = 0.2 SOL
- TOTAL ACQUIRED = 104,445.81873 ROOSTER = 0.4 SOL

**T3 - User Pauses Cycle**
- No execution

**T4 - User Pauses Cycle**
- No execution

**Continues until completion of 1 SOL**

### Example 2: With Initial Execution, Only Positive Variation

**Configuration**:
- Initial execution: Yes
- Direction filter: Positive variation only

**Timeline**:

**T0 - With initial execution, only positive variation**
- ROOSTER MC = $3,670 USD
- BUY = 54,421.76870748 ROOSTER = 0.2 SOL

**T1 - (+10%) MC variation**
- ROOSTER MC = $4,037 USD
- BUY = 49,474.335188 ROOSTER = 0.2 SOL
- TOTAL ACQUIRED = 103,896.10389548 ROOSTER = 0.4 SOL

**T2 - (-10%) MC variation**
- No execution (negative variation filtered out)

**T3 - User Pauses Cycle**
- No execution

**T4 - User Pauses Cycle**
- No purchase, only for initial

**Continues until completion of 1 SOL**

## Technical Considerations

- Order tracking must persist through pause/resume cycles
- Accurate market cap monitoring is required
- Real-time variation calculation needed
- Transaction execution must handle network delays

## Use Cases

- Automated accumulation during volatility
- Risk-managed position building
- Market-neutral trading strategies
- Volatility-based dollar-cost averaging

---

**Status**: Draft specification
**Next Steps**: Technical feasibility assessment, UI/UX design, implementation planning
