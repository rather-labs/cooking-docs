---
title: Cooking Demo - Visual Alignment & Multi-Chart View Discussion
date: 2025-08-22
type: demo
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Naji Osmat
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Vadim Pleshkov
  - Varya Nekhina
  - Marcos Tacca
  - Shakeib Shaida (shakeib98@gmail.com)
  - Rizvi Aseem (rizviaseem2001@gmail.com)
status: completed
tags:
  - demo
  - visual-alignment
  - design-updates
  - ai-journal
  - hyperliquid-integration
  - multi-chart-view
  - leo-designs
  - bubble-maps
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

Shakib Shaida introduced as new technical team member focusing on AI assistant research. Hyperliquid backend integration declared complete pending DNS resolution testing. Lucas proposed postponing multi-chart view to next roadmap to prioritize visual alignment with Leo's designs (typography, colors, buttons, iconography). Rizvi emphasized importance of private beta visual quality matching Leo's standards and using third-party integrations to save development time. Inside X identified for bubble maps integration ($200/month unlimited access, Solana support only). Apple account issues persist; temporary solution proposed using different account for testing. Team confirmed visual updates priority over multi-chart feature, with Leo handling mobile UX/UI alongside Martians' development work.

## Meeting Details

**Duration:** 73 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. New Team Member Introduction

**Shakib Shaida:**
- Technical background, more technical than Naji
- **Primary Role:** Follow-up on technical features, especially AI assistant
- **Focus:** Research for new feature implementation pre-beta launch
- **Special Assignment:** Hyperliquid research to accelerate feature investigation
- **Background:** Previously worked on different division; rotating to Cooking team

**Communication Setup:**
- Shakib requested access to indexing data (token prices, candle data, protocols)
- Lucas to expose API for Drocks team (AI journal developers)
- Slack channel to be created for bilateral communication
- Martin requested design document for explicit interface requirements

### 2. AI Journal Development Strategy

**Context:** External team (Drocks) building AI journal features to accelerate launch.

**Purpose:**
- Reduce pressure on Lucas's team
- Meet tight September deadline
- Allow Lucas's team to focus on core platform features

**Shakib's Support Role:**
- Oversee AI journal development
- Ensure compatibility between teams
- Bridge communication between Drocks and Cooking teams
- Provide indexer data access to expedite development

**Gregory's Emphasis:**
- Timelines extremely tight for September launch
- Essential all other points from roadmap completed on time
- AI journal development offloaded to save bandwidth

### 3. Apple Account Persistent Issues

**Status:** Still blocked; no progress since last week.

**Problems:**
- Cannot access Apple developer portal
- Account locked in verification loop
- Email verification failures
- "Unblock account" → "Verify yourself" → Won't accept email (endless loop)

**Proposed Workaround:**
- Publish from different Apple account temporarily for testing
- Use Tars or other existing account
- **Not for public App Store:** Only for internal TestFlight testing
- Later transition to proper Cooking account for official launch

**Concerns:**
- Lucas uncertain if Apple allows publisher changes
- Could require going through approval process again
- Mystery: Apple's processes "work in mysterious ways"
- Decision: Proceed with workaround to unblock testing

**Zen's Suggestion:**
- Try new email account (not mobile@cooking)
- Generate fresh credentials after call
- Test if different email resolves verification issues

### 4. Backend Development Progress

**Hyperliquid Integration:**
- **Status:** Completely integrated with Hyperliquid
- **Blocker:** DNS records preventing testing
- **Local Testing:** Successful end-to-end
- **Production Testing:** Awaiting DNS resolution
- **Builder Codes:** Implemented; ready to apply surcharges on operations

**Batched Transactions:**
- Successfully integrated limiters
- Finishing batched bridge implementation
- Multiple users share Solana gas fees for Hyperliquid bridge
- Slower than individual bridge but more cost-effective

**Bug Fixes:**
- Hyperliquid testing blocked by DNS (end-to-end tested locally)
- Telegram connection to Chrome resolved
- User wallet creation and interaction fixed
- Security password generation issues resolved
- Custom order table fetching errors fixed

### 5. Upcoming Backend Features

