---
title: Cooking Demo - iOS App Strategy & Perpetuals UI
date: 2025-06-27
type: demo
attendees:
  - Lucas Cufré
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Naji Osmat
  - Martin Aranda
status: completed
tags:
  - demo
  - ios-app
  - kyc-requirements
  - perpetuals
  - performance-optimization
  - clickhouse
related:
  - "[[2025-06-20-cooking-demo]]"
  - "[[04-knowledge-base/technical/architecture/clickhouse-migration]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team discussed critical iOS App Store strategy considerations including category selection, KYC requirements, and Apple's in-app purchase policies. Lucas presented initial perpetuals trading screen designs integrating Hyperliquid, while Martin reported significant backend performance improvements through ClickHouse integration. Key decisions included prioritizing Europe/North America markets, conducting performance optimization research to match competitors like Echo, and shifting social login implementation earlier to support mobile app development. Production deployment awaits AWS ClickHouse database approval.

## Meeting Details

**Duration:** 53 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. iOS App Store Strategy & Compliance

**Context:** Lucas researched requirements for listing a crypto trading app on the iOS App Store.

**Key Points:**
- **Challenge:** No specific App Store category for trading terminals; risk of being classified as gambling
- **Proposed Solution:** List under "Finance" category, similar to Vector.fun
- **KYC Concerns:** Full KYC might deter native DGEN users, but web app would remain KYC-free
- **Comparison:** Vector and MetaMask don't require KYC for trading/swaps, suggesting it's avoidable through licensing
- **Apple Fees:** 20% in-app purchase fee doesn't apply to on-ramping (confirmed by Gregory's experience with MetaMask)
- **Licensing:** Legal team can pursue necessary licenses if provided examples from other apps

**Key Takeaways:**
- Finance category is viable for App Store listing
- KYC may be avoidable through proper licensing
- On-ramping is not classified as in-app purchase
- Need to investigate licenses held by Vector and similar apps

### 2. Target Market & Go-to-Market Strategy

**Initial Market Focus:**
- **Primary:** Europe and North America (main iOS markets)
- **Secondary:** Rest of world
- **Additional:** GCC area (UAE, Saudi Arabia) to be investigated

**Compliance Considerations:**
- EU compliance requirements more stringent than North America
- May affect go-to-market timeline
- Need legal consultation for market-specific requirements

### 3. Whitelist Solution & Production Readiness

**Status:** Completed and tested

**Features:**
- Full control over who can access Cooking platform
- Ready for production deployment pending approvals
- Backend and indexer stable after stress testing

**Production Blockers:**
- AWS ClickHouse database approval required
- ClickHouse database needed within same VPN as servers
- Estimated go-live: Monday or Tuesday (after approval)

**Key Decision:** ClickHouse is critical for good product performance

### 4. Cost Optimization - Vercel

**Current Status:**
- Reduced Vercel bill from $400 to $200 by removing team members
- Leveraging new whitelist solution instead of Vercel whitelisting

**Action Plan:**
- Further reduce costs by limiting team members ($20 per member)
- Keep only essential personnel (deployment and account owner)
- Move most team members to guest access once production is live

### 5. AWS Migration Plans

**Current Situation:**
- Previous migration to existing AWS account faced too many issues
- Billing issues with current AWS setup

**Updated Plan:**
- Create new AWS environment around August 2025
- Target for beta launch in September 2025
- New AWS account will be main one going forward

### 6. Performance Optimization Research

**Current Status:**
- Refactored cache service for better platform consistency
- Martin's research identified significant execution time improvements:
  - **Initial:** 6-8 seconds
  - **Current:** 2.5-3 seconds (after optimization)
  - **Target:** 1.5-2 seconds (with additional refactoring)

**Competitor Comparison:**
- **Echo** achieves sub-second chart and execution times
- Echo can chart and execute on 1-second intervals
- Indexer currently runs with 200-300ms latency after blockchain state

**Key Discussion Points:**
- Echo is a "unicorn" with extremely fast performance
- Team uncertain if current resources can match Echo's speed
- Lucas personally advocates for prioritizing speed over other backlog items
- Zen emphasizes extreme importance for user retention and attraction

