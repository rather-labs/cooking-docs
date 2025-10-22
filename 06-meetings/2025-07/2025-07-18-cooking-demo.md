---
title: Cooking Demo - On-Ramp Decision & Mobile Design Direction
date: 2025-07-18
type: demo
attendees:
  - Lucas Cufré
  - Gregory Chapman (greg@ember.app)
  - Martin Aranda
  - Naji Osmat
  - Zen (z@ember.app)
  - Vadim Pleshkov
  - Varya Nekhina (varya@evilmartians.com)
status: completed
tags:
  - demo
  - onramper
  - mobile-design
  - wallet-ux
  - lets-bank
  - martians
related:
  - "[[2025-07-11-cooking-demo]]"
  - "[[04-knowledge-base/technical/integrations/onramper]]"
  - "[[04-knowledge-base/design/mobile-app]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team finalized the decision to use Onramper over Crossmint for on-ramp/off-ramp integration due to superior documentation, revenue sharing model, and redundancy through aggregation. Vadim Pleshkov from Evil Martians presented comprehensive mobile app designs for wallet, token details, and history pages, proposing a simplified money visualization separating Solana balance from meme coin portfolio. A critical UX decision was made to simplify transaction buttons from four options (Deposit/Top-up/Swap/Withdraw) to two (Top Up/Cash Out). The Martians team estimated completion of all main screens by end of August (6 weeks), with priority on functionality over visual refinements to meet the September deadline.

## Meeting Details

**Duration:** 1 hour 2 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Development Progress Updates

**Backend & Integration:**
- Hyperliquid backend integration development operational
- Solana deposit flow now fully functional in dev environment
- JUP-listed tokens now fully supported in development
- Pump Swap transaction parsing errors corrected
- Radium trade performance improved

**Frontend:**
- Testing finalized for search token model
- Batch operations, table selects, dialogs, toasts, and inputs tested
- Perpetuals section rebuild using current library:
  - Wallet select component
  - Dashboard section (above charts)
  - Perpetual contract search model
  - Deposit flow model
  - Convert Solana to USDC model

**Mobile:**
- Martian mobile engineer onboarding in progress
- Research completed on on-ramping solutions
- Telegram login finished and tested
- Home, signup, and login flows continuing

**Let's Bank Integration:**
- Indexer portion nearly complete
- Capable of indexing tokens for Jupiter trading
- Full implementation expected by following week
- Architecture compatible with existing platform (similar to Radium)

### 2. On-Ramp Solution: Onramper vs. Crossmint

Lucas presented detailed research comparing the two solutions.

**Crossmint Analysis:**

**Advantages:**
- Unique no-KYC checkout experience for specific items (meme coins, NFTs)
- AML certification (crucial for App Store compliance)
- Integration flexibility (embeddable widget and headless API)
- Mobile-first design

**Disadvantages:**
- **Critical:** Limited functionality documentation
  - Cannot determine transaction routing
  - Unclear which protocols users access
  - Risk of users accessing unsupported tokens
  - No information on off-ramp functionality
- Regulatory limitations (OFAC restrictions in US)
- Operational constraints:
  - Gas fee requirement issue (users stuck without Solana)
  - Commercial uncertainty (no public pricing, must contact sales)
  - Significant friction for agile development

**Onramper Analysis:**

**Advantages:**
- Ramp aggregator (25+ on-ramp providers, 7+ off-ramp)
- Comprehensive coverage across regions
- Intelligent routing and KYC optimization
- Clear commercial structure ($2,000/year essential plan for 6 on-ramps)
- No direct fees to end users (revenue from volume kickback)
- 2.5% average savings per transaction for users
- Margin opportunity for Cooking on saved costs
- **Superior documentation** (one of best Lucas has seen)
- Geographic restrictions handled via aggregator redundancy
- Direct communication channel (Greg and Naji have Telegram/email contact)

**Disadvantages:**
- No direct fiat-to-meme-coin checkout flow
- Requires established entity for business agreement
- Cannot operate in gaming/gambling industries
- AML certification status needs confirmation

**Revenue Model Insight:**
Onramper doesn't charge end users directly; they earn from volume-based kickbacks from providers. The 2.5% average savings can be partially captured by Cooking while still offering competitive rates.

**Team Discussion:**

**Gregory:** "We do have direct comms with them [Onramper] as well. That could probably make things a lot easier."

