---
title: Limit Orders - 2025-08-25
type: meeting
meeting_type: technical_deep_dive
topic: Limit Orders
date: 2025-08-25
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Limit Orders Technical Discussion - Cooking.gg
**Date:** August 25, 2025
**Duration:** ~1 hour
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk

## Executive Summary
The team conducted an in-depth technical discussion on implementing advanced order types including limit orders, take profit (TP), and stop loss (SL) for both spot and perpetuals trading. Key decisions included order execution architecture, database schema design, order matching logic, and user interface patterns for order management.

## Meeting Context
As Cooking.gg expands beyond basic market orders, users require sophisticated trading tools. The team needed to architect a robust order management system that supports limit orders with TP/SL attachments, handles order lifecycle management, integrates with multiple DEXs and CEXs, and provides real-time order status updates.

## Technical Discussion

### Order Types Architecture
**Core Order Types to Implement**:
1. **Market Orders**: Immediate execution at current market price (already implemented)
2. **Limit Orders**: Execution at specified price or better
3. **Take Profit (TP)**: Conditional order to close position at profit target
4. **Stop Loss (SL)**: Conditional order to close position at loss threshold
5. **TP/SL Combined**: Single order with both profit target and loss protection

**Order Relationship Model**:
- **Primary Order**: Main limit order or position entry
- **Attached Orders**: TP/SL orders linked to primary order
- **OCO (One-Cancels-Other)**: TP and SL mutually exclusive; filling one cancels the other
- **Parent-Child Relationship**: Closing/canceling parent order automatically cancels children

### Limit Order Execution Architecture
**Execution Flow**:
1. **Order Submission**: User specifies token, side (buy/sell), quantity, limit price
2. **Validation**: Check available balance, price reasonability, minimum order size
3. **Order Placement**: Submit order to order book (on-chain or exchange)
4. **Monitoring**: Continuously check for order fills via WebSocket or polling
5. **Fill Detection**: Update order status and user balance on partial/full fill
6. **Cancellation**: Support user-initiated cancellation or auto-cancel on expiry

**Technical Challenges**:
- **On-Chain Limit Orders**: Solana DEXs handle limit orders differently (some use order books, others use AMMs with price conditions)
- **Cross-Protocol Support**: Need to abstract differences between Jupiter, Radium, Orca order mechanisms
- **Fill Notification**: Real-time detection of order fills without excessive polling
- **Partial Fills**: Handle partially filled orders and remaining quantity

### Database Schema Design
**Orders Table Structure**:
```sql
CREATE TABLE orders (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL,
  order_type VARCHAR(20) NOT NULL, -- 'market', 'limit', 'tp', 'sl'
  status VARCHAR(20) NOT NULL, -- 'pending', 'partial', 'filled', 'canceled', 'failed'
  token_address VARCHAR(64) NOT NULL,
  side VARCHAR(10) NOT NULL, -- 'buy', 'sell'
  quantity DECIMAL(20, 8) NOT NULL,
  filled_quantity DECIMAL(20, 8) DEFAULT 0,
  limit_price DECIMAL(20, 8), -- NULL for market orders
  trigger_price DECIMAL(20, 8), -- For TP/SL orders
  parent_order_id UUID, -- For TP/SL linked to primary order
  provider VARCHAR(50), -- 'jupiter', 'radium', 'hyperliquid', etc.
  transaction_signature VARCHAR(128),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  expires_at TIMESTAMP,
  metadata JSONB -- Protocol-specific data
);
```

**Indexes for Performance**:
- `idx_orders_user_status` on (user_id, status) for user order history
- `idx_orders_pending` on (status, created_at) for monitoring pending orders
- `idx_orders_parent` on (parent_order_id) for TP/SL lookups
- `idx_orders_token` on (token_address, status) for market-specific queries

### Order Monitoring & Fill Detection
**Monitoring Strategy**:
- **WebSocket Subscriptions**: Subscribe to order status updates from providers
- **Polling Fallback**: Every 10 seconds for providers without WebSocket support
- **Transaction Monitoring**: Watch blockchain for order fill transactions
- **State Reconciliation**: Hourly full state sync to catch missed updates

