---
title: Daily Standup - 2025-10-13
type: meeting
meeting_type: daily_standup
date: 2025-10-13
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** October 13, 2025 (Monday)
**Duration:** 53:14
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

Critical pre-launch week with Wednesday internal delivery deadline (official Friday). Launch will be open beta accessed via referral codes (not Friends and Family), expecting 200-2,000 users. Major architectural discussion about Jupiter integration revealing fundamental issues: showing arbitrage prices from divergent sources without provider visibility creates "zero predictability" for users. Eduardo proposed discriminating prices by provider (mimicking Jupiter/DexScreener model) but requires significant indexer restructuring. Team decided to first filter out arbitrage prices, concentrate on individual swaps from high-liquidity pools. Eco integration continuing despite requiring liquidity pool address (similar latency to Jupiter when address provided). Esteban addressing critical duplicate transaction issue. Portfolio wallet manager has spinner continuation bug and token amount display error. Byron finalized iOS configurations for TestFlight distribution.

## Team Updates

### Luis Rivera (Frontend Developer)
- **Friday**: Definitively solved all Cooking header issues
- **Weekend**: Updated Advanced Orders - many right-side components were missing
- **Current**: Finishing bottom panel tables, should complete by mid-day
- **Status**: Advanced Orders view will be complete after bottom panel update

### Marko Jauregui (Frontend Developer)
- **Friday**: Completed various referral-related bug fixes (now working well)
- **Saturday**: Built new portfolio page (complete and ready)
- **Question**: Any specific pages to review, or proceed with backlog bugs?
- **Assignment**: Will continue with bugs from backlog

### Martin Lecam (Backend/Frontend Developer - Returning)
- Welcome back to team
- Assigned first task: Complete filters feature pending from cowork session
- Lucas will review backlog and pass additional tasks

