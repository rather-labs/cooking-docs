---
title: Cooking Weekly Sync - September 22, 2025
type: meeting-note
date: 2025-09-22
attendees: [Lucas Cufré, Naji Osmat, Gregory Chapman, Zen]
meeting-type: standup
tags: [cooking-app, development-update, mobile-development, charts, gaming, pvp]
summary: |
  Weekly sync meeting discussing the current state of the Cooking app development. Key updates included fixes for chart outliers, market cap and liquidity issues, progress on limit orders, and mobile app development status. The team also tested the new PvP gaming feature and discussed future gaming additions like slots.
related-docs:
  - Development roadmap
  - Mobile app testing documentation
---

# Cooking Weekly Sync - September 22, 2025

**Date:** 2025-09-22
**Time:** Duration approximately 18 minutes
**Attendees:** Lucas Cufré, Naji Osmat, Gregory Chapman, Zen
**Facilitator:** Lucas Cufré (presenting updates)

## Executive Summary

This weekly sync meeting focused on critical updates for the Cooking platform development. Lucas Cufré led the discussion by presenting the current state of development efforts across multiple fronts. The team has successfully identified and begun addressing the chart outlier issues that have been affecting the user experience, implementing a first version of a filter to create smoother price charts that better match competitor offerings. Significant progress was made on the desktop application with fixes for market cap and liquidity display issues, and the team expects to have limit order functionality ready for production by end of day.

Mobile development is progressing according to schedule with the onboarding flow, Kitchen page, wallet management, and portfolio overview completed. The development team expects to complete the mobile app development within two weeks, aligning with the desktop roadmap timeline. However, testing and App Store deployment processes will add additional time to the release schedule.

The latter portion of the meeting shifted to testing the new PvP gaming feature, where Gregory and Zen conducted live testing of the $5 betting functionality. While some connection issues were identified for players joining matches, the game proved engaging and addictive according to team feedback. Future plans include adding slot games and building an IP around the gaming platform with potential marketing support from the Abstract team's agency.

## Action Items

- [ ] **Complete chart filtering implementation for smoother display** - Assigned to: Development Team - Due: 2025-09-22 (EOD) - Priority: High
- [ ] **Deploy market cap as Y-axis parameter on charts** - Assigned to: Development Team - Due: 2025-09-22 (EOD) - Priority: High
- [ ] **Complete limit order testing and production deployment** - Assigned to: Development Team - Due: 2025-09-22 (EOD) - Priority: High
- [ ] **Merge PRs for token details and advanced orders** - Assigned to: Development Team - Due: 2025-09-22 (EOD) - Priority: High
- [ ] **Deploy Cooking tag feature** - Assigned to: Development Team - Due: 2025-09-22 - Priority: Medium
- [ ] **Message team when last changes are pushed for video** - Assigned to: Lucas Cufré - Due: 2025-09-22 (EOD) - Priority: High
- [ ] **Send Fireflies recording to Lucas** - Assigned to: Naji Osmat - Due: 2025-09-22 - Priority: Low
- [ ] **Provide mobile demo video for Friday** - Assigned to: Lucas Cufré - Due: 2025-09-27 - Priority: Medium
- [ ] **Fix PvP connection issues for joining players** - Assigned to: QQ - Due: ASAP - Priority: High
- [ ] **Add back button navigation to gaming platform** - Assigned to: QQ - Due: TBD - Priority: Low
- [ ] **Populate Velvet Vault VIPs leaderboard** - Assigned to: Gregory/Team - Due: TBD - Priority: Low

## Index

1. Chart Outliers and Filtering Implementation
2. Market Cap and Liquidity Fixes
3. Limit Orders and Advanced Trading Features
4. User Settings and Security Features
5. Mobile Application Development Progress
6. PvP Gaming Platform Testing
7. Future Gaming Features and Marketing Strategy

---

## Topics: Breakdown

### Topic 1: Chart Outliers and Filtering Implementation

#### Executive Summary
The development team has identified the root cause of chart outliers and implemented a first version of a filter to address the issue. The goal is to match competitor chart displays while maintaining accuracy of actual Solana network prices.

#### Key Takeaways
- Root cause of chart outliers has been identified
- First version of filter is now deployed
- Team is working to match competitor chart displays
- Larger candles still visible represent actual price movements on Solana
- Full implementation expected by end of day for video recording

#### Discussion Details
Lucas explained that while the filter is working, some larger candles remain visible as these represent legitimate price movements tracked on the Solana network. The team is balancing accuracy with user experience to create smoother charts that align with industry standards.

---

### Topic 2: Market Cap and Liquidity Fixes

#### Executive Summary
Fixes for market cap and liquidity display issues have been deployed, with additional work underway to implement market cap as the Y-axis parameter on charts.

