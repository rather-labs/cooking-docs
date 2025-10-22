---
title: Cooking Demo - Stop Loss Architecture & Legal Challenges
date: 2025-07-25
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
  - stop-loss-architecture
  - take-profit
  - position-management
  - hyperliquid-geoblocking
  - mobile-design
  - timeline-concerns
related:
  - "[[2025-07-18-cooking-demo]]"
  - "[[04-knowledge-base/technical/trading/stop-loss-take-profit]]"
  - "[[04-knowledge-base/legal/hyperliquid-geoblocking]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team faced critical architectural and legal challenges this week. Vadim proposed shifting stop loss and take profit management from order-level to position-level for better UX, but Lucas identified this requires fundamental backend schema changes originally planned for portfolio-wide management next month - implementation in mobile app by October 1st deadline deemed uncertain. A major legal blocker emerged: Hyperliquid successfully integrated on devnet but team discovered geoblocking prevents use of Ohio AWS server, and users from non-sanctioned countries accessing via Cooking would effectively use it as a VPN, creating serious legal liability. The team is approximately one week behind schedule on mobile development, with concerns about meeting the September deadline.

## Meeting Details

**Duration:** 1 hour 18 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Development Progress Updates

**Backend:**
- **Major Achievement:** Deposit flow and conversion flow completed
- Can now deposit and convert Solana to USDC on Hyperliquid
- Critical part for trading perpetuals finished
- Continuing work on schemas and remaining endpoints
- Started speed of execution improvements (addressing previous concerns)
- **Performance Win:** Martin reduced execution time by ~800ms (1 of 6 identified pain points)

