---
title: Daily Standup - 2025-10-01
type: meeting
meeting_type: daily_standup
date: 2025-10-01
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** October 1, 2025
**Duration:** 47:10
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

Launch delayed two weeks to October 15 for Eco router integration - a strategic decision to implement superior transaction routing and MEV protection. Team faced critical Solana byte limit issue causing 50% transaction failure rate, temporarily resolved by removing additional fees. Major focus on stabilizing development environment for client video demo, with specific attention to Pengu and Farcoin token flows. Esteban expressed concerns about integrating 6,000+ lines of transaction service code, leading to decision to postpone microservice deployment until post-Eco integration.

## Team Updates

### Luis Rivera (Frontend Developer)
- Completed all pending Perpetuals tasks
- Assisted German with portfolio P&L chart alignment issue
- Implemented fast/slow withdrawal validation with Federico's endpoint
- Corrected amount validation: fast withdraw uses endpoint check, slow withdraw validates minimum $15
- All tickets closed, ready to support German with additional work

### German Derbes Catoni (Frontend Developer)
- Completed Wallet Manager improvements and modal updates
- Working through Javi's Token Details bug reports
- Adding provider images to header and fixing various page details
- Planning review of orders functionality after recent updates
- Addressing missing links and footer elements

### Marko Jauregui (Frontend Developer)
- Implemented Kitchen badges (sniper, top 10, early trades, insiders)
- Working on badge tooltips
- Fixed various frontend bugs
- Ready to take additional tasks

### Federico Caffaro (Backend Developer)
- Completed withdrawal fix without creating new table - using existing Hyper Liquid endpoint
- Endpoint checks user wallet role; adds $1 fee for first-time users
- Continuing multi-layer referral system development
- Restructuring entities to rebuild user referral tree backwards

### Martin Lecam (Backend Developer)
- Completed time-based history functionality
- Confirming changes for new microservice connections
- Available for additional tasks

### Esteban Restrepo (Backend Developer)
- Worked with Luis on timeframe implementation for charts
- Concerns about integrating 6,000+ lines of transaction code before launch
- Proposed postponing microservice integration for project health
- Focused on: 1) Timeframes by seconds, 2) Double transaction issue, 3) Auto-priority fee
- Transaction service already built, needs integration testing

### Eduardo Yuschuk (Indexer Developer)
- Working through various bug tickets from Javier
- Successfully deployed production environment
- Started Eco integration work
- Needs priority clarification for Eco vs. other tasks

### Byron Chavarria (Mobile Developer)
- Resolved version conflicts between iOS 26 and 18.1
- Finalizing token details screen - awaiting meeting with Lucas and Martin for data clarification
- Continuing advancement on remaining tasks post-meeting

### Santiago Gimenez (Backend Developer)
- Assisting frontend team with various changes
- Starting work on new features: dynamic configuration, portfolio level, token watchlist
- Will develop backend logic first, then frontend
- Dynamic fee feature impacts backoffice for portfolio take profit/stop loss positioning

### Martin Aranda (Technical Lead)
- Jupiter badges (early trades, insiders, snipers) won't work due to missing data
- Fixed critical transaction byte limit issue - 50% of transactions failing
- Had to remove additional fees (Cooking wallet + referral transfers) to stay under Solana's byte limit
- Implemented transaction retry logic with signature control
- Proposed table partitioning for position_full and folder tables using wallet hash for performance improvement
- Moved position queries to more synchronous approach to avoid multiple concurrent queries

### Darío Balmaceda (Infrastructure)
- Proposed comparing prices with competitors for more effective filtering
- Suggested alternative approaches to price anomaly detection

## Key Discussion Topics

### Two-Week Launch Extension
- **New Target**: October 15, 2025 (Wednesday)
- **Reason**: Client requested Eco router integration
- **Benefits**: Superior execution speed and direct contact with Eco development team
- **Impact**: Allows time for thorough testing of transaction microservice

### Eco Router Integration
- Primary router before Jupiter fallback
- Better execution speeds than current Jupiter implementation
- Direct relationship with Eco's development team through existing advisor
- Rate limited, so Jupiter will continue handling significant volume

### Transaction Byte Limit Crisis
- **Issue**: 50% of transactions failing due to Solana byte limit
- **Root Cause**: Jupiter transaction + Cooking wallet transfer + referral transfers exceeded limit
- **Temporary Fix**: Removed additional fee transfers to make transactions work
- **Impact**: Currently not collecting Cooking fees or referral transfers
- **Long-term Solution**: Need to separate fee collection into independent transaction linked to swap

### Position Update Delay Problem
- Positions taking 5-10 minutes to update due to ClickHouse replication
- Double accounting issue from multiple table replication
- Lucas communicated to client, blamed on network issues during RPC outages
- Client expecting resolution "by tomorrow" for over a week

### Video Demo Requirements
- Stable environment needed urgently for client video production
- Critical flow: Login → Kitchen → Filters → Portfolio → Token Details (Pengu/Farcoin) → Charts → Limit Order
- Testing focus: Portfolio calculations, position updates, chart accuracy
- Charts breaking when switching timeframes (15-minute causing complete redraw failure)

## Technical Highlights

### Transaction Architecture Decisions
- **Postponed**: 6,000+ line microservice integration
- **Reason**: Too risky to test comprehensively before Friday deadline
- **Priority Order**: 1) Timeframes, 2) Double transaction fix, 3) Auto-priority fee
- **Microservice Status**: Already built and ready, just needs integration testing

### Solana Byte Limit Workaround
- Removed fee transfers from swap transactions
- Need strategy for linked transactions (only charge fee if swap succeeds)
- Martin working on double transaction approach

### ClickHouse Performance Optimization
- **Proposed Solution**: Partition position_full and folder tables by wallet hash
- **Testing Results**: Reduced query time from 12-14 seconds to ~1 second
- **Partitioning Strategy**: Using hash modulo (tested with 32 and 64 partitions)
- **Implementation Plan**: Create new table with new materialized view, test, then rename

### Chart Price Filtering Issues
- Pengu and Farcoin showing dramatic price drops (to 1/6 of actual value)
- Affecting market cap calculations significantly
- Eduardo investigating trusted token sources instead of aggressive filtering
- Current EMA filtering breaks price signal integrity

### Auto-Priority Fee Strategy
- Only applies to swaps, not wallet-to-wallet transfers
- Wallet transfers can use very low or hardcoded priority fee
- Cache Jupiter's returned priority fee value to display to users
- Each transaction saves fee calculation, not refreshing every 3 seconds
- Default slippage: 30% for all users

## Action Items

### Critical (Today/Tomorrow)
- [ ] **Esteban**: Implement timeframes by seconds for charts
- [ ] **Esteban**: Handle double transaction issue for limit orders and transaction service methods
- [ ] **Esteban**: Work on auto-priority fee (can extend to tomorrow)
- [ ] **Eduardo**: Review price filtering for charts (Pengu and Farcoin)
- [ ] **Eduardo**: Create new partitioned table for position_full with materialized view
- [ ] **Martin**: Document Eco integration plan with development timeline and testing approach
- [ ] **Byron**: Finalize token details screen information requirements

### This Week (By Wednesday)
- [ ] **All Features**: Must be closed by Wednesday for Thursday/Friday testing
- [ ] **Javier**: Test positions in empty wallet with Farcoin and Pengu purchases
- [ ] **Javier**: Verify portfolio calculations are correct in dev
- [ ] **Javier**: Test selling and position updates
- [ ] **Javier**: Complete flow with limit order close
- [ ] **Marko**: Assist with Diamond Hands and Insider frontend implementation
- [ ] **Javier**: Retest transactions after fee fix
- [ ] **Javier & Martin**: Discuss Positions discrepancies

### Post-Launch
- [ ] **Esteban**: Deploy transaction microservice to AWS for isolated testing
- [ ] **Esteban**: Mock auto-priority fee endpoints for frontend integration
- [ ] **Team**: Full integration testing of transaction microservice (~1 week)
- [ ] **Santiago**: Continue development on dynamic configuration, portfolio level, token watchlist

## Important Notes

### Launch Timeline Change
- **Original**: Friday (this week)
- **New Target**: October 15, 2025 (~2 weeks)
- **Reason**: Eco integration strategic opportunity
- **Client Awareness**: Communicated and accepted

### Eco Integration Benefits
- Superior execution speed compared to current implementation
- MEV protection included in routing
- Direct development team relationship through existing advisor
- Will become primary router with Jupiter as fallback

### Transaction Fee Collection Paused
- Cooking wallet fees temporarily disabled
- Referral transfers temporarily disabled
- Required to stay under Solana byte limit
- Need architectural solution for fee collection

### Development Environment Priorities
1. Stable environment for client video
2. Portfolio update flow working (Pengu/Farcoin)
3. Charts displaying correctly across timeframes
4. Limit order creation flow functional

### Testing Priorities
- All features frozen Wednesday
- Thursday/Friday dedicated to testing only
- No new features during testing window
- Focus on stability over new functionality

### ClickHouse Optimization Approach
- Create new partitioned tables alongside existing
- Test thoroughly before switching
- Use materialized views for data population
- Consider historical data migration strategy (batching required)

### Auto-Priority Fee Design
- User-level configuration stored in database
- Order-level configuration saved at creation time
- Orders don't change when user toggles auto-priority
- Only applies to swaps, not transfers
- Default slippage: 30%

### Known Issues
- Chart timeframe switching causes rendering failures
- Position updates delayed 5-10 minutes
- Double accounting in position calculations
- Price filtering too aggressive or too lenient
- Diamond Hands showing 36,000 holders (unsustainable for frontend)

### Risk Mitigation
- Postponing risky microservice integration
- Prioritizing stability for client demo
- Two-week extension allows proper Eco integration testing
- Focusing on completing existing work before new features
