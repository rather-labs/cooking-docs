---
title: Weekly Demo - September 26, 2025
type: meeting-note
date: 2025-09-26
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, perpetuals, performance, mobile, beta-launch]
summary: |
  Weekly development progress review showing significant completions across the platform. Backend achieved major milestones with Perpetuals slow withdraw/deposit testing, external wallet support, and comprehensive performance improvements. Frontend completed multiple features including Perpetuals operations, user settings, and chart enhancements. Indexer resolved critical data issues and improved filtering. Mobile continues with trading operations and pending orders implementation.
related-docs:
  - [Perpetuals Complete Feature Set]
  - [Performance Improvements Documentation]
  - [External Wallet Support]
  - [Beta Launch Preparation]
---

# Weekly Demo - September 26, 2025

**Date:** 2025-09-26
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week marked substantial progress toward platform readiness with multiple critical features reaching completion and testing phases. The backend team is actively testing Perpetuals slow withdraw and deposit functionality while supporting externally created Solana wallets, a key feature for user onboarding. Major completions include resolution of internal order execution errors, significant loading time and chart population improvements, full social login implementation, Cooking tag support, and custom referral code functionality.

The frontend team achieved several important milestones including Perpetuals limit orders testing, market cap implementation, extended timeframe charts with USD valuation, and import functionality for external Solana wallets. Completed features include fast deposit/withdraw for Perpetuals, market close operations, resolution of multiple UI bugs, and full User Settings implementation.

The indexer team successfully resolved critical issues including bonding curve completion tracking for new tokens, portfolio data accuracy problems, token supply tracking for price bars, and price outlier filtering for cleaner charts. They also fixed holding amount duplication and SOL balance display issues for top traders. Mobile development continues with trading operations and token history implementation, while work progresses on pending orders functionality.

## Action Items

- [ ] **Complete Perpetuals slow mode testing** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Finalize external wallet support testing** - Assigned to: Backend/Frontend Teams - Due: Next sprint - Priority: High
- [ ] **Deploy all completed features to staging** - Assigned to: DevOps Team - Due: Next week - Priority: High
- [ ] **Complete mobile trading operations** - Assigned to: Mobile Team - Due: Next sprint - Priority: High
- [ ] **Prepare for beta launch** - Assigned to: All Teams - Due: After testing completion - Priority: Critical

## Index

1. Backend Testing and Completions
2. Frontend Feature Completions
3. Indexer Critical Fixes
4. Mobile Final Development
5. Platform Readiness Status

---

## Topics: Breakdown

### Topic 1: Backend Testing and Completions

#### Executive Summary
Backend team achieved major completions while advancing critical testing for Perpetuals and external wallet support.

#### Key Takeaways
**Testing:**
- Slow withdraw for Perpetuals
- Slow deposit for Perpetuals
- Support for externally created Solana wallets

**Completed:**
- Internal error resolution for order execution across providers
- Significant improvements in loading times and chart population
- Full social login implementation
- Cooking tag support
- Custom referral code functionality

#### Discussion Details
The support for externally created wallets is crucial for users who already have Solana wallets and want to import them. The performance improvements directly impact user experience with faster loading times.

---

### Topic 2: Frontend Feature Completions

#### Executive Summary
Frontend team completed multiple critical features and resolved numerous bugs, significantly improving platform stability and functionality.

#### Key Takeaways
**Testing:**
- Perpetuals limit orders
- Scroll issues on certain breakpoints in Perpetuals
- Market Cap implementation
- Charts with extended timeframes
- USD valuation on charts
- Advanced orders UI alignment
- Import externally created Solana wallets

**Completed:**
- Fast deposit for Perpetuals
- Fast withdraw for Perpetuals
- Market Close for Perpetuals
- Multiple UI bug fixes
- User Settings full implementation

#### Discussion Details
The completion of Perpetuals fast operations provides users with quick access to their funds. Extended timeframe charts and USD valuation enhance trading analysis capabilities.

---

### Topic 3: Indexer Critical Fixes

#### Executive Summary
Indexer team resolved multiple critical data accuracy issues and implemented important filtering improvements.

#### Key Takeaways
**Testing:**
- Bonding curve marked as completed for newly minted tokens
- Incorrect data on certain tracked tokens in Portfolio
- Token supply tracking for bars
- Price outliers filter for charts
- Pump.fun trades filter tracking corrections

**Completed:**
- Fixed holding amount duplication on token positions
- Fixed SOL balance display for top traders

#### Discussion Details
These fixes are critical for data accuracy and user trust. The price outlier filtering will result in cleaner, more readable charts by removing anomalous data points.

---

### Topic 4: Mobile Final Development

#### Executive Summary
Mobile team continues final feature implementation for trading functionality and order management.

#### Key Takeaways
- Trading operations implementation ongoing
- Token history implementation ongoing
- Pending orders functionality in development

#### Discussion Details
These represent the final core features needed for mobile launch. Trading operations are essential for users to execute trades from mobile devices.

---

### Topic 5: Platform Readiness Status

#### Executive Summary
The platform is approaching beta launch readiness with most critical features completed or in final testing phases.

#### Key Takeaways
- Core trading features completed
- Performance optimizations implemented
- Data accuracy issues resolved
- User onboarding features ready
- Mobile app nearing completion

---

## Decisions Made

1. **Support external wallets** - Enable existing Solana users to easily onboard
2. **Implement comprehensive referral system** - Drive user acquisition
3. **Prioritize data accuracy** - Essential for user trust

## Blockers and Risks Identified

- **Mobile testing capability** - Impact: High - Owner: Management - Still awaiting Apple Account
- **Beta launch coordination** - Impact: Medium - Owner: All Teams - Requires synchronized deployment

## Parking Lot

- Post-beta feature roadmap
- Advanced analytics features
- Mobile app store submission

## Next Steps

- Complete all active testing
- Deploy completed features to staging
- Prepare beta launch plan
- Finalize mobile trading operations
- Coordinate beta launch activities

## References

- Beta launch checklist
- Feature completion status
- Testing documentation
- Performance benchmarks report