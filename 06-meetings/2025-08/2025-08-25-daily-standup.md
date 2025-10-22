---
title: Daily Standup - 2025-08-25
type: meeting-note
meeting_type: Daily Standup
date: 2025-08-25
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca]
duration: 31 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_08_25 09_28 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-08-25

## Meeting Information
- **Type:** Daily Standup
- **Date:** August 25, 2025
- **Duration:** 31 minutes
- **Platform:** Google Meet
- **Language:** Spanish (translated to English)

## Attendees
- Eduardo Yuschuk
- Santiago Gimenez
- Luis Rivera
- Florencia Redondo
- Lucas Cufré
- Martin Aranda
- Mauricio Hernán Cabrera
- Marko Jauregui
- Federico Caffaro
- Javier Grajales
- Byron Chavarria
- Martin Lecam
- Esteban Restrepo
- German Derbes Catoni
- Marcos Tacca

## Summary
Team discussed critical issues with contract search functionality, progress on frontend implementations, backend optimizations, and preparation for an important demo on Monday. Focus on resolving search functionality and ensuring core features are stable for the demonstration.

## Team Updates

### Luis Rivera
- **Status:** Frontend bug fixes and functionality issues
- **Completed:** Resolved frontend errors, Perpetuals notifications working
- **Current Issue:** Contract search only accepts full ticker (not partial search)
- **Current Work:** Implementing Advanced Charts Trading View
- **Next Steps:** Complete chart integration and order creation

### Lucas Cufré
- **Status:** Prioritization and demo preparation
- **Decision:** Accept full ticker search as temporary solution
- **Rationale:** Prioritize functionality over perfect search with 5 weeks to delivery
- **Current Work:** Preparing for important Monday demo
- **Next Steps:** Finalize demo preparation

### German Derbes Catoni
- **Status:** Home page completion
- **Target:** Complete by noon today
- **Current Work:** Finishing home page implementation
- **Next Steps:** Visual bugs fixes and token replacement tasks

### Martin Lecam
- **Status:** Wallet connection implementation
- **Progress:** Backend complete, working on frontend integration
- **Current Work:** Frontend integration of wallet connect
- **Next Steps:** Complete integration today

### Marko Jauregui
- **Status:** Account linking development
- **Progress:** Backend nearly complete, needs unit tests
- **Current Work:** Frontend integration preparation
- **Next Steps:** Complete testing and frontend support

### Federico Caffaro
- **Status:** HyperLiquid and trading features
- **Completed:** Order Books levels, live trades endpoint
- **Issue:** Observable pattern refactoring needed
- **Current Work:** Redis lock issue investigation
- **Next Steps:** Resolve lock issues and continue testing

### Esteban Restrepo
- **Status:** Clickhouse migration complete
- **Achievement:** BWAP service migrated to Clickhouse
- **Improvement:** Organized Clickhouse module for better dependency injection
- **Next Steps:** Work on transaction service scaling

### Eduardo Yuschuk
- **Status:** Redis to PostgreSQL migration
- **Progress:** Moved block storage back to PostgreSQL
- **Current Work:** Reviewing new Munit and Raydium instructions
- **Next Steps:** Continue monitoring and optimization

### Byron Chavarria
- **Status:** Mobile authentication and referral
- **Completed:** Auth0 integration review with Martin
- **Current Work:** Referral code UI nearly complete
- **Next Steps:** Complete referral implementation

### Santiago Gimenez
- **Status:** Kitchen refactor with new design system
- **Progress:** All components ready except token card
- **Priority:** Complete token card today per Lucas
- **Next Steps:** Finish Kitchen implementation

### Javier Grajales
- **Status:** Testing DCA and TWAP orders
- **Issues Found:** Orders only work with Moonshot, fail with Jupiter/Pumpfun
- **Problems:** DCA sell timing inconsistencies, duplicate transactions
- **Current Work:** Investigating BWAP/TWAP execution failures
- **Next Steps:** Continue testing and issue documentation

### Martin Aranda
- **Status:** Architecture and performance monitoring
- **Focus:** System stability for demo
- **Observation:** Memory stabilized after garbage collection
- **Next Steps:** Ensure demo environment stability

## Key Discussion Points

### Contract Search Functionality
- Current limitation: requires full ticker entry
- Temporary solution: accept current functionality
- Future improvement: implement partial search
- List of all perpetuals available for selection

### Monday Demo Preparation
- Critical demo scheduled for Monday
- Need all core features stable
- Focus on functionality over perfection
- Team alignment on priorities

### Trading Order Issues
- DCA/TWAP only working with Moonshot provider
- Jupiter and Pumpfun integration problems
- Duplicate transaction display issues
- BWAP/TWAP orders not executing

### UI/UX Updates Priority
- Kitchen card completion urgent
- New design system implementation ongoing
- Focus on demo-critical screens
- Advanced orders need review

## Action Items
- [ ] Luis Rivera: Prioritize Trading View charts for other charts
- [ ] Santiago Gimenez: Complete Kitchen token card today
- [ ] German Derbes Catoni: Finish home page by noon
- [ ] Federico Caffaro: Investigate and fix Redis lock issues
- [ ] Javier Grajales: Document all trading order issues
- [ ] Martin Aranda: Review PRs for demo readiness
- [ ] Lucas Cufré: Finalize demo script and preparation
- [ ] Team: Ensure stability for Monday demo

## Technical Details
- **Search Limitation:** API requires exact ticker match
- **Perpetuals List:** Full list available via paginated endpoint
- **Memory Status:** Garbage collector working correctly at 28% threshold
- **Provider Issues:** Only Moonshot working for complex orders

## Blockers & Risks
- Search functionality limitations for demo
- Trading provider integration issues
- Tight timeline for Monday demo
- Some advanced features not ready

## Decisions Made
- Accept full ticker search for now
- Prioritize demo stability over new features
- Focus on core functionality completion
- Defer search improvements post-demo

## Demo Readiness Checklist
- [ ] Core trading operations functional
- [ ] Authentication flow complete
- [ ] Charts and data visualization ready
- [ ] Mobile app basic features working
- [ ] No critical bugs in main flow

## Links & References
- Related Features: Contract search, Trading operations, Monday demo
- Related Meetings: Demo preparation session before Monday

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*