**Fill Detection Logic**:
```javascript
async function checkOrderFill(orderId) {
  const order = await getOrderFromDB(orderId);
  const providerStatus = await getOrderStatusFromProvider(order);

  if (providerStatus.filled_quantity > order.filled_quantity) {
    // Partial or full fill detected
    await updateOrderFillQuantity(orderId, providerStatus.filled_quantity);
    await updateUserBalance(order.user_id, order.token_address, fillDelta);
    await notifyUser(order.user_id, 'order_filled', orderDetails);

    if (providerStatus.filled_quantity === order.quantity) {
      await markOrderCompleted(orderId);
      await triggerChildOrders(orderId); // Execute TP/SL if applicable
    }
  }

  if (providerStatus.status === 'canceled' || providerStatus.status === 'expired') {
    await markOrderCanceled(orderId);
    await cancelChildOrders(orderId);
  }
}
```

### Take Profit & Stop Loss Implementation
**TP/SL Order Lifecycle**:
1. **Creation**: User sets TP/SL when entering position or adds to existing position
2. **Monitoring**: Continuously monitor current price against trigger prices
3. **Trigger Detection**: When price reaches trigger, convert to market order
4. **Execution**: Execute market order to close position
5. **OCO Handling**: Cancel opposite order (cancel SL if TP triggered, vice versa)

**Trigger Price Monitoring**:
- **Price Feed**: Use real-time price data from indexer (1-second granularity)
- **Trigger Comparison**:
  - TP triggers when price >= TP price (for longs) or <= TP price (for shorts)
  - SL triggers when price <= SL price (for longs) or >= SL price (for shorts)
- **Slippage Protection**: Add configurable slippage tolerance to account for price movement during execution

**Technical Implementation**:
```javascript
async function monitorTPSL() {
  const activeTPSL = await getActiveTPSLOrders();

  for (const order of activeTPSL) {
    const currentPrice = await getCurrentPrice(order.token_address);
    const shouldTrigger = checkTriggerCondition(order, currentPrice);

    if (shouldTrigger) {
      // Convert to market order
      const marketOrder = await createMarketOrderFromTPSL(order);
      await executeMarketOrder(marketOrder);

      // Cancel OCO order
      const ocoOrder = await getOCOOrder(order.id);
      if (ocoOrder) {
        await cancelOrder(ocoOrder.id);
      }

      // Update parent order status
      await markOrderClosed(order.parent_order_id);
    }
  }
}

// Run monitoring loop every second
setInterval(monitorTPSL, 1000);
```

### Protocol-Specific Implementations
**Jupiter Limit Orders**:
- Jupiter supports limit orders via their Limit Order API
- Orders stored on-chain in program-owned accounts
- Use WebSocket to monitor order fills
- Support partial fills and order amendments

**Radium Limit Orders**:
- Radium uses on-chain order book for limit orders
- Requires interaction with Radium OpenBook program
- Need to monitor order book state changes
- Handle order placement fees and minimum order sizes

**Hyperliquid Limit Orders** (for perpetuals):
- Native limit order support via API
- Robust WebSocket API for real-time updates
- Support advanced order types (GTC, IOC, FOK)
- Lower latency compared to on-chain solutions

### User Interface Design
**Order Entry Form**:
- **Price Input**: Large, prominent price selector with +/- buttons and direct input
- **Quantity Input**: Support both token quantity and USD value entry with auto-conversion
- **TP/SL Toggle**: Expandable section to add TP/SL to order
- **Order Preview**: Display estimated total, fees, and potential outcomes before confirmation
- **Quick Actions**: Preset buttons for common price offsets (1%, 5%, 10% from current)

**Order Management Screen**:
- **Active Orders Tab**: List of pending limit orders with current price, fill status, and quick cancel
- **Order History Tab**: Completed, canceled, and failed orders with filters by date/status
- **Order Details Modal**: Detailed view with full order parameters, fill history, and transaction links
- **Bulk Actions**: Multi-select to cancel multiple orders at once

**Mobile Adaptations**:
- Swipe to cancel order gesture
- Bottom sheet for TP/SL configuration
- Persistent notification for pending orders with quick access to management

