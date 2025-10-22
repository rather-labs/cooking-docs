---
title: Daily Standup - 2025-10-03
type: meeting
meeting_type: daily_standup
date: 2025-10-03
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** October 3, 2025
**Duration:** 47:07
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

Critical client demo preparation day with focus on stabilizing development environment for video recording. Team successfully resolved position update issues - now updating in under 5 minutes with temporary double-counting at purchase that normalizes quickly. Martin implemented "final" clause solution reducing position query time to 12 seconds. German completed major Wallet Manager improvements and limit order field validations. Esteban clarified auto-priority fee and slippage configuration requirements. ClickHouse challenges dominated technical discussions, with Eduardo and Martin troubleshooting replication delays and data migration strategies. Team confirmed stable version ready for production deployment pending Javier's final testing approval.

## Team Updates

### German Derbes Catoni (Frontend Developer)
- Fixed multiple bugs and improved Wallet Manager table (switch button, skeleton loader)
- Enhanced limit order input validations and field conversions
- Changed slider to allow any percentage (not just stepped values)
- Fixed upward switch not updating amount issue
- Resolved transaction continuation issue (preventing multiple submissions)
- Working on limit order input field refinements per Lucas feedback
- Will review Home, Kitchen, Login for video or continue with Orders updates

### Luis Rivera (Frontend Developer)
- Completed chart functionality with different timeframes using Esteban's service
- Added carousel for positions display
- Fixed token image display issues (was showing default instead of placeholder when no image)
- Corrected hardcoded amounts to follow header switch (SOL/USD)
- Made hover-triggered carousel fix as requested by Lucas
- Identified glitch: carousel resets on mouse-over
- Supporting German by taking over tickets

### Marko Jauregui (Frontend Developer)
- Fixed multiple frontend bugs
- Implemented Kitchen badges (sniper, top 10)
- Will implement badge tooltips
- Consulting with Juli about scroll implementation
- Ready to support wherever needed

### Federico Caffaro & Martin Lecam (Backend - Referrals)
- Completed referral system frontend integration
- Tested volume calculations updating correctly across different levels
- System working well in testing
- Referrals module is decoupled, facilitating testing and integration
- Wallet created for testing claims (pending funding for full claim testing)