### Federico Caffaro (Backend Developer)
- **Stress Testing Branch**: Ready with mass user creation endpoint (skips providers, creates wallets)
- **Transaction Mocking**: Configured to skip blockchain submission for testing
- **Endpoints Ready**: Quick operations and other endpoints ready for load testing
- **Search Bug**: Fixed 429 error in search when typing/deleting rapidly (adjusted throttler)
- **Wallet History**: Reviewed issue Lucas reported, everything working correctly (Javi couldn't replicate)
- **Note**: Removed SOL funds from test wallet with triple transaction, left wallet untouched for Esteban's investigation

### Esteban Restrepo (Backend Developer - Transaction Microservice)
- **Saturday Morning**: Discovered DNS deployed, completed transaction microservice deployment
- **Configuration Issues**: Spent morning coupling microservices (queue misalignment issues)
- **Testing**: Started Swagger backend testing of transactions
- **Focus**: Dedicated to transaction fixes, Javi reporting all transaction issues directly
- **Duplicate Transaction Issue**: Found case duplicated by external ID, will verify no transaction with same ID before processing
- **Timeframe**: Resolving multiple transaction issue today and tomorrow

### Eduardo Yuschuk (Indexer Developer)
- **Weekend Work**: Price filtering logic improvements
- **Major Insight**: Fundamental Jupiter integration problem - showing arbitrage prices from divergent sources
- **Key Issue**: Platform has "zero predictability" on user pricing vs other platforms
- **Current Approach**: Filtering now includes providers and pools within Jupiter
- **Strategy**: Propagate only prices from major pools (launchers, Radium, Orca, Meteora)
- **Focus**: Individual swaps (not engineered multi-hop routes for cheaper prices)
- **Attack Prevention**: Filter mini-pools for price manipulation using volume-based discrimination
- **Pump Swap Bug**: Fixed incorrect amount and collateral amount (based on pool structure, needed translation to SOL-based pricing)
- **Impact**: Bug visible in frontend, fix being deployed

### Darío Balmaceda (Infrastructure)
- **Friday**: Completed 3 PRs (indexer sort changes, 2 backend PRs: incinerator feature, two-client decoupling)
- **Status**: All PRs tested, tagged for Cloud review, ready for merge
- **Query Optimization**: Found optimizations for details query
  - Worst case: 50% reduction in rows read
  - Best case: 10x reduction in rows read
  - Speed gain: Minimal (300ms → slightly faster) but RAM usage significantly reduced
  - Important: One of most frequently executed queries
- **Kitchen Query**: Analyzing optimization possibilities
  - Inner join between bonding curves and mint_latest tables
  - Cache component exists
  - Partitioning could help but requires major migration
  - ~100ms improvement not worth large migration at this stage

### Byron Chavarria (Mobile Developer)
- **Saturday**: Finalized certificates, provisioning profiles, App Store Connect configurations
- **Xcode Setup**: Complete for running on physical devices
- **TestFlight**: Ready to upload versions for internal and client testing
- **iOS 26**: Adjustments and validations for navigation, button handling, backgrounds, interactions
- **PR**: Submitted for Martin's review
- **Current**: Continuing limit order work (visual presentation details and data handling)

### Lucas Cufré (Project Lead)
- **Weekend**: Extensive testing Friday and Saturday
- **Eco Meetings**: Multiple sessions with Eco team
- **Portfolio Page**: Designed and passed to Marcos (needs Javi's alignment review)
- **Portfolio Update**: Now in dev with new tables, changed cell interactions
- **Critical Issues Found**:
  1. Transaction finalization notification not working (spinner continues after positions disappear)
  2. Spinner transfers to next table rows when positions deleted
  3. Token amount shows in Solana value instead of actual token quantity (prevents transferring total tokens)

### Javier Grajales (QA/Testing)
- **Friday**: Closed many tickets, reviewed various issues
- **Saturday**: Started transaction testing
- **Wallet Manager Issues**: Found problems with transfers between own accounts (SOL and tokens)
- **Market Orders**: Testing revealed triple execution issue (same as Lucas experienced)
- **Test Wallet**: Left untouched for Esteban's investigation (only removed SOL funds for other wallet use)
- **Current**: Reading limiter and take profit/stop loss Notion documentation
- **Next**: Review portfolio page implementation, organize all wallet manager tickets

### Santiago Gimenez (Frontend/Backend Developer)
- **Friday**: Testing various features
- **Status**: Most Notion tasks complete
- **Question**: Continue testing or move to features? (Will coordinate with Lucas)

### Martin Aranda (Technical Lead)
- **DNS Deployed**: Saturday morning
- **Eco Integration**: Will handle service integration (Esteban focused on transaction bugs)
- **Routing Priority**: Proposed Jupiter → Eco → others (Lucas agreed for this week given Eco's state)
- **QuickNode Concern**: 70 million requests per month (wants to identify source)
- **Total Supply**: Can optimize requests, average 10-30 tokens per request
- **Security Module**: Discussed with Eduardo - will write TypeScript module for transaction validation
- **Nonce Account**: Investigating Eco recommendation (decided against implementation - too cumbersome)

## Key Discussion Topics

### Launch Strategy - Open Beta via Referral Codes
- **Not Friends and Family**: Open beta approach
- **Access Method**: Only via referral code link (cooking.com/login won't work without code)
- **Viral Mechanism**: Referred users can generate their own referral codes
- **Model**: Replicating Bullex Neo methodology (dominated market via referral-only beta)
- **User Expectations**: 200-2,000 initial users
- **Marketing**: No bombastic marketing campaign, organic growth through referrals
- **Internal Deadline**: Wednesday (official Friday) to avoid weekend on-call work

### Fundamental Jupiter Integration Problem
- **Current State**: Showing divergent prices from multiple sources including arbitrage
- **Visibility Issue**: No provider discrimination - users see aggregated price from unknown sources
- **Execution Gap**: Price shown vs execution route completely opaque
- **Predictability**: "Zero predictability" on what price user will actually get
- **Comparison Problem**: Prices don't make sense compared to other platforms
- **User Impact**: Platform with least price predictability in market

### Proposed Solution - Provider Discrimination
- **Concept**: Show prices discriminated by provider (like DexScreener, Jupiter frontend)
- **Benefit**: Coherent price series per provider, known execution routes
- **Technical Impact**: Requires indexer and core architecture restructuring
- **Scope**: Affects instant price, time series (need to aggregate all provider series per token)
- **Alternative**: If pools not indexed, at least discriminate by provider using Jupiter API
- **Competition**: All competitors already doing this (indexing Orca, Meteora pools)
- **Eduardo's View**: "To compete, you have to index this. I don't see a path for the application if we don't eventually index that."

### Interim Solution - Filter Arbitrage, Focus High Liquidity
- **Phase 1**: Eliminate arbitrage-generated prices (outliers causing chart issues)
- **Phase 2**: Concentrate on individual swaps from providers (not multi-hop engineered routes)
- **Phase 3**: Filter low trading volume pools
- **Result**: High-liquidity price series, Jupiter routes as needed, Eco option for speed
- **Trade-off**: Still obfuscating information, experienced traders will notice "something's weird"
- **Lucas Concern**: Need to understand target trader - memecoins require knowledge, contradicts "for everyone" vision

### Eco Integration Challenges
- **Speed Proof**: Client insists on Eco due to demonstrated execution speed in POC
- **Problem**: Eco endpoint requires liquidity pool address (defeats router purpose)
- **Latency Reality**: Search cost must be absorbed somewhere (Eco or internally)
- **Test Results**: 500ms Jupiter vs 620ms Eco when address provided (virtually same)
- **Partial Implementation Opportunity**: Kitchen first two columns (newly minted, pre-graduation tokens)
- **Rationale**: Known single AMM, known liquidity pool = can pass address immediately
- **Caveat**: Token can appear in any other market even during launcher bonding curve
- **Post-100% Graduation**: Route through Jupiter (multiple pools, address unknown)
- **Eco Development State**: "Less than alpha" - team is Cooking's guinea pigs
- **Quote**: "Literally they told us to pass everything we find because it's in full development and we're doing the real testing."

### Duplicate Transaction Crisis
- **Lucas Case**: 0.001 SOL PNG purchase via market order → triple execution
- **Pattern**: Multiple sales attempted, all tripled
- **Javi Case**: Three executions (same count as Lucas)
- **Evidence**: All distinct transactions visible in wallet audit on Solscan
- **Root Cause**: External ID duplication in processing
- **Fix**: Verify no transaction with same external ID before processing
- **Timeline**: Critical fix today/tomorrow

### Wallet Manager Bugs
- **Spinner Continuation**: After transaction completes and positions disappear, spinner keeps running
- **Spinner Transfer**: Spinners from deleted positions transfer to next table rows
- **Timeout**: 2-minute timeout triggers error when transaction service doesn't confirm
- **Token Amount Display**: Shows SOL value instead of token quantity
- **Impact**: Can't transfer total tokens (max button uses SOL valuation, not actual token count)
- **Assignment**: Marko taking ownership of wallet manager issues

### Security Module Development
- **Rejected**: AML/terrorism financing providers (wrong use case, high latency)
- **Rejected**: Language model analysis (slow execution time)
- **Rejected**: Transaction simulation (100-300ms latency, kills Eco speed advantage)
- **Chosen**: Hardcoded rule-based logic in TypeScript
- **Rules**:
  1. Interpret instructions: swaps must be related chain (SOL → token or token → SOL)
  2. No deviation to unrelated tokens
  3. Transfer instructions (fees) capped at maximum percentage of total
- **Assignment**: Eduardo implementing tomorrow (today occupied)
- **Integration**: Martin handling Eco service integration in parallel

### Nonce Account Decision
- **Eco Recommendation**: Use Solana nonce account for multiple transactions with same nonce
- **Mechanism**: Smart contract per wallet, registers transaction nonce
- **Benefit**: Create multiple transactions with same nonce, only one executes, increments nonce
- **Problems**:
  1. Requires smart contract creation transaction for each wallet before any Eco transaction
  2. Limits active transactions to one at a time (all transactions until nonce updates = only one executes)
  3. Requires tracking nonce state, managing transaction queue
- **Assessment**: "Cumbersome," "potential mess"
- **Decision**: Not implementing nonce account despite Eco repeating recommendation 3 times
- **Alternative**: Send only one of multiple transactions Eco returns

## Technical Highlights

### Price Filtering Logic Improvements
- **Provider Discrimination**: Now filters by providers and pools within Jupiter
- **Volume-Based**: Individual swap volume and general pool volume tracked in memory
- **Pool Selection**: Propagate only major pools (launchers, Radium, Orca, Meteora)
- **Attack Prevention**: Filter mini-pools created to manipulate price (deposit liquidity, trade, close pool)
- **Swap Type**: Individual swaps only (not engineered multi-hop routing for cheaper prices)
- **Arbitrage Elimination**: In progress, fixing chart outliers issue
- **Root Cause**: "With Jupiter index I made a machine for aggregating arbitrages"

### Pump Swap Bug Fix
- **Issue**: Amount and collateral amount sent incorrectly
- **Cause**: Based on pool structure (token A vs token B positioning)
- **Problem**: Pool might have SOL as collateral but token as base (inverse of expected)
- **Solution**: Translation to SOL-based pricing regardless of pool structure
- **Visibility**: Bug visible in frontend, fix deployed

### Stress Testing Setup
- **Mass User Creation**: Endpoint creates users and wallets, skips providers
- **Transaction Mocking**: Configured to skip blockchain submission
- **Endpoint Coverage**: Quick operations and all other endpoints ready
- **Search Optimization**: Throttler adjusted to prevent 429 errors during rapid typing

### Transaction Microservice Deployment
- **Saturday Morning**: DNS deployed, enabled microservice deployment
- **Queue Issues**: Morning spent resolving queue misalignment between microservices
- **Testing**: Swagger-based backend testing in progress
- **External ID Check**: Adding verification to prevent duplicate transaction processing

### QuickNode Request Analysis
- **Volume**: 70 million requests per month
- **Sources**: Frontend, backend, indexer all using QuickNode
- **Indexer**: Eduardo believes indexer not primary cause (uses Hello Moon in config)
- **Panel**: Not very detailed, mostly billing information
- **Action**: Eduardo investigating where requests being lost

### ClickHouse Query Optimizations
- **Details Query**: 50% to 10x reduction in rows read (minimal speed gain but significant RAM reduction)
- **Kitchen Query**: Inner join optimization under investigation
- **Incinerator Feature**: PR ready for merge
- **Two-Client Architecture**: PR ready for merge (API client higher priority, cron client lower)

### iOS TestFlight Configuration
- **Certificates**: Complete
- **Provisioning Profiles**: Complete
- **App Store Connect**: Configured
- **Xcode**: Ready for physical device deployment
- **Versioning**: Can control internal vs client test versions
- **iOS 26 Compatibility**: Navigation, buttons, backgrounds, interactions validated

## Action Items

### Critical (Today/Tomorrow)
- [ ] **Esteban**: Fix duplicate transaction issue (verify external ID uniqueness before processing)
- [ ] **Esteban**: Resolve multiple transaction replication issue
- [ ] **Marko**: Fix wallet manager spinner continuation bug
- [ ] **Marko**: Fix token amount display (show token quantity, not SOL valuation)
- [ ] **Marko**: Implement transaction key/ID per row to prevent spinner transfer
- [ ] **Martin**: Review Byron's iOS PR
- [ ] **Martin**: Integrate Eco into service (Jupiter → Eco → others priority)
- [ ] **Eduardo**: Deploy Pump Swap amount/collateral fix
- [ ] **Eduardo**: Continue price filtering improvements (eliminate arbitrage prices)

### This Week (Wednesday Internal Deadline)
- [ ] **Martin & Darío**: Update production ClickHouse today
- [ ] **Martin**: Tomorrow - finalize production infrastructure (autoscaling configurations)
- [ ] **Martin**: Tomorrow - deploy and test transaction microservice in production
- [ ] **Eduardo**: Tomorrow - implement security module (TypeScript transaction validation rules)
- [ ] **Eduardo**: Investigate QuickNode request source (70M/month)
- [ ] **Eduardo**: Optimize Total Supply requests (average 10-30 tokens per request)
- [ ] **Luis**: Complete Advanced Orders bottom panel tables by mid-day
- [ ] **Martin Lecam**: Complete filters feature from cowork
- [ ] **Javier**: Review portfolio page alignment
- [ ] **Javier**: Organize wallet manager tickets comprehensively
- [ ] **Javier**: Continue transaction and order testing
- [ ] **Byron**: Continue limit order visual and data work
- [ ] **Darío**: Submit Kitchen query optimization PR
- [ ] **Darío**: Submit details query optimization PR (mint-related improvements)

### Strategic
- [ ] **Team**: Discuss provider-discriminated pricing architecture with client
- [ ] **Team**: Evaluate long-term pool indexing strategy (Orca, Meteora, etc.)
- [ ] **Team**: Define target trader profile (knowledgeable memecoin trader vs "everyone")
- [ ] **Eduardo**: Evaluate feasibility of indexing major AMM pools for competition parity

## Important Notes

### Launch Timing and Strategy
- **Official Deadline**: Friday, October 17, 2025
- **Internal Target**: Wednesday, October 15, 2025
- **Rationale**: Avoid weekend on-call work responding to issues from Friday launch
- **Access Model**: Referral code only (no direct login without code)
- **Growth Model**: Viral - referred users generate codes, expanding access organically
- **User Range**: 200-2,000 expected initial users
- **Stage**: Open beta (not Friends and Family, not full public launch)

### Team Welcome
- **Marcos Tacca**: Officially welcomed to team mid-crisis
- **Lucas Comment**: "Welcome to Cooking. This has been the last year of development. I'm glad you're here because it gives you context when I go out pulling my hair. It comes from somewhere."
- **Timing**: Joining during critical pre-launch week with architectural debates

### Philosophical Product Discussion
- **Target User Conflict**: "For everyone" vision vs memecoin trader reality
- **Solana Complexity**: Operating on Solana requires certain knowledge level
- **Memecoin Nature**: Not for "noob who just downloaded Phantom and put in some money from Binance"
- **Provider Visibility**: Experienced traders will notice lack of provider transparency
- **Competitive Parity**: All competitors show provider-discriminated pricing
- **Decision Needed**: Client must accept trader-focused paradigm or commit to major restructuring

### Eco Development Maturity
- **State**: "Less than alpha"
- **Testing Role**: "We're doing the real testing"
- **Recommendation Intensity**: Nonce account suggestion repeated 3 times in meeting
- **Implementation Reality**: Too cumbersome for platform needs
- **Speed Parity**: 500ms vs 620ms when address provided (virtually identical)
- **Future Value**: Continued collaboration to refine as Eco matures

### Transaction Service Status
- **Deployment**: Complete (Saturday morning after DNS)
- **Queue Configuration**: Resolved after morning debugging
- **Testing**: In progress via Swagger
- **Critical Bug**: Duplicate transactions (triple execution pattern)
- **Communication**: All transaction issues routed directly to Esteban
- **Timeline**: Bug fixes today and tomorrow critical for Wednesday target

### Price Filtering Philosophy
- **Current Problem**: "Machine for aggregating arbitrages" creating chart outliers
- **Short-term**: Filter arbitrage, focus high-liquidity individual swaps
- **Medium-term**: Discriminate by provider using Jupiter API
- **Long-term**: Index major AMM pools (competitive necessity)
- **Trade-off**: Transparency vs development time vs competitive positioning

### QuickNode Usage Concern
- **Volume**: 70 million requests/month
- **Expected**: Total Supply ~2 million/month
- **Gap**: 68 million unaccounted requests
- **Sources**: Frontend, backend, indexer all potential contributors
- **Action**: Investigation needed to identify leak
- **Cost**: "Throwing money at problem" acknowledged but needs optimization

### Portfolio/Wallet Manager Priority
- **New Design**: Tables updated, cell interactions changed
- **Critical Bugs**: Spinner behavior, amount display
- **Testing**: Javi reviewing alignment, Marko fixing bugs
- **User Flow**: Transfer functionality broken (can't send total token amount)

### Infrastructure Deployment Plan
- **Today**: Update production ClickHouse
- **Tomorrow**: Finalize infrastructure (autoscaling), deploy transaction microservice to production
- **Testing**: Production transaction microservice testing tomorrow
- **PRs Ready**: Incinerator feature, two-client architecture, indexer sort changes
- **Wednesday**: Internal launch target

### Security Module Approach
- **Rejected Approaches**: AML providers, LLM analysis, transaction simulation
- **Chosen**: Hardcoded rule-based interpretation
- **Performance**: Minimal latency impact (critical for Eco speed advantage)
- **Rules**: Swap chain validation, transfer cap enforcement
- **Implementation**: Tomorrow (Eduardo busy today)
