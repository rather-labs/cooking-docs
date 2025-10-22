---
title: Portfolio-Wide Take Profit / Stop Loss
type: feature-specification
status: planned
priority: high
created: 2025-09-23
date: 2025-10-20
updated: 2025-10-20
tags: [portfolio, take-profit, stop-loss, risk-management, position-management]
related:
  - "[[limit-orders-methodology]]"
  - "[[trading-methods]]"
  - "[[platform-vision-requirements]]"
---

# Portfolio-Wide Take Profit / Stop Loss

## Overview

Easily manage risk with a set-and-forget strategy at position and wallet level. The intention here is to allow Cooking traders to manage their positions from the portfolio page by setting a target PnL and a percentual amount of their holdings to lock in this order type.

---

## Concept

Portfolio level TP/SL orders are meant to be understood as a **new type of entity that seats above regular orders**.

---

## Key Characteristics

### Dynamic Order Size

**orderSize** is not defined as an integer, rather as a **percentage of the user total holding**.

**Rationale**: This is to allow other orders to increase the holding size without excluding the new tokens from the risk management strategy.

**Example**:
- User holds 100,000 ROOSTER tokens
- Portfolio TP/SL set for 50% of holdings
- Order size = 50,000 ROOSTER
- User buys 20,000 more ROOSTER
- Order size automatically updates to 60,000 ROOSTER (50% of 120,000)

### Dynamic Target PnL

**targetPnL** will not translate immediately into a target price, rather it will be kept as a **dynamic parameter** to be recalculated constantly as `targetPnL * avgEntryPrice`.

**Rationale**: This is also to allow other orders to increase the holding size without excluding the new tokens from the risk management strategy.

**Example**:
- Average entry price: 0.0037 SOL
- Target PnL: +20%
- Target price = 0.0037 * 1.2 = 0.00444 SOL
- User buys more at 0.0040 SOL
- New average entry: 0.0038 SOL
- Target price recalculates = 0.0038 * 1.2 = 0.00456 SOL

---

## Edge Cases

### Case 1: Limit Order TP/SL Interaction

Having orderSize and targetPnL as dynamic values allow for the user to also manage their TP and SL at the **limit order level**.

**Scenario**:
- Portfolio TP/SL set for 100% at +20%
- User also has a limit order with its own SL at -10%
- Limit order SL triggers first

**Result**:
- Total holding decreases
- Portfolio TP/SL orderSize recalculates to smaller amount
- Percentage definition (100%) still holds true

**Behavior**:
- Both levels of TP/SL can coexist
- More specific (limit order level) can trigger first
- Portfolio level adjusts dynamically

### Case 2: Complete Liquidation

If for whatever reason the user liquidates **all of their holding** using other methods than portfolio TP/SL, like transfers or sell orders, the outstanding orders should **auto-cancel** as the orderSize cannot be null.

**Triggers**:
- Manual sell orders
- Transfers out
- Other automated orders

**Action**:
- Check holding balance = 0
- Cancel all portfolio TP/SL orders for that token
- Notify user

---

## Allocation Rules

### Multiple Orders

Users will be able to set their TP/SL into **as many orders as they want** as long as the total sums up to a **100%**.

**Applies to**:
- 100% for take profit side
- 100% for stop loss side

**Examples**:

**Take Profit Ladder**:
- 30% at +20% PnL
- 40% at +50% PnL
- 30% at +100% PnL
- **Total: 100%** ✓

**Stop Loss Layers**:
- 50% at -10% PnL
- 50% at -20% PnL
- **Total: 100%** ✓

**Invalid Configuration**:
- 40% at +20% PnL
- 40% at +50% PnL
- **Total: 80%** ✗ (Must equal 100%)

---

## Order Management

### Creation
- Set from portfolio page
- Multiple orders per side
- Must total 100% per side

### Cancellation
- Users can manually cancel outstanding orders
- Auto-cancel when holding = 0
- Individual order cancellation

### Edit Capabilities
- **Not included in this version**
- Future enhancement
- For now: cancel and recreate

---

## Platform Availability

### Initial Release
- **Desktop** first implementation

### Future
- Should be available for **mobile** as well
- Consistent behavior across platforms

---

## Analytics & Logging

### Order Logging

Each order should be **logged** as well as their **status updates** for product analysis:

**Logged Data**:
- **Timestamps**: Created, updated, triggered, cancelled
- **Token**: Contract address, symbol
- **Order Parameters**:
  - Percentage allocation
  - Target PnL
  - Direction (TP/SL)
- **Status Updates**: Pending, active, filled, cancelled
- **Execution Data**: Actual price, slippage, fees

### Analytics Use Cases
- Adoption rate
- Most common TP/SL targets
- Success rates
- User behavior patterns

---

## User Interface

### Portfolio Page Enhancement