**Lucas's Recommendation:**
> "I would highly recommend you guys to go with Onramper instead of Crossmint for all of these things... basically documentation, redundancies, revenue sharing, cost transparency."

**Naji's Response:** Agreed Onramper is superior option, needs final confirmation on Crossmint checkout from Riz but considers it something that can be added later.

**Final Decision:** Proceed with Onramper as primary on-ramp/off-ramp solution

### 3. Integration Approach: Widget vs. Headless API

**Lucas's Recommendation:** Use widget route

**Reasoning:**

**Widget Benefits:**
- Handles all edge cases already (network errors, bank failures, KYC issues)
- Each edge case can spawn multiple steps
- Already optimized user experience
- Can be customized and styled to match Cooking branding
- Web view integration appears native to users
- Feasible within September timeline

**Headless API Challenges:**
- Requires custom UI for every scenario
- Exponential edge cases to handle:
  - Network errors
  - Bank approval failures
  - KYC verification issues
  - Multiple verification flows
  - Status updates and confirmations
- Significant development time
- Not achievable by October 1st deadline

**Implementation Options:**
1. Hosted form with URL (e.g., crossmint.cooking.com in browser)
2. Embedded web view (appears native within app)

**Styling Capabilities:**
- Dark mode support
- Customizable radius, colors
- Can remove header to avoid double headers
- White-label option (remove "powered by" branding - may require enterprise tier)

**Decision:** Use widget integration (embedded web view approach)

**Strategic Note:** Can always switch to headless API in future, but widget enables faster time-to-market.

### 4. Mobile App Design Presentation (Vadim Pleshkov)

Vadim presented comprehensive design work for the mobile application.

**Application Map Overview:**
- Identified all main screens to be built
- Marked screens potentially deferrable post-launch:
  - Onboarding sequence (can use existing tutorial)
  - Some referral features
  - Connected accounts (easy to add later)
  - Help center (GitBook external solution)

**Priority Focus:**
- Main page/home
- Wallet page with cash in/out
- Portfolio view
- Wallet settings
- Settings page

**Estimated Timeline:** All main screens complete by end of August (6 weeks) with 80% confidence

### 5. Wallet Screen Design & Money Visualization

**Current Challenge:** Solana listed as one position among others in wallet - "Web3 way of thinking" that frustrates newer users.

**Proposed New Approach:**

**Two-Tier Visualization:**

1. **Balance (Available to Spend):**
   - Solana balance explicitly shown
   - Labeled as "available to spend"
   - What user can use to buy coins or cash out

2. **Portfolio (Accumulated Value):**
   - Sum of all meme coins owned
   - Separate from Solana balance
   - Not included in available balance

**Mental Model:** Similar to Robinhood
- "Buying power" (Solana balance)
- "Stocks/holdings" (meme coin portfolio)

**Example Flow:**
- User sells 100 Solana worth of coins
- Balance increases by 100 Solana
- Portfolio decreases by 100 Solana equivalent
- Clear movement between the two categories

**Team Response:**

**Lucas (Conceptually):** Agrees with concept, recommends exploring:
- Number length handling (up to 6 decimal places in crypto)
- Visual hierarchy between balance and portfolio
- Container/card treatment to clarify relationship
- Clear indication that portfolio results from balance conversion

**Naji:** Supportive of the concept as a test approach

**Decision:** Proceed with two-tier visualization concept, pending visual refinement

### 6. Transaction Button Simplification

**Current Approach:** Four buttons with confusing labels
- Deposit
- Top Up
- Swap
- Withdraw

**Vadim's Proposal:** Two simple buttons
- **Top Up:** Money into wallet
- **Cash Out:** Money out of wallet

**Top Up Flow Options:**
1. Transfer Solana from another wallet (internal transfer)
2. Top up from Onramper (on-ramp widget)

**Cash Out Flow Options:**
1. Withdraw to another wallet
2. Cash out via Onramper (off-ramp widget)

**Benefits:**
- More friendly for users
- Clear intent: adding or extracting money
- Simpler mental model
- Standard financial app pattern

**Naji's Response:** "I do like this as a test concept. Yeah, I think it's good."

**Decision:** Implement simplified two-button approach (Top Up / Cash Out)

**Implementation Note:** Accessibility considerations for font resizing to be addressed in technical implementation

### 7. Token Details & History Event Pages

