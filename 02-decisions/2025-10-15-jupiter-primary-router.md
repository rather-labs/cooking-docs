---
title: Jupiter as Primary Router (Rejecting Echo)
type: decision-record
decision-id: ADR-100
date: 2025-10-15
status: accepted
owner: Lucas Cufré, Martin Aranda
stakeholders: [Lucas Cufré, Martin Aranda, Eduardo Yuschuk, Julian Martinez, Marcos Tacca, Sain (Client), Zen (Client)]
tags: [technical, routing, jupiter, echo, performance, architecture, client-management]
summary: |
  Decision to maintain Jupiter as the primary transaction router for Cooking.gg and reject Echo integration for beta launch despite strong client advocacy. After extensive testing, Echo demonstrated architectural incompatibility, unreliable performance (60% failure rate), and fundamental indexing conflicts. Jupiter provides proven reliability, better actual performance, and alignment with platform architecture.
related-docs:
  - ../06-meetings/2025-10/2025-10-15-indexer-deep-dive.md
  - ../06-meetings/2025-10/2025-10-11-echo-integration-1.md
  - ../06-meetings/2025-10/2025-10-11-echo-integration-2.md
  - ../06-meetings/2025-10/2025-10-14-liquidity-pools.md
  - ../06-meetings/2025-10/2025-10-16-mobile-app-final-sync.md
---

# Jupiter as Primary Router (Rejecting Echo)

## Context and Problem Statement

Cooking.gg requires a reliable, fast transaction routing engine to execute token swaps on Solana. The client (Sain) strongly advocated for Echo integration based on promises of sub-100ms transaction speeds from their advisor Alan, who collaborates with the Echo development team. Echo claimed to offer significant competitive advantage over existing platforms like Photon and Bullx.

The engineering team was pressured to integrate Echo as the primary router despite having a proven, working Jupiter-based system that had recently been optimized to achieve 2-3 second transaction confirmations (improved from 5-6 seconds).

**Key tensions:**
- Client expectations vs. engineering assessment
- Promised performance vs. tested reality
- Speed optimization vs. platform reliability
- Client relationship management vs. technical integrity
- Beta launch timeline pressure (3 days to launch)
- 10 days already spent debugging Echo integration

## Decision

**Proceed with Jupiter as the primary transaction router and reject Echo integration for beta launch.**

If Echo integration is absolutely required by client, limit scope to Kitchen phase tokens only (Pump.fun and Launch Lab bonding curve tokens with single liquidity pools), where Echo's architectural limitations have minimal impact.

**Scope:**
- **Primary Router**: Jupiter for all standard trading
- **Backup Systems**: HelloMoon and native routing as fallback
- **Limited Echo Use** (if required): Kitchen tokens only (bonding curves < 100%)
- **Excluded from Echo**: Multi-pool tokens, complex transactions, all user-facing trading

