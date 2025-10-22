---
title: Cooking Weekly Sync - September 1, 2025
type: meeting-note
date: 2025-09-01
attendees: [Lucas Cufré, Naji Osmat, Zen, Shakeib Shaida, Martin Aranda]
meeting-type: standup
tags: [roadmap, features, optimization, mobile-app, integrations]
summary: |
  Weekly sync discussing roadmap priorities for post-September delivery, including fee customization, wallet tracker, and multi-language support. Key focus on performance optimization to match competitors like Bullex and Echo. Discussion of Apple Developer account blockers for mobile testing and integration timeline for AI Trading Journal from DRUGS team.
related-docs:
  - Cooking GT New Features Document
  - Competitor Feature Comparison
---

# Cooking Weekly Sync - September 1, 2025

**Date:** 2025-09-01
**Time:** ~40 minutes
**Attendees:** Lucas Cufré, Naji Osmat, Zen, Shakeib Shaida, Martin Aranda
**Facilitator:** Lucas Cufré

## Executive Summary

The team conducted their weekly sync meeting to discuss the product roadmap for the post-September delivery phase. Lucas presented a tentative roadmap prioritizing fee customization as the first feature to enable back office integration, followed by watchlist functionality, position-level take profit/stop loss, wallet tracker, multi-language support, and account management. A significant portion of the discussion focused on performance optimization, with emphasis on matching competitor speeds, particularly Bullex and Echo. The team acknowledged current limitations in transaction execution speed and discussed the need for infrastructure improvements including private mempool RPCs. The Apple Developer account setup remains a blocker for mobile testing, with Greg responsible for creating a personal account as a temporary solution. The integration with the AI Trading Journal from the DRUGS team was noted as a major unknown that could impact timelines.

## Action Items

- [ ] **Send roadmap documentation to Zen via Telegram** - Assigned to: Lucas Cufré - Due: 2025-09-02 - Priority: High
- [ ] **Include past completed work view in roadmap** - Assigned to: Lucas Cufré - Due: 2025-09-02 - Priority: Medium
- [ ] **Chase up Greg on Apple Developer account setup** - Assigned to: Naji Osmat - Due: 2025-09-02 - Priority: High
- [ ] **Test TradingView integration for partner demo** - Assigned to: Martin Aranda - Due: 2025-09-02 - Priority: High
- [ ] **Schedule call with Joe for tomorrow 5pm Emirates time** - Assigned to: Naji Osmat - Due: 2025-09-02 - Priority: Medium
- [ ] **Send Fireflies recording to Lucas** - Assigned to: Naji Osmat - Due: 2025-09-01 - Priority: Low
- [ ] **Research speed optimization strategies and Echo implementation** - Assigned to: Shakeib Shaida - Due: Ongoing - Priority: High
- [ ] **Continue pricing discussions with Bubble Maps via Telegram** - Assigned to: Lucas Cufré - Due: 2025-09-02 - Priority: Medium

## Index

1. Apple Developer Account Status
2. Roadmap Features and Prioritization
3. Performance Optimization Requirements
4. External Integrations and Pricing
5. TradingView Integration Status

---

## Topics: Breakdown

### Topic 1: Apple Developer Account Status

#### Executive Summary
The Apple Developer account setup remains incomplete, blocking mobile app testing. Greg was supposed to provide credentials but hasn't delivered. The team discussed using a personal account as a temporary workaround to avoid delays.

#### Key Takeaways
- Apple Developer account approval is still pending
- Greg was supposed to create an anonymous Gmail and personal account as temporary solution
- This is blocking mobile app testing progress
- Naji will follow up with Greg to ensure account creation

#### Discussion Details
Lucas raised that he's still missing the Apple account credentials that Greg promised to provide last Friday. Zen clarified that the plan discussed on Friday was to use a personal account temporarily and switch later to avoid testing delays. The organizational account promotion hasn't been completed.

---

### Topic 2: Roadmap Features and Prioritization

#### Executive Summary
Lucas presented a comprehensive roadmap for post-September delivery, prioritizing fee customization as the foundation for back office integration. The roadmap includes watchlist functionality, position-level risk management, wallet tracker, multi-language support, and account management, with most features running in parallel where possible.