### Esteban Restrepo (Backend Developer - Transactions)
- Working with Luis on timeframes implementation
- Confirmed auto-priority fee and slippage configuration requirements
- **Auto-Priority Fee Strategy**:
  - Only applies to swaps, not wallet-to-wallet transfers
  - Transfers use very low/hardcoded priority fee
  - Cache priority fee from Jupiter to display to users
  - Orders save user configuration at creation time (don't change if user toggles later)
- **Slippage**: Default 30%, configurable per user, saved per order at creation
- Building on base version (not new microservice yet)
- Using decoupled service for easy migration later

### Eduardo Yuschuk (Indexer Developer)
- Struggled with ClickHouse challenges and replication issues
- Key learnings: Load testing must be done in near-production scenarios
- Emphasized importance of replica timing and query structure
- Concerned about partitioned queries potentially reading all partitions
- Explained position amount duplication problem (purchases reflected multiple times inconsistently)

### Darío Balmaceda (Infrastructure)
- Working on Membr migration
- Optimizing queries to eliminate need for "final" clause
- Discussed ClickHouse migration strategy for historical data
- Available to collaborate on performance improvements

### Javier Grajales (QA/Testing)
- Testing back and forth on various tickets
- Successfully tested positions update in under 5 minutes (duplicated initially, then normalized)
- Reported ClickHouse issues in logs
- Found DCA/Limit history black screen issue (tokens without metadata) - now fixed to show tokens without info
- Raised question about SOL/USD conversion in limit order input amount field
- Identified imported wallet transaction signing issues (format incompatibility)
- Will continue testing and raise Luis ticket for token display issue

### Byron Chavarria (Mobile Developer)
- Finalizing L-Ramper integration in application
- Planning testing phase
- Needs test account for mobile device testing
- Raised question about pentest for transactional security verification
- Suggested including SSL pinning in application to prevent man-in-the-middle attacks
- Waiting on client account access

### Santiago Gimenez (Backend Developer)
- Started work on token watchlist feature
- Anticipating changes to multiple components
- Focusing on backend logic first, then frontend

### Martin Aranda (Technical Lead)
- Resolved transaction signing issues with imported wallets (works for Martin, not for Lucas)
- Identified wallet format incompatibility: Solflare exports numeric format (Uint8), platform expects hexadecimal
- Phantom uses Base58, Metamask uses Hex, Solflare uses Uint8
- Implemented "final" clause in position queries, reducing update time to 12 seconds
- First position load without "final" for fast initial data, subsequent updates use "final" for accuracy
- Proposed external audit for pentest security verification
- Confirmed prioritization: resolve imported wallet issues later (not critical for launch)

## Key Discussion Topics

### Client Video Demo Requirements
- **Critical**: Stable environment needed immediately for client video
- **Client Context**: Team promised "tomorrow" for over a week
- **Goal**: Ready to receive real users (currently blocked by Eco integration timeline)
- **Test Flow**: Login → Kitchen (filters) → Portfolio → Token Details (Pengu/Farcoin) → Charts → Limit Order
- **Key Metrics**: Portfolio calculations must be accurate, position updates must work

### Position Update Problem Resolution
- **Current State**: Updates in under 5 minutes (previously 5-10 minutes)
- **Behavior**: Initial purchase shows duplicate, normalizes quickly
- **Technical Solution**: Implemented "final" clause in ClickHouse queries
- **Query Time**: 12 seconds with "final" clause
- **Strategy**: First load without "final" (fast), subsequent updates with "final" (accurate)
- **User Experience**: Acceptable 12-second delay considered reasonable by Lucas

### ClickHouse Performance Challenges
- **Data Duplication**: Positions showing 2-4x actual amounts due to replication
- **Root Cause**: Data aggregated directly from partitioned trades
- **Solutions Considered**:
  - Resolve within database engine
  - Use "final" clause (implemented - 12 second queries)
  - Backend merge of duplicate tuples (considered impractical for large result sets)
- **Historical Data Migration**: 4 months of trade history saturated RAM when creating new table
- **Strategy Needed**: Batch migration approach for historical data with timestamp-based incremental loading

### Auto-Priority Fee Configuration
- **Scope**: Only swaps, not wallet-to-wallet transfers
- **User Configuration**: Stored at user level, saved at order creation
- **Order Behavior**: Orders execute with configuration from creation time (don't change if user toggles)
- **Display Strategy**: Cache Jupiter priority fee response, refresh on each transaction
- **Rationale**: Low latency not critical, visualization most important

### Slippage Configuration
- **Default**: 30% for all new users
- **User-Level**: Configurable and stored in user table
- **Order-Level**: Must be saved at order creation time
- **Consistency**: Same pattern as auto-priority fee (snapshot at creation)

### Wallet Import Compatibility
- **Issue**: Different wallet providers export private keys in different formats
- **Formats**:
  - Phantom: Base58
  - Metamask: Hexadecimal
  - Solflare: Uint8 (numeric array)
- **Current Support**: Platform supports 2 of 3 formats (Phantom, Metamask)
- **Decision**: Deprioritize Solflare format support - let users do extra work or export seed phrase

## Technical Highlights

### ClickHouse Optimization
- **Partitioning Strategy**: Tested wallet hash modulo partitioning (32 and 64 partitions)
- **Performance Gain**: 12-14 seconds → ~1 second for partitioned queries
- **Implementation Approach**: Create new table with materialized view, test, rename
- **Query Structure**: Must avoid reading all partitions unnecessarily
- **Replication Timing**: Critical for performance with mass data initialization
- **"Final" Clause Impact**: Ensures data consistency at cost of query time (12 seconds acceptable)

### Transaction Service Design
- **Configuration Storage**: Priority fee and slippage saved at order creation
- **Immutability**: Orders don't change when user modifies global settings
- **Caching**: Jupiter priority fee cached and reused for display
- **Transfer Strategy**: Wallet-to-wallet uses low/hardcoded priority fee
- **Swap Strategy**: Uses auto or manual based on user setting at order creation

### Referral System
- **Status**: Frontend integration complete
- **Testing**: Volume calculations working across multiple levels
- **Architecture**: Decoupled module for easy testing
- **Claims**: Need funded wallet for full testing (wallet created, pending funds)

### Chart Implementation
- **Timeframes**: All timeframes working (1 second to 1 day) using Esteban's service
- **Countback**: Latest update not yet integrated (causes Trading View errors)
- **Performance**: Generally good in local and development environments

### Mobile Security
- **Pentest**: Planned external audit for security verification
- **SSL Pinning**: Byron recommended to prevent man-in-the-middle attacks
- **Test Account**: Blocked waiting for client to provide account access

## Action Items

### Critical (Today)
- [ ] **German**: Review limit order input field per Lucas feedback
- [ ] **German**: Create video recording for Advanced Orders showing limit orders, filters, form, percentages
- [ ] **German**: Option to review Home, Kitchen, Login for video OR continue Orders updates
- [ ] **Luis**: Implement carousel hover fix (currently resets on mouse-over)
- [ ] **Javier**: Test complete position flow with empty wallet
  - Buy Farcoin and Pengu positions
  - Verify portfolio calculations correct in dev
  - Test selling for position updates
  - Close with limit order
- [ ] **Marko**: Implement badge tooltips
- [ ] **Marko**: Consult with Juli about scroll implementation
- [ ] **Marko**: Take additional frontend bugs

### This Week
- [ ] **Federico**: Pass wallet public address to Lucas for referrals testing
- [ ] **Eduardo/Martin**: Collaborate on ClickHouse query optimization
- [ ] **Darío**: Share Membr migration strategy applicable to position_full migration
- [ ] **Martin**: Discuss with Byron about SSL pinning implementation next week
- [ ] **All**: Prepare for production deployment pending Javier's testing approval

### Strategic
- [ ] **Team**: Schedule external pentest security audit
- [ ] **Martin/Darío**: Develop historical data migration strategy for ClickHouse (batch approach)
- [ ] **Team**: Implement Solflare wallet import format support (deprioritized)

## Important Notes

### Demo Readiness
- **Status**: Token details, Kitchen, Login looking good per Lucas
- **Focus**: Limit orders functionality, filters, form, percentage calculations, number display
- **Math Validation**: Lucas and Javi verified calculations are correct
- **Goal**: Record video for client showing Advanced Orders functionality

### Position Updates Behavior
- **Javier's Testing**: Positions updated in under 5 minutes in dev
- **Pattern**: Duplicates at 30 seconds, normalizes for purchase
- **Selling**: Not yet tested
- **Query Strategy**: Fast initial load (no "final"), accurate updates (with "final" - 12 seconds)

### ClickHouse Learnings
- **Load Testing**: Must be done in near-production scenarios (empty database tests misleading)
- **Replication**: Timing critical when mass-initializing data
- **Query Structure**: Must carefully consider partition reads
- **RAM Saturation**: 4 months of historical trades overwhelmed system during migration
- **Solution**: Incremental timestamp-based batch loading for historical data

### Configuration Immutability Decision
- **Rationale**: Changing past orders asynchronously creates user confusion
- **Analogy**: Like changing slippage globally affecting all existing DCA orders
- **Example**: User creates order with auto-priority enabled, later disables - order still executes with auto-priority
- **Implementation**: Store configuration snapshot at order creation time

### Production Deployment Readiness
- **Blocker**: Waiting for Javier's final testing approval
- **Goal**: Stable version ready by end of day
- **Purpose**: Client can begin testing
- **Mobile**: Still blocked on account access from client

### Code Freeze Approach
- **Question Raised**: Will there be a code freeze and demo today?
- **Answer**: Depends on Javier's testing results within next 30 minutes
- **Plan**: If tests pass → freeze → demo → 2 hours for client video → resume work
- **Deployment**: Stable version to production end of day for client testing

### Wallet Import Strategy
- **Supported**: 2 of 3 major formats (Phantom Base58, Metamask Hex)
- **Not Supported**: Solflare Uint8 numeric format
- **Decision**: Users can do conversion work or export seed phrase
- **Political Joke**: "Make a political party in the elections. Stop messing around."
- **Priority**: Mapped as future volume, not blocking launch
