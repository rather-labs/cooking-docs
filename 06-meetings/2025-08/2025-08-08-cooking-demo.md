---
title: Cooking Demo - Roadmap Approval & Backend Refactoring
date: 2025-08-08
type: demo
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Naji Osmat
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Vadim Pleshkov
  - Varya Nekhina
  - Marcos Tacca (LAABS Head of Projects)
  - Rizvi Aseem
status: completed
tags:
  - demo
  - roadmap
  - backend-refactoring
  - hyperliquid-integration
  - mobile-ux
  - design-review
  - geoblocking
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

Lucas Cufré introduced Marcos Tacca as LAABS' new Head of Projects. The team awaits roadmap approval while proceeding with backend refactoring for Hyperliquid perpetuals to overcome geoblocking in Ohio. Backend migration from monolith to monorepo is essential but not yet complete. Fee structures for Hyperliquid deposits/withdrawals were discussed, with builder codes already implemented in production. Mobile app design received feedback about not meeting visual standards compared to the web app, with plans for Leo to handle final UX/UI. Three features (multi-language, market cap algorithm, portfolio TP/SL) confirmed for Q4 to accommodate refactoring scope.

## Meeting Details

**Duration:** 56 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Introduction of New Team Members

**Context:** Team introductions and role clarifications.

**Key Points:**
- **Marcos Tacca:** Introduced as LAABS Head of Projects, coordinating multiple projects
- **Vadim Pleshkov:** Evil Martians account manager
- **Varya Nekhina:** Evil Martians designer
- **Rizvi Aseem:** Joined later in call for design discussions

### 2. Roadmap Approval Status

**Status:** Not yet approved by executive leadership.

**Blockers:**
- Gregory Chapman still awaiting domain approval for "Apple account issue"
- No personal contact with leadership since previous call

**Action Required:**
- Final executive approval needed before proceeding
- Team operating under interim approval assumption

### 3. Backend Refactoring for Hyperliquid

**Context:** Essential refactoring to overcome geoblocking issues.

**Technical Details:**
- **Current Architecture:** Monolithic application on AWS Ohio server
- **Problem:** Hyperliquid geoblocks Ohio IP addresses
- **Solution:** Relocate Hyperliquid service instance to non-geoblocked location
- **Migration:** Monolith → Monorepo architecture

**Key Clarification:**
- Naji initially thought refactoring was complete
- Lucas clarified: Refactoring necessary to deploy service instances in different geolocations
- Allows users to connect to Hyperliquid from various locations

**Impact on Roadmap:**
- Initial scope no longer achievable with refactoring included
- Three features pushed to Q4 as discussed previously
- Team confident in meeting deadline with adjusted scope

### 4. Hyperliquid Fee Structures

**Deposit/Withdrawal Fees:**
- **Bidirectional:** Solana ↔ USDC (both directions chargeable)
- **Fee Types:** Percentage fee and/or flat fee supported
- **Two Modes:**
  - Fast mode: Higher fees
  - Slow mode: Lower fees, allows larger profit participation

**Builder Codes:**
- Already implemented in Hyperliquid production API
- Allows developers to impose specific transaction fees
- Complexity assessment ongoing for integration
- Implementation dependent on current backend refactoring workload

**Fee Attribution:**
- Surcharge portion (builder code) subject to partner commission program
- Hyperliquid's own fees cannot be controlled (except via treasury staking in future)
- Controllable fees treated same as other cooking fees for referral system

**Decision Needed:**
- Lucas requested confirmation on bridge fee percentages
- Naji to provide fee structure similar to spot trading fee document
- Bridge fees apply to both deposit and withdrawal

### 5. Backend Development Progress

**Completed:**
- Let's Punk implementation
- Radium launchpad integration
- Liquidity and bonding curve database updates
- Auth0 with TurnKey integration (improved user creation handling)

**In Progress:**
- Hyperliquid contract information for traded assets (nearly complete)
- USDC asset withdrawal to Solana (nearly complete)
- Integration and testing (blocked by monorepo migration)