**Rationale for Limited Echo Scope:**
- Kitchen tokens have single liquidity pools (matches Echo's architecture)
- Lower user impact if failures occur
- Can be indexed separately without breaking main indexer
- Provides compromise position with client while protecting product integrity

## Rationale

### Technical Testing Results

**Echo Performance Reality:**
```
Promised: < 100ms transaction generation
Actual Testing Results:
- Established tokens (multiple pools): ~1800ms
- New tokens (single pool): 500-700ms
- Success rate: ~40%
- Failure rate: ~60%
```

**Jupiter Performance (Current System):**
```
Transaction build time: 400-600ms consistently
Success rate: ~95%
Confirmation time: 2-3 seconds (improved from 5-6s)
Trade indexing: 100% coverage
Supports complex transactions: Yes
```

**Echo at best equals Jupiter's average performance, but with 60% failure rate.**

### Fundamental Architecture Incompatibility

**1. Indexing Conflict (Critical)**

Echo's architecture creates fundamental data loss:
- Echo routes directly to individual liquidity pools
- Cooking indexes main DEX contracts (Raydium AMM, Pump.fun, Jupiter aggregator)
- **Echo transactions bypass indexed contracts**
- **Result**: Trades executed via Echo invisible in trade history

**Impact of data loss:**
- Broken portfolio tracking
- Inaccurate profit/loss calculations
- Incomplete transaction history
- Undermines core platform value proposition

**Echo developer's response:** "Your indexer approach is wrong, needs to be more low-level"

**What this actually means:**
- Requires indexing every individual liquidity pool contract on Solana
- Exponentially increasing scope (thousands of pools, constantly growing)
- Team assessment: "To support Echo fully, we'd need to index the entire Solana universe"

**2. Multi-Hop Limitation**

- Echo only supports single-pool direct routing
- Cannot optimize across multiple AMMs/DEXs
- Cooking's value proposition: best price across all liquidity sources
- Echo bypasses this optimization, potentially giving users worse prices

**3. Quote Asset Restriction**

Echo auto-selects "best" pool which may use any quote asset (SOL, USDC, USD1):
- User has SOL, wants to buy TOKEN_X
- Echo selects USD1/TOKEN_X pool (best liquidity)
- Generates transaction requiring USD1
- User lacks USD1 → transaction fails with "insufficient funds"
- No way to specify quote asset preference (Echo dev: "99% won't add this feature")

**4. Constant Instability**

- Echo constantly changing API and behavior
- Local environment works, deployed environment fails
- Integration maintenance burden unsustainable
- Lucas: "I cannot professionally recommend launching Echo in its current state"

### Client Relationship Context

**Why client insisted on Echo:**
- Client advisor (Alan) collaborates with Echo team
- Alan co-develops Echo Telegram bot
- Client shown controlled POC demos with "incredible or impossible" speeds
- Client believes Echo = competitive advantage
- Client rejects detailed technical emails without analysis

**Communication breakdown:**
- Engineering team sends detailed technical analysis
- Client responds with simple rejection, no engagement with details
- Julian: "He doesn't seem to analyze emails, just says no"
- Technical concerns dismissed as engineering incompetence

**Team morale impact:**
- Martin: "They're obsessed with Echo. We write them, they reject everything. I'm fed up."
- Lost 10 days debugging integration instead of testing/polishing for beta
- Timeline pressure: 1 week development + 1 week testing plan abandoned

### Product Philosophy Alignment

**Core value proposition of Cooking.gg:**
- Accurate, complete trading data
- Best price routing across all DEXs
- Comprehensive token discovery and market insights
- Social features based on complete on-chain data

**Echo's limited integration would:**
- Sacrifice data completeness for marginal (nonexistent) speed gains
- Break portfolio tracking and P&L accuracy
- Reduce platform to "just a transaction executor, not a trading platform"
- Lose token discovery, market insights, social features

**Team consensus:** Product integrity > client appeasement

### Recent Performance Improvements (Jupiter)

System already dramatically improved without Echo:
- Microservices refactor of trade logic
- Reduced Jupiter swap hops from 7 to 3
- Target "second best" price instead of perfect optimization (avoids conflicts with fee addition)
- **Result**: 2-3 second confirmations (down from 5-6 seconds)
- Proven reliability and stability

## Consequences

### Positive
- **Reliable user experience**: 95% success rate vs Echo's 40%
- **Complete data integrity**: All trades indexed and visible in history
- **Better actual performance**: Jupiter 400-600ms vs Echo 500-2000ms in reality
- **Product completeness**: Maintains token discovery, analytics, social features
- **Proven technology**: Jupiter handles ~80% of all Solana DEX volume
- **Team confidence**: Can professionally stand behind the technology
- **Maintainable architecture**: No exponential indexer expansion required
- **Multi-protocol support**: Can route through Raydium, Orca, etc. for best prices
- **Stable integration**: Not constantly breaking with API changes

### Negative
- **Client relationship strain**: Client strongly desired Echo integration
- **Perceived as unresponsive**: Client may view as team ignoring requirements
- **Lost client advisor influence**: Alan's Echo advocacy dismissed
- **Competitive anxiety**: Client fears being slower than Photon/Bullx (unfounded)
- **Communication breakdown**: Demonstrated gap in technical communication with client
- **Time investment lost**: 10 days spent investigating ultimately rejected technology

### Neutral
- Documentation trail established for future disputes
- Client education opportunity (if direct technical conversation happens)
- Validates need for better stakeholder technical communication processes
- Limited Echo integration still possible for Kitchen tokens if client insists

## Alternatives Considered

### Option 1: Echo as Primary Router (Client Preference)
**Description:** Integrate Echo as main transaction routing engine as client requested

**Pros:**
- Client satisfaction and relationship management
- Potential for sub-100ms speeds (if promises accurate)
- Competitive marketing angle

**Cons:**
- 60% failure rate in testing (unacceptable for production)
- Fundamental indexing incompatibility → data loss
- No multi-hop support → worse prices for users
- Quote asset restriction → user transaction failures
- Constant instability and API changes
- Worse actual performance than Jupiter in testing
- Breaks core product value proposition
- Requires exponential indexer architecture rewrite

**Why Rejected:** Technical testing demonstrated Echo is slower, less reliable, and architecturally incompatible. Cannot professionally recommend launching product that loses 60% of trade data and fails 60% of transactions.

### Option 2: Hybrid Jupiter + Echo System
**Description:** Jupiter for complex trades, Echo for simple single-pool swaps

**Pros:**
- Compromise between technical needs and client desires
- Could use Echo for specific use cases it handles well
- Demonstrates effort to accommodate client

**Cons:**
- Complex routing decision logic required
- Still faces indexing problems for Echo trades
- Users confused by inconsistent performance
- Maintenance burden of two systems
- Quote asset problem persists
- Minimal performance benefit in practice

**Why Rejected:** Adds complexity without solving fundamental problems. Testing showed Echo doesn't even excel in its supposed specialty (simple swaps).

### Option 3: "Track Only Our Transactions" Indexer
**Description:** Index only Cooking-initiated transactions instead of main DEX contracts

**Pros:**
- Guarantees coverage of user trades regardless of router
- Lower scope than indexing entire Solana
- Solves immediate Echo indexing conflict

**Cons:**
- Loses market data, prices, volume, liquidity for non-user trades
- Breaks token discovery feature
- Eliminates trending token detection
- Removes social features (see what other traders doing)
- Undermines platform differentiation
- Lucas: "Turns us into just a transaction executor, not a trading platform"

**Why Rejected:** Sacrifices core product value to accommodate flawed integration. Would need to rebuild product vision around limited capabilities.

### Option 4: Delay Beta Launch for Echo Development
**Description:** Push beta launch timeline to fully develop Echo integration

**Pros:**
- More time to solve Echo challenges
- Could achieve client requirement
- Reduces launch pressure

**Cons:**
- Already spent 10 days with no viable solution
- Fundamental architecture incompatibility likely unsolvable
- Delays user feedback and iteration
- Misses market timing
- Team morale impact (more time on failing integration)
- No guarantee Echo integration will ever be production-ready

**Why Rejected:** Echo's fundamental architectural mismatch cannot be solved with more time. Jupiter system is ready, proven, and superior in actual testing.

## Implementation Notes

### Current System Configuration
1. **Primary Router**: Jupiter aggregator
   - Transaction build time: 400-600ms
   - Swap optimization: Target second-best price (reduced from 7 to 3 hops)
   - Success rate: ~95%
   - Full indexing coverage

2. **Backup Systems**:
   - HelloMoon RPC (adds ~500ms latency but provides redundancy)
   - Native routing system
   - Automatic fallback on Jupiter failures

3. **Performance Optimizations**:
   - Microservices architecture for trade logic
   - Reduced transaction complexity
   - Optimized fee structure integration
   - Result: 2-3 second end-to-end confirmations

### If Limited Echo Integration Required
**Scope**: Kitchen phase tokens only (Pump.fun, Launch Lab bonding curves)

**Why Kitchen tokens work with Echo:**
- Single liquidity pool (matches Echo's architecture)
- No multi-hop optimization needed
- Can be indexed separately (Pump.fun contract indexing)
- Limited user impact if failures occur
- Bonding curve mechanics simpler than AMM trading

**Implementation approach:**
1. Separate Echo service for Kitchen tokens
2. Dedicated indexing for Pump.fun/Launch Lab contracts
3. Clear user communication about Kitchen vs. regular trading
4. Jupiter as fallback if Echo fails
5. Comprehensive monitoring and failure logging

### Client Communication Strategy
1. **Request direct technical meeting** (not email):
   - Minimum 30-minute deep dive
   - Demonstrate actual test results
   - Show current system improvements (2-3s confirmations)
   - Present Echo failure data and architecture conflicts
   - Explain indexing philosophy and trade-offs

2. **Document everything**:
   - Technical analysis emails
   - Test result data
   - Meeting notes and decisions
   - Lucas: "When this inevitably explodes, they can't say we didn't warn them"

3. **Establish technical veto process**:
   - Define boundaries for technical compromises
   - Create escalation path for architecturally unsound client requests
   - Protect engineering team from implementing known-bad solutions

## References

### Meeting Notes
- [Indexer Deep Dive 2025-10-15](../06-meetings/2025-10/2025-10-15-indexer-deep-dive.md) - Final decision meeting
- [Echo Integration Session 1 2025-10-11](../06-meetings/2025-10/2025-10-11-echo-integration-1.md) - Initial testing results
- [Echo Integration Session 2 2025-10-11](../06-meetings/2025-10/2025-10-11-echo-integration-2.md) - Technical deep dive
- [Liquidity Pools Discussion 2025-10-14](../06-meetings/2025-10/2025-10-14-liquidity-pools.md) - Indexing architecture
- [Mobile App Sync 2025-10-16](../06-meetings/2025-10/2025-10-16-mobile-app-final-sync.md) - Performance validation

### Technical Context
- Jupiter handles ~80% of Solana DEX volume
- Current system already optimized: 2-3s vs original 5-6s confirmations
- Echo developer: Yumen (via client advisor Alan)
- Testing environment: Both local and deployed AWS environments

### Client Context
- Client: Sain (based in Japan, timezone challenges)
- Client advisor: Alan (Echo advocate, co-develops Echo Telegram bot)
- Client expectation: Sub-100ms transactions for competitive advantage
- Reality: Echo's promised speeds unachievable in production

## Revision History
- 2025-10-11: Initial Echo testing and architecture analysis
- 2025-10-15: Final decision after extensive testing - Jupiter as primary router
- 2025-10-21: Formal ADR documented from meeting notes
