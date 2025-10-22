---
title: HelloMoon vs Jupiter Routing Solution - Comparative Analysis
type: technical-doc
date: 2025-05-14
last-updated: 2025-10-20
status: active
owner: Lucas Cufré
stakeholders: [Engineering Team, Product Team]
tags: [routing, jupiter, hellomoon, performance, dex, integration, solana]
summary: |
  Comprehensive performance and feature comparison between HelloMoon and Jupiter routing
  solutions for the Cooking trading platform. Testing shows Jupiter delivers 3.2x faster
  transaction times and significantly broader protocol support, recommending direct Jupiter
  integration over HelloMoon's wrapped implementation.
related-docs:
  - ../../business/requirements/trading-execution-requirements.md
source-file: C204 - HelloMoon vs Jupiter - Comparative analysis.md
---

# HelloMoon vs Jupiter Routing Solution - Comparative Analysis

## Overview

This analysis evaluates the most suitable long-term routing solution for the Cooking trading platform, prioritizing speed, stability, and scalability. The comparison focuses on HelloMoon (currently being integrated) versus Jupiter API as the primary routing provider.

## Executive Summary

**Recommendation:** Transition to direct Jupiter API integration.

**Key Findings:**
- **Speed:** Jupiter is 3.2x faster for transactions (335ms vs 1074ms)
- **Protocol Coverage:** Jupiter supports 60+ protocols vs HelloMoon's 7 protocols
- **Ecosystem Responsiveness:** Jupiter shows faster adoption of new protocols (pump.swap, Moonit)
- **Integration Efficiency:** Direct Jupiter integration is more logical than using HelloMoon's wrapped Jupiter implementation

## Background Context

We are currently integrating HelloMoon's routing solution, positioned as a protocol-agnostic service supported by a dedicated node. In theory, this should offer faster execution and simplified integration with multiple protocols.

However, practical limitations have emerged:
- When **pump.fun** launched **pump.swap**, HelloMoon integration was not immediately supported
- During the **Moonshot** to **Moonit** migration, support was delayed
- These delays impact user experience quality in a fast-moving ecosystem

## Performance Benchmarking

### Test Configuration

**Test Pair:**
- **STARBUTTS/SOL** – pump.fun (DcmLeCeH1yDDjLVfRC72XVr2YFFyNjvbBrRMFF5ppump)
- **USDC/SOL** – Solana native token (EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v)

**Test Methodology:**
- Market order execution on production-equivalent environment
- Multiple runs to ensure consistency
- Measurement of both transaction time and price fetching time

### Results Summary

| Metric | HelloMoon | Jupiter API | Jupiter Advantage |
|--------|-----------|-------------|-------------------|
| **Transaction Time** | 1074 ms | 335 ms | **3.2x faster** (68.8% improvement) |
| **Price Fetching Time** | 655 ms | 309 ms | **2.1x faster** (52.8% improvement) |
| **Test Environment** | Production credentials | Free-tier credentials | Jupiter likely faster on paid tier |

### Performance Analysis

**HelloMoon Performance:**
- Transaction Time: 1074ms
- Price Fetching: 655ms
- _Tested under Production settings with full credentials_

**Jupiter API Performance:**
- Transaction Time: 335ms — **3.2× faster (68.8% improvement)**
- Price Fetching: 309ms — **2.1× faster (52.8% improvement)**
- _Tested using free-tier credentials; paid tier likely offers superior performance_

**Key Insight:** Jupiter outperforms HelloMoon even when Jupiter is tested on free-tier credentials vs HelloMoon's production setup.

## Protocol Support Comparison

### HelloMoon Supported Protocols (7 total)

1. PumpFun
2. Pump Swap AMM
3. Raydium V4
4. Moonshot / MoonIt (except flatcurve)
5. Raydium CLMM
6. Raydium CPMM
7. Meteora DLMM

### Jupiter API Supported Protocols (60+ total)

**DEX Aggregators & AMMs:**
- 1DEX
- Aldrin, Aldrin V2
- Bonkswap
- Boop.fun
- Crema, Cropper
- Daos.fun
- DexLab
- FluxBeam
- GooseFX GAMMA
- Guacswap
- Invariant
- Lifinity V2
- Mercurial
- Oasis
- Orca V1, Orca V2
- Penguin
- Perena
- Phoenix
- Saber, Saber (Decimals)
- Saros
- SolFi
- StepN
- Token Mill, Token Swap
- Whirlpool
- Woofi
- ZeroFi

**Meteora Variants:**
- Meteora
- Meteora DAMM v2
- Meteora DLMM

**Raydium Variants:**
- Raydium
- Raydium CLMM
- Raydium CP
- Raydium Launchlab

**Specialized Protocols:**
- Dynamic Bonding Curve
- Helium Network
- Moonit
- Obric V2
- OpenBook V2
- Perps
- Pump.fun, Pump.fun Amm
- Sanctum, Sanctum Infinity
- Solayer
- Stabble Stable Swap
- Stabble Weighted Swap
- Virtuals

### Protocol Coverage Analysis

**Coverage Ratio:** Jupiter supports **8.6x more protocols** than HelloMoon (60+ vs 7)

**Strategic Implications:**
- Jupiter's broad coverage reduces integration complexity
- Single API endpoint vs managing multiple protocol-specific integrations
- Future-proofing against ecosystem evolution

## Ecosystem Integration & Responsiveness

### Jupiter Advantages

**Community Engagement:**
- Strong engagement with development teams across Solana ecosystem
- Positioned as a leading partner for integrations and ongoing support
- Rapid adoption of new protocols and features