### Order Expiration & Time-in-Force
**Supported Time-in-Force Options**:
1. **GTC (Good Till Canceled)**: Order remains active until filled or manually canceled
2. **GTT (Good Till Time)**: Order expires at specified timestamp
3. **IOC (Immediate or Cancel)**: Fill immediately at limit price or better, cancel remainder
4. **FOK (Fill or Kill)**: Fill entire order immediately or cancel entirely

**Implementation Notes**:
- GTC is default for most DEX limit orders
- GTT requires background job to auto-cancel expired orders
- IOC and FOK only supported on protocols with native support (e.g., Hyperliquid)
- Clear UI indication of selected time-in-force option

### Error Handling & Edge Cases
**Common Failure Scenarios**:
1. **Insufficient Balance**: Validate before submission, handle balance changes during pending order
2. **Price Moved**: Limit price no longer favorable, offer to update or cancel
3. **Low Liquidity**: Warn user if order size likely to cause significant slippage
4. **Protocol Downtime**: Gracefully handle API unavailability, queue retries
5. **Blockchain Congestion**: Monitor transaction confirmation, retry with higher fee if needed

**Edge Case Handling**:
- **Concurrent Modifications**: Handle user canceling order while fill is processing
- **Partial Fill Cancellation**: Support canceling unfilled portion of partially filled order
- **TP/SL Trigger Simultaneously**: Define priority (typically SL takes precedence)
- **Order Book Removal**: Detect if order removed from book without fill (e.g., market shutdown)

## Key Technical Decisions
- **Decision 1:** Use unified order table with polymorphic type column - Simplifies queries and maintains consistency across order types
- **Decision 2:** Implement TP/SL as child orders with parent-child relationship - Provides clean data model and simplifies OCO logic
- **Decision 3:** 1-second polling frequency for TP/SL trigger monitoring - Balances responsiveness with system load
- **Decision 4:** Support GTC and GTT time-in-force options initially - Covers majority of use cases; IOC/FOK deferred to future
- **Decision 5:** WebSocket primary with polling fallback for order monitoring - Ensures real-time updates with reliability

## Architecture & Design Considerations
- **Idempotency**: Ensure order submissions and cancellations are idempotent to handle retries safely
- **Audit Trail**: Log all order state transitions for debugging and compliance
- **Rate Limiting**: Implement user-level rate limits on order submissions to prevent abuse
- **Fee Calculation**: Accurately calculate and display all fees (network, protocol, platform) before submission
- **Order Validation**: Comprehensive validation on both frontend and backend

## Performance & Scalability Notes
- **Order Monitoring Load**: With 1000 concurrent pending orders, expect ~1000 DB queries/sec for monitoring
- **Optimization**: Batch order status checks per provider to reduce API calls
- **Caching**: Cache current prices in Redis to avoid repeated indexer queries
- **Database Indexes**: Critical for fast queries on large order history tables
- **Background Jobs**: Use job queue (e.g., Bull, BullMQ) for order monitoring and expiration

## Action Items
- [ ] **Martin**: Implement orders table schema and migrations
- [ ] **Eduardo**: Build order monitoring service with WebSocket and polling support
- [ ] **Lucas**: Design order entry and management UI screens
- [ ] **Martin**: Integrate Jupiter Limit Order API
- [ ] **Eduardo**: Implement TP/SL trigger detection logic
- [ ] **Team**: Define test scenarios covering all order states and edge cases

## Follow-up Items
- Evaluate advanced order types (trailing stop, OCO standalone, bracket orders)
- Plan for conditional orders based on multiple criteria
- Determine analytics to track (fill rate, average time to fill, cancellation rate)
- Design API for programmatic order management (for power users/bots)

## Technical References
- Jupiter Limit Order API: https://station.jup.ag/docs/limit-order/limit-order-api
- Radium OpenBook Program: https://docs.raydium.io/raydium/protocol/openbook-integration
- Hyperliquid Order Types: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/order-types
- OCO Order Pattern: https://www.investopedia.com/terms/o/oco.asp

---
**Recording:** Transcription available
**Related Documents:**
- Order Management Requirements (04-knowledge-base/business/requirements/)
- Trading Engine Architecture (04-knowledge-base/technical/)
