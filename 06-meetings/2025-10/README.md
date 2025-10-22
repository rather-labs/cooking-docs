---
title: October 2025 - Daily Standup Meetings
type: index
date: 2025-10-21
summary: Index of Cooking.gg daily standups from October 2025, documenting the closed beta launch preparation and execution.
---

# October 2025 - Daily Standup Meetings

This directory contains structured meeting notes from Cooking.gg daily standups during October 2025.

## Overview

**Period Covered:** October 1-17, 2025 (8 meetings)
**Meeting Type:** Daily Standup
**Team:** Cooking.gg Development Team
**Language:** English (translated from Spanish)
**Critical Milestone:** Closed beta launch preparation and execution

## Files

- `2025-10-01-daily-standup.md` - Launch delayed 2 weeks for Eco integration, Solana byte limit crisis
- `2025-10-03-daily-standup.md` - Client demo prep, position updates resolved, code freeze discussion
- `2025-10-06-daily-standup.md` - Holiday work, ClickHouse crisis resolution via projection optimization
- `2025-10-08-daily-standup.md` - ClickHouse merge saturation, pixel-perfect design feedback
- `2025-10-10-daily-standup.md` - Type-safe API clients, production deployment preparation
- `2025-10-13-daily-standup.md` - Open beta strategy, Jupiter integration problems, Eco challenges
- `2025-10-15-daily-standup.md` - Internal delivery target, ClickHouse optimization, DNS deployment
- `2025-10-17-daily-standup.md` - **LAUNCH DAY** - Closed beta announced, 3-second transactions achieved

## Major Milestones by Week

### Week 1 (Oct 1-6): Launch Delay and Crisis Management

**Launch Extension Decision (Oct 1)**
- Original: Friday (that week)
- New Target: October 15 (~2 weeks)
- Reason: Eco router integration strategic opportunity
- Client: Communicated and accepted

**Solana Byte Limit Crisis (Oct 1)**
- 50% transaction failure rate
- Root cause: Jupiter transaction + Cooking fees + referral transfers exceeded limit
- Temporary fix: Removed fee transfers to make transactions work
- Impact: Not collecting Cooking fees or referral commissions
- Long-term solution: Separate linked transaction for fee collection

**ClickHouse Crisis and Resolution (Oct 6)**
- Problem: Merge processes saturating instances, 1,000+ queries stuck
- Solution: Darío created new projection optimizing queries
- Result: 10x reduction in rows read, dramatically faster portfolio/holders queries
- Configuration: Two ClickHouse clients (API higher priority, cron jobs lower)

### Week 2 (Oct 8-13): Refinement and Architecture Debates

**Pixel Perfect Design Review (Oct 8)**
- US design agency conducting intensive late-stage review
- Safari officially in scope (previously Chrome-only assumption)
- Task division: Javier on functionality, Santiago on design QA
- Image issues: Re-exported all to PNG for Safari compatibility

**Type-Safe API Client Generation (Oct 10)**
- Trigger: Production bug from backend change breaking frontend
- Solution: Auto-generated typed clients for all services
- Impact: Compile-time type checking instead of runtime failures

**Fundamental Jupiter Integration Problem (Oct 13)**
- Current: Showing arbitrage prices from divergent sources
- Issue: "Zero predictability" - users can't anticipate actual execution price
- Proposed: Provider-discriminated pricing (like DexScreener, Jupiter frontend)
- Impact: Requires major indexer and architecture restructuring

### Week 3 (Oct 15-17): Launch Execution

**Internal Delivery Target (Oct 15 - Wednesday)**
- Official deadline: Friday
- Internal goal: Wednesday to avoid weekend on-call
- ClickHouse optimization: 5x memory reduction (16M → 6M rows), 2x speed improvement
- Transaction microservice: Deployed after DNS resolution