**Decision:**
- Schedule dedicated research sprint on performance optimization
- Sprint to focus on: indexer, charts, and data optimization
- Timeline: After Hyperliquid and mobile app planning research
- Goal: Explore ways to match Echo's performance levels

**Technical Opportunities:**
- Further token fetching refactor (potential 1.5s improvement)
- Skip Turnkey signing, sign directly (saves ~0.5s, but increases security risk)
- ClickHouse integration will significantly help

### 7. Backend Progress

**Jupiter Supported Tokens:**
- Continued progress, dependent on ClickHouse integration
- Ready for testing once ClickHouse is available

**Indexer Improvements:**
- Migrations to new indexer provider improved performance
- Better performance for: bar data, last traded prices, token details, positions
- ClickHouse integration completed on indexer side
- Indexer latency: 200-300ms after blockchain state

**Hyperliquid Integration:**
- Started core Hyperliquid integration into backend
- Initial phase complete

### 8. Frontend UI Improvements

**Completed:**
- Normalized model structure across all models
- Added skeleton loaders to quick operations panels
- Implemented skeleton loaders on most pages
- Created 404 screen for invalid token addresses
- Normalized table structure
- Started work on perpetuals screen

**User Experience:**
- Better loading experience with skeleton loaders
- Improved error handling with 404 screen
- More consistent UI across platform

### 9. Perpetuals Screen Design & Functionality

**Overview:** Lucas presented initial designs for perpetuals trading interface

**Key Features:**

**Navigation & Wallet:**
- New menu entry for perpetuals
- Modified wallet menu showing USDC and Solana balances
- Convert and deposit options with dual-select button
- Estimated exchange rates displayed with fee considerations

**Deposit/Transfer:**
- Initial phase: Quick transfers only (not slow/batched transfers)
- **Minimum deposit:** 0.2 SOL (fixed in Solana, not USDC)
- Deposit flow: Spot wallet → Hyperliquid Solana wallet → Spot sale → Perpetual wallet (USDC)
- Withdrawal flow: Reverse of deposit
- Network selector for deposits from external wallets

