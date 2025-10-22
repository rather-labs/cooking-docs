---
title: Daily Standup - 2025-10-15
type: meeting
meeting_type: daily_standup
date: 2025-10-15
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** October 15, 2025 (Wednesday - Internal Delivery Target)
**Duration:** 30:34
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

Critical internal delivery day with production deployment planned in stagger stages. Byron resolved iOS 16/17 navigation bugs. Darío achieved major ClickHouse optimization - unified query templates for Kitchen and Mint details reducing memory consumption 5x (16M to 6M rows read) and doubling average performance. Eduardo ready for ClickHouse production migration with updated SQL definitions. Esteban completed transaction microservice deployment after DNS resolution, now focused on fixing transaction confirmation polling issue Lucas reported. Market orders and TWAP working correctly, but inner swap transactions showing incorrect token names in Wallet History. Marko fixed wallet manager holding amount display and sell-all infinite spinner. Transaction polling confirmation issue prioritized for 11 AM client meeting.

## Team Updates

### Byron Chavarria (Mobile Developer)
- **Yesterday**: Advanced limit order creation (final details)
- **iOS Navigation Bugs**: Found issues in iOS 17 and iOS 16 (minimum supported version)
- **Today**: Working on navigation corrections
- **PR**: Will likely submit today once fixes complete

### Darío Balmaceda (Infrastructure - ClickHouse Optimization)
- **Major Achievement**: Optimized Kitchen and Mint details query templates
- **Memory Reduction**: 16 million rows → 6 million rows read (5x improvement) for Graduate column queries
- **Technical Solution**: Found 2023 workaround for ClickHouse issue - prevents re-reading filtered rows on each left join
- **Query Unification**: Merged previously separated Kitchen and Mint details queries (shared similar logic, needed inner join)
- **Performance**: 2x average speed improvement
- **Testing**: Needs to verify Search query returns same results with template changes
- **Impact**: Reduces ClickHouse resource consumption significantly
- **Status**: Will submit PR after Search query verification

### Eduardo Yuschuk (Indexer Developer)
- **ClickHouse Migration**: Ready for production migration
- **SQL Definitions**: Updated in indexer repository
- **Will Execute**: Migration when has time, or team can run if preferred
- **Darío Feedback**: Requested preserving conceptual insights and fundamental tips about ClickHouse (not excessive examples, but key unlocking concepts)
- **Future Use**: ClickHouse likely needed for this data volume across other projects
- **Radium Completion**: Reviewing what's required to finish Radium integration
- **Meteora Estimate**: Will have precise estimate by midday (not random guess, reasonable calculation)
- **Approach**: Same techniques as Radium, different contracts/IDLs, fundamental techniques controlled
- **Risk**: Not super risky, methodology established

### Martin Aranda (Technical Lead)
- **Security Validator**: Asked Eduardo about Eco security validator status
- **Eduardo Response**: Ready to use, can develop iteratively, no need for super validator yet
- **ClickHouse Deployment**: Confirmed moving forward with Darío's HTTP user creation
- **User Separation**: Backend HTTP user (duplicate of backend user) for differentiating cron jobs vs user queries
- **Priority**: Currently disabled (not hitting resource limits), can enable if needed
- **Volume Growth Concern**: More integrations = more data volume = higher operational costs

### Federico Caffaro (Backend Developer)
- **Missing Migration**: Sent missing transactions table migration file
- **Fee Wallet Update**: Changed from private key to Turnkey (tested, working)
- **Wallet IDs**: Forgot to save when sent 100 PRs, will generate 2 new IDs and save (needed for export/transfer)
- **Production Flag**: Notify when going to production to flag Hyper Liquid referral feature and pass to PR
- **Claims Bug**: Found bug in fee distribution - fees were charged to platform instead of user (now fixed, charges user)

