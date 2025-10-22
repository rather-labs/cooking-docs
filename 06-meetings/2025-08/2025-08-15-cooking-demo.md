---
title: Cooking Demo - DNS Resolution & Fee Structure Finalization
date: 2025-08-15
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
status: completed
tags:
  - demo
  - dns-configuration
  - hyperliquid-fees
  - perpetuals-ui
  - backend-refactoring
  - mobile-app-progress
  - priority-fees
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

Team demonstrated significant progress with backend refactoring for Hyperliquid integration, now testing end-to-end locally while awaiting DNS configuration deployment. Fee structures for Hyperliquid bridge and builder codes were discussed in detail, with confirmation that bridge fees apply bidirectionally and builder code surcharges are subject to the partner commission system. Perpetuals UI demonstration showed functional trading interface with TradingView charts pulling Hyperliquid data. Mobile app development progressed with wallet and token pages ready, operations flows nearly complete, and cash in/out functionality ready for production. Discussion about priority fees on transfers led to proposal to remove them from simple send transactions to simplify user experience.

## Meeting Details

**Duration:** 65 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Backend Refactoring Progress

**Context:** Trading services migration to monorepo architecture.

**Key Achievements:**
- Heavy refactoring completed for trading services migration
- Hyperliquid service extraction to standalone monorepo
- Backend integration for Hyperliquid supported assets completed
- End-to-end testing successful on local environment

**Blockers:**
- **DNS Records:** Blocking deployed architecture testing
- Martin checking every 10 minutes with automated script
- Zen confirmed DNS records added, but in different format (potential issue)
- Cannot test on deployed environment until DNS propagation complete

**Status:**
- Local testing: ✅ Complete
- Deployed testing: ⏳ Awaiting DNS resolution

### 2. Native Protocol Integration

**Let's Book Integration:**
- Completed native transaction support
- Similar to pump.fun, pump swap, Radium, Moonshot implementations
- Allows direct protocol operations without routing

**Indexer Improvements:**
- Fixed bug: Some tokens returned from ClickHouse without provider
- Provider field essential for routing transactions correctly
- Validation errors resolved
- Mirror work completed for new protocol support

### 3. Social Login Implementation

**Completed Integrations:**
- **Gmail, Apple, Telegram:** Buttons added to login screen
- Using Auth0 for most social logins (except Telegram)
- Auth0 simplifies flow, especially for Apple (previously problematic)

**Pending Integrations:**
- **Twitter/X:** Next week implementation
- **Solana Wallet:** Next week implementation
- **Visual Update:** Complete login screen redesign upcoming

**Technical Note:**
- Auth0 circumvents Twitter's expensive premium API ($7k/month)
- No issues with X integration using Auth0

### 4. Hyperliquid Fee Structures Deep Dive

**Bridge Fees Discussion:**
- **Question:** Are deposits bidirectional? Can fees be charged both ways?
- **Answer:** Yes, both Solana → USDC and USDC → Solana can be charged
- **Fee Types:** Both percentage and flat fees supported
- **Two Modes:**
  - Fast mode: Higher fees
  - Slow mode: Lower fees, larger profit share

**Builder Code Surcharges:**
- **What We Control:** Builder code surcharge portion
- **What We Don't Control:** Hyperliquid's base fees (only improvable via treasury staking)
- **Partner Program:** Surcharge portion subject to partner commission system
- **Status:** Implementation complexity being assessed

**Fee Application Decision:**
- Bridge fees: Subject to partner program where controllable
- Treat same as spot trading fees for consistency
- Naji to confirm exact percentages for bridge operations

**Key Question from Lucas:**
- Priority: Charging transaction fees vs. referral system?
- **Answer:** Both important, but product stability comes first
- No point charging fees if product doesn't work
- Still important to have charging capability ready

### 5. Perpetuals UI Demonstration

**Environment Context:**
- Currently on dev environment
- Deploying continuously (may encounter breaking changes)
- Wallet selector updated to show USDC balance on Hyperliquid
- Conversion flow between spot and perpetual wallets functional

**UI Features Demonstrated:**
- **Wallet Management:**
  - Spot wallet balance (Solana)
  - Perpetual wallet balance (USDC on Hyperliquid)
  - Conversion between wallets with exchange rate estimates
  - Quick deposit access with dynamic wallet selection

- **Search Functionality:**
  - Command+K (Mac) / Control+K (Windows) hotkey
  - Quick token search across platform
  - Currently non-customizable (future enhancement)
  - Skeleton loading performance issue noted (Martin to check)

