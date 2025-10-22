---
title: Beta Release Specifications - October 17, 2025 Launch
type: requirements
date: 2025-08-11
updated: 2025-10-21
status: completed
tags:
  - beta-release
  - product-specifications
  - desktop-features
  - mobile-features
  - release-planning
  - closed-beta
  - referral-only
summary: Comprehensive specifications for October 17, 2025 closed beta release including desktop and mobile iOS features. Successfully launched with referral-only access model, 99.9% uptime, and 3-second transaction completion time.
source-decisions:
  - ADR-200: Multilevel Referral Program Structure
  - ADR-201: Closed Beta via Referral-Only Access
  - ADR-203: September Beta Launch Timeline (revised to October 17)
  - ADR-401: Biometric Authentication for Mobile Trading
---

# Q3 2025 Beta Release Specifications

## Desktop Platform

### Authentication & Login

**Social Login Options**:
- Telegram
- Google
- Apple
- Twitter
- Solana Wallet

**Implementation**:
- No KYC required for signup
- Default login method set on signup
- Fallback methods can be enabled later

### The Kitchen (Token Discovery Hub)

#### Core Components

**Stove**: Real-time token streaming during bonding curve phases
- Just Prepped
- Simmering Nicely
- Plated Up

**Specials**: Token categorization by performance
- Trending
- Gainers
- Losers
- Sortable by timeframe

#### Trading Features

**Fee Settings**:
- Quick priority fee management
- Slippage configuration
- Accessible from Kitchen interface

**Quick Buy**:
- Enable/disable toggle
- Configurable order size
- Kitchen card integration

#### Advanced Filtering (Desktop Only)

Filter criteria:
- Launchpad/protocol
- Social presence (minimum 1 social link)
- Top 10 holders percentage
- Developer holdings
- Holder count
- Liquidity levels
- Volume metrics
- Market cap ranges
- Transaction counts
- Buy/sell ratios

#### Search & Discovery

**Global Search**:
- Available platform-wide
- Keyboard shortcut: Cmd+K (Mac) / Ctrl+K (Windows)
- Search by name or contract address

**Supported Protocols**:
- Direct Kitchen access:
  - Pump.Fun
  - Pump.Swap
  - Moonshot
  - Moonit
  - Raydium
  - Let'sBonk.Fun
- Via Search/Custom Orders:
  - Jupiter aggregator (~50 protocols)

**Quick Operations Panel**:
- Modal for rapid buy/sell operations
- Accessible when selecting positions from global ribbon

### Portfolio Management

**Active Positions**:
- Comprehensive position table
- Current wallet association
- Real-time updates

**Trade History**:
- Complete transaction log
- Wallet-specific filtering

**Activity Breakdown Charts**:
- Historical holdings visualization
- Categories:
  - Invested
  - Sold
  - Holding

### Wallet Manager

#### Cooking Wallets

Features:
- Create new wallet
- Import external Solana wallets
- Copy address functionality
- Export seed phrase
- Name customization
- Archive capability

#### Withdraw Wallets

Management options:
- Create withdraw wallet
- Copy address
- Update naming
- Delete functionality

#### Transaction Operations

- **Deposit**: Solana funding
- **Withdraw**: Saved or external addresses
- **Transfer**: Between Cooking wallets

#### Security

**Security Password**:
- Required for sensitive actions
- Password creation flow
- Update capability

**Wallet History**:
- Complete transaction log
- Internal and external interactions

### Custom Orders System

**Automatic Features**:
- Network-based priority fee suggestions

#### Market Orders

**Description**: Spot swaps between SOL and tokens

**Parameters**:
- Direction: BUY/SELL
- Order Size: Minimum 0.000001 SOL
- Gas Fee: Variable with network
- Slippage: 30% default, directional
- Priority Fee: 0.008 SOL default
- Platform Fee: 1% commission

#### DCA (Dollar Cost Averaging)

**Description**: Scheduled market orders over time

**Additional Parameters**:
- Execution Interval (Minutes/Hours/Days)
- Pause/resume capability
- Cancellation option

