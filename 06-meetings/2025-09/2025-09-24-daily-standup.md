---
title: Daily Standup - 2025-09-24
type: meeting-note
meeting_type: Daily Standup
date: 2025-09-24
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
duration: 30 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_09_24 09_28 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-09-24

## Meeting Information
- **Type:** Daily Standup
- **Date:** September 24, 2025
- **Duration:** 30 minutes
- **Platform:** Google Meet
- **Language:** Spanish (translated to English)

## Attendees
- Eduardo Yuschuk
- Santiago Gimenez
- Luis Rivera
- Florencia Redondo
- Lucas Cufré
- Martin Aranda
- Marko Jauregui
- Federico Caffaro
- Javier Grajales
- Byron Chavarria
- Martin Lecam
- Esteban Restrepo
- German Derbes Catoni
- Marcos Tacca
- Darío Balmaceda

## Summary
Final sprint approaching with October 3rd delivery deadline. Federico Caffaro focused on referral and multilevel systems. Esteban Restrepo testing transactions microservice. Luis Rivera confirmed bars functionality with frontend. Eduardo Yuschuk implementing SOL/USD price capture and propagation. Darío Balmaceda investigating ClickHouse optimization with CPU usage issues. Byron Chavarria completed wallet and token endpoints integration. Martin Lecam submitted referrals PR. Lucas Cufré defining post-October 3rd roadmap including token watchlist, wallet tracker, and dynamic commission configuration.

## Team Updates

### Federico Caffaro
- **Status:** Starting multilevel referral system
- **Progress:** Completed slow deposit testing and fixes
- **Blockers:** None reported
- **Next Steps:** Full focus on referral implementation

### Esteban Restrepo
- **Status:** Microservice testing and deployment
- **Progress:** Transactions microservice in testing phase
- **Blockers:** None reported
- **Next Steps:** Deploy microservice, implement dynamic timeframes

### Luis Rivera
- **Status:** Bars integration and UI updates
- **Progress:** Bars functional with frontend, supporting multiple timeframes
- **Blockers:** Waiting for bars to function again
- **Next Steps:** Complete Perpetuals closure, test limits functionality

### Eduardo Yuschuk
- **Status:** Price propagation and Total Supply
- **Progress:** SOL/USD price capture working, using Redis cache
- **Blockers:** None reported
- **Next Steps:** Complete Total Supply table, review tickets

### Darío Balmaceda
- **Status:** ClickHouse optimization
- **Progress:** Identified high CPU usage, slow backend interaction
- **Blockers:** Complex performance issues
- **Next Steps:** Test resource segregation strategies

### Byron Chavarria
- **Status:** Mobile integration complete
- **Progress:** Wallet, limit order, and token endpoints integrated
- **Blockers:** None reported
- **Next Steps:** Complete testing and polish

### Martin Lecam
- **Status:** Referrals implementation
- **Progress:** Submitted PR for backend referrals
- **Blockers:** May not apply due to upcoming changes
- **Next Steps:** Work on frontend for multilevel referral

### German Derbes Catoni
- **Status:** Advance Orders development
- **Progress:** Working to complete orders functionality
- **Blockers:** None reported
- **Next Steps:** Complete Advance Order, then Wallet Manager

### Santiago Gimenez
- **Status:** Visual QA and modals
- **Progress:** Token Details QA complete, privacy policy modal v1 done
- **Blockers:** None reported
- **Next Steps:** Finalize legal modals

### Marko Jauregui
- **Status:** Wallet frontend work
- **Progress:** Working on wallet functionality
- **Blockers:** None reported
- **Next Steps:** Complete wallet frontend today

### Lucas Cufré
- **Status:** Sprint coordination and planning
- **Progress:** Defining post-October 3rd roadmap
- **Blockers:** None reported
- **Next Steps:** Coordinate final sprint delivery

## Key Discussion Points

### Final Sprint Timeline
- October 3rd is hard delivery deadline
- This Friday is penultimate demo
- Following Friday is final demo
- Team entering "crunch mode" for final push

### Post-Delivery Roadmap
- New initiatives being defined for after October 3rd
- Token watchlist feature planned
- Wallet tracker functionality
- Portfolio level configurations
- Dynamic commission settings

### Critical Path Items
- Multilevel referral system is priority
- Auto-adjusted profit feature needs research
- Gas price display for frontend required
- Dynamic timeframes for bars needed

### ClickHouse Optimization
- Considering horizontal or vertical scaling
- Workload segregation being tested
- Read replica option being evaluated
- High CPU usage identified as issue

## Action Items
- [ ] Federico Caffaro: Complete referral implementation
- [ ] Luis Rivera: Write to Esteban about dynamic timeframes for bars
- [ ] Esteban Restrepo: Make bars return dynamically, implement gas price display
- [ ] Esteban Restrepo: Notify Javier when transaction PR is ready
- [ ] Luis Rivera: Complete Perpetuals closure, test all functionality
- [ ] German Derbes Catoni: Complete Advance Order, move to Wallet Manager
- [ ] Marko Jauregui: Complete wallet frontend today
- [ ] Martin Lecam: Handle multilevel frontend when Federico advances
- [ ] Eduardo Yuschuk: Complete Total Supply today, review ticket list
- [ ] Darío Balmaceda: Test resource segregation strategies

## Technical Details
- **Timeframe Support:** 1s, 5s, 15s, 30s, 1m, 3m, 5m, 15m, 30m, 1h, 6h, 12h
- **SOL/USD Price:** Captured from swaps, cached in Redis, updated per block
- **ClickHouse:** High CPU usage during queries, considering scaling options
- **Microservices:** Transactions module with HTTP and MQ interfaces

## Links & References
- October 3rd Delivery: Final sprint deadline
- Post-Launch Roadmap: New features and initiatives
- ClickHouse Documentation: Workload configuration strategies

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*