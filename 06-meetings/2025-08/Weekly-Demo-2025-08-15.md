---
title: Weekly Demo - August 15, 2025
type: meeting-note
date: 2025-08-15
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, monorepo, letsbonk, perpetuals, mobile, dns-blocking]
summary: |
  Weekly development progress review featuring monorepo refactoring for trading services, native Let'sBonk.Fun transaction implementation, Perpetuals UI deployment to DEV, and continued mobile development despite ongoing TestFlight blocking. Critical DNS records issue blocking backend testing identified. Frontend achieved multi-provider login capabilities and navigation improvements.
related-docs:
  - [Monorepo Migration Plan]
  - [Let'sBonk.Fun Integration]
  - [Perpetuals Testing Documentation]
  - [DNS Configuration Requirements]
---

# Weekly Demo - August 15, 2025

**Date:** 2025-08-15
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week marked significant architectural improvements with the backend team initiating a monorepo refactor for trading services (VWAP, TWAP, DCA) and extracting the HyperLiquid service, improving code organization and maintainability. The team completed backend integration for HyperLiquid contract information, though frontend integration remains pending. A critical achievement was the implementation of native Let'sBonk.Fun trade broadcasting, allowing direct interaction with this emerging launchpad.

However, the team faces a critical blocker with DNS records on NameCheap preventing backend refactor testing, which could delay deployment. The indexer team fixed important bugs including tokens being returned without providers (making them untradeable) and various validation errors, while also implementing Let'sBonk.Fun native transaction support.

Frontend development successfully deployed the Perpetuals UI to DEV for testing and enhanced the login screen with Gmail, Apple, and Telegram buttons, though Twitter and Wallet integration remain pending. Navigation improvements were delivered through sidebar and wallet selector updates. Mobile development continues despite the ongoing Apple Account blocker, with Wallet Management flows now under development while the team awaits TestFlight access for QA testing.

## Action Items

- [ ] **Configure DNS records on NameCheap** - Assigned to: DevOps/Management - Due: Immediate - Priority: Critical
- [ ] **Obtain Apple Account for TestFlight** - Assigned to: Management - Due: Immediate - Priority: Critical
- [ ] **Define Perpetuals fee structure** - Assigned to: Business Team - Due: Immediate - Priority: High
- [ ] **Complete frontend integration for contract info** - Assigned to: Frontend Team - Due: Next week - Priority: High
- [ ] **Implement Twitter and Wallet login** - Assigned to: Frontend Team - Due: Next sprint - Priority: Medium

## Index

1. Backend Monorepo Refactor
2. Critical Blockers and Pending Items
3. Indexer Bug Fixes
4. Frontend UI Deployment and Updates
5. Mobile Development Status

---

## Topics: Breakdown

### Topic 1: Backend Monorepo Refactor

#### Executive Summary
Backend team initiated significant architectural improvements through monorepo migration while completing critical Perpetuals and launchpad integrations.

#### Key Takeaways
- Refactored trading services (VWAP, TWAP, DCA) to monorepo architecture
- Extracted HyperLiquid service to monorepo
- Completed backend integration of HyperLiquid contract information
- Implemented native Let'sBonk.Fun trade broadcasting

#### Discussion Details
The monorepo refactor represents a major architectural improvement, centralizing related services for better code sharing and maintenance. This will significantly improve development velocity and reduce code duplication across trading services.

---

### Topic 2: Critical Blockers and Pending Items

#### Executive Summary
Multiple critical blockers are impacting development progress, with DNS configuration and business decisions preventing testing and deployment.

#### Key Takeaways
- DNS records on NameCheap blocking backend refactor testing
- Apple Account still unavailable for mobile TestFlight
- Perpetuals fee structure for deposits/withdrawals undefined
- Question about including fees in Partner Program schema unresolved

#### Discussion Details
The DNS configuration blocker is particularly critical as it prevents testing of the monorepo refactor, potentially delaying deployment of improved architecture. The continued absence of business decisions on fee structures is blocking Perpetuals completion.

---

### Topic 3: Indexer Bug Fixes

#### Executive Summary
Indexer team resolved critical bugs affecting token tradeability and data validation while implementing launchpad support.

#### Key Takeaways
- Fixed bug where tokens returned without provider (untradeable)
- Resolved validation errors across the system
- Implemented Let'sBonk.Fun native transaction broadcasting

#### Discussion Details
The provider bug fix is critical as it was preventing users from trading certain tokens. This directly impacted platform functionality and user experience.

---

### Topic 4: Frontend UI Deployment and Updates

#### Executive Summary
Frontend team successfully deployed Perpetuals to DEV and enhanced authentication options while improving navigation components.

#### Key Takeaways
- Deployed Perpetuals UI to DEV environment
- Added Gmail, Apple, and Telegram login buttons
- Pending: Twitter and Wallet integration
- Pending: Complete visual update of login screen
- Updated Sidebar navigation component
- Updated Wallet selector component

---

### Topic 5: Mobile Development Status

#### Executive Summary
Mobile team continues development despite critical TestFlight blocker, focusing on core wallet functionality.

#### Key Takeaways
- Awaiting TestFlight for QA process initiation
- Developing Wallet Management flows
- First initiative remains untested due to Apple Account absence

---

## Decisions Made

None - still awaiting critical business decisions and infrastructure access.

## Blockers and Risks Identified

- **DNS records configuration** - Impact: Critical - Owner: DevOps/Management - Needs resolution by: Immediate
- **Apple Account missing** - Impact: Critical - Owner: Management - Needs resolution by: Immediate
- **Perpetuals fees undefined** - Impact: High - Owner: Business Team - Needs resolution by: This week
- **Mobile timeline risk** - Impact: High - Owner: Mobile Team - Blocked by Apple Account

## Parking Lot

- Monorepo deployment strategy
- Complete authentication provider integration
- Mobile beta testing approach

## Next Steps

- Configure DNS records immediately
- Acquire Apple Developer Account urgently
- Obtain fee structure decisions
- Complete Perpetuals testing once DNS resolved
- Continue mobile development in parallel

## References

- Monorepo architecture documentation
- DNS configuration requirements
- Let'sBonk.Fun API documentation
- Mobile testing strategy (blocked)