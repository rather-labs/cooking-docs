---
title: Methodology for Implementing Limit Orders with Take Profit and Stop Loss
type: feature-specification
status: in-development
priority: critical
created: 2025-09-09
date: 2025-10-20
updated: 2025-10-20
tags: [limit-orders, take-profit, stop-loss, trading, risk-management]
related:
  - "[[trading-methods]]"
  - "[[trading-methods-ux-design]]"
  - "[[portfolio-wide-tpsl]]"
---

# Methodology for Implementing Limit Orders with Take Profit and Stop Loss

## 1. Core Architecture Overview

The system should be built with a **position-centric approach** rather than order-centric, as this aligns with user expectations and simplifies UX.

**Key Principle**: Take Profit and Stop Loss should be managed at the **token position level**, while still creating appropriate underlying limit orders in the backend.

---

## 2. Enhanced Order Parameters Structure

Building upon Cooking's existing general and optional parameters:

### Extended General Parameters

- **token**: Base asset (existing)
- **orderSize**: Amount to trade (SOL for BUY, token units for SELL) (existing)
- **parameter**: Choose between 'price' or 'marketCap' threshold (existing)
- **parameterValue**: Threshold value to trigger execution (existing)

### New TP/SL Parameters

- **takeProfitEnabled**: Boolean to enable TP functionality
- **takeProfitParameter**: 'price' or 'marketCap' for TP trigger
- **takeProfitValue**: Target value for profit-taking
- **stopLossEnabled**: Boolean to enable SL functionality
- **stopLossParameter**: 'price' or 'marketCap' for SL trigger
- **stopLossValue**: Threshold value for loss prevention

---

## 3. Order Logic Implementation

### 3.1 Directional Logic

Follow Cooking's existing directional trigger system (inspired by Jupiter's approach):

#### For BUY orders with TP/SL:

- **Main trigger**: `marketCap <= targetValue` or `price <= targetValue`
- **Take Profit**: `marketCap >= takeProfitValue` (activates after main order fills)
- **Stop Loss**: `marketCap <= stopLossValue` (activates after main order fills)

#### For SELL orders with SL only:

- **Main trigger acts as Take Profit**: `marketCap >= targetValue`
- **Stop Loss**: `marketCap <= stopLossValue` (additional protection)

### 3.2 Order Lifecycle Management

1. **Primary Order Creation**: Create the main limit order with specified conditions
2. **Secondary Order Queue**: Upon primary order execution, automatically create TP/SL orders
3. **Mutual Exclusion**: TP and SL orders should cancel each other when one executes
4. **TTL Inheritance**: Secondary orders inherit remaining TTL from primary order

**Execution Flow**:

```
BUY Limit Order Created
    ↓
[Waiting for trigger condition]
    ↓
Trigger condition met → Execute BUY
    ↓
[Position opened]
    ↓
Automatically create:
  - Take Profit order (sell at profit target)
  - Stop Loss order (sell at loss threshold)
    ↓
[One of them triggers]
    ↓
Execute triggered order → Cancel the other
    ↓
[Position closed]
```

---

## 4. Order Relationship Handling

### Database Schema Considerations

**Primary Orders**:
- Can exist independently
- No required parent reference
- Generate position_id upon execution

**TP/SL Orders**:
- Must reference both `position_id` and `parent_order_id`
- Linked lifecycle to position
- Cascade cancellation logic

**Relationships**:
```
Order Table:
  - id (PK)
  - position_id (FK, nullable)
  - parent_order_id (FK, nullable)
  - order_type (primary, take_profit, stop_loss)
  - status (pending, active, filled, cancelled)
```

### Cascade Cancellation Logic

**Scenarios**:

