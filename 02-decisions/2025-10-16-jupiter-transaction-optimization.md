---
title: Jupiter Transaction Optimization Strategy
type: decision-record
decision-id: ADR-106
date: 2025-10-16
status: accepted
owner: Martin Aranda
stakeholders: [Lucas Cufré, Zen (Client), Backend Team, Eduardo Yuschuk]
tags: [technical, performance, jupiter, transaction-optimization, trading]
summary: |
  Decision to optimize Jupiter routing by targeting second-best price instead of perfect price
  and limiting transaction complexity (max 3 swaps/hops vs 7), improving transaction success
  rate and reducing confirmation time from 5-6 seconds to 2-3 seconds.
related-docs:
  - ../06-meetings/2025-10/2025-10-16-mobile-app-final-sync.md
  - 2025-10-15-jupiter-primary-router.md
  - 2025-09-26-microservices-by-algorithm.md
---

# ADR-106: Jupiter Transaction Optimization Strategy

## Context and Problem Statement

When integrating with Jupiter (Solana's primary aggregator for token swaps), the platform faced a critical tradeoff between transaction optimization and reliability:

**Original Jupiter Configuration:**
- Jupiter's default optimization aggressively searches for best possible price
- Can route through up to 7 different swaps/hops to achieve optimal price
- Complex multi-hop transactions have higher failure rates
- Sometimes conflicts with platform fee addition
- Transaction confirmation times: **5-6 seconds**

**User Experience Requirements:**
- Fast transaction confirmations (target: <3 seconds)
- High success rate (failed transactions frustrate users)
- Competitive pricing (but not at expense of reliability)
- Predictable execution

**Technical Challenge:**
Jupiter's aggressive optimization created conflicts when adding platform fees to transactions, causing some transactions to fail. The complexity of 7-hop routes also increased:
- Network congestion sensitivity
- Slippage likelihood
- Transaction failure rates
- Confirmation latency

**Problem Statement:**
How can we balance getting users competitive prices while ensuring fast, reliable transaction execution and compatibility with our fee structure?

## Decision

**Implement constrained Jupiter optimization targeting second-best price with maximum 3 swaps/hops**, combined with microservices refactoring of trade logic.

### Optimization Parameters

**Price Target:**
- **Previous:** Optimize for absolute best price (can cause conflicts and failures)
- **New:** Target second-best price from Jupiter's routing options
- Typically 0.1-0.3% worse than perfect price
- Significantly more reliable and faster

**Swap Complexity:**
- **Previous:** Allow up to 7 swaps/hops per transaction
- **New:** Limit to maximum 3 swaps/hops
- Reduces transaction complexity and failure points
- Improves confirmation speed

**Fee Integration:**
- Simplified routing resolves conflicts with platform fee addition
- Fees can be reliably added without breaking transaction construction
- No edge cases where fees cause transaction rejection

### Performance Improvements

**Transaction Confirmation Time:**
- **Before:** 5-6 seconds average
- **After:** 2-3 seconds average
- **Improvement:** ~50% reduction in confirmation time

**Success Rate Improvements:**
- Reduced multi-hop complexity → fewer points of failure
- Better compatibility with fee addition → fewer construction failures
- More predictable execution → fewer slippage rejections

**Achieved Through:**
1. Jupiter optimization constraints
2. Microservices refactoring of trade logic (see ADR-002)
3. Improved transaction construction pipeline

## Rationale

### Why Second-Best Price?

**Price vs Reliability Tradeoff:**
- Best price often requires complex routing through obscure liquidity pools
- Second-best price typically uses more established, liquid routes
- User impact: Paying 0.2% more vs experiencing 30%+ failure rate

**Example Scenario:**
- Best Price Route: SOL → obscure-pool → intermediate-token → target-token (4-5 hops)
- Second-Best Price Route: SOL → Raydium → target-token (1-2 hops)
- Price difference: 0.2% (~$0.20 on $100 trade)
- Reliability difference: 95% vs 70% success rate
- Speed difference: 2.5s vs 5.5s confirmation

**Business Justification:**
- Users value speed and reliability over marginal price improvements
- Failed transactions create support burden and user frustration
- Faster confirmations improve trading experience and competitiveness
- Predictable execution builds user confidence

### Why Maximum 3 Swaps/Hops?

**Complexity Analysis:**
- **1 hop:** Direct swap (SOL → USDC via Raydium)
  - Success rate: ~95%
  - Confirmation: 1.5-2s
- **2-3 hops:** Through one intermediate token
  - Success rate: ~85-90%
  - Confirmation: 2-3s
- **4-7 hops:** Through multiple intermediate tokens
  - Success rate: ~60-75%
  - Confirmation: 4-6s

**Sweet Spot:** 3 hops provides good price discovery while maintaining high reliability.

**Network Conditions Sensitivity:**
- Complex routes more affected by network congestion
- During high traffic, 7-hop routes often time out
- Simpler routes complete even under congestion

### Microservices Architecture Synergy

The trade logic microservices refactoring (ADR-002) enabled:
- Better separation of routing optimization from execution
- Independent scaling of routing service
- A/B testing different optimization strategies
- Faster deployment of routing improvements

Combined with Jupiter constraints, this architectural change contributed significantly to the 5-6s → 2-3s improvement.

## Consequences

### Positive Consequences

- **50% Faster Confirmations:** 5-6s → 2-3s average transaction time
- **Higher Success Rates:** Fewer multi-hop failures and construction errors
- **Better UX:** Faster, more predictable trading experience
- **Competitive Advantage:** 2-3s confirmations faster than most competitors
- **Reduced Support Burden:** Fewer failed transaction support tickets
- **Fee Integration Reliability:** No conflicts between optimization and platform fees
- **Scalability:** Simpler transactions handle network congestion better

### Negative Consequences

- **Slightly Worse Pricing:** 0.1-0.3% worse than theoretical best price
- **Missed Arbitrage Opportunities:** Some complex routes with better prices not accessible
- **Less Utilization of Long-Tail Liquidity:** Smaller pools not used as frequently
- **Potential User Complaints:** Sophisticated traders may notice non-optimal pricing

### Mitigation Strategies

**For Pricing Concerns:**
- Monitor actual price difference vs best price (typically <0.2%)
- Communicate speed/reliability benefits to users
- Offer "advanced mode" in future for users who want max optimization (at their own risk)

**For Sophisticated Traders:**
- Provide transaction details showing routing used
- Transparency about optimization strategy
- Option to use external aggregators if they prefer max optimization

### Neutral Consequences

- **Jupiter Relationship:** Still using Jupiter as primary router, just with different parameters
- **Future Flexibility:** Can adjust optimization parameters based on network conditions
- **Monitoring Required:** Need to track price difference vs theoretical best to ensure strategy remains valid

## Alternatives Considered

### Option 1: Keep Maximum Optimization (7 Hops)

**Description:** Continue allowing Jupiter's full optimization with up to 7 swaps.

**Pros:**
- Best possible prices for users
- Maximum utilization of available liquidity
- Competitive on price metrics

**Cons:**
- 5-6 second confirmations (too slow)
- Higher failure rates (poor UX)
- Conflicts with fee addition (technical issues)
- Poor performance during network congestion

**Rejected:** User experience and reliability more important than marginal price improvements.

### Option 2: Ultra-Conservative (1-2 Hops Max)

**Description:** Limit to only the simplest direct swaps.

**Pros:**
- Absolute maximum speed (~1.5s confirmations)
- Highest reliability (~95%+ success)
- Simplest to implement and maintain

**Cons:**
- Significantly worse pricing for many token pairs
- Limited token coverage (not all pairs have direct routes)
- User complaints about pricing
- Competitive disadvantage on price

**Rejected:** Too conservative; 3 hops provides much better price discovery without significant reliability cost.

### Option 3: Dynamic Optimization Based on Conditions

**Description:** Adjust hop limit dynamically based on network congestion, token liquidity, trade size, etc.

**Pros:**
- Optimal balance for each specific trade
- Maximum optimization when network allows
- Simpler routes during congestion

**Cons:**
- Complex implementation and maintenance
- Unpredictable user experience (confirmations vary widely)
- Difficult to explain to users why times vary
- More edge cases and potential bugs
- May not resolve fee integration conflicts

**Rejected:** Complexity not justified for current needs; can revisit post-beta if data shows clear benefit.

### Option 4: Switch to Different Aggregator

**Description:** Use a different routing provider with better optimization parameters.

**Pros:**
- Potential for better default optimization
- Different provider strengths

**Cons:**
- Jupiter is industry leader with best liquidity access
- Migration cost and risk
- No guarantee other providers would be better
- Would still need to tune optimization parameters

**Rejected:** Problem is optimization strategy, not provider; Jupiter remains best choice (see ADR-100).

## Implementation Notes

### Configuration Changes

**Jupiter API Parameters:**
```javascript
{
  slippageBps: 50,  // 0.5% slippage tolerance
  onlyDirectRoutes: false,
  asLegacyTransaction: false,
  maxAccounts: 30,  // Reduced from 64 to limit complexity
  // Optimization constraints:
  maxSplitOnly: false,
  restrictIntermediateTokens: true,
  onlyTopRoutes: true  // Use only established routes
}
```

**Custom Route Filtering:**
- Filter Jupiter's route suggestions to maximum 3 hops
- Select second-best route by default
- Fallback to best route if second-best unavailable or >0.5% worse

### Performance Monitoring

**Metrics to Track:**
- Average confirmation time (target: 2-3s)
- Transaction success rate (target: >85%)
- Actual price vs theoretical best price (acceptable: <0.3% difference)
- User complaints about pricing vs speed
- Fee integration failure rate (target: <1%)

**Alerts:**
- Critical: Confirmation time >4s for >10% of transactions
- Warning: Price difference >0.5% from theoretical best
- Warning: Success rate <80%
- Info: Network congestion affecting routing

### A/B Testing Results (Pre-Decision)

**Test Period:** October 10-14, 2025
**Sample Size:** ~500 transactions

| Metric | 7-Hop Max | 3-Hop Max | Improvement |
|--------|-----------|-----------|-------------|
| Avg Confirmation Time | 5.2s | 2.7s | **48% faster** |
| Success Rate | 72% | 89% | **+17 points** |
| Avg Price Difference from Best | 0% | 0.18% | -0.18% |
| User Satisfaction | 3.2/5 | 4.1/5 | **+28%** |

Results clearly validated the 3-hop approach.

## References

### Related Meetings
- [2025-10-16 Mobile App Final Sync](../06-meetings/2025-10/2025-10-16-mobile-app-final-sync.md) - Performance improvements discussion

### Related ADRs
- [ADR-100: Jupiter as Primary Router](2025-10-15-jupiter-primary-router.md) - Routing provider decision
- [ADR-002: Microservices Architecture by Trading Algorithm](2025-09-26-microservices-by-algorithm.md) - Architectural changes that enabled optimization

### Technical References
- Jupiter API documentation
- Solana transaction optimization best practices
- Platform performance benchmarks

---

**Status:** Accepted and Implemented
**Implementation Date:** October 16, 2025
**Owner:** Martin Aranda (Backend Team)
**Review Date:** Post-beta launch (analyze actual vs expected performance)
