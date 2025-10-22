---
title: Echo Integration 2 - 2025-10-11
type: meeting
meeting_type: technical_deep_dive
topic: Echo
date: 2025-10-11
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Echo Integration Session 2 - Architecture Deep Dive - Cooking.gg
**Date:** October 11, 2025, 09:18 GMT-03:00
**Duration:** ~15 minutes (continuation session)
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk

## Executive Summary
Follow-up session diving deeper into Echo's API capabilities, testing specific protocol compatibility (Pump.fun, Launch Lab), and establishing limited integration scope. Team confirmed Echo can work for specific token categories but identified fundamental limitations preventing broader use.

## Meeting Context
Continuation of earlier Echo discussion, focusing on protocol-level testing to determine exact scope where Echo integration is viable without compromising Cooking's data integrity and user experience.

## Technical Discussion

### Protocol-Specific Testing Results
**Pump.fun Compatibility**:
- Tested transactions through Echo using Pump.fun tokens
- **Result**: All transactions route through F6P contract (main Pump.fun contract)
- **Conclusion**: Echo transactions **are visible** in Cooking's indexer
- **Status**: ✅ Compatible for integration

**Launch Lab Compatibility**:
- Tested transactions using Launch Lab tokens
- **Result**: Transactions route through 3UJ contract (Launch Lab's main contract)
- **Conclusion**: Echo transactions **are visible** in Cooking's indexer
- **Status**: ✅ Compatible for integration

**Radium AMM (Graduated Tokens)**:
- Echo routes directly to CPMM or CLMM pools
- Bypasses Radium AMM main contract (MP8)
- **Result**: Echo transactions **not visible** in Cooking's indexer
- **Status**: ❌ Not compatible without indexer expansion

### Confirmed Integration Scope
**Viable for Echo**:
1. Pump.fun tokens (in bonding curve or graduated)
2. Launch Lab tokens (in bonding curve or graduated)

**Not Viable for Echo**:
1. Radium AMM tokens (established tokens with multiple pools)
2. Orca pools
3. Meteora pools
4. Any multi-hop routes

**Technical Justification**:
- Pump.fun and Launch Lab use single main contract
- All transactions flow through contract Cooking already indexes
- No data loss risk for these specific protocols

### USD1 Quote Asset Problem
**Issue Identified**:
- Echo selects "best" liquidity pool
- For some Launch Lab and Radium tokens, best pool uses USD1 as quote asset
- Cooking users hold SOL, not USD1
- Transaction fails if user lacks USD1 balance

**Example Scenario**:
```
User wants to buy TOKEN_X
Echo finds best price in USD1/TOKEN_X pool
Generates transaction requiring USD1
User only has SOL
Transaction fails with "Insufficient balance" error
```

**Workarounds Evaluated**:
1. **Pre-check quote asset**: Call Echo's `/generate` endpoint first to see what asset needed
   - **Problem**: Adds latency (~500-1000ms), defeats Echo's speed advantage
2. **Specify exact pool address**: Force SOL-based pool
   - **Problem**: Echo becomes just a transaction builder, not a router (defeats purpose)
3. **Support multiple quote assets**: Allow users to hold SOL, USDC, USD1
   - **Problem**: Fragments liquidity, complicates UX, requires currency conversion flows

**Team Decision**: Accept limitation, use Echo only for tokens with SOL-based pools

### Client Communication Strategy
**What to Communicate to Sain**:
1. Echo integration is possible but with significant limitations
2. Viable only for Pump.fun and Launch Lab tokens in Kitchen
3. Cannot replace Jupiter as primary router for established tokens
4. Quote asset mismatch (USD1) causes failures for subset of tokens
5. Requires ongoing development from Echo team to support trading pair specification

**Proposed Phased Approach**:
- **Phase 1**: Integrate Echo for Kitchen (Pump.fun, Launch Lab) with SOL-based pools
- **Phase 2**: Expand to other protocols as Echo adds features and Cooking expands indexer
- **Phase 3**: Make Echo primary if/when architectural gaps resolved

### Echo Developer Engagement
**Questions Posed to Echo Dev (Yumen)**:
1. Can you add endpoint to query best pool without generating transaction?
2. Can you support specifying desired quote asset (e.g., force SOL pairs)?
3. What's your roadmap for multi-hop swap support?
4. Can you provide advance notice of contract/API changes?

**Developer Response** (from transcripts):
- Will **not** add trading pair specification to API (99% sure)
- Focused on speed optimizations, not feature expansion
- Multi-hop swaps "maybe" in future, no timeline
- Can add quote asset info to `/generate` response

## Key Technical Decisions
- **Decision 1:** Limit Echo integration to Pump.fun and Launch Lab in Kitchen - Only scope where architecture aligns
- **Decision 2:** Do not use Echo for tokens with USD1 pools - Prevents user-facing transaction failures
- **Decision 3:** Maintain Jupiter as primary router - Proven, reliable, comprehensive
- **Decision 4:** Position Echo as "optional speedup" not "replacement" - Manages expectations
- **Decision 5:** Document all limitations for stakeholders - Transparency on trade-offs

## Action Items
- [ ] **Lucas**: Draft detailed email to Sain explaining limitations and proposed scope
- [ ] **Martin**: Implement Echo integration for Kitchen (Pump.fun + Launch Lab only)
- [ ] **Eduardo**: Add detection logic for USD1 pools to avoid Echo routing
- [ ] **Team**: Create fallback flow: Echo -> Jupiter if Echo fails
- [ ] **Lucas**: Set up recurring check-in with Echo dev for feature updates

## Follow-up Items
- Monitor Echo usage metrics if integrated (success rate, latency, user feedback)
- Re-evaluate Echo scope if they add trading pair specification
- Plan indexer expansion if demand for Radium CPMM/CLMM coverage increases

## Technical References
- Pump.fun Contract (F6P): [Solana Explorer Link]
- Launch Lab Contract (3UJ): [Solana Explorer Link]
- Echo API Documentation: [Link from team communications]

---
**Recording:** Transcription available
**Related Documents:**
- Echo Integration Limitations Doc (04-knowledge-base/technical/)
- Client Communication: Echo Scope (to be drafted)
