---
title: Liquidity Pools - 2025-10-14
type: meeting
meeting_type: technical_deep_dive
topic: Liquidity Pools
date: 2025-10-14
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Liquidity Pools Technical Discussion - Cooking.gg
**Date:** October 14, 2025, 13:58 GMT-03:00
**Duration:** ~44 minutes
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk

## Executive Summary
Comprehensive discussion on Radium indexing challenges, Echo integration complications specific to liquidity pools, and the fundamental trade-offs between routing optimization and data indexing completeness. The team made critical decisions about protocol coverage scope and Echo integration limitations.

## Meeting Context
As Echo integration discussions continued with the client, the team discovered deeper architectural incompatibilities related to how Radium handles liquidity pools and routing. This meeting explored the technical depth of these issues and established clear boundaries for what can and cannot be supported.

## Technical Discussion

### Radium Liquidity Pool Architecture
**Radium's Evolution**:
- **Phase 1 (Legacy)**: All swaps through Radium AMM contract (MP8)
  - Simple architecture, easy to index
  - All trades visible by monitoring one contract
- **Phase 2 (Current)**: Multiple routing paths
  - Direct pool access (CPMM, CLMM contracts)
  - AMM aggregation routes
  - Cross-pool routing for optimized prices

**Indexing Challenge**:
- **Old Approach**: Monitor Radium AMM → see all Radium trades
- **New Reality**: Trades can bypass AMM contract → invisible to indexer
- **Echo's Approach**: Direct pool routing → bypasses monitored contracts

### Echo + Radium Incompatibility
**The Core Problem**:
```
User wants to trade TOKEN on Radium
Radium has 3 liquidity pools for TOKEN:
  - Pool A: SOL/TOKEN (Constant Product)
  - Pool B: USDC/TOKEN (Constant Product)
  - Pool C: SOL/TOKEN (Concentrated Liquidity)

Traditional Router (Jupiter):
  ✅ Evaluates all pools
  ✅ Routes through Radium AMM contract
  ✅ Cooking indexer sees the trade
  ✅ Best price guaranteed

Echo Router:
  ✅ Evaluates all pools
  ❌ Routes directly to Pool C (fastest, not through AMM contract)
  ❌ Cooking indexer doesn't see the trade
  ❓ Best price maybe (depends on pool state at execution)
```

**Impact on Cooking**:
- Trade executes successfully
- User balance updates correctly
- **But**: Trade missing from history, charts, analytics
- **Result**: Broken user experience

### Proposed Solutions & Trade-offs
**Option 1: Index Every Liquidity Pool**
- **Approach**: Monitor all individual pool contracts
- **Pros**: Complete data coverage, no missed trades
- **Cons**:
  - Hundreds of pools currently, thousands in future
  - New pools created daily
  - Massive indexer complexity
  - High operational cost
  - Constant maintenance burden

**Option 2: Index Main Contracts + Jupiter**
- **Approach**: Current system (what Cooking does today)
- **Pros**: 80% coverage with 20% effort, stable, maintainable
- **Cons**: Miss direct pool swaps (including Echo trades)

**Option 3: Hybrid Approach**
- **Approach**: Main contracts + top N high-volume pools
- **Pros**: Better coverage without full pool indexing
- **Cons**: Still miss long-tail pools, complexity increase

**Team Decision**: **Option 2** - Focus on Jupiter + main contracts
- Jupiter captures ~80% of Solana trade volume
- Proven reliability
- Architectural alignment with Cooking
- Acceptable trade-off

### Jupiter vs Echo: Architectural Philosophy
**Jupiter's Advantage**:
- **Centralized Entry Point**: All trades through Jupiter aggregator contract
- **Event Emission**: Emits CPI (Cross-Program Invocation) logs with full swap details
- **Known Universe**: Finite set of contracts to monitor
- **Indexer-Friendly**: Designed for observability

**Echo's Philosophy**:
- **Direct Pool Access**: Bypass aggregators for speed
- **Minimal Overhead**: No intermediate contracts
- **User-Centric**: Optimized for trader, not for data observers
- **Indexer-Hostile**: Not designed with third-party indexing in mind

**Fundamental Incompatibility**:
- Echo's design optimizes for execution speed
- Cooking's architecture requires comprehensive data capture
- No technical solution without changing one side's fundamentals

### Echo Integration: Final Scope Definition
**Confirmed Working Scenarios**:
1. **Pump.fun tokens (Kitchen phase)**
   - Single liquidity pool (bonding curve)
   - All transactions through F6P contract (indexed)
   - ✅ Safe to integrate

2. **Launch Lab tokens (Kitchen phase)**
   - Single liquidity pool (bonding curve)
   - All transactions through 3UJ contract (indexed)
   - ✅ Safe to integrate