**Trading Interface:**
- Market order form with leverage modifier
- Variable leverage per contract (e.g., SOL/USD at 20x)
- Contract selector modal for choosing trading pairs
- Two screen sizes supported:
  - Large screen (15"): Full order book and trades
  - Small screen (<14", ~13"): Compact order book view

**Positions & Orders:**
- Position aggregation: Multiple positions on same token are combined
- "One way" feature: New positions add to or subtract from existing holding
- Leverage averages when positions are combined
- Initial version: No editing take-profit/stop-loss after position opens
- Edit functionality to come with limit orders implementation

**Data Tables (from Hyperliquid):**
- **Position History:** Long/short, direction, size, position value (notional)
- **Funding History:** Timestamp, amount paid/received, rate (based on oracle vs mark price difference)
- **Order History:** Executed orders per position
- No leverage display in trade history (set at position creation)

**Roadmap Items (Not in Initial Release):**
- Minimizable/collapsible interface sections
- Setting orders directly on chart (requires $25k TradingView API)
- Editing take-profit/stop-loss after position opens
- Expanded chart functionality

**Hyperliquid-Specific Features:**
- Positions aggregate automatically (can't have multiple positions with different leverages)
- Long and short positions on same token cancel each other out
- Margin liberated based on position changes
- Funding cycles: Long pays short (or vice versa) based on oracle/mark price difference

### 10. Priority Shift: Social Login

**Rationale:**
- Mobile app development starting next Monday
- Mobile developer onboarding next week
- Having social login ready enables parallel development
- Mobile dev can work on authentication while team works on Hyperliquid integration

**Implementation Plan:**
- Move social login earlier in priority queue
- Include: Apple ID, Google login, Twitter login
- Perform in parallel with Hyperliquid integration

**Benefits:**
- Better workflow for mobile development
- Less waiting time for mobile developer
- Streamlined mobile app development process

**Decision:** Team agreed to prioritize social login implementation

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Target Finance category for iOS App Store | Similar apps (Vector) use this successfully | Avoids gambling/casino classification |
| Focus on EU & North America markets first | Primary iOS markets | May require additional compliance work |
| Investigate GCC area (UAE, Saudi) | Potential market opportunity | Additional research needed |
| Schedule performance optimization research sprint | Critical for user retention | Timeline: After Hyperliquid and mobile planning |
| Implement quick transfers only initially | Faster time to market | 0.2 SOL minimum deposit requirement |
| No minimizable UI sections in initial perpetuals release | Focus on core functionality | Roadmap item for future |
| Don't include chart order-setting initially | Requires expensive TradingView API ($25k) | Revisit after other priorities |
| Shift social login implementation earlier | Support mobile app development | Enables parallel development workflows |
| Production deployment waits for ClickHouse | Required for performance | Target: Monday or Tuesday |
| Reduce Vercel team members further | Cost optimization ($20/member) | Keep essential personnel only |
| Create new AWS environment for beta | Previous migration had too many issues | Target: August 2025 |

## Action Items

### High Priority

- [ ] **Zen** - Investigate licenses held by Vector.fun and similar crypto apps for App Store operation without KYC; inform legal team (Due: July 4, 2025)
- [ ] **Naji** - Complete AWS ClickHouse setup and configuration (Due: Within 1 hour of meeting, URGENT)
- [ ] **Naji** - Notify Lucas when ClickHouse integration is complete (Due: Same day)
- [ ] **Martin** - Message Naji on Slack if further action needed for ClickHouse prod environment config (Due: As needed)

### Medium Priority

- [ ] **Lucas & Team** - Conduct research sprint on optimizing execution speeds to match Echo (Target: After Hyperliquid & mobile research)
- [ ] **Lucas** - Research GCC area markets (UAE, Saudi Arabia) (Due: July 10, 2025)
- [ ] **Martin** - Provide list of Vercel members' emails to Zen for cost reduction (Due: July 3, 2025)
- [ ] **Lucas** - Send email with meeting minutes (Due: June 27, 2025)

### Low Priority

- [ ] **Gregory** - Monitor Vercel payments and address any issues (Ongoing)
- [ ] **Team** - Notify Gregory of any Vercel payment failures (As needed)

## Technical Notes

### ClickHouse Integration
- Critical for performance improvements
- Required in same VPN as servers
- AWS plugin needs to be enabled
- Blocks production deployment

### Performance Optimization Opportunities
1. Further token fetching refactor (-1.5s estimated)
2. Direct signing vs Turnkey (-0.5s, but security trade-off)
3. ClickHouse migration (significant improvement expected)
4. Indexer optimizations

### Hyperliquid Quirks Discovered
- "One way" position aggregation
- Leverage averaging on combined positions
- Funding cycle mechanics
- 0.2 SOL minimum for quick transfers

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| iOS App Store approval uncertainty | Market access delay | Research similar apps' licensing |
| AWS ClickHouse approval pending | Production deployment blocked | Naji to complete setup ASAP |
| Performance not matching Echo | User retention risk | Dedicated research sprint planned |
| EU compliance requirements | Extended go-to-market timeline | Legal consultation needed |
| 0.2 SOL minimum deposit | May deter small traders | Clear user communication required |

## Next Steps

1. **Immediate:** Complete AWS ClickHouse setup (Naji - same day)
2. **This Week:** Deploy to production environment (Monday/Tuesday)
3. **Next Week:** Onboard mobile developer and begin app development
4. **Upcoming:** Begin social login implementation (moved up in priority)
5. **Future Sprint:** Performance optimization research (after Hyperliquid & mobile planning)

## Key Metrics & Numbers

- **Vercel cost reduction:** $400 → $200 (50% decrease)
- **Execution time improvement:** 6-8s → 2.5-3s (60% improvement)
- **Target execution time:** 1.5-2s (another 40-50% improvement planned)
- **Indexer latency:** 200-300ms after blockchain state
- **Hyperliquid minimum deposit:** 0.2 SOL
- **Example leverage:** SOL/USD at 20x
- **TradingView advanced API cost:** $25k

## References

- Vector.fun - iOS App Store listing example
- Echo - Performance benchmark competitor
- Hyperliquid - Perpetuals integration provider
- ClickHouse - Database performance solution

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
