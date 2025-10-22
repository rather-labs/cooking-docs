---
title: Cooking Demo - Let's Punk Integration & Mobile Design Review
date: 2025-08-01
type: demo
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Naji Osmat
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Vadim Pleshkov
  - Varya Nekhina
status: completed
tags:
  - demo
  - lets-punk-integration
  - mobile-design
  - hyperliquid
  - backend-refactoring
  - apple-account-issues
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team completed Let's Punk integration including backend, indexer, and frontend implementations. Backend refactoring toward monorepo architecture is essential for Hyperliquid perpetuals functionality due to geoblocking issues. Mobile design standards were discussed with concerns raised about visual polish not matching web app quality. Significant blockers include Apple developer account issues and DNS record updates needed for AWS configuration. The team agreed to postpone multi-language support, market cap algorithm, and portfolio-level stop loss/take profit features to early Q4.

## Meeting Details

**Duration:** 53 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Backend Development Updates

**Context:** Lucas Cufré reported on backend implementation progress.

**Key Points:**
- **Let's Punk Integration:** Completed native token operation support for Let's Punk
- **Turnkey Updates:** Simplified wallet creation logic and improved scalability for social login implementation
- **Indexer Work:** Finished Let's Punk implementation (both backend and indexer)
- **Radium Launchpad:** Integrated as required for Let's Punk support
- **Database Updates:** Updated liquidity and bonding curve databases with specific values and parameter expressions

**Technical Details:**
- Integration timeline: Approximately 10-14 days (7 days typical baseline)
- Complexity varies by protocol dependency
- Let's Punk heavily dependent on Radium, enabling faster implementation

### 2. Frontend Progress

**Key Implementations:**
- Added Let's Punk support with filter refactoring for multiple bonding providers
- Improved UI with switches instead of checkboxes for protocol visibility
- Switch design: On = protocol shown, Off = filtered out
- At least one protocol must remain selected at all times

**User Experience Improvements:**
- Clearer interface: "Hide" vs "Check" confusion eliminated
- Intuitive protocol filtering
- Prevention of user errors (at least one protocol always active)

### 3. Mobile App Status

**Completed:**
- Kitchen integration
- Home UI implementation

**Blocked:**
- QA testing blocked by Apple account issues
- Cannot create business account (insufficient employee count)
- Greg took over personal account creation but encountered issues

**Apple Account Issues:**
- Email domains not accepted (.com, cooking.gg, Gmail all rejected)
- Greg and Martin both attempted setup
- Critical blocker for TestFlight deployment

### 4. Backend Refactoring for Hyperliquid

**Context:** Monolith to monorepo migration required for perpetuals functionality.

**Technical Requirements:**
- Current: Monolithic server in Ohio, AWS
- Problem: Ohio IP geoblocked by Hyperliquid
- Solution: Separate service instance in non-geoblocked location (Europe)
- Architecture change: Move from horizontal scaling monolith to independent microservices

**Impact:**
- Significant scope change to roadmap
- Three features pushed to Q4
- Essential for perpetuals functionality

### 5. Fee Structure & Builder Codes

**Bridge Fees:**
- Bidirectional: Solana → USDC and USDC → Solana
- Two modes:
  - Fast mode: Higher fees
  - Slow mode: Lower fees, larger profit share
- Fee types: Both percentage and flat fees supported

**Builder Codes:**
- Hyperliquid API already deployed to production
- Allows developer-imposed specific fees on transactions
- Complexity assessment ongoing
- Implementation timeline dependent on refactoring workload

**Key Decision:**
- Surcharge (builder code) subject to partner commission system
- Bridge fees for controllable portions follow standard referral structure

### 6. Mobile Design Standards Discussion

**Context:** Vadim Pleshkov presented wallet page designs with three main tabs: positions, pending orders, and history.

**Gregory Chapman's Concerns:**
- Visual quality doesn't meet web app standards
- UX acceptable, but design quality insufficient for tier-one product
- Product represents millions in investment; must reflect that visually

**Lucas Cufré's Defense:**
- Same color palette and components used
- Mobile and web ecosystems inherently different
- Direct one-to-one translation not possible
- Focus on simplifying inherently complex product for novice users

**Resolution:**
- Vadim to consult with Lucas on visual adjustments
- Development can begin immediately
- Team acknowledged urgency of building visually premium product

### 7. Timeline Pressures

**Deadlines:**
- Application in development for nearly a year (September = one year mark)
- Many key partners and influencers waiting for launch
- Private beta needed by September for initial users
- Continuous delays to match competitors unsustainable

**Balancing Act:**
- Less features polished vs. all functionality with design compromise
- Gregory: Cannot reduce feature set; must be tier-one product
- Naji: Must launch to start acquiring users; improvements always possible later

