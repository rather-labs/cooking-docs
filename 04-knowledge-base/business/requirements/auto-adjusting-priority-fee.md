---
title: Auto-Adjusting Priority Fee
type: feature-specification
status: planned
priority: medium
created: 2025-09-04
date: 2025-10-20
updated: 2025-10-20
tags: [priority-fee, transaction-optimization, network-conditions, jupiter]
related:
  - "[[trading-methods]]"
  - "[[data-explanations]]"
---

# Auto-Adjusting Priority Fee

## Overview

To guarantee the user always gets their transaction through and don't overspend if not decided to, Cooking will implement an automatic adjustment on the priority fee for all operations determined from network parameters.

## Feature Scope

This new feature should also apply for **future-facing operations** like:
- DCA (Dollar-Cost Averaging)
- TWAP (Time-Weighted Average Price)
- VWAP (Volume-Weighted Average Price)
- Other algorithmic trading methods

**Key Behavior**: The priority fee will now be a **dynamic value**.

---

## How It Works

### Default Behavior

When the user starts defining an order with whichever direction they choose, the **default parameter** from Cooking will be to consume an **auto-adjusted priority fee from Jupiter's swap API feed**.

### For Future-Facing Operations

In the case that the transactions are operations that will occur several times in the future, and the auto-adjusted priority fee feature was kept as a parameter:

**Behavior**:
- The priority fee should **adjust based on the network conditions of each execution time**
- Each individual transaction within the order will use the current network-optimal fee
- No manual intervention required from the user

### Manual Override Option

In the case that a future-facing operation (such as a DCA) is created but the auto-adjusted priority fee feature is **not kept as a parameter**:

**Behavior**:
- User will be **forced to determine said value in SOLANA terms**
- Exactly as it is currently defined
- Fixed fee for all transactions in the order
- User takes responsibility for fee adequacy

---

## User Experience

### Order Creation Flow

#### Step 1: Fee Selection

When creating any order, user sees:

```
Priority Fee:
○ Auto-Adjust (Recommended) - Network optimized
○ Manual - Set fixed fee

[Current network fee: 0.008 SOL]
```

#### Step 2: Auto-Adjust (Default)

If **Auto-Adjust** is selected:
- Display current network fee as reference
- Note: "Fee will adjust based on network conditions"
- For future orders: "Each execution will use optimal fee at that time"

#### Step 3: Manual Override

If **Manual** is selected:
- Input field for SOL amount
- Display current network fee as guidance
- Warning: "Fixed fee may result in slower transactions if network becomes congested"

### Display During Execution

#### For Immediate Orders (Market)
- Show actual fee used
- Indicate if it was auto-adjusted or manual

#### For Future Orders (DCA, TWAP, VWAP, Limit)
- Show current network fee
- Indicate "Auto-adjusting" or "Fixed at X SOL"
- Historical log of fees used per execution

---

## Technical Implementation

### Jupiter Integration

**Data Source**: Jupiter's swap API feed

**API Endpoint** (conceptual):
```
GET /api/jupiter/priority-fee
Response: {
  "priorityFee": "0.008",
  "unit": "SOL",
  "timestamp": "2025-09-04T13:42:00Z",
  "networkCondition": "normal"
}
```

**Polling Strategy**:
- Poll every 30 seconds for up-to-date fee
- Cache for immediate use
- Fallback to last known value if API unavailable

### Fee Calculation Logic

#### For Auto-Adjust Mode

```pseudo
function getPriorityFee(orderType, executionTime):
  if orderType == "immediate":
    return getCurrentNetworkFee()

  if orderType == "future":
    # Fetch at execution time
    return getFutureNetworkFee(executionTime)

function getCurrentNetworkFee():
  jupiterFee = fetchJupiterPriorityFee()

  if jupiterFee.success:
    return jupiterFee.value
  else:
    return getFallbackFee()  # Use cached or default
```

