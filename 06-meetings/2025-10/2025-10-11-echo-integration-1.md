---
title: Echo Integration 1 - 2025-10-11
type: meeting
meeting_type: technical_deep_dive
topic: Echo
date: 2025-10-11
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Echo Integration Session 1 - Technical Discussion - Cooking.gg
**Date:** October 11, 2025, 09:06 GMT-03:00
**Duration:** ~12 minutes (short session)
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk

## Executive Summary
Initial Echo integration session addressing transaction generation speed, API limitations, and architectural compatibility concerns. Team identified critical gaps in Echo's routing capabilities that impact Cooking's multi-protocol architecture.

## Meeting Context
Following client (Sain) request to integrate Echo as primary transaction router for faster execution speeds, team began technical evaluation. This session uncovered fundamental architectural mismatches between Echo's design and Cooking's requirements.

## Technical Discussion

### Echo Transaction Performance
**Promised Performance**: Sub-100ms transaction generation
**Actual Performance in Testing**:
- Established tokens (multiple liquidity pools): ~1800ms
- New tokens (single liquidity pool): ~500-700ms
- Failure rate: ~60% in proof-of-concept testing

**Comparison to Jupiter**:
- Jupiter: 400-600ms consistently
- Jupiter failure rate: < 5%
- Echo theoretical best case equals Jupiter average case

### Echo Architecture Limitations
**Critical Limitation**: No multi-hop swap support
- Echo routes directly to single liquidity pool
- Cannot optimize across multiple AMMs
- User must specify exact pool or token

**Impact on Cooking**:
- Cooking's router selects best price across all DEXs
- Echo bypasses this optimization
- Results in potentially worse prices for users

**Trading Pair Restriction**:
- Echo doesn't support specifying quote asset
- Auto-selects "best" pool which may be USD1, USDC, or SOL
- Cooking supports SOL-only trading pairs
- Mismatch causes transaction failures if user lacks required quote asset

### Technical Integration Challenges
**Indexing Problem**:
- Echo goes directly to liquidity pools
- Cooking indexes main DEX contracts (Radium AMM, Pump.fun, etc.)
- Echo transactions bypass indexed contracts
- Result: Trades executed via Echo not visible in Cooking's trade history

**Data Loss Risk**:
- Missing trade records breaks portfolio tracking
- Inaccurate P&L calculations
- Incomplete transaction history

**Solution Complexity**:
- Would require indexing every individual liquidity pool
- Exponentially increases indexer scope
- Constant maintenance as new pools created

## Key Technical Decisions
- **Decision 1:** Limit Echo to specific use cases only - Cannot be primary router due to architectural mismatches
- **Decision 2:** Kitchen tokens (bonding curve < 100%) as potential Echo scope - Single liquidity pool limitation aligns with Echo's design
- **Decision 3:** Continue with Jupiter as primary router - Proven performance, comprehensive features, compatible with architecture

## Action Items
- [ ] **Team**: Communicate limitations to client (Sain)
- [ ] **Martin**: Continue parallel Echo testing for kitchen tokens
- [ ] **Lucas**: Document Echo vs Jupiter trade-offs for stakeholders

## Follow-up Items
- Determine if Echo integration worthwhile for limited scope
- Evaluate client's flexibility on routing requirements
- Plan communication strategy for managing expectations

---
**Recording:** Transcription available
**Related Documents:**
- Echo Integration Analysis (04-knowledge-base/technical/)
- Router Comparison Matrix (to be created)
