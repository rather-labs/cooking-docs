---
title: Cooking Demo - ClickHouse Migration & Liquidity Tracking
date: 2025-07-04
type: demo
attendees:
  - Lucas Cufré
  - Gregory Chapman (greg@ember.app)
  - Martin Aranda
  - Naji Osmat
  - Zen (z@ember.app)
status: completed
tags:
  - demo
  - clickhouse
  - liquidity-tracking
  - jupiter-integration
  - amm-lifecycle
  - token-metrics
related:
  - "[[2025-06-27-cooking-demo]]"
  - "[[04-knowledge-base/technical/architecture/clickhouse-migration]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team successfully completed migration to the new ClickHouse server, achieving significant performance improvements with the system now live in production. Jupiter-supported tokens are being indexed and expected to be tradable by mid-next week. A key technical discussion centered on liquidity tracking challenges after tokens migrate from AMMs like Pump.fun to DEXes, with the decision to track liquidity only on platforms where it's accurately measurable (Pump.fun and Radium) while providing approximations for Moonshot and Jupiter tokens. The Martian development team was approved to begin mobile development work with a tight 90-day timeline to product readiness by end of September.

## Meeting Details

**Duration:** 27 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Martian Development Team Onboarding

**Context:** Discussion about the mobile development team recommended by Leo.

**Key Points:**
- Team appears professional and well-recommended
- Lucas emphasized conservative design choices due to tight timeline
- 90-day window to have product ready by end of September
- Naji noted that simplicity in UX often requires more time to achieve

**Decision:** Proceed with Martian team with focus on simplicity and timeline constraints

### 2. Development Progress Updates

**Backend Achievements:**
- Hyperliquid core integration operational
- Solana deposit flow testing in progress
- Core service integration underway
- Turnkey integration on Hyperliquid side progressing

**ClickHouse Migration:**
- Successfully migrated transfers, holders, traders, and wallets to new server
- Significant performance improvement achieved
- **Major milestone:** System is now live in production
- No new issues reported since migration

**Indexer Progress:**
- Finished indexing Jupiter-supported tokens
- Expected to be tradable by mid-next week
- Working on completing trading functionality

**Frontend Updates:**
- Testing skeleton loaders for active positions, model portfolio page, and referrals
- New components for tooltips, colors, icons, and links completed
- Started work on perpetuals screen

**Mobile Development:**
- New mobile engineer onboarded
- Infrastructure and native components set up
- Work begun on color alignment and signup/login/home flows
- Social login integration (Telegram) achieved

### 3. AMM and Token Metrics Lifecycle Challenge

**Problem Statement:** How to track token metrics after migration from platforms like Pump.fun to Pump.swap, where market cap resets to zero.

**Technical Challenge:**
- All metrics except liquidity can be tracked by indexing blocks (volume, total transactions, etc.)
- Liquidity tracking requires looking across all protocols that have indexed a particular token
- This is a one-to-many situation rather than straightforward block indexing

**Industry Standard Approach:**
- Most platforms use two separate links for pre-migration and post-migration tokens
- No protocol has successfully combined both into one chart

**Proposed Solutions Discussed:**

1. **Track via Total Value Locked (TVL)**
   - Would require indexing all protocols supporting each token
   - Represents a significant feature in itself

2. **Protocol-Specific Tracking:**
   - Pump.fun: TVL can be tracked
   - Moonshot: Does not provide TVL information directly
   - Radium: Liquidity is trackable (confirmed by third-party tools like Dex Screener)
   - Jupiter: API might not provide direct liquidity for all aggregated AMMs

3. **Hybrid Approach (Final Decision):**
   - Track truthful liquidity values for Pump.fun and Radium only
   - Show approximate values for Moonshot and Jupiter tokens
   - Use formulas to approximate liquidity for AMMs
   - Display disclaimer if needed

**Key Insights:**
- Moonshot provides approximation for liquidity (accuracy questionable)
- Jupiter's aggregation across multiple pools makes accurate calculation difficult
- Other tracking platforms (Dex Screener, Axiom) don't clarify calculation methods
- Industry operates in a "black box" manner regarding liquidity calculations

### 4. Jupiter API and Latency Concerns

