---
title: Support and Trade Perpetuals through HyperLiquid DEX
type: feature-specification
status: active
priority: high
created: 2025-05-29
date: 2025-10-21
updated: 2025-10-21
tags: [perpetuals, derivatives, hyperliquid, trading, integration, geolocation, vpn]
related:
  - "[[trading-methods]]"
  - "[[platform-vision-requirements]]"
  - "[[roadmap-q2-q3-2025]]"
source-meetings:
  - 2025-07-24-hyperliquid-integration.md
  - 2025-07-25-cooking-demo.md
  - 2025-07-30-daily-standup.md
---

# HyperLiquid Perpetuals Integration

## Overview

In order to enable Cooking traders the ability to operate perpetual contracts we will integrate HyperLiquid's DEX solution since it supports over 100+ assets, with new ones being added as the community deems them relevant.

## Value Proposition

To provide a perpetual trading experience that is enticing enough to keep the trader logged in to Cooking as opposed to just jumping into HyperLiquid's DEX, we will introduce two factors:

### 1. HyperLiquid's Referral Program

- All traders that log into the DEX through Cooking will be referred users
- **User Benefit**: 4% fee discount on their first $25 million dollars of traded volume
- **Cooking Requirement**: First acquire referral code by trading $10,000.00 in volume
- **Cooking Benefit**: Receive 10% commission on fees applied to operations performed by these referrals

### 2. Solana Wallet Compatibility and Spot Trade

- Cooking traders can move their own SOL to the DEX using native Solana addresses
- Once liquidity is deposited, use HyperLiquid's Spot trading feature to execute a sell on the pair SOL/USDC
- Immediately credits the user with assets necessary to operate perpetual contracts
- **Note**: This operation will have a certain operational fee charged by Cooking
- **Optional**: Bundled deposits (cheaper but slower) - explained below

## Fee Structure

It is important to note that we will **not include an extra fee layered on top** of the fees charged by the DEX:

- No technical possibility through the available APIs
- Same methodology carried out by competitors such as Axiom
- Competitors give users cashback on each transaction

## Implementation Roadmap

### Phase 1: Initial Delivery (Priority)

**Scope**:
- Bridge IN/OUT native Solana and swap to USDC using HyperLiquid's DEX
- Search supported perpetual contracts
- Display perpetual contract relevant information
- Open and Close Market orders, including:
  - TP/SL (Take Profit / Stop Loss)
  - Cross margin
  - All available leverage points per contract
- Include Perpetuals in:
  - 'Portfolio'
  - 'Trade History'
  - 'Positions'

### Phase 2: Advanced Features

**Scope**:
- Create Isolated Margin orders
- Update Isolated Margin orders
- Order Book display
- Open and Close Limit Orders, including order parameters such as:
  - IOC (Immediate Or Cancel)
  - GTC (Good Till Cancelled)
  - ALO (Add Liquidity Only)
  - TP/SL
  - Reduce Only

**Rationale**: More complex features demand more thorough testing and a bigger amount of potential edge cases to brace for.

## Technical Challenges

### US Geolocation Restrictions and Workaround

**Challenge Identified**: HyperLiquid implements geographic restrictions blocking US and sanctioned countries

**Background** (July 2025):
- HyperLiquid Terms explicitly prohibit trading or accessing from the US
- Initial testing revealed Ohio AWS servers are geoblocked
- Users from non-sanctioned countries accessing via Cooking would effectively use it as a VPN
- Legal liability concerns regarding circumventing geo-restrictions

**Implemented Solution** (July 2025):
- **Infrastructure Decision**: Deploy backend services in geographically compliant regions
- **VPN Strategy**: Use VPN connections through non-blocked regions (Argentina, Brazil, Mexico, Europe)
- **API Access**: Backend handles all Hyperliquid API communications from compliant locations
- **User Protection**: Users interact only with Cooking backend, not directly with Hyperliquid
- **Legal Compliance**: Backend operates in regions where Hyperliquid access is permitted

**Technical Implementation**:
```
User (Any Location)
    ↓
Cooking.gg Frontend
    ↓
Cooking Backend (Deployed in Compliant Region: Argentina/Brazil/Mexico/Europe)
    ↓ (VPN if needed)
Hyperliquid API
```

**Status**: ✅ Resolved - Backend deployed in compliant regions, successfully operational for October 17, 2025 beta launch

### Client-Side Data Acquisition

We have found several technical difficulties during research and assessment, mainly on acquiring live data on perpetual contracts:

**Required Data**:
- Last traded price
- Mark price
- Liquidation price
- Oracle price
- 24h Change
- Other real-time metrics

**Issue**: HyperLiquid does not provide a public method for integration

**Status**: Resolved during implementation

**Priority**: Resolving this topic should be of the upmost importance

## Referral Program Setup

### Registering Cooking Users as HL Referrals

**Requirement**: Cooking must acquire a custom referral code

**Process**:
1. Trade a total notional volume of $10,000.00 USD in perpetual contracts
2. Custom referral code becomes available
3. All incoming users registered as referred traders

**Account Creation**:
- May be able to log in to HyperLiquid using an email
- Avoids having direct access to the client wallet's private key

## Bridge Solution

### Overview

It is paramount that users receive immediate access to USDC liquidity on Arbitrum since that is the quoting asset for perpetual contracts.

### Pseudo-Bridge Implementation