**Next Week Priorities:**
1. **Tal X Login Integration** - Finish and test (by Monday)
2. **Solana Wallet Login** - Finish and test (by Monday)
3. **Referral Program Enhancements:**
   - Custom referral codes implementation
   - Multi-level referral program
4. **Externally Created Wallets:** Support turning external Solana wallets into TurnKey wallets
5. **Wallet Indicators:** Add badges to tables
6. **Bubble Maps:** Introduction of bubble maps feature
7. **Auto-Adjust Priority:** Network condition-based priority fee using Jupiter Swap API

**Indexer Updates:**
- Radium launchpad V2 changes identified and updated
- Special cases mapped for token indexing
- Full indexer review for beta readiness

### 6. Frontend Development Status

**Perpetuals:**
- Still blocked on backend integration
- Everything tested locally; awaiting dev environment deployment

**Bug Fixes:**
- Token details: Symbol vs. name display corrected
- Limit orders: Value overstepping iconography fixed
- Search: Empty state added for failed token fetches
- Copy to clipboard: Toast overflow issues resolved
- Password readability: Improved

**Next Week Priorities:**
1. **New Login Screen:** Social logins, custom referral codes, multi-level referral program
2. **TradingView Chart Updates:** Advanced charts integration
3. **Multi-Chart View:** Under discussion (may be postponed)

### 7. Multi-Chart View vs. Visual Alignment Debate

**Lucas's Proposal:**
- Postpone multi-chart view to next roadmap
- Allocate resources to visual alignment instead
- Focus on: Typography, colors, buttons, iconography
- Achieves ~80% alignment with Leo's designs
- Structural layout already close to Leo's vision

**Rationale:**
- 5 weeks until deadline
- Heavy testing load
- UI outdated; known issues to fix
- Cannot tackle everything: Form changes, iconography, typography, colors, effects
- Multi-chart less critical than visual polish for beta

**Multi-Chart Context:**
- Allows stacking four token charts simultaneously
- Doesn't require paid TradingView subscription (unlike order placement on charts)
- Lucas: Can implement if given extra frontend developer
- Otherwise: Choose between multi-chart OR visual alignment

**Rizvi's Response:**
- **Support postponement:** Multi-chart not essential for private beta
- **Priority:** Visual polish matching Leo's designs
- **Reason:** Private beta users (family, friends, top traders) assess look/feel and trading features
- **Not assessing:** Utility features like multi-chart
- **Current state:** Platform feels like "completely different product" from Leo's designs
- **Must achieve:** Visual consistency for September deadline

**Competitive Strategy Discussion:**
- Competitors (Bullx, Axiom) ship 30+ updates every 1-2 months
- Impossible to compete feature-by-feature
- **Key differentiators for Cooking:**
  1. **AI Assistant:** Optimize trading experience per user
  2. **B2B SDK:** White-label terminal solution for partners
- Use third-party integrations where possible (unless core features)
- Example: Echo's execution (sub-1-second on-chain) - consider partnership vs. building

**Naji's Agreement:**
- Multi-chart not high priority
- Visual alignment critical for first impressions
- September launch important after nearly one year development

### 8. Bubble Maps Integration

**Inside X Selected:**
- Used by Photon, Bullx, and Axiom
- Most common vendor among top competitors

**Pricing Clarification:**
- **Lucas's Initial Research:** $300/month (via native token)
- **Shakib's Correction:** $200/month fixed fee for unlimited access (integration pricing)
- **Consumer pricing:** Different tier ($25k/year mentioned)
- **Conclusion:** Proceed with $200/month plan

**Limitations:**
- **Hyperliquid:** Not supported currently (on roadmap)
- **Scope:** Solana only (spot trading)
- **Not needed for perpetuals:** Order book system with central counterparty (no holder distribution visualization needed)

**Decision:** Implement for spot trading only; Hyperliquid support not needed.

### 9. TradingView Upgrade Decision

**Current Status:**
- Using free TradingView library
- Implementing advanced charts
- Free tier sufficient for beta

**Paid Tier Discussion:**
- **Cost:** $25,000/year
- **Gregory's Suggestion:** Purchase now to avoid surprises later
- **Breakdown:** Maximum $6k spent by September launch
- **Rationale:** Eliminate potential fuckups; ensure stability

