---
title: Weekly Demo - August 8, 2025
type: meeting-note
date: 2025-08-08
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, perpetuals, auth0, mobile, apple-testflight]
summary: |
  Weekly development progress review showing significant advancement in Perpetuals functionality with contract information and withdrawal features nearing completion. Important decisions pending on fees and referral codes. Auth0 implementation initiated for improved authentication. Mobile development completed first initiative but remains blocked by Apple Account availability.
related-docs:
  - [Perpetuals Fee Structure Proposal]
  - [Auth0 Integration Plan]
  - [Mobile TestFlight Requirements]
---

# Weekly Demo - August 8, 2025

**Date:** 2025-08-08
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week saw substantial progress on the Perpetuals trading feature despite some pending business decisions. The backend team nearly completed critical components including contract information retrieval for traded assets and USDC to SOL withdrawal functionality. Both features are pending final integration and testing. Important decisions are still needed regarding cooking fees for deposits/withdrawals and the referral code structure for perpetuals. The team also initiated work on geoblocking for regulatory compliance and began implementing Auth0 to improve user wallet creation through Turnkey integration.

The indexer team resolved a critical bug affecting Total Holders calculation and optimized Let'sBonk performance on Clickhouse, improving data accuracy and query speed. Frontend development is approaching deployment readiness with the Perpetuals interface completed and ready for DEV environment testing. The team continued work on aligning the visual library between Figma designs and the codebase, ensuring consistency across all interfaces.

Mobile development reached a significant milestone with the first initiative tentatively complete, including QA testing. However, the team remains critically blocked by the absence of an Apple Account, preventing TestFlight deployment and formal testing. Development has begun on Wallet Management and Portfolio features while waiting for the blocker to be resolved.

## Action Items

- [ ] **Define cooking fees for Perps deposits/withdrawals** - Assigned to: Business Team - Due: Immediate - Priority: High
- [ ] **Determine Perpetuals referral code structure** - Assigned to: Business Team - Due: Next week - Priority: High
- [ ] **Acquire Apple Account for TestFlight** - Assigned to: Management - Due: Critical/Immediate - Priority: Critical
- [ ] **Complete Perps contract info integration** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Deploy Perpetuals UI to DEV** - Assigned to: Frontend Team - Due: Next sprint - Priority: High

## Index

1. Backend Perpetuals Development
2. Pending Business Decisions
3. Indexer Bug Fixes and Optimization
4. Frontend and Mobile Progress

---

## Topics: Breakdown

### Topic 1: Backend Perpetuals Development

#### Executive Summary
Backend team made significant progress on Perpetuals functionality with contract information and withdrawal features nearing completion, while initiating important security and authentication improvements.

#### Key Takeaways
- Almost finished getting contract information for each traded asset (pending integration and testing)
- Almost finished USDC to SOL withdrawal functionality
- Started security implementation for geoblocking users
- Initiated Auth0 implementation for improved Turnkey wallet creation

#### Discussion Details
The contract information retrieval is essential for displaying accurate perpetual contract details to users. The withdrawal functionality enables users to convert their USDC trading collateral back to SOL for withdrawal from the platform. Geoblocking implementation is crucial for regulatory compliance in restricted jurisdictions.

---

### Topic 2: Pending Business Decisions

#### Executive Summary
Critical business decisions are needed to complete Perpetuals implementation, particularly regarding fee structures and referral programs.

#### Key Takeaways
- Cooking fees for deposits/withdrawals need to be determined
- Question raised about including these fees in Partner Program schema
- Perpetuals referral code structure needs definition

#### Discussion Details
These decisions are blocking final implementation of the Perpetuals feature. The fee structure will impact user economics and platform revenue. The referral code system needs to be designed to incentivize user acquisition while maintaining profitability.

---

### Topic 3: Indexer Bug Fixes and Optimization

#### Executive Summary
Indexer team resolved critical calculation bugs and improved performance for recently integrated features.

#### Key Takeaways
- Fixed bug affecting Total Holders calculation
- Implemented performance improvements for Let'sBonk on Clickhouse
- Improved data accuracy and query performance

---

### Topic 4: Frontend and Mobile Progress

#### Executive Summary
Frontend team completed Perpetuals UI ready for testing while mobile development finished first initiative but remains blocked by infrastructure issues.

#### Key Takeaways
- Perpetuals UI ready for DEV deployment and testing
- Continued visual library alignment between Figma and codebase
- Mobile first initiative tentatively complete
- Apple Account still blocking TestFlight and QA testing
- Started development on Wallet Management and Portfolio features

#### Discussion Details
The continued absence of an Apple Account is creating significant risk for mobile delivery timelines. Despite development progress, no formal testing or validation can occur without TestFlight access.

---

## Decisions Made

None - waiting on critical business decisions for Perpetuals fees and referral structure.

## Blockers and Risks Identified

- **Perpetuals fee structure undefined** - Impact: High - Owner: Business Team - Needs resolution by: Immediate
- **Apple Account missing** - Impact: Critical - Owner: Management - Needs resolution by: Immediate
- **Mobile delivery timeline at risk** - Impact: High - Owner: Mobile Team - Blocked by Apple Account

## Parking Lot

- Perpetuals advanced features (leverage adjustments, advanced order types)
- Mobile beta testing strategy
- Auth0 migration timeline for existing users

## Next Steps

- Obtain business decisions on Perpetuals fees and referral codes
- Urgently acquire Apple Developer Account
- Complete Perpetuals backend integration
- Deploy and test Perpetuals UI in DEV
- Continue mobile development while pursuing TestFlight access

## References

- Perpetuals contract specifications
- Auth0 integration documentation
- Mobile delivery timeline (at risk)
- Fee structure proposal document (pending)