**Launch Day Success (Oct 17 - Friday)**
- **Transaction Breakthrough**: Stable 3-second completion (down from 5-6 seconds)
- **Client Demo**: Showed transaction logs proving performance, client impressed
- **Monday Launch**: 5 client internal users begin testing
- **October 27**: Closed beta with 30-40 whitelist users (if no critical issues)
- **Eco Decision**: Not launching with Eco due to architectural incompatibility

## Key Technical Achievements

### Transaction Performance
- **Before**: 5-6 second completion, unreliable confirmations
- **After**: Stable 3 seconds, working confirmation notifications
- **Evidence**: Inspector logs showing 3-second completion times
- **Client Impact**: Satisfied client, stopped demanding Eco integration

### ClickHouse Optimization
- **Query Template**: 5x reduction in rows read (16M → 6M)
- **Speed**: 2x average performance improvement
- **Memory**: Significant reduction in resource consumption
- **Architecture**: Two-client setup (API priority vs cron jobs)
- **Recovery**: Backup restore after merge crisis, better long-term scaling

### Transaction Microservice
- **Lines of Code**: 6,000+ comprehensive architecture
- **Event-Driven**: RabbitMQ for asynchronous processing
- **Horizontal Scaling**: Handles high transaction volumes
- **Retry Logic**: Automatic reconstruction on failure
- **Fee Integration**: Multi-referral system integrated

### Infrastructure Improvements
- **Type Safety**: Auto-generated API clients prevent runtime errors
- **DNS Resolution**: Unblocked microservice deployment
- **Autoscaling**: Configured for production deployment
- **Monitoring**: Enhanced observability for transaction flows

## Critical Issues Overcome

### Solana Byte Limit
- **Problem**: 50% failure rate from transaction size
- **Temporary**: Disabled fee collection to make transactions work
- **Solution**: Martin implemented loop reducing swap complexity iteratively
- **Mechanism**: Reduces max hops until transaction fits byte limit

### ClickHouse Merge Crisis
- **Symptoms**: Instances saturated, 1,000+ queries pending, complete lockup
- **Root Cause**: Partitioned materialized views causing excessive merges
- **Resolution**: Dropped partitioned views, recreated with optimized projection
- **Prevention**: Careful partition strategy, query structure monitoring

### Refresh Token Cookie Bug
- **Issue**: Cookie not setting on login, appearing only after expiration
- **Browsers**: Both Chrome and Safari affected
- **Solution**: Switched from Axios to Fetch for specific endpoint
- **Root Cause**: Axios credential handling problem

### Transaction Confirmation Polling
- **Problem**: Notifications never appearing despite backend resolving quickly
- **Impact**: Client demo preparation urgency (11 AM meeting)
- **Resolution**: Fixed frontend batching issue
- **Result**: Confirmations working correctly by launch

## Architecture Challenges

### Jupiter Integration Fundamental Issues
- **Current**: Aggregated arbitrage prices from unknown sources
- **Visibility**: No provider discrimination, opaque execution routes
- **Predictability**: "Zero predictability" vs other platforms
- **Competitive Gap**: All competitors show provider-discriminated pricing
- **Proposed**: Discriminate by provider, index major AMM pools
- **Decision**: Client must accept trader-focused paradigm or commit to restructuring

### Eco Router Incompatibility
- **Problem**: Architectural incompatibility between Cooking and Eco
- **Specific**: Eco requires liquidity pool address (defeats router purpose)
- **Latency**: 500ms Jupiter vs 620ms Eco when address provided (virtually same)
- **Partial Opportunity**: Kitchen first two columns (known single AMM)
- **Development State**: "Less than alpha," Cooking is Eco's guinea pig
- **Decision**: Not launching with Eco, architectural reconciliation requires both teams

### Price Filtering Strategy
- **Short-term**: Filter arbitrage, focus high-liquidity individual swaps
- **Medium-term**: Discriminate by provider using Jupiter API
- **Long-term**: Index major AMM pools (competitive necessity per Eduardo)
- **Trade-off**: Transparency vs development time vs competitive positioning

## Team Dynamics and Recognition

### Holiday Work Ethic
Multiple standups occurred on Argentine national holidays:
- October 6 (Monday holiday)
- October 10 (Holiday)
- Team worked weekends leading to launch