**Decision:**
- Upgrade to paid version immediately
- Zen to coordinate payment with Riz
- Naji to provide payment addresses
- Lucas to contact TradingView rep (Joe) to schedule upgrade call

**TradingView Rep Context:**
- Joe has been "pushy" about seeing integration
- Wants to ensure proper implementation
- May want to showcase if well-done
- Team to delay showing until satisfied with quality

### 10. Design Communication & Leo's Role

**Issue:** Design elements not aligning with product logic.

**Examples from Lucas:**
- Advanced orders tab design doesn't scale for all order types
- Custom orders need extensive parameter support
- Leo's proposal uses tabs; Cooking has 5+ order types (DCA, TWAP, VWAP, custom, etc.)
- Tabs would create "infinite scrollable tab section" - poor UX for traders
- Current solution: Dropdown selector (more practical)

**Gregory's Solution:**
- Lucas to identify components that don't align with product logic
- Put in separate Figma file
- Send to Leo urgently for redesign
- Leo currently focusing on mobile (working from scratch)

**Rizvi's Addition:**
- Comment directly on Leo's Figma or communicate however works best
- **Critical:** Fast communication to avoid rework
- Leo working on mobile simultaneously
- Sooner feedback provided, sooner Leo can adjust

**Lucas's Plan:**
- Update internal library to Leo's latest design decisions
- Clone Leo's version for modifications
- Show proposal of screen with modifications
- Communicate misalignments to Leo (Figma comments or separate file)

### 11. Account Management & Referral Program

**Account Management Preview:**
- Spot wallet balance shown
- Perpetual wallet balance shown
- Shared wallet positions aggregated
- Historical PnL with timeline filters
- Position breakdown for multi-wallet holdings
- Rizvi's favorite screen: "Really, really well done"

**Referral Program:**
- Multi-level referral visualization
- Volume rewards display
- Referral tier levels
- Transaction volume of referrals

**Decision:**
- Perpetuals referral program postponed for more consideration
- Current focus: Spot trading referral program only
- Perpetuals complexity requires additional thought

### 12. Audit & Security

**Status:**
- Shakib reviewed contracts
- Changes needed only for art and background elements
- Audit payment pending address from auditor
- Zen to handle payment once address provided

**Emphasis from Zen:**
- Custody and security Shakib's primary responsibility
- Not just identifying risks - making them impossible
- Updates must not cause friction
- No problems can arise
- Gregory reinforced this point with Shakib previously; will follow up again

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Postpone multi-chart view to next roadmap | Prioritize visual alignment with Leo's designs | Resources allocated to typography, colors, buttons, iconography |
| Upgrade to TradingView paid version immediately | Eliminate unknowns; ensure stability (~$6k by Sept) | Zen coordinating payment; Lucas scheduling call with Joe |
| Inside X for bubble maps ($200/month) | Used by top competitors; good pricing | Solana spot only (Hyperliquid not needed) |
| Perpetuals referral program postponed | Needs more consideration; complex | Focus on spot trading referrals for beta |
| Use temporary Apple account for testing | Unblock TestFlight deployment | May need re-approval for final Cooking account |
| Shakib oversees AI journal development | Technical expertise; accelerate research | Drocks team builds AI features; Shakib ensures compatibility |
| Fast design communication with Leo | Avoid rework; he's building mobile too | Lucas to identify misalignments; communicate urgently |

## Action Items

### High Priority

- [ ] **Shakib** - Set up Slack channel with Lucas and Drocks team (Due: August 23, 2025, immediately after call)
- [ ] **Lucas** - Expose indexer API for Drocks team (token prices, candles, protocols) (Due: August 24, 2025)
- [ ] **Zen** - Generate new Apple account credentials with different email; send to Greg (Due: August 22, 2025, after call)
- [ ] **Gregory** - Create temporary Apple developer account for TestFlight testing (Due: August 23, 2025, end of day)
- [ ] **Lucas** - Contact TradingView rep (Joe) to schedule paid version upgrade call (Due: August 23, 2025)
- [ ] **Zen** - Coordinate TradingView payment with Riz (Due: August 26, 2025)
- [ ] **Naji** - Provide payment addresses to Zen for TradingView (Due: August 23, 2025)

