---
title: Daily Standup - 2025-10-17
type: meeting
meeting_type: daily_standup
date: 2025-10-17
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** October 17, 2025 (Friday - Launch Day)
**Duration:** 1:01:16
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

**Launch Day Success**: Client internal testing begins Monday with 5 users. If no critical issues discovered, closed beta with 30-40 whitelist users starts October 27. Major breakthrough: transactions now complete in stable 3 seconds (down from 5-6 seconds), confirmed notifications working correctly. Extensive client meeting demonstrated dev version with transaction logs showing 3-second completion times - client impressed and satisfied. Martin fixed critical refresh token cookie issue by switching from Axios to Fetch for specific endpoint. ClickHouse query template optimization deployed showing 2x performance improvement. Team coordinating comprehensive stress testing plan. Lucas emphasized frontend polish priority for immediate client impact. Luis lost money on Hyper Liquid longs, entire team sympathizes with crypto trading pain.

## Team Updates

### Martin Aranda (Technical Lead)
- **Refresh Token Crisis Resolved**: Fixed critical authentication bug
- **Root Cause**: Development token expires in 1 day, production in 1 minute (now 10 minutes - more reasonable)
- **Cookie Behavior**: Cookie not setting on login, mysteriously appeared after expiration and kickout
- **Solution**: Changed specific endpoint from Axios to Fetch - Axios not sending credentials properly
- **Reproducibility**: Occurring in both Chrome and Safari
- **Transfer Token Bug**: Fixed lookup issue - now searches by user ID first (previously found first match regardless of user)
- **Context**: Marco, Martin, Javier all imported same wallet causing collision
- **Metadata**: Will address when has time
- **Transaction Errors**: Working through error mapping improvements

### Luis Rivera (Frontend Developer)
- **Yesterday Afternoon**: Attacked numerous bugs and tickets
- **Evening**: Internet outage, couldn't work, stayed up recovering lost hours
- **Perpetuals Trading**: Lost money on Bitcoin long (classic hubris - understood market perfectly for 3 seconds, then crashed)
- **Positions Carousel**: Working on replicating reported issue
- **Bar Chart Issue**: Reported to Martin - needs endpoint hit more frequently per second
- **Friday Hours**: Asked to split hours between Saturday and Sunday (Lucas approved)
- **Company Library Alignment**: Found many bugs, will self-assign C5 range tickets
- **Advanced Orders**: Completed after extensive reviews
- **Learn More Modals**: Updated information
- **Assignment**: Focus exclusively on Prefi settings refactor (German handling other fixes)

### Marko Jauregui (Frontend Developer)
- **Referral Registration Page**: Almost finished new intro page to referral program
- **Final Review**: Will compare against Figma for perfection
- **Availability**: Ready for frontend bug fixes after referral page complete
- **Toasts**: Investigating stuck toast behavior (some dismiss in 3 seconds, others stay indefinitely)
- **Top 10 Trader Icon**: Addressing size inconsistency issue

### Federico Caffaro (Backend Developer)
- **Hyper Liquid Observables**: Merged with exponential backoff retry for reconnection
- **Stress Testing Planning**: Met with Javier to coordinate comprehensive test
- **Test Scope**:
  - User and wallet creation
  - Orders from multiple wallets with all providers (Jupiter, etc.)
  - Position verification and WebSocket testing
  - Robust referral tree building for load testing
  - Perpetuals testing (Hyper Liquid)
- **Transaction Mocking Question**: Will transactions exclude Solana submission but test providers?
- **Metadata**: To address when able
- **Production Wallets**: Will pass 2 wallet public addresses to Lucas for funding
- **Hyper Liquid Referral**: Lucas to notify when going to production to flag referrals feature and switch to PR
- **Fee Distribution Bug**: Fixed - fees were charged to platform, now charged to user

### Esteban Restrepo (Backend Developer)
- **Timeframes**: Working with Luis on implementation
- **Priority Work Order**:
  1. Timeframes by seconds for charts
  2. Double transaction issue handling
  3. Auto-priority fee implementation (can extend to tomorrow)