```
┌──────────────────────────────────────────────────────────────┐
│ Portfolio                                      [⚙️ Settings]  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ ┌────────────────────────────────────────────────────────┐  │
││ ROOSTER                                                 ││  │
││ 104,445 tokens                                          ││  │
││ Avg Entry: 0.0037 SOL                                   ││  │
││ Current: 0.0041 SOL                                     ││  │
││ PnL: +10.8% (+0.43 SOL)                                 ││  │
││                                                         ││  │
││ Portfolio TP/SL:                                        ││  │
││ ┌─────────────────────────────────────────────────┐    ││  │
│││ Take Profit (3 orders active)                   │││  ││  │
│││ • 30% @ +20% (0.00444 SOL)                      │││  ││  │
│││ • 40% @ +50% (0.00555 SOL)                      │││  ││  │
│││ • 30% @ +100% (0.0074 SOL)                      │││  ││  │
││└─────────────────────────────────────────────────┘    ││  │
││                                                         ││  │
││ ┌─────────────────────────────────────────────────┐    ││  │
│││ Stop Loss (1 order active)                      │││  ││  │
│││ • 100% @ -15% (0.00315 SOL)                     │││  ││  │
││└─────────────────────────────────────────────────┘    ││  │
││                                                         ││  │
││ [Edit Portfolio TP/SL]                                  ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Creation Modal

```
┌──────────────────────────────────────────────────────────────┐
│ Set Portfolio TP/SL - ROOSTER                                │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ Current Holdings: 104,445 ROOSTER                            │
│ Average Entry: 0.0037 SOL                                    │
│ Current Price: 0.0041 SOL                                    │
│                                                              │
│ ─────────────────────────────────────────────────────────── │
│                                                              │
│ Take Profit Orders                                           │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐  │
││ Order 1                                     [✕ Remove]  ││  │
││ Percentage: [30]%                                       ││  │
││ Target PnL: [+20]%                                      ││  │
││ → Triggers at: 0.00444 SOL                              ││  │
││ → Sells: 31,333 ROOSTER                                 ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐  │
││ Order 2                                     [✕ Remove]  ││  │
││ Percentage: [40]%                                       ││  │
││ Target PnL: [+50]%                                      ││  │
││ → Triggers at: 0.00555 SOL                              ││  │
││ → Sells: 41,778 ROOSTER                                 ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐  │
││ Order 3                                     [✕ Remove]  ││  │
││ Percentage: [30]%                                       ││  │
││ Target PnL: [+100]%                                     ││  │
││ → Triggers at: 0.0074 SOL                               ││  │
││ → Sells: 31,333 ROOSTER                                 ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
│ Total TP Allocation: 100% ✓                                  │
│ [+ Add TP Order]                                             │
│                                                              │
│ ─────────────────────────────────────────────────────────── │
│                                                              │
│ Stop Loss Orders                                             │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐  │
││ Order 1                                     [✕ Remove]  ││  │
││ Percentage: [100]%                                      ││  │
││ Target PnL: [-15]%                                      ││  │
││ → Triggers at: 0.00315 SOL                              ││  │
││ → Sells: 104,445 ROOSTER (all holdings)                 ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
│ Total SL Allocation: 100% ✓                                  │
│ [+ Add SL Order]                                             │
│                                                              │
│ [Create Orders]  [Cancel]                                    │
└──────────────────────────────────────────────────────────────┘
```

---

## Validation Rules

### Allocation Validation
- TP orders must total 100% (if any TP orders)
- SL orders must total 100% (if any SL orders)
- Cannot exceed 100% on either side
- Each order must be > 0%

### PnL Validation
- TP targets must be positive (+%)
- SL targets must be negative (-%)
- No overlapping triggers on same side

### Order Count
- Minimum: 1 order per side (if using that side)
- Maximum: 10 orders per side (configurable)

---

## Technical Implementation

### Database Schema

```sql
CREATE TABLE portfolio_tpsl_orders (
  id BIGINT PRIMARY KEY,
  user_id BIGINT,
  token_address VARCHAR(88),
  order_type VARCHAR(10),  -- 'take_profit' or 'stop_loss'
  percentage_allocation DECIMAL(5,2),  -- 0.01 to 100.00
  target_pnl_percentage DECIMAL(10,2),  -- e.g., 20.00 for +20%
  status VARCHAR(20),  -- 'active', 'triggered', 'cancelled'
  created_at TIMESTAMP,
  triggered_at TIMESTAMP NULL,
  cancelled_at TIMESTAMP NULL
);

CREATE INDEX idx_portfolio_tpsl_user_token
  ON portfolio_tpsl_orders(user_id, token_address, status);
```

### Dynamic Calculation Service

```pseudo
function calculatePortfolioTPSL(userId, tokenAddress):
  holdings = getUserHoldings(userId, tokenAddress)
  avgEntry = calculateAverageEntry(userId, tokenAddress)
  currentPrice = getCurrentPrice(tokenAddress)

  activeOrders = getActivePortfolioTPSL(userId, tokenAddress)

  for order in activeOrders:
    # Dynamic order size
    orderSize = holdings * (order.percentage_allocation / 100)

    # Dynamic target price
    targetPrice = avgEntry * (1 + order.target_pnl_percentage / 100)

    # Check if triggered
    if shouldTrigger(order.order_type, currentPrice, targetPrice):
      executeOrder(order, orderSize, currentPrice)
```

---

## Future Enhancements

### Edit Capabilities
- Modify existing orders without cancelling
- Rebalance allocations

### Advanced Strategies
- Trailing stop loss
- Time-based decay
- Volatility-adjusted targets

### Cross-Position Features
- Portfolio-wide PnL triggers
- Correlated position management

---

**Status**: Planned
**Priority**: High - Advanced risk management tool
**Platform**: Desktop first, mobile later
**Next Steps**:
1. Design portfolio page UI enhancements
2. Implement dynamic calculation logic
3. Build order allocation validation
4. Create portfolio TP/SL management interface
5. Test edge cases (liquidation, limit order interaction)
6. Deploy to desktop
7. Monitor adoption and effectiveness
8. Plan mobile implementation