### Esteban Restrepo (Backend Developer - Transactions)
- **Saturday**: Discovered DNS deployed, completed transaction microservice deployment
- **Morning Configuration**: Coupled microservices (had queue misalignment issues - pointing to different queues)
- **Testing**: Started Swagger backend transaction testing
- **Bug Fixes**:
  - Maximum balance transfer error (fixed)
  - Duplicate transactions (fixed)
  - Fee charging (fixed)
- **Fee Integration**: Integrated fees with Federico's multi-referral system
- **Current Issue**: Transaction confirmation not appearing despite backend resolving quickly (investigating)
- **Javier Coordination**: All transaction issues reported directly to Esteban

### Luis Rivera (Frontend Developer)
- **Advanced Orders**: Complete after taking longer than expected (many reviews)
- **Yesterday**: Lucas sent minor additional fixes (now resolved)
- **Current**: Focusing on other tickets
- **Last Night**: Updated Learn More modal information
- **Prefi Settings**: Started refactor last night after remembering priority
- **Assignment**: Will focus exclusively on Prefi, passing other work to German

### German Derbes Catoni (Frontend Developer)
- **Status**: Reviewed channel threads, not yet checked Notion tickets
- **Assignment**: Safari compatibility priority (typography weight, alignment adjustments)
- **Plan**: Opening Safari now to compare differences vs Chrome

### Marko Jauregui (Frontend Developer)
- **Bug Fixes**: Liquidating various tickets
- **Toast Duration**: Fixed extended duration issue (Lucas to retest)
- **Technical**: Changed duration, disabled timer pause on hover/click (RX default behavior still might affect)
- **Observation**: Some toasts dismiss in 3 seconds, others get stuck without user interaction
- **Next**: Will investigate stuck toast behavior
- **Top 10 Trader Icon**: German reported icon display issue in table (giant vs normal size)
- **Availability**: Ready to help with priority tickets

