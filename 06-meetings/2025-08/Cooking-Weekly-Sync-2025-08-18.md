---
title: Cooking Weekly Sync - Product & Engineering
type: meeting-note
date: 2025-08-18
attendees: [Lucas Cufré, Naji Osmat, Gregory Chapman, Vadim Pleshkov, Varya Nekhina]
meeting-type: standup
tags: [Cooking, RatherLabs, Product, Sync, UX, Engineering, Referrals, Trading]
summary: |
  Weekly sync meeting focused on finalizing Hyperliquid integration, discussing fee structures for perpetuals, and reviewing UX designs for trading operations. Key decisions made about removing detailed fee breakdowns from pre-transaction screens, deferring take profit/stop loss features for sell orders, and planning AI trading journal feature development.
related-docs:
  - Fee structure documentation
  - Referral program specifications
  - Trading operations UX designs
---

# Cooking Weekly Sync - Product & Engineering

**Date:** 2025-08-18
**Time:** ~1:13:00 duration
**Attendees:** Lucas Cufré, Naji Osmat, Gregory Chapman, Vadim Pleshkov, Varya Nekhina
**Facilitator:** Naji Osmat

## Executive Summary

This weekly sync meeting covered critical aspects of the Cooking platform development, with a primary focus on finalizing the Hyperliquid integration, establishing fee structures for perpetual trading, and refining the user experience for trading operations. The team discussed the completion timeline for Hyperliquid modifications (expected within the week), addressed concerns about transaction speed improvements needed before go-to-market, and made significant UX decisions regarding fee displays and limit order functionality.

The meeting revealed that DNS records and Apple account KYC issues are being resolved, clearing the path for Hyperliquid integration completion. A notable technical discussion centered on the complexity of implementing an AI trading journal for Solana-based meme coins, with the decision to bring in a specialized AI technical resource (Shakib) to lead this effort. The team also spent considerable time refining the fee display UX, ultimately deciding to simplify pre-transaction fee information and move detailed breakdowns to post-transaction history views.

Key decisions included keeping the same referral structure for both spot and perpetual trading (with potential volume tier adjustments), removing detailed cooking fee breakdowns from pre-transaction screens, and deferring take profit/stop loss features for sell limit orders due to technical constraints. The team scheduled a roadmap prioritization meeting for the following week to address competing priorities including transaction speed improvements, AI assistant features, and various smaller feature implementations.

## Action Items

- [ ] **Send documentation for Apple account KYC to Zane** - Assigned to: Lucas Cufré - Due: 2025-08-18 - Priority: High
- [ ] **Complete documentation on market details and security concerns** - Assigned to: Lucas Cufré - Due: 2025-08-18 - Priority: Medium
- [ ] **Forward Alan's message regarding fees and surcharge** - Assigned to: Naji Osmat - Due: 2025-08-18 - Priority: High
- [ ] **Review and provide feedback on referral program structure** - Assigned to: Naji Osmat - Due: 2025-08-20 - Priority: High
- [ ] **Prepare referral program sketches and schedule meeting** - Assigned to: Vadim Pleshkov - Due: 2025-08-19 - Priority: High
- [ ] **Remove fee details sheet from pre-transaction screens** - Assigned to: Vadim Pleshkov - Due: 2025-08-23 - Priority: Medium
- [ ] **Schedule roadmap prioritization meeting for next week** - Assigned to: Naji Osmat - Due: 2025-08-19 - Priority: High
- [ ] **Onboard Shakib for AI technical leadership** - Assigned to: Gregory Chapman - Due: 2025-08-23 - Priority: Medium
- [ ] **Send Fireflies recording to Lucas** - Assigned to: Naji Osmat - Due: 2025-08-18 - Priority: Low
- [ ] **Review UX designs and provide feedback** - Assigned to: All - Due: 2025-08-23 - Priority: Medium

## Index

1. Hyperliquid Integration Status
2. Fee Structure for Perpetuals and Referrals
3. Transaction Speed Improvements
4. AI Trading Journal Feature
5. UX Design: Fee Display and Trading Operations
6. Take Profit/Stop Loss Implementation
7. Timeline and Deliverables

---

## Topics: Breakdown

### Topic 1: Hyperliquid Integration Status

#### Executive Summary
The Hyperliquid integration is nearing completion with DNS records being resolved and Apple account KYC in progress. The team expects to reach the finish line within the week, pending documentation submissions to Zane.

#### Key Takeaways
- DNS record issues will be resolved within the hour according to Zane
- Apple account KYC documentation needs to be sent to complete setup
- Integration of market orders and operations is nearly complete
- Limit orders integration to begin immediately after market orders
- Builder codes implementation scheduled after limit orders

#### Discussion Details
Lucas had a call with Zane earlier in the day to address outstanding issues. The main blockers were DNS records (being resolved) and Apple account KYC requirements. Gregory confirmed that Naji has answers for the Apple-side KYC requirements, which should resolve the remaining blockers.

---

### Topic 2: Fee Structure for Perpetuals and Referrals

#### Executive Summary
The team discussed maintaining consistent fee structures across spot and perpetual trading, with a 1% fee on perpetuals and the same referral kickback structure. Concerns were raised about volume tier adjustments needed due to the significantly higher volumes in perpetual trading.

#### Key Takeaways
- No deposit or withdrawal fees on the bridge (only gas fees)
- 1% fee to be applied on perpetual trading
- Same referral structure for both spot and perpetuals
- Volume tiers may need reconsideration due to perpetual trading volumes
- Hyperliquid's referral program entry requires only $10,000 in traded volume

