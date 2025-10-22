---
title: Daily Standup - 2025-10-08
type: meeting
meeting_type: daily_standup
date: 2025-10-08
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** October 8, 2025
**Duration:** 1:05:09
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

Critical ClickHouse crisis dominated the standup as merge processes saturated all three instances causing complete system unresponsiveness. Lucas received intensive "Pixel Perfect" feedback from US design agency requiring meticulous Safari and Chrome QA. Team reorganized priorities: Javier focuses on Advanced Orders functionality testing, Santiago on design QA. Luis completed carousel fix and Val Max requirement. Esteban finished transaction backend integration awaiting DNS resolution for deployment. Darío and Martin spent entire session debugging ClickHouse merge issues, ultimately dropping partitioned materialized views to stabilize system. Team worked through political humor given Argentina's unique holiday context.

## Team Updates

### Luis Rivera (Frontend Developer)
- **Carousel Solution**: Fixed to activate dynamically based on available screen space (not hardcoded to 4 positions)
- **Val Max Requirement**: Completed and ready for testing
- **Component Alignment**: Will review login div image alignment (looks good in Chrome/Safari after PNG conversion but needs positioning adjustment)
- **Status**: Ready to take additional tickets after carousel and Val Max completion

### German Derbes Catoni (Frontend Developer)
- Completed advanced orders details including scroll overflow fix
- Resolved toast notification positioning issues
- Working on criteria validation for selling without funds (will send criteria to Lucas for review)
- Investigating toast notification extended display time issue

### Marko Jauregui (Frontend Developer)
- Working on Referral flow fixes: model flows and internal transfers adjustments
- Next task: adjust referral UI to match design as closely as possible
- Ready to take assigned task from Javi and other pending tickets

### Federico Caffaro (Backend Developer)
- Implemented withdrawal fix: integrated endpoint to verify Hyper Liquid user role
- Added first-time wallet interaction USD fee ($1 for first-time Perpetuals users)
- Restructured multi-layer referral system entities to rebuild user referral tree
- Computer crashed while pulling changes, had to re-implement optimizations locally
- Can retroactively link dev Perpetuals accounts to Hyper Liquid referral code for testing

### Esteban Restrepo (Backend Developer)
- Completed backend transaction integration upload
- Needs frontend polling integration for synchronous transactions
- Repository push to registry failed (will review with Jesús)
- Still needs to combine legacy transactions GET with current transactions
- **Priority Work**: Timeframes by seconds, double transaction handling, auto-priority fee

### Eduardo Yuschuk (Indexer Developer)
- Advancing Eco integration work
- Discussed with Martin whether external security service makes sense
- Most external services are AML/terrorism financing focused (introduces significant latency)
- Proposed two security approaches:
  1. Static transaction analysis (signatures, wallets, program calls)
  2. Transaction simulation to see fund flows
- Working on price precision improvements across all protocols
- Wants to implement calculation using post-trade amounts instead of exchange price
- Identified Radium price issues

