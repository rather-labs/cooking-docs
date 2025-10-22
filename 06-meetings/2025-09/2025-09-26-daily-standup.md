---
title: Daily Standup - 2025-09-26
type: meeting
meeting_type: daily_standup
date: 2025-09-26
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
language: English (translated from Spanish)
translation_note: Spanish summaries translated to English, technical terms preserved
---

# Daily Standup - Cooking.gg
**Date:** September 26, 2025
**Duration:** 58:05
**Attendees:** Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda

## Executive Summary

Major performance breakthrough achieved - backend query speeds dramatically improved through cron decoupling and priority adjustments. The team successfully overcame critical loading time issues (reduced from 30-60 seconds to near-instant), positioning the project for Friday's demo. Key progress includes completed wallet import functionality, advanced orders refinement, and a comprehensive transaction microservice architecture presentation. Team preparing for Buenos Aires cowork next week while addressing tooltip design issues and planning for the upcoming beta phase with real users.

## Team Updates

### Lucas Cufré (Project Lead)
- Addressed browser configuration challenges (Safari/Chromium dependencies)
- Confirmed Buenos Aires cowork logistics: ACO Workspace, Escalabrini Ortiz 1135, 9 AM - 6 PM schedule
- Emphasized critical performance improvements resolved the most challenging bottleneck
- Announced upcoming beta phase requiring 24/7 on-call rotation system with additional compensation

### Martin Aranda (Backend Lead)
- Successfully decoupled crons from main backend queries, dramatically improving backend performance
- Assigned higher priority to query connection pools (dedicating 2 cores per replica)
- Working on Turnkey interaction errors for wallet import
- Projected significant milestone achievement within one week including Esteban's priority fee work, referrals completion, and bubble maps integration

### Luis Rivera (Frontend Developer)
- Updated positions table with market close limit order designs
- Added slow mode to withdrawal functionality
- Fixed scroll issue in Perpetuals screen
- Discussed need for global Maxwidth implementation for tooltips to improve readability

### German Derbes Catoni (Frontend Developer)
- Completed advanced orders details including scroll overflow fix
- Resolved toast notification positioning issues
- Working on criteria validation for selling without funds

### Marko Jauregui (Frontend Developer)
- Finalized Import Wallet frontend functionality
- Ready to take on additional tickets

### Federico Caffaro (Backend Developer)
- Implemented withdrawal fix integrating endpoint to verify Hyper Liquid user role
- Added first-time wallet interaction USD fee
- Restructured multi-layer referral system entities to rebuild user referral tree

### Esteban Restrepo (Backend Developer)
- Presented comprehensive transaction microservice architecture
- Demonstrated asynchronous event-driven transaction handling system
- Explained retry mechanism for failed transactions with automatic reconstruction
- Proposed frontend polling solution for transaction status updates using internal transaction IDs

### Eduardo Yuschuk (Indexer Developer)
- Reported and fixed Pam Swap price filtering issues for graduated tokens
- Identified Jupiter/indexer price data overwriting problem causing inconsistent readings
- Expressed concerns about ClickHouse optimization needs and indexer knowledge centralization
- Emphasized Solana's dynamic nature requiring constant code evolution

### Byron Chavarria (Mobile Developer)
- Completing token details section
- Starting trading operations integration
- Targeting Monday demo

### Darío Balmaceda (DevOps/Infrastructure)
- Successfully decoupled crons from backend, significantly improving performance
- Performance improvement achieved through connection pool separation and priority increase

## Key Discussion Topics

### Performance Breakthrough
- Loading times improved from 30-60 seconds to near-instantaneous
- Critical bottleneck (screen and chart loading) successfully resolved
- Team attributed success to Darío, Eduardo, Martin Aranda, and Luis Rivera's combined efforts
- Kitchen continued streaming data after being left open overnight - previously would have crashed

### Microservices Architecture Decision
- Decided not to implement gateway for microservices communication initially
- Frontend will have direct knowledge of all microservices
- Chose simpler approach to accelerate delivery

### Transaction Service Architecture
- Esteban presented 6000+ lines of code for transaction microservice
- Event-driven architecture using RabbitMQ for transaction processing
- Horizontal scaling capability for handling high transaction volumes
- Transaction retry logic with automatic reconstruction on failure
- Confirmation worker for polling RPC to verify finalized transactions

### ClickHouse Concerns
- Eduardo raised concerns about ClickHouse optimization and maintenance needs
- Large data volumes requiring dedicated optimization time
- Knowledge centralization issue - indexer knowledge currently concentrated in Eduardo
- Need to decentralize technical knowledge to avoid operational bottlenecks

### Buenos Aires Cowork Planning
- Location: ACO Workspace, Escalabrini Ortiz 1135
- Schedule: 9 AM - 6 PM with lunch provided
- Two days covered by project, three days by Raider
- Accommodation already reserved by Raider

## Technical Highlights

### Backend Architecture
- **Cron Decoupling**: Successfully separated crons from main backend queries with increased priority
- **Connection Pool Optimization**: Dedicated 2 cores per replica for query processing
- **Transaction Service**: New microservice with event-driven architecture for transaction handling
- **Retry Mechanism**: Automatic transaction retry with signature regeneration on blockchash failures

### Frontend Improvements
- **Tooltips**: Implementing global Maxwidth for multi-line content display
- **Advanced Orders**: Completed scroll overflow fixes and validation improvements
- **Wallet Import**: Frontend functionality complete, backend Turnkey integration in progress
- **Slow Mode**: Added to withdrawal functionality

### Indexer Updates
- **Pam Swap Filtering**: Fixed token price propagation for graduated tokens
- **Price Data**: Resolved Jupiter/indexer price overwriting issues
- **Dynamic Protocol Handling**: Continuous evolution required for Solana's changing protocols

### Infrastructure
- **Production Environment**: Deployed successfully
- **Scaling Strategy**: Prepared for 2,000 expected users but ready for 200,000
- **On-Call System**: Planning passive guard rotation for 24/7 beta phase operations

## Action Items

### Immediate (Pre-Demo)
- [ ] **Luis Rivera**: Add global Maxwidth to all Tooltip components
- [ ] **German Derbes Catoni**: Review and send criteria to Lucas about which inputs to disable when selling without funds
- [ ] **German Derbes Catoni**: Investigate toast notification extended display time issue
- [ ] **Marko Jauregui**: Take assigned task from Javi and other pending tickets
- [ ] **Martin Aranda**: Review chart data oscillation between indexer and 100%
- [ ] **Luis Rivera**: Create ticket to review trending functionality in Kitchen special view

### This Week
- [ ] **Byron Chavarria**: Complete trading operations integration for Monday demo
- [ ] **Byron Chavarria**: Update task status from "not started" to reflect actual progress
- [ ] **Martin Aranda & German Derbes Catoni**: Integrate bubble maps (now Baps Insidex) and add data to Token Details tables
- [ ] **Esteban Restrepo**: Create AWS infrastructure and deploy transaction service for isolated testing
- [ ] **Martin Aranda**: Implement simpler frontend microservices communication without gateway

### Strategic
- [ ] **Team**: Update Notion for client reporting requirements
- [ ] **Eduardo**: Dedicate time to ClickHouse optimization and maintenance
- [ ] **Team**: Decentralize indexer knowledge beyond Eduardo to avoid operational bottlenecks
- [ ] **Lucas/Martin**: Plan on-call rotation system with compensation structure for beta phase

## Important Notes

### Project Milestones
- **One Week Goal**: Significant milestone including priority fees, referrals completion, and bubble maps integration
- **Friday Demo**: Expected to conclude around 12:30 PM, no additional work expected that day
- **Next Week**: Beta phase begins with real users requiring 24/7 operations

### Referral Program Strategy
- Open program with no user limits per referral code
- System must scale from 2,000 to 200,000 users
- Multi-layer referral tree reconstruction implemented

### Market Context
- **Solana Traction**: Lucas shared vision of upcoming ETF normalization facilitating institutional investment
- **Competitive Position**: Solana gaining ground against Ethereum in daily active users and volume
- **Dynamic Ecosystem**: Protocols constantly evolving requiring continuous code adaptation

### On-Call System (Beta Phase)
- Passive guard rotation with additional compensation
- Extra hourly pay for actual work during on-call periods
- Guard pay separate from regular hours worked
- Necessary to ensure 24/7 operation with real users

### Critical Issues Resolved
- Screen loading performance (from 30-60s to 1-2s)
- Chart loading performance dramatically improved
- Backend query prioritization optimized
- Pam Swap token price propagation fixed

### Pending Concerns
- ClickHouse optimization and scaling
- Indexer knowledge centralization
- Transaction confirmation polling strategy
- Frontend microservices communication architecture
- Error notification system for failed transactions (nice-to-have)