**Developer Experience:**
- Well-documented API
- Active developer community
- Comprehensive SDKs and tools

### HelloMoon Limitations

**Protocol Lag:**
- Delayed support for pump.swap launch
- Delayed support for Moonshot → Moonit migration
- May not be responsive to fast-moving ecosystem changes

**Integration Approach:**
- HelloMoon wraps Jupiter API in many cases
- Adds additional latency layer
- Less direct control over routing logic

## Architecture Considerations

### Current State: HelloMoon Integration

**Investment Made:**
- Initial integration work completed
- Development time invested
- Testing infrastructure established

### Recommended State: Direct Jupiter Integration

**Rationale:**
1. **Remove Unnecessary Layer:** HelloMoon often wraps Jupiter API; direct integration is more efficient
2. **Performance:** 3.2x faster execution critical for memecoin trading where milliseconds matter
3. **Protocol Coverage:** Access to 60+ protocols vs 7
4. **Token Listing:** Since we intend to offer access to Jupiter-listed tokens, direct integration is logical
5. **Future-Proofing:** Jupiter's ecosystem position ensures continued innovation

### Migration Path

**Transition Strategy:**
1. Complete current HelloMoon integration for baseline functionality
2. Implement Jupiter API integration in parallel
3. A/B test both providers with subset of users
4. Gradual migration based on performance metrics
5. Deprecate HelloMoon integration post-validation

**Estimated Migration Effort:**
- API Integration: 2-3 weeks
- Testing & Validation: 1-2 weeks
- Gradual Rollout: 2-3 weeks
- **Total:** 5-8 weeks

## Technical Integration Details

### Jupiter API Integration Points

**Core Endpoints:**
- `/quote` - Get swap quotes
- `/swap` - Execute swap transactions
- `/swap-instructions` - Get raw instructions for custom transactions
- `/tokens` - List supported tokens
- `/markets` - Get market data

**Key Features:**
- Automatic route optimization
- MEV protection
- Slippage configuration
- Priority fee management
- Partial fill support

### Performance Optimization Opportunities

With direct Jupiter integration:
1. **Caching:** Implement intelligent quote caching (30-60 second TTL)
2. **Batch Requests:** Group multiple quote requests
3. **WebSocket Feeds:** Real-time price updates for active pairs
4. **Paid Tier:** Upgrade to Jupiter's paid tier for guaranteed performance SLAs

## Risk Analysis

### Risks of Staying with HelloMoon

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Slower execution loses users to competitors | High | High | Switch to Jupiter |
| Protocol support lag limits token availability | Medium | High | Switch to Jupiter |
| Wrapped API adds latency | Medium | High | Switch to Jupiter |
| Limited ecosystem responsiveness | Medium | Medium | Switch to Jupiter |

### Risks of Switching to Jupiter

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Migration effort impacts other roadmap items | Medium | Low | Phased rollout |
| Sunk cost in HelloMoon integration | Low | High | Accept as learning cost |
| Jupiter API changes/deprecations | Low | Low | Standard API versioning |
| Vendor lock-in | Low | Medium | Maintain abstraction layer |

## Cost Analysis

### HelloMoon Costs
- **Development:** Already invested (sunk cost)
- **Operational:** Node infrastructure + API fees
- **Maintenance:** Ongoing protocol updates and monitoring

### Jupiter Costs
- **Development:** 5-8 weeks engineering time
- **Operational:** API fees (free tier → paid tier as needed)
- **Maintenance:** Lower due to better ecosystem support

### Cost-Benefit Analysis
- **Performance Gain:** 3.2x faster transactions = better user retention
- **Development Efficiency:** Broader protocol support = fewer custom integrations
- **Market Positioning:** Faster execution = competitive advantage in memecoin trading

## Conclusion

Based on comprehensive testing and analysis, **Jupiter has consistently demonstrated superior performance and broader protocol coverage**. Given our intention to offer access to Jupiter-listed tokens, a direct integration with their swap solution is more logical and efficient than using HelloMoon's wrapped implementation.

### Recommendation

**Transition to direct Jupiter API integration** to deliver a superior trading experience for our users, with focus on:
1. Product quality through faster execution
2. User satisfaction through broader token access
3. Long-term platform scalability

While we recognize the initial investment in HelloMoon's swap API, we believe that transitioning to a direct Jupiter integration will ultimately deliver better outcomes aligned with our product goals.

## Next Steps

1. **Immediate:** Present findings to stakeholders for approval
2. **Week 1-2:** Design Jupiter integration architecture
3. **Week 3-5:** Implement Jupiter API integration
4. **Week 6-7:** Parallel testing with HelloMoon
5. **Week 8+:** Gradual migration and HelloMoon deprecation

## Appendix

### Test Transaction IDs
- HelloMoon Test TX: [Transaction ID to be added]
- Jupiter Test TX: [Transaction ID to be added]

### Additional Resources
- [Jupiter API Documentation](https://station.jup.ag/docs)
- [HelloMoon API Documentation](https://docs.hellomoon.io)
- Internal testing scripts: `/testing/routing-benchmarks/`

### Glossary Terms
- **AMM (Automated Market Maker):** Protocol that uses liquidity pools for trading
- **MEV (Maximal Extractable Value):** Value that can be extracted by reordering transactions
- **Protocol-agnostic:** Works across multiple blockchain protocols
- **Slippage:** Difference between expected and executed trade price
- **Wrapped API:** API that calls another API internally

---

**Document Status:** Active
**Review Cycle:** Quarterly or upon significant Jupiter/HelloMoon updates
**Last Reviewed:** 2025-10-20
**Next Review:** 2026-01-20
