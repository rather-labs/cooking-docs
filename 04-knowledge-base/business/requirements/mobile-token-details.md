---
title: Mobile App - Token Details Screen
type: feature-specification
status: in-development
priority: critical
created: 2025-06-30
date: 2025-10-20
updated: 2025-10-20
tags: [mobile, token-details, trading, market-orders, limit-orders]
related:
  - "[[mobile-signup-login-home]]"
  - "[[mobile-wallet]]"
  - "[[trading-methods]]"
---

# Mobile App - Token Details Screen

## Product Vision

Cooking Mobile app should be an **initial stepping stone for non-crypto natives** to start their journey. With this objective in mind we will focus on a **clean UI**, with a **clear navigation system** that makes it obvious where the user is standing at all times.

---

## Token Information Display

When accessing a token, the user should be delivered into a **'Token Details' screen** where they'll be able to gain information regarding:

### Basic Information
- **Token's Name**: Full name and symbol
- **Contract Address**: With copy button
- **Token Age**: Time since creation
- **Current Protocol**: Where the token is listed (Pump.fun, Raydium, etc.)
- **Token Social Links**: Twitter, Telegram, website

### Price & Performance
- **Current Price**: Real-time price in SOL or USD
- **PnL by Timeframe**:
  - 1 minute
  - 5 minutes
  - 30 minutes
  - 1 hour

### User's Holdings
- **Token Balance**: Amount of tokens held
- **Total Amount Held**: Current value in SOL/USD
- **Total Amount Sold**: Historical sales value

### Market Activity
- **Total Operations**: Aggregated count of all transactions
  - Split by buys/sells
- **Total Traded Volume**: Aggregated trading volume
  - Split by buys/sells
- **Unique Addresses**: Total number of unique wallets that transacted
  - Split by buys/sells (makers)

---

## User's Trading History

### Historical Operations List

It is expected for the user to find here a **historical list of all their operations** for said token:

**Sort Order**: Ascending from the present (newest first)

**Display Per Operation**:
- Transaction type (BUY/SELL)
- Amount
- Price at execution
- Total value in SOL
- Timestamp
- Transaction status
- Link to explorer

---

## Trading Functionality

From this place the user will be able to operate the token by executing swaps.

### Market Orders

**Immediate execution** at current market price.

#### Parameters

- **Direction**: BUY or SELL
- **Base Asset**:
  - BUY: 'selectedToken'
  - SELL: SOL
- **Quote Asset**:
  - BUY: SOL
  - SELL: 'selectedToken' (must have balance)
- **Execution Time**: Immediate
- **Order Size**: Must be greater than 0
- **GAS**: Value retrieved by network conditions
- **Priority Fee**: Value set by user, must be greater than 0
- **Slippage**: Value set by user, must be greater than 0

### Limit Orders

**Triggered execution** when market conditions are met.

#### Parameters

- **Direction**: BUY or SELL
- **Base Asset**:
  - BUY: 'selectedToken'
  - SELL: SOL
- **Quote Asset**:
  - BUY: SOL
  - SELL: 'selectedToken' (must have balance)
- **Execution Time**: Triggered by condition
- **Conditional Trigger**: Can be greater than or lower than Market Cap/Price
- **Order Size**: Value must be greater than 0
- **GAS**: Value retrieved by network conditions
- **Priority Fee**: Value set by user, must be greater than 0
- **Slippage**: Value set by user, must be greater than 0

#### Optional Parameters

- **Time To Live (TTL)**:
  - Can be set in minutes, hours, or days
  - Minutes is the default
- **Take Profit**:
  - Positive target PnL expressed in percentages
  - Example: +20% profit target
- **Stop Loss**:
  - Negative target PnL expressed in percentages
  - Example: -10% loss limit

---

## Order Management

### Logging

Each operation should be **logged and displayed** in the user's trading history.

### Cancellation

Limit orders can be **canceled** if:
- They have not met their TTL threshold, OR
- Their conditions have not been met

**Cannot Cancel**:
- Orders that have been filled
- Orders that have expired (TTL reached)

---

## User Interface Design

### Token Details Screen

