---
title: Project Glossary
type: glossary
date: 2025-10-17
last-updated: 2025-10-22
status: active
owner: Project Team
tags: [foundation, terminology, reference]
summary: |
  Comprehensive glossary of domain-specific terms, acronyms, and concepts
  used throughout the project to ensure consistent understanding. Enhanced
  with 95+ new terms from meeting notes covering infrastructure, trading,
  security, business terminology, and authentication patterns.
---

# Project Glossary

This glossary defines key terms, acronyms, and concepts used throughout the project. Keep this updated as new terminology emerges.

## How to Use This Glossary
- Terms are organized alphabetically
- Each entry includes: term, definition, context, and related terms
- When adding new terms, maintain alphabetical order
- Update this monthly or when significant new terminology is introduced

---

## A

### Auth0
**Definition:** Managed authentication and authorization platform providing social login and identity management services.

**Context:** Integrated in September 2025 per ADR-102 for Twitter, Google, Apple, and Telegram login. Custom callback implemented for Turnkey wallet integration. $96k first-year savings vs in-house implementation. Critical for mobile app development workflow.

**Related Terms:** Social Login, Turnkey, ADR-102, Authentication

**Examples:** "Auth0 handles Google/Twitter/Apple login and passes tokens to Turnkey for wallet creation"

---

### Axios
**Definition:** Promise-based HTTP client library for browser and Node.js used for making API requests.

**Context:** Initially used for authentication endpoints but discovered issue with cookie credential handling in October 2025. Switched to native Fetch API for refresh token endpoint to resolve cookie-setting bug. Issue affected both Chrome and Safari browsers.

**Related Terms:** Fetch API, HTTP Client, Authentication, Cookies

**Examples:** "Axios wasn't sending credentials properly for cookie-based auth, switched to Fetch for that specific endpoint"

---

### ACM (AWS Certificate Manager)
**Definition:** AWS service for managing SSL/TLS certificates used to secure communications.

**Context:** Part of the infrastructure security strategy for HTTPS connections and encrypted communications between services.

**Related Terms:** AWS, WAF, Security, TLS

**Examples:** "ACM automatically renews SSL certificates for our domains"

---

### ADR (Architecture Decision Record)
**Definition:** A document that captures an important architectural decision made along with its context and consequences.

**Context:** Used throughout this project to track significant technical and business decisions. Found in the `02-decisions/` directory.

**Related Terms:** Decision Record, Technical Decision

**Examples:** "See ADR-100 for the Jupiter router decision"

---

### AHT (Average Holding Time)
**Definition:** The average duration a wallet holds a token before selling or trading it, calculated using the FIFO method with weighted averages.

**Context:** A key metric for understanding holder behavior and token stability. Used in Diamond Hands calculations and token analysis. Can be measured at token-wallet, token-centric, or wallet-centric levels.

**Related Terms:** Diamond Hands, FIFO, Profit & Loss (PnL), Token Metrics

**Examples:** "This wallet has an AHT of 5 days for this token, indicating medium-term holding behavior"

---

### AMM (Automated Market Maker)
**Definition:** DEX protocol using liquidity pools and algorithmic pricing instead of traditional order books for token trading.

**Context:** Core mechanism for decentralized trading on platforms like Raydium and Orca. Users trade against liquidity pools rather than other traders directly.

**Related Terms:** Liquidity Pool, Raydium, Orca, DEX

**Examples:** "Raydium's AMM provides constant product pricing for token swaps"

---

## B

### Bonding Curve
**Definition:** A mathematical curve that determines the price of a token based on its supply. As more tokens are purchased, the price increases along the curve.

**Context:** Used in platforms like Pump.fun to manage token pricing and liquidity. Tokens progress through stages on the bonding curve before graduating to full DEX liquidity.

**Related Terms:** Pump.fun, Liquidity, Token Lifecycle

**Examples:** "This token is at 45% on its bonding curve" or "Tokens in the Discovery view are organized by bonding curve progress"

---

### Bridge Fees
**Definition:** Costs associated with transferring assets across different blockchain networks (cross-chain transfers).

**Context:** Strategic decision per ADR-202 to charge zero bridge fees for Solana ↔ USDC/Arbitrum transfers. Prioritizes user acquisition over revenue in beta phase. Simplifies user experience and competitive positioning.

**Related Terms:** Cross-Chain, USDC, Arbitrum, Solana, ADR-202

**Examples:** "Zero bridge fees make it easier for users to move funds between chains"

---

### Booster Coins
**Definition:** Off-chain, non-transferable currency within Cooking.gg that can be used to purchase boosters (in-app items providing benefits).

**Context:** Earned through trading and completing quests on the platform. Can be exchanged for gasless transactions, point multipliers, and prize crates.

**Related Terms:** Boosters, Leaderboard, Gamification

**Examples:** "Use Booster Coins to purchase a 2x points multiplier"

---

### Boosters
**Definition:** In-app items that provide benefits to users, purchased with Booster Coins.

**Context:** Part of the gamification system. Includes gasless transactions, point multipliers, and randomized prize crates.

**Related Terms:** Booster Coins, Gamification, Leaderboard

**Examples:** "Activate a booster for gasless trading for the next hour"

---

### Borsh
**Definition:** Binary serialization format optimized for Solana smart contracts, with implementations in Rust and JavaScript/TypeScript.

**Context:** Used for parsing Solana program events in the indexer. JavaScript/TypeScript implementation has limitations with optional parameters compared to Rust version. Pam Fun and Pam Swap protocol updates in October 2025 exposed these limitations, requiring manual parsing workarounds for optional fields.

**Related Terms:** Solana, Indexer, Serialization, Protocol Integration

**Examples:** "JavaScript Borsh can't safely handle optional attributes like Rust version, so we manually trim the last parameter for Pam Fun events"

---

## C

### ClickHouse
**Definition:** A high-performance, column-oriented database management system optimized for real-time analytics and time-series data.

**Context:** Integrated into Cooking.gg's architecture to dramatically improve performance, particularly for indexer data, bar data, and real-time price updates. Migration completed in July 2025 with significant performance gains. Critical for production deployment.

**Related Terms:** Indexer Service, Database, Performance Optimization, AWS

**Examples:** "ClickHouse migration reduced execution time from 6-8 seconds to 2.5-3 seconds"

---

### Closed Beta
**Definition:** Limited-access testing phase where platform is available only to selected users before public launch.

**Context:** Launched October 17, 2025 with referral-only access model per ADR-201. Internal testing (5 users) October 21-27 determines October 27 full launch (30-40 users). Replicates Bullex Neo viral growth methodology.

**Related Terms:** Referral-Only Access, Referral Program, ADR-201, ADR-203

