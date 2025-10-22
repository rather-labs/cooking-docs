---
title: August 2025 - Meetings
type: index
date: 2025-10-21
summary: Index of Cooking.gg meeting notes from August 2025, covering advanced order types, weekly demos, and daily standups.
---

# August 2025 - Meetings

This directory contains structured meeting notes from Cooking.gg meetings during August 2025.

## Overview

**Period Covered:** August 2025
**Meeting Types:** Weekly Demos, Daily Standups, Technical Deep Dives, Weekly Syncs
**Team:** Cooking.gg Development Team
**Language:** English (translated from Spanish)

## Files

### Technical Deep Dive Meetings (Batch 10)
- `2025-08-25-limit-orders.md` - Advanced order types implementation (Limit, TP/SL)

### Weekly Demo Meetings
- `2025-08-01-cooking-demo.md` - Weekly product demonstration
- `2025-08-08-cooking-demo.md` - Weekly product demonstration
- `2025-08-15-cooking-demo.md` - Weekly product demonstration
- `2025-08-22-cooking-demo.md` - Weekly product demonstration
- `2025-08-29-cooking-demo.md` - Weekly product demonstration

### Weekly Syncs
- `Cooking-Weekly-Sync-2025-08-18.md` - Team synchronization meeting
- `Cooking-Weekly-Sync-2025-08-25.md` - Team synchronization meeting
- `Sync-Z-Lucas-2025-08-18.md` - Leadership sync
- `Sync-Z-Lucas-2025-08-25.md` - Leadership sync

### Daily Standups
- `2025-08-01-daily-standup.md` through `2025-08-29-daily-standup.md` (13 meetings)

### Monthly Summary
- `2025-08-summary.md` - Comprehensive August overview

## Major Themes

### Advanced Order Types (August 25)
Comprehensive technical design for limit orders with TP/SL support:

- **Order Types**: Market, Limit, Take Profit, Stop Loss, Combined TP/SL
- **Order Relationships**: Parent-child model with OCO (One-Cancels-Other) logic
- **Database Schema**: Unified orders table with polymorphic type column
- **Order Monitoring**: WebSocket primary with polling fallback
- **Protocol Support**: Jupiter, Radium, Hyperliquid integrations
- **Time-in-Force**: GTC (Good Till Canceled) and GTT (Good Till Time)

## Technical Highlights

### Order Management System
**Architecture**:
- Unified database schema for all order types
- Parent-child relationships for TP/SL attached to primary orders
- 1-second polling for TP/SL trigger monitoring
- Real-time fill detection via WebSocket subscriptions

**Order Lifecycle**:
1. Submission → Validation → Placement
2. Monitoring → Fill Detection → Status Update
3. Completion or Cancellation → Cleanup

**Key Features**:
- Partial fill handling
- Order expiration and auto-cancellation
- TP/SL trigger price monitoring
- OCO logic (filling one cancels the other)

### Protocol-Specific Implementations
**Jupiter Limit Orders**:
- Native API support via Jupiter Limit Order API
- WebSocket monitoring for fills
- Partial fill support

**Radium Limit Orders**:
- OpenBook integration for on-chain order book
- Order placement fees and minimum sizes
- State change monitoring

**Hyperliquid Limit Orders**:
- Native support with advanced order types
- GTC, IOC, FOK support
- Lower latency than on-chain solutions

### Database Design
**Orders Table**:
- UUID primary key
- Order type, status, side, quantities, prices
- Parent-child relationships via `parent_order_id`
- Provider-specific metadata in JSONB column
- Critical indexes for performance

### User Interface
**Order Entry**:
- Price and quantity inputs with validation
- TP/SL expandable configuration section
- Order preview with fees and estimates
- Quick action buttons for common price offsets

**Order Management**:
- Active orders with real-time status
- Order history with filtering
- Bulk cancellation support
- Detailed order modal with full history

## Key Decisions

### Technical Architecture
- **Decision**: Unified order table with polymorphic design - Simplifies queries and consistency
- **Decision**: TP/SL as child orders with OCO logic - Clean data model
- **Decision**: 1-second trigger monitoring frequency - Balances responsiveness with load
- **Decision**: WebSocket primary with polling fallback - Real-time with reliability
- **Decision**: Support GTC and GTT initially - Covers majority use cases

### Order Monitoring
- **Decision**: Hybrid monitoring approach (WebSocket + periodic polling)
- **Decision**: Hourly full state reconciliation to catch missed updates
- **Decision**: Idempotent order operations for safe retries

## Critical Issues & Solutions

### Order Fill Detection
- **Challenge**: Real-time detection without excessive API calls
- **Solution**: WebSocket subscriptions with 10-second polling fallback

### TP/SL Triggering
- **Challenge**: Accurate trigger detection with price volatility
- **Solution**: 1-second monitoring loop with slippage protection

### Partial Fills
- **Challenge**: Managing partially filled orders
- **Solution**: Track filled_quantity separately, support canceling unfilled portion

### Cross-Protocol Differences
- **Challenge**: Each DEX/CEX has different order mechanisms
- **Solution**: Abstraction layer with provider-specific implementations

## Action Items Carried Forward

### Development
- [ ] Implement orders table schema and migrations
- [ ] Build order monitoring service with WebSocket support
- [ ] Integrate Jupiter Limit Order API
- [ ] Implement TP/SL trigger detection logic
- [ ] Design order entry and management UI

### Testing
- [ ] Define test scenarios for all order states
- [ ] Test edge cases (concurrent modifications, fills during cancellation)
- [ ] Load test monitoring system with 1000+ pending orders

### Future Enhancements
- [ ] Evaluate advanced order types (trailing stop, bracket orders)
- [ ] Plan conditional orders based on multiple criteria
- [ ] Design programmatic order management API

## Meeting Attendance

**Regular Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Marcos Tacca, and extended team

---

**Note:** These meetings were originally conducted in Spanish and have been translated to English while preserving technical terminology.