```
┌─────────────────────────────────────────┐
│ [← Back]  ROOSTER         [⋮ More]      │
├─────────────────────────────────────────┤
│ 🐓 ROOSTER                               │
│ Pump.fun • 2h ago                        │
│ [🐦] [💬] [🌐]                           │
│                                         │
│ ┌───────────────────────────────────┐  │
││ $0.0037 SOL                       ││  │
││ +5.2% (1m) +12.5% (5m) ...        ││  │
│└───────────────────────────────────┘  │
│                                         │
│ [📋 Copy Contract]                      │
│ abc123...xyz789                         │
│                                         │
│ ─────────────────────────────────────  │
│                                         │
│ Your Holdings                           │
│ 54,421 ROOSTER                          │
│ ≈ 0.201 SOL ($8.45)                    │
│ PnL: +10.8% (+0.018 SOL)                │
│                                         │
│ ─────────────────────────────────────  │
│                                         │
│ Market Stats                            │
│ Transactions: 1,234 (Buy: 890 Sell: 344)│
│ Volume: 125 SOL (Buy: 85 Sell: 40)     │
│ Makers: 456 (Buy: 320 Sell: 136)       │
│                                         │
│ ─────────────────────────────────────  │
│                                         │
│ [💰 Buy] [💸 Sell]                      │
│                                         │
│ ─────────────────────────────────────  │
│                                         │
│ Your Trade History                      │
│ ┌─────────────────────────────────┐    │
││ BUY  0.2 SOL → 54,421 ROOSTER   ││    │
││ 2h ago • $0.0037                 ││    │
││ [View on Explorer]               ││    │
│└─────────────────────────────────┘    │
│ ...more transactions...                 │
│                                         │
└─────────────────────────────────────────┘
```

### Market Order Modal

```
┌─────────────────────────────────────────┐
│ Buy ROOSTER                        [✕]  │
├─────────────────────────────────────────┤
│                                         │
│ You Pay (SOL)                           │
│ ┌─────────────────────────────────────┐ │
││ [1.0____________]  SOL              ││ │
││ Balance: 5.23 SOL  [Max]            ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ You Receive (≈)                         │
│ ┌─────────────────────────────────────┐ │
││ 270,270 ROOSTER                     ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ Current Price: 0.0037 SOL               │
│ Slippage: 30%                           │
│ Priority Fee: 0.008 SOL                 │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ Total Cost                          ││ │
││ Amount:      1.0 SOL                ││ │
││ Cooking Fee: 0.01 SOL               ││ │
││ Gas + Prio:  0.0081 SOL             ││ │
││ ───────────────────────────          ││ │
││ Total:       1.0181 SOL             ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ [Confirm Purchase]                      │
│                                         │
└─────────────────────────────────────────┘
```

### Limit Order Modal

```
┌─────────────────────────────────────────┐
│ Limit Order - Buy ROOSTER          [✕]  │
├─────────────────────────────────────────┤
│                                         │
│ Order Size (SOL)                        │
│ [1.0____________]  [Max]                │
│                                         │
│ Trigger When                            │
│ ○ Price  ● Market Cap                   │
│ [≤] [3,500____] USD                     │
│ Current: 3,670 USD (-4.6%)              │
│                                         │
│ ☑ Take Profit                           │
│ ┌─────────────────────────────────────┐ │
││ Target PnL: [+20___]%               ││ │
││ → Triggers at 0.00444 SOL           ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ☑ Stop Loss                             │
│ ┌─────────────────────────────────────┐ │
││ Max Loss: [-10___]%                 ││ │
││ → Triggers at 0.00333 SOL           ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ Time to Live (TTL)                      │
│ [24] [Hours ▼]                          │
│                                         │
│ [Create Limit Order]                    │
│                                         │
└─────────────────────────────────────────┘
```

---

## Mobile-Specific Considerations

### Touch Interactions
- Large touch targets for buttons
- Swipe gestures for navigation
- Pull to refresh for price updates

### Performance
- Optimize chart rendering
- Lazy load transaction history
- Cache token metadata

### Network Handling
- Graceful degradation on poor connection
- Queue orders for later submission if offline
- Clear loading states

---

## Validation & Error Handling

### Input Validation
- Order size must be > 0
- Must have sufficient balance
- Priority fee must be > 0
- Slippage must be > 0
- TP must be positive %
- SL must be negative %

### Error Messages
- Clear, actionable error messages
- Suggest solutions when possible
- Link to help documentation

### Confirmation Dialogs
- Confirm all trades before execution
- Show final costs and fees
- Allow review before submit

---

## Analytics & Tracking

### Key Metrics
- Token views
- Time spent per token
- Order creation rate (market vs limit)
- Order success rate
- TP/SL usage
- Average order size
- Cancellation rate for limit orders

---

**Status**: In development
**Priority**: Critical - Core trading functionality
**Platform**: iOS & Android
**Dependencies**: Trading engine, real-time price feeds, order management system
**Next Steps**:
1. Design mobile-optimized trading interface
2. Implement market order flow
3. Build limit order creation with TP/SL
4. Add order management (view/cancel)
5. Integrate with trading history
6. Test across various network conditions
7. Beta test with real users
