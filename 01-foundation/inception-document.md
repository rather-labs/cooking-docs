---
title: Cooking.gg Inception Document
type: foundational-doc
date: 2024-10-03
last-updated: 2025-10-19
status: active
owner: Project Team
stakeholders: [Leadership, Engineering Team, Product Team]
tags: [inception, platform-architecture, product-vision, technical-spec, business-model]
summary: |
  Comprehensive inception document (de-risking report) for Cooking.gg platform.
  Defines project vision, technical architecture, platform features, business model,
  roadmap, and resource requirements for the Solana-based meme token trading platform.
related-docs:
  - [../02-decisions/2024-10-03-telegram-authentication.md]
  - [../04-knowledge-base/technical/architecture-overview.md]
  - [glossary.md]
---

# Cooking.gg Inception Document

**Document Type:** De-risking Report
**Date:** October 3, 2024
**Status:** Active

## Table of Contents

1. [Project Summary](#project-summary)
2. [Project Estimation](#project-estimation)
3. [Platform Overview](#platform-overview)
4. [Metrics & Indicators](#metrics--indicators)
5. [Technical Architecture](#technical-architecture)
6. [Future Development](#future-development)
7. [Business Model](#business-model)

---

## Project Summary

### Purpose and Objectives

The Cooking.gg platform is designed to be a Solana-based trading platform tailored for the growing market of meme-based tokens, with the potential to expand to other blockchains in the future. The platform's primary focus is to offer a simple-to-use yet engaging experience for a broad audience, ensuring it appeals to both experienced traders and newcomers. It will leverage established protocols like Pump.fun, Moonshot, and Raydium to enable seamless token trading within these ecosystems.

#### Key Objectives

- **User-Friendly Experience:** Ensure that the platform is intuitive and easy to navigate for all users, regardless of their experience level. Users will benefit from a simplified login through Telegram, allowing easy access to the platform. Additionally, the platform will feature custodial wallets, allowing users to quickly buy and sell without needing to sign each transaction, simplifying the overall trading process. Combined with on-ramps, this makes the platform accessible even to those unfamiliar with crypto trading.

- **Competitive Edge:** The platform will feature custom indicators like Diamond Hands to give traders better insights into market behavior, along with the Quick Operations Panel, which allows users to easily manage their positions from anywhere on the platform. Additionally, configurable hotkeys will streamline user interactions and enhance trading efficiency.

- **Engaging User Interaction:** Incorporate engaging features such as achievements, badges, and boosters to enhance the trading experience, fostering user retention and active participation without overwhelming the core trading functionality. Users can earn points by trading and completing quests, competing on a leaderboard, with a jackpot distributed among the top-performing wallets.

- **Scalability:** Design the platform with future growth in mind, ensuring it can easily integrate additional blockchains and protocols as the ecosystem of meme-based tokens continues to expand.

- **Telegram Trading Bot:** Alongside the web platform, users will be able to manage their portfolios, check token prices, view their positions, and execute buy and sell orders directly through a Telegram bot. This bot will mirror the simplicity and ease-of-use of the web app, ensuring quick transactions with minimal friction.

### Business Context

The cryptocurrency market has evolved significantly in recent years, giving rise to a subcategory of assets known as meme or community coins. These assets have gained notoriety due to their extreme volatility and the backing of large communities on social media. Coins like Dogecoin and Shiba Inu have captured the attention of speculative investors, creating an increasingly competitive space for tools that facilitate the trading of these currencies.

The platform is designed to compete in the existing market for meme-token trading by focusing on providing a fast, efficient, safe, and engaging user experience. The main competitors in this space include BullX and Photon, both of which serve as models for many of the platform's core features.

**Key Differentiators:**
- Condensed key token views into a single, comprehensive view
- Quick Operations Panel for efficient position management
- Custom indicators (Diamond Hands, Average Holding Time)
- Leaderboard with engaging mechanics
- Simplified onboarding with custodial wallets and on-ramps

The platform targets meme traders, both experienced and new, and aims to simplify the onboarding process, making it accessible to those unfamiliar with crypto.

---

## Project Estimation

### Roadmap Timeline

#### Backend Infrastructure and Desktop Version

**Duration:** Week 1 to Week 13

This phase is dedicated to developing the core features of the platform's desktop version, along with building the necessary backend infrastructure. Key tasks:

- **Infrastructure Set Up & Maintenance:** Establish the technical environment for the platform, including server configurations and database setup
- **Telegram Integration:** Incorporate Telegram functionality for login and wallet management
- **Custodial Wallet Provider Integration:** Connect with custodial wallet provider for automated wallet creation and management
- **Ramps Integration:** Implement on-ramp services to convert fiat into crypto assets
- **Indexer Service:** Develop and deploy the indexer to track real-time token prices, trade volumes, and metrics
- **Transaction Relay Service:** Establish service to facilitate buy/sell transactions and integrate platform fees
- **UX/UI Design & Component Standardization:** Build and refine the platform's user interface
- **Frontend Development:** Develop frontend components for all key views

#### Telegram Trading Bot

**Duration:** Week 12 to Week 14

The second phase focuses on developing a Telegram Trading Bot that will allow users to execute key trading actions directly from Telegram.

### Key Releases

- **Release 001 (Week 5-6):** Implementation of login functionality through Telegram, custodial wallet funding via self-custodial wallets and on-ramps
- **Release 002 (Week 8-9):** Launch of Discovery and Token Expanded View page
- **Release 003 (Week 12):** Introduction of Quick Operations Panel and Portfolio views, Transaction Relay Service operational
- **Release 004 (Week 14-15):** Completion of platform backend and desktop version (including leaderboard) and Telegram Trading Bot

### Resources

**Required Team:**
- **Blockchain Engineer:** Solana ecosystem development, smart contracts (Rust), backend services, DApps
- **Backend Engineer:** Server-side logic, APIs, software architecture, design patterns
- **Frontend Engineer:** User-facing interface, responsive design, blockchain integration
- **DevOps Engineer:** Deployment, monitoring, infrastructure maintenance
- **UX/UI Designer:** Intuitive, user-friendly experience design

---

## Platform Overview

### Design & User Experience

The platform's interface is designed to be intuitive and engaging, minimizing unnecessary clicks and allowing users to focus on quick transactions.

**Key Design Principles:**
- **Ease of use:** Unified token views and transaction screens, streamlined processes
- **Consistency:** Cohesive themed design across all views
- **Simplicity:** Short welcome tutorial, minimal complexity
- **Accessibility:** Clear fonts, easy navigation, well-organized layouts, hotkeys integration

### Core Platform Views

#### 1. Login through Telegram
- Seamless authentication via Telegram account
- Automatic custodial wallet generation on first login
- One-time login page with private key download option

#### 2. General Layout
- **Header:** Notifications, position overview, "Sell All Positions" button, inventory (Boosters), USD/SOL toggle
- **Expandable Side Menu:** View navigation, settings, logout

#### 3. Wallet Manager
- Deposit/withdraw funds between self-custodial and custodial wallets
- On-ramp service integration
- Balance overview and transaction history

#### 4. Portfolio
- Holdings overview with Active Positions, Gainers, Losers, Past Positions tabs
- Custom trading strategies (Take Profit, Stop Loss, Buy Dip)
- Complete trading history

#### 5. Discovery
Two tabs with three columns each:
- **Lifecycle Tab:** Tokens at different stages of bonding curve
- **Explore Tab:** Trending tokens, gainers, and losers
- Features: Token cards, expanded view, quick buy, configurable hotkeys

#### 6. Quick Operations Panel (QOP)
- Expandable from any view by selecting a position
- Token overview with key metrics
- User's position details (holdings, invested amount, PnL)
- Trading options: buy/sell orders, predefined strategies
- Gas settings and transaction parameters

#### 7. Leaderboard
- Points system: earn through trading, profitability, quests, referrals
- Badges for status and points
- Jackpot rewards: Booster Coins and/or actual money
- Boosters: gasless transactions, points multipliers, trading benefits

#### 8. Token Details View
- Price and trade history
- Advanced indicators (AHT, Diamond Hands)
- Trading options with custom strategies

### Platform Theme: Cooking

The platform adopts a cooking theme to complement the playful and community-driven nature of meme coins:

- **Creative Section Names:** "The Kitchen" (Dashboard), "Fresh Ingredients" (Discovering New Coins)
- **Cooking-Themed Iconography:** Ovens/stoves represent transaction progress
- **Fun & Functional:** Playful visuals with familiar cooking terminology while maintaining serious trading functionality

---

## Metrics & Indicators

### Standard Indicators

Widely used objective metrics:
- **Liquidity:** Total liquidity available for the token
- **Market Cap:** Token valuation based on circulating supply and price
- **Volume:** Token traded within specific period
- **Age:** Time elapsed since token creation
- **Transaction Volume:** Total number of transactions
- **PnL (Profit and Loss):** Cumulative profit or loss
- **Total Holders:** Number of wallets holding the token

### Use-Case Specific Indicators

Tailored to meme-token trading:

**Token Metrics:**
- **Top 10 Holdings:** Percentage held by 10 largest wallets
- **Dev Holdings:** Percentage held by developer wallet
- **Dev Sold:** Boolean flag if developer sold entire position
- **Insider Holdings:** Percentage held by insider wallets
- **Snipers:** Number of wallets buying immediately after launch
- **Bonding Curve %:** Token's position on bonding curve
- **Average Holding Time (AHT):** Average duration tokens are held
- **Diamond Hands (DH):** Wallets holding long-term while profitable

**Audit Indicators:**
- **Is Mintable:** Whether new tokens can be minted
- **Is Token Data Mutable:** If token data can be changed post-deployment
- **Is Freezable:** If token accounts can be frozen
- **Update Authority:** Entity that can update token information
- **Owner Balance:** Tokens held by developer/deployer
- **$TOKEN Pooled:** Tokens in liquidity pools
- **$COIN Pooled:** Quote tokens pooled for liquidity
- **LP Burned:** Percentage of LP tokens burned
- **Top 10 Holders:** Supply percentage held by top wallets
- **Deployer Address:** Wallet that deployed the token

### Indicator Calculation Approaches

#### Token-Wallet Level (Pairwise)
Metrics calculated for each specific wallet and token pair, providing micro-level insights.

#### Token-Centric Approach
Metrics aggregated for each token across all wallets, providing insights into token-specific behavior.

#### Wallet-Centric Approach
Metrics aggregated across all tokens a wallet has interacted with, providing comprehensive portfolio-wide view.

### Detailed Metrics Explanation

#### Average Holding Time (AHT)
Using FIFO (First-In-First-Out) method:
- Track token buys with price and timestamp
- Match sales to earliest purchases
- Calculate holding time as difference between sale and purchase dates
- Weighted average based on number of tokens held

#### Profit & Loss (PnL)
Using FIFO method to track price differences between purchases and sales.

#### Diamond Hands (DH)
**Definition:** At token-wallet level, a Diamond Hand wallet holds a token longer than average (via AHT) and maintains positive PnL.

**Identification Criteria:**
- **AHT:** Top X% of holders OR longer than predefined threshold
- **PnL:** Greater than 0 OR exceeding predefined profit threshold

---

## Technical Architecture

### Layered Architecture Overview

The system is divided into distinct layers with information flowing from lower to upper layers (except transactions, which flow downward).

[Link to architecture diagram](#)

### 1. Authentication & User Management

#### Login with Telegram
- **Core Features:** Telegram-based login, automatic custodial wallet creation
- **User Flow:** Login initiation → Telegram authorization → Backend validation → Wallet creation → Session start
- **Technical Implementation:** Telegram Widget with SHA signature verification, JWT/session token generation

#### Session Management
- **Features:** Session persistence via JWT, Single Sign-On (SSO)
- **Technical:** Secure cookie/JWT storage, token expiration and refresh, logout invalidation

#### Custodial Wallet Creation
- **Features:** Automated wallet generation, linking to user account
- **Technical:** Integration with custodial wallet provider, secure key management

#### Security Considerations
- OAuth 2.0 for Telegram authentication
- Encrypted custodial wallets
- Secure session token storage (HttpOnly, Secure, SameSite)
- Token expiry and refresh mechanisms

### 2. Custodial Wallet Service

**Key Benefits:**
- No manual transaction signing
- Frictionless onboarding
- No private key management by users

#### Custodial Wallet Creation
Automated generation upon first login, secure wallet linking, private keys managed by provider.

#### Custodial Wallet Funding
- **Deposits:** From self-custodial wallets or on-ramp services
- **Withdrawals:** To self-custodial wallets
- **Benefits:** Ease of use, flexibility

#### DFNS as Top Choice
- **Innovative Security:** MPC (Multi-Party Computation) technology
- **Tailored for Modern Platforms:** Highly customizable infrastructure
- **Scalability:** Multi-chain and multi-platform support
- **Developer-Centric:** Easy integration
- **Pricing:**
  - Starter: $50/month (100 wallets, 1 team member, 1 blockchain)
  - Basic: $500/month (10,000 wallets, 3 team members, 3 blockchains)
  - Pro: $2,000+/month (50,000 wallets, 5 team members, unlimited blockchains)

#### Security Measures
- **TSS with MPC:** Private keys split and distributed
- **Privacy:** Parties cannot access each other's partial keys
- **Distributed Signing:** Transactions signed without reconstructing private key
- **Access Control:** Strict protocols for authorized transactions

### 3. Indexer Service

**Core Purpose:**
- Provide real-time data related to token performance, wallet balances, transaction history
- Calculate specialized indicators (AHT, Diamond Hands) for each wallet-token pair

#### Key Requirements

**Data Ingestion:**
- Real-time transaction data from Solana blockchain
- Integration with Solana RPC endpoints, WebSockets, event listeners
- Historical data recovery via getsignaturesforaddress + gettransaction
- Scalability for high transaction volumes

**Data Storage:**
- Efficient storage for large transaction and wallet data
- Fast querying of token performance, wallet transactions, historical data
- Parallel/concurrent aggregate information writing
- Support for metrics aggregation over time

**Data Processing & Aggregation:**
- Real-time processing for custom indicators
- AHT, Diamond Hands, transaction summaries, token-specific metrics
- Batch processing jobs or streaming data pipelines
- Scalable through parallelization

**API Layer:**
- REST or GraphQL APIs exposing processed data
- Endpoints for wallet data, token transactions, leaderboard rankings, token metrics
- Minimum latency for real-time experience
- Caching strategies for performance

**Redundancy and Recovery:**
- Built-in redundancy for data collection and storage
- Automated backups and disaster recovery
- Automatic recovery system for data gaps

#### Real-time Streaming Technical Details

**Purpose:** Abstract complexities of Solana blockchain interaction, translate blockchain events into protocol-specific events.

**Sub-Services:**
- **Blockchain Management:** Provider management, RPC connections, load balancing, failover
- **Protocol Subsystem:** Interpret on-chain events from Pump.fun, Moonshot, Raydium
- **Token Life Cycle Management:** Detect new tokens, track updates, monitor migrations
- **Token Price Extraction:** Identify trade events, extract price information

#### Data Aggregator Technical Details

Transform raw protocol events into meaningful insights:
- **Real-time Prices:** Process price-determining events into refined representations
- **Time Series Data:** Construct historical price time series
- **Token Information:** Track token metadata and updates
- **Indicators:** Build and update indicators in real-time

#### Data Provider Technical Details

Manage web application subscriptions to active tokens, time series, real-time prices, trade status, indicators, and metadata.

### 4. Transaction Relay Service

**Core Purpose:**
- Facilitate buy/sell transactions between users and blockchain protocols
- Seamless integration with custodial wallets
- Implement 1% platform fee without interfering with protocol logic

#### Key Requirements

**Custodial Wallet Integration:**
- Instant buy/sell without user approval for each transaction
- Secure and reliable connection to wallet provider API

**Transaction Composition:**
- Construct Solana transactions with multiple instructions
- Trade instructions + platform fee instruction
- SPL token compatibility

**Fee Deduction Logic:**
- Deduct 1% automatically to platform wallet
- Separate instruction within same transaction

**Transaction Finality:**
- Confirm on-chain completion
- Handle failed transactions gracefully with retry mechanisms
- Real-time feedback to users

**Gas Settings:**
- Customizable transaction parameters: priority fees, slippage limits
- Bribe and MEV protection considerations (not in initial release)

#### Technical Details

**Transaction Sources:**
- Frontend user interaction
- Telegram service
- Automated trading service (future)

**Main Tasks:**
- **Transaction Composition:** Apply relevant rules based on origin
- **Execution Assurance:** Monitor, propagate, retry for successful blockchain execution

#### Bribes and MEV Protection Considerations

Not necessary for current Solana environment:
- Solana not currently overcrowded
- Limited use case for bribes (bundle processing, speed optimization for snipers)
- Uncertain effectiveness (only JITO validators)
- Changes in JITO validator architecture reduce MEV protection effectiveness

### 5. Trading Bot in Telegram

**Core Purpose:**
Allow users to interact with platform through Telegram, managing wallets, viewing positions, executing trades.

**Features:**
- Wallet management and funding
- View positions
- Execute buy/sell orders
- Lists of latest and trending tokens
- Withdrawal to external wallets

#### Key Requirements

**Layered Architecture:**
- **Presentation Layer:** Handle user commands, validate inputs
- **Business Logic Layer:** Core functionality, trade execution, transaction coordination
- **Data Access Layer:** CRUD operations, data from databases, APIs, cloud storage, RPC nodes

**Open-Closed Design:**
- Support essential trading features initially
- Easily accommodate new commands via Open-Closed Principle
- Future: limit orders, automated strategies, detailed portfolio insights, alerts

### 6. Ramps

**Core Purpose:**
Enable seamless conversion between fiat and crypto (on-ramps and off-ramps).

#### Key Requirements
- **Versatility:** Support additional providers without major rework
- **Low Coupling:** Independent provider integrations

#### Ramp Providers

**Moonpay:**
- Payment methods: Apple Pay, Google Pay, credit/debit cards, bank transfers (on-ramp); bank accounts, PayPal, Visa cards (off-ramp)
- SDKs for frontend integration
- API for backend integration and full customization

#### Ramp Aggregators

**Onramper:**
- Unified solution for multiple on-ramp/off-ramp services
- **Widget:** Quick deployment with some customization
- **API:** Full customization of ramp experience
- **Pricing:**
  - Essential: $199/month (limited ramps)
  - Premium: Custom pricing (19+ providers, advanced control, custom fees, dedicated support)

---

## Future Development

### Automated Trading Service

**Note:** Postponed to later stage due to complexity and time requirements.

#### Core Features
- **Customizable Strategies:** User-defined trading rules based on market conditions
- **Automated Execution:** Continuous monitoring, automatic trade execution
- **Multi-Step Strategies:** Complex trading strategies (e.g., sell 50% at market cap +50%, remaining 50% when doubled)

#### Process Flow
1. **Strategy Creation:** Users configure via platform interface
2. **Monitoring:** Continuous monitoring of price movements and market conditions
3. **Execution:** Automatic trade execution when conditions met
4. **Notification:** Users notified of executed trades or invalid conditions

#### Technical Details
- **Real-Time Data Processing:** Monitor all relevant assets, evaluate user rules in real-time
- **Rule-Based Execution:** Process individual rules at user+token level
- **Lifecycle Monitoring:** Track open positions, check closing conditions
- **Scalability Considerations:** Handle growing processing load with user base
- **Transaction Handling:** Ensure accurate buy/sell operations with user restrictions

#### Benefits
- Hands-free trading
- Precision and control
- Real-time action

---

## Business Model

### 1% Transaction Fee

**Implementation:**
- Users receive 99% of trade value
- 1% directed to platform wallet
- Fee incorporated within trade transaction

**Key Concepts:**
- **Solana Transaction Instruction:** Fee instruction included alongside protocol instructions
- **Fee Deduction:** Automatic 1% deduction
- **Custodial Wallet Advantage:** No additional user approval required

**Challenges & Considerations:**
- **User Perception:** Fee less noticeable with high-frequency trading and rapid price fluctuations
- **Program Compatibility:** Fee instruction must coexist with Solana transaction structure and protocol smart contracts

---

## Closing Remarks

The Cooking platform is designed to offer a streamlined, engaging, and innovative experience for meme token traders. Through careful planning, design, and development, we have laid a solid foundation that will differentiate the platform from competitors by prioritizing ease of use, customizability, and performance.

Our focus remains on delivering core functionalities with precision, while ensuring flexibility for future expansions and enhancements. From custodial wallets and ramps to indexer and transaction relay services, every aspect has been designed to provide an unparalleled trading experience.

The "Cooking" branding adds a fresh layer of creativity and personality, ensuring the platform stands out visually while remaining approachable and enjoyable. The thoughtful integration of key features like the Quick Operations Panel and intuitive token views ensures the platform is both powerful and user-friendly.

---

**Related Documents:**
- [Telegram Authentication Decision](../02-decisions/2024-10-03-telegram-authentication.md)
- [Architecture Overview](../04-knowledge-base/technical/architecture-overview.md)
- [Glossary](glossary.md)

**Last Updated:** 2025-10-19
