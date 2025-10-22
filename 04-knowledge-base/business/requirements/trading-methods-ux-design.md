---
title: Cooking Trading Methods - UX Design Specification
type: ux-specification
status: in-development
priority: critical
created: 2025-09-09
date: 2025-10-20
updated: 2025-10-20
tags: [ux-design, trading, user-interface, order-management]
related:
  - "[[trading-methods]]"
  - "[[limit-orders-methodology]]"
  - "[[platform-vision-requirements]]"
---

# Cooking Trading Methods - UX Design Specification

*This document extends the trading methods specification with detailed UX design considerations for all order types.*

---

## General Parameters UX

These parameters are shared by all order types and are mandatory:

### Gas Fee
**Display**: Auto-calculated, shown in real-time
- Current value prominently displayed
- Network congestion indicator
- Historical average for comparison

### Slippage
**Display**: Adjustable slider or input field
- Default: 30%
- Range: 0.1% - 50%
- Directional explanation:
  - BUY: "Price cannot exceed +30%"
  - SELL: "Price cannot fall below -30%"

### Priority Fee
**Display**: Auto-adjust toggle + manual input
- Default: 0.008 SOL (auto-adjust recommended)
- Network-based recommendation
- Explanation tooltip

### Fee (Platform Commission)
**Display**: Clear, transparent breakdown
- "1% Cooking fee"
- Referral discount applied (if applicable)
- Total cost calculation

### Direction
**Display**: Toggle or radio buttons
- ● BUY  ○ SELL
- Visual distinction (green/red)
- One-click toggle

### Order Size
**Display**: Input field with validation
- SOL for BUY / Token for SELL
- Max button for balance
- Real-time USD equivalent
- Balance indicator below

---

## Optional Parameters UX

### Time To Live (TTL)
**Display**: Time picker
- Unit input + dropdown (Minutes/Hours/Days)
- Presets: 1h, 6h, 24h, 7d
- Clear expiration countdown

### Take Profit / Stop Loss
**Display**: Expandable sections with toggles
- Checkbox to enable
- Conditional fields when enabled
- PnL% or absolute value input
- Visual profit/loss indicators (green/red)

### Price Limit
**Display**: Optional field
- "Maximum price (BUY)" / "Minimum price (SELL)"
- Warning if current price exceeds limit
- Skip notification when limit exceeded

---

## Market Order UX

### Interface
**Simplest order type** - streamlined for speed:

```
┌────────────────────────────────┐
│ Market Order                   │
├────────────────────────────────┤
│ Token: [ROOSTER         ▼]    │
│ Direction: ● Buy  ○ Sell       │
│ Amount: [1.0] SOL              │
│ ≈ 54,421 ROOSTER               │
│                                │
│ Current Price: 0.0037 SOL      │
│ Slippage: [30]%                │
│                                │
│ ┌──────────────────────────┐  │
││ Total Cost                ││  │
││ Amount:      1.0 SOL      ││  │
││ Cooking Fee: 0.01 SOL     ││  │
││ Gas Fee:     0.0001 SOL   ││  │
││ Priority Fee: 0.008 SOL   ││  │
││ ─────────────────────────  ││  │
││ Total:       1.0181 SOL   ││  │
│└──────────────────────────┘  │
│                                │
│ [Buy ROOSTER]                  │
└────────────────────────────────┘
```

**Key UX Considerations:**
- Clear display of current market price
- Real-time fee calculation
- Slippage impact visualization
- One-click execution

---

## DCA Order UX

### Interface
**Focus on time-based automation**:

```
┌────────────────────────────────┐
│ DCA Order                      │
├────────────────────────────────┤
│ Token: [ROOSTER         ▼]    │
│ Direction: ● Buy  ○ Sell       │
│                                │
│ Total Amount: [5.0] SOL        │
│ Per Execution: [0.5] SOL       │
│                                │
│ Execute Every:                 │
│ [1] [Hours ▼]                  │
│                                │
│ ○ Start immediately            │
│ ● Schedule for:                │
│   [2025-10-21 09:00]          │
│                                │
│ Expected Duration: 10 hours    │
│ Total Executions: 10           │
│                                │
│ [Create DCA Order]             │
└────────────────────────────────┘
```

**Active DCA Display**:

```
┌────────────────────────────────────────┐
│ DCA Order - ROOSTER                    │
├────────────────────────────────────────┤
│ ▓▓▓▓▓▓▓░░░  60% Complete              │
│                                        │
│ Executed: 6 / 10                       │
│ Spent: 3.0 SOL                         │
│ Acquired: 326,530 ROOSTER              │
│ Avg Price: 0.0036 SOL                  │
│                                        │
│ Next Execution: in 23 minutes          │
│                                        │
│ [❚❚ Pause] [✕ Cancel]                 │
└────────────────────────────────────────┘
```

