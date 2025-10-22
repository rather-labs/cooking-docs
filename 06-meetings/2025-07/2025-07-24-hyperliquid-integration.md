---
title: Hyperliquid Integration - 2025-07-24
type: meeting
meeting_type: technical_deep_dive
topic: Hyperliquid
date: 2025-07-24
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Marcos Tacca]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Hyperliquid Integration Technical Discussion - Cooking.gg
**Date:** July 24, 2025
**Duration:** ~1 hour 15 minutes
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Marcos Tacca

## Executive Summary
The team conducted a comprehensive technical discussion on integrating Hyperliquid perpetuals trading into Cooking.gg. Key decisions included implementing cross-margin trading, handling API geoblocking restrictions, developing a comprehensive permissions system, and establishing proper market data synchronization strategies.

## Meeting Context
Following Sain's request to integrate perpetuals trading capabilities, the team needed to evaluate Hyperliquid as the chosen platform, understand API constraints, design the technical architecture for cross-margin vs isolated margin trading, and establish integration patterns that align with Cooking's existing spot trading infrastructure.

## Technical Discussion

### Hyperliquid Platform Architecture
The team reviewed Hyperliquid's technical specifications:
- **API Access**: Uses both REST API and WebSocket connections for real-time data
- **Geoblocking**: Hyperliquid implements geographic restrictions blocking US and sanctioned countries
- **Workaround Strategy**: Team identified that using VPN connections through non-blocked regions (Argentina, Brazil, Mexico, Europe) allows API access
- **Infrastructure Decision**: Deploy backend services in geographically compliant regions to handle all Hyperliquid API communications

### Cross-Margin vs Isolated Margin Implementation
**Critical Decision**: Implement cross-margin as the default and only margin mode for initial release

**Technical Rationale**:
- **Simplified User Experience**: Cross-margin provides automatic risk management across all positions
- **Reduced Liquidation Risk**: Entire account balance acts as collateral, reducing likelihood of position-specific liquidations
- **Lower Maintenance Requirements**: Single collateral pool eliminates need for per-position margin management UI
- **API Simplicity**: Hyperliquid's cross-margin mode requires fewer API calls and simpler order management logic

**Implementation Approach**:
- Display total available margin prominently in UI
- Show aggregate P&L across all positions
- Implement portfolio-level risk metrics rather than position-level
- Defer isolated margin implementation to future iteration based on user demand

### Position Management & Order Types
**Core Features for MVP**:
1. **Market Orders**: Immediate execution at best available price
2. **Limit Orders**: Execution at specified price or better
3. **Take Profit (TP)**: Automatic position closure at profit target
4. **Stop Loss (SL)**: Automatic position closure at loss threshold

**Technical Specifications**:
- **TP/SL Architecture**: Implemented as separate orders linked to main position
- **Order Modification**: Support editing TP/SL levels after position entry
- **Cancellation Logic**: Closing main position automatically cancels associated TP/SL orders
- **WebSocket Monitoring**: Real-time tracking of order status changes and fills

### Permissions System Architecture
**Requirement**: Granular control over user access to perpetuals features

**Proposed Permission Levels**:
1. **View Only**: Read access to perpetuals markets and prices
2. **Trade Enabled**: Full trading capabilities (create/modify/cancel orders)
3. **Funding Operations**: Deposit/withdrawal permissions for margin account
4. **Admin**: Full access including sub-account management

**Technical Implementation**:
- Backend permission checks before API call execution
- Frontend UI elements conditionally rendered based on permissions
- Permission verification on each WebSocket message
- Audit logging of all permission-gated actions

### Market Data & Price Feeds
**Data Synchronization Strategy**:
- **WebSocket Primary**: Real-time orderbook and trade data via WebSocket
- **REST API Fallback**: Polling mechanism if WebSocket disconnects
- **Update Frequency**: Tick-by-tick for active markets, 1-second aggregation for UI rendering
- **Historical Data**: Fetch OHLCV data from Hyperliquid's historical endpoints