#### Key Takeaways
- Market cap and liquidity issues are now fixed in production
- Implementation of market cap on Y-axis is in progress
- Expected completion by end of day
- Team wants stable version before video recording begins

---

### Topic 3: Limit Orders and Advanced Trading Features

#### Executive Summary
Limit order functionality is nearing completion with testing beginning today and production deployment expected by end of day. Front-end implementation is more than halfway complete.

#### Key Takeaways
- Limit order testing starting today
- Production deployment expected by end of day
- Front-end implementation over 50% complete
- Advanced orders form using Leo's latest design
- Several PRs ready to merge for token details

#### Discussion Details
The team has made significant progress on advanced trading features with multiple pull requests ready for merging. The implementation follows the latest design specifications from Leo.

---

### Topic 4: User Settings and Security Features

#### Executive Summary
All logging methodologies have been tested successfully, with the Cooking tag feature ready for deployment and security password creation/update functionality implemented.

#### Key Takeaways
- All logging methods tested and working
- Cooking tag feature deployment scheduled for today
- Shortcuts tested on both Mac and Windows
- Security tab implementation complete
- Users can create and update security passwords

---

### Topic 5: Mobile Application Development Progress

#### Executive Summary
Mobile development is on track with core features completed and token details/trading operations currently in development. The team expects development completion in two weeks, with additional time needed for testing and App Store approval.

#### Key Takeaways
- Completed: onboarding flow, sign-up/login, Kitchen page, quick buy, wallet management, portfolio overview, search
- In progress: token details page and trading operations
- Development timeline: 2 weeks to completion
- Testing estimated at 2 additional weeks
- App Store approval process timing uncertain

#### Discussion Details
Lucas emphasized that while development is on schedule, the testing phase has been delayed as it wasn't conducted alongside development. The App Store submission process adds uncertainty to the final release timeline, potentially requiring a week or more for approval.

---

### Topic 6: PvP Gaming Platform Testing

#### Executive Summary
Gregory and Zen conducted live testing of the PvP gaming feature, identifying some connection issues but finding the game engaging and addictive. The $5 betting functionality is working with minor bugs to address.

#### Key Takeaways
- PvP hosting works reliably, joining has intermittent connection issues
- Game is "really addicting" according to team feedback
- Players lose money quickly without realizing (good for engagement)
- Color coding needed: player should always be green, opponent red
- P&L page has display issues on some devices
- Referral system working but claiming functionality needs adjustment

#### Discussion Details
During live testing, the team discovered that while hosting PvP matches works well, players joining matches sometimes experience connection delays or failures. The game's difficulty and pacing successfully masks how quickly players lose money, which the team views as positive for engagement. Several UI improvements were identified including the need for consistent back button navigation and proper color coding for players.

---

### Topic 7: Future Gaming Features and Marketing Strategy

#### Executive Summary
Plans are underway to expand the gaming platform with slot games and build an intellectual property around it, with potential marketing support from the Abstract team's agency.

#### Key Takeaways
- Slot games planned as next addition after current game completion
- Building IP around gaming platform for marketing purposes
- Abstract team's agency willing to provide heavy marketing push
- Multiple game types being considered: Plinko, coin toss, slots
- Focus on creating unified gaming experience under single brand

#### Discussion Details
Zen revealed plans to leverage connections with the Abstract team's marketing agency for promotional support. While the Abstract team cannot officially promote directly, their agency can provide significant marketing push including retweets and campaigns. Gregory, with prior experience in online slots, will lead UX planning for the slot game addition.

---

## Decisions Made

1. **Proceed with chart filtering to match competitor displays** - Balancing accuracy with user experience
2. **Maintain current mobile development timeline** - Two weeks for development completion
3. **Expand gaming platform with slots next** - Building IP around gaming offerings
4. **Leverage Abstract team's agency for marketing** - Unofficial promotion through their marketing agency

## Blockers and Risks Identified

- **PvP connection issues for joining players** - Impact: High - Owner: QQ - Needs resolution by: ASAP
- **Mobile testing delays** - Impact: Medium - Owner: Lucas - Testing not conducted alongside development
- **App Store approval timeline uncertainty** - Impact: Medium - Owner: Team - Could delay mobile launch by 1+ weeks

## Parking Lot

- Detailed slot game UX planning
- Full gaming platform branding and IP development
- Marketing campaign specifics with Abstract team's agency

## Next Steps

- Complete all end-of-day deliverables for video recording
- Continue mobile development according to 2-week timeline
- Begin comprehensive mobile testing phase
- Address PvP gaming connection issues
- Start planning slot game implementation

## References

- Development roadmap documentation
- Leo's design specifications for advanced orders
- Mobile testing protocols
- Gaming platform technical specifications