#### Limit Orders

**Description**: Conditional swaps based on thresholds

**Trigger Options**:
- Market Cap thresholds
- Price targets
- Greater than/lower than operators

**Optional Parameters**:
- Time To Live (TTL)
- Take Profit (BUY orders only)
- Stop Loss (both directions, SELL limited to SL only)

#### TWAP (Time-Weighted Average Price)

**Description**: Large order distribution algorithm

**Parameters**:
- Total order size
- Execution duration
- Interval options: 1min, 5min, 30min, 1hr
- Optional price limits

#### VWAP (Volume-Weighted Average Price)

**Description**: Volume-based execution strategy

**Parameters**:
- Reference period for volume monitoring
- Volume percentage for sizing
- Execution intervals
- Optional price limits

#### Custom Orders

**Description**: Advanced multi-condition limit orders

**Condition Stack (2-7 conditions)**:
- Liquidity thresholds
- Top 10 holder percentage
- Developer selling activity
- Holder count changes
- Price change percentages (1m/5m/1h/24h)
- Average holding time
- Market cap/price limits

**Features**:
- All conditions must be met (AND logic)
- Independent TP/SL execution
- Most flexible order type

### Additional Features

**Charts**:
- Candle charts for all tokens
- TradingView Advanced Charts integration

**Position Management**:
- Real-time position table
- Token holdings display

**Order Management**:
- Future order visibility
- Audit capabilities
- Pause/cancel functions
- Trade history per order type

### Positions Modal

- Global access via sidebar
- Available from any platform location
- Complete position overview

### Multi Chart View

- Support for 4 simultaneous charts
- Different token comparison
- Price movement mapping

### Referral Program

**Features**:
- Automatic link association on signup
- One-time custom code creation
- Referral sharing tools
- Reward claiming interface
- Historical rewards tracking
- Referral list visibility
- Multi-level structure with tiered bonuses
- Self-trade incentives

### Token Details

**Transaction Data**:
- Protocol-specific logging via indexer

**Holder Information**:
- Balance in SOL and USD
- Token amounts
- Supply percentage

**Rankings & Analytics**:
- PnL-based holder ranking
- Advanced candle charts
- Bubblemaps integration

**Token Metrics**:
- User holdings and sales
- PnL calculations
- Timeframe-based analysis
- Transaction statistics
- Volume metrics
- Individual wallet interactions
- Market cap, liquidity, bonding curve data

**Trading Integration**:
- Direct token operations from details page

### Perpetuals Trading

#### Bridge Functionality

**Solana to USDC Conversion**:
- Fast (expensive) method
- Slow (cheaper) method
- Cooking fee included

#### Trading Interface

**Features**:
- Dedicated contract search UI
- Position management dashboard
- LONG and SHORT operations
- Market and Limit orders
- Take Profit and Stop Loss for limits
- Per-asset leverage management

## Mobile iOS Platform

### Authentication & Login

**Social Login Methods**:
- Telegram
- Google
- Apple
- Twitter
- Solana Wallet

**Implementation**:
- Turnkey integration
- Default method selection
- Fallback method configuration
- Mandatory referral choice after T&C
- Invite code validation

### Home Screen (Kitchen)

**Token Discovery Hub**:
- Real-time WebSocket updates
- Continuous token streaming

**Content Sections**:

*Stove*:
- Just Prepped
- Simmering Nicely
- Plated Up

*Specials*:
- Trending
- Gainers
- Losers
- Timeframe selection

**Search Functionality**:
- Global token search
- Name or contract address
- All protocol support

**Quick Buy**:
- Kitchen-exclusive feature
- SOL quote asset only
- Default: 0.01 SOL, 0.008 priority, 30% slippage
- Immediate execution
- Balance validation

**Native Components**:
- iOS design patterns
- Optimized performance

### Token Details

**Essential Information**:
- Market cap
- Liquidity
- Price movements
- Basic candle chart

**User Data**:
- Current position
- Amount sold
- PnL with timeframe
- Pending orders

**Trading Access**:
- Market orders
- Basic limit orders