**Indexer Improvements:**
- Fixed bug in total holders calculation
- Performance improvements for Let's Punk blocks
- All changes dependent on ClickHouse integration

### 6. Frontend Development Updates

**Completed:**
- Let's Punk support added with filter refactoring
- Multiple bonding provider support
- Perpetuals UI nearly ready for dev deployment
- Synchronization with previous Figma component versions (Leo's earlier work)

**Blocked:**
- Testing perpetuals UI (awaiting backend completion)
- QA testing for first initiative (signup, login, home) blocked by Apple account
- TestFlight environment unavailable without Apple account

**First Initiative Status:**
- Signup, login, and home pages considered tentatively complete
- Cannot proceed with QA without TestFlight access
- Earlier testing means earlier Apple approval process initiation

### 7. Mobile Design Standards Discussion

**Vadim's Presentation:**
- Wallet page with three tabs: positions, pending orders, history
- Improved header with more compact position view
- Optional fields: time-to-live, stop-loss/take-profit
- Color mapping: Purple (future events), Green (successful), Red (failed/cancelled)

**Gregory's Feedback:**
- Visual design doesn't meet Cooking's tier-one standards
- UX is solid and on track
- Visually not enticing or "happy to look at"
- Doesn't reflect premium product with millions in development investment
- Comparison: Would Trading 212, Robin Hood, or Binance use these designs?

**Discussion Points:**
- Vadim explained mobile requires larger, more accessible elements (Apple guidelines)
- Less "tight and compact" than desktop due to touch interface requirements
- Lucas defended using same typeface, color palette, and components
- Gregory and Naji expressed concerns about final quality not meeting expectations

### 8. Design Strategy Pivot

**Leo's Involvement:**
- Leo to handle final UX (not just UI as originally planned)
- Leo already showing "drastic improvements" in 24 hours
- Leo's experience:
  - Previously worked with Robin Hood during their prime
  - Understands trading product standards
  - Knows mobile user expectations for financial apps

**Reasoning:**
- Leo most familiar with Cooking project
- Better to have single designer handle both UX and UI
- Requires communication on specific flow details (e.g., stop loss/take profit mechanics)

**Timeline Strategy:**
- Continue with current Martians designs through September
- Leo needs ~2 weeks to complete his designs
- Post-September: 1-2 week sprint to implement Leo's visual updates ("V2")
- Allows Leo time to prepare, receive feedback, iterate

**Rizvi's Context:**
- Two ways for Cooking to dominate: AI assistant and B2B software kit (SDK)
- Focus on core differentiators rather than competing feature-by-feature
- Use third-party integrations where possible to save development time
- Private beta users will assess look, feel, and trading features (not utilities like multi-chart)

### 9. Roadmap Adjustments Confirmed

**Features Pushed to Early Q4:**
1. **Multi-language support** - Only needed for public launch
2. **Market cap algorithm** - Too advanced for private beta users
3. **Portfolio-level TP/SL** - Includes both portfolio-wide and individual position management

**Prioritization for Q4:**
- Portfolio TP/SL prioritized first (most valuable)
- Two-fold feature:
  - Portfolio-wide thresholds (set and forget)
  - Individual position management (for users who DCA into positions)

**Rationale:**
- Private beta primarily family, friends, and top traders
- Focus on core trading features, not utility features
- High-profile partners expect polished, tier-one product
- September = one year of development; time to launch

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Proceed with interim roadmap approval | Cannot delay while awaiting executive confirmation | Team working at risk until formal approval |
| Backend refactoring essential for perpetuals | Hyperliquid geoblocking requires architecture change | Three features moved to Q4 |
| Leo handles both UX and UI for mobile | Better consistency; Leo knows Cooking best | Martians delivers to September, Leo's V2 follows |
| Continue development with Martians designs | Enable immediate development progress | Visual polish sprint after September |
| Prioritize portfolio TP/SL in Q4 | Most valuable feature for users | Multi-language and market cap lower priority |
| Bridge fees subject to referral program | Consistency across all Cooking fees | Partner commission applies to controllable fees |
| Use private beta for feature validation | Not all users need every feature | Focus on core differentiators |

## Action Items

### High Priority

- [ ] **Naji** - Obtain final roadmap approval from executive leadership (Due: August 12, 2025)
- [ ] **Gregory** - Resolve domain approval for Apple account (Due: August 10, 2025, URGENT)
- [ ] **Naji** - Provide bridge fee structure document (deposit/withdrawal percentages) (Due: August 10, 2025)
- [ ] **Lucas & Martin** - Complete backend monorepo refactoring (Due: Ongoing through August)
- [ ] **Martin** - Update DNS records for AWS configuration (Due: Immediately, URGENT)

### Medium Priority

- [ ] **Lucas & Team** - Assess builder codes implementation timeline (Due: August 15, 2025)
- [ ] **Leo** - Complete UX/UI designs for mobile app (Due: August 22, 2025, ~2 weeks)
- [ ] **Vadim & Lucas** - Identify design elements not aligning with product logic (Due: August 12, 2025)
- [ ] **Team** - Schedule weekly sync for Tuesday instead of Friday (Due: August 13, 2025)

### Low Priority

- [ ] **Lucas** - Share initiatives with Leo for product definition guidance (Due: August 10, 2025)
- [ ] **Lucas** - Send email with meeting minutes and roadmap updates (Due: August 8, 2025)
- [ ] **Team** - Plan Q4 roadmap details with reprioritized features (Due: August 22, 2025)

## Technical Notes

### Backend Architecture
- Monolith to monorepo migration critical path
- Hyperliquid service requires European deployment (non-geoblocked)
- Separate service deployment for different geolocations
- Budget considerations for infrastructure restructuring

### Builder Codes Implementation
- Hyperliquid API endpoint already in production
- Allows fee imposition on wallets under Cooking control
- Integration complexity assessment ongoing
- Dependent on refactoring completion timeline

### Mobile Design Considerations
- Apple guidelines require larger touch targets
- Cannot directly translate desktop designs one-to-one
- Mobile ecosystem inherently different from web
- Balance between visual polish and usability

### Performance Considerations
- ClickHouse integration critical for improvements
- Indexer optimizations for Let's Punk
- Database updates for liquidity and bonding curves

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Roadmap not formally approved | Working at risk; potential direction changes | Naji pursuing executive approval urgently |
| Apple account domain issues | Cannot access TestFlight for testing | Gregory working on domain approval |
| DNS records not updated | Blocks backend refactoring testing | Martin to update immediately |
| Backend refactoring complexity | Potential timeline impacts | Three features moved to Q4 to compensate |
| Mobile design quality concerns | First impressions with key partners at risk | Leo taking over final UX/UI; V2 sprint planned |
| September deadline pressure | Quality vs. speed tradeoff | Focused scope with post-launch improvements |
| Geoblocking uncertainty | Hyperliquid access issues | Monorepo architecture enables geographic flexibility |

## Next Steps

1. **Immediate:** Obtain roadmap approval and resolve Apple account domain issues
2. **This Week:** Provide bridge fee structure; continue backend refactoring
3. **Next Week:** Reassess timelines and deliverables for September (Tuesday sync meeting)
4. **Two Weeks:** Leo completes mobile UX/UI designs
5. **September:** Deploy with Martians designs; plan Leo's V2 implementation sprint
6. **Q4:** Implement multi-language, market cap algorithm, portfolio TP/SL

## Key Metrics & Numbers

- **Development timeline:** Nearly 1 year by September
- **Leo's design turnaround:** ~2 weeks expected
- **Visual update sprint:** 1-2 weeks post-September
- **Features pushed to Q4:** 3 (multi-language, market cap algo, portfolio TP/SL)
- **Bridge fee modes:** 2 (fast and slow)
- **Backend architecture:** Monolith → Monorepo (major refactoring)

## References

- Hyperliquid - Perpetuals trading platform integration
- Builder Codes - Hyperliquid fee imposition API
- Auth0 & TurnKey - Authentication and wallet services
- Leo - Lead designer for Cooking (web and mobile)
- Evil Martians - External design agency (Vadim and Varya)

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
