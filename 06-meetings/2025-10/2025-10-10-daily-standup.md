---
title: Daily Standup - 2025-10-10
type: meeting
meeting_type: daily_standup
date: 2025-10-10
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** October 10, 2025 (Holiday)
**Duration:** 44:32
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

Holiday standup focused on final QA refinements and ClickHouse recovery. Martin implemented type-safe API client generation to prevent runtime errors between frontend and backend. Darío resolved major ClickHouse crisis via backup recovery, with dramatic performance improvements on portfolio and holders queries post-recovery. Lucas distributed primarily frontend-focused tasks driven by intense client "Pixel Perfect" feedback. Federico and Javier planned comprehensive stress testing using simulated transactions in dev environment. Team working toward urgent deployment pending DNS resolution - meeting scheduled immediately post-demo due to Japan time zone constraints (12-hour difference with client).

## Team Updates

### Martin Aranda (Technical Lead)
- **Major Achievement**: Developed type-safe API client generator for frontend-backend communication
- **Trigger**: Production bug caused by Esteban's backend change breaking frontend transfers (no type safety)
- **Solution**: Generates typed API clients for all services automatically
- **Impact**: Will catch type mismatches at development time instead of runtime
- **Future**: Needs decision on when to run generation (GitHub actions timing)
- **Bug Fix**: Transfer token lookup now searches by user ID first (previously found first match regardless of user)
- **Context**: Imported wallet issue where Marco, Martin, and Javi all imported same wallet

### Luis Rivera (Frontend Developer)
- **Work Yesterday**: Attacked numerous bugs and tickets through afternoon
- **Internet Outage**: Lost connection evening, couldn't work, stayed up recovering hours
- **Current**: Working on positions carousel (struggling to replicate issue)
- **Bar Chart Issue**: Reported to Martin, needs endpoint hit more frequently per second
- **Friday Hours**: Asked permission to split hours between Saturday and Sunday (Lucas approved)
- **Observation**: Found many bugs in Company Library Alignment project, will assign self to C5 range

### Marko Jauregui (Frontend Developer)
- Almost finished new referral registration page (intro page to referral program)
- Will review against Figma for final perfection
- Then available for frontend bug fixes

### Federico Caffaro (Backend Developer)
- Merged observables for Hyper Liquid with exponential backoff retry for reconnection
- Met with Javier to plan stress testing approach
- **Stress Test Plan**:
  - User and wallet creation
  - Orders from multiple wallets
  - All providers (Jupiter, etc.) testing
  - Position verification and WebSocket testing
  - Build robust referral tree to test loading
  - Perpetuals testing
- **Question**: Will transactions be mocked (excluding Solana submission but testing providers)?
- **Lunch Tomorrow**: Early start, break at noon, resume afternoon through completion

### Esteban Restrepo (Backend Developer)
- Working with Luis on timeframes implementation
- **Priority Work**:
  1. Timeframes by seconds for charts
  2. Double transaction issue handling
  3. Auto-priority fee implementation (can extend to tomorrow)