**Token Card Design:**
- Revised card view for clarity
- Working with Lucas on internal structure
- Visual refreshes planned incrementally
- Market details included
- Security considerations section with explanatory sheet (cryptic icons explained on tap)
- Token address and links
- Pending and history views

**History Event Page:**

**Two-Section Design:**

1. **Colorful Top Section (Essence):**
   - Transaction summary at a glance
   - Amount spent and received
   - Visual clarity on what happened

2. **Details Section (Transaction Details):**
   - Exact price information
   - Fee breakdown
   - Calculation-ready data
   - Order status (fulfilled/failed/created)
   - For pending orders: stop loss and take profit details

**Design Philosophy:**
- Standard iOS stamper component reused throughout
- Easier to build (fits deadline)
- Direct navigation from notifications
- Pending orders page uses same template with additional TP/SL information

**Vadim's Plan:** Complete full wallet page next week for developer handoff

### 8. Design-to-Development Workflow

**Developer Access:**
- Direct access to Figma file
- Work from live designs
- Inspect components directly

**Design Delivery Format:**

**Banner Information:**
- Flow name
- Screen list
- Version number
- Changes from previous version

**Version Control:**
- Two active versions typically:
  - Production version (deployed)
  - Next version (with modifications)
- Team works from versioned designs

**Screen Components:**
- Main screens with full complexity
- All variants documented
- Elements with annotations
- Models and flow diagrams
- Source components shown

**Visual Language Changes:**
- Will occur but version-controlled
- Structural changes minimal once established
- Stylistic changes (colors, systems) require cleanup time
- Developers focus on structure, styling can be adjusted as work progresses

**Example Deliverable:** Wallet manager version with screens, variants, annotations, and component sources

### 9. Development Timeline Estimation

**Varya's Projection:**
- All main screens complete by end of August
- 80% confidence level
- Approximately 6 weeks from current date (July 18)

**Considerations:**
- Potential for unknown issues
- Possible feature additions
- Initial realistic estimation
- Prioritizing essential features only given tight deadline

**Lucas's Suggestions for Optimization:**

1. **Contextual Features:**
   - Trading operations in modal sheets instead of full screens
   - Reduces complexity and screen count

2. **Referrals Page:**
   - Reduce complexity
   - Simplify to basic fields for referral code
   - Detailed explanations to GitBook instead of in-app

3. **Help Center:**
   - GitBook as primary strategy
   - Avoid building in-house help center
   - Point to external documentation

**Vadim's Confirmation:** Can simplify screens to essential functionality while maintaining usability

### 10. Widget Integration for Cash Operations

**Varya's Question:** Clarified use of widgets for cash in/out sections

**Vadim's Confirmation:**
- Onramper widget used for these flows
- Shows web view at appropriate point
- Greatly reduces team involvement
- Only needs to know when transaction completes
- Can then return user to main page with updated balance

**Impact on Scope:**
- Significantly reduces design and development time
- No need to manually create complex on-ramp flows
- Widget handles all edge cases
- Ideal solution for timeline constraints

**Vadim's Approval:**
> "Perfect. I totally agree with this decision especially with the time constraints."

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Select Onramper over Crossmint | Superior documentation, revenue sharing, redundancy | Primary on-ramp/off-ramp solution |
| Use widget integration (not headless API) | Time constraints, handles edge cases | Faster implementation, defer custom UI |
| Implement two-tier money visualization | Clearer for normie users | Better UX, familiar mental model |
| Simplify to two transaction buttons (Top Up/Cash Out) | Less confusing than four options | Improved user clarity |
| Use embedded web view for widgets | Appears native to users | Seamless experience |
| Complete main screens by end August | Realistic timeline assessment | 6-week delivery target |
| Defer visual refinements if needed | Functionality over aesthetics | Meet September deadline |
| Use GitBook for help documentation | Faster than in-app help center | External documentation solution |
| Simplify referrals page | Reduce complexity | Focus on core functionality |
| Implement trading operations as modals | Instead of full screens | Reduce screen count, faster development |

## Action Items

### High Priority

- [ ] **Naji** - Get final confirmation on Crossmint checkout deprioritization from Riz (Due: July 22, 2025)
- [ ] **Vadim** - Complete full wallet page design for developer handoff (Due: Week of July 21, 2025)
- [ ] **Vadim** - Finalize two-tier money visualization with number length handling (Due: July 25, 2025)
- [ ] **Team** - Confirm Onramper AML certification status for App Store (Due: July 25, 2025)

