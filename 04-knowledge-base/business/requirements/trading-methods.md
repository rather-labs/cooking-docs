---
title: Trading Methods Specification
type: feature-specification
status: in-development
priority: critical
created: 2025-07-21
date: 2025-10-22
updated: 2025-10-22
tags: [trading, orders, market, limit, dca, twap, vwap, custom-orders]
related:
  - "[[trading-methods-ux-design]]"
  - "[[limit-orders-methodology]]"
  - "[[platform-vision-requirements]]"
---

# Cooking Trading Methods Guide

## Overview

Cooking supports six distinct trading methods, each designed for different trading strategies and market conditions. All methods support both BUY and SELL operations and share common parameters while offering unique configuration options.

---

## General Parameters

All trading methods require these mandatory parameters:

### Direction
All transactions can be either a purchase or a sale: **BUY** or **SELL**.

### Order Size
Total amount to trade (expressed in SOL for purchases, in token for sales).
- If the transaction is a **purchase**: expressed in **SOL**
- If the transaction is a **sale**: expressed in the **selected token**
- Always expressed numerically as an integer greater than zero

### Gas Fee
The cost incurred from broadcasting the transaction into the blockchain. Varies depending on network congestion.

### Priority Fee
Fee paid directly to block validators for better transaction positioning.
- Default: 0.008 SOL
- Works as an incentive to get a better position of the trade on the block when broadcasting to the chain

### Slippage
Maximum acceptable price movement tolerance. This parameter is **directional**:
- Default: 30%
- **BUY transactions**: Price cannot be greater than the max slippage percentage, or else it will fail
- **SELL transactions**: Price cannot be smaller than the max slippage percentage, or else it will fail

### Fee
Cooking commission (1% of total order size). This is where the referral discounts and referral commissions stem from.

---

## Optional Parameters

Not all order types share these parameters or have the ability to set them.

### Time To Live (TTL)
**Deadline for order execution**. If it did not execute by said time it will automatically cancel.
- Set as: **unit + time unit** (Minutes, Hours, Days)
- Default: **Minutes**
- Available for: Limit and Custom orders

### Take Profit / Stop Loss
Acts as a safeguard for the position managed at the position level while creating appropriate underlying limit orders in the backend.
- User defines threshold as price or market cap trigger
- **Important**: TP/SL orders execute only after the main order executes (for BUY orders)
- Available for: Limit orders only

### Price Limit
For order types that execute several transactions along a set timeframe, users can set a price threshold they are not willing to exceed. This parameter is **directional**:
- **BUY transactions**: Price limit = maximum price acceptable
- **SELL transactions**: Price limit = minimum price acceptable
- Available for: TWAP orders only

---

## 1. Market Order

### Description
An immediate spot swap between SOL and a token at the current market price.

### How It Works
Executes instantly when confirmed, exchanging assets at the best available market rate.

### Configuration
- Requires all General Parameters
- No optional parameters
- No timing controls

### Required Parameters
- All General parameters

### Optional Parameters
- None

### Execution
- Immediate execution at current market price
- Single transaction
- No time delay

### Best For
Traders who want immediate execution at current market prices.

### Example
Buy 10 SOL worth of TOKEN XYZ right now at market price.

---

## 2. DCA (Dollar Cost Averaging) Order

### Description
Automated market orders executed at regular intervals over time.

### How It Works
Splits your total order into equal-sized market orders executed at your chosen frequency.

### Configuration

**Order Size**: Total amount to be either bought or sold

**Execution Interval**: Frequency of trades
- Set as: **unit + time unit** (Minutes, Hours, Days)
- Default: **Minutes**

### Management
- Can be paused and reactivated
- Can be canceled entirely
- Transaction cycle determined from creation time

### Behavior

**Transaction Failures**:
The transaction can fail by many reasons, with the most common being not having enough balance to execute.

**Order Management**:
- **Pause**: DCA orders can be paused and re-activated at user's desire
- **Cycle Timing**: Transaction cycle always determined in reference to the time of creation of the order
- **Cancel**: Users can stop the cycles altogether by Canceling a DCA order