#### For Manual Mode

```pseudo
function getPriorityFee(orderType, userDefinedFee):
  # Use the user-defined fee for all executions
  return userDefinedFee
```

### Database Schema

**Order Table Extension**:
```sql
ALTER TABLE orders ADD COLUMN priority_fee_mode VARCHAR(20);
-- Values: 'auto' | 'manual'

ALTER TABLE orders ADD COLUMN priority_fee_value DECIMAL(18,9);
-- NULL for auto mode, user value for manual mode
```

**Execution Log**:
```sql
CREATE TABLE execution_logs (
  id BIGINT PRIMARY KEY,
  order_id BIGINT,
  executed_at TIMESTAMP,
  priority_fee_used DECIMAL(18,9),
  network_condition VARCHAR(20),
  transaction_hash VARCHAR(88)
);
```

---

## Benefits

### For Users

✅ **Cost Optimization**: Never overpay for priority fees
✅ **Guaranteed Execution**: Adequate fees ensure transactions go through
✅ **Convenience**: No need to monitor network conditions manually
✅ **Flexibility**: Can override to manual if preferred

### For Platform

✅ **Better UX**: Users don't face failed transactions due to low fees
✅ **Competitive Advantage**: Smart fee management differentiates platform
✅ **Reduced Support**: Fewer issues with stuck/failed transactions

---

## Edge Cases & Error Handling

### Jupiter API Unavailable

**Scenario**: Jupiter API is down or unreachable

**Handling**:
1. Use cached last known fee
2. If no cache, use platform default (e.g., 0.008 SOL)
3. Notify user of fallback mode
4. Retry API in background

### Network Congestion Spike

**Scenario**: Network suddenly becomes very congested

**Handling**:
- Auto-adjust will capture the increased fee
- Display warning to user if fee exceeds historical average by >3x
- User can cancel/modify order if desired

### Manual Fee Too Low

**Scenario**: User sets manual fee below network minimum

**Handling**:
- Display warning: "Fee may be too low for current network conditions"
- Show current network fee for comparison
- Allow user to proceed at their own risk
- Track execution success rate for analytics

---

## User Education

### In-App Tooltips

**Auto-Adjust Mode**:
> "Automatically adjusts priority fee based on real-time network conditions. Ensures your transaction goes through while minimizing costs."

**Manual Mode**:
> "Set a fixed priority fee for all executions. Recommended for advanced users who want predictable costs. May result in slower or failed transactions during network congestion."

### Help Documentation

Topics to cover:
- What is a priority fee?
- How does auto-adjustment work?
- When should I use manual mode?
- What if my transaction still fails?

---

## Analytics & Monitoring

### Metrics to Track

**Adoption**:
- % of orders using auto-adjust vs manual
- User conversion from manual to auto-adjust

**Performance**:
- Average fee paid (auto vs manual)
- Transaction success rate by mode
- Time to execution by mode

**Network Conditions**:
- Fee trends over time
- Congestion patterns
- Correlation between fee and success rate

---

## Future Enhancements

### Advanced Fee Strategies

- **Conservative**: Use slightly higher fee to ensure fastest execution
- **Economic**: Use minimum viable fee to save costs
- **Balanced**: Current behavior (recommended optimal)

### Predictive Fees

- Machine learning to predict fee requirements
- Time-of-day patterns
- Event-based adjustments (new token launches, etc.)

### Gas Price Alerts

- Notify users when network fees drop significantly
- Suggest rescheduling large orders to cheaper times

---

**Status**: Planned
**Priority**: Medium - Improves user experience and transaction success rate
**Dependencies**: Jupiter API integration
**Next Steps**:
1. Integrate Jupiter priority fee API
2. Design UI for fee mode selection
3. Implement fee calculation logic
4. Add execution logging
5. Create user education materials
6. Test across various network conditions
7. Deploy with monitoring
8. Analyze adoption and optimize