### Darío Balmaceda & Martin Aranda (Infrastructure - ClickHouse Crisis Management)
- **Crisis**: All three ClickHouse instances stuck with merge processes, 1,000+ queries pending per instance
- **Timeline**: Issue started 6:30 PM (one instance), 7:30 PM (three instances merging simultaneously)
- **Root Cause**: Partitioned materialized views causing excessive merge operations
- **Symptoms**: Queries getting stuck, reaching 1,000 query limit, complete unresponsiveness
- **Solution Attempts**:
  1. Disabled use_concurrency_control (didn't solve issue)
  2. Multiple restarts (temporary relief, issue returned within hour)
  3. Analyzed merge parts dashboard (32 merges running constantly)
- **Final Resolution**: Dropped partitioned materialized views, recreated standard holders MB
- **Outcome**: System stabilized, queries responding, merge counts reduced

### Byron Chavarria (Mobile Developer)
- Working on limit order creation at visual level
- Incorporating elements for bottom sheet display
- Pending account access for OTP and push notification testing
- Needs 5 minutes with working account for browser and Xcode testing
- Push notifications require physical device (can't test in simulator)
- Asked about on-ramp status (Lucas handling)

### Santiago Gimenez (Backend/Frontend Developer)
- Working on Refer and Bubble Maps features
- Started new filter design exploration
- Will shift to design QA focus per Lucas request (Chrome and Safari)

### Javier Grajales (QA/Testing)
- Tested holder categories (Sniper, Insider, Diamond Hands) - working well
- Missing examples for "De Bot" and "De Sold" categories
- Reviewed carousel and reported defect
- Found issue with token transfers between own wallets (two different errors reported to Martin)
- Pending Advanced Orders testing once microservices deployed to dev
- Awaiting scalability testing coordination with Federico

### Martin Aranda (Technical Lead)
- Spent entire session debugging ClickHouse with Darío
- Discovered use_concurrency_control creates scheduler requiring CPU cycles (causes queries to get stuck when resources saturated)
- Proposed table partitioning solution (tested reducing from 32 to 16 partitions)
- Investigated merge behavior and query stuck patterns
- Coordinated materialized view drops and recreation

## Key Discussion Topics

### Client "Pixel Perfect" Feedback
- **Source**: US design agency conducting intensive late-stage review
- **Scope**: Reviewing everything at pixel-perfect level (very demanding)
- **Task Division**:
  - **Javier**: Focus exclusively on functionality (especially Advanced Orders after microservices deploy to dev)
  - **Santiago**: Design QA in Chrome and Safari with meticulous attention
- **Safari Now In-Scope**: Must test in Safari (previously assumed Chrome-only)
- **Image Challenges**: Rendering issues in Safari requiring re-export to PNG format
- **Login Images**: Lucas re-exported all to 1000x1000 PNG, stored in Cooking Internal Team Drive folder
- **Lucas Emphasis**: "They're very intense, I need you with a lot of eye and a lot of criteria"

### ClickHouse Merge Crisis Deep Dive
- **Initial Symptoms**: Queries getting stuck, insert queries pending
- **Dashboard Analysis**: All three instances showing 31 merge parts running
- **Historical Pattern**: Single instance merging (normal) → Two instances (6 PM) → Three instances (7:30 PM) = stuck
- **Query Limit**: 1,000 concurrent queries per instance, once reached = complete lockup
- **Use Concurrency Control**:
  - Purpose: Prioritize API queries over cron jobs
  - Problem: Requires CPU cycles for scheduler, gets stuck when resources exhausted
  - Test: Disabled to see if queries stop getting stuck (inserts kept accumulating)
- **Async Inserts**: Also need CPU cycles for batch processing, causing similar stuck behavior
- **Total Merge Parts**: Growing from 4,000 to 8,500+ linearly
- **Partition Theory**: 32 partitions = 32 merge parts running (hitting merge_running limit)

### Partitioned Materialized Views Problem
- **Design**: Created partitioned holders_mb_1 and holders_mb_2 for performance optimization
- **Unintended Consequence**: Excessive merge operations across partitions
- **Data Flow**: transfers_tmp (null table) → materialized views → populate tables
- **Merge Behavior**: Saturated all three replicas simultaneously
- **Performance Before Crisis**: Top holders query and holders query both optimized and fast
- **Decision**: Drop partitioned views, recreate standard non-partitioned table with projection and correct ordering

### Table Structure Explanation
- **transfers_tmp**: Null table (in-memory only), data processed and immediately deleted
- **transfers**: Main table populated by materialized view from transfers_tmp
- **holders**: Populated by materialized view from transfers
- **Data Flow**: indexer → transfers_tmp → materialized view observer → other tables
- **Materialized View Logic**: Line 31 in SQL definition specifies "to default.holders" (pushes data to holders table)
- **Real-time Processing**: transfers_tmp only contains current real-time data, immediately deleted
- **Historical Data**: 4 months of trades overwhelmed RAM during migration attempt

### Proposed Solutions and Testing
- **Priority Adjustment**: Initially disabled cron priority (didn't solve problem)
- **Projection Strategy**: Create holders_2 table without partitioning but with correct projection and ordering
- **Query Optimization**: wallet_mint ordering for queries without final clause (don't need exact data for top holders)
- **Final Clause Issue**: Queries with final clause ignore projections, requiring alternative approach
- **Partition Reduction**: Considered reducing from 32 to 16 partitions using hexadecimal
- **Table Recreation**: Can't modify ordering in-place, must create new table and rename
- **Monitoring Gaps**: Dashboard graphs lack descriptions and underlying query definitions

### Network and Configuration Observations
- **HTTP Concurrency**: Reached 1,000 concurrent HTTP queries
- **TCP Connections**: Never exceeded 15 (unusual - should match HTTP count)
- **Potential Explanation**: HTTP/3 over UDP (QUIC protocol), but handshakes still require TCP
- **Hosted Limitations**: Can't configure XML directly, limiting optimization options
- **30-Day Trial**: Time pressure for optimization decision
- **Graph Monitoring**: Lacks useful descriptions making metric interpretation difficult

### Search and Token Info Issues
- **Current Problems**: Search and token info queries having issues
- **Workaround**: Patching with Jupiter data
- **Priority**: Lower since workaround exists

## Technical Highlights

### ClickHouse Debugging Tools Discovered
- **Merge Parts Dashboard**: Shows active merge operations per instance (found at 31 running on all three)
- **24-Hour View**: Revealed merge pattern progression from one to three instances
- **Advanced Dashboard**: Shows total merge parts growing from 4,000 to 8,500+
- **Query Metrics**: Total HTTP queries, TCP connections, running queries per instance
- **Limitations**: Many metrics lack descriptions or underlying query definitions

### Materialized View Cascade
- **Architecture**: transfers_tmp → materializes to → transfers → materializes to → holders
- **Real-time Focus**: transfers_tmp only processes current data (null table, memory-only)
- **Scaling Issue**: 20 minutes after initialization, 1 million records in holders
- **Expected Volume**: Should be small (real-time only), but accumulated quickly

### Performance Configuration Trade-offs
- **use_concurrency_control**: Enables query prioritization but requires CPU scheduling cycles
- **async_insert**: Enables batch processing but requires CPU for batching
- **Partition Count**: More partitions = more parallel merges = higher resource consumption
- **Server Settings**: Limited configuration options for merge limitation
- **Hosted Constraints**: Can't directly access XML configuration in ClickHouse Cloud

### Transaction Byte Limit Context (Continued Issue)
- **Problem**: 50% transaction failure rate from Solana byte limit
- **Cause**: Jupiter transaction + Cooking wallet fee + referral transfers exceeded limit
- **Current State**: Fee transfers disabled to make transactions work
- **Impact**: Not collecting Cooking fees or referral commissions
- **Planned Solution**: Separate linked transaction for fee collection (Esteban working on this)

## Action Items

### Critical (Today)
- [ ] **Luis**: Add global Maxwidth to all Tooltip components
- [ ] **Luis**: Review login component image alignment in divs
- [ ] **German**: Send criteria to Lucas about which inputs to disable when selling without funds
- [ ] **German**: Investigate toast notification extended display time issue
- [ ] **Marko**: Take assigned task from Javi and other pending tickets
- [ ] **Javier**: Focus on Advanced Orders testing once microservices deployed to dev (Chrome and Safari)
- [ ] **Santiago**: Design QA in Chrome and Safari with meticulous attention (especially Safari as weakest environment)

### This Week
- [ ] **Esteban**: Verify DNS deployment with Jesús for endpoint
- [ ] **Esteban**: Combine legacy transactions GET with current implementation
- [ ] **Esteban**: Priority items: 1) Timeframes by seconds, 2) Double transaction handling, 3) Auto-priority fee
- [ ] **Eduardo**: Review price precision across all protocols
- [ ] **Eduardo**: Continue debugging ClickHouse functionality with Darío and Martin
- [ ] **Federico**: Link all dev Perpetuals accounts as referrals to Lucas's Hyper Liquid code
- [ ] **Darío & Martin**: Continue ClickHouse optimization and query stuck problem resolution
- [ ] **Lucas**: Resolve on-ramp issue for Byron
- [ ] **Lucas**: Address application latency problem

### Strategic
- [ ] **Martin**: Write to Lucas to activate Claus subscription (about to expire)
- [ ] **Martin**: Review total SM part metrics
- [ ] **Martin**: Implement frontend polling when synchronous transaction occurs
- [ ] **Eduardo**: Continue Eco integration (after resolving ClickHouse stability)
- [ ] **Darío**: Enable search visibility
- [ ] **Team**: Prepare for stress testing coordination between Federico and Javier

## Important Notes

### Team Morale and Context
- **Holiday Work**: Team working through unusual political holiday in Argentina
- **Political Humor**: References to Matías Alé (celebrity with psychotic episode), presidential singing correlation with economic crises
- **International Context**: Luis mentioned Peru's 7th president in 10 years, Javier confirmed Venezuela tensions
- **ClickHouse Stress**: Martin joked about needing a priest for ClickHouse, Lucas suggested pilgrimage to Luján
- **Lucas Anecdote**: Knows Father Ignacio in Rosario (famous for miracles), Sri Lankan priest in Argentina

### Design QA Expectations
- **Santiago's Role**: Meticulous design review in both Chrome and Safari
- **Safari Priority**: "Weakest environment" requiring special attention
- **Scope**: Layout, typography rendering, image rendering
- **Typography Differences**: Some browser differences acceptable if technically unavoidable
- **Image Rendering**: Known challenges in Safari requiring specific solutions
- **Component Library**: Many unassigned bugs in Component Library Alignment project for team distribution

### ClickHouse Lessons Learned
- **Load Testing Context**: Must be done in near-production scenarios (empty database misleading)
- **Replication Timing**: Critical when mass-initializing data
- **Partition Strategy**: More isn't always better - can cause merge saturation
- **Query Structure**: Must carefully avoid reading all partitions unnecessarily
- **Projection Limitations**: Final clause ignores projections, requiring alternative optimization strategies
- **Historical Migration**: 4 months of trades saturated RAM, needs batching strategy

### Advanced Orders Testing Priority
- **Blocker**: Waiting for microservices deployment to dev
- **Reason**: Legacy integration will be deprecated, testing it wastes time
- **Scope**: Complete end-to-end functionality in latest version
- **Browsers**: Both Chrome and Safari required (Safari now officially in scope)
- **Lucas Emphasis**: Don't expect Safari problems but prefer to be conservative

### Transaction Microservice Status
- **Code Complete**: 6,000+ lines ready
- **Integration Pending**: Needs DNS resolution for deployment
- **Testing Plan**: Deploy to AWS for isolated testing first
- **Timeline**: This week if DNS unblocked
- **Priority Items**: Timeframes, double transaction handling, auto-priority fee

### Bubble Maps Integration
- **Status**: Martin and German to integrate "Baps Insidex" (formerly Bubble Maps)
- **Data Addition**: Add data to Token Details tables
- **Jupiter Badges**: Early trades, insiders, snipers won't work (missing data)
- **Diamond Hands**: Showing 36,000 holders (unsustainable for frontend rendering)

### Client Video Demo Requirements
- **Purpose**: Stable environment urgently needed for client video production
- **Flow**: Login → Kitchen → Filters → Portfolio → Token Details (Pengu/Farcoin) → Charts → Limit Order
- **Critical**: Portfolio calculations, position updates, chart accuracy
- **Issue**: Charts breaking when switching timeframes (15-minute causing complete redraw failure)

### On-Call System Discussion
- **Beta Phase**: Requires 24/7 operations with real users
- **Structure**: Passive guard rotation with additional compensation
- **Payment**: Extra hourly pay for actual work during on-call periods, separate guard pay
- **Necessity**: Ensure continuous operation during beta with real user base

### ClickHouse Current State
- **CPU Usage**: 16-17 of 30 limit (elevated but stable)
- **Status**: Responding, relatively fast, stable
- **Strategy**: Keep throwing money at problem until optimized
- **Cache Performance**: 99% cache hit rate (gigabytes of RAM helping)
- **Monitoring**: Continuous observation required for merge parts and query accumulation