### Medium Priority

- [ ] **Lucas** - Update library to Leo's latest designs; show modified screen proposal (Due: August 26, 2025)
- [ ] **Lucas** - Communicate design misalignments to Leo (Figma/separate file) (Due: August 26, 2025)
- [ ] **Lucas & Team** - Complete Tal X and Solana wallet login integration (Due: August 26, 2025)
- [ ] **Team** - Implement custom referral codes and multi-level program (Due: August 29, 2025)
- [ ] **Lucas** - Send meeting minutes with latest agreements and roadmap to Leo (Due: August 23, 2025)

### Low Priority

- [ ] **Zen** - Pay audit fee once address provided (Due: When address received)
- [ ] **Gregory** - Follow-up call with Shakib on custody/security focus (Due: August 24-25, 2025 weekend)
- [ ] **Team** - Implement AWS alert monitoring ($80/month) for CPU usage debugging (Due: August 29, 2025)

## Technical Notes

### API Exposure for AI Journal
- Drocks team needs: Token prices, candle data, protocol information
- Indexer already has all data indexed
- Exposing API accelerates AI journal development
- Martin requested explicit design document for interfaces

### Multi-Chart Implementation
- Requires additional frontend developer if included
- Doesn't need paid TradingView (that's for order placement on charts)
- Can stack four token charts
- Not critical for beta; utility feature vs. core trading

### Visual Alignment Strategy
- Structural layout already ~90% aligned
- Main differences: Typography, colors, buttons, iconography, spacing
- 80% target achievable with focused effort
- Layout modifications are heaviest work (deferred)

### Bubble Maps Technical Details
- Inside X integration: $200/month unlimited
- Solana support only (Hyperliquid on roadmap)
- Not needed for perpetuals (order book system)
- Used by Photon, Bullx, Axiom

### Advanced Orders Complexity
- Custom orders most complex scenario
- Multiple conditionals: price, liquidity, holders, time, etc.
- Leo's tab design doesn't scale
- Dropdown selector more practical for 5+ order types

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Apple account verification loop | TestFlight testing blocked | Try new email; use temporary account for testing |
| DNS records not resolved | Hyperliquid testing on deployed environment blocked | Zen investigating; works locally |
| Leo's designs not aligning with logic | Rework if not caught early | Fast communication; Lucas identifying issues |
| Multi-chart vs. visual alignment tradeoff | Feature sacrifice required | Team agreed: Visual alignment priority |
| AI journal timeline | Could impact September deadline | Offloaded to Drocks team with Shakib oversight |
| TradingView surprise issues | Could derail perpetuals | Upgrading to paid version now ($25k/year) |
| CPU usage spikes on AWS | Performance degradation | Implementing alerts ($80/month) for debugging |

## Next Steps

1. **Immediate:** Set up Drocks Slack channel; create new Apple account attempt
2. **This Week:** Schedule TradingView upgrade call; expose indexer API; update designs to Leo's standards
3. **Next Week:** Complete social login integrations; implement custom referrals; finish visual alignment
4. **Ongoing:** AI journal development by Drocks; Shakib ensures compatibility
5. **Monday Call:** Discuss next roadmap (excluding AI journal for now)

## Key Metrics & Numbers

- **Time to deadline:** 5 weeks (from August 22 to end September)
- **TradingView paid version:** $25,000/year (~$6k by September)
- **Inside X bubble maps:** $200/month (unlimited access)
- **AWS monitoring alerts:** $80/month
- **Competitor update frequency:** 30+ updates every 1-2 months (Bullx, Axiom)
- **Development timeline:** Nearly 1 year by September
- **Visual alignment target:** 80% match to Leo's designs

## References

- Inside X - Bubble maps provider
- Drocks - External AI journal development team
- Shakib Shaida - New technical team member
- TradingView - Advanced charting library
- Echo - Sub-1-second execution benchmark
- Leo - Lead designer (Cooking web and mobile)
- Tal X (Twitter/X) - Social login integration
- Jupiter Swap API - Priority fee auto-adjustment

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