**Direct Deposit Discussion:**
- **Current:** Must bridge through Solana to USDC
- **Rationale:** Ensures Cooking captures bridge fee
- **Alternative:** Enable direct USDC deposit (no fee for Cooking)
- **Feasibility:** Simple to implement if desired
- **Naji's Concern:** How many users will actually use Cooking for Hyperliquid trading?
  - Users already on Hyperliquid likely won't switch
  - Evidence: Axiom and Phantom support perps, but low usage

**Market Observation:**
- Community feedback: Can trade perps on Axiom/Phantom, but "nobody does"
- Question whether perpetuals will see significant adoption

### 6. Perpetuals Trading Interface

**Chart Integration:**
- TradingView advanced charts implemented
- Real-time data from Hyperliquid
- Currently shows SOL/USD (proposal to default to BTC/USD instead)
- Mock data displayed until backend fully connected

**Trading Features:**
- Market and limit order support (limit orders pending)
- Leverage adjustment per asset
- Asset selector with all trading pairs
- Order book and trades stream visible
- Position management with market close capability

**UI Bug Identified:**
- Currency denomination not resetting when switching assets
- Example: Viewing BTC/USD should show "Hype" but showed "ETH"
- Lucas acknowledged: "We found the bug"

### 7. Mobile Application Progress

**Vadim's Update:**
- **Wallet & Token Pages:** Covered and ready
- **Operations Flows:** Almost ready, awaiting new style application
- **Cash In/Out:** Practically ready for production
- **Address Book:** Practically ready for production
- **User Settings:** Practically ready for production
- **Onboarding Parts:** Missing pieces practically ready

**Work in Progress:**
- Referral program (finishing next week)
- Operations (finishing next week)
- UX work completion target: Next week

**Completed Pages with Updated Styles:**
- Wallet page ready
- Token page ready
- Explainer pages awaiting content from Lucas

### 8. Transfer Fee Structure Debate

**Context:** Mobile cash-out screen showing priority fees.

**Current Implementation:**
- Gas fee displayed
- Priority fee displayed
- Total projected fees shown

**Naji's Concern:**
- Priority fee confusing for crypto newcomers
- "What's a priority fee to someone who doesn't understand blockchains?"
- Makes product less simple for target users

**Lucas's Defense:**
- Gas fees highly dynamic; can change during transaction input
- Showing maximum amount with dynamic fees causes enable/disable flickering
- Priority fee important during Solana congestion
- High-liquidity users historically locked out without priority fee options

**Naji's Counterargument:**
- MetaMask shows similar dynamic fees; users accept it
- For transfers (not trading), why rush? Can wait one extra second
- Priority fee makes sense for trading operations, not simple sends

**Proposed Solution:**
- Remove priority fee from transfer forms
- Use base gas fee only for sends/cash-outs
- Keep priority fee for trading operations
- Lucas and Martin to assess technical feasibility

**Implementation Consideration:**
- Can Cooking predict/suggest fees users would pay?
- Should priority fee be advanced feature (desktop only)?
- Mobile: Keep it simple; Web: Allow advanced controls

### 9. Address Book & Wallet Management

**Address Book Naming:**
- **Web App:** "Withdraw Wallets"
- **Mobile:** "Address Book"
- **Rationale:** "Address Book" easier concept for crypto newcomers
- **Decision:** Rename web app to "Address Book" for consistency

**Address Book Functionality:**
- Listed addresses with send capability
- Add new addresses with security password confirmation
- Cash out directly from address book
- Works at account level (all wallets)

### 10. Account Management & Security

**Connected Accounts:**
- Select authentication method to connect
- Confirm with security password before web view
- **Important:** Password required before losing control to external service
- Security password independent of all connected accounts

**Account Deletion:**
- Cannot delete accounts from within app
- Must unlink from original service (e.g., Google security settings)
- Cooking maintains linkage even after external unlink
- Can reclaim access by re-establishing linkage

**Data Deletion:**
- 7-day grace period after deletion request
- User data deleted after grace period
- **Seed phrase NOT deleted** (Cooking never has access)
- User must export seed phrase before deletion to retain funds

**Funds with Deleted Account:**
- Cooking deletes user information only
- Seed phrase contains all funds; Cooking never accesses it
- User responsible for exporting seed phrase
- Suggestion: Force seed phrase viewing/verification before deletion

### 11. Security Password Management

**Security Password Flow:**
- Created during onboarding (forced)
- Protects sensitive operations
- Change password option available
- Shows last change timestamp

**Forgotten Password:**
- "I forgot my security password" link to support
- **Critical Issue:** No defined recovery flow
- **Martin's Concern:** Hacking risk if reset too easy
- **Vadim's Concern:** Account unusable if password lost