#### Discussion Details
The team debated whether to include perpetual trading volumes in the referral program calculations. Lucas pointed out that with 40x leverage on BTC, users can easily achieve high trading volumes with minimal capital, which could skew the program. Naji agreed to research and think through the implications, potentially keeping spot volume as the determinant for perpetual benefits or creating separate tier structures.

---

### Topic 3: Transaction Speed Improvements

#### Executive Summary
Lucas raised concerns about transaction speed compared to competitors like Echo, emphasizing this should be a priority before go-to-market. The team acknowledged that while some improvements can be made now, matching competitor speeds may require dedicated resources and deep technical research.

#### Key Takeaways
- Current transaction speed can be improved but may not match Echo's performance
- Speed improvements should be prioritized in the next roadmap
- Resources may need to shift from new features to performance optimization
- Deep research required for significant time-to-execution improvements

---

### Topic 4: AI Trading Journal Feature

#### Executive Summary
The AI trading journal feature was identified as a significant technical undertaking with no ready-made solutions for Solana-based meme coin ecosystems. The team decided to bring in Shakib, an AI technical specialist, to lead research and development efforts.

#### Key Takeaways
- No existing solutions found for Solana meme coin trading analysis
- Potential approaches include building an MCP for on-chain transaction analysis
- Could wrap existing LLMs trained on other networks
- Shakib to join by end of week to lead technical research
- Feature requires significant development effort

#### Discussion Details
Lucas explained that creating an AI trading journal for Solana's meme coin ecosystem would require either building a custom NCP (Network Communication Protocol) to analyze on-chain transactions or wrapping existing LLMs from other networks. The complexity of the feature necessitates bringing in specialized AI expertise.

---

### Topic 5: UX Design: Fee Display and Trading Operations

#### Executive Summary
The team engaged in extensive discussion about fee display in the trading interface, ultimately deciding to simplify pre-transaction displays and move detailed breakdowns to post-transaction history screens. The focus shifted to showing only essential information that users need to make trading decisions.

#### Key Takeaways
- Remove detailed cooking fee breakdown from pre-transaction screens
- Show fees in USD terms to emphasize low costs
- Keep total projected fees visible but without detailed breakdown
- Detailed fee information available in transaction history
- Priority fees remain editable for advanced users
- Implement validation to prevent transactions when insufficient funds

#### Discussion Details
The discussion centered on balancing transparency with simplicity. Gregory advocated for "less is more," suggesting that overwhelming users with fee details before transactions isn't necessary. The team agreed that showing fees in USD terms (e.g., "fees less than $0.01") could actually serve as a marketing point for the platform's low costs. Advanced users who need to adjust priority fees can still do so through settings.

---

### Topic 6: Take Profit/Stop Loss Implementation

#### Executive Summary
Technical limitations were identified in implementing take profit and stop loss features for sell limit orders. The team decided to defer these features for sell orders while keeping them for buy limit orders, with plans to implement position-based TP/SL in the future.

#### Key Takeaways
- Take profit and stop loss work logically for buy limit orders
- Sell limit orders cannot have both TP and SL due to technical constraints
- Current system doesn't support "one cancels other" (OCO) orders
- Future implementation should tie TP/SL to positions rather than orders
- For now, users can create independent limit orders for different scenarios

#### Discussion Details
Vadim presented the challenge of implementing TP/SL for sell orders, explaining that it creates a UX nightmare when users need to understand which condition applies based on their entry price. Lucas confirmed that the current system treats limit orders as conditional market orders (if price reaches X, execute market order), which differs from traditional order book exchanges. The team agreed to postpone this feature until they can implement proper position-based management.

---

### Topic 7: Timeline and Deliverables

#### Executive Summary
The team confirmed the timeline for current deliverables with a demonstration scheduled for Friday and final presentation on Monday. The roadmap prioritization meeting was scheduled for the following week to address competing priorities.

#### Key Takeaways
- Operations functionality mostly complete, focusing on referral program
- Friday demonstration of all features with feedback session
- Monday final presentation of completed features
- Roadmap prioritization meeting scheduled for next week
- Three outstanding items from current roadmap need prioritization

---

## Decisions Made

1. **Simplify fee displays** - Remove detailed cooking fee breakdowns from pre-transaction screens to reduce complexity
2. **Maintain unified referral structure** - Keep same referral program for spot and perpetuals with potential tier adjustments
3. **Defer sell order TP/SL** - Remove take profit and stop loss options from sell limit orders due to technical constraints
4. **Display fees in USD** - Show all fees in USD terms to emphasize low platform costs
5. **Bring in AI expertise** - Onboard Shakib to lead AI trading journal technical development
6. **Prioritize speed improvements** - Consider allocating resources to transaction speed optimization over new features

## Blockers and Risks Identified

- **Transaction speed competitiveness** - Impact: High - Owner: Lucas Cufré - Needs resolution by: Before go-to-market
- **AI journal complexity** - Impact: Medium - Owner: Shakib (incoming) - Needs resolution by: TBD
- **Perpetual volume tier structure** - Impact: Medium - Owner: Naji Osmat - Needs resolution by: Before perpetuals launch

## Parking Lot

- Detailed implementation of OCO (one cancels other) orders
- Position-based take profit and stop loss management
- Dynamic gas fee calculations with tolerance thresholds
- Bribe fee implementation in settings

## Next Steps

- Demonstration of completed features scheduled for Friday
- Final presentation on Monday with all feedback incorporated
- Roadmap prioritization meeting next week to balance speed improvements, AI features, and other development
- Shakib onboarding by end of week for AI technical leadership

## References

- Google Sheet with feature explanations sent to Zane
- Fee structure documentation from Alan
- UX designs for trading operations (Figma)
- Referral program specifications document