#### Key Takeaways
- **Fee Customization** (first priority): Enable custom fees per token, provider, and referral code
- **Watchlist**: Persistent favorite tokens list with search and real-time data
- **Position-level TP/SL**: Aggregate risk management across all purchase types (DCA, TWAP, VWAP, etc.)
- **Wallet Tracker**: Public profile view exposing wallet metrics and holdings
- **Multi-language Support**: AI-powered automatic translation for global accessibility
- **Account Management**: Aggregated view of all wallets and positions
- Timeline targets December release but acknowledges holiday season challenges

#### Discussion Details
The fee customization feature will support:
- Token-level fees (by contract address)
- Provider-level fees (Pump Fund, Jupiter, etc.)
- Referral code discounts
- Platform-wide fee adjustments

Shakeib suggested moving multi-language support earlier in parallel with wallet tracker, and starting account management sooner. The team discussed the technical complexity of the account management feature, which requires shifting from single-wallet to multi-wallet paradigm and implementing real-time updates for up to 20 wallets per user.

---

### Topic 3: Performance Optimization Requirements

#### Executive Summary
Zen emphasized that speed and performance are critical for launch success. The team discussed current limitations in matching competitor speeds, particularly Bullex and Echo, and the need for infrastructure improvements including private mempool RPCs.

#### Key Takeaways
- Current implementation cannot match Bullex's transaction execution speed
- Need private mempool RPCs for improved performance
- Two backend developers dedicated to optimization this week
- Echo achieved 1-second candle charts - team working toward this goal
- Smart MEV protection requires private mempool implementation
- Consider leveraging internal stakeholder connections to Echo team for insights

#### Discussion Details
Martin confirmed that achieving Bullex-level speeds will require:
- Infrastructure changes including private mempool RPCs
- Continued optimization of current codebase
- Possible architectural changes for real-time data processing

Lucas noted that Bullex has proprietary RPC and routing systems that are difficult to replicate. The team discussed potentially getting help from the Echo team if internal connections exist, as they've achieved exceptional speed improvements.

---

### Topic 4: External Integrations and Pricing

#### Executive Summary
Lucas provided updates on pricing negotiations with data providers and discussed the unknown timeline impact of the AI Trading Journal integration from the DRUGS team.

#### Key Takeaways
- InsideX pricing: $1,200/month flat rate per chain (Solana)
- Bubble Maps (via Coingecko) being evaluated as alternative
- AI Trading Journal integration timeline unknown - cannot estimate without technical documentation
- Need endpoint specifications and potential refactoring requirements before estimation

#### Discussion Details
The DRUGS team integration remains a major unknown that could impact the roadmap. Shakeib has created a communication channel, but the team needs technical documentation before providing accurate estimates. The integration effort will depend on the endpoints required and any necessary refactoring.

---

### Topic 5: TradingView Integration Status

#### Executive Summary
The TradingView integration was completed yesterday but encountered build issues. Testing is pending for an important partner demo scheduled for tomorrow.

#### Key Takeaways
- Integration code merged but had build issues
- Martin fixed build issues today
- Testing still needed before partner demo
- First impressions crucial for partner relationship

#### Discussion Details
Martin integrated the feature yesterday but discovered it's not working properly yet. He will continue working on it and provide updates to ensure the demo can proceed smoothly.

---

## Decisions Made

1. **Prioritize fee customization before back office integration** - Required dependency for back office functionality
2. **Move multi-language support to run in parallel with wallet tracker** - Better resource utilization
3. **Use personal Apple Developer account temporarily** - Avoid delays in mobile testing

## Blockers and Risks Identified

- **Apple Developer Account** - Impact: High - Owner: Greg/Naji - Needs resolution by: Immediate
- **TradingView Integration Issues** - Impact: High - Owner: Martin - Needs resolution by: 2025-09-02
- **Performance Gap vs Competitors** - Impact: High - Owner: Martin/Backend Team - Ongoing
- **AI Trading Journal Integration Unknown Scope** - Impact: Medium - Owner: Lucas/Shakeib - Needs technical specs

## Parking Lot

- Smart MEV protection implementation details
- Specific performance benchmarking targets
- Holiday season launch strategy

## Next Steps

- Complete TradingView integration testing for partner demo
- Establish communication with DRUGS team for technical specifications
- Continue performance optimization efforts with focus on transaction speed
- Set up call with Joe for tomorrow at 5pm Emirates time

## References

- Cooking GT New Features document (Slack)
- Competitor Feature Comparison spreadsheet
- AI Product Layer documentation