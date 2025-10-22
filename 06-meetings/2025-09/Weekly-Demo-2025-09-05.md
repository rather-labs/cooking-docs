---
title: Weekly Demo - September 5, 2025
type: meeting-note
date: 2025-09-05
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, perpetuals, performance, mobile, terms-conditions]
summary: |
  Weekly development progress review featuring continued Perpetuals development, significant performance improvements across services, successful social login implementation, and advancement in frontend visual updates. Mobile referral system completed pending testing. Critical pending items include Terms and Conditions and social media accounts blocking mobile release.
related-docs:
  - [Performance Optimization Metrics]
  - [Social Login Implementation]
  - [Terms and Conditions Requirements]
  - [Mobile Release Blockers]
---

# Weekly Demo - September 5, 2025

**Date:** 2025-09-05
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week delivered important progress on platform performance and user experience enhancements. The backend team continued developing Perpetuals slow mode for deposits and withdrawals while implementing significant performance improvements for main screen loading and service data exposure. Social login testing was completed successfully, marking a major milestone for user onboarding flexibility. The team identified critical platform dependencies requiring immediate attention: Terms and Conditions documentation needed for both web and mobile platforms, and X/Twitter and Discord accounts for community building.

The indexer team made substantial improvements to Clickhouse query definitions, enhancing platform performance, while also improving block indexing to prefer higher quality prices and implementing SPL token burn event handling. These changes directly impact data accuracy and user experience. Frontend development progressed with the implementation of User Settings modal for account linking/de-linking, additional navigation hotkeys for power users, and visual updates to the Kitchen interface. The new login screen implementation was completed, modernizing the authentication experience.

Mobile development successfully implemented the referral system (pending testing) and the security password creation flow (pending testing), while continuing work on Wallet functionality. The Terms and Conditions requirement was identified as a critical blocker for mobile release, requiring immediate business attention.

## Action Items

- [ ] **Create Terms and Conditions document** - Assigned to: Legal/Business - Due: Immediate - Priority: Critical
- [ ] **Create X/Twitter and Discord accounts** - Assigned to: Marketing/Business - Due: This week - Priority: High
- [ ] **Complete Perpetuals slow mode** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Test mobile referral system** - Assigned to: Mobile Team - Due: When TestFlight available - Priority: High
- [ ] **Deploy new login screen** - Assigned to: Frontend Team - Due: Next sprint - Priority: Medium

## Index

1. Backend Performance and Features
2. Indexer Optimization
3. Frontend User Experience Updates
4. Mobile Development Progress
5. Critical Pending Definitions

---

## Topics: Breakdown

### Topic 1: Backend Performance and Features

#### Executive Summary
Backend team focused on performance optimization and completing critical authentication features while advancing Perpetuals capabilities.

#### Key Takeaways
- Actively developing Perpetuals slow mode for deposits/withdrawals
- Implementing performance improvements for main screen loading
- Optimizing data exposure for different services
- Social login successfully tested and implemented

#### Discussion Details
The performance improvements for main screens directly impact user experience, reducing load times and improving responsiveness. The successful social login implementation provides multiple authentication options, crucial for user acquisition.

---

### Topic 2: Indexer Optimization

#### Executive Summary
Indexer team delivered multiple improvements enhancing data quality and query performance across the platform.

#### Key Takeaways
- Updated Clickhouse query definitions for performance
- Improved block indexing to prefer higher quality prices
- Implemented SPL token burn event handling

#### Discussion Details
The preference for higher quality prices in block indexing ensures users see the most accurate and reliable price data. SPL token burn handling is essential for accurate supply tracking and market cap calculations.

---

### Topic 3: Frontend User Experience Updates

#### Executive Summary
Frontend team enhanced user control and navigation efficiency while progressing visual standardization efforts.

#### Key Takeaways
- Implementing User Settings modal for account linking/de-linking
- Adding extra navigation hotkeys for efficiency
- Applying visual updates to Kitchen interface
- Testing typography and color alignment to Ooze designs
- New login screen successfully implemented

#### Discussion Details
The User Settings modal provides users with control over their linked accounts, essential for the multi-provider authentication system. Navigation hotkeys significantly improve efficiency for power traders.

---

### Topic 4: Mobile Development Progress

#### Executive Summary
Mobile team completed critical features but remains blocked by testing infrastructure and business requirements.

#### Key Takeaways
- Referral system successfully implemented (pending testing)
- Security password creation flow completed (pending testing)
- Continuing development on Wallet functionality
- Blocked by Terms and Conditions requirement

#### Discussion Details
The Terms and Conditions document is a critical blocker for mobile release, as app stores require this for publication. Without it, the mobile app cannot proceed to testing or release.

---

### Topic 5: Critical Pending Definitions

#### Executive Summary
Several business-level decisions and assets are blocking development progress across platforms.

#### Key Takeaways
- Terms and Conditions required for web and mobile (blocking mobile)
- X/Twitter account needed for social features and community
- Discord account needed for community building

---

## Decisions Made

1. **Prioritize Terms and Conditions creation** - Critical blocker for mobile
2. **Establish social media presence** - Required for community features
3. **Continue performance optimization** - Key differentiator for platform

## Blockers and Risks Identified

- **Terms and Conditions missing** - Impact: Critical - Owner: Legal/Business - Blocking mobile release
- **Social media accounts missing** - Impact: Medium - Owner: Marketing - Needed for launch
- **Apple TestFlight access** - Impact: High - Owner: Management - Ongoing blocker

## Parking Lot

- Community management strategy
- Content moderation policies
- Advanced hotkey customization

## Next Steps

- Create Terms and Conditions immediately
- Establish X/Twitter and Discord accounts
- Complete Perpetuals slow mode development
- Continue mobile development pending blockers
- Deploy completed frontend features

## References

- Terms and Conditions template requirements
- Social media account setup guide
- Performance optimization benchmarks
- Mobile app store requirements