**Examples:** "Closed beta launch achieved 99.9% uptime with 30-40 whitelist users"

---

### Commission Tiers
**Definition:** Volume-based earning rates for referral program, ranging from 30-45% of platform fees from referred users.

**Context:** 3-tier structure per ADR-200: 30% base, 35% mid-tier, 45% top tier. Progression based on personal trading volume. Additional 10% performance bonus available.

**Related Terms:** Referral Program, Multilevel Referral, Performance Bonus, ADR-200

**Examples:** "Reach top commission tier (45%) by maintaining high personal trading volume"

---

### Crossmint
**Definition:** A crypto payment infrastructure provider offering checkout solutions for NFT and token purchases without requiring users to hold crypto.

**Context:** Initially considered for on-ramp integration but deprioritized in favor of standard KYC-based on-ramp solutions. Created dead-end user experience requiring Solana for gas.

**Related Terms:** On-Ramps, Onramper, Payment Processing

**Examples:** "Crossmint checkout was considered but rejected due to UX concerns"

---

### Cross-Margin
**Definition:** Margin trading mode where a single margin balance is shared across all open positions, allowing profits from one position to offset losses in another.

**Context:** Supported margin mode for Hyperliquid perpetuals trading. Provides capital efficiency by using total account balance as collateral.

**Related Terms:** Perpetuals, Hyperliquid, Margin Trading, Isolated Margin

**Examples:** "Cross-margin mode allows you to use your entire account balance for multiple positions"

---

### Custodial Wallet
**Definition:** A cryptocurrency wallet where a third party (the platform) holds and manages the private keys on behalf of the user.

**Context:** Cooking.gg provides custodial wallets automatically upon login, allowing users to trade without signing each transaction. Simplifies onboarding for crypto-inexperienced users.

**Related Terms:** Self-Custodial Wallet, DFNS, Private Key

**Examples:** "Your custodial wallet is created automatically when you first log in through Telegram"

---

## D

### Data Aggregator
**Definition:** Backend service component that transforms raw protocol events from the blockchain into meaningful insights and actionable information for the application.

**Context:** Part of the Indexer Service architecture. Processes real-time prices, builds time series data, tracks token information, and constructs indicators.

**Related Terms:** Indexer Service, Real-time Streaming, Protocol Events

**Examples:** "The Data Aggregator processes bursts of price-determining events to build refined real-time price data"

---

### DCA (Dollar Cost Averaging)
**Definition:** Trading strategy where orders are executed at regular intervals to reduce impact of volatility by averaging entry price over time.

**Context:** One of the advanced trading algorithms being implemented on the platform. Allows users to build positions gradually rather than single large orders.

**Related Terms:** TWAP, VWAP, Trading Algorithms, Limit Orders

**Examples:** "Set up DCA to buy $100 of SOL every day for 30 days"

---

### DFNS
**Definition:** A custodial wallet service provider being considered for Cooking.gg's wallet infrastructure.

**Context:** Recommended provider for secure, automated wallet creation and management in the technical architecture.

**Related Terms:** Custodial Wallet, Security, Wallet Provider

**Examples:** "We're integrating with DFNS for custodial wallet services"

---

### Diamond Hands
**Definition:** A custom indicator showing tokens held by wallets that rarely sell, indicating strong conviction or long-term holding behavior.

**Context:** One of Cooking.gg's differentiating custom indicators that provides unique trading insights not available on competitor platforms.

**Related Terms:** Average Holding Time (AHT), Custom Indicators, Token Metrics

**Examples:** "This token has 65% Diamond Hands, suggesting strong holder conviction"

---

**Related Terms:**

**Examples:**

---

## E

### Echo
**Definition:** Alternative Solana swap router/aggregator that was evaluated as potential replacement for Jupiter in October 2025.

**Context:** Client requested integration due to perceived performance advantages. After comprehensive testing revealed architectural incompatibility (requires liquidity pool addresses) and no meaningful performance gains, integration was rejected. Jupiter demonstrated 500ms performance vs 620ms Echo (when fairly tested). Client accepted decision after October 17 demo showing 3-second transaction performance.

**Related Terms:** Jupiter, Routing, ADR-100, Performance

**Examples:** "Echo integration was rejected per ADR-100 due to architectural incompatibility with our indexer abstraction"

---

### ECS (Elastic Container Service)
**Definition:** AWS container orchestration service chosen over EKS (Kubernetes) for simpler operational overhead.

**Context:** Selected in September 2025 for production deployment. Provides faster time-to-production (5-6 weeks), lower operational burden for small team, and native AWS integrations. Successfully deployed for October 17 beta launch.

**Related Terms:** EKS, AWS, Docker, Infrastructure, ADR-300

**Examples:** "ECS deployed our microservices with automatic scaling and multi-AZ failover"

---

### EKS (Elastic Kubernetes Service)
**Definition:** AWS-managed Kubernetes service considered but rejected in favor of ECS.

**Context:** Evaluated for container orchestration in September 2025. Rejected due to higher operational complexity, longer implementation timeline, and team unfamiliarity. ECS chosen instead per ADR-300.

**Related Terms:** ECS, Kubernetes, AWS, Infrastructure

**Examples:** "EKS was considered but ECS better fit our timeline and team capabilities"

---

## F

### Face ID
**Definition:** Apple's facial recognition biometric authentication technology using TrueDepth camera and Secure Enclave.

**Context:** Required for all trading operations on iOS mobile app per ADR-401. Provides hardware-backed security for wallet operations. Fallback to security password for devices without Face ID.

**Related Terms:** Touch ID, Biometric Authentication, Secure Enclave, ADR-401

**Examples:** "Authenticate with Face ID to execute this trade on iPhone"

---

### Feature Freeze
**Definition:** Period where no new features are added, focusing exclusively on bug fixes, polish, performance optimization, and testing.

**Context:** Mid-August through October 17, 2025 freeze per ADR-302 protected timeline commitment. Enabled 50% performance improvement (6s → 3s transactions). Successfully maintained for 8-9 weeks. Critical for beta launch success.

**Related Terms:** Bug Fixing, Performance Optimization, ADR-302, Technical Debt

**Examples:** "Feature freeze allowed team to focus on stability and achieve 99.9% uptime at launch"

---

### Fetch API
**Definition:** Modern native JavaScript/browser API for making HTTP requests, replacing older XMLHttpRequest.

**Context:** Used as replacement for Axios for specific authentication endpoints in October 2025. Resolved cookie credential handling issues that Axios couldn't handle properly. Now handles refresh token endpoint to ensure cookies set correctly in both Chrome and Safari.

**Related Terms:** Axios, HTTP Client, Authentication, Cookies