**Process**:
1. User sends native Solana from a Cooking wallet to HyperLiquid Spot wallet
2. Automatically execute spot sell on pair SOL/USDC in HyperLiquid
3. Transfer resulting USDC (now on Arbitrum) to Perpetuals wallet
4. Speed: As fast as each individual action concatenated can be

**Fees**: Each operation fee + additional Cooking fee

### Batched Bridge (Slow Mode)

Traders can reduce operational costs by opting for a slower bridge methodology that relies on batching transactions.

#### Two Bridge Modes

**1. Fast Mode**:
- One-to-one deposit of SOL into HL spot wallet
- Immediate spot swap for USDC
- Transfer into perpetuals wallet
- Chain is seamless and transparent
- **Trade-off**: All costs paid by user, fastest possible conversion

**2. Slow Mode**:
- Many-to-one deposit of SOL into intermediate Cooking wallet
- **Minimum requirement**: 0.2 SOL before transferring
- Transfer into HL spot wallet
- Execute spot swap for USDC
- Transfer corresponding funds to Perpetual wallets of each user
- **Trade-off**: Slower due to minimum requirement, but gas fee shared between users

**Withdrawal**: Both methods are equal and opposite for withdrawals

**Account Creation**: Automatic account creation on HL enabled if user operates perpetuals for first time and selects slow mode

## Perpetuals Data Requirements

### Market Information

Cooking will allow users to search and operate any perpetual contract supported on HyperLiquid DEX.

**Contract Data**:
- Information to populate charts
- **Mark Price**: Contract's fair price
- **Oracle**: Median of external prices reported by validators, used for computing funding rates
- **24h Change**: 24-hour price change percentage
- **24h Volume**: 24-hour trading volume
- **Open Interest**: Total outstanding position of all users on this contract
- **Funding / Countdown**: Fee that long holders pay shorts or viceversa per cycle to keep funding as close as Mark price as possible

### Position Data

- Coin
- Size
- Position Value
- Entry Price
- Mark Price
- PnL (ROE%)
- Liq Price (Liquidation Price)
- Margin
- Funding
- TP/SL

### Trade History

- Time
- Coin
- Direction
- Price
- Size
- Trade Value
- Fee
- Closed PnL

### Funding History

- Time
- Coin
- Size
- Position Side
- Payment
- Rate

### Order History

- Time
- Type
- Coin
- Direction
- Size
- Filled Size
- Order Value
- Price
- Reduce Only
- Trigger Condition
- TP/SL
- Status
- Order ID

## Market Orders: Open and Closing

### Order Capabilities

Cooking will allow users to open market orders for each available contract listed on HyperLiquid on either direction (long/short).

### Order Configuration

**Leverage**:
- User can modify default leverage value per contract parameters

**Balance Calculation**:
- User can open positions according to available balance in Perpetual wallet
- **Available Balance** = totalBalance - lockedMargin
- Display total holding of current open positions

### Order Size Requirements

**Minimum Size**:
- Order must declare size bigger than 10 USD or equivalent in baseAsset
- Alternatively, declare size as percentage of maximum order size based on leverage
  - Example: If balance is 20 USD and max leverage is x40, max order = 800 USD, 25% = 200 USD

**Margin Calculation**:
- HyperLiquid will not register order unless trader has enough balance to lock for opening margin
- Formula: `position_size * mark_price / leverage`

### Order Parameters

**Each Market order can include**:
- Up to one (optional) Take Profit
- Up to one (optional) Stop Loss
- Reduce Only parameter (optional)

## Security Considerations

- Secure handling of bridged funds
- Transaction validation and confirmation
- Slippage protection during bridge operations
- Error handling for failed transactions

## User Experience Considerations

- Clear communication of bridge modes and trade-offs
- Real-time status updates during bridge process
- Transparent fee breakdown
- Education about perpetuals trading risks

---

## Implementation Status

**Overall Status**: ✅ Active - Deployed with October 17, 2025 beta launch

### Phase 1: Initial Delivery ✅ Complete
- ✅ Bridge IN/OUT native Solana and swap to USDC using HyperLiquid's DEX
- ✅ Search supported perpetual contracts
- ✅ Display perpetual contract relevant information
- ✅ Open and Close Market orders with TP/SL, cross margin, all available leverage points
- ✅ Perpetuals integrated in Portfolio, Trade History, and Positions
- ✅ US geolocation workaround implemented (backend in compliant regions)

### Phase 2: Advanced Features 🔄 In Progress
- Isolated Margin orders (create and update)
- Order Book display
- Limit Orders with advanced parameters (IOC, GTC, ALO, TP/SL, Reduce Only)

### Key Achievements
1. ✅ US geolocation issue resolved through compliant region deployment
2. ✅ Cross-margin trading implemented as default
3. ✅ Bridge solution operational (fast and slow modes)
4. ✅ Successfully deployed for closed beta October 17, 2025
5. ✅ Integration with referral program

### Technical References
- See [2025-07-24 Hyperliquid Integration Meeting](../../../06-meetings/2025-07/2025-07-24-hyperliquid-integration.md) for architectural decisions
- See [2025-07-25 Cooking Demo](../../../06-meetings/2025-07/2025-07-25-cooking-demo.md) for US geolocation challenge discussion
- See [2025-07-30 Daily Standup](../../../06-meetings/2025-07/daily-standups/2025-07-30-daily-standup.md) for legal compliance considerations
