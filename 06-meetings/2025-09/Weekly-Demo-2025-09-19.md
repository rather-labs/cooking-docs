---
title: Weekly Demo - September 19, 2025
type: meeting-note
date: 2025-09-19
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, perpetuals, clickhouse, portfolio, mobile]
summary: |
  Weekly development progress review featuring completion of major features including hotkeys, search behavior improvements, complete Perpetuals market order functionality, and significant Clickhouse performance improvements. Critical bug fixes for portfolio data accuracy and multiple frontend components under testing. Mobile development nears completion with trading operations integration underway.
related-docs:
  - [Perpetuals Market Order Documentation]
  - [Clickhouse Performance Improvements]
  - [Portfolio Data Accuracy Fixes]
  - [Mobile Trading Operations]
---

# Weekly Demo - September 19, 2025

**Date:** 2025-09-19
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week delivered significant completions across multiple platform components, marking substantial progress toward production readiness. The backend team completed hotkeys implementation, resolved Jupiter token search errors, and fixed critical social login bugs when linking Solana wallets. The Perpetuals market order functionality was fully completed, including order creation, closing, leverage updates, SOL to USDC conversions, and comprehensive history tracking. A critical bug causing errors when the Perpetuals page remained open for extended periods was resolved, improving stability.

Performance improvements through Clickhouse optimization are in testing, with significant impacts on TradingView charts loading and token metrics accuracy. The team is also testing order execution across all supported protocols and continuing Perpetuals withdrawal testing in both fast and slow modes. The indexer team addressed critical data accuracy issues including incorrect portfolio PnL calculations, invested amounts, and SOL balance displays for top traders. They also began tracking token supply for accurate market cap calculations and resolved issues with USDC/USDT population.

Frontend development is actively integrating and testing multiple features including Perpetuals limit orders, Token Details, Advanced Orders, and the Referral Program. Mobile development reached near completion with the referral system, portfolio, and positions features done pending testing, while token details and trading operations are being integrated.

## Action Items

- [ ] **Complete Clickhouse performance testing** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Resolve remaining portfolio data issues** - Assigned to: Indexer Team - Due: This week - Priority: Critical
- [ ] **Complete frontend feature testing** - Assigned to: Frontend Team - Due: Next sprint - Priority: High
- [ ] **Finalize mobile trading operations** - Assigned to: Mobile Team - Due: Next week - Priority: High
- [ ] **Deploy tested Perpetuals features** - Assigned to: DevOps Team - Due: After testing - Priority: High

## Index

1. Backend Completions and Testing
2. Indexer Data Accuracy Fixes
3. Frontend Integration and Testing
4. Mobile Near Completion
5. Performance Improvements

---

## Topics: Breakdown

### Topic 1: Backend Completions and Testing

#### Executive Summary
Backend team achieved multiple feature completions while advancing critical testing for platform-wide improvements and Perpetuals functionality.

#### Key Takeaways
**Completed:**
- Hotkeys implementation
- Search behavior improvements
- Jupiter token search error resolution
- Settings bug fix for Solana wallet linking
- Perpetuals Market Order complete functionality:
  - Create order
  - Close order through market order
  - Update leverage
  - Convert and deposit SOL to USDC
  - Order History
  - Funding History
  - Positions table
- Fixed Perpetuals timeout bug

**Testing:**
- Clickhouse improvements impacting:
  - TradingView Charts
  - Token metrics loading and accuracy
- Order execution for each supported protocol
- Perpetuals withdrawal (fast mode)
- Perpetuals deposit (slow mode)
- Perpetuals withdrawal (slow mode)

#### Discussion Details
The completion of Perpetuals market orders represents full trading capability for this feature. The Clickhouse improvements promise significant performance gains across data-intensive operations.

---

### Topic 2: Indexer Data Accuracy Fixes

#### Executive Summary
Indexer team resolved critical data accuracy issues affecting user portfolios and trading metrics while improving platform data quality.

#### Key Takeaways
**Testing:**
- Incorrect portfolio PnL data
- Incorrect portfolio invested amounts
- SOL balance showing 0 for top traders
- Token supply tracking for market cap calculations

**Completed:**
- USDC and USDT population issues resolved
- Clickhouse replica improvements

#### Discussion Details
The portfolio data accuracy issues were critical as they directly affected user's understanding of their trading performance. Token supply tracking enables accurate market cap calculations, essential for proper token valuation.

---

### Topic 3: Frontend Integration and Testing

#### Executive Summary
Frontend team is actively integrating and testing multiple major features approaching production deployment.

#### Key Takeaways
**Integrating and Testing:**
- Perpetuals limit orders
- Token Details interface
- Advanced Orders
- Referral Program

#### Discussion Details
These features represent core trading functionality and user acquisition mechanisms. Their successful integration and testing are crucial for platform launch.

---

### Topic 4: Mobile Near Completion

#### Executive Summary
Mobile development approaches completion with core features implemented and final integrations underway.

#### Key Takeaways
**Development done, pending test:**
- Referral system
- Portfolio
- Positions

**Integrating:**
- Token details and trading operations

#### Discussion Details
The mobile app is nearing feature completion, with only trading operations integration remaining. Testing remains blocked by Apple Account availability.

---

### Topic 5: Performance Improvements

#### Executive Summary
Significant performance improvements through Clickhouse optimization are in testing, promising better user experience across the platform.

#### Key Takeaways
- TradingView Charts loading optimization
- Token metrics accuracy improvements
- Overall query performance enhancements
- Reduced latency for data-intensive operations

---

## Decisions Made

1. **Prioritize data accuracy fixes** - Critical for user trust
2. **Complete Perpetuals testing before deployment** - High-risk feature requiring thorough validation
3. **Focus on core mobile features** - Ensure quality over quantity for initial release

## Blockers and Risks Identified

- **Portfolio data accuracy** - Impact: Critical - Owner: Indexer Team - Active resolution
- **Mobile testing blocked** - Impact: High - Owner: Management - Apple Account still needed

## Parking Lot

- Advanced Perpetuals features
- Extended mobile functionality
- Performance monitoring dashboard

## Next Steps

- Complete all active testing phases
- Resolve portfolio data accuracy issues
- Finish mobile trading operations integration
- Deploy completed features to staging
- Continue pursuing mobile testing capability

## References

- Perpetuals testing documentation
- Clickhouse optimization metrics
- Portfolio calculation specifications
- Mobile feature checklist