- **Configuration Details**:
  - Auto-priority fee: Only swaps (not wallet-to-wallet transfers)
  - Transfers: Very low or hardcoded priority fee
  - Display: Cache Jupiter priority fee for user display
  - Orders: Save configuration at creation time (don't change if user toggles later)
  - Slippage: Default 30%, user-configurable, saved per order at creation
- **Architecture**: Building on base version (not new microservice), using decoupled service for easy migration
- **Notion Update**: Archiving completed transaction optimization and bug tickets per Lucas/Martin guidance
- **Balance Verification**: Implementing for TWAP, DCA, BWAP to check before sending to transaction engine
- **Error Mapping**: Removing stack traces from error responses
- **Referral Testing**: Verified primary user receives fees from referred user operations correctly
- **Transaction Failures**: Many due to very low balance + mint creation cost

### Eduardo Yuschuk (Indexer Developer)
- **Price Filtering**: Improved filter prioritizing reliable sources over Jupiter
- **Jupiter Issue**: Uses arbitrage and "crazy prices", maintains single stable source
- **Strategy**: Use Jupiter only when no higher-confidence sources available
- **Confidence Sources**: Market makers, bonding curves for new tokens
- **Dynamic Approach**: Discover via Jupiter, upgrade to better source when found
- **Precision Debt**: Wants to calculate from post-trade amounts instead of exchange price
- **Token Burning**: Proposed filtering burned tokens (transferred to "incinerator" wallet) from holders list
- **ClickHouse**: Wants to persist changes to repository (avoid losing reference if instance disappears)
- **Total Supply Discrepancies**: Some tokens missing from ClickHouse, Jupiter fallback working as patch
- **Holders Discrepancies**: Some negative values (delta tracking), missing top 10 holders vs Jupiter/Action
- **Explanation**: Unindexed data causes discrepancies (mostly historical gaps, not new tokens)
- **Indexing Latency**: 200ms average concerning (recovery times worsen at 300ms)
- **Postgres Lock Error**: Non-blocking, no data loss, working to resolve without imposing process pauses
- **Eco Validator**: Will improve transaction validator (validate amounts, prevent wallet draining)
- **Price Filter Deployment**: Running improved filter in dev to eliminate scarce liquidity pools and manipulated prices
- **Radium/Meteora**: Reviewing completion requirements, will have estimate by midday
- **Solana Rent**: Explained mechanics - perpetual storage cost for wallets and token accounts

### Darío Balmaceda (Infrastructure)
- **Query Template Changes**: Kitchen and Mint templates implemented, functioning well
- **Performance**: 2x average speed improvement (honestly not sure effort was worth it, but done now)
- **Logic Unification**: Better to have unified logic vs separate queries for future expansion
- **ClickHouse Recovery**: Restored from backup (data gap), portfolio queries much faster, better scaling
- **Two-Client Plan**: Creating separate ClickHouse clients with different configurations:
  - API client: Higher priority, more CPU
  - Cron jobs client: Lower priority, less CPU
- **Implementation**: Different users with separate priority settings, backward compatible (undefined variables default to original)
- **Password Rotation**: Needs to add for ClickHouse (similar to RDS)
- **Production Deployment**: Asked about timing - Lucas prefers showing dev state first, then push late afternoon/tomorrow
- **User Priorization**: Currently disabled (not hitting resource limits), can enable if needed
- **HTTP User**: Will create separate user for differentiating cron vs user queries

### Byron Chavarria (Mobile Developer)
- **iOS Navigation**: Finally resolved iOS 16 and 18.3 navigation issues
- **Token Details**: Continuing final information details work
- **TestFlight**: Will publish version when ready, send to Lucas
- **L-Ramper**: Finalizing integration in application
- **Range Selector**: Question about decimal values 0-1 or different format (Martin will investigate)
- **Apple Account**: Tested successfully, logged in Xcode and browser
- **Schemas**: Preparing three schemas (production, UAT, development), will complete today
- **Limit Order Creation**: Finishing limit order creation work

### Javier Grajales (QA/Testing)
- **Market Orders**: Buy and sell functioning correctly
- **TWAP**: Working well
- **Wallet Classification**: Tested successfully
- **Diamond Hands**: Definition now compares unrealized PNL (instead of PNL) - ticket created
- **Manual Comparison**: Slot matching working well (creator slot, next 10 buyers, developer label all correct)
- **Top Holder Percentage**: Didn't notice error Lucas reported
- **Holders Issues**:
  - Incinerator appearing in list (Eduardo addressing)
  - Zero-amount holders appearing (needs filtering)
- **Chart Issues**: Reported several to Luis
- **Test Funding**: Needs funds for testing (Lucas offered immediate transfer)
- **Stress Testing**: Ready to coordinate with Federico
- **Apache AB**: Planning concurrency testing
- **Wallet History**: Inner transactions showing wrong token names resolved (per Eduardo's midday fix)
- **Token Transfer Sale**: Failure case - needs Eduardo to review wallet privately
- **Holding Amount**: Definition changes needed for token details display
- **Number Standard**: UI adjustment needed to prevent excessively long numbers

### Santiago Gimenez (Backend/Frontend Developer)
- **Testing**: Portfolio and purchase testing
- **Notion Tasks**: Nearly all complete
- **Issue Reporting**: Raising all discovered problems
- **Tables**: Some have stroke bottom not in design (minor discrepancy)
- **Design Documentation**: Creating design implementation documentation for future reference

### German Derbes Catoni (Frontend Developer)
- **Assignment**: Safari compatibility (typography weight, alignment)
- **Login Review**: Reviewing login page for client
- **Status**: Will begin Safari comparison work

### Lucas Cufré (Project Lead)
- **Client Meeting**: Long session to address Eco architectural incompatibilities
- **Eco Issues**: Fundamental incompatibility between Cooking and Eco architectures, conceptually irreconcilable
- **Client Push**: Sain very insistent on using Eco for launch
- **Demo Success**: Showed dev version, transactions completing in stable 3 seconds
- **Transaction Evidence**: Opened inspector to show response times, logs demonstrating 3-second completion
- **Client Reaction**: Impressed and reassured, stopped pushing for Eco integration
- **Eco Decision**: Not launching with Eco due to architectural incompatibility (requires development on both sides)
- **Team Recognition**: "Tremendous work," acknowledged exceptional effort everyone putting in
- **Launch Timeline**:
  - Monday: 5 client internal users begin testing
  - October 27: Closed beta with 30-40 whitelist users (if no catastrophic issues)
  - Whitelist: Will remain enabled (closed beta approach)
- **Next Quarter**: Begin architecture hardening for scalability, indexer improvements, contract completion, price series separation
- **Marketing**: Planned "fulera" (intense) campaign for full launch
- **Frontend Priority**: Resolve maximum frontend issues (highest immediate impact area)
- **Mobile Work**: Significant UI updates coming from client (Byron has "a ton of work ahead")
- **Sain Context**: Person who pays, highest business authority
- **Ris Context**: Product vision holder, working with external design agency
- **Greg & Nashi**: Trader (finance titles) and marketing person (constant contact)

## Key Discussion Topics

### Launch Strategy - Closed Beta via Whitelist
- **Not Friends and Family**: Closed beta with whitelist-only access
- **Access Control**: cooking.com/login won't work without referral code
- **Viral Mechanism**: Referred users can generate own codes, expanding access organically
- **User Range**: 30-40 initial whitelist users
- **Internal First**: 5 client team members testing Monday
- **Gate**: No catastrophic issues during week → beta launch October 27
- **Post-Beta**: Iterative feedback loop, feature additions, improvements
- **Q4 Focus**: Architecture hardening, scalability improvements, indexer enhancements

### Transaction Performance Breakthrough
- **Previous**: 5-6 seconds completion time
- **Current**: Stable 3 seconds
- **Confirmation**: Toast notifications appearing correctly, proper timing
- **Demo Impact**: Lucas showed inspector with transaction logs proving 3-second completion
- **Client Satisfaction**: "Made the night and day difference"
- **Alternative Scenario**: Without this improvement, client would continue demanding Eco integration
- **Fallback System**: Security checking in backend without extra latency impressed client
- **Commitment Met**: Team delivered everything promised

### Eco Architectural Incompatibility
- **Fundamental Issues**: Conceptual differences preventing reconciliation
- **Development Need**: Requires work from both Cooking and Eco teams
- **Client Understanding**: Accepted that incompatibility is architectural, not implementation quality
- **Alternative Path**: Client was pushing hard for Eco before seeing current performance
- **Resolution**: Demonstrating 3-second stable transactions satisfied client without Eco

### Refresh Token Cookie Mystery Solved
- **Dev Token**: Expires in 1 day
- **Prod Token**: Was expiring in 1 minute (updated to 10 minutes - more reasonable)
- **Weird Behavior**: Cookie not setting on login, suddenly appearing after expiration
- **Browser Scope**: Occurring in both Chrome and Safari
- **HTTP Only Cookie**: Changed for security (more secure approach)
- **Domain Setting**: Added domain restriction for cookie registration
- **Path & Settings**: All correct configurations
- **The Mystery**: Cookie only appears in application storage AFTER initial failure
- **Solution**: Switching from Axios to Fetch for specific endpoint resolved issue
- **Root Cause**: Axios credential handling problem
- **Manual Refresh**: After kickout, manual refresh call works perfectly (cookie already stored)

### Balance Verification Logic
- **Problem**: Noise in transaction database from failed insufficient balance attempts
- **Current**: Transactions sent to engine even without sufficient balance
- **Proposal**: Verify balance before sending to transaction microservice
- **Benefits**: Less unnecessary backend load, cleaner database (fewer failed states)
- **Scope**: TWAP, DCA, BWAP orders
- **User Communication Challenge**:
  - Can't cancel entire order (user might refund wallet)
  - Should skip this iteration, keep order active
  - No notification system yet (no notification center, Telegram bot, etc.)
- **Decision**: Mark iteration as failed (insufficient balance), don't send to transaction engine, display in table as failed
- **Standard Approach**: Common pattern in many products to show failed iterations

### Liquidity Pool Validation Discussion
- **Question**: Can we validate pool liquidity before submitting transaction? (similar to balance check)
- **Use Case**: Prevent "custom program error: insufficient liquidity" failures
- **Eduardo Response**: Information exists, could query via Jupiter API or similar
- **Latency Concern**: Extra API call adds delay (contradicts fast transaction goal)
- **Long-term Solution**: Index pool information (like competitors do for Orca, Meteora)
- **Eduardo Emphasis**: "To compete, you have to index this. I don't see a path for the application if we don't eventually index that."
- **Current**: Error occurs during confirmation worker (transaction sent, not confirmed, generic error)
- **Improvement**: Better error mapping for clearer user communication
- **Retry Limitation**: System only retries when RPC rejects immediately, not during node processing

### Price Source Prioritization Strategy
- **Current Problem**: Jupiter using arbitrage, "crazy prices", no predictability
- **Tier 1**: Market makers, bonding curves (highest confidence)
- **Tier 2**: Direct protocol prices
- **Tier 3**: Jupiter aggregator (fallback only)
- **Dynamic Upgrading**: Start with available source, upgrade when better discovered
- **Filtering Goal**: Eliminate scarce liquidity pools, manipulated prices
- **Chart Quality**: Prevent outliers creating band patterns instead of lines
- **Lucas Context**: Sain pushing to reverse-engineer Eco mechanics
- **Eco Approach**: Works low-level, only indexes needed information
- **Future Path**: Opening compatibility to more providers improves router (Cooking's router, not Jupiter)
- **Indexer Architecture**: Leveling up could reduce Jupiter dependency
- **Competitive Strategy**: Could potentially compete with Jupiter if indexer improved sufficiently

### Stress Testing Coordination
- **Federico & Javier**: Planning comprehensive load testing
- **Test Components**:
  - User creation (mass endpoint, skips providers, creates wallets)
  - Wallet creation (multiple per user)
  - Order placement (multiple wallets, multiple providers)
  - Position verification (calculations correctness)
  - WebSocket testing (real-time position updates)
  - Referral tree (multi-level tree to test loading performance)
  - Perpetuals (Hyper Liquid integration)
- **Transaction Mocking**: Configured to skip blockchain submission, test provider interaction
- **Environment**: Dev during low-usage periods
- **Method**: Apache AB for concurrency, custom scripts for specific scenarios
- **Endpoints Ready**: Quick operations and other endpoints ready for testing

### Token Account Creation Cost Issues
- **Javier Case**: Multiple charges for token account despite previous ownership
- **Pattern**: Buy Pengu → Sell all → Buy again → Sell all → Extra costs
- **Hypothesis**: Close account on complete sell, must reopen on repurchase
- **Solscan Verification**: Check for "close account" transaction
- **Rent Reclaim**: Platform might recover rent when closing account
- **Reopen Cost**: Must pay rent again to reopen account
- **Complex Transaction**: Eduardo identified two temporary token accounts created
- **Protocol Layering**: Multiple protocol integration creating inefficiencies
- **Cost Impact**: Affects minimum token amounts required to initiate operations
- **Eduardo Analysis**: Transaction "really complicated," not optimally efficient

## Technical Highlights

### ClickHouse Query Template Optimization Impact
- **Performance**: 2x average speed improvement
- **Logic**: Unified previously separate Kitchen and Mint details queries
- **Memory**: 5x reduction in rows read (16M → 6M for Graduate queries)
- **Darío Honesty**: "Honestly not sure effort was worth it, but done and good to have unified"
- **Future Benefit**: Easier to expand unified logic vs maintaining separate queries
- **Recovery**: Portfolio queries much faster post-backup recovery, better long-term scaling architecture

### Two-Client ClickHouse Architecture
- **Purpose**: Separate API traffic from cron job traffic
- **API Client**: Higher priority, more CPU allocation
- **Cron Client**: Lower priority, less CPU
- **Implementation**: Different users with separate priority configuration
- **Backward Compatibility**: Undefined variables default to original single client
- **Monitoring**: Can differentiate query volume between cron jobs and users
- **Priority Control**: Currently disabled (not hitting limits), can enable if needed

### Transaction Configuration Immutability
- **Auto-Priority Fee**: Saved at order creation, doesn't change if user toggles setting later
- **Slippage**: Saved at order creation, default 30%, user-configurable
- **Rationale**: Prevent confusing asynchronous changes to existing orders
- **Swap vs Transfer**: Transfers use hardcoded low priority, swaps use user configuration
- **Display**: Cache Jupiter priority fee response for user visualization
- **Refresh**: Per transaction, not continuous (latency acceptable for display)

### Type-Safe API Client Generation
- **Trigger**: Production bug from backend change breaking frontend transfers (no type safety)
- **Solution**: Auto-generates typed API clients for all services
- **Coverage**: Main backend + all microservices
- **Benefit**: Compile-time type checking vs runtime failures
- **Example**: Transfer funds endpoint type change caught immediately
- **Pending**: Decide when to run generation (GitHub actions timing)

### Referral System Architecture
- **Fee Distribution**: Tested and working correctly
- **Verification**: Primary user receives fees from referred user operations
- **Claims**: Successfully tested claim functionality
- **Wallet Funding**: Created test wallet, pending funds for full claim testing (Lucas handling)

### Error Mapping Robustness
- **Insufficient Liquidity**: Custom program error not well-communicated to user
- **Stack Traces**: Esteban removing from error responses (overly detailed for users)
- **Iterative Improvement**: Impossible to map all blockchain errors, continuously expanding coverage
- **Confirmation Worker**: Errors during transaction confirmation need better mapping

### Solana Rent Mechanics Detailed
- **Wallet Account**: Address (number), may/may not have storage
- **SOL Storage**: In wallet account itself
- **Token Storage**: Separate SPL token account per token type (joint table: wallet + token)
- **Rent**: No longer rental, perpetual storage cost
- **USDC Example**: Requires separate token account creation (not just wallet)
- **Wrapped SOL**: SPL token, needs separate account
- **Close Account**: Platform can recover rent when user sells all tokens
- **Reopen Account**: Must pay rent again when repurchasing

## Action Items

### Critical (Today)
- [ ] **Byron**: Publish TestFlight version when ready, send to Lucas
- [ ] **Martin**: Address metadata request when able
- [ ] **Federico**: Pass 2 production wallet public addresses to Lucas for funding
- [ ] **Lucas**: Fund production wallets (Hyper Liquid and referral)
- [ ] **Luis**: Focus on Prefi settings refactor
- [ ] **German**: Safari login compatibility (typography, alignment)
- [ ] **Marko**: Review referral registration page against Figma, fix toast stuck behavior

### This Week
- [ ] **Esteban**: Remove stack traces from error mapping
- [ ] **Esteban**: Complete balance verification for TWAP/DCA/BWAP
- [ ] **Martin**: Investigate range selector value format for Byron
- [ ] **Federico & Javier**: Execute comprehensive stress testing plan
- [ ] **Eduardo**: Provide Meteora integration estimate by midday
- [ ] **Darío**: Deploy ClickHouse query template optimization to production (after Lucas reviews dev)
- [ ] **Javier**: Pass wallet to Eduardo privately for complex transaction analysis
- [ ] **Lucas**: Send number standard specification for UI adjustment
- [ ] **Team**: Archive completed transaction optimization and bug tickets

### Strategic
- [ ] **Eduardo**: Persist ClickHouse changes to indexer repository
- [ ] **Eduardo**: Implement improved price filtering in dev for review
- [ ] **Eduardo**: Continue Eco validator improvements (amount validation, wallet draining prevention)
- [ ] **Team**: Plan Q4 architecture hardening roadmap
- [ ] **Team**: Prioritize indexer improvements (contracts, price series separation)
- [ ] **Team**: Schedule production deployment after dev demonstration

## Important Notes

### Launch Day Celebration
- **Martin Recognition**: "I want to thank you all for all the effort you're putting in. I know today is a holiday and you're all working. I know tomorrow is Saturday and you're going to work it and I'm very grateful with you all that you're holding on so we can deliver and come out on time."
- **Lucas Response**: "Completely agree. I promise we'll make it more comfortable, calmer from here on. I believe it's public knowledge the titanic work we've put in these last months. It's a Pareto of s***. The last 20% costs a barbaric amount."
- **Team Achievement**: Delivered everything promised despite architectural challenges
- **Client Satisfaction**: Impressed with 3-second transaction performance, stopped pushing Eco integration

### Beta Launch Parameters
- **Monday Internal**: 5 client team members (Sain, Ris, Greg, Nashi, +1)
- **October 27 Closed Beta**: 30-40 whitelist users
- **Access Model**: Referral code required (no direct login)
- **Viral Growth**: Referred users generate codes, organic expansion
- **Gate Condition**: No catastrophic issues during internal testing week
- **Post-Launch**: Feedback iteration, feature additions, improvements

### Client Personas
- **Sain**: Pays the bills, highest business authority, very pushy on Eco
- **Ris**: Product vision, working with external design agency, reviews UI before team testing
- **Greg**: Trader with finance background, technical user perspective
- **Nashi**: Marketing person, growth strategy
- **External Design Agency**: "Pixel perfect" review causing intensive late-stage changes

### Crypto Trading Sympathy
- **Luis**: Lost money on Hyper Liquid Bitcoin long ("understood market perfectly for 3 seconds")
- **Lucas**: Lost $XXX last week (shorts on Bitcoin/Ethereum, had profit, then crashed)
- **Market Observation**: 2 billion in liquidations since yesterday (European news trigger)
- **Consensus**: "Trading perpetuals is closest thing to casino gambling"
- **Luis Joke**: "If it hits 104k I'm longing again. Don't care if I get liquidated."

### Frontend Priority Rationale
- **Lucas**: "Resolve maximum frontend issues - highest immediate impact area"
- **Client Feedback**: Design agency pixel-perfect review generating most issues
- **User Experience**: Visual polish more immediately noticeable than backend improvements
- **Testing Division**: Javier on functionality, Santiago on design QA

### Mobile Work Incoming
- **Client Presentation**: Showed Mobile UI updates in yesterday's meeting
- **Byron Impact**: "Byron, the other day you asked if we had work - we have a ton of work ahead"
- **L-Ramper**: Finalizing integration
- **TestFlight**: Ready for client testing once published
- **Schemas**: Three environments (production, UAT, development)

### Transaction Performance Context
- **Previous State**: 5-6 seconds, unreliable confirmations
- **Current State**: Stable 3 seconds, confirmations working
- **Demo Evidence**: Inspector showing transaction logs with timestamps
- **Client Requirement**: Visual proof of speed (not just claims)
- **Fallback Proof**: Backend security checking without latency
- **Alternative**: Without this, client would keep demanding Eco despite incompatibility

### ClickHouse Recovery Learnings
- **Backup Restore**: Lost data gap during recovery
- **Performance**: Dramatically improved post-recovery
- **Scaling**: Better long-term architecture characteristics
- **Cost Strategy**: "Keep throwing money at problem until optimized"
- **Monitoring**: CPU elevated (16-17 of 30) but stable
- **Cache**: 99% hit rate with gigabytes of RAM

### Balance Verification Philosophy
- **Goal**: Prevent unnecessary transaction engine load
- **Approach**: Check before sending, not during processing
- **User Experience**: Show failed iterations in table (standard pattern)
- **Communication Gap**: No notification system yet (notification center, Telegram bot)
- **Future State**: When notification system exists, can alert user proactively
- **Current**: User sees failed status in order history table

### Pool Liquidity Validation Complexity
- **Information**: Exists and queryable (Jupiter API, etc.)
- **Latency**: Extra API call adds delay (contradicts fast transaction goal)
- **Long-term**: Need to index pool data (like competitors Orca, Meteora, etc.)
- **Eduardo Position**: "To compete, you have to index this. I don't see a path for the application if we don't eventually index that."
- **Current Workaround**: Better error mapping when liquidity insufficient
- **Limitation**: System doesn't retry when transaction processes but fails (only when RPC rejects immediately)

### Q4 Roadmap Preview
- **Not Completing**: Lucas realistic about timeframe ("I don't say we'll close it")
- **Begin Work**: Start architecture hardening systematically
- **Prioritization**: Where to start, what impact, how to advance
- **Focus Areas**: Indexer improvements, contract completion, price series separation
- **Scaling**: Prepare for growth from 30-40 to larger user base
- **Marketing**: Full launch will have "fulera" (intense/significant) campaign

### Wallet Account Complexity
- **Close Account**: Platform recovers rent when user sells all tokens
- **Reopen Cost**: Must pay rent again when repurchasing
- **Efficiency**: Multi-protocol integration creating layered inefficiency
- **Cost Impact**: Affects minimum amounts needed to open positions
- **User Education**: Complex mechanics not transparent to average user
- **Eduardo Analysis**: Transaction "really complicated," shows protocol layering issues

### Number Display Standard
- **Issue**: Token amounts too long in UI
- **Holding Amount**: Definition changes needed for token details
- **Lucas Owes**: Number standard specification for consistent formatting
- **Purpose**: Prevent excessively long number strings, improve readability
- **Javier Question**: "Me equivoco?" (Am I wrong?) - Lucas confirms owes specification

### Testing Accounts and Funding
- **Source**: Using Raider account (Team Cook discontinued)
- **Javier Need**: Immediate funds for testing
- **Lucas Response**: Direct transfer from personal account
- **Production**: Federico passing wallet addresses for funding
- **Amount**: Lucas offering "arbitrary 2 SOL" per wallet

### Stress Testing Readiness
- **Branch**: Federico created test branch with mass user creation endpoint
- **Mocking**: Transactions skip blockchain submission, test provider interaction
- **Coordination**: Javier and Federico planning timing
- **Method**: Apache AB for load, scripts for scenarios
- **Environment**: Dev during off-hours
