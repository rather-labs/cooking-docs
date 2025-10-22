---
title: Weekly Demo - May 16, 2025
type: meeting-note
date: 2025-05-16
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, testing]
summary: |
  Weekly development progress review covering significant work across backend, indexer, and frontend. Main focus on testing improvements to queries for various trading features (Specials, Limit Orders, DCA, TWAP, VWAP), new launchpad support (pump.fun, moonshot), and multiple UI fixes. All development was done locally due to AWS DEV deployment being blocked from May 9-15.
related-docs:
  - [Technical assessment between Jupiter and HelloMoon's swap API]
---

# Weekly Demo - May 16, 2025

**Date:** 2025-05-16
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week's development progress was significantly impacted by the inability to deploy to the DEV AWS environment from May 9th to 15th, requiring all development work to be completed locally with testing pending. Despite this constraint, the team made substantial progress across all major components of the Cooking platform.

The backend team focused heavily on improving query performance for various trading features including Specials, Limit Orders, DCA, TWAP, VWAP, and Wallet operations, all awaiting testing. A technical assessment was also conducted comparing Jupiter and HelloMoon's swap API solutions to determine the optimal integration path.

The indexer team enhanced support for emerging launchpads with improvements to pump.fun and moonshot minting capabilities and bonding curves, along with Raydium AMM enhancements. Frontend development addressed multiple user interface issues including button sizing, image caching, privacy improvements for referrals, and the implementation of a token stream pause feature for the Kitchen interface.

## Action Items

- [ ] **Complete testing of backend query improvements** - Assigned to: Backend Team - Due: Next sprint - Priority: High
- [ ] **Complete testing of indexer improvements for launchpads** - Assigned to: Indexer Team - Due: Next sprint - Priority: High
- [ ] **Test and validate frontend fixes in DEV environment** - Assigned to: Frontend Team - Due: When AWS access restored - Priority: High
- [ ] **Finalize technical assessment of swap APIs** - Assigned to: Backend Team - Due: Next week - Priority: Medium

## Index

1. Development Environment Constraints
2. Backend Development Progress
3. Indexer Improvements
4. Frontend Updates and Fixes

---

## Topics: Breakdown

### Topic 1: Development Environment Constraints

#### Executive Summary
AWS DEV environment was inaccessible for deployment from May 9-15, forcing all development work to be completed locally with testing deferred until environment access is restored.

#### Key Takeaways
- All development from May 9-15 was done locally
- Testing is pending for all features developed during this period
- AWS access restoration is critical for validation

---

### Topic 2: Backend Development Progress

#### Executive Summary
Backend team focused on query optimization for trading features and conducted a technical assessment of swap API solutions, with all improvements awaiting testing.

#### Key Takeaways
- Technical assessment completed comparing Jupiter vs HelloMoon swap APIs
- Query improvements implemented for Specials (pending testing)
- Query improvements implemented for Limit Orders (pending testing)
- Query improvements implemented for DCA operations (pending testing)
- Query improvements implemented for TWAP operations (pending testing)
- Query improvements implemented for VWAP operations (pending testing)
- Query improvements implemented for Wallet operations (pending testing)

---

### Topic 3: Indexer Improvements

#### Executive Summary
Indexer team enhanced support for emerging launchpads and improved AMM functionality, with all features pending testing in the DEV environment.

#### Key Takeaways
- Enhanced mint support for pump.fun platform (pending testing)
- Enhanced mint support for moonshot platform (pending testing)
- Improved bonding curves for pump.fun (pending testing)
- Improved bonding curves for moonshot (pending testing)
- Enhanced AMM functionality for Raydium (pending testing)

---

### Topic 4: Frontend Updates and Fixes

#### Executive Summary
Frontend team addressed multiple UI/UX issues and implemented new features to improve user experience, with several items already deployed and others pending testing.

#### Key Takeaways
- Fixed 'Search' button color issue
- Fixed 'Activate' button sizing in DCA orders
- Improved image caching performance
- Implemented privacy protection for referral names through truncation
- Fixed field validations in withdraw wallet creation
- Added vertical separators to Token Details screen
- Implemented pause functionality for token stream on hover in Kitchen (pending testing)
- Fixed total rewards display in Referral Program (pending testing)
- Added success toast for Referral Program reward retrieval (pending testing)
- Fixed token social link navigation issue (pending testing)
- Fixed SOL/USD currency toggle in Token Details price indicator (pending testing)

---

## Decisions Made

1. **Local development approach** - Continue development locally until AWS access restored
2. **Prioritize testing queue** - All pending features to be tested immediately upon environment restoration

## Blockers and Risks Identified

- **AWS DEV Environment Access** - Impact: High - Owner: DevOps Team - Needs resolution by: Immediate

## Parking Lot

- Long-term infrastructure improvements to prevent deployment blockages
- Backup deployment environment considerations

## Next Steps

- Restore AWS DEV environment access
- Execute comprehensive testing of all pending features
- Complete swap API technical assessment decision
- Continue with next sprint development priorities

## References

- Technical assessment documentation for Jupiter vs HelloMoon comparison
- AWS deployment issue tracking ticket