**Examples:** "Switched to Fetch API for refresh token endpoint to fix cookie-setting bug"

---

### FIFO (First-In-First-Out)
**Definition:** An accounting method where the first tokens bought by a wallet are assumed to be the first ones sold, used for calculating holding time and PnL.

**Context:** Core methodology for calculating Average Holding Time (AHT) and Profit & Loss (PnL) for wallet-token pairs.

**Related Terms:** AHT, PnL, Token Metrics

**Examples:** "Using FIFO, we match each sale with the earliest corresponding purchase to calculate holding time"

---

## G

### Gasless Transactions
**Definition:** A booster feature that allows users to execute transactions without paying gas fees for a limited time.

**Context:** One of the boosters available in the platform's gamification system, purchasable with Booster Coins.

**Related Terms:** Boosters, Booster Coins, Gamification

**Examples:** "Activate a gasless transaction booster for the next hour of trading"

---

### GraphQL
**Definition:** Query language for APIs allowing clients to request exactly the data they need with a single endpoint.

**Context:** Alternative API architecture considered for flexible data querying. REST API currently used for primary API communications.

**Related Terms:** REST API, API, Type-Safe API Client

**Examples:** "GraphQL would allow clients to specify nested data requirements in single query"

---

## H

### Hatom
**Definition:** An external client project that occasionally requires work hours from the Cooking.gg development team.

**Context:** Hours worked on Hatom are tracked separately as they are billed as extra hours to the client, not counted toward Cooking.gg development time.

**Related Terms:** Time Tracking, Resource Management

**Examples:** "Log your Hatom hours separately in the channel for billing purposes"

---

### HelloMoon
**Definition:** Solana blockchain data provider and RPC service offering real-time data access and analytics.

**Context:** Used as data source and RPC provider for Solana blockchain queries. Provides trade data fallback alongside Jupiter for protocols not fully indexed by the platform.

**Related Terms:** Jupiter, RPC, Protocol Integration, Data Provider, Solana

**Examples:** "HelloMoon RPC endpoints provide reliable Solana blockchain access for indexing"

---

### Hyperliquid
**Definition:** A decentralized exchange (DEX) for perpetual futures trading, integrated with Cooking.gg for perpetuals functionality.

**Context:** Provides the infrastructure for perpetuals trading features on the platform, including leverage trading and position management.

**Related Terms:** Perpetuals, DEX, Leverage Trading, USDC

**Examples:** "Convert SOL to USDC through Hyperliquid to open a perpetuals position"

---

## I

### IAM (Identity and Access Management)
**Definition:** AWS service for managing permissions and access control to cloud resources.

**Context:** Part of the infrastructure security architecture for controlling service-to-service authentication and resource access permissions.

**Related Terms:** AWS, Security, Infrastructure

**Examples:** "IAM roles define which services can access ClickHouse and RDS databases"

---

### Inside X
**Definition:** A third-party service provider offering bubble map visualizations for cryptocurrency markets.

**Context:** Selected for bubble map integration at $200/month subscription. Provides Solana market visualization only (Hyperliquid bubble maps not needed for perpetuals). Selected in August 2025.

**Related Terms:** Bubble Maps, Visualization, Market Analysis

**Examples:** "Inside X provides real-time bubble maps showing market movements and token clustering"

---

## J

### JITO
**Definition:** A Solana validator service that offers transaction bundling and MEV (Maximal Extractable Value) protection features.

**Context:** Discussed in the context of bribes and MEV protection. Platform decided not to implement JITO features in initial release due to limited applicability and uncertain effectiveness in current Solana environment.

**Related Terms:** MEV Protection, Validators, Solana, Bribes

**Examples:** "JITO validators can bundle up to 5 transactions together, but bribes only work if a JITO validator picks up the transaction"

---

### Jupiter
**Definition:** Decentralized exchange aggregator on Solana that provides optimal swap routes across multiple liquidity sources. Selected as primary router per ADR-100.

**Context:** Primary routing protocol integrated for token trading after comprehensive testing in October 2025. Demonstrated 500ms performance vs 620ms Echo. Provides routing abstraction without requiring pool addresses. Successfully powering 3-second transaction completion times. Also used as data source for tokens not fully indexed.

**Related Terms:** Echo, Routing, Swap Aggregator, ADR-100, Pump.fun, Moonshot, Raydium

**Examples:** "Jupiter routes trades through optimal liquidity pools for minimal slippage"

---

### JWT (JSON Web Token)
**Definition:** Compact, URL-safe token format for securely transmitting information between parties as a JSON object.

**Context:** Used for authentication token format in API communications. Refresh token cookie implementation migrated from Axios to Fetch API. Production tokens extended to 10 minutes.

**Related Terms:** Auth0, Authentication, API Security

**Examples:** "JWT contains user authentication claims and expires after 10 minutes"

---

## K

### Kafka
**Definition:** Distributed event streaming platform used for building real-time data pipelines and event-driven architecture.

**Context:** Part of the backend infrastructure for handling high-volume message streams and real-time data processing across microservices.

**Related Terms:** RabbitMQ, Event-Driven Architecture, Microservices

**Examples:** "Kafka streams blockchain events to multiple consumer services"

---

### Keychain
**Definition:** Apple's secure credential storage system for iOS/macOS that stores passwords, keys, and certificates in encrypted form.

**Context:** Used for securely storing authentication credentials and sensitive data on iOS mobile app. Integrated with biometric authentication.

**Related Terms:** Secure Enclave, Face ID, Touch ID, iOS Security

**Examples:** "User credentials stored securely in iOS Keychain with biometric protection"

---

## L