### Martin Lecam (Backend/Frontend Developer)
- **Progress**: Closed all pending bugs except one (Order History not showing despite response)
- **Response Data**: Has data, correct types, but not displaying visually
- **PR**: Submitted to Martin for review
- **Filters**: Already sent to test (working except Jupiter filters as agreed), implemented special view (Santi's design with lines) and normal view (three icons)
- **Status**: Ready for Lucas to test
- **Yesterday**: Took ticket from Luis (almost got stabbed for stealing work)
- **Metadata**: Still owes Martin the metadata request from yesterday

### Javier Grajales (QA/Testing)
- **Market Orders**: Buy and sell working correctly (no more triple execution)
- **TWAP**: Working perfectly
- **Missing**: Limit order operation limits (assigned to Luis)
- **Wallet History**: Inner transactions showing wrong token names (USDC, Bon instead of Fcoin, Pengu)
- **Location**: Portfolio → Trade History
- **Eduardo Response**: Long swaps and inner swaps now flagged, discriminated, don't translate to trades
- **Timing**: Materialized view change deployed midday yesterday, afternoon tests should be correct
- **Invested Amount**: Showing zero for some operations in portfolio (reported privately to Eduardo)
- **Next**: Testing limit orders once enabled, stress testing with Federico when ready

### Santiago Gimenez (Frontend/Backend Developer)
- **Friday**: Testing various features
- **Status**: Most Notion tasks complete
- **Question**: Continue testing or move to features? (will coordinate with Lucas)

## Key Discussion Topics

### Production Deployment Strategy
- **Timing**: Once stable in dev, deploy to production
- **Original Plan**: Post-daily deployment (won't make it - too many fixes remaining)
- **Staged Approach**:
  1. ClickHouse first
  2. Indexer once ClickHouse complete
  3. Backend and frontend simultaneously after indexer
- **ClickHouse Today**: Update production ClickHouse (Eduardo/Darío coordinating)
- **Tomorrow**: Infrastructure finalization (autoscaling), transaction microservice production deployment/testing

### Critical Transaction Confirmation Issue
- **Problem**: Notifications never appear despite backend resolving transactions
- **Pattern**: All 10 transactions stuck at "transaction initialized" toast, no confirmation response
- **Most Visible**: Portfolio sell-all - initialization toast appears, then timeout after 2 minutes
- **Root Cause Investigation**:
  - External ID found correctly
  - 5 retry attempts failed
  - Polling mechanism finding transaction ID
  - Appears to be frontend batching issue
- **Urgency**: Client meeting 11 AM, needs visual confirmation of transaction completion
- **Workaround**: Lucas can show inspector response if not fixed
- **Priority**: Must resolve in next hour if possible

### Inner Transaction Display Problem
- **Issue**: Wallet History showing inner swap tokens instead of actual purchased tokens
- **Example**: Buying Fcoin or Pengu displays USDC or Bon in history
- **Root Cause**: Complex swaps with intermediate steps
- **Eduardo's Fix**: Long swaps and inner swaps now flagged and discriminated, shouldn't translate to trades
- **Deployment**: Materialized view dropped and recreated midday yesterday
- **Testing**: Afternoon transactions should work correctly (Javier will verify)
- **Assigned**: Eduardo reviewing Javier's specific wallet case

### ClickHouse Query Template Optimization Details
- **Problem**: Left joins re-read all previously filtered rows (wasteful iteration over known 10 records)
- **Solution**: Found 2023 GitHub issue with bizarre workaround
- **Memory Impact**: Massive reduction in rows read (16M → 6M for Graduate queries)
- **Speed Improvement**: 2x faster on average (though fast already due to in-memory operation)
- **Query Unification**: Previously separate Kitchen and Mint details queries now unified
- **Search Query**: Must verify returns same results before PR submission
- **Martin Note**: Might save conceptual insights for future projects using ClickHouse

### Wallet Manager Fixes
- **Holding Amount**: Was showing Invested instead of correct holding value
- **Token Selector**: Data duplication bug (discussed with Martin, now fixed)
- **Sell-All Spinner**: Fixed infinite propagation when transaction fails (now has fallback)
- **Button Disable**: Sell-all button disabled during brief period post-transaction before row disappears
- **Stroke Issue**: Some table rows have stroke bottom not in design (Santiago identified)

### Fee Wallet Production Funding
- **Context**: Dev wallets changed, transactions failing without proper funding
- **Issue**: Wallet not created on blockchain, rent exceeds transfer amount (0.0015 SOL transfers)
- **Dev Fix**: Esteban funded in dev, now working
- **Production Need**: Must fund both wallets:
  1. Hyper Liquid admin wallet
  2. Referral wallet
- **Lucas Offer**: Will send arbitrary 2 SOL to each production wallet
- **Federico**: Will pass public addresses for funding

### Filters Implementation Status
- **Working**: All filters except Jupiter-related (as agreed to exclude)
- **Special View**: Santi's design with lines
- **Normal View**: Three icons
- **Testing**: Lucas to verify functionality
- **Order History**: One bug remains (data present, not displaying)

## Technical Highlights

### ClickHouse Template Optimization
- **Technique**: Prevents re-reading filtered data on subsequent left joins
- **Source**: 2023 GitHub issue workaround (described as "bizarre")
- **Kitchen Query**: Unified with Mint details (previously separate despite similarity)
- **Graduate Column**: 16M → 6M rows read (62.5% reduction)
- **Web App Performance**: Noticeable improvement
- **ClickHouse Consumption**: Significant resource reduction (welcomed improvement)
- **Queries Modified**: Details, Search, Kitchen (graduated), Kitchen (non-graduated)

### Transaction Microservice Deployment
- **Saturday Morning**: DNS deployed, unblocked deployment
- **Queue Configuration**: Required morning coupling work (misaligned queue references)
- **Testing Method**: Swagger backend endpoint testing
- **Integration**: Fee system now working with Federico's multi-referral
- **Bugs Fixed**: Max balance transfer, duplicates, fee charging
- **Remaining Issue**: Confirmation polling not reaching frontend

### Security Validator Iteration
- **Status**: Ready to use as-is
- **Approach**: Iterative development (not super validator immediately)
- **Rationale**: Unknown if Eco survives long-term (like other providers Cooking has used)
- **Initial Checks**: Parameter validation of calls, incrementally increase complexity
- **Martin Plan**: Generalize for all providers (not just Eco) - trust in Jupiter/SDKs but can be exploited
- **Performance**: Static validator, no latency impact

### Transaction Confirmation Polling Logic
- **Mechanism**: External ID added to pending queue, batch method processes
- **Batch Response**: Returns only found transactions (can return empty)
- **Problem**: External ID never reaches confirmed status
- **Testing**: Esteban testing via Swagger - never encountered error
- **Frontend Issue**: Suspected patching problem in frontend batch handling
- **First Operation**: Added correctly to batch
- **Second Operation**: Not added correctly
- **Martin**: Will investigate frontend batch implementation

### Referral System Verification
- **Test Scenario**: User creates referral code, referred user makes swaps
- **Fee Distribution**: Primary user receives fee from referred user's operations
- **Claiming**: Successfully claimed fees
- **Transaction Failures**: Many failures due to low balance + mint creation cost
- **Insight**: When user has very low balance and no mint created, mint creation cost causes transaction failure

## Action Items

### Critical (Next Hour - Pre-Meeting)
- [ ] **Martin**: Investigate frontend transaction polling batch implementation
- [ ] **Esteban**: Review backend transaction confirmation external ID handling
- [ ] **Martin & Esteban**: Resolve transaction confirmation notification issue before 11 AM client meeting
- [ ] **Byron**: Complete iOS navigation fixes, submit PR

### Today
- [ ] **Darío**: Verify Search query returns same results with template changes
- [ ] **Darío**: Submit PR for ClickHouse query template optimization
- [ ] **Darío**: Create separate HTTP user for ClickHouse (duplicate backend user)
- [ ] **Eduardo**: Run ClickHouse production migrations (or coordinate with team)
- [ ] **Eduardo**: Continue Radium completion review
- [ ] **Eduardo**: Deliver Meteora integration estimate by midday
- [ ] **Federico**: Generate 2 new wallet IDs and save for future reference
- [ ] **Federico**: Pass production wallet public addresses to Lucas for funding
- [ ] **Lucas**: Fund production Hyper Liquid and referral wallets (2 SOL each)
- [ ] **German**: Safari compatibility review (typography weight, alignment)
- [ ] **Luis**: Focus exclusively on Prefi settings refactor
- [ ] **Marko**: Investigate stuck toast behavior (inconsistent dismiss timing)
- [ ] **Marko**: Fix Top 10 trader icon size inconsistency
- [ ] **Martin Lecam**: Complete metadata work owed to Martin
- [ ] **Javier**: Test afternoon transactions to verify inner swap fix
- [ ] **Javier**: Coordinate stress testing timing with Federico
- [ ] **Esteban**: Complete balance verification feature
- [ ] **Esteban**: Remove stack from error mapping

### Strategic
- [ ] **Darío**: Document ClickHouse conceptual insights and fundamental tips for future projects
- [ ] **Martin**: Decide on ClickHouse migration execution (Eduardo vs team)
- [ ] **Martin**: Review Order History display bug (data present, not rendering)
- [ ] **Eduardo**: Review Javier's wallet case for inner transaction display
- [ ] **Eduardo**: Investigate Invested amount showing zero issue
- [ ] **Team**: Prepare for staged production deployment (ClickHouse → Indexer → Backend/Frontend)

## Important Notes

### Internal Delivery Target - Wednesday
- **Official Deadline**: Friday
- **Internal Goal**: Wednesday completion
- **Rationale**: Avoid weekend on-call work if issues arise from Friday launch
- **Current Status**: Too many fixes remaining for immediate post-daily deployment
- **Revised Plan**: Deploy when stable, likely Thursday

### Client Meeting Context
- **Time**: 11 AM
- **Purpose**: Demonstrate transaction engine improvements
- **Critical Need**: Transaction confirmation visibility
- **Current State**: Backend resolves in 350ms average (Quick Operation V2)
- **Problem**: Notifications not appearing for client demonstration
- **Backup Plan**: Lucas can show inspector if notification fix incomplete

### ClickHouse Optimization Impact
- **Memory**: 5x reduction in rows read for critical queries
- **Speed**: 2x average performance improvement
- **Resource Consumption**: Significant reduction (important for scaling)
- **Query Execution**: Kitchen queries frequently executed, optimization meaningful
- **Web App**: Noticeable performance improvement expected

### Transaction Issues Resolved
- **Market Orders**: Buy and sell working (no more triple execution)
- **TWAP**: Working perfectly
- **Max Balance Transfer**: Fixed
- **Duplicate Transactions**: Fixed
- **Fee Charging**: Fixed (was charging platform, now charges user correctly)

### Transaction Issues Remaining
- **Confirmation Polling**: External ID not reaching confirmed state in frontend
- **Inner Swap Display**: Wrong token names in Wallet History (fix deployed yesterday, needs verification)
- **Invested Amount**: Showing zero for some operations

### Wallet Funding Critical Path
- **Dev Issue**: Wallet not created on blockchain caused all swap failures
- **Root Cause**: Rent cost exceeded tiny SOL transfers (0.0015 SOL)
- **Recommendation**: Always create and fund fee wallet before deployment
- **Production Checklist**:
  1. Create wallet on blockchain
  2. Fund with sufficient SOL for rent
  3. Applies to: Hyper Liquid admin wallet, referral wallet

### Solana Rent Mechanics
- **Wallet**: Address (number), may or may not have storage chunk
- **SOL Storage**: In wallet account (includes rent)
- **Token Storage**: Separate token account per SPL token (joint table: wallet + token)
- **Rent**: No longer rental, perpetual existence cost
- **USDC Example**: Needs separate account (not just wallet account)
- **Wrapped SOL**: SPL token, needs separate account

### Error Mapping Strategy
- **Custom Program Error**: Insufficient liquidity in pool not well-communicated to user
- **Occurred In**: Confirmation worker (transaction sent, not confirmed, generic error mapped)
- **Esteban Plan**: Robustly map errors for clearer user communication
- **Limitation**: Impossible to map ALL blockchain errors comprehensively
- **Approach**: Iteratively improve mapping coverage

### Testing Priorities
- **Javier**: Market orders, TWAP, Wallet History inner swaps, invested amount display, limit orders
- **German**: Safari compatibility across all screens
- **Luis**: Prefi settings refactor completion
- **Santiago**: Continue testing, document design patterns for future reference
- **Marko**: Toast behavior, Top 10 trader icon, general frontend bugs

### Production Deployment Readiness
- **ClickHouse**: Ready (Darío's optimization, Eduardo's migrations)
- **Indexer**: Awaiting ClickHouse completion
- **Transaction Microservice**: Deployed to dev, tested via Swagger, needs production deployment tomorrow
- **Frontend**: Several fixes in progress, stabilization ongoing
- **Backend**: Fee wallet funding pending, otherwise ready

### Design Documentation
- **Santiago Initiative**: Documenting how design is being implemented for future reference
- **Tables**: Some rows have stroke bottom not in design (minor issue)
- **Process**: Good practice for maintaining design consistency

### Staged Deployment Benefits
- **Risk Mitigation**: Each component deployed and verified before next
- **Rollback Capability**: Can revert specific component if issues arise
- **Testing**: Validate each layer before adding complexity
- **Order**: ClickHouse (data) → Indexer (data processing) → Backend/Frontend (presentation)
