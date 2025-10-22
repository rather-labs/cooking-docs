---
title: Cooking Weekly Sync
type: meeting-note
date: 2025-09-12
attendees: [Naji Osmat, Martin Aranda, Lucas Cufré, Gregory Chapman, Shakib (mentioned)]
meeting-type: technical
tags: [ui-issues, performance, testing, video-production, backend-optimization]
summary: |
  Technical sync meeting focused on addressing critical UI and performance issues in the Cooking platform that are blocking video production for partners. The team reviewed multiple bugs including incorrect token values, slow loading times, and UI/UX inconsistencies. Key decisions were made about displaying values in USD by default and prioritizing performance optimization through load balancer implementation.
related-docs:
  - Development environment updates
  - Backend optimization roadmap
---

# Cooking Weekly Sync

**Date:** 2025-09-12
**Time:** Not specified (approximately 28 minutes)
**Attendees:** Naji Osmat, Martin Aranda, Lucas Cufré, Gregory Chapman, Shakib (mentioned but didn't join)
**Facilitator:** Naji Osmat

## Executive Summary

The team conducted a thorough review of the Cooking platform's production environment, identifying multiple critical issues that are preventing the creation of partner demonstration videos. Naji Osmat walked through several user experience problems while testing the platform with real funds, including incorrect token holdings display, infinite loading states, and chart rendering issues.

The discussion revealed that many of these issues stem from backend performance problems and incomplete data indexing for older tokens. The team agreed on several UI/UX improvements, particularly around displaying values in USD by default rather than Solana, and committed to fixing the most critical issues by end of week. A major backend optimization effort including load balancer implementation was identified as crucial for platform stability.

Gregory Chapman emphasized that these issues are blocking video production for partners, as the current state makes it difficult to demonstrate the platform's features effectively. The team agreed to prioritize fixing existing features before deploying new ones like perpetuals to production.

## Action Items

- [ ] **Fix token holdings display to show dollar values instead of percentages** - Assigned to: Lucas Cufré - Due: This week - Priority: High
- [ ] **Implement carousel for token display with quick operations panel** - Assigned to: Lucas Cufré - Due: This week - Priority: High
- [ ] **Add redirect functionality when clicking on tokens in portfolio** - Assigned to: Martin Aranda (ticket already created) - Due: This week - Priority: High
- [ ] **Complete backend optimization and load balancer implementation** - Assigned to: DevOps team - Due: End of week - Priority: High
- [ ] **Fix chart rendering issues (candle-by-candle loading bug)** - Assigned to: Backend team - Due: Already fixed in dev - Priority: High
- [ ] **Update all market cap and liquidity calculations** - Assigned to: Backend team - Due: Next week - Priority: High
- [ ] **Complete UI revamp for all pages** - Assigned to: Frontend team - Due: End of next week - Priority: High
- [ ] **Add migration countdown/timer for tokens** - Assigned to: Frontend team - Due: This week - Priority: Medium
- [ ] **Fix slider functionality for percentage input** - Assigned to: Frontend team - Due: This week - Priority: Medium
- [ ] **Send meeting minutes** - Assigned to: Lucas Cufré - Due: End of day - Priority: Low

## Index

1. Platform Stability and Performance Issues
2. Token Display and Portfolio Management
3. Chart and Market Data Accuracy
4. UI/UX Improvements and Standardization
5. Video Production Blockers
6. Development and Deployment Strategy

---

## Topics: Breakdown

### Topic 1: Platform Stability and Performance Issues

#### Executive Summary
The platform is experiencing severe performance issues with endpoints timing out and infinite loading states, making it nearly unusable for testing and video production. The team identified that backend optimization and load balancer implementation are critical to resolving these issues.

#### Key Takeaways
- Multiple endpoints are experiencing timeouts and infinite loading states
- Quick menu and token details pages frequently fail to load
- DevOps is conducting an audit of all performance pain points
- Load balancer implementation is expected this week
- Development environment is more stable than production currently

#### Discussion Details
The team discussed moving testing to the development environment as it has more recent fixes and better performance. Martin suggested this as a temporary solution while the production environment is being stabilized. The load balancer implementation through AWS is expected to significantly improve loading times across all screens.

---

### Topic 2: Token Display and Portfolio Management

#### Executive Summary
Current token display shows misleading information with percentage changes instead of dollar values for holdings, and users cannot easily navigate to token details from their portfolio. These issues significantly impact user experience and understanding of their positions.

#### Key Takeaways
- Token holdings currently show percentages (0.01%) instead of dollar values
- Portfolio clicks only copy addresses instead of redirecting to token pages
- Need to implement a carousel for all owned tokens with quick operations access
- P&L calculations are incorrect for some tokens (Pengu and Launchpad)
- Positions modal needs UI updates to match new design

#### Discussion Details
Lucas explained that the original design showed P&L fluctuation based on last purchase price, but users expect to see actual dollar holdings. The team identified data inconsistencies with tokens traded before the latest deployment, particularly affecting Pengu and Launchpad tokens. A ticket has already been created for the portfolio redirect functionality.

---

### Topic 3: Chart and Market Data Accuracy

#### Executive Summary
Charts and market data display numerous inaccuracies including wrong market caps, incorrect liquidity values, and prices shown in Solana instead of USD. The backend refactor is needed to properly calculate total supply and provide accurate data.

#### Key Takeaways
- Market cap shows negative values for established tokens (e.g., -$40 for multi-billion dollar coins)
- Charts default to Solana values instead of USD
- Liquidity calculations are incorrect due to indexing issues
- Backend refactor needed to recalculate total supply for accurate market cap
- Team decided to show market cap and liquidity in USD only, no Solana option

#### Discussion Details
The root cause is that market cap was only calculated when tokens were first indexed, causing issues for older tokens. Charts currently show prices in Solana regardless of the platform toggle setting. Naji emphasized that traders make decisions based on dollar values, not Solana values, especially since most new tokens have standardized 1 billion supply.

---

### Topic 4: UI/UX Improvements and Standardization

#### Executive Summary
The platform needs consistent value display standards, with USD as the default across all interfaces. Several UI elements need refinement including sliders, input fields, and the migration status display.

#### Key Takeaways
- Default all displays to USD with optional Solana toggle only where appropriate
- Slider needs to function as a percentage selector, not require manual input
- Cannot enter negative values in percentage fields
- Migration status needs countdown timer or progress indicator
- "Invested" values should display in USD to match "Holdings" display

#### Discussion Details
The team agreed that while buying might happen in Solana, trading decisions are based on USD values. The slider functionality issue where users must input percentages manually rather than sliding to select was identified as a poor UX pattern. Leo hasn't responded to questions about expected slider behavior, so the team decided on a standard single-pointer slider implementation.

---

### Topic 5: Video Production Blockers

#### Executive Summary
Gregory Chapman emphasized that current platform issues are preventing the creation of demonstration videos for partners. The instability and errors make it impossible to showcase the platform's features effectively.

#### Key Takeaways
- Partner video production is blocked by platform instability
- Quick menu feature cannot be properly demonstrated due to loading issues
- Zain shared the environment believing it was ready, but issues remain
- Need stable environment for recording without errors or long load times
- Team should prioritize fixing current features before adding new ones

#### Discussion Details
Nadia experienced numerous errors when trying to buy tokens during video recording attempts. The quick menu, identified as a main UX feature to showcase, frequently fails to load. Gregory suggested focusing on stabilizing existing features before deploying perpetuals to production.

---

### Topic 6: Development and Deployment Strategy

#### Executive Summary
The team agreed to focus on stabilizing current features in production before adding new functionality. Development environment will be used for testing while production is being optimized.

#### Key Takeaways
- QA is ongoing for all UI updates in development environment
- New login, user settings, and kitchen already implemented in dev
- Token details expected complete by end of day or tomorrow
- All UI revamp expected complete and QA'd by end of next week
- Perpetuals won't be deployed to production until current issues are resolved

#### Discussion Details
Lucas outlined the current state of development: login, user settings, and kitchen are complete; token details nearly done; wallet manager and portfolio still need work. Martin confirmed perpetuals are not yet in production and Gregory advocated for keeping them out until the current environment is stable.

---

## Decisions Made

1. **Display all market caps and liquidity in USD only** - No Solana option needed as traders make decisions based on dollar values
2. **Use development environment for testing and video recording** - More stable with recent fixes while production is being optimized
3. **Prioritize fixing existing features over deploying new ones** - Don't add perpetuals until current issues resolved
4. **Default entire UI to USD** - With toggle to Solana only where it makes sense (not for charts/market cap)
5. **Implement standard slider behavior** - Single pointer that sets percentage by position, not manual input

## Blockers and Risks Identified

- **Backend performance issues** - Impact: High - Owner: DevOps team - Needs resolution by: End of week
- **Incorrect token data for older tokens** - Impact: High - Owner: Backend team - Needs resolution by: Next week
- **Video production blocked** - Impact: High - Owner: Development team - Needs resolution by: This week
- **Load balancer implementation delay** - Impact: High - Owner: DevOps - Needs resolution by: This week

## Parking Lot

- Perpetuals deployment and testing
- Full positions modal UI update
- Additional token data sources and integrations

## Next Steps

- Immediate focus on performance optimization and load balancer implementation
- Complete critical UI fixes by end of week
- Move testing to development environment
- Complete all UI revamps by end of next week
- Prepare stable environment for partner video production

## References

- Development environment for testing
- Backend optimization roadmap
- UI/UX design specifications
- Meeting recording (Fireflies - to be shared by Naji)