**Confirmed Non-Working Scenarios**:
1. **Radium tokens (any)**
   - Multiple liquidity pools
   - Echo routes directly to pools
   - ❌ Cannot integrate without data loss

2. **Orca, Meteora, other AMMs**
   - Similar pool architecture to Radium
   - Direct routing bypasses main contracts
   - ❌ Cannot integrate without data loss

**Integration Decision Matrix**:
| Protocol | Token Stage | Echo Compatible? | Reasoning |
|----------|-------------|------------------|-----------|
| Pump.fun | Kitchen (< 100% bonding) | ✅ Yes | Single pool, indexed contract |
| Pump.fun | Graduated (on DEX) | ❌ No | Multiple pools possible |
| Launch Lab | Kitchen | ✅ Yes | Single pool, indexed contract |
| Launch Lab | Graduated | ❌ No | Multiple pools possible |
| Radium | Any | ❌ No | Direct pool routing |
| Orca | Any | ❌ No | Direct pool routing |
| Meteora | Any | ❌ No | Direct pool routing |

### Client Communication: Setting Expectations
**Key Messages for Sain**:
1. **Echo Integration is Possible** - But only for Kitchen tokens (Pump.fun, Launch Lab)
2. **Echo Cannot Replace Jupiter** - Architectural incompatibility for established tokens
3. **This is an Echo Limitation** - Not a Cooking implementation issue
4. **Timeline for Broader Support** - Requires either:
   - Echo adding "main contract" routing option, OR
   - Cooking building comprehensive pool indexer (months of work, high cost)
5. **Recommended Path Forward** - Use Echo for Kitchen, Jupiter for everything else

**Business Impact Framing**:
- Kitchen tokens = ~30% of trading volume
- Echo provides marginal speed improvement (500ms vs 600ms)
- Jupiter provides comprehensive coverage, reliability
- Trade-off: Slightly faster for 30% of trades vs complete data for 100% of trades

### Technical Debt & Future Considerations
**If Full Pool Indexing Required**:
- Estimated effort: 3-4 months development
- Ongoing maintenance: 20% of indexer team time
- Infrastructure cost: +$2-3k/month (ClickHouse storage + compute)
- Operational complexity: High (new pools, protocol upgrades)

**Alternative: Wait for Echo Evolution**:
- If Echo adds trading pair specification
- If Echo adds "observable routing" mode
- If Echo partners with indexing providers
- Timeline: Unknown, no commitment from Echo team

**Alternative: Embrace Data Loss for Speed**:
- Accept that Echo trades won't appear in history
- Rely on wallet-level transaction history
- Sacrifice analytics completeness for execution speed
- **Team Verdict**: Unacceptable - undermines product value proposition

## Key Technical Decisions
- **Decision 1:** Do NOT integrate Echo for Radium or multi-pool tokens - Data loss unacceptable
- **Decision 2:** Limit Echo to Kitchen (Pump.fun + Launch Lab only) - Only safe integration scope
- **Decision 3:** Maintain Jupiter as primary router - Proven, compatible architecture
- **Decision 4:** Do NOT build comprehensive pool indexer now - Cost/benefit unfavorable
- **Decision 5:** Clearly communicate limitations to client - Transparency on technical constraints

## Architecture & Design Considerations
- **Indexer Philosophy**: Completeness over speed for data layer
- **Router Philosophy**: Reliability and observability over marginal speed gains
- **Product Philosophy**: User trust built on accurate data, not fastest execution
- **Technical Debt**: Avoid taking on massive indexer expansion without clear ROI

## Action Items
- [ ] **Lucas**: Draft comprehensive explanation email for Sain covering all limitations
- [ ] **Martin**: Test Pump.fun and Launch Lab transactions thoroughly with Echo
- [ ] **Eduardo**: Document current indexer coverage and contracts monitored
- [ ] **Lucas**: Prepare timeline and cost estimate for full pool indexing (for reference)
- [ ] **Team**: Create decision matrix document for future protocol integration evaluations

## Follow-up Items
- Monitor Echo roadmap for architectural changes
- Evaluate alternative routing providers (if they emerge)
- Re-assess pool indexing if trading volume distribution shifts significantly
- Plan quarterly review of indexer coverage vs market needs

## Technical References
- Radium CPMM Documentation: https://docs.raydium.io/raydium/protocol/concentrated-liquidity
- Jupiter Aggregator Architecture: https://station.jup.ag/docs/apis/swap-api
- Solana CPI Logs: https://docs.solana.com/developing/programming-model/calling-between-programs

---
**Recording:** Transcription available
**Related Documents:**
- Echo Integration Final Scope Document (04-knowledge-base/business/requirements/)
- Indexer Coverage Analysis (04-knowledge-base/technical/)
- Router Evaluation Matrix (04-knowledge-base/technical/)