**Proposed Solutions:**
- **Cooldown Period:** Wait 1 week after password change before withdrawals allowed
- **OTP Verification:** Send one-time password to all linked auth methods (Telegram, Gmail, Apple ID)
  - Verify identity through multiple channels
  - Requires control of authentication methods, not just physical device access
- **Not Foolproof:** Determined hackers could still compromise
- **Need:** Dedicated thought and CS team involvement

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Builder code surcharges subject to partner program | Consistency with fee structure | Partner commissions apply to controllable fees |
| Bridge fees bidirectional and partner-program-eligible | Revenue consistency across operations | Both deposit and withdrawal can be charged |
| Remove priority fee from transfers (proposed) | Simplify UX for crypto newcomers | Lucas & Martin to assess feasibility |
| Rename "Withdraw Wallets" to "Address Book" | Easier concept for newcomers | Consistency between web and mobile |
| Default perpetuals chart to BTC/USD | More appropriate default asset | Changed from SOL/USD |
| Force seed phrase export before account deletion (proposed) | Prevent fund loss | User safety measure |
| Continue DNS troubleshooting | Critical for deployment testing | Martin monitoring; Zen investigating format |
| Defer password recovery flow definition | Complex security implications | Requires CS team and deeper thought |

## Action Items

### High Priority

- [ ] **Zen & Martin** - Resolve DNS record format issue for AWS deployment (Due: August 16, 2025, URGENT)
- [ ] **Naji** - Provide bridge fee percentage structure document (Due: August 17, 2025)
- [ ] **Lucas & Martin** - Assess feasibility of removing priority fee from transfers (Due: August 19, 2025)
- [ ] **Lucas** - Provide explainer page content to Vadim for mobile app (Due: August 19, 2025)

### Medium Priority

- [ ] **Vadim** - Finalize referral program designs (Due: August 22, 2025)
- [ ] **Vadim** - Complete operations flows with new styles (Due: August 22, 2025)
- [ ] **Lucas & Team** - Define security password recovery flow (Due: August 29, 2025)
- [ ] **Team** - Consider cooldown period and OTP for password resets (Due: August 29, 2025)

### Low Priority

- [ ] **Lucas** - Implement hotkey customization for Command+K (Due: Q4 roadmap)
- [ ] **Team** - Explore advanced settings for priority fee on web (Due: Q4 roadmap)
- [ ] **Lucas** - Fix currency denomination reset bug in perpetuals UI (Due: August 16, 2025)

## Technical Notes

### DNS Configuration
- Records added by Zen but format may be incorrect
- Martin monitoring with automated 10-minute check script
- Blocks deployed environment testing
- Local end-to-end testing successful

### Fee Structure Architecture
- Bridge fees: Bidirectional (Solana ↔ USDC)
- Builder codes: Hyperliquid API for surcharges
- Partner program: Applies to all controllable fees
- Two modes: Fast (higher fee) and slow (lower fee, more profit)

### Priority Fee Considerations
- Dynamic gas fees on Solana
- Congestion scenarios require priority fees
- Balance between simplicity and functionality
- Different needs: Trading (priority critical) vs. Transfers (can wait)

### Security Architecture
- Security password: Account-level protection
- Independent from authentication methods
- Required before external service handoff
- Recovery flow undefined (security vs. usability tradeoff)

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| DNS records not propagating | Cannot test deployed Hyperliquid integration | Zen and Martin investigating format issue |
| Priority fee UX confusion | User experience for crypto newcomers | Evaluating removal from transfers |
| Security password recovery undefined | User lockout or security vulnerability | Team to design robust recovery flow |
| Perpetuals adoption uncertainty | Low usage despite development investment | Monitor beta user behavior; community sentiment |
| Account deletion fund loss | Users losing access to funds | Force seed phrase export/verification |

## Next Steps

1. **Immediate:** Resolve DNS configuration for deployment testing
2. **This Week:** Finalize bridge fee structure; assess priority fee removal
3. **Next Week:** Complete mobile referral program and operations flows
4. **Ongoing:** Define security password recovery flow with CS team input
5. **Testing:** Begin full Hyperliquid integration testing once DNS resolved

## Key Metrics & Numbers

- **Mobile UX completion:** Next week (target)
- **Referral program completion:** Next week
- **Operations flows completion:** Next week
- **DNS check frequency:** Every 10 minutes (automated)
- **Social logins completed:** 3 (Gmail, Apple, Telegram)
- **Social logins pending:** 2 (Twitter/X, Solana Wallet)
- **Account deletion grace period:** 7 days

## References

- Auth0 - Social login provider
- TurnKey - Wallet creation service
- Hyperliquid - Perpetuals trading platform
- TradingView - Advanced charting library
- Let's Book - New protocol integration
- ClickHouse - Database performance solution

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