### Medium Priority

- [ ] **Backend Team** - Complete Let's Bank full implementation (Due: Week of July 21, 2025)
- [ ] **Vadim** - Move to token details page after wallet completion (Due: Early August, 2025)
- [ ] **Varya & Vadim** - Maintain version control on design files (Due: Ongoing)
- [ ] **Lucas** - Ensure developer access to all Figma files (Due: July 18, 2025)
- [ ] **Vadim** - Research and implement iOS standard components (Due: Ongoing through August)

### Low Priority

- [ ] **Team** - Investigate Onramper white-label tier for branding removal (Due: August 2025)
- [ ] **Lucas** - Send weekly minutes email (Due: July 18, 2025)

## Technical Notes

### Onramper Integration Specifications

**Commercial Tiers:**
- Essential Plan: $2,000/year (6 on-ramp providers, no off-ramp)
- Premium Plan: Contact sales (includes off-ramp)
- White-label option available (remove "powered by" branding)

**Revenue Model:**
- No direct charge to end users
- Kickback from volume redirected to providers
- 2.5% average savings vs. direct provider use
- Margin opportunity for Cooking to capture savings while remaining competitive

**Technical Requirements:**
- Established entity needed for business agreement
- Cannot operate in gaming/gambling verticals
- AML certification status to be confirmed

**Widget Customization:**
- Dark mode support
- Border radius customization
- Color scheme customization
- Header can be hidden to avoid duplication
- "Powered by" removable (enterprise tier)

### Let's Bank Integration Status

**Current Progress:**
- Indexer: 95% complete
- Backend fallbacks: In development
- Trading capability: Via Jupiter
- Full native support: Expected next week

**Architecture Notes:**
- Similar structure to Radium
- Database schema compatible
- Faster integration due to architectural alignment

### Mobile App Design Specifications

**Screen Priority Levels:**

**High Priority (By End August):**
- Home page
- Wallet page with cash operations
- Portfolio view
- Token details
- Trading operations (as modals)
- Settings page

**Lower Priority (Potentially Post-Launch):**
- Onboarding sequence
- Advanced referral features
- Connected accounts
- In-app help center

**Visual Design Timeline:**
- Structure: Established now
- Visual refinement: Iterative through August
- Color system cleanup: As time permits
- iOS component alignment: Ongoing

### Design Delivery Format

**Required Components:**
- Version banner with flow name, screens, changes
- Main screens with full complexity
- All variants of components
- Annotated elements
- Models and flow diagrams
- Source components visible
- Two-version system (production + next)

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| September deadline pressure | Potential quality compromises | Focus on core features, defer nice-to-haves |
| Onramper AML certification unclear | App Store approval risk | Confirm status before integration |
| Visual language changes from Leo | Development rework required | Version control, accept some inconsistency |
| Six-week timeline for all screens | Tight schedule, little buffer | 80% confidence, essential features only |
| Crossmint checkout still desired by Riz | Potential scope creep | Firm on post-launch addition |
| Number display in balance (6 decimals) | UI layout challenges | Explore vertical or compact layouts |

## Next Steps

1. **This Week:** Lucas shares Figma files with Vadim
2. **Next Week:** Vadim completes wallet page designs
3. **Next Week:** Let's Bank integration completed
4. **Week of July 21:** Developers begin implementing wallet screens
5. **Early August:** Move to token details page designs
6. **End of August:** All main screens completed (target)
7. **September:** Testing and refinement
8. **October 1:** Target launch date

## Key Metrics & Numbers

- **Design timeline:** 6 weeks to complete main screens (80% confidence)
- **Onramper cost:** $2,000/year essential plan (6 on-ramps)
- **Average savings:** 2.5% per transaction vs. direct providers
- **Onramper providers:** 25+ on-ramp, 7+ off-ramp
- **Decimal precision:** Up to 6 decimal places for crypto values
- **Version control:** 2 active versions (production + next)
- **Deferred screens:** Onboarding, advanced referrals, connected accounts, help center

## References

- Onramper - Selected on-ramp/off-ramp aggregator
- Crossmint - Alternative provider (deprioritized)
- Let's Bank - AMM being integrated
- Evil Martians - Design team (Vadim Pleshkov, Varya Nekhina)
- Robinhood - UX comparison for balance visualization
- GitBook - External documentation solution
- Figma - Design collaboration platform

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