### Lamports
**Definition:** Smallest unit of SOL (Solana's native token), where 1 SOL = 1,000,000,000 lamports.

**Context:** Used for precise transaction fee calculations and micro-payments on Solana. Similar to satoshis for Bitcoin.

**Related Terms:** SOL, Solana, Transaction Fees, Priority Fee

**Examples:** "Transaction cost 5,000 lamports (0.000005 SOL) in base fee plus priority fee"

---

### Launchpad
**Definition:** A platform or protocol for creating and launching new tokens, typically with bonding curve mechanisms.

**Context:** Multiple launchpads are integrated with Cooking.gg, including Pump.fun, Moonshot, and consideration for others like Let's Bonk Fan.

**Related Terms:** Pump.fun, Moonshot, Bonding Curve, Token Launch

**Examples:** "This token was launched on Pump.fun launchpad and is now trading on Raydium"

---

### Let's Punk (Let's Bonk)
**Definition:** A Solana-based launchpad protocol for creating and trading new tokens, integrated with Cooking.gg.

**Context:** Integration completed in August 2025. Part of expanding protocol coverage beyond Pump.fun and Moonshot.

**Related Terms:** Pump.fun, Moonshot, Launchpad, Protocol Integration

**Examples:** "Let's Punk integration adds another source of tokens to the Discovery view"

---

### Leverage Trading
**Definition:** Trading with borrowed funds to amplify potential returns (and risks), using a multiplier on the initial investment.

**Context:** Available through Hyperliquid integration for perpetuals trading. Leverage varies per contract (e.g., 20x for SOL/USD pair).

**Related Terms:** Hyperliquid, Perpetuals, Margin Trading

**Examples:** "Open a 20x leverage position on SOL/USD perpetuals with a 0.2 SOL minimum deposit"

---

### Limit Orders
**Definition:** Orders to buy or sell tokens at a specific price or better, executed only when market conditions meet the specified criteria.

**Context:** Advanced trading feature being implemented on the platform. Includes considerations for liquidity triggers and execution mechanisms. Mobile app completion includes limit order creation functionality.

**Related Terms:** Market Orders, Trading Strategies, Order Types, DCA, TWAP

**Examples:** "Set a limit order to buy when the token price drops to $0.50"

---

### Liquidity
**Definition:** The availability of tokens for trading, typically measured by the amount pooled in decentralized exchanges.

**Context:** Key metric for token health and trading viability. Affects slippage and price stability during trades.

**Related Terms:** Liquidity Pools, Raydium, DEX, Market Cap

**Examples:** "Higher liquidity allows for smoother trading with less price volatility"

---

### Liquidity Pools
**Definition:** Smart contract-based reserves of tokens locked in pairs to facilitate decentralized trading.

**Context:** Core mechanism for DEX trading on protocols like Raydium. Platform tracks liquidity metrics and pool information for trading decisions.

**Related Terms:** Raydium, DEX, AMM, LP Tokens

**Examples:** "The SOL/USDC liquidity pool on Raydium provides trading depth for perpetuals"

---

## M

### Materialized Views
**Definition:** Pre-computed query results stored in database for faster data retrieval, automatically updated when underlying data changes.

**Context:** ClickHouse materialized views used for OHLCV data per ADR-101. Dramatically improves charting performance by pre-aggregating candlestick data. Critical for 1-second interval TradingView charts.

**Related Terms:** ClickHouse, OHLCV, TradingView, Performance, ADR-101

**Examples:** "Materialized views pre-aggregate OHLCV data for instant chart rendering"

---

### Multi-AZ (Multi-Availability Zone)
**Definition:** AWS deployment strategy distributing infrastructure across multiple availability zones for high availability and fault tolerance.

**Context:** Implemented in September 2025 for production deployment across 3 availability zones. Achieved 99.9%+ uptime during October 2025 beta launch. Provides automatic failover for database and compute layers with RTO < 4 hours, RPO < 15 minutes. Cost increase ~50% (~$250/month) justified by reliability requirements per ADR-500.

**Related Terms:** High Availability, AWS, RTO, RPO, Infrastructure, ADR-500

**Examples:** "Multi-AZ deployment ensured 99.9% uptime during beta launch"

---

### Indexer Service
**Definition:** A backend service that tracks and aggregates real-time blockchain data including token prices, trade volumes, and market metrics.

**Context:** Core technical component of Cooking.gg that provides the data for all token displays and custom indicators. Evolved to microservices architecture by protocol (ADR-005) in September 2025.

**Related Terms:** Transaction Relay Service, Real-time Streaming, Data Aggregator, Microservices

**Examples:** "The Indexer Service streams real-time price updates to the Discovery view"

---

## M

### Meme Token
**Definition:** Cryptocurrency tokens typically created as jokes or based on internet memes, characterized by extreme volatility and community-driven value.

**Context:** The primary asset class traded on Cooking.gg. Examples include Dogecoin, Shiba Inu, and tokens on Pump.fun.

**Related Terms:** Community Coins, Solana, Pump.fun

**Examples:** "Cooking.gg specializes in meme token trading on Solana"

---

### Market Cap Variation
**Definition:** Trading strategy that monitors and triggers based on changes in token market capitalization over time.

**Context:** One of the advanced trading algorithms being implemented on the platform. Allows automated trading based on significant market cap movements.

**Related Terms:** Trading Algorithms, DCA, TWAP, Market Cap

**Examples:** "Set alert to buy when market cap increases by 50% in 1 hour"

---

### Market Orders
**Definition:** Orders to buy or sell tokens immediately at the best available current market price.

**Context:** Standard order type for instant execution. Primary trading method on the platform for immediate position entry/exit.

**Related Terms:** Limit Orders, Trading Strategies, Order Types

**Examples:** "Execute market order to buy 100 tokens at current best price"

---

### MEV (Maximal Extractable Value)
**Definition:** Profit extracted by reordering, inserting, or censoring transactions within blocks during the block production process.

**Context:** Discussed in context of JITO validators and MEV protection strategies. Platform decided not to implement JITO MEV protection features in initial release due to limited applicability on Solana.

**Related Terms:** JITO, Solana, Validators, Front-Running

**Examples:** "MEV bots can front-run large trades by paying higher priority fees"

---

### Microservices
**Definition:** Architectural pattern where application is composed of small, independent services that communicate over network protocols.

**Context:** Architecture evolved to microservices by trading algorithm (ADR-002) and by protocol (ADR-005) in September 2025. Each algorithm (TWAP, DCA, etc.) and protocol (Pump.fun, Raydium, etc.) runs as separate service. Unified transaction layer. Direct frontend communication without API gateway.

**Related Terms:** Architecture, Event-Driven Architecture, Kafka, RabbitMQ, ADR-002, ADR-005

**Examples:** "Microservices architecture allows independent scaling of TWAP and DCA services"

---

### MFA (Multi-Factor Authentication)
**Definition:** Security method requiring multiple verification methods to authenticate users, combining something they know (password) with something they have (device) or are (biometric).

**Context:** Implemented through combination of Auth0 social login, biometric authentication (Face ID/Touch ID), and security password for wallet operations.

**Related Terms:** Auth0, Face ID, Touch ID, Security Password, Authentication

**Examples:** "MFA requires both Google login and Face ID to execute wallet transfers"

---

### Moonshot
**Definition:** A Solana-based protocol for launching and trading new tokens, integrated with Cooking.gg.

**Context:** One of three primary protocols (along with Pump.fun and Raydium) that Cooking.gg integrates with for token trading.

**Related Terms:** Pump.fun, Raydium, Protocol Integration

**Examples:** "Buy this token through Moonshot protocol"

---

### Multilevel Referral
**Definition:** 3-tier referral program structure where users earn commissions from direct referrals (Level 1), their referrals' referrals (Level 2), and third-level referrals.

**Context:** Implemented per ADR-200 for viral growth. Level 1: Full commission tier rate (30-45%), Level 2: Reduced rate, Level 3: Further reduced. Creates network effects and exponential user acquisition.

**Related Terms:** Referral Program, Commission Tiers, Viral Growth, ADR-200

**Examples:** "Multilevel structure means you earn from your referrals and their referrals too"

---

## N

### Next.js Proxy
**Definition:** Server-side proxy layer implemented in Next.js to handle cross-domain cookie authentication between frontend and multiple backend microservices.

**Context:** Implemented in October 2025 as part of cookie-based authentication migration. Solves complexity of multi-service architecture where frontend and backends are on different domains. Handles cookie parsing and forwarding. Allows developers to configure which backends are local vs remote using server-side environment variables (without NEXT_PUBLIC_ prefix).

**Related Terms:** Cookie Authentication, CORS, Microservices, Next.js

**Examples:** "Next.js proxy acts as intermediary for cross-domain cookie handling between frontend and transaction service"

---

### OHLCV (Open/High/Low/Close/Volume)
**Definition:** Standard candlestick chart data format showing opening price, highest price, lowest price, closing price, and trading volume for a time period.

**Context:** Core data format for TradingView integration. Stored in ClickHouse materialized views for high-performance charting per ADR-101. Updated via WebSocket real-time candle updates.

**Related Terms:** TradingView, ClickHouse, Charting, ADR-101

**Examples:** "ClickHouse OHLCV materialized views power 1-second interval charting"

---

### Orca
**Definition:** Solana-based automated market maker (AMM) DEX providing efficient token swaps and liquidity pools.

**Context:** Major liquidity provider on Solana. Pool indexing for Orca considered for Q1 2026 as part of provider-discriminated pricing strategy to improve competitive positioning.

**Related Terms:** AMM, Raydium, Liquidity Pool, DEX, Solana

**Examples:** "Orca pools provide deep liquidity for major Solana token pairs"

---

## O

### Onramper
**Definition:** A crypto on-ramp/off-ramp aggregator providing fiat-to-crypto conversion services through a widget integration.

**Context:** Selected as the primary on-ramp provider for Cooking.gg in July 2025, chosen over Crossmint. Provides widget integration for faster implementation. Subject to KYC/KYB requirements and AML certification verification.

**Related Terms:** On-Ramps, Crossmint, KYC, Fiat Conversion

**Examples:** "Onramper widget allows users to purchase SOL with credit card or bank transfer"

---

## P

### Pam Fun (Pump.fun)
**Definition:** Alternative spelling/pronunciation of Pump.fun protocol name, commonly used in Spanish-speaking team communications.

**Context:** Solana-based token launchpad protocol integrated with Cooking.gg. Protocol underwent updates in October 2025 adding new purchase operation with optional parameters, exposing JavaScript Borsh serialization limitations.

**Related Terms:** Pump.fun, Pam Swap, Raydium, Protocol Integration, Borsh

**Examples:** "Pam Fun protocol update added optional event parameter requiring manual parsing workaround"

---

### Pam Swap (PumpSwap)
**Definition:** DEX/swap protocol on Solana integrated with Cooking.gg indexer, underwent simultaneous updates with Pam Fun in October 2025.

**Context:** Part of protocol integration suite. Updates added optional parameters to event structures, requiring manual parsing due to JavaScript Borsh limitations. Both Pam Fun and Pam Swap updates deployed together.

**Related Terms:** Pam Fun, Pump.fun, DEX, Protocol Integration, Borsh

**Examples:** "Both Pam Fun and Pam Swap were updated with manual parameter trimming for optional fields"

---

### Performance Bonus
**Definition:** Additional 10% earnings on top of commission tiers for referrers who maintain significant personal trading volume.

**Context:** Part of multilevel referral program per ADR-200. Incentivizes referrers to be active traders themselves, not just recruiters.

**Related Terms:** Commission Tiers, Referral Program, Multilevel Referral, ADR-200

**Examples:** "Performance bonus adds 10% to your 45% tier commission for total 55% earnings"

---

### Perpetuals
**Definition:** Perpetual futures contracts that allow traders to speculate on the price of assets with leverage, without an expiration date.

**Context:** Trading feature integrated through Hyperliquid, allowing users to open leveraged positions on token price movements. Also known as "perps" in crypto trading communities.

**Related Terms:** Hyperliquid, Leverage Trading, Futures, USDC, Cross-Margin

**Examples:** "Trade SOL/USD perpetuals with up to 20x leverage on Hyperliquid"

---

### Priority Fee
**Definition:** Additional fee paid on Solana to incentivize validators to prioritize transaction processing, beyond the base transaction fee.

**Context:** Critical for ensuring timely execution in competitive trading scenarios. Higher priority fees increase likelihood of faster transaction inclusion in blocks.

**Related Terms:** Lamports, Solana, Transaction Fees, MEV

**Examples:** "Pay 0.001 SOL priority fee to ensure fast execution during high network congestion"

---

### PnL (Profit and Loss)
**Definition:** The cumulative profit or loss on a token position, calculated using FIFO method to match sales with purchases.

**Context:** Core metric for evaluating trading performance at token-wallet, token-centric, or wallet-centric levels. Used in Diamond Hands calculations.

**Related Terms:** AHT, FIFO, Diamond Hands, Trading Performance

**Examples:** "This wallet has a positive PnL of 150% on this token"

---

### Pump.fun
**Definition:** Popular Solana-based platform for launching and trading meme tokens using a bonding curve mechanism.

**Context:** Primary protocol integrated with Cooking.gg. Many tokens in the Discovery view originate from Pump.fun. Also spelled "Pumpfun" in some contexts. Tokens graduate from bonding curve to full DEX liquidity on Raydium.

**Related Terms:** Bonding Curve, Moonshot, Raydium, Meme Token, Launchpad, Pumpfun

**Examples:** "This token graduated from Pump.fun's bonding curve to Raydium at $69k market cap"

---

## Q

### Quick Operations Panel (QOP)
**Definition:** A persistent, expandable panel in Cooking.gg's header that allows users to manage open positions from any page without navigation.

**Context:** Key differentiating feature providing superior UX compared to competitors. Shows position details, token metrics, and buy/sell options.

**Related Terms:** User Experience, Position Management, Trading Interface

**Examples:** "Click any position in the header to open the Quick Operations Panel"

---

## R

### Referral Code
**Definition:** Custom user identifier used to track and attribute new user registrations to specific referrers.

**Context:** Part of closed beta referral-only access model per ADR-201. Each code grants 25-50 slots. Enables viral growth mechanism and commission tracking.

**Related Terms:** Referral Program, Closed Beta, Referral-Only Access, ADR-201

**Examples:** "Share your referral code CRYPTO2025 to invite friends to closed beta"

---

### Referral Program
**Definition:** User acquisition incentive system where existing users earn commissions by referring new traders to the platform.

**Context:** 3-tier multilevel structure per ADR-200 with 30-45% commission rates plus 10% performance bonus. Critical for viral growth strategy during closed beta.

**Related Terms:** Multilevel Referral, Commission Tiers, Performance Bonus, ADR-200

**Examples:** "Referral program pays 45% commission on fees from users you refer"

---

### Referral-Only Access
**Definition:** Invite-only beta structure where new users can only join through referral codes from existing users.

**Context:** Closed beta launch strategy per ADR-201. Creates exclusivity and viral growth mechanism. Each code grants 25-50 slots. Replicates Bullex Neo market dominance methodology.

**Related Terms:** Closed Beta, Referral Code, Viral Growth, ADR-201

**Examples:** "Platform access requires referral code during closed beta phase"

---

## S

### RabbitMQ
**Definition:** Message queue system used for event-driven architecture and asynchronous communication between microservices.

**Context:** Part of the backend infrastructure enabling decoupled service communication and reliable message delivery across distributed systems.

**Related Terms:** Kafka, Event-Driven Architecture, Microservices

**Examples:** "RabbitMQ queues transaction events for processing by multiple services"

---

### Raydium
**Definition:** An automated market maker (AMM) and decentralized exchange on Solana, integrated with Cooking.gg for token trading.

**Context:** One of three primary protocols (along with Pump.fun and Moonshot) providing liquidity and trading infrastructure.

**Related Terms:** DEX, AMM, Pump.fun, Moonshot, Liquidity

**Examples:** "Trade this token on Raydium for deeper liquidity"

---

### Redis
**Definition:** In-memory data structure store used for high-performance caching and JSON block storage.

**Context:** Implemented for Solana blockchain JSON block storage in June 2025 per ADR-104. Provides 50x-100x faster writes than PostgreSQL, $800/month cost savings, and 5x-10x reprocessing speedup. Critical for indexer performance.

**Related Terms:** Cache, PostgreSQL, Performance, ADR-104

**Examples:** "Redis caches blockchain data for sub-millisecond retrieval times"

---

### REST API
**Definition:** Stateless web API architecture using HTTP methods (GET, POST, PUT, DELETE) for resource manipulation.

**Context:** Primary API architecture for frontend-backend communication. Type-safe client generation from OpenAPI specification per ADR-103 prevents runtime errors.

**Related Terms:** GraphQL, Type-Safe API Client, API, ADR-103

**Examples:** "REST API endpoints provide token data, user positions, and trading operations"

---

### RPC (Remote Procedure Call)
**Definition:** Network communication protocol allowing programs to execute procedures on remote servers as if they were local function calls.

**Context:** Used for Solana blockchain communication via HelloMoon and QuickNode RPC providers. Critical for blockchain data access and transaction submission. QuickNode provides 70M requests/month capacity.

**Related Terms:** HelloMoon, QuickNode, Solana, Blockchain

**Examples:** "RPC calls to Solana nodes fetch transaction history and submit new trades"

---

### RPO (Recovery Point Objective)
**Definition:** Maximum acceptable data loss window measured in time, defining how much data can be lost in a disaster recovery scenario.

**Context:** Platform target is < 15 minutes of data loss. Achieved through regular database backups, transaction logs, and multi-AZ replication per ADR-500.

**Related Terms:** RTO, Multi-AZ, High Availability, Disaster Recovery

**Examples:** "RPO of 15 minutes means we can lose at most 15 minutes of transaction data in worst-case scenario"

---

### RTO (Recovery Time Objective)
**Definition:** Target time to restore service after an outage or disaster, defining maximum acceptable downtime.

**Context:** Platform target is < 4 hours for full service restoration. Achieved through multi-AZ deployment, automated failover, and documented recovery procedures per ADR-500.

**Related Terms:** RPO, Multi-AZ, High Availability, Disaster Recovery

**Examples:** "RTO of 4 hours means we aim to restore full service within 4 hours of any major outage"

---

## S

### Secure Enclave
**Definition:** Apple's dedicated hardware security processor that stores and protects biometric data and cryptographic keys separate from main processor.

**Context:** Critical component for iOS mobile app security per ADR-401. Stores Face ID/Touch ID biometric templates and protects wallet operation authentication. Hardware-backed security preventing key extraction.

**Related Terms:** Face ID, Touch ID, Keychain, iOS Security, ADR-401

**Examples:** "Private keys protected in Secure Enclave, isolated from main iOS system"

---

### Security Password
**Definition:** Additional password required for critical wallet operations (transfers, withdrawals) beyond standard login authentication.

**Context:** Implemented per ADR-400 for wallet operation protection. Client-side hashing with backend encrypted storage. Required for all sensitive wallet actions. Serves as fallback authentication for devices without biometric capabilities.

**Related Terms:** ADR-400, MFA, Biometric Authentication, Wallet Security

**Examples:** "Enter security password to authorize this withdrawal from your wallet"

---

### Social Login
**Definition:** Authentication method allowing users to sign in using existing social media accounts (Google, Apple ID, Twitter/X) instead of creating new credentials.

**Context:** Implemented in September 2025 to support mobile app development. Allows multi-account linking with requirement that one primary method remains linked. Prioritized over other features for mobile development workflow.

**Related Terms:** Authentication, Mobile App, User Onboarding, Auth0, ADR-102

**Examples:** "Sign in with Google, Apple ID, or Twitter without creating a password"

---

### Slippage
**Definition:** The difference between expected price of a trade and the actual executed price, typically caused by market movement or low liquidity.

**Context:** Critical metric for trade execution quality. Higher slippage occurs in low-liquidity tokens. Router optimization (Jupiter) aims to minimize slippage through optimal routing.

**Related Terms:** Jupiter, Liquidity, AMM, Price Impact

**Examples:** "Trade executed with 2.3% slippage due to low liquidity in this token"

---

### Solana
**Definition:** A high-performance blockchain platform known for fast transactions and low fees, primary blockchain for Cooking.gg.

**Context:** Initial blockchain support for the platform, with plans to expand to other chains in future.

**Related Terms:** Blockchain, Meme Token, Protocol

**Examples:** "Cooking.gg is built on Solana for fast, low-cost trading"

---

### SSE (Server-Sent Events)
**Definition:** Real-time data streaming protocol chosen over WebSocket for unidirectional server-to-client updates.

**Context:** Migrated from WebSocket to SSE in August 2025 per ADR-003. Addresses AWS 60-second timeout issues with 25-second heartbeat mechanism. Better scalability for one-way real-time price and position updates. Simpler reconnection handling and infrastructure requirements.

**Related Terms:** WebSocket, Real-Time Updates, ADR-003

**Examples:** "SSE streams real-time price updates with automatic reconnection and 25-second heartbeats"

---

### Stop Loss (SL)
**Definition:** Automated order trigger that closes a position when price drops to a specified level to limit potential losses.

**Context:** Risk management feature discussed for perpetuals implementation. Architectural debate between order-level vs position-level implementation. May be excluded from mobile v1 due to complexity.

**Related Terms:** Take Profit, Trailing Stop, Perpetuals, Risk Management, Hyperliquid

**Examples:** "Set stop loss at -10% to automatically close if position moves against you"

---

### Take Profit (TP)
**Definition:** Automated order trigger that closes a position when price reaches a specified profit level to lock in gains.

**Context:** Risk management feature discussed for perpetuals implementation. Works in conjunction with stop loss for complete position management.

**Related Terms:** Stop Loss, Trailing Stop, Perpetuals, Risk Management, Hyperliquid

**Examples:** "Set take profit at +50% to automatically close and secure gains"

---

### Trailing Stop
**Definition:** Dynamic stop loss that automatically adjusts upward as price moves favorably, locking in profits while allowing continued upside.

**Context:** Advanced risk management feature considered for perpetuals trading. More complex than static stop loss/take profit.

**Related Terms:** Stop Loss, Take Profit, Perpetuals, Risk Management

**Examples:** "Trailing stop at 15% follows price up, selling if price drops 15% from peak"

---

### TWAP (Time-Weighted Average Price)
**Definition:** Trading algorithm that executes large orders by distributing them evenly across a specified time period to reduce market impact.

**Context:** One of the advanced trading algorithms being implemented on the platform. Helps minimize slippage on large orders.

**Related Terms:** VWAP, DCA, Trading Algorithms, Slippage

**Examples:** "Use TWAP to buy 10,000 tokens distributed evenly over 4 hours"

---

### Turnkey
**Definition:** Wallet signing and key management service providing secure wallet infrastructure without users managing seed phrases.

**Context:** Adopted per ADR-501 for wallet management and transaction signing. Integrates with Auth0 social login. Multi-chain support (Solana + EVM for Hyperliquid). Seamless onboarding for "normie" users without seed phrases. $250k-500k savings vs in-house development. Achieved 95% registration completion rate (vs 20-30% wallet-connection).

**Related Terms:** Auth0, Wallet Management, ADR-501, ADR-102, Custodial Wallet

**Examples:** "Turnkey creates and manages wallets automatically on social login via Auth0"

---

### Type-Safe API Client
**Definition:** Compile-time type checking for API client code generated from OpenAPI specification to prevent runtime errors.

**Context:** Implemented per ADR-103 in October 2025. OpenAPI-based TypeScript client generation prevents frontend-backend type mismatches. Triggered by production transfer bug caused by type errors. Eliminates entire class of runtime errors.

**Related Terms:** TypeScript, OpenAPI, REST API, ADR-103

**Examples:** "Type-safe client catches API contract violations at compile time, not runtime"

---

### UDF (Universal Data Feed)
**Definition:** TradingView's data protocol for feeding real-time and historical price data to their charting library.

**Context:** Implemented as adapter layer per ADR-101 to connect ClickHouse OHLCV data to TradingView charts. Enables high-performance charting with 1-second intervals.

**Related Terms:** TradingView, OHLCV, ClickHouse, ADR-101

**Examples:** "UDF adapter translates ClickHouse queries into TradingView-compatible data format"

---

### Stakeholder
**Definition:** Any individual, group, or organization that can affect, be affected by, or perceive itself to be affected by the project.

**Context:** Used in project planning, communication strategies, and decision-making processes.

**Related Terms:** Project Sponsor, End User, Team Member

**Examples:** "We need to consult stakeholders before making this architectural change"

---

## T

### Touch ID
**Definition:** Apple's fingerprint recognition biometric authentication technology using capacitive sensors and Secure Enclave.

**Context:** Required for all trading operations on iOS mobile app per ADR-401 (along with Face ID). Provides hardware-backed security for wallet operations. Used on devices without Face ID capability.

**Related Terms:** Face ID, Biometric Authentication, Secure Enclave, ADR-401

**Examples:** "Authenticate with Touch ID to execute this trade on iPad"

---

### TradingView
**Definition:** Popular charting and technical analysis platform with advanced features for financial markets.

**Context:** Commercial Charting Library integrated per ADR-101 with UDF (Universal Data Feed) adapter. ClickHouse OHLCV materialized views for performance. WebSocket real-time candle updates. Mobile optimization implemented. Advanced API considered for order placement on charts.

**Related Terms:** Charts, Technical Analysis, OHLCV, UDF, ADR-101, ClickHouse

**Examples:** "TradingView charts support 1-second interval candles with real-time updates"

---

### Transaction Relay Service
**Definition:** Backend service that facilitates buy/sell transactions and integrates platform fees while interacting with protocols like Pump.fun, Moonshot, and Raydium.

**Context:** Core technical component enabling trade execution on Cooking.gg.

**Related Terms:** Indexer Service, Protocol Integration, Trade Execution

**Examples:** "The Transaction Relay Service processes your buy order and adds the platform fee"

---

## U

### Unit
**Definition:** A banking/financial service provider integrated for deposit tracking and fiat-to-crypto conversion functionality.

**Context:** Used for tracking deposits and managing on-ramp processes from fiat to cryptocurrency.

**Related Terms:** On-Ramps, Deposits, Fiat Conversion

**Examples:** "Unit tracks deposit status as funds move through the on-ramp process"

---

### USDC (USD Coin)
**Definition:** A stablecoin pegged to the US Dollar, used as collateral and quote currency for perpetuals trading.

**Context:** Required currency for Hyperliquid perpetuals trading. Users can convert SOL to USDC for opening perpetual positions.

**Related Terms:** Hyperliquid, Perpetuals, Stablecoin, Collateral

**Examples:** "Convert 0.2 SOL to USDC to meet the minimum deposit for perpetuals trading"

---

## V

### Vector.fun
**Definition:** A competitor crypto trading platform with mobile app presence, used as reference for regulatory and app store considerations.

**Context:** Referenced during iOS App Store licensing research. Vector operates without full KYC requirements, serving as a model for Cooking.gg's approach.

**Related Terms:** Competitors, App Store, KYC, Mobile App

**Examples:** "Vector.fun successfully lists on the iOS App Store under the finance category without requiring KYC"

---

### Viral Growth
**Definition:** Organic user expansion mechanism where existing users naturally recruit new users through incentivized referral program.

**Context:** Core growth strategy for closed beta per ADR-200 and ADR-201. Multilevel referral structure with 30-45% commissions creates exponential user acquisition. Replicates Bullex Neo market dominance methodology.

**Related Terms:** Referral Program, Multilevel Referral, Closed Beta, ADR-200, ADR-201

**Examples:** "Viral growth mechanism targets 100x user expansion through referral network effects"

---

### VPC (Virtual Private Cloud)
**Definition:** Isolated cloud network within AWS that provides security and control over networking resources.

**Context:** Part of the infrastructure security architecture, isolating production resources from public internet and providing network-level security controls.

**Related Terms:** AWS, Security, Infrastructure, Networking

**Examples:** "Services communicate within the VPC for enhanced security and performance"

---

### VWAP (Volume-Weighted Average Price)
**Definition:** Trading algorithm that executes large orders distributed based on historical volume patterns to minimize market impact.

**Context:** One of the advanced trading algorithms being implemented on the platform. Executes more during high-volume periods and less during low-volume periods.

**Related Terms:** TWAP, DCA, Trading Algorithms, Slippage

**Examples:** "Use VWAP to execute large buy order following typical 24-hour volume distribution"

---

### Vercel
**Definition:** A cloud platform for static sites and serverless functions, used for hosting Cooking.gg's frontend.

**Context:** Platform deployment service with tiered pricing based on team members. Cost optimization achieved through whitelist solution and team member management.

**Related Terms:** Deployment, Frontend Hosting, DevOps

**Examples:** "Reduced Vercel bill from $400 to $200 by removing unnecessary team members using the new whitelist solution"

---

## W

### WAF (Web Application Firewall)
**Definition:** AWS security service that protects web applications from common exploits and attacks.

**Context:** Implemented in September 2025 per ADR-402 with managed rule sets for DDoS protection, SQL injection prevention, and XSS protection. Integrated with CloudFront Shield. Cost ~$79/month for enterprise-grade security.

**Related Terms:** AWS, Security, CloudFront, ADR-402

**Examples:** "WAF blocked 1,247 malicious requests this month using AWS managed rules"

---

### Webhook
**Definition:** HTTP callback mechanism for event notifications, allowing servers to push data to other systems when events occur.

**Context:** Used for integrating with third-party services and triggering automated workflows based on platform events.

**Related Terms:** REST API, Event-Driven Architecture, API Integration

**Examples:** "Webhook notifies external system when large trade is executed"

---

### WebSocket
**Definition:** Bidirectional real-time communication protocol, replaced by SSE for most use cases.

**Context:** Originally used for real-time updates but migrated to SSE in August 2025 due to AWS 60-second timeout issues and infrastructure complexity. SSE better suited for unidirectional server-to-client updates per ADR-003.

**Related Terms:** SSE, Real-Time Updates, ADR-003

**Examples:** "WebSocket was replaced by SSE for more reliable real-time price streaming"

---

## X

### [Term Name]
**Definition:**

**Context:**

**Related Terms:**

**Examples:**

---

## Y

### [Term Name]
**Definition:**

**Context:**

**Related Terms:**

**Examples:**

---

## Z

### [Term Name]
**Definition:**

**Context:**

**Related Terms:**

**Examples:**

---

## Acronyms Quick Reference

| Acronym | Full Form | Definition |
|---------|-----------|------------|
| ACM | AWS Certificate Manager | SSL/TLS certificate management |
| ADR | Architecture Decision Record | Document capturing important decisions |
| AHT | Average Holding Time | Average duration a wallet holds a token |
| AMM | Automated Market Maker | DEX protocol for automated trading |
| API | Application Programming Interface | Set of protocols for building software |
| AWS | Amazon Web Services | Cloud computing platform |
| DCA | Dollar Cost Averaging | Time-distributed order strategy |
| DEX | Decentralized Exchange | Peer-to-peer cryptocurrency exchange |
| ECS | Elastic Container Service | AWS container orchestration |
| EKS | Elastic Kubernetes Service | AWS Kubernetes service |
| FIFO | First-In-First-Out | Accounting method for tracking trades |
| IAM | Identity and Access Management | AWS permission system |
| JWT | JSON Web Token | Authentication token format |
| KYB | Know Your Business | Business identity verification |
| KYC | Know Your Customer | Customer identity verification |
| MEV | Maximal Extractable Value | Transaction reordering profit |
| MFA | Multi-Factor Authentication | Multiple verification methods |
| OHLCV | Open/High/Low/Close/Volume | Candlestick chart data format |
| PnL | Profit and Loss | Trading performance metric |
| QOP | Quick Operations Panel | Header panel for position management |
| REST | Representational State Transfer | Web API architecture |
| RPC | Remote Procedure Call | Network communication protocol |
| RPO | Recovery Point Objective | Acceptable data loss window |
| RTO | Recovery Time Objective | Target recovery time |
| SL | Stop Loss | Automatic loss prevention |
| SOL | Solana | Native token of Solana blockchain |
| SSE | Server-Sent Events | Real-time streaming protocol |
| TP | Take Profit | Automatic profit-taking |
| TWAP | Time-Weighted Average Price | Time-distributed orders |
| UDF | Universal Data Feed | TradingView data protocol |
| USDC | USD Coin | US Dollar stablecoin |
| VPC | Virtual Private Cloud | Isolated cloud network |
| VWAP | Volume-Weighted Average Price | Volume-distributed orders |
| WAF | Web Application Firewall | Security layer |

---

## Common Phrases and Conventions

### "[Project-Specific Phrase]"
**Meaning:** What this phrase means in the context of this project

**When Used:** Typical situations where this phrase appears

**Example:** "We need to [phrase] before we can proceed"

---

## Deprecated Terms

These terms are no longer in use but may appear in older documents:

### [Old Term Name]
**Was:** Old definition

**Now Use:** [New term or approach]

**Deprecated:** YYYY-MM-DD

**Reason:** Why this term was deprecated

---

## Maintenance Notes

**Last Major Review:** YYYY-MM-DD
**Next Scheduled Review:** YYYY-MM-DD
**Maintainer:** [Name/Team]

### How to Add New Terms
1. Determine the appropriate alphabetical section
2. Use the template format (Term, Definition, Context, Related Terms, Examples)
3. Update the "Last Updated" date in the frontmatter
4. If adding an acronym, also add to the Acronyms Quick Reference table

### Review Process
- Monthly review during regular maintenance
- Ad-hoc updates as new terminology emerges
- Remove or deprecate terms that are no longer relevant