**Martin's Recognition (Oct 17)**: "I want to thank you all for all the effort you're putting in. I know today is a holiday and you're all working. I know tomorrow is Saturday and you're going to work it and I'm very grateful with you all that you're holding on so we can deliver and come out on time."

**Lucas's Response**: "Completely agree. I promise we'll make it more comfortable, calmer from here on. I believe it's public knowledge the titanic work we've put in these last months. It's a Pareto of s***. The last 20% costs a barbaric amount."

### Crypto Trading Sympathy
Running joke throughout October about team members losing money trading:
- Luis lost on Hyper Liquid Bitcoin longs ("understood market perfectly for 3 seconds")
- Lucas lost hundreds on Bitcoin/Ethereum shorts
- Consensus: "Trading perpetuals closest to casino gambling"

### Task Stealing Humor
- Martin Lecam "almost got stabbed" by Luis for stealing ticket
- Team coordination on who takes which bugs and features
- Collaborative atmosphere despite pressure

## Launch Strategy

### Closed Beta Parameters
- **Not Friends and Family**: Open beta via referral codes
- **Access**: cooking.com/login requires referral code
- **Viral Mechanism**: Referred users generate own codes
- **User Range**: 30-40 initial whitelist users
- **Internal First**: 5 client team members (Sain, Ris, Greg, Nashi, +1)
- **Gate**: No catastrophic issues during internal week → beta Oct 27

### Client Personas
- **Sain**: Pays bills, highest business authority
- **Ris**: Product vision, external design agency coordination
- **Greg**: Trader with finance background
- **Nashi**: Marketing, growth strategy
- **External Agency**: "Pixel perfect" design review

### Post-Launch Plan (Q4)
- Feedback iteration, feature additions, improvements
- Architecture hardening for scalability
- Indexer enhancements (contracts, price series separation)
- Preparation for full marketing campaign

## Recurring Blockers

### ClickHouse Optimization
- Persistent theme: balancing performance vs resource consumption
- Knowledge centralization in Eduardo (risk)
- Large data volumes requiring dedicated optimization
- "Keep throwing money at problem" until optimized

### Transaction Fee Collection
- Temporarily disabled due to byte limit
- Blocking revenue generation
- Needs architectural solution (linked transactions)
- Critical for business model

### Eco Integration Complexity
- Client pushing hard despite architectural incompatibility
- Requires development on both sides
- Latency not meaningfully better when tested properly
- Team demonstrated alternative met requirements

### DNS Management
- Client in Japan (12-hour time difference)
- Blocking microservice deployment for testing
- Required screen-share workshop for resolution
- Eventually resolved, unblocking progress

## Action Items Carried to Q4

### Architecture
- [ ] Begin systematic architecture hardening
- [ ] Evaluate provider-discriminated pricing with client
- [ ] Plan long-term pool indexing strategy (Orca, Meteora)
- [ ] Define target trader profile (knowledgeable vs "everyone")

### Indexer
- [ ] Dedicated ClickHouse optimization time allocation
- [ ] Decentralize indexer knowledge beyond Eduardo
- [ ] Index major AMM pools for competitive parity
- [ ] Complete Radium and Meteora contract integration

### Transactions
- [ ] Implement linked transaction for fee collection
- [ ] Resolve Solana byte limit architectural solution
- [ ] Enhance error mapping for user communication
- [ ] Pool liquidity validation before transaction submission

### Infrastructure
- [ ] Continue ClickHouse query optimization
- [ ] Implement password rotation for ClickHouse
- [ ] Monitor QuickNode request volume (70M/month)
- [ ] Production deployment of optimized components

## Meeting Attendance

**Regular Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

**New Member:** Marcos Tacca joined mid-October during critical pre-launch period

---

**Note:** These meetings were originally conducted in Spanish and have been translated to English while preserving technical terminology. October 2025 represents the culmination of months of intensive development work leading to the Cooking.gg closed beta launch.