**Considerations:**
- Potential latency issues when fetching liquidity values
- Need for real-time updates
- Risk of hitting rate limits when fetching for every token
- Infinite token supply makes comprehensive tracking challenging

**Action Items:**
- Martin to investigate Jupiter API latency for liquidity updates
- Team to reconvene Monday to finalize liquidity tracking approach

### 5. ClickHouse Server Status

**Confirmation:**
- Ram successfully accessed new server
- All data migrated successfully
- System fully operational
- No new issues reported

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Proceed with Martian development team | Professional, recommended by Leo | Mobile development begins immediately |
| Prioritize simplicity in design | 90-day timeline to September deadline | May sacrifice some "bells and whistles" |
| Track truthful liquidity only for Pump.fun and Radium | These platforms provide accurate data | Clear differentiation in data quality |
| Use approximations for Moonshot and Jupiter | Industry standard approach | Acceptable with or without disclaimer |
| Don't reveal unsupported protocols | Avoid showing system limitations | Maintain competitive positioning |
| Continue with ClickHouse deployment | Performance improvements critical | Production environment stabilized |

## Action Items

### High Priority

- [ ] **Martin** - Get clarity on Jupiter API latency for liquidity information updates (Due: Before Monday, July 7, 2025)
- [ ] **Team** - Reconvene Monday to finalize liquidity tracking resolution (Due: July 7, 2025)

### Medium Priority

- [ ] **Backend Team** - Complete Jupiter token trading functionality (Due: Mid-next week, ~July 9, 2025)
- [ ] **Martin** - Investigate formulas for AMM liquidity approximation (Due: July 7, 2025)

### Completed

- [x] **Naji** - Resolve ClickHouse server access issues
- [x] **Backend Team** - Migrate all data to new ClickHouse server
- [x] **Team** - Deploy production environment

## Technical Notes

### Liquidity Tracking Approach

**Trackable Platforms:**
- Pump.fun: Full TVL tracking available
- Radium: Liquidity trackable (supported by Dex Screener, Dex Tools)
- Pump.swap: Trackable once token migrates

**Approximation Required:**
- Moonshot: No direct TVL, approximation using Solana and token amounts
- Jupiter: Aggregated pools make direct calculation difficult
- Formula-based approach using available data points

### Data Indexing Strategy

**Block-Based Metrics (Available):**
- Volume
- Total transactions
- Total supply
- Market cap
- Total buys
- Total sells

**Protocol-Based Metrics (Challenging):**
- Liquidity (requires protocol-specific indexing)
- Pool information
- AMM-specific data

### Performance Metrics

**ClickHouse Migration Results:**
- Transfers: Migrated successfully
- Holders: Migrated successfully
- Traders: Migrated successfully
- Wallets: Migrated successfully
- Performance: Significant improvement noted
- Status: Live in production with no issues

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Tight 90-day timeline | Quality vs. speed trade-off | Focus on core functionality, simple UX |
| Liquidity tracking complexity | User trust in data accuracy | Clear disclosure, industry-standard approach |
| Jupiter API rate limits | Scalability concerns | Investigate latency and feasibility |
| Moonshot data approximation | Potential inaccuracy | Accept as industry norm, no disclosure |

## Next Steps

1. **Monday, July 7:** Team meeting to finalize liquidity tracking approach
2. **Mid-Next Week:** Jupiter-supported tokens become tradable
3. **Ongoing:** Continue mobile development with Martian team
4. **September 30:** Target deadline for product readiness

## Key Metrics & Numbers

- **Timeline to product readiness:** 90 days (end of September)
- **ClickHouse migration scope:** Transfers, holders, traders, wallets
- **Jupiter tokens:** Indexing complete, trading by mid-next week
- **Supported AMMs:** Pump.fun, Moonshot, Radium (Pump.swap trackable post-migration)
- **Jupiter aggregated AMMs:** 50+ protocols

## References

- Pump.fun - Launch platform with TVL tracking
- Pump.swap - Migration destination with liquidity tracking
- Moonshot - Launch platform (limited TVL data)
- Radium - DEX with trackable liquidity
- Jupiter - Aggregator supporting 50+ AMMs
- Dex Screener - Third-party tracking tool
- Dex Tools - Third-party tracking tool
- Axiom - Competitor tracking platform

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