### Wallet Management

**Simplified Operations**:
- Balance viewing
- Position overview
- Basic deposit/withdraw
- Multi-wallet switching

**Fiat On-Ramp**:
- Onramper widget integration
- Apple Pay support

**Security**:
- Integrated security password

### Portfolio View

**Features**:
- Active positions table
- Trade history
- Essential information only

### Trading Capabilities

#### Market Orders

**Simplified Interface**:
- BUY/SELL direction
- Minimum 0.000001 SOL
- 30% default slippage
- 0.008 SOL priority fee
- 1% platform commission

#### Basic Limit Orders

**Parameters**:
- BUY/SELL direction
- Market Cap OR Price triggers
- Greater than/lower than operators
- Optional TTL

### Settings & Preferences

**Display Configuration**:
- SOL/USD toggle
- Cross-platform sync

**Referral Access**:
- Settings menu entry
- Invite code input

### User Experience

**Design Philosophy**:
- Non-crypto native focus
- Clear navigation indicators
- Minimal customization
- Brand identity preservation

**Performance**:
- Native iOS components
- Smooth animations
- Real-time updates
- No manual refresh needed

**Companion App**:
- Streamlined features
- Position monitoring focus
- Basic trading operations

## Platform Integration

Both desktop and mobile platforms share:
- Unified backend infrastructure
- Cross-platform wallet synchronization
- Consistent security protocols
- Shared referral program
- Real-time data feeds

## Beta Launch Summary

**Launch Date**: October 17, 2025
**Launch Type**: Closed Beta - Referral-Only Access (ADR-201)
**Status**: ✅ Successfully Launched

### Launch Metrics

**Performance**:
- **Transaction Completion**: 3 seconds (down from 5-6 seconds pre-launch)
- **Uptime**: 99.9% achieved
- **Query Performance**: 15x improvement from ClickHouse migration

**User Acquisition**:
- **Launch Strategy**: Closed beta via referral-only access
- **Referral Model**: 25-50 slots per referral code during beta
- **Initial Users**: 5 users on October 20, expanded to 30-40 on October 27
- **Growth Mechanism**: 3-level multilevel referral program (ADR-200)

### Key Features Deployed

**Desktop Platform** ✅:
- Auth0 social login (Twitter, Google, Apple, Telegram, Solana Wallet)
- Full trading suite (Market, Limit, DCA, TWAP, VWAP, Custom Orders)
- Hyperliquid perpetuals integration (with US geolocation workaround)
- TradingView advanced charts
- Multilevel referral program (30-55% commission structure)
- ClickHouse-powered analytics (15x performance improvement)
- Security password for wallet operations

**Mobile iOS Platform** ✅:
- Native iOS app with Auth0 social login
- Biometric authentication (Face ID/Touch ID) for trading (ADR-401)
- Home screen token discovery (Kitchen)
- Market and basic limit orders
- Wallet management with Turnkey integration
- Onramper fiat on-ramp
- Security password with biometric fallback
- Cross-platform synchronization

### Timeline Revision

**Original Timeline**: September 2025 beta launch (ADR-203)
**Revised Timeline**: October 17, 2025
**Reason**: Feature freeze for stability (August-October), ensuring production-ready quality over speed

### Post-Launch Status

**Current Phase**: Production Beta
**Access Model**: Referral-only (closed beta continuing)
**Focus Areas**:
- User feedback integration
- Performance monitoring
- Mobile app completion
- Referral program optimization

## Cross-References

- Related to: [[roadmap-q2-q3-2025]] - Development timeline
- Related to: [[stakeholder-requirements]] - Requirements driving features
- Related to: [[platform-user-documentation]] - User guide for beta features
- Related to: [[mobile-app-prd]] - Detailed mobile specifications
- See: [ADR-201: Closed Beta via Referral-Only Access](../../02-decisions/2025-08-11-closed-beta-referral-only-access.md)
- See: [ADR-203: September Beta Launch Timeline](../../02-decisions/2025-08-11-september-beta-launch-timeline.md)