- **Configuration Clarification**:
  - Auto-priority fee: Only swaps (not wallet-to-wallet transfers)
  - Transfers use very low/hardcoded priority fee
  - Cache Jupiter priority fee to display to users
  - Orders save configuration at creation (don't change if user toggles later)
  - Slippage: Default 30%, configurable per user, saved per order at creation
- Building on base version (not new microservice yet), using decoupled service for easy migration
- Off for 40 minutes for bank errands

### Eduardo Yuschuk (Indexer Developer)
- **Price Filtering**: Improved filter prioritizing reliable sources over Jupiter
- **Rationale**: Jupiter uses arbitrage and "crazy prices", maintains single stable source
- **Strategy**: Use Jupiter prices only when no higher-confidence sources available
- **Confidence Sources**: Market makers and bonding curves for new tokens
- **Dynamic Approach**: Discover token via Jupiter, use those prices until better source found
- **Question**: Should implement in dev and review price series?
- **Debt**: Precision debt on prices - wants to calculate from post-trade amounts instead of exchange price
- **Token Burning**: Proposed handling burned tokens transferred to "incinerator" wallet (not shown in holders list)
- **ClickHouse Changes**: Wants to persist changes to repository to avoid losing reference if instance disappears

### Darío Balmaceda (Infrastructure)
- **ClickHouse Recovery**: Restored from backup after merge processes spiraled out of control
- **Data Loss**: Information gap due to backup recovery
- **Performance Improvement**: Portfolio queries now much faster after indexer restart
- **Scalability**: Queries scale better as data populates (better long-term architecture)
- **Holders Queries**: Also functioning well post-recovery
- **Two-Client Plan**: Creating two ClickHouse backend clients with different configurations:
  - API client: Higher priority, more CPU
  - Cron jobs client: Lower priority, less CPU usage
- **Configuration**: Uses different users with separate priorities
- **Password Rotation**: Needs to add to ClickHouse (currently only exists for RDS)
- **Implementation**: If variables undefined, defaults to original client (backward compatible)

### Byron Chavarria (Mobile Developer)
- Finalizing limiters specifically in creation form
- **Question**: Range selector values - decimals from 0 to 1 or different format? (Martin will investigate)
- **Apple Account**: Tested successfully, logged in both Xcode and browser
- **Schemas**: Preparing three schemas (production, UAT, development)
- Will complete today
- Finishing limit order creation work

### Javier Grajales (QA/Testing)
- **Wallet Classification**: Tested and working correctly
- **Exception**: Diamond Hands definition now compares unrealized PNL (instead of PNL) - ticket created
- **Manual Comparison**: Slot matching working well:
  - Creator slot matches
  - Next 10 buyers match
  - Developer label working
- **Top Holder Percentage**: Didn't notice error Lucas reported
- **Holders Issues**:
  - Incinerator appearing in list (Eduardo addressing)
  - Zero-amount holders appearing (needs filtering)
- **Chart Issues**: Reported several to Luis
- **Test Funding**: Needs funds for testing (Lucas offered immediate transfer)
- **Stress Testing**: Ready to coordinate with Federico when ready
- Planning Apache AB for concurrency testing

### Santiago Gimenez (Backend/Frontend Developer)
- Not present at beginning of call

## Key Discussion Topics

### Type Safety Between Frontend and Backend
- **Problem**: Backend changes breaking frontend at runtime
- **Example**: Esteban's transfer funds endpoint migration caused frontend transfer failures
- **Root Cause**: No type checking between services
- **Solution**: Auto-generated typed API clients
- **Coverage**: All services (current and future microservices)
- **Detection**: Catches type mismatches during development instead of production
- **Pending Decision**: When to run generation (continuous integration timing)

### Stress Testing Strategy
- **Environment**: Dev during low-usage times (not spinning up separate infrastructure)
- **Mock Level**: Simulate transactions excluding Solana submission, but test Jupiter/providers
- **Approach**: Federico creating branch for testing, Martin helping with GitHub action deployment
- **Throttling**: May temporarily disable or create specific test branch
- **Tag Strategy**: Esteban suggested tagging dev branch to mark stable state before testing changes
- **Verification Needed**: Check if transaction library mock skips signature and transaction construction
- **Current Limitation**: Hardcoded to Jupiter only (need to reconfigure for multi-provider testing)

### Bar Chart Throttling Issue
- **Current**: Default 10 requests per 10 seconds on all endpoints
- **Problem**: Bar chart needs more frequent hits
- **Proposed**: 5 requests per second for bar chart endpoint
- **Question**: Can Trading View configure exponential backoff to avoid abuse?
- **Martin**: Will investigate Trading View backoff configuration options
- **Implementation**: Simple change once PR with endpoint documentation updates merged

### Session Management and Token Refresh
- **Issue**: Lucas getting kicked out in prod and dev
- **Question**: Multiple windows with same account open?
- **Current Behavior**: Latest refresh token stored in database, only that token valid
- **Result**: Two sessions = one gets kicked when other refreshes
- **Likely Cause**: Lucas using Safari and Chrome simultaneously with same Telegram account
- **Design**: Intentional to ensure latest refresh token always used
- **Testing Plan**: Lucas will test with two accounts (Raider and Telegram) in two browsers

### Limiters Visual Representation
- **Question**: Will limiter configuration changes affect mobile presentation/design?
- **Answer**: No changes to mobile app, only to web Advanced Orders table
- **Change**: Trigger representation format changed for easier scanning
- **Mobile**: Already considered in original design

### DNS Resolution Urgency
- **Client Location**: Japan (12-hour time difference)
- **Current Time for Client**: 10:10 PM
- **Risk**: Post-demo too late (client sleeping)
- **Request**: Access to domain dashboard for direct DNS management
- **Client Response**: Screen-share workshop session best they can offer
- **Plan**: 15-minute session immediately post-demo (11:30 AM demo time)
- **Blocker Impact**: Preventing deployment and testing of Esteban's transaction microservices

### Price Filtering Philosophy
- **Jupiter Approach**: Maintains stable price source, trades don't impact chart
- **Current Problem**: Jupiter using arbitrage, "crazy prices"
- **Proposed**: Prioritize higher-confidence sources over Jupiter
- **Higher Confidence**: Market makers, bonding curves
- **Fallback**: Use Jupiter when no better source available
- **Dynamic**: Upgrade from Jupiter to better source when discovered
- **Martin's Concern**: Still wants to explore non-trade price sources for AMMs (bonding curves different - literally the price)
- **Timing**: Not needed now, future enhancement

### Token Burning Handling
- **Current Issue**: Burned tokens still showing in holders list
- **Solana Mechanism**: Transfers to "incinerator" address
- **Proposed Solution**: Filter out incinerator address from holders queries
- **Additional Filter**: Remove holders with zero token amount
- **Implementation**: WHERE token_amount > 0 AND address != incinerator
- **Note**: Impossible to have negative token amounts in Solana (natural numbers only)
- **Current Workaround**: Frontend filters zeros, but should filter in query
- **Martin**: Will create issue and fix

### ClickHouse Performance Post-Recovery
- **Before**: Instances saturated with merges, 1,000+ queries stuck
- **Recovery**: Backup restore, lost data gap
- **After**: Portfolio queries much faster, better scaling characteristics
- **CPU**: 16-17 of 30 limit (elevated compared to previous 8, but stable)
- **Cache**: 99% cache hit rate with gigabytes of RAM
- **Strategy**: "Keep throwing money at problem" until optimized
- **Production Timing**: Darío asked about deploying same changes today
- **Lucas Preference**: Show dev state first, then push to prod late afternoon/tomorrow

## Technical Highlights

### Type-Safe API Client Generation
- **Purpose**: Prevent runtime errors from type mismatches between frontend and backend
- **Mechanism**: Auto-generates typed clients from backend API definitions
- **Scope**: All services (main backend + all microservices)
- **Benefit**: Compile-time type checking instead of runtime failures
- **Example Prevention**: Transfer funds endpoint type change would be caught immediately

### ClickHouse Two-Client Architecture
- **Problem**: Cron jobs and API competing for resources
- **Solution**: Separate clients with different priority levels
- **API Client**: Higher priority, more CPU allocation
- **Cron Client**: Lower priority, less CPU usage
- **Implementation**: Different users with separate priority settings
- **Backward Compatibility**: Undefined variables default to original client
- **Additional Needs**: Password rotation mechanism (like RDS)

### Transaction Configuration Immutability
- **Auto-Priority Fee**: User-level setting, saved at order creation
- **Order Behavior**: Executes with creation-time configuration (doesn't change if user toggles setting later)
- **Rationale**: Avoid confusing asynchronous changes to existing orders
- **Analogy**: Like changing slippage globally affecting all existing DCA orders
- **Slippage**: Same pattern - default 30%, user configurable, snapshotted at order creation
- **Transfer vs Swap**: Transfers use hardcoded low priority fee, swaps use user configuration

### Stress Testing Approach
- **User Creation**: Generate multiple test users
- **Wallet Creation**: Multiple wallets per user
- **Order Placement**: Multiple wallets, multiple providers
- **Position Verification**: Check position calculations correct
- **WebSocket Testing**: Verify real-time position updates
- **Referral Tree**: Build multi-level tree to test loading performance
- **Perpetuals**: Test Hyper Liquid integration
- **Transaction Mocking**: Exclude blockchain submission, include provider (Jupiter) interaction

### Price Source Prioritization
- **Tier 1**: Market makers, bonding curves (highest confidence)
- **Tier 2**: Direct protocol prices
- **Tier 3**: Jupiter aggregator (fallback only)
- **Dynamic Upgrading**: Start with available source, upgrade when better source discovered
- **Filtering Goal**: Avoid "crazy prices" from arbitrage opportunities
- **Chart Quality**: Prevent band-like price series (ceiling/floor instead of line)

## Action Items

### Critical (Today)
- [ ] **Martin & Jesús**: Confirm exact DNS records for domain configuration
- [ ] **Martin & Lucas**: 15-minute DNS resolution session immediately post-demo
- [ ] **Esteban**: Complete timeframes by seconds implementation
- [ ] **Esteban**: Handle double transaction issue
- [ ] **Esteban**: Work on auto-priority fee (can extend to tomorrow)
- [ ] **Lucas**: Transfer funds to Javier for testing

### This Week
- [ ] **Martin**: Implement bar chart throttling increase (5 requests/second)
- [ ] **Martin**: Investigate Trading View exponential backoff configuration
- [ ] **Martin**: Merge endpoint documentation PR, then implement throttling change
- [ ] **Martin**: Create issue for incinerator address filtering
- [ ] **Martin**: Add token_amount > 0 filter to holders query
- [ ] **Martin**: Implement frontend polling for synchronous transactions
- [ ] **Martin**: Combine legacy transactions GET with current implementation
- [ ] **Martin**: Investigate range selector value format for Byron
- [ ] **Federico**: Coordinate with Martin on test branch and GitHub action setup
- [ ] **Federico & Javier**: Execute comprehensive stress testing plan in dev
- [ ] **Darío**: Submit PR for two-client ClickHouse implementation
- [ ] **Darío**: Persist ClickHouse changes to indexer repository
- [ ] **Darío**: Add password rotation mechanism for ClickHouse (similar to RDS)
- [ ] **Eduardo**: Implement improved price filtering in dev for review
- [ ] **Eduardo**: Create ticket for token burning/incinerator handling
- [ ] **Luis**: Continue working on positions carousel replication
- [ ] **Luis**: Self-assign C5 range bugs from Company Library Alignment
- [ ] **Marko**: Final Figma comparison for referral registration page
- [ ] **Byron**: Complete three schema preparation (prod, UAT, dev)

### Strategic
- [ ] **Team**: Decide when to run API client generation (GitHub actions timing)
- [ ] **Team**: Review and approve two-client ClickHouse architecture
- [ ] **Team**: Plan production deployment of ClickHouse optimizations (after dev demonstration)
- [ ] **Eduardo**: Continue exploration of non-trade price sources for AMMs (future enhancement)

## Important Notes

### Holiday Work Acknowledgment
- **Martin**: "I want to thank you all for all the effort you're putting in. I know today is a holiday and you're all working. I know tomorrow is Saturday and you're going to work it and I'm very grateful with you all that you're holding on so we can deliver and come out on time."
- **Lucas**: "Completely agree. I promise we'll make it more comfortable, calmer from here on. I believe it's public knowledge the titanic work we've put in these last months. It's a Pareto of s***. The last 20% costs a barbaric amount."
- **Context**: Team working through national holiday and weekend for delivery deadline

### DNS Resolution Context
- **Client**: In Japan, 12-hour time difference
- **Demo Time**: 11:30 AM Argentina time (11:30 PM Japan time)
- **Problem**: Post-demo too late for client (nearly midnight)
- **Urgency**: Blocking microservices deployment for testing
- **Client Limitation**: Won't provide direct dashboard access, only screen-share session
- **Strategy**: Resolve immediately post-demo while client still available

### Testing Environment Funding
- **Previous Source**: Team Cook accounts (discontinued by client)
- **Current Source**: Raider account
- **Immediate Need**: Javier needs funds for testing
- **Lucas Solution**: Direct transfer from personal account
- **Mobile Testing**: Byron also needs account access for OTP and push notifications

### ClickHouse Recovery Aftermath
- **Data Gap**: Lost information during backup recovery
- **Performance Gain**: Dramatic improvement in query speed
- **Scalability Improvement**: Better long-term growth characteristics
- **Monitoring**: CPU elevated (16-17) but stable and predictable
- **Next Steps**: Apply same changes to production after demonstrating dev stability

### Configuration Philosophy
- **Immutability**: Orders execute with creation-time configuration
- **User Settings**: Change for future orders, don't affect existing
- **Rationale**: Prevent confusing asynchronous changes to live orders
- **Consistency**: Same pattern for auto-priority fee, slippage, other user-level settings

### Stress Testing Scope
- **Goal**: Validate system handles high concurrency and load
- **Approach**: Real provider integration (Jupiter), mocked blockchain submission
- **Environment**: Dev during off-hours to avoid impacting development
- **Method**: Apache AB for load, custom scripts for specific scenarios
- **Coordination**: Federico and Javier leading, Martin assisting with infrastructure

### Price Filtering Strategy
- **Current Problem**: Jupiter arbitrage causing "crazy prices"
- **High-Level Coherent**: Lucas agrees with approach philosophically
- **Need Review**: Wants detailed review before implementation
- **Martin Concern**: Still wants to explore alternative price sources for AMMs (not urgent)
- **Implementation**: Deploy to dev, review price series, iterate

### Frontend Task Distribution
- **Focus**: Primarily frontend (most client feedback coming from design review)
- **Exceptions**: Login and Advanced Orders (require dedicated session with Luis)
- **Size**: Small tasks being distributed across team
- **Source**: Lucas creating issues from client "Pixel Perfect" review
- **Assignment**: If not your scope, reassign without concern

### Referral Testing Progress
- **Marko**: Almost finished registration page
- **Javi**: Generating multiple wallets linked with referrals
- **Federico**: Can retroactively link dev accounts for testing
- **Goal**: Test referral tree building and fee distribution

### Auto-Priority Fee and Slippage
- **User Level**: Stored in user table, configurable
- **Order Level**: Snapshotted at creation time (immutable after creation)
- **Auto-Priority Scope**: Only swaps (not wallet-to-wallet transfers)
- **Transfer Fee**: Very low or hardcoded (no auto-priority)
- **Display**: Cache Jupiter's returned priority fee, show to user
- **Refresh**: Per transaction, not every 3 seconds (latency acceptable for visualization)
- **Default Slippage**: 30% for all users

### Session Management Design
- **Intent**: Ensure latest refresh token always valid
- **Consequence**: Multiple sessions for same account = one gets kicked
- **User Experience**: Acceptable trade-off for security
- **Lucas Workaround**: Use different accounts in different browsers
- **Alternative**: Could allow multiple concurrent sessions (requires design change discussion)