**Key UX Considerations:**
- Progress visualization
- Clear execution schedule
- Pause/resume prominently displayed
- Next execution countdown
- Running average price
- Balance validation warnings

---

## Limit Order UX (with TP/SL)

### Unified Interface
**Single form with conditional sections**:

```
┌─────────────────────────────────────────┐
│ Limit Order                             │
├─────────────────────────────────────────┤
│ Token: [ROOSTER            ▼]          │
│ Direction: ● Buy  ○ Sell                │
│ Amount: [1.0] SOL                       │
│                                         │
│ Trigger When:                           │
│ ○ Price  ● Market Cap                   │
│ [≤] [3,500] USD                         │
│ Current: 3,670 USD                      │
│ (Trigger at -4.6%)                      │
│                                         │
│ ☑ Take Profit                           │
│ ┌───────────────────────────────────┐  │
││ ○ Price  ● Market Cap             ││  │
││ [≥] [4,500] USD                   ││  │
││ (Profit target: +22%)             ││  │
│└───────────────────────────────────┘  │
│                                         │
│ ☑ Stop Loss                             │
│ ┌───────────────────────────────────┐  │
││ ○ Price  ● Market Cap             ││  │
││ [≤] [3,000] USD                   ││  │
││ (Max loss: -14%)                  ││  │
│└───────────────────────────────────┘  │
│                                         │
│ TTL: [24] Hours                         │
│                                         │
│ [Create Limit Order]                    │
└─────────────────────────────────────────┘
```

**Order Listing Behavior**:

For **Buy Limit Orders**:
- Primary order listed immediately
- TP/SL listed when main order executes
- Clear status indicators

For **Sell Limit Orders**:
- Main order (TP) listed immediately
- Stop Loss listed immediately
- Both independent but linked

**Position Management View**:

```
┌──────────────────────────────────────────┐
│ Position: ROOSTER                        │
├──────────────────────────────────────────┤
│ Holdings: 104,445 ROOSTER                │
│ Avg Entry: 0.0037 SOL                    │
│ Current: 0.0041 SOL                      │
│                                          │
│ Unrealized PnL: +10.8%                   │
│ ┌──────────────────────────────────┐    │
││ +0.43 SOL                        ││    │
│└──────────────────────────────────┘    │
│                                          │
│ Active Orders:                           │
│ ┌────────────────────────────────────┐  │
││ 🎯 Take Profit @ 0.0045 SOL       ││  │
││    Status: Active                  ││  │
││    [Modify] [Cancel]               ││  │
│└────────────────────────────────────┘  │
│ ┌────────────────────────────────────┐  │
││ 🛡️ Stop Loss @ 0.0030 SOL          ││  │
││    Status: Active                  ││  │
││    [Modify] [Cancel]               ││  │
│└────────────────────────────────────┘  │
│                                          │
│ [Close Entire Position]                  │
└──────────────────────────────────────────┘
```

**Key UX Considerations:**
- Toggle switches for TP/SL activation
- Visual indicators (🎯 for TP, 🛡️ for SL)
- Status: Pending, Active, Filled
- Independent cancel buttons
- Visual connection lines showing relationships
- Clear explanation of listing behavior
- One-click position closure

---

## TWAP Order UX

### Interface
**Focus on time-based distribution**:

```
┌────────────────────────────────┐
│ TWAP Order                     │
├────────────────────────────────┤
│ Token: [ROOSTER         ▼]    │
│ Direction: ● Buy  ○ Sell       │
│                                │
│ Total Order Size: [100] SOL    │
│                                │
│ Execution Duration:            │
│ [1] [Hour ▼]                   │
│                                │
│ Execute Every:                 │
│ ○ 1 minute                     │
│ ● 5 minutes                    │
│ ○ 30 minutes                   │
│ ○ 1 hour                       │
│                                │
│ Per Execution: ~8.33 SOL       │
│ Total Executions: 12           │
│                                │
│ ☑ Price Limit: [110] USD       │
│                                │
│ [Create TWAP Order]            │
└────────────────────────────────┘
```

**Active TWAP Display**:

```
┌──────────────────────────────────────────┐
│ TWAP Order - ROOSTER                     │
├──────────────────────────────────────────┤
│ Timeline:                                │
│ 0:00 ▓▓▓▓▓▓▓░░░░░░ 0:60                │
│                                          │
│ Executed: 7 / 12 (58%)                   │
│ Spent: 58.3 SOL                          │
│ Avg Price: 0.0036 SOL                    │
│                                          │
│ Skipped: 1 (Price limit exceeded)        │
│                                          │
│ Next: in 2 minutes                       │
│ Completes: in 25 minutes                 │
│                                          │
│ [Cancel Remaining]                       │
└──────────────────────────────────────────┘
```

