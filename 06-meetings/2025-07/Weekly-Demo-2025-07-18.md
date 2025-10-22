---
title: Weekly Demo - July 18, 2025
type: meeting-note
date: 2025-07-18
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, hyperliquid, jupiter, mobile, ramp-solutions]
summary: |
  Weekly development progress review featuring completion of HyperLiquid SOL deposit flow, full Jupiter token support in DEV, significant frontend component testing, and mobile development progress including ramp solution research and Telegram login completion. The team also achieved important bug fixes for PumpSwap transaction parsing and Raydium trade performance improvements.
related-docs:
  - [HyperLiquid Deposit Flow Documentation]
  - [Jupiter Token Support Implementation]
  - [Mobile Ramp Solutions Comparison]
---

# Weekly Demo - July 18, 2025

**Date:** 2025-07-18
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week delivered significant progress in platform capabilities and mobile development foundation. The backend team completed the HyperLiquid SOL deposit flow, enabling users to fund their perpetual trading accounts, and achieved full support for Jupiter listed tokens in the DEV environment, substantially expanding tradeable assets. Continued work on HyperLiquid integration promises to deliver complete perpetual trading functionality soon.

The indexer team resolved critical bugs affecting PumpSwap failed transaction parsing and improved Raydium trade performance, enhancing platform reliability. Testing of migrated trades in Clickhouse confirmed the performance benefits of the new architecture. Frontend development reached a testing phase for multiple new component systems including search modals, badges, tables, selects, dialogs, toasts, and inputs. The Perpetuals UI components are also in final testing, including wallet selection, dashboard, search functionality, and deposit/convert modals.

Mobile development achieved a significant milestone with Telegram login functionality completed and tested. The team conducted research on ramp solutions, evaluating Crossmint and Onramper for fiat on-ramp capabilities. Continued progress on the home screen and authentication flows establishes a solid foundation for the mobile application launch.

## Action Items

- [ ] **Deploy Jupiter token support to production** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Complete HyperLiquid integration** - Assigned to: Backend Team - Due: Next sprint - Priority: High
- [ ] **Finalize ramp solution selection** - Assigned to: Mobile Team - Due: Next week - Priority: Medium
- [ ] **Complete frontend component testing** - Assigned to: Frontend Team - Due: Next week - Priority: Medium

## Index

1. Backend Trading Capabilities
2. Indexer Bug Fixes and Performance
3. Frontend Component Testing
4. Mobile Development Milestones

---

## Topics: Breakdown

### Topic 1: Backend Trading Capabilities

#### Executive Summary
Backend team completed critical trading infrastructure with HyperLiquid deposits operational and full Jupiter token support ready for deployment.

#### Key Takeaways
- Completed HyperLiquid SOL Deposit Flow
- Achieved full support for Jupiter listed tokens in DEV
- Continuing work on remaining HyperLiquid integration features

#### Discussion Details
The completion of the SOL deposit flow enables users to fund their HyperLiquid accounts directly from the platform, a critical step for perpetual trading. Jupiter token support dramatically expands the number of tradeable assets available on the platform.

---

### Topic 2: Indexer Bug Fixes and Performance

#### Executive Summary
Indexer team resolved critical parsing errors and performance issues while validating Clickhouse migration benefits.

#### Key Takeaways
- Fixed bug for parsing PumpSwap failed transactions
- Completed testing of migrated trades in Clickhouse
- Improved performance for Raydium trades

#### Discussion Details
The PumpSwap parsing fix ensures that failed transactions are properly tracked, providing users with complete transaction history. Raydium performance improvements directly impact the user experience for one of the most popular DEXs.

---

### Topic 3: Frontend Component Testing

#### Executive Summary
Frontend team advanced to comprehensive testing phase for new component systems and Perpetuals UI, nearing production readiness.

#### Key Takeaways
- Testing Search Token modal
- Testing Badge component
- Testing Tables component
- Testing Selects component
- Testing Dialog component
- Testing Toast notifications
- Testing Input components
- Testing Perpetuals WalletSelect UI
- Testing Perpetuals Dashboard UI
- Testing Search Perpetual Contract functionality
- Testing Deposit Modal
- Testing Convert Modal

#### Discussion Details
The comprehensive testing phase ensures all new components meet quality standards before production deployment. The Perpetuals UI testing is particularly critical given the high-stakes nature of perpetual trading.

---

### Topic 4: Mobile Development Milestones

#### Executive Summary
Mobile team completed critical authentication infrastructure and began evaluating fiat on-ramp solutions for seamless user onboarding.

#### Key Takeaways
- Completed research on ramp solutions (Crossmint vs Onramper)
- Finished and tested Telegram login functionality
- Continuing work on Home/Sign Up/Log In screens

#### Discussion Details
The ramp solution selection is critical for mobile user acquisition, as it enables users to fund their accounts directly with fiat currency. Telegram login provides a seamless authentication option for the large Telegram user base in crypto.

---

## Decisions Made

1. **Evaluate Crossmint vs Onramper** - Decision pending on mobile ramp solution
2. **Proceed with Jupiter token deployment** - Ready for production after DEV validation

## Blockers and Risks Identified

- **Ramp solution selection** - Impact: Medium - Owner: Mobile Team - Needs resolution by: Next week

## Parking Lot

- Additional authentication methods for mobile
- Advanced perpetuals features
- Mobile beta testing strategy

## Next Steps

- Complete HyperLiquid integration
- Deploy Jupiter tokens to production
- Select and integrate mobile ramp solution
- Finish component testing and deploy to production

## References

- Jupiter token list documentation
- HyperLiquid deposit flow specs
- Crossmint vs Onramper comparison analysis