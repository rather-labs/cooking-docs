---
title: Daily Standup - 2025-10-06
type: meeting
meeting_type: daily_standup
date: 2025-10-06
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** October 6, 2025 (Monday - Holiday)
**Duration:** 35:21
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

Team worked through holiday weekend addressing critical UI refinements and Eco API integration preparation. German completed token details modifications, Marko finished referral flow improvements, and Federico implemented Hyper Liquid optimizations. Lucas emphasized urgent need to begin Eco API testing to avoid integration issues similar to Hyper Liquid experience. Darío resolved major ClickHouse performance crisis by creating new projection, dramatically reducing rows read and improving query speed. Team confirmed using Raider account for testing since client discontinued Team Cook accounts. DNS resolution meeting scheduled immediately post-demo due to Japan time zone difference (12-hour gap).

## Team Updates

### German Derbes Catoni (Frontend Developer)
- Modified token details chart backgrounds to match Figma design
- Limited prices and coordinated pricing displays
- Started updating Advanced Orders (expected completion soon)
- Will review requested typography size adjustments for login page per client feedback

### Marko Jauregui (Frontend Developer)
- Working on Referral flow fixes including modal flows and internal transfers
- Adjusting referral UI to match design as closely as possible
- Looking for new tasks after completing current work

### Federico Caffaro (Backend Developer)
- Completed PR for Vill CS and Referal CS
- Implemented Hyper Liquid optimizations and code organization
- Fixed referral bug: configuration must happen before funds arrive at Perpetuals
- Can now retroactively assign dev accounts as referrals for testing
- Will link all Perpetuals dev accounts to provided Hyper Liquid referral code

### Esteban Restrepo (Backend Developer)
- Completed backend transaction integration
- Needs frontend developer to integrate polling for synchronous transactions
- Push to repository registry failed - will coordinate with Jesús (DevOps)
- Still needs to merge legacy transactions GET with current implementation

### Eduardo Yuschuk (Indexer Developer)
- Working on Eco API integration
- Discussed security service options (external vs internal)
- Most external services focus on AML/terrorism financing (introduces significant latency)
- Proposed two approaches:
  1. Static transaction analysis (check signatures, wallets, program calls)
  2. Transaction simulation to see fund flows
- Emphasized need to avoid buying more problems for client

### Darío Balmaceda (Infrastructure - ClickHouse Hero)
- **Major Achievement**: Resolved critical ClickHouse performance issue
- Created new projection optimizing queries, reducing rows read by factor of 10
- Tables consolidated successfully after merge crisis
- Portfolio and holders queries dramatically improved in speed
- Will create two ClickHouse backend clients with different configurations:
  - API client: higher priority, more CPU
  - Cron jobs client: lower priority, less CPU usage

### Byron Chavarria (Mobile Developer)
- Advancing L-Ramper integration preparation
- Finishing token details view data integration
- Pending account access for OTP and physical device testing
- Needs on-ramp account credentials (Lucas handling)

### Javier Grajales (QA/Testing)
- Reported referral flow issues: modal not appearing on first login after account deletion
- Tested holder categories (Sniper, Insider, Diamond Hands) - working correctly
- Missing examples for "De Bot" and "De Sold" categories
- Reviewed carousel (found defect)
- Found issue with token transfers between own wallets (two different errors)
- Tested first login and referral modals
- Generating multiple wallets linked with referrals for testing

### Santiago Gimenez (Frontend Developer)
- Working on Refer and Bubble Maps features
- Started design for new filters (exploration phase)
- Will shift focus to design QA per Lucas request

### Martin Aranda (Technical Lead)
- Proposed load testing plan with Javier and Federico
- Discussed using simulated transactions (excluding Solana submission part)
- Suggested testing in dev environment during low-usage times
- Investigating Eco API endpoint returning 500 error
- Endpoint generates 7 parallel transactions with same nonce (times out after 5 seconds)

## Key Discussion Topics

### Eco API Integration Urgency
- **Lucas Priority**: Begin testing Eco API immediately to evaluate speed and structure
- **Lesson Learned**: Avoid Hyper Liquid integration mistakes (geolocation issues discovered only in Mainnet)
- **Strategy**: Exhaust investigation phase before development, document unknowns clearly
- **Parallel Work**: Esteban and Martin to research Eco in parallel, share findings
- **Goal**: Complete transaction microservice integration this week

### Client Feedback - "Pixel Perfect" Design Review
- US design agency reviewing everything at pixel-perfect level
- **Task Division**:
  - **Javier**: Focus on functionality testing (especially Advanced Orders after microservices deploy)
  - **Santiago**: Design QA in Chrome and Safari
- **Safari Now In Scope**: Must test in Safari (never defined as out-of-scope)
- **Image Issues**: Lucas re-exported all images as 1000x1000 PNG (stored in Drive - Cooking Internal Team folder)
- **Login Images**: Changed from SVG to PNG to fix Safari rendering issues
- **Component Alignment**: Luis and Marcos to adjust image alignment in login divs

### Referral Flow Problems
- **Issue**: Modal not appearing on first login after account deletion
- **Expected Flow**:
  - New user without referral code URL → Modal asking "Want to be a referral?"
  - If yes → Input referral code
  - If skip → Can join later as referral program member
- **Create Code Modal**: Should allow one-time custom code update or use default
- **Bug Confirmed**: Update call not being made when first modal appears
- **Missing Feature**: No button to edit referral code - team discovered this was never implemented

### ClickHouse Performance Crisis Resolution
- **Problem**: Instances saturated with merge processes, queries getting stuck
- **Root Cause**: Three instances simultaneously merging, saturating resources
- **Impact**: Once 1,000 queries accumulated, system became completely unresponsive
- **Solution**:
  - Created new projection with correct ordering
  - Dramatically reduced rows read (10x improvement)
  - Portfolio queries now fast and scalable
  - Holders queries optimized
- **Configuration Issue**: Use concurrency control requires CPU cycles for scheduling, causing queries to get stuck when merges saturate system
- **Proposed Enhancement**: Two ClickHouse clients with different priority levels

### DNS Management Challenge
- **Issue**: Client in Japan (12-hour time difference) making DNS changes difficult
- **Request**: Access to domain dashboard for direct DNS management
- **Client Response**: Best they can do is screen-share workshop session
- **Plan**: 15-minute session post-demo to resolve DNS immediately
- **Urgency**: Blocking deployment of Esteban's transaction microservices for testing

## Technical Highlights

### ClickHouse Optimization Success
- **Before**: Queries taking 12-14 seconds, instances getting stuck with 1,000+ pending queries
- **After**: Sub-second queries, stable performance
- **Key Change**: New projection ordering data differently for optimal query patterns
- **Side Benefit**: 99% cache hit rate with gigabytes of RAM
- **Monitoring**: CPU at 16-17 (limit 30) - elevated but stable compared to previous 8

### Transaction Service Integration Status
- **Backend**: Complete, needs deployment
- **Frontend**: Needs polling implementation for transaction status
- **DNS Blocker**: Preventing deployment to dev for testing
- **Priority**: Get deployed ASAP for comprehensive testing

### Eco Security Analysis
- **External Services**: Mostly AML/terrorism financing (wrong use case, high latency)
- **Static Analysis**: Check transaction signatures, wallets, program calls (~2ms)
- **Simulation**: Execute transaction to see fund flow (higher latency)
- **Decision Pending**: Client choice between third-party service vs internal implementation
- **Latency Concern**: Unavoidable in either approach (external or internal)

### Referral System Testing
- **Capability**: Can now retroactively link dev accounts to Hyper Liquid referral code
- **Purpose**: Test fee retrieval in dev before production testing
- **Plan**: Link all Perpetuals dev accounts as referrals to provided code

### Load Testing Strategy
- **Approach**: Simulated transactions excluding Solana blockchain submission
- **Focus**: Jupiter and provider interaction, not blockchain finalization
- **Environment**: Dev during low-usage periods
- **Method**: Apache AB for high concurrency, scripts for specific test scenarios
- **Scope**: User creation, wallet creation, orders from multiple wallets with multiple providers

## Action Items

### Critical (Immediately)
- [ ] **Martin & Lucas**: Meet with client to resolve DNS post-demo (~15 minutes)
- [ ] **Esteban**: Complete backend transaction integration merge
- [ ] **Esteban**: Coordinate with Jesús on repository push failure
- [ ] **German**: Adjust login page typography sizes per client specifications
- [ ] **Lucas**: Resolve on-ramp credentials for Byron

### Today
- [ ] **Esteban & Martin**: Begin Eco API testing (velocities, response structure, issues)
- [ ] **Esteban**: Polish transaction microservice for deployment
- [ ] **Eduardo**: Work on transaction security integration
- [ ] **Eduardo**: Integrate Radium fixes into dev environment
- [ ] **Darío**: Make ClickHouse projection changes in DEP
- [ ] **Darío**: Coordinate with Lucas/Martin for trade operation to verify consistency
- [ ] **Federico**: Link all dev Perpetuals accounts as referrals to provided Hyper Liquid code
- [ ] **Marko**: Adjust referral UI to match design

### This Week
- [ ] **Javier**: Focus on referral code flow testing
- [ ] **Santiago**: Review missing edit button for referral code
- [ ] **Martin**: Implement frontend polling for synchronous transactions
- [ ] **Martin**: Combine legacy transactions GET with current implementation
- [ ] **Federico & Javier**: Develop load testing plan using simulated transactions
- [ ] **Team**: Continue reviewing assigned tickets in Component Library Alignment and Bugs projects

## Important Notes

### Team Recognition
- **Holiday Work**: Team working through Monday holiday showing exceptional dedication
- **Client Pressure**: "Pixel Perfect" review from US design agency intensifying requirements
- **Lucas Comment**: Will distribute issues focused mainly on frontend (most client feedback area)
- **Small Tasks**: Mostly small issues except login and Advanced Orders (requires dedicated session)

### Eco Integration Context
- **Client Location**: Japan (12-hour time difference complicating coordination)
- **Previous Lesson**: Hyper Liquid integration revealed geolocation issues only in Mainnet
- **Prevention Strategy**: Thorough investigation before development commitment
- **Timeline**: Need to move quickly while being thorough

### ClickHouse Recovery
- **Data Loss**: Backup recovery resulted in information gap
- **Cause**: Merge processes spiraled out of control, instances became inoperable
- **Current State**: Stable, fast, scalable
- **Monitoring**: Elevated CPU (16-17) but consistent and manageable
- **Future Plans**: Persist all ClickHouse changes to repository for reference

### Referral Code Flow Clarification
- **New User Path 1**: No referral code in URL → Modal asking to join as referral → Input code OR skip
- **New User Path 2**: Can join referal program later by creating/using code
- **Code Creation**: Auto-generated default code, one-time custom update allowed
- **Referral Tree**: User can be both referrer (with code) and referred (under someone else)
- **Missing UI**: Edit button for referral code never implemented (now being added)

### Safari Rendering Issues
- **Scope Change**: Safari now officially in scope (was never defined as out-of-scope)
- **Image Solution**: Re-exported all 3D images and referral badges as 1000x1000 PNG
- **Typography**: Differences in rendering between browsers (acceptable if not fixable)
- **Priority**: Ensure functionality works, then optimize appearance per browser

### Testing Accounts
- **Source**: Using Raider account (client discontinued Team Cook accounts)
- **Access**: Lucas resolving throughout the day
- **Purpose**: Enable mobile device testing and OTP verification

### Load Testing Approach
- **Mock Level**: Solana blockchain submission mocked, Jupiter/providers real
- **Environment**: Dev during off-hours to avoid impacting active work
- **Verification**: Check if transaction library mock skips signing and construction
- **Providers**: Currently hardcoded to Jupiter only, will need reconfiguration for multi-provider testing

### Transaction Fee Collection
- **Status**: Still not collecting Cooking fees or referral fees
- **Blocker**: Solana byte limit issue from previous discussions
- **Planned Solution**: Separate linked transaction for fee collection (Esteban working on this)
- **Timeline**: Urgent priority to implement this week