**Key UX Considerations:**
- Timeline visualization
- Clear interval selection
- Average price tracking
- Skip notifications
- Completion countdown

---

## VWAP Order UX

### Interface
**Focus on volume-based execution**:

```
┌────────────────────────────────┐
│ VWAP Order                     │
├────────────────────────────────┤
│ Token: [ROOSTER         ▼]    │
│ Direction: ● Buy  ○ Sell       │
│                                │
│ Total Inventory: [100] SOL     │
│                                │
│ Volume Reference Period:       │
│ [30] [Minutes ▼]               │
│                                │
│ Trade % of Volume: [10]%       │
│                                │
│ Execute Every:                 │
│ ● 5 minutes                    │
│                                │
│ Max Duration: [60] Minutes     │
│                                │
│ Current 30m Volume: 85 SOL     │
│ Next Execution: ~8.5 SOL       │
│                                │
│ [Create VWAP Order]            │
└────────────────────────────────┘
```

**Active VWAP Display**:

```
┌──────────────────────────────────────────┐
│ VWAP Order - ROOSTER                     │
├──────────────────────────────────────────┤
│ Volume-Based Progress:                   │
│ ▓▓▓▓▓▓▓░░░  60 / 100 SOL               │
│                                          │
│ Market Volume Trend:                     │
│ ▁▂▃▅▆▇█▇▆▅▃▂▁                          │
│                                          │
│ Executions: 7                            │
│ Avg Trade Size: 8.6 SOL                  │
│ Avg Price: 0.0036 SOL                    │
│                                          │
│ Next: Based on market volume             │
│ Timeout: in 45 minutes                   │
│                                          │
│ [Cancel Remaining]                       │
└──────────────────────────────────────────┘
```

**Key UX Considerations:**
- Volume monitoring display
- Dynamic order size shown
- Market impact visualization
- Volume trend chart

---

## Custom Order UX

### Condition Builder Interface

```
┌─────────────────────────────────────────┐
│ Custom Order                            │
├─────────────────────────────────────────┤
│ Token: [ROOSTER            ▼]          │
│ Direction: ● Buy  ○ Sell                │
│ Amount: [1.0] SOL                       │
│                                         │
│ Conditions (All must be met):           │
│                                         │
│ ┌───────────────────────────────────┐  │
││ 1. Liquidity                      ││  │
││    [Drops to] [5,000] USD         ││  │
││    Current: 8,500 USD             ││  │
││    [Remove]                        ││  │
│└───────────────────────────────────┘  │
│                                         │
│ ┌───────────────────────────────────┐  │
││ 2. Top 10 Holders                 ││  │
││    [Less than] [40]%              ││  │
││    Current: 52%                    ││  │
││    [Remove]                        ││  │
│└───────────────────────────────────┘  │
│                                         │
│ [+ Add Condition]                       │
│                                         │
│ Time Limit:                             │
│ ☑ Cancel if not met in [6] Hours       │
│                                         │
│ [Create Custom Order]                   │
└─────────────────────────────────────────┘
```

**Monitoring Dashboard**:

```
┌──────────────────────────────────────────┐
│ Custom Order - ROOSTER                   │
├──────────────────────────────────────────┤
│ All conditions must be met:              │
│                                          │
│ ☐ Liquidity ≤ 5,000 USD                 │
│    Current: 8,500 USD  (-41%)           │
│    ▓▓▓▓▓▓░░░░                           │
│                                          │
│ ☑ Top 10 Holders < 40%                  │
│    Current: 38%  ✓                      │
│    ▓▓▓▓▓▓▓▓▓▓                           │
│                                          │
│ Progress: 1 / 2 conditions met           │
│                                          │
│ Expires in: 4 hours 23 minutes           │
│                                          │
│ [Cancel Order]                           │
└──────────────────────────────────────────┘
```

**Key UX Considerations:**
- Drag-and-drop condition builder
- Real-time condition monitoring
- Progress bars for each condition
- Clear AND logic indication
- Alert for near-trigger conditions

---

## Key UX Design Principles

### Clarity & Transparency
- Clear indication of order states and relationships
- Real-time feedback on market conditions
- Transparent fee calculations

### User Control
- Independent order management
- Easy modification and cancellation
- Clear execution behavior

### Progressive Complexity
- Simple interfaces for basic orders
- Advanced options accessible but not overwhelming
- Contextual help and tooltips

### Risk Management
- Clear visualization of potential outcomes
- Prominent risk parameters
- Confirmation dialogs for high-risk actions

### Performance Feedback
- Real-time execution progress
- Historical performance data
- Optimization recommendations

---

**Status**: In development
**Priority**: Critical - Directly impacts user experience
**Related**: All trading method specifications
**Next Steps**: Prototype key interfaces, conduct user testing, iterate based on feedback