1. **User cancels primary order before execution**:
   - Primary order cancelled
   - No TP/SL orders created (weren't created yet)

2. **User cancels TP order after execution**:
   - TP order cancelled
   - SL order remains active
   - Position still open

3. **TP order executes**:
   - TP order filled
   - SL order automatically cancelled
   - Position closed

4. **SL order executes**:
   - SL order filled
   - TP order automatically cancelled
   - Position closed

5. **User manually closes position**:
   - All related orders cancelled
   - Position marked closed

---

## 5. Real-time Monitoring System

### 5.1 Market Data Processing

Leverage Cooking's existing indexer service:

**Monitoring Requirements**:
- Monitor real-time price and market cap changes
- Evaluate all active limit orders against current market conditions
- Process orders in **FIFO order** when multiple triggers activate simultaneously

**Technical Implementation**:
```pseudo
function monitorMarketConditions():
  while true:
    currentMarketData = fetchLatestMarketData()

    activeOrders = getActiveOrders()

    for order in activeOrders:
      if evaluateOrderTrigger(order, currentMarketData):
        queueOrderForExecution(order)

    processExecutionQueue()  # FIFO
    sleep(POLLING_INTERVAL)
```

---

## 6. User Interface Design

### 6.1 Unified Order Creation

Inspired by Axiom's simplicity - **Single form interface**:

**Components**:
1. **Primary order configuration** (existing Cooking UI)
2. **Toggle switches** for TP/SL activation
3. **Conditional parameter selection** (price vs marketCap)

**Layout**:
```
┌─────────────────────────────────────┐
│ Create Limit Order                  │
├─────────────────────────────────────┤
│ Token: [ROOSTER        ▼]          │
│ Direction: ● Buy  ○ Sell            │
│ Order Size: [1.0] SOL               │
│                                     │
│ Trigger When:                       │
│ ○ Price  ● Market Cap               │
│ [≤] [3500] USD                      │
│                                     │
│ ┌─────────────────────────────────┐│
││ ☑ Take Profit                    ││
││   ○ Price  ● Market Cap          ││
││   [≥] [4500] USD                 ││
│└─────────────────────────────────┘│
│                                     │
│ ┌─────────────────────────────────┐│
││ ☑ Stop Loss                      ││
││   ○ Price  ● Market Cap          ││
││   [≤] [3000] USD                 ││
│└─────────────────────────────────┘│
│                                     │
│ TTL: [24] Hours                     │
│                                     │
│ [Create Order]                      │
└─────────────────────────────────────┘
```

### 6.2 Position Management View

Integrate with Cooking's Quick Operations Panel:

**Display Elements**:
- Aggregate position with average entry price
- Show active TP/SL levels with visual indicators
- Allow modification of TP/SL without closing position
- One-click position closure option

**Position Card Example**:
```
┌──────────────────────────────────────────┐
│ ROOSTER Position                         │
├──────────────────────────────────────────┤
│ Holdings: 104,445 ROOSTER                │
│ Entry Price: 0.0037 SOL (avg)            │
│ Current Price: 0.0041 SOL                │
│ PnL: +10.8% (+0.43 SOL)                  │
│                                          │
│ ├─ Take Profit: 0.0045 SOL 🎯           │
│ └─ Stop Loss: 0.0030 SOL 🛡️             │
│                                          │
│ [Modify TP/SL] [Close Position]          │
└──────────────────────────────────────────┘
```

---

## 7. Advanced Features

### 7.1 Partial Order Execution

**Feature**: Support percentage-based TP/SL

**Example Configuration**:
- "Sell 50% at 2x"
- "Sell remaining 50% at 3x"

**Implementation**:
- Multiple TP orders with different triggers
- Each order holds partial position size
- All orders reference same position_id

### 7.2 Portfolio-Level Risk Management

**Feature**: Global stop loss across all positions

**Behavior**:
- Monitor total portfolio PnL
- Trigger liquidation if threshold breached
- Close all positions simultaneously

**Use Case**:
- "Close everything if I'm down more than 20% overall"

---

## 9. Error Handling & Edge Cases

### 9.1 Insufficient Liquidity

**Scenario**: Order can't be fully filled due to low liquidity

**Handling**:
- Graceful degradation when orders can't be fully filled
- Partial execution handling with remaining order management
- User notification system for execution failures

**Actions**:
1. Execute partial fill
2. Update order size to remaining
3. Keep order active for remainder
4. Notify user of partial fill

### 9.2 Market Gap Events

**Scenario**: Price gaps that skip over trigger levels

**Handling**:
- Handle price gaps that skip over trigger levels
- Execute at best available price
- Document slippage in execution log

**Example**:
- TP set at $100
- Price jumps from $95 to $105 (no $100 execution possible)
- Execute at $105 (best available)
- Record +5% positive slippage

---

## 10. Testing Strategy

### 10.1 Unit Tests

**Test Coverage**:
- Order trigger logic validation
- Position aggregation accuracy
- Secondary order creation logic
- Cascade cancellation behavior
- TTL inheritance
- Parameter validation

### 10.2 Integration Tests

**Test Coverage**:
- End-to-end order lifecycle testing
- Market data processing pipeline validation
- Multi-user concurrent order execution
- Database consistency under load
- Real-time monitoring accuracy

### 10.3 Edge Case Tests

**Scenarios**:
- Simultaneous TP and SL trigger (should be impossible, but test)
- Primary order cancellation mid-execution
- Network disruption during execution
- Extreme market volatility
- Order book liquidity exhaustion

---

## Implementation Phases

### Phase 1: Core Functionality
- [ ] Basic limit orders with single TP/SL
- [ ] Position tracking
- [ ] Secondary order creation
- [ ] Mutual exclusion logic

### Phase 2: Enhanced Features
- [ ] Partial order execution
- [ ] Multiple TP levels
- [ ] Position modification
- [ ] Advanced UI

### Phase 3: Portfolio Features
- [ ] Portfolio-wide stop loss
- [ ] Cross-position risk management
- [ ] Advanced analytics

---

**Status**: In development - Phase 1
**Priority**: Critical - Core trading feature
**Dependencies**: Limit orders, position tracking, real-time market monitoring
**Next Steps**:
1. Finalize database schema
2. Implement order relationship logic
3. Build monitoring service
4. Create unified order creation UI
5. Develop position management interface
6. Comprehensive testing
7. Deploy to production