### Required Parameters
- All General parameters
- Execution Interval

### Optional Parameters
- None

### Best For
Reducing the impact of volatility by averaging purchase/sale prices over time.

### Use Cases
- Automated accumulation strategies
- Risk-managed position building over time
- Volatility-independent investing

### Example
Buy 1 SOL worth of TOKEN XYZ every hour for the next week.

---

## 3. Limit Order

### Description
A conditional order that executes when a specific price or market cap threshold is reached, with optional Take Profit and Stop Loss protection managed at the position level.

### How It Works
Order remains "open" until market conditions meet your trigger, then executes automatically. The system uses a **position-centric approach**, managing Take Profit and Stop Loss at the token position level while creating appropriate underlying limit orders in the backend.

### Trigger Parameters

Cooking currently supports two trigger parameters:

#### Price
- The spot price for the asset

#### Market Cap
- Value resulting of the total token supply multiplied by the spot price
- Always expressed in **Solana**

### Configuration Parameters

**Primary Order Parameters**:
- **token**: The base asset to trade
- **orderSize**: Amount to trade (SOL for BUY, token units for SELL)
- **parameter**: Choose 'price' or 'marketCap' as the trigger threshold type (not both)
- **parameterValue**: The specific threshold value that activates the order

**Take Profit Parameters** (Optional):
- **takeProfitEnabled**: Boolean to enable TP functionality
- **takeProfitParameter**: Choose 'price' or 'marketCap' for TP trigger
- **takeProfitValue**: Target value for profit-taking

**Stop Loss Parameters** (Optional):
- **stopLossEnabled**: Boolean to enable SL functionality
- **stopLossParameter**: Choose 'price' or 'marketCap' for SL trigger
- **stopLossValue**: Threshold value for loss prevention

### Order Behavior by Direction

The system automatically determines trigger direction based on whether your parameterValue is above or below the current market value. This directional logic applies to all limit order triggers: main orders, Take Profit, and Stop Loss.

#### BUY Limit Orders

When creating a BUY limit order, you typically want to enter a position when the price drops. The triggers work as follows:

**Main Order Trigger**: Set parameterValue LOWER than current value
- Creates trigger: `parameter <= parameterValue`
- Example: Current price is 0.2 SOL, you want to buy at 0.1 SOL
- Result: `price <= 0.1` (executes when price drops to or below 0.1)

**Take Profit Trigger**: Set takeProfitValue HIGHER than your buy price
- Creates trigger: `takeProfitParameter >= takeProfitValue`
- Example: After buying at 0.1 SOL, you want to sell at 0.3 SOL
- Result: `price >= 0.3` (executes when price rises to or above 0.3)

**Stop Loss Trigger**: Set stopLossValue LOWER than your buy price
- Creates trigger: `stopLossParameter <= stopLossValue`
- Example: After buying at 0.1 SOL, you want to exit if it drops to 0.08 SOL
- Result: `price <= 0.08` (executes when price drops to or below 0.08)

**Order Activation**:
- **TP/SL orders only activate AFTER the main order executes** (not listed before)
- TP and SL are mutually exclusive: when one executes, it cancels the other
- TP and SL inherit remaining TTL from primary order

**Complete BUY Example**:
```
Current price: 0.15 SOL
- Main: price <= 0.1 SOL (buy when price drops from 0.15 to 0.1)
- Take Profit: price >= 0.3 SOL (after buying at 0.1, sell when price rises to 0.3)
- Stop Loss: price <= 0.08 SOL (after buying at 0.1, sell if price drops to 0.08)
```

#### SELL Limit Orders

When creating a SELL limit order, you already hold the token and want to exit. The triggers work as follows:

**Main Order Trigger** (acts as Take Profit): Set parameterValue HIGHER than current value
- Creates trigger: `parameter >= parameterValue`
- Example: Current price is 0.15 SOL, you want to sell at 0.3 SOL
- Result: `price >= 0.3` (executes when price rises to or above 0.3)