### 8. Settings and Configuration UI

**Proposed Solution:**
- Sidebar modal for account-level configurations
- Features: Profile picture, Cooking tag, login methods setup
- Help center and keyboard shortcuts per screen
- Work in progress, pending final implementation

### 9. Roadmap Reassessment

**Pushed to Q4:**
1. Multi-language support
2. Market cap algorithm
3. Portfolio-level stop loss/take profit

**Rationale:**
- Backend refactoring for Hyperliquid geoblocking more complex than expected
- Three-item delay enables September deadline achievement
- Features reassessed based on private beta feedback

**Priority Discussion:**
- Portfolio TP/SL deemed most important (both portfolio-wide and individual entry levels)
- Multi-language only needed for public launch (not private beta)
- Market cap algorithm too advanced for private beta

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Push three features to Q4 | Backend refactoring complexity for Hyperliquid | Enables September deadline |
| Approve backend monorepo refactoring | Required for perpetuals functionality | Major architecture change |
| Define builder codes as priority | Essential for operation and revenue | Subject to partner commission system |
| Bridge fees bidirectional with two modes | Optimize user experience and profit | Fast and slow mode implementation |
| Continue with current mobile designs | Enable development to proceed immediately | Visual polish as follow-up work |
| Apple account resolution needed urgently | Critical path for TestFlight testing | Greg to continue troubleshooting |
| Prioritize portfolio TP/SL for early Q4 | Most valuable feature for users | Multi-language and market cap lower priority |

## Action Items

### High Priority

- [ ] **Greg** - Resolve Apple developer account issues; try alternative email solutions (Due: Immediately, URGENT)
- [ ] **Martin** - Update DNS records on NameCheap for AWS configuration (Due: Immediately, URGENT)
- [ ] **Lucas & Team** - Complete backend refactoring for Hyperliquid geoblocking (Due: Ongoing through August)
- [ ] **Naji & Greg** - Define and confirm bridge fee structure (both fast and slow modes) (Due: August 5, 2025)

### Medium Priority

- [ ] **Lucas & Martin** - Assess builder codes implementation complexity and timeline (Due: August 8, 2025)
- [ ] **Vadim & Lucas** - Refine mobile designs to better align with web app visual quality (Due: August 15, 2025)
- [ ] **Team** - Finalize Q4 roadmap with reprioritized features (Due: August 8, 2025)

### Low Priority

- [ ] **Lucas** - Send meeting minutes (Due: August 1, 2025)
- [ ] **Team** - Review and approve updated timeline documentation (Due: August 5, 2025)

## Technical Notes

### Backend Architecture Changes
- Migration from monolith to monorepo required
- Hyperliquid service needs European deployment (non-geoblocked)
- Microservices architecture for independent deployment
- Budget implications for infrastructure restructuring

### Protocol Integration Timeline
- Baseline: 7 days typical
- Range: 5-9 days depending on complexity
- Let's Punk: ~10-14 days (with Radium dependency advantage)
- Complexity factors: Protocol-provided data completeness

### Fee Implementation
- Bidirectional bridge fees supported
- Builder codes (Hyperliquid API) already in production
- Referral system integration for fee discounts
- Flat fee and percentage fee both supported

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Apple developer account blocked | Cannot deploy TestFlight for testing | Greg trying alternative email solutions |
| DNS records not updated | Blocks backend refactoring completion | Martin to update immediately on NameCheap |
| Mobile design quality concerns | First impression risk with partners | Vadim to enhance visual polish while dev proceeds |
| Backend refactoring complexity | Potential timeline delays | Three features moved to Q4 to compensate |
| September deadline pressure | Quality vs. speed trade-off | Focused scope with Q4 follow-up features |

## Next Steps

1. **Immediate:** Resolve Apple account and DNS records (critical path blockers)
2. **This Week:** Complete bridge fee structure definition
3. **Next Week:** Assess builder codes complexity; finalize Q4 roadmap
4. **Ongoing:** Backend refactoring for Hyperliquid perpetuals
5. **August:** Complete perpetuals integration and mobile development

## Key Metrics & Numbers

- **Development timeline:** ~1 year by September deadline
- **Protocol integration:** 7-9 days typical
- **Let's Punk integration:** 10-14 days
- **Backend refactoring:** Significant effort (multiple weeks)
- **Features pushed to Q4:** 3 (multi-language, market cap algo, portfolio TP/SL)
- **Mobile app progress:** Kitchen integration and Home UI complete

## References

- Let's Punk - New bonding curve protocol integration
- Radium Launchpad - Dependency for Let's Punk
- Hyperliquid - Perpetuals trading integration
- Turnkey - Wallet creation service
- Builder Codes - Hyperliquid fee API

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