**Orderbook Management**:
- Maintain local orderbook state from WebSocket updates
- Implement orderbook snapshot refresh every 30 seconds
- Display configurable depth (default: 10 levels each side)
- Calculate mid-market price, spread, and liquidity metrics

### Account State Management
**Critical Technical Challenge**: Synchronizing account state between Cooking's backend and Hyperliquid

**Solution Architecture**:
1. **Initial State Sync**: Fetch complete account state on user login
2. **WebSocket Updates**: Subscribe to account-specific channels for real-time updates
3. **Reconciliation**: Periodic full state refresh every 60 seconds to catch any missed updates
4. **Conflict Resolution**: Hyperliquid state is source of truth; local state updates on mismatch

**State Components**:
- Available margin balance
- Active positions (size, entry price, unrealized P&L)
- Open orders (all types: market, limit, TP, SL)
- Position history and trade history
- Funding payments received/paid

### Risk Management Features
**Mandatory Risk Controls**:
1. **Max Position Size**: Configurable limit per market
2. **Max Leverage**: Cap at platform maximum (50x on Hyperliquid)
3. **Daily Loss Limit**: Circuit breaker to prevent catastrophic losses
4. **Price Impact Warnings**: Alert users when order would significantly move market

**Pre-Trade Validation**:
- Verify sufficient margin before order submission
- Check position size limits
- Calculate estimated liquidation price
- Display margin utilization percentage

## Key Technical Decisions
- **Decision 1:** Implement cross-margin only for MVP - Simplifies UX and reduces development complexity while providing better risk management for most users
- **Decision 2:** Deploy backend services in non-geoblocked regions - Ensures reliable API access while complying with Hyperliquid's restrictions
- **Decision 3:** WebSocket-primary architecture with REST fallback - Provides real-time updates with resilience against connection issues
- **Decision 4:** Build comprehensive permissions system - Enables gradual rollout and proper access control for different user segments
- **Decision 5:** Hyperliquid as source of truth for account state - Prevents state synchronization bugs by always deferring to upstream platform

## Architecture & Design Considerations
- **Microservices Pattern**: Separate perpetuals trading service from spot trading infrastructure
- **State Management**: Implement robust state synchronization with conflict resolution
- **Error Handling**: Comprehensive retry logic for API failures with exponential backoff
- **WebSocket Resilience**: Automatic reconnection with state resync on connection loss
- **UI/UX Consistency**: Match interaction patterns from spot trading interface

## Performance & Scalability Notes
- **API Rate Limits**: Hyperliquid enforces rate limits; implement request queuing and throttling
- **WebSocket Efficiency**: Single WebSocket connection per user session, multiplexed for all subscriptions
- **Database Design**: Separate tables for perpetuals positions and orders to avoid schema conflicts with spot trading
- **Caching Strategy**: Cache market metadata (tick sizes, lot sizes) with 1-hour TTL

## Action Items
- [ ] **Eduardo**: Research VPN infrastructure options for backend deployment in compliant regions
- [ ] **Martin**: Design database schema for perpetuals positions, orders, and trade history
- [ ] **Lucas**: Draft user-facing documentation explaining cross-margin concepts
- [ ] **Team**: Create technical specification document detailing all API endpoints and WebSocket channels needed
- [ ] **Martin**: Implement Hyperliquid API client library with authentication and WebSocket support
- [ ] **Eduardo**: Set up monitoring and alerting for API health and WebSocket connection stability

## Follow-up Items
- Determine exact permission model and user segments for phased rollout
- Evaluate whether to support multi-account trading (sub-accounts on Hyperliquid)
- Plan testing strategy including testnet usage before mainnet deployment
- Design mobile-specific UI for perpetuals trading

## Technical References
- Hyperliquid API Documentation: https://hyperliquid.gitbook.io
- WebSocket API Reference: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/websocket
- Cross-Margin Mechanics: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/cross-and-isolated-margin

---
**Recording:** Transcription available
**Related Documents:**
- Perpetuals Trading Requirements (to be created in 04-knowledge-base/business/requirements/)
- Hyperliquid Integration Architecture Doc (to be created)
