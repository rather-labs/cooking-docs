---
title: Q2 & Q3 2025 Product Roadmap
type: roadmap
date: 2025-05-13
tags:
  - roadmap
  - product-planning
  - development-timeline
  - feature-prioritization
summary: Comprehensive development roadmap for Q2 and Q3 2025, outlining prioritized features and resource allocations
---

# Q2 & Q3 2025 Product Roadmap

## Executive Summary

Following strategic discussions with Zain, Naji, and Greg, we've aligned on development priorities for the next phase. The Cooking trading terminal is positioned for experienced Solana traders, with a long-term goal of simplifying onboarding for non-web3 users.

**Important Note**: Time estimates are effort-based rather than fixed delivery dates, allowing flexibility to adjust priorities as needed.

## Prioritized Feature Development

### 1. Support Jupiter Listed Tokens

**Description**: Enable users to search and operate tokens listed in the Jupiter API, leveraging Jupiter as an aggregator of protocols and launchpads.

**Time Estimate**: 8 weeks
**Resources Required**:
- 1 Indexer
- 1 Frontend Developer
- 1 Backend Developer

---

### 2. Support and Trade Perpetuals through HyperLiquid DEX

**Description**: Enable Cooking users to interact with Perpetual contracts on the HyperLiquid DEX and chain.

**Technical Approach**:
- Connect custom UI to HyperLiquid APIs
- Execution takes place on HyperLiquid DEX
- Provide seamless bridge for Solana liquidity consumption on other chains
- Collect fees on cross-chain transactions

**Time Estimate**: 6-8 weeks
**Resources Required**:
- 1 Indexer
- 1 Frontend Developer
- 1 Backend Developer

---

### 3. Improve Security on Wallet Manager

**Purpose**: Enhance security framework within the trading terminal

**Key Features**:
- Mandatory security password for critical operations
- Secure private key management
- Authorized execution for:
  - Generating withdraw wallets
  - Executing transfers
- Improved user confidence in wallet management

**Time Estimate**: 4 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 4. Upgrade the Charts SDK

**Description**: Enhance chart capabilities using TradingView's Advanced Charts SDK

**Included Features**:
- Expanded chart functionality
- Enhanced data visualization
- Multiple chart views support

**Out of Scope**:
- Target prices from charts (requires Trading Platform API)
- Multiple charts in same view (requires Trading Platform API)

**Time Estimate**: 3 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 5. Technical Stress Testing

**Objective**: Ensure production readiness through comprehensive stress testing

**Testing Scenarios**:
- High transaction volumes in short windows
- Concurrent user login stress tests
- Breaking point identification and improvement
- Performance benchmarking

**Time Estimate**: 8 weeks
**Resources Required**:
- 1 Indexer
- 1 Frontend Developer
- 1 Backend Developer

---

### 6. Referral Program v2 - Multi-level

**Purpose**: Enhance user acquisition and engagement

**Features**:
- Multilevel commission structure
- Earnings from direct referrals and sub-referrals
- Higher commission opportunities based on trading fees
- Community building incentives

**Time Estimate**: 4 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 7. Multi Language Support

**Description**: Expand platform accessibility through internationalization

**Implementation**:
- Multi-language solution with user preference settings
- Dictionary repository construction
- LLM-powered high-fidelity translations

**Time Estimate**: 4 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 8. Improve Tables and Bubblemaps

**Enhancement Areas**:
- Token Holders table expansion
- Transactions table improvements
- Top Traders table enhancements
- Bubblemaps implementation

**Time Estimate**: 3 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 9. Import Existing Solana Wallets

**Description**: Enable operation with externally-generated Solana wallets

**Benefits**:
- Peace of mind for experienced traders
- Full custody of private keys
- Increased platform adoption

**Time Estimate**: 2 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 10. New Login Methods

**Purpose**: Lower entry barriers for non-web3 users

**Supported Methods**:
- Email authentication
- X/Twitter social login
- Apple ID
- Gmail
- Direct wallet connection

**Time Estimate**: 4 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 11. Auto Adjusting Priority Fee

**Description**: Reduce cognitive load through intelligent fee management

**Implementation**:
- Dynamic priority fee adjustment
- Network consultation for optimal fees
- Application to open-ended positions (limit, DCA, TWAP, VWAP, Custom)

**Time Estimate**: 4 weeks
**Resources Required**:
- 1 Indexer
- 1 Frontend Developer
- 1 Backend Developer

---

### 12. Portfolio Wide TP/SL

**Description**: Portfolio-level risk management strategies

**Features**:
- Overarching risk management
- Multiple parameter strategies
- Strategy pause and deletion
- Portfolio-wide application

**Time Estimate**: 2 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 13. Multi Chart View

**Description**: Advanced trading interface for seasoned traders

**Capabilities**:
- 2-4 simultaneous charts
- Token information filtering
- Chart resizing and sorting
- Position monitoring across multiple tokens

**Time Estimate**: 3 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

---

### 14. Market Cap Percentage Variation Algorithm

**Purpose**: Enable new profit generation strategies

**Description**: Allow traders to open positions based on market capitalization variation

**Features**:
- Specific parameter definition for trades
- Enhanced trading experience
- Strategic decision-making tools

**Time Estimate**: 4 weeks
**Resources Required**:
- 1 Frontend Developer
- 1 Backend Developer

## Resource Summary

### Total Effort Estimates by Feature Category

- **Infrastructure & Security**: 15 weeks
- **Trading Features**: 14-16 weeks
- **User Experience**: 13 weeks
- **Analytics & Visualization**: 6 weeks
- **Strategy & Algorithms**: 6 weeks

### Team Composition Requirements

Consistent need for:
- Indexer specialists
- Frontend developers
- Backend developers

## Success Metrics

- Production readiness by end of Q3
- Successful stress test completion
- Feature adoption rates
- User acquisition through referral program
- Trading volume increases

## Cross-References

- Related to: [[stakeholder-requirements]] - Requirements driving this roadmap
- Related to: [[beta-release-q3-2025]] - Beta release specifications
- Related to: [[platform-vision-requirements]] - Strategic vision alignment