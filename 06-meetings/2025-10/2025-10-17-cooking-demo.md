---
title: Cooking Demo - ClickHouse Production Deployment & Dubai Trip Planning
date: 2025-10-17
type: demo
attendees:
  - Lucas Cufré
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Martin Aranda
  - Naji Osmat
  - Marcos Tacca
  - Shakeib Shaida (shak@ember.app)
status: completed
tags:
  - demo
  - clickhouse
  - production-deployment
  - ui-updates
  - bubble-maps
  - inside-x
  - documentation
  - auto-priority-fee
related:
  - "[[2025-10-10-cooking-demo]]"
  - "[[04-knowledge-base/technical/architecture/clickhouse-migration]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team successfully deployed ClickHouse improvements to production, resolving position update lag issues. Major UI updates include advanced orders interface, revamped portfolio screen with Soul Scan links, and successful integration of Inside X bubble maps feature. The partner program page has been refactored to latest design with multi-level program support. A new auto-priority fee feature is being tested to optimize Solana transaction costs based on network congestion. Documentation is complete on Gitbook and awaiting DNS publication. The team also coordinated Dubai travel plans, with Lucas and Marcos arriving October 7th and Gregory arriving October 8th.

## Meeting Details

**Duration:** 17 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Dubai Travel Coordination

**Travel Dates:**
- **Lucas & Marcos:** Departing October 5th at 11 PM
- **Arrival:** October 7th, 12:30 AM (early morning)
- **Flight duration:** 18 hours from Argentina (Lucas), 6 hours from Germany (Marcos)
- **Gregory:** Targeting October 8th arrival (one day after team)

**Attendees Expected in Dubai:**
- Gregory Chapman
- Naji Osmat
- Shakeib Shaida
- Zen
- Possibly Ali (Dubai-based, will join for some sessions)

**Gregory's Background Context:**
- Recent extensive travel: UK → California → Singapore → UK → Dubai (May 2025)
- Multiple 18-hour flights completed
- UK to Dubai: ~7 hours (relatively short compared to recent travel)

**Ali Introduction:**
- Ali is Dubai-based team member
- Lucas has only spoken with Ali once, never met in person
- Ali will join for some Dubai sessions, not daily

### 2. ClickHouse Production Deployment

**Status:** Successfully deployed to production

**Impact:**
- Position update lag completely resolved
- Transactions now update as quickly as in development environment
- Previously identified delay issues eliminated
- Production performance now matches development expectations

**Technical Achievement:**
- ClickHouse enhancements fully implemented
- Performance optimization delivered
- No reported issues with deployment

**Quote:**
> "Right now when you generate a transaction or anything of the sort, that is going to update as quick as it is now on dev. So the issue with the positions being taken a little while to update has been solved." - Lucas Cufré

### 3. Advanced Orders UI Update

**Current Status:** UI updated, minor fixes in progress

**What's Working:**
- Latest design implemented
- Functional market and limit orders
- Table updates to new design

**Issues Being Addressed Today:**
- Minor visual elements requiring adjustment
- Fine-tuning of interface components
- Polish and refinement work

**Overall Assessment:** "Pretty much anything and everything that we've set out to achieve"

### 4. Portfolio Screen Revamp

**Important Note:** Not final design - Leo hasn't provided final design yet

**Team Decision:** Updated to interim design rather than wait

**Improvements Implemented:**

**Table Updates:**
- New table design from component library
- Cleaner, more modern appearance
- Improved data presentation

**Soul Scan Integration:**
- Direct links to blockchain explorer added
- Users can review transaction details on-chain
- Click-through functionality from portfolio to Soul Scan
- Enhanced transparency and verification capability

**Transaction Display:**
- Clear categorization of transaction types
- Improved transaction history visibility

**Current Limitation:** Awaiting final design from Leo for complete implementation

### 5. Token Trading & Real-Time Updates

**Demonstration of Speed:**
- Token purchase with real-time update
- Sell interaction uses new spinner UI element
- Transaction confirmation within seconds
- Position updates immediately after confirmation
- Portfolio reflects changes with minimal delay

**UI Enhancement:**
- New spinner animation for sell transactions
- Visual feedback during transaction processing
- Improved user experience during trades

**Performance:**
- Quick transaction execution
- Rapid position updates
- Seamless portfolio refresh

### 6. Token Details & Badge System

**Visual Issue Identified:**
- Token details page has rendering problem
- Currently being fixed
- Affects badge display

**Badge System Features:**
- Wallet classification badges implemented
- Categories displayed:
  - Top 10 holders
  - Diamond hands
  - Snipers
  - Developer wallets
  - Wallet interaction tracking
  - Buy/sell timing indicators

**Status:** Functional but visual polish needed

### 7. Inside X Bubble Maps Integration

**Status:** Successfully integrated

**Functionality:**

**Initial Load:**
- First access to token requires bubble map generation
- Generation happens via Inside X engine
- Delay during first generation is Inside X processing time
- Not a Cooking performance issue

**Example Scenario:**
- Some tokens (new/unused) require initial bubble map creation
- "Nobody has interacted with this particular wallet" message
- Processing time depends on Inside X API response

**Live Example:**
- Demonstrated with Pengu token (well-known token)
- Interactive bubble map display
- Shows all wallets that interacted with contract
- Cluster holding amounts visible
- Filtering capabilities demonstrated
- "Show everything" option available

**User Experience:**
- Seamless integration once loaded
- Rich wallet interaction visualization
- Clustering analysis of token holders

### 8. Empty State Improvements

**No Positions Placeholder:**
- New empty state design for portfolio
- "No positions" message with visual placeholder
- Call-to-action: "Start Trading" button
- CTA redirects to advanced orders screen

**User Flow:**
- Click "Start Trading" → redirected to advanced orders
- Pre-selected token (e.g., Pengu) can be traded immediately
- Market order placement simplified
- Confirmation flow streamlined

**Demo:**
- Showed complete flow from empty portfolio to first trade
- Demonstrated market order placement
- Real-time position appearance after trade
- Immediate portfolio update

**UI Issue Noted:** Vertical spacing slightly tight (being fixed)

### 9. Partner Program Redesign

**Status:** Complete refactoring to latest design

**Features Implemented:**

**Multi-Level Program:**
- Fully implemented and tested
- Multiple tiers supported
- Tier progression tracking

**Dashboard Display:**
- Last 30 days statistics
- Personal volume traded
- Fees generated from volume
- Kickback eligibility status

**Example Data:**
- Personal volume: 380 USDC
- Not eligible for 50k kickback at 5% level
- Clear tier requirements displayed

**Visual Status:** Up to date with latest design specifications

### 10. Login Screen Updates

**Image Assets:**
- All images changed and updated
- Seamless reload performance
- New visual assets integrated

**Typography Issue - Safari Specific:**

**Problem:**
- Text rendering too bold in Safari
- Does not match design specifications
- Chrome renders correctly

**Root Cause:**
- Safari-specific font rendering
- Browser-level typography handling difference

**Demonstration:**
- Showed same page in Chrome vs Safari
- Chrome: Correct typography weight
- Safari: Over-bold rendering
- Requires Safari-specific fix

**Status:** Being resolved specifically for Safari

### 11. Filter System Updates

**Status:** Filters updated across platform

**Current Focus:** Visual issues requiring resolution

**Team Allocation:**
- Both frontend engineers working on visual fixes
- Dedicated effort to polish and refinement

### 12. Auto-Priority Fee Feature

**Status:** Testing phase

**Purpose:** Optimize Solana transaction costs based on network congestion

**Functionality:**

**User Interface:**
- Toggle switch in settings
- Enabled by default
- User can disable if preferred

**How It Works:**
- Fetches current Solana network congestion
- Calculates optimal priority fee setting
- Adjusts per transaction automatically
- Prevents overspending on low-congestion periods
- Prevents underspending during high-congestion (ensures execution)

**Benefit:**
- "DCA the auto-priority fee" - averages optimal pricing
- Ensures orders reach validator quickly
- Cost-optimized transaction execution

**Quote:**
> "You are not overspending or subspending. Basically that is going to help you get orders in the validator as quickly as possible." - Lucas Cufré

### 13. Documentation Status

**Platform:** Gitbook

**Content Status:** Complete

**What's Included:**
- All currently supported features documented
- User guides
- Technical documentation
- Platform capabilities

**Pending Action:**
- Publish site under proper DNS
- Change from Gitbook domain to docs.cooking.gg
- Publishing mechanism ready, just needs DNS configuration

**Current URL:** Gitbook subdomain (temporary)
**Target URL:** docs.cooking.gg (pending DNS setup)

### 14. Onramper Documentation Review

**Status:** Pending Onramper team review

**Timeline:**
- More than one business day elapsed
- No response yet from Onramper

**Suggested Action:**
- Gregory to ping Onramper team via Telegram
- Direct outreach to expedite review
- Documentation ready on Cooking side

**Blocker:** Waiting on external party response

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Deploy ClickHouse to production | Position updates fully optimized | Resolves critical performance issue |
| Update portfolio to interim design | Leo hasn't provided final design | Enables progress rather than blocking |
| Enable auto-priority fee by default | Optimizes user transaction costs | Better UX, cost savings |
| Use Gitbook for documentation | Standard documentation platform | Professional, maintainable docs |
| Test complete by Monday for production | Weekend development completed | Ready for Monday production testing |
| Gregory to follow up with Onramper via Telegram | Email review taking too long | Direct communication may expedite |
| Both FE engineers on visual fixes | Polish required before launch | Ensures quality user experience |

## Action Items

### High Priority

- [ ] **Frontend Engineers** - Complete visual fixes for Safari typography issue (Due: October 18, 2025)
- [ ] **Frontend Engineers** - Fix vertical spacing on portfolio empty state (Due: October 18, 2025)
- [ ] **Frontend Engineers** - Resolve token details page visual rendering issue (Due: October 18, 2025)
- [ ] **Gregory** - Contact Onramper via Telegram to expedite documentation review (Due: October 18, 2025)

### Medium Priority

- [ ] **DevOps/Team** - Publish Gitbook documentation under docs.cooking.gg DNS (Due: October 20, 2025)
- [ ] **Team** - Deploy all updates to production for Monday testing (Due: October 20, 2025)
- [ ] **Team** - Complete final testing of auto-priority fee feature (Due: October 20, 2025)

### Low Priority

- [ ] **Team** - Obtain final portfolio design from Leo (Due: TBD)

## Technical Notes

### ClickHouse Deployment
- Production deployment successful
- Position update lag eliminated
- Performance now matches dev environment
- No reported issues with migration

### Auto-Priority Fee Implementation
- Queries Solana network congestion
- Calculates optimal priority per transaction
- Default-on with user override option
- Averages costs over time
- Ensures fast validator inclusion

### Browser Compatibility
- Safari typography rendering differs from Chrome
- Requires browser-specific fixes
- Chrome rendering correct
- Issue isolated to Safari font handling

### Inside X Integration
- Bubble maps successfully integrated
- First-time generation delay is external (Inside X API)
- Subsequent loads fast
- Rich wallet interaction visualization

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Onramper documentation review delayed | May delay on-ramp integration | Gregory to ping via Telegram |
| Safari typography rendering issue | Affects iOS/Mac users | Both FE engineers dedicated to fix |
| Leo hasn't provided final portfolio design | Portfolio using interim design | Team moved forward with library design |
| Token details visual bug | Affects badge display | Being fixed today |
| DNS setup for docs.cooking.gg pending | Documentation not on proper domain | Publishing ready, just needs DNS config |

## Next Steps

1. **Immediate:** Complete Safari typography fix (FE Engineers - October 18)
2. **Immediate:** Fix token details rendering issue (FE Engineers - October 18)
3. **Today/Tomorrow:** Gregory contacts Onramper via Telegram (October 18)
4. **Monday:** Production testing with all updates deployed (October 20)
5. **Next Week:** Publish documentation under docs.cooking.gg (October 20)
6. **October 5-7:** Team travel to Dubai for in-person collaboration
7. **October 7-8:** Dubai meetings begin with most team present

## Key Metrics & Numbers

- **ClickHouse deployment:** Production - position updates now real-time
- **Flight durations:** 18 hours (Argentina), 6 hours (Germany), 7 hours (UK)
- **Travel dates:** October 5th departure, October 7th arrival (Lucas/Marcos), October 8th (Gregory)
- **Partner program example:** 380 USDC volume, not yet eligible for 50k tier kickback
- **Documentation review:** >1 business day elapsed
- **Frontend engineers allocated:** 2 (both on visual fixes)
- **Browser testing:** Chrome (correct) vs Safari (typography issue)

## References

- ClickHouse - Database optimization (successfully deployed)
- Inside X - Bubble maps integration provider
- Soul Scan - Solana blockchain explorer
- Gitbook - Documentation platform
- Onramper - On-ramp solution (documentation pending review)
- Dubai - Team meeting location (October 7-8+)
- Leo - Design lead (final portfolio design pending)

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
