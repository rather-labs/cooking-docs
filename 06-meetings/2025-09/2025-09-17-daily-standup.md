---
title: Daily Standup - 2025-09-17
type: meeting-note
meeting_type: Daily Standup
date: 2025-09-17
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
duration: 68 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_09_17 09_28 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-09-17

## Meeting Information
- **Type:** Daily Standup
- **Date:** September 17, 2025
- **Duration:** 68 minutes
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
- Esteban Restrepo
- German Derbes Catoni
- Marcos Tacca
- Darío Balmaceda (New team member)

## Summary
Lucas Cufré introduced Darío Balmaceda joining for the final sprint to help with pending tasks and ClickHouse optimization. Luis Rivera reported Market Orders and Perpetuals errors are resolved. Martin Aranda disabled branch protections on Develop due to urgency. German Derbes Catoni's Token Details module is nearly ready. Eduardo Yuschuk resolved client observations and temporarily disabled Jupiter indexing. Esteban Restrepo integrated bars from Redis with fast performance. Major discussions centered on ClickHouse performance issues, with queries taking 2.5x longer during data insertions, and backend performance degrading over time despite local consistency.

## Team Updates

### Lucas Cufré
- **Status:** Sprint coordination and new team member onboarding
- **Progress:** Introduced Darío Balmaceda to the team, coordinating final sprint
- **Blockers:** Clients actively monitoring development environment
- **Next Steps:** Manage final sprint delivery and client expectations

### Darío Balmaceda (New)
- **Status:** Onboarding and ClickHouse optimization
- **Progress:** Analyzing ClickHouse performance issues, can dedicate 4 hours daily
- **Blockers:** Commitments with Membring limiting availability
- **Next Steps:** Investigate ClickHouse parallelization and optimization

### Luis Rivera
- **Status:** Market Orders and Perpetuals fixes
- **Progress:** Resolved all bugs indicated by Javier, tables now have tooltips
- **Blockers:** Token logos are circular instead of rectangular as expected
- **Next Steps:** Document formulas in Notion, adjust Ethereum icon

### Martin Aranda
- **Status:** Branch management and performance investigation
- **Progress:** Disabled branch protections for urgency, investigating slowness
- **Blockers:** ClickHouse queries slow during insertions
- **Next Steps:** Optimize materialized views and caching strategy

### German Derbes Catoni
- **Status:** Token Details nearly complete
- **Progress:** Main functionality done, orders section separated to reduce PR size
- **Blockers:** None reported
- **Next Steps:** Complete Advanced Orders and Wallet Manager alignment

### Eduardo Yuschuk
- **Status:** Client observations and indexing issues
- **Progress:** Resolved client-reported issues, fixed Jupiter indexing problems
- **Blockers:** Token migration visibility challenges
- **Next Steps:** Implement outlier filter for price bars

### Esteban Restrepo
- **Status:** Redis bars integration
- **Progress:** PR submitted, consulting Redis every 300ms with excellent performance
- **Blockers:** Some bars arriving with zero data
- **Next Steps:** Handle zero-value bars and implement timeframe aggregation

### Federico Caffaro
- **Status:** Bug fixes and slow withdraw
- **Progress:** Fixed Perpetuals bugs, working on slow withdraw functionality
- **Blockers:** None reported
- **Next Steps:** Complete slow withdraw, then move to multilevel referral system

### Byron Chavarria
- **Status:** Portfolio implementation
- **Progress:** Finalizing portfolio section, iOS 18 considerations
- **Blockers:** iOS 18 visual and behavior changes incoming
- **Next Steps:** Complete portfolio and prepare for iOS 18 updates

### Santiago Gimenez
- **Status:** Library updates and visual alignment
- **Progress:** Updated icons in library, performed refactoring
- **Blockers:** None reported
- **Next Steps:** Continue visual refinements

### Javier Grajales
- **Status:** Testing and bug reporting
- **Progress:** Found issues with users without Perpetual Wallet
- **Blockers:** Network errors in Perpetuals
- **Next Steps:** Continue comprehensive testing

## Key Discussion Points

### ClickHouse Performance Crisis
- Queries taking 2.5x longer during data insertions
- Materialized views recalculating on each insert, blocking queries
- Backend performance degrading over time despite stable local performance
- Darío investigating parallelization possibilities for materialized views
- Considering temporary solution prioritizing speed over immediate data updates

### New Team Member Integration
- Darío Balmaceda joining for final sprint
- 4 hours daily availability due to Membring commitments
- Added to GitHub and Notion for collaboration
- Focus on ClickHouse optimization given expertise

### Critical UI/UX Issues
- Hyperliquid token logos are circular SVGs vs expected rectangular format
- Ethereum logo displaying poorly due to SVG format
- Need exception handling for Ethereum logo
- Tables require tooltips and proper decimal precision

### Token Migration Feedback
- Users unable to trade tokens during migration (2-10 minutes)
- Need visual feedback for migration status
- Competition shows migration status differently
- Decided to deprioritize for current sprint

## Action Items
- [ ] Santiago Gimenez: Adjust icon in Perpetuals dashboard for contract selection
- [ ] Luis Rivera: Document formulas in Notion ticket
- [ ] Eduardo Yuschuk: Create task to investigate token migration duration
- [ ] Javier Grajales: Review Pengu purchases and contract data loading issues
- [ ] Martin Aranda & Eduardo Yuschuk: Evaluate adding liquidity to bar chart data
- [ ] Esteban Restrepo: Adjust queries for timeframe data optimization
- [ ] Darío Balmaceda: Investigate ClickHouse parallelization for materialized views
- [ ] Lucas Cufré: Add Darío to internal channel
- [ ] German Derbes Catoni: Complete time estimation for Advanced Orders alignment
- [ ] Federico Caffaro: Document formulas and complete slow withdraw

## Technical Details
- **ClickHouse Issues:** Materialized views causing 2.5x query slowdown during inserts
- **Redis Integration:** Bars querying every 300ms with excellent performance
- **Token Migration:** 2-10 minute unavailability during launchpad to DEX migration
- **iOS 18 Impact:** Required visual and behavioral adjustments for next 6 months

## Links & References
- ClickHouse Optimization: Investigation into parallelization strategies
- iOS 18 Guidelines: Apple's new design requirements
- Migration Tracking: Research into real-time migration status

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*