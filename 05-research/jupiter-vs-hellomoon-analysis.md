---
title: HelloMoon vs Jupiter - Comparative Analysis
type: research
status: completed
priority: high
created: 2025-05-14
updated: 2025-10-20
date: 2025-10-20
tags: [research, routing, jupiter, hellomoon, performance, integration]
related:
  - "[[coin-trading-research]]"
  - "[[platform-vision-requirements]]"
decision: Recommend Jupiter for routing solution
---

# HelloMoon vs Jupiter - Comparative Analysis

## Executive Summary

The primary goal of this analysis is to determine the most suitable long-term routing solution for the Cooking trading platform—one that prioritizes **speed**, **stability**, and **scalability**.

**Recommendation**: Transition to direct Jupiter integration for superior performance and broader protocol support.

## Current State

At present, we are in the process of integrating HelloMoon's routing solution, which is positioned as a protocol-agnostic service supported by a dedicated node. In theory, this should offer faster execution and simplified integration with multiple protocols.

## Identified Limitations

However, in practice, we've encountered some limitations:

### Protocol Support Delays

- When **pump.fun** launched **pump.swap**, the integration was not immediately supported
- Similar issue occurred during the migration from **Moonshot** to **Moonit**, where support was also delayed

These cases highlight potential challenges in relying on a solution that may not be as responsive to fast-moving changes in the ecosystem—something that is crucial for maintaining a high-quality user experience.

## Performance Comparison

### Speed of Execution

To evaluate performance, we executed market orders for the following pairs:

**Test Pairs**:
- **STARBUTTS/SOL** – pump.fun (DcmLeCeH1yDDjLVfRC72XVr2YFFyNjvbBrRMFF5ppump)
- **USDC/SOL** - Solana native token (EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v)

### Results

#### HelloMoon Performance
- **Transaction Time**: 1074 ms
- **Price Fetching Time**: 655 ms
- _Tested under Production settings and credentials to reflect optimal conditions_

#### Jupiter API Performance
- **Transaction Time**: 335 ms — **3.2× faster (68.8% improvement)**
- **Price Fetching Time**: 309 ms — **2.1× faster (52.8% improvement)**
- _Tested using the free-tier credentials provided upon login. Paid-tier credentials likely offer even better performance_

## Protocol Support Comparison

### HelloMoon Supported Protocols (8)
1. PumpFun
2. Pump Swap AMM
3. Raydium V4
4. Moonshot / MoonIt (except flatcurve)
5. Raydium CLMM
6. Raydium CPMM
7. Meteora DLMM

### Jupiter API Supported Protocols (57+)
1. 1DEX
2. Aldrin
3. Aldrin V2
4. Bonkswap
5. Boop.fun
6. Crema
7. Cropper
8. Daos.fun
9. DexLab
10. Dynamic Bonding Curve
11. FluxBeam
12. GooseFX GAMMA
13. Guacswap
14. Helium Network
15. Invariant
16. Lifinity V2
17. Mercurial
18. Meteora
19. Meteora DAMM v2
20. Meteora DLMM
21. Moonit
22. Oasis
23. Obric V2
24. OpenBook V2
25. Orca V1
26. Orca V2
27. Penguin
28. Perena
29. Perps
30. Phoenix
31. Pump.fun
32. Pump.fun Amm
33. Raydium
34. Raydium CLMM
35. Raydium CP
36. Raydium Launchlab
37. Saber
38. Saber (Decimals)
39. Sanctum
40. Sanctum Infinity
41. Saros
42. Solayer
43. SolFi
44. Stabble Stable Swap
45. Stabble Weighted Swap
46. StepN
47. Token Mill
48. Token Swap
49. Virtuals
50. Whirlpool
51. Woofi
52. ZeroFi

## Ecosystem Engagement

Jupiter's team has shown strong engagement with development teams across the Solana ecosystem, positioning them as a leading partner for integrations and ongoing support.

## Recommendation Rationale

### Performance Advantages
- **3.2× faster transaction execution**
- **2.1× faster price fetching**
- Significant user experience improvement

### Protocol Coverage
- **7× more protocols supported** (57 vs 8)
- Faster adoption of new protocols
- Better long-term flexibility

### Integration Logic
- Given our intention to offer access to Jupiter-listed tokens
- Direct integration with their swap solution is more logical and efficient
- More efficient than using HelloMoon's wrapped implementation of the Jupiter API

### Ecosystem Position
- Jupiter is the leading DEX aggregator on Solana
- Strong community support
- Active development and rapid protocol adoption
- Established partnership network

## Migration Considerations

### Investment Recognition
We recognize that there has been an initial investment in integrating HelloMoon's swap API.

### Long-term Benefits
We believe that transitioning to a direct Jupiter integration will ultimately deliver a superior trading experience for our users.

### Strategic Recommendation
We strongly encourage consideration of this approach as part of our continued focus on product quality and user satisfaction.

## Conclusion

Based on our testing, Jupiter has consistently demonstrated:
- **Fastest performance** in transaction execution
- **Broadest protocol coverage** in the Solana ecosystem
- **Best ecosystem engagement** and support

The performance improvements and protocol coverage justify the migration effort, especially considering the long-term benefits for user experience and platform capabilities.

---

**Status**: Analysis complete
**Decision**: Recommend Jupiter integration
**Next Steps**:
1. Estimate migration effort
2. Plan migration timeline
3. Design backward compatibility strategy
4. Implement Jupiter integration
5. Deprecate HelloMoon integration