**Stop Loss Trigger**: Set stopLossValue LOWER than current value
- Creates trigger: `stopLossParameter <= stopLossValue`
- Example: Current price is 0.15 SOL, you want to exit if it drops to 0.08 SOL
- Result: `price <= 0.08` (executes when price drops to or below 0.08)

**Order Activation**:
- **SL is active immediately alongside the main order** (both listed from creation)
- Main order and SL are independent and can be cancelled separately
- SL provides downside protection while main order targets profit

**Complete SELL Example**:
```
Current price: 0.15 SOL (you already hold the token)
- Main: price >= 0.3 SOL (sell when price rises from 0.15 to 0.3 for profit)
- Stop Loss: price <= 0.08 SOL (sell if price drops from 0.15 to 0.08 to limit losses)
```

### Order Lifecycle Management

1. **Primary Order Creation**: Main limit order is created with specified conditions
2. **Secondary Order Activation**:
   - **BUY orders**: TP/SL queue for activation and only become active after primary order fills
   - **SELL orders**: SL is active immediately from creation alongside main order
3. **Mutual Exclusion**: For BUY orders, when either TP or SL executes, the other is automatically cancelled
4. **TTL Inheritance**: Secondary orders inherit the remaining TTL from the primary order

### Order Management & Independence

- **Independent Cancellation**: All orders (main, TP, SL) can be cancelled individually
- **No Cascade Cancellation**: Cancelling one order does NOT automatically cancel related orders
- **FIFO Processing**: Orders are processed in First-In-First-Out order when multiple triggers activate simultaneously
- **Real-time Monitoring**: System continuously evaluates all active limit orders against current market conditions
- **Execution Tracking**: Each order tracked independently even when linked to a position

### Order Lifecycle States

1. **Opened**: Order created, waiting for market conditions
2. **Triggered**: Market conditions met, execution attempted
3. **Filled**: Order successfully executed
4. **Cancelled**: Manually cancelled or TTL deadline met

**Note**: Order will be filled or canceled by the time the TTL deadline is met, whatever happens first.

### Gas Fee Calculation

For future-facing orders, GAS fee calculated **at the time of execution** since network conditions are variable.

### Required Parameters
- All General parameters
- Trigger parameter (Market Cap or Price)
- Trigger value

### Optional Parameters
- Time To Live (TTL)
- Take Profit (BUY only)
- Stop Loss

### Important Notes

- Gas fee calculated at execution time for each order (network conditions vary)
- Orders can exist independently without TP/SL
- TP/SL orders reference both position_id and parent_order_id for relationship tracking
- Future enhancement: Parameter value editing after order creation (not currently available)

### Best For
Entering positions at specific price points while automatically managing risk and reward targets with position-level protection.

### Complete Example

You want to buy 5 SOL worth of TOKEN XYZ when price drops to 0.1 SOL, with automated profit-taking at 0.3 SOL and loss protection at 0.08 SOL.

- Create BUY Limit Order:
  - Main: `price <= 0.1 SOL` (order listed immediately)
  - Take Profit: `price >= 0.3 SOL` (queued, not listed yet)
  - Stop Loss: `price <= 0.08 SOL` (queued, not listed yet)
- When main order executes at 0.1 SOL:
  - Position opened
  - TP order activates and lists: "Sell at price >= 0.3 SOL"
  - SL order activates and lists: "Sell at price <= 0.08 SOL"
  - Both are now active and monitoring the market
- If price reaches 0.3 SOL:
  - TP executes (sells position at profit)
  - SL automatically cancels (mutually exclusive)
- OR if price drops to 0.08 SOL:
  - SL executes (sells position to limit loss)
  - TP automatically cancels (mutually exclusive)

---

## 4. TWAP Order (Time-Weighted Average Price)

### Description
An algorithmic trading strategy that breaks down a large order into smaller trades executed at regular time intervals.

### How It Works
Divides your total order size equally across the execution duration, trading at consistent intervals.

### Configuration Parameters

#### 1. Order Type
- **BUY** or **SELL**

#### 2. Total Order Size
- Total amount of the token to be traded using the TWAP strategy
- Complete amount to trade