**Frontend:**
- Finishing tests for form controls (radio buttons, checkboxes, switches)
- Started implementation on hold case
- Command to quickly open search model on desktop (requested feature)
- Continuing work on syncing visual components (2 versions behind Leo's latest due to frequent changes)

**Indexer:**
- Started working on speed of execution improvements with backend
- Fixed ClickHouse bug where token price showed as infinity

**Mobile:**
- Splash screen completed
- Telegram login completed (finished previous week)
- Terms and conditions screen completed
- Working on home flow: stove and specials, quick settings, search token
- Filters now working (minor visual issues remaining)
- Backend integration for kitchen and filters completed this morning
- Visual details on cards need revamp (known from start)
- Mobile engineer working on quick settings (expected done by Monday/Tuesday)

**Timeline Status:** Team currently at approximately the "quick settings" point in the flow, about one week behind schedule

### 2. Visual Language Change Management

**The Challenge:**
- Leo has changed visual language 2-3 times since current roadmap started
- Each major visual change requires ~2 weeks of work to update tokens and review flows
- Pushes back committed features

**Lucas's Concern:**
> "I need you guys to understand that those visual changes from our architecture right now, it's not that big of a deal because we can manage it in a sort of lean way, but every time that he modifies the visual language in a big manner, that is a work of about two weeks and upwards."

**Resolution:**
- Leo can continue making changes to visual language
- **Critical agreement:** Designs in dev/production won't match latest Leo versions
- Functionality prioritized over visual refinement to meet September deadline

**Naji's Position:**
> "I'd rather have the product ready to be tested in September than having something that looks nice but doesn't work by September."

**Action:** Naji to communicate to Riz and team that visual updates will be deferred to avoid delays on essential features

### 3. On-Ramp Final Decision: Onramper Confirmed

**Confirmation:** Team proceeding with Onramper, not Crossmint checkout

**Rationale Recap:**
- Don't need checkout feature (can add later)
- Meeting deadline is priority
- Widget integration approach confirmed
- Two-step process acceptable given timeline

**Naji's Statement:**
> "I think it's fine to go with Onramper. We don't need the checkout."

**Lucas's Clarification:**
- Not marrying this solution permanently
- Can switch to headless API later if needed
- But that would be exponentially more work
- Current approach enables October 1st deadline

**Implementation Confirmed:** Embedded widget, customizable to match Cooking branding

### 4. Stop Loss & Take Profit: The Architectural Challenge

Vadim presented a critical UX problem that sparked extensive technical discussion.

**The UX Problem:**

**Current Implementation:**
- Stop loss and take profit are parameters of orders, not positions
- Creating a buy limit order with SL/TP creates 3 orders:
  1. Main order (open status)
  2. Stop loss order (unrealized status, dependent on #1)
  3. Take profit order (unrealized status, dependent on #1)
- For users to see SL/TP on positions, they must:
  1. Go to position
  2. Click to token details
  3. Click on pending orders
  4. Find the SL/TP orders there

**Why This Is Problematic:**

1. **No Indication on Position View:**
   - Users can't see if position has SL/TP set
   - Must drill down multiple levels to discover

2. **Market Orders:**
   - Currently don't support SL/TP at all
   - Users with market-bought positions have no way to set protection

3. **Manual Workaround Required:**
   - To set stop loss on existing position, must:
   - Calculate price manually for desired % loss
   - Create separate sell limit order at that price
   - No connection to original position
   - Complex and error-prone

4. **Confusing Sell Order UX:**
   - When creating sell limit order, SL/TP options don't make sense
   - Target price effectively IS the take profit
   - Only stop loss makes sense for sell orders
   - But then both TP and SL options are shown

**Vadim's Proposed Solution:**

**Position-Level Management:**
- Make SL/TP parameters of positions, not orders
- Every position can optionally have SL/TP set
- Can set when creating position (advance setup) OR
- Can add to existing position anytime (post-creation)

**User Flow:**
1. View position in portfolio
2. See SL/TP status directly on position card
3. Tap "Manage" to set or adjust SL/TP
4. Simple screen with sliders/inputs for percentages
5. Save and it applies to entire position

**Mental Model:**
- Position has parameters: size, entry price, SL%, TP%
- SL/TP are properties of what you own, not how you bought it
- Similar to centralized exchange pattern

**Visual Implementation:**
- Position cards show SL/TP indicators
- Manage button opens dedicated screen
- Can combine SL and TP in single screen
- Screen accessible from multiple entry points (including charts in future)

**What Happens Under the Hood:**
- Still creates limit orders in backend
- But triggered by position parameters, not order parameters
- New order trigger types: "sell if loss > X%" and "sell if gain > X%"
- Orders recalculate based on aggregated position entry price

**The Technical Reality:**

**Lucas's Explanation of Current Architecture:**

> "Every stop take profit and stop loss is a limit order, it's a sell limit order for a specific price. The way that we handle them is by expressing the order price as an integer."

**What Position-Level Requires:**

1. **PNL Calculation Change:**
   - Currently: PNL based on specific order entry price and fees
   - Proposed: PNL based on aggregated average entry price across all orders
   - Must sum all entry prices and all fee costs
   - Then calculate SL/TP from that aggregate

2. **Schema Restructuring:**
   - Change from order-level to position-level architecture
   - New trigger types needed for percentage-based SL/TP
   - Fundamentally different from current integer-based price triggers

3. **Order Aggregation:**
   - When user doubles down on position, average entry moves
   - SL/TP must recalculate based on new average
   - Complex price calculation for aggregated positions

**Why This Is a Major Undertaking:**

**Lucas's Key Point:**
> "That feature was initially meant and thought of only for desktop. At the time of inception it was only meant for web app."

**The Original Plan:**
- Portfolio-wide SL/TP management scheduled for next month
- Would handle aggregate PNL across all positions
- Same calculation complexity needed
- Designed for web app, not scoped for mobile

**Timeline Implications:**

**Lucas's Concern:**
> "I don't know that we can skip this intermediate step... I am not sure that we can move into mobile and still keep the deadline for the time that we've agreed on."

**Critical Questions:**
1. Can we integrate this new backend architecture into mobile?
2. Can we complete it and still meet October 1st deadline?
3. Should we defer this feature entirely from mobile v1?

**The Debate:**

**Naji's Perspective:**
> "I would rather just not do things twice, right? If we know we're getting there, I'd rather just have things ready to do it properly and not have to redo it."

- Prefers to wait for proper implementation
- Avoid building intermediate solution that gets thrown away
- Better to skip feature than build it twice

**Lucas's Reality Check:**
> "Let's let's imagine that feature it's not going to get in time and think about how we can solve for what we currently have because yes it is going to happen but I don't know that we can get it into mobile testing and working perfectly as we expect."

- Uncertainty about fitting into current timeline
- Backend feature not originally scoped for mobile
- Working endpoints designed for web, not tested for mobile use case

**Compromise Explored:**

**Vadim's Suggestion:**
> "We can just like for the first version of the app remove stop losses from the mobile app completely... at the moment that we allow it on the backend side we can add this feature as it's sort of intended in a more user-friendly way from the start."

**Options on the Table:**

1. **Skip SL/TP entirely in mobile v1**
   - Cleanest approach
   - Avoids building intermediate solution
   - Add proper version when backend ready

2. **Show current implementation despite UX issues**
   - Functional but confusing
   - Would require teaching users complex workaround
   - Gets replaced soon anyway

3. **Rush to implement position-level**
   - Uncertain if achievable by deadline
   - Risk to overall timeline
   - May compromise quality

**No Final Decision:** Team to workshop further, but leaning toward skipping SL/TP in mobile v1

### 5. Related Issue: Limit Order Take Profit Logic

**Naji's Observation:**
> "When you create a sell limit order, the take profit doesn't make sense. Only stop loss makes sense."

**The Logic:**
- Sell limit order has target price
- That target price IS the take profit price
- Adding separate TP would create two targets in same direction
- Only one can execute
- Other becomes meaningless

**Lucas's Confirmation:**
- For sell orders, TP optional variable doesn't make sense
- SL is the only meaningful parameter
- Both shouldn't be shown for sell orders

**Design Implication:** Vadim can hide TP option for sell orders in current UI

### 6. Wallet Page Design Completion

**Vadim's Update:**
- Working on pending and history list views
- Once finalized, wallet page complete
- Next focus: Token details page

**Varya's Confirmation:**
- Wallet screens ready early next week
- Then moving to token details
- Maintaining momentum toward end-August completion

**Visual Language Iteration:**
- Structural changes minimal once established
- Stylistic changes (colors, systems) will happen
- Requires time to clean up and configure
- Developers can start on structure while styling evolves

### 7. Design Delivery Timeline

**Varya's Projection (Restated):**
- All main screens by end of August
- 80% confidence level
- ~6 weeks from July 18

**Varya's Caution:**
> "Keep in mind that we don't want to spend too much time on designs. Like there are so many screens to ship and we're very tight on deadline."

**Priority:** Continue shipping new screens over perfecting existing ones

### 8. Critical Legal Issue: Hyperliquid Geoblocking

**The Discovery:**

**Lucas's Report:**
> "We've successfully integrated on Devnet to make deposits and swap it for USDC on Devnet and it works and it works fine. It is super responsive."

**Then the problem:**
> "We tried testing on mainnet mainly because the terms and conditions on the side of Hyperliquid explicitly says that trading or accessing Hyperliquid from the US is prohibited... we found ourselves geoblocked."

**The Technical Situation:**

1. **Hyperliquid Terms:** Trading or accessing from US prohibited
2. **API Unclear:** Terms say nothing about API access
3. **Testing Result:** Ohio AWS server is geoblocked
4. **Implication:** Cannot use current server location for Hyperliquid integration

**The Legal Problem:**

**Lucas's Warning:**
> "Users from non-sanctioned places that may log into Cooking and try to trade perpetuals are going to effectively be using Cooking as a VPN and that can lead you guys into some serious trouble."

**The Scenario:**
- User in US (prohibited region) accesses Cooking
- Cooking server in non-US location connects to Hyperliquid
- User trades perpetuals through Cooking
- **Result:** Cooking acting as VPN to circumvent Hyperliquid's geo-restrictions
- **Legal Risk:** Serious liability for Cooking/Ember

**Comparable Situation:**
- Phantom Wallet has same issue
- US users report inability to trade perpetuals from Phantom app
- Hyperliquid doesn't allow it

**Technical Solution Required:**
- Move AWS server out of US (UK, Spain, etc.)
- Unknown costs
- Unknown timeline for migration
- But doesn't solve legal liability issue

**Legal Consultation Needed:**

**Both Teams Taking Action:**
- Ratherlabs: Submitted to internal legal counsel
- Cooking/Ember: Must consult own legal team

**Critical Questions for Legal:**
1. Can Cooking operate Hyperliquid integration for non-US users if some users might be in US?
2. What user verification is required to prevent VPN-like usage?
3. What liability exists if US user accesses despite restrictions?
4. Should Cooking implement its own geoblocking for US users?
5. Are there licensing options to operate in US properly?

**Lucas's Directive:**
> "That is something that you guys should inquire your legal team because that is way out of our scope."

**Impact on Timeline:**
- Blocker discovered this week
- Lucas spent most of week dealing with this vs. fee structure review
- Cannot proceed with Hyperliquid integration until resolved
- Potential major roadblock to perpetuals launch

### 9. Slippage Configuration

**Naji's Position:** Don't overcomplicate it

**Requirements:**
- No upper limit on slippage percentage
- User sets manually based on risk tolerance
- Standard percentage approach
- User takes responsibility for high slippage choices

**Lucas's Agreement:**
- No upper limit confirmed
- Will not automate slippage (user responsibility prevents liability)
- Auto-adjusting priority in scope for near future feature
- User must consciously set high slippage if desired

**Reasoning:** If user sets 100% slippage and gets sandwiched, that's their informed choice - Cooking not taking responsibility

### 10. Timeline Concerns & Next Features

**Lucas's Status Report:**
> "I am seriously concerned about timelines because I was not expecting, although Vadim is working fast, I am going to give him that, we are we are behind schedule right now, we are about a week behind schedule right now and I am concerned about the end of September deadline."

**Reasons for Delay:**
- Mobile engineer requires significant syncing time with Lucas
- Lucas is only product person on project
- Time spent on Hyperliquid legal issue
- Visual language changes causing rework

**Current Status:** ~1 week behind on mobile development

**Naji's Request:**
- Summarize all issues in weekly minutes/email
- Cover AWS/Hyperliquid legal issues
- Want to address blockers systematically
- Avoid further delays

**Upcoming Discussions:**
- Next features roadmap (deferred to next week or week after)
- Admin panel needs to be added to roadmap (before end of year, before smaller details)
- Review of feature priority document

**Strategy:** Work through issues one by one to prevent cascading delays

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Functionality over visual refinement | September deadline priority | Designs in production won't match latest Leo updates |
| Onramper confirmed (not Crossmint) | Timeline and functionality requirements | Widget integration approach |
| No upper limit on slippage | User responsibility model | Users can set any percentage |
| Don't automate slippage | Avoid platform liability | User explicitly chooses risk |
| Stop loss/take profit approach TBD | Position-level requires major backend work | May skip from mobile v1 entirely |
| Hide TP from sell orders (interim) | TP doesn't make sense on sell limits | Cleaner UX for current implementation |
| Prioritize shipping screens over perfection | Tight deadline (6 weeks to end August) | Focus on structure, iterate styling |
| Legal consultation required on Hyperliquid | Serious liability risks | Blocker until legal guidance received |

## Action Items

### Critical Priority

- [ ] **Legal Team (Cooking/Ember)** - Urgent consultation on Hyperliquid geoblocking liability (Due: ASAP, this is a BLOCKER)
- [ ] **Legal Team (Cooking/Ember)** - Determine if Cooking needs own geoblocking for US users (Due: ASAP)
- [ ] **Legal Team (Ratherlabs)** - Internal counsel review of VPN liability scenario (Due: In progress)
- [ ] **Naji** - Communicate to Riz and team: visual updates deferred to prioritize functionality (Due: July 26, 2025)

### High Priority

- [ ] **Backend Team** - Assess feasibility of position-level SL/TP in mobile for Oct 1 deadline (Due: July 29, 2025)
- [ ] **Lucas & Team** - Workshop SL/TP approach: skip v1, interim solution, or rush implementation (Due: August 1, 2025)
- [ ] **DevOps** - If legal permits: Plan AWS server migration out of US (UK/Spain/etc.) (Due: TBD pending legal)
- [ ] **Vadim** - Complete wallet page designs (Due: Week of July 28, 2025)
- [ ] **Vadim** - Begin token details page designs (Due: Early August 2025)

### Medium Priority

- [ ] **Lucas** - Send weekly minutes with all issues summarized (AWS, Hyperliquid, SL/TP, timeline) (Due: July 25, 2025)
- [ ] **Team** - Schedule next features roadmap discussion (Due: Week of August 4 or 11, 2025)
- [ ] **Team** - Add admin panel to roadmap (before end of year) (Due: Next roadmap meeting)
- [ ] **Vadim** - Hide TP option from sell order UI (Due: August 1, 2025)
- [ ] **Mobile Engineer** - Complete quick settings screen (Due: July 29-30, 2025)

### Low Priority

- [ ] **Martin** - Continue speed optimization work (5 more pain points identified) (Due: Ongoing)
- [ ] **Lucas** - Review Hyperliquid fee structure (deferred due to legal issue) (Due: After legal resolution)

## Technical Notes

### Stop Loss / Take Profit Architecture

**Current Implementation (Order-Level):**
- SL/TP are parameters of orders
- Expressed as integer price values
- Creating buy order with SL/TP creates 3 orders:
  - 1 open order
  - 2 unrealized orders (dependent on first)
- PNL calculated from specific order entry price + fees

**Proposed Implementation (Position-Level):**
- SL/TP are parameters of positions
- Expressed as percentage thresholds
- Requires new trigger types: "sell if loss > X%" and "sell if gain > X%"
- PNL calculated from aggregated average entry price across all position orders
- Must sum all entry prices and all fee costs
- Recalculates when position size changes (user doubles down)

**Why It's Complex:**
- Schema change from order-based to position-based
- Aggregate calculation across multiple orders forming one position
- Dynamic recalculation on position changes
- Originally designed for portfolio-wide feature (next month)
- Not scoped for mobile in original planning

**Related Feature:**
- Portfolio-wide SL/TP management (scheduled next month for web)
- Same calculation complexity
- Would allow SL/TP across entire portfolio, not just single position
- Ultimate solution for meme coin volatility

### Hyperliquid Geoblocking Technical Details

**Discovery Process:**
1. Successfully integrated on Hyperliquid devnet
2. Deposits and USDC swaps working perfectly
3. Responsive performance
4. Attempted mainnet testing
5. Discovered Ohio AWS server is geoblocked

**Current Server Location:** AWS Ohio (US)

**Hyperliquid Restrictions:**
- US access prohibited (explicit in T&C)
- Canada appears to be under same restriction
- API access not explicitly mentioned in T&C (gray area)
- Mainnet enforces geoblocking

**Technical Workaround:**
- Move server to non-restricted region (UK, Spain, etc.)
- Cost unknown
- Timeline unknown
- Migration complexity TBD

**Legal Problem Unsolved by Server Move:**
- Cooking still potentially acting as VPN
- US users could still access via non-US server
- Liability question remains
- May require Cooking to implement own geoblocking
- Phantom Wallet precedent: they block US users from perpetuals

### Performance Optimization Progress

**Speed of Execution Initiative:**
- 6 pain points identified
- 1 completed this week: 800ms reduction
- 5 remaining pain points
- Ongoing work

### Mobile Development Status

**Completed:**
- Splash screen
- Telegram login
- Terms and conditions screen

**In Progress:**
- Home flow (stove/specials, quick settings, search)
- Filters (working, minor visual issues)
- Card visual revamp (planned from start)

**Current Position:** Approximately at "quick settings" in flow diagram

**Behind Schedule:** ~1 week

### Design Workflow

**Version Control:**
- Two active versions (production + next)
- Leo making changes in separate version
- Production designs frozen
- Styling updates deferred

**Delivery Timeline:**
- Main screens by end August (6 weeks from July 18)
- 80% confidence
- Structure prioritized over styling
- Iterate on visual polish as time permits

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| **CRITICAL:** Hyperliquid US geoblocking | Cannot launch perpetuals without legal clarity | Urgent legal consultation both teams |
| **CRITICAL:** VPN liability if US users access | Potential legal action against Cooking/Ember | Legal team must determine acceptable approach |
| Position-level SL/TP backend complexity | Major feature may not make mobile v1 | Consider skipping from v1, add later |
| Timeline slippage (1 week behind) | September deadline at risk | Focus on essential features, defer polish |
| AWS server migration required | Cost and time unknown | Plan pending legal guidance |
| Mobile engineer sync time overhead | Reduces Lucas's capacity | Expected but impact timeline |
| Leo's visual language changes | 2+ weeks rework each time | Freeze production designs, accept inconsistency |
| Portfolio-wide SL/TP scheduled next month | Overlaps with mobile crunch time | May need to deprioritize one or other |

## Next Steps

1. **Immediate:** Legal teams consult on Hyperliquid geoblocking (BLOCKER)
2. **This Week:** Naji communicates visual deferral to Riz/team
3. **Next Week:** Assess position-level SL/TP feasibility for mobile
4. **Next Week:** Vadim completes wallet designs, starts token details
5. **Early August:** Workshop SL/TP final decision (skip/interim/implement)
6. **Mid-August:** Pending legal resolution, plan AWS migration if needed
7. **End August:** All main screens targeted for completion
8. **September:** Testing, refinement, deadline pressure
9. **October 1:** Current target launch date (at risk)

## Key Metrics & Numbers

- **Timeline status:** ~1 week behind schedule
- **Design completion target:** End of August (6 weeks from July 18)
- **Design confidence:** 80%
- **Performance improvement this week:** 800ms reduction (1 of 6 pain points)
- **Remaining optimization opportunities:** 5 pain points
- **SL/TP order creation:** 1 buy order with SL/TP = 3 total orders
- **Mobile screens completed:** 3 (splash, Telegram login, T&C)
- **Mobile screens in progress:** Home flow (3 components)
- **Visual language changes since roadmap start:** 2-3 major revisions
- **Rework time per visual language change:** ~2 weeks

## References

- Hyperliquid - Perpetuals provider (US geoblocked)
- Phantom Wallet - Comparison for US perpetuals blocking
- AWS Ohio - Current server location (problematic)
- CFTC - May require certifications for perpetuals
- Onramper - Confirmed on-ramp solution
- Evil Martians - Design team (Vadim, Varya)
- Leo - Visual designer (frequent iterations)

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