#### 3. Execution Duration
- Total duration over which the TWAP order will execute
- Total time to complete all trades
- Set as: **unit + time unit** (Minutes, Hours, Days, Years)
- Default: **Minutes**

#### 4. Execution Interval
- Defines how often trades will be executed within the selected execution period
- Trade frequency
- Available options:
  - Every 1 minute
  - Every 5 minutes
  - Every 30 minutes
  - Every 1 hour

#### 5. Price Limit (Optional)
- Maximum buy price or minimum sell price
- If market price exceeds this limit, the order will be skipped
- **BUY**: Maximum acceptable price
- **SELL**: Minimum acceptable price
- Orders skip execution if price exceeds limit

### Required Parameters
- All General parameters
- Total Order Size
- Execution Duration
- Execution Interval

### Optional Parameters
- Price Limit

### Best For
Minimizing market impact and achieving average execution prices less affected by short-term volatility.

### Example Use Case

**Configuration**:
- Order Type: Sell
- Total Order Size: 100 SOL
- Execution Duration: 1 hour
- Execution Interval: Every 5 minutes
- Price Limit: $110 per SOL (optional)

**Outcome**:
- Every 5 minutes, system executes a sell order for: `100 SOL / (60min / 5min) = 8.33 SOL`
- 12 executions total
- After 1 hour, full 100 SOL sold at time-weighted average price

---

## 5. VWAP Order (Volume-Weighted Average Price)

### Description
An algorithmic execution strategy that aims to execute trades in line with the market's volume distribution over a set period.

### How It Works

Monitors market volume over a reference period and executes trades as a percentage of that volume.

The VWAP strategy divides a total inventory into smaller trades, executed periodically based on market volume:

#### Step 1: Determine Market Volume
- System monitors total traded volume in reference period (e.g., last 30 minutes)
- Timeframe to monitor market volume
- Set as: **unit + time unit** (Minutes, Hours, Days, Years)
- Default: **Minutes**

#### Step 2: Calculate Order Size
- Percentage of total market volume (e.g., 10%) determines trade size for each execution interval
- At each interval, order size = (Market Volume in Reference Period) × (Volume %)

#### Step 3: Execute Trades Periodically
- Algorithm places buy/sell orders at defined intervals (e.g., every 5 minutes)
- Trade frequency
- Available options:
  - Every 1 minute
  - Every 5 minutes
  - Every 30 minutes
  - Every 1 hour

#### Step 4: Continue Until Completion or Timeout
- Runs until total inventory fully executed or max trade time reached
- Maximum time to complete (auto-stops when inventory depleted)
- Duration set as: **unit + time unit** (Minutes, Hours, Days, Years)
- Default: **Minutes**

### Key Characteristic

The VWAP Algorithm **discovers the correct order size** for the transaction, but the **exchange rate is determined by market conditions**, making this effectively a **Market order with dynamic order definition procedure**.

### Configuration Parameters

1. **Total Inventory**: Complete amount to trade
2. **Volume Reference Period**: Timeframe to monitor market volume
3. **Volume To Trade**: Percentage of market volume to execute per interval
4. **Execution Interval**: Trade frequency (1min, 5min, 30min, 1hr)
5. **Duration**: Maximum time to complete entire inventory

### Required Parameters
- All General parameters
- Total Inventory
- Volume Reference Period
- Volume To Trade
- Execution Interval
- Duration

### Optional Parameters
- None

### Best For
Achieving execution prices close to market benchmark while minimizing impact on highly liquid markets.

### Example Use Case

**Configuration**:
- Total Inventory: 100 SOL
- Execution Interval: 5 minutes
- Volume Reference Period: 30 minutes
- Volume To Trade: 10%
- Duration: 60 minutes

**Execution Timeline**:
- **T0**: 30mVol(80 SOL) × 10% = 8 SOL → 92 SOL left in Inventory
- **T1**: 30mVol(85 SOL) × 10% = 8.5 SOL → 83.5 SOL left in Inventory
- **T2**: 30mVol(90 SOL) × 10% = 9 SOL → 74.5 SOL left in Inventory
- **...continues until 100 SOL fully executed or 60 minutes elapsed**

---

## 6. Custom Order

### Description
Multi-condition limit orders that execute when 2-7 specified market conditions are met simultaneously.

Essentially Limit Orders with **multiple parameters** to be met in order to execute. Parameters are **additive**, meaning users can stack anywhere from **2 to 7** conditions.

### How It Works
Monitors multiple token metrics; order triggers only when all selected conditions are satisfied (additive logic).

### Available Conditions (Stack 2-7)

#### 1. Liquidity Amount
Trigger when liquidity reaches a threshold.
- **Example**: Buy 1 SOL if liquidity drops to 5K
- **Example**: If liquidity rises above 20K, sell 1 SOL

#### 2. Top 10 Holders %
Trigger based on token concentration.
- **Example**: If the top 10 holders own more than 50%, sell 1 SOL

#### 3. Dev Sold
Trigger based on developer token sales.
- **Example**: If the dev sells 100% of their holdings, sell 2 SOL

#### 4. Holders Count
Trigger based on total holder count.
- **Example**: If the number of holders drops below 100, sell everything

#### 5. Price Change Percentage
Trigger on % price changes over timeframes.
- **Timeframes**: 1m / 5m / 1h / 24h
- **Example**: Buy 2 SOL if price increases 30% in 5 minutes

#### 6. Average Holding Time
Trigger based on token's average holding duration.
- **Example**: Sell 1 SOL if average holding time drops to 2 seconds

### Available Scenarios

#### Time-Limited Orders
Users can set time limits for their orders. If the condition is not met within the specified timeframe, the order will be automatically canceled.

**Example**:
- If the dev sells 100% of their holdings in the next 6h, sell everything
- If it doesn't happen within that period, cancel the order

#### Multi-Condition Orders
Users can combine multiple conditions to execute an order.

**Example 1**:
- If the number of holders drops by 20% **AND** the price change in the last minute is -20%, then sell everything within the next 12h

**Example 2**:
- If liquidity increases by 30% **AND** the top 10 holders' percentage drops below 40%, buy 2 SOL

### Logic
- **Conditions are additive** (AND logic)
- All specified conditions must be met for execution
- Optional TTL for automatic cancellation
- Complex risk management strategies enabled

### Required Parameters
- All General parameters
- 2-7 conditions from available options

### Optional Parameters
- Time To Live (TTL)

### Best For
Advanced traders monitoring multiple market metrics simultaneously to catch specific risk/opportunity scenarios.

### Example
Sell 5 SOL if (liquidity drops below 10K) AND (top 10 holders exceed 60%) AND (holder count drops below 150).

---

## Choosing the Right Trading Method

| Method | Execution | Timing | Complexity | Best Use Case |
|--------|-----------|--------|------------|---------------|
| **Market** | Immediate | Now | Simple | Quick trades at current price |
| **DCA** | Scheduled | Multiple | Simple | Reducing volatility impact |
| **Limit** | Conditional | When triggered | Moderate | Entry at specific price points |
| **TWAP** | Algorithmic | Time-based | Moderate | Large orders with minimal impact |
| **VWAP** | Algorithmic | Volume-based | Advanced | Trading with market flow |
| **Custom** | Conditional | When all conditions met | Advanced | Complex multi-metric strategies |

---

## Order Type Comparison Matrix

| Feature | Market | DCA | Limit | TWAP | VWAP | Custom |
|---------|--------|-----|-------|------|------|--------|
| Immediate Execution | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Recurring Execution | ❌ | ✅ | ❌ | ✅ | ✅ | ❌ |
| Price Trigger | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ |
| Volume-Based | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Multi-Condition | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| TP/SL Support | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| TTL Support | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Price Limit | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Pause/Resume | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |

---

## Optional Parameters Summary

- **Time To Live (TTL)**: Available for Limit and Custom orders
- **Take Profit/Stop Loss**: Available for Limit orders (restrictions apply)
- **Price Limit**: Available for TWAP orders only

---

**Status**: In development
**Priority**: Critical - Core trading functionality
**Next Steps**: Complete Custom Order conditions, finalize VWAP implementation, comprehensive testing
