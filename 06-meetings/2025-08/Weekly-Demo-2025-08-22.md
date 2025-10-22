---
title: Weekly Demo - August 22, 2025
type: meeting-note
date: 2025-08-22
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, perpetuals, referrals, mobile, social-login]
summary: |
  Weekly development progress review showing significant advancement in Perpetuals functionality with multiple features pending test despite DNS blocking. Major improvements include custom referral codes implementation, multi-level referral program development, and comprehensive bug fixes across the platform. Mobile development faces potential delays due to continued Apple Account unavailability, now exploring EvilMartians design integration.
related-docs:
  - [Perpetuals Testing Suite]
  - [Referral Program Enhancement]
  - [Bug Fix Documentation]
  - [Mobile Design Alignment]
---

# Weekly Demo - August 22, 2025

**Date:** 2025-08-22
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week delivered substantial progress on Perpetuals functionality and platform enhancements despite ongoing infrastructure blockers. The backend team completed development of comprehensive Perpetuals features including surcharge application, TP/SL settings, position management, and order execution capabilities, though testing remains blocked by DNS record issues. Significant platform improvements were achieved with custom referral codes now in testing and multi-level referral program under development. Critical bug fixes were implemented including Telegram-Chrome connectivity issues, Security Password creation problems, and Custom Orders fetching errors.

The indexer team enhanced Raydium Launchpad functionality to support latest provider updates and conducted a full service review in preparation for beta launch. They also implemented special case mapping for token indexing, improving platform coverage. Frontend development is actively testing the complete Perpetuals feature set while addressing multiple UI bugs including symbol/name display corrections, value overflow in limit orders, and readability improvements. The new login screen implementation marks a significant UX improvement.

Mobile development faces increasing timeline pressure with the Apple Account still unavailable, prompting the team to communicate high probability of delivery delays. Social login implementation was completed, and work continues on Wallet and Portfolio Management while updating the visual language to align with EvilMartians designs.

## Action Items

- [ ] **Resolve DNS records immediately** - Assigned to: Management/DevOps - Due: Critical/Immediate - Priority: Critical
- [ ] **Complete Perpetuals testing once DNS resolved** - Assigned to: Backend Team - Due: Upon DNS fix - Priority: High
- [ ] **Finalize referral program features** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Address mobile timeline concerns** - Assigned to: Management - Due: Immediate - Priority: High
- [ ] **Complete UI bug fixes** - Assigned to: Frontend Team - Due: Next sprint - Priority: Medium

## Index

1. Backend Perpetuals Features (Pending Test)
2. Bug Fixes and Platform Improvements
3. Frontend Testing and UI Updates
4. Mobile Development Challenges
5. Next Development Priorities

---

## Topics: Breakdown

### Topic 1: Backend Perpetuals Features (Pending Test)

#### Executive Summary
Backend team completed comprehensive Perpetuals functionality development, with all features awaiting testing once DNS blocking is resolved.

#### Key Takeaways
Features pending test (blocked by DNS):
- Apply surcharge on perp operations with builder codes
- Set TP/SL (Take Profit/Stop Loss) on perpetuals
- Fully and partially close positions
- Open limit orders
- Open market orders
- Get position data
- Get order history
- Get funding history
- Get user trades

#### Discussion Details
The completion of these features represents full Perpetuals functionality. The DNS blocking is critical as these high-risk trading features require thorough testing before production deployment.

---

### Topic 2: Bug Fixes and Platform Improvements

#### Executive Summary
Multiple critical bugs were resolved improving platform stability, while new referral features enhance user acquisition capabilities.

#### Key Takeaways
Bugs Fixed:
- Telegram connection issues with Google Chrome
- Security Password creation and wallet interaction problems
- User orders fetching issues in Custom Orders tables

New Features:
- Custom referral codes (testing phase)
- Multi-level referral program (development phase)

---

### Topic 3: Frontend Testing and UI Updates

#### Executive Summary
Frontend team is actively testing Perpetuals while addressing numerous UI improvements and implementing enhanced authentication options.

#### Key Takeaways
Testing:
- Complete Perpetuals feature end-to-end

Bugs Fixed:
- Changed SYMBOL to NAME in Token Details and Search
- Fixed value overstepping iconography in limit orders
- Added empty state for unsuccessful token searches
- Fixed Ctrl+K issue on Chrome/Windows
- Fixed 'copied to clipboard' toast notifications
- Improved Security Password modal readability

New Features:
- New login screen implementation

---

### Topic 4: Mobile Development Challenges

#### Executive Summary
Mobile team continues development under severe timeline pressure due to ongoing Apple Account blocker, while making progress on core features.

#### Key Takeaways
- High probability of delivery delay communicated
- Social login implementation completed
- Wallet Management development ongoing
- Portfolio Management development ongoing
- Visual language update to EvilMartians designs in progress

#### Discussion Details
The team has formally communicated delivery risks due to the Apple Account blocker. Without TestFlight access, no testing or validation can occur, creating cascading delays.

---

### Topic 5: Next Development Priorities

#### Executive Summary
Team identified clear priorities for upcoming development once current blockers are resolved.

#### Key Takeaways
Backend Next:
- Finish Twitter and Solana Wallet login integration
- Complete referral program custom codes
- Finalize multi-level referral program
- Support externally created Solana wallets
- Add wallet indicators to tables and Bubblemaps
- Implement auto-adjusting priority fees

Frontend Next:
- Complete new login screen
- Implement referral program custom codes UI
- Build multi-level referral program interface
- Update TradingView charts
- Implement multi-chart view

---

## Decisions Made

1. **Communicate mobile delivery risks** - Formal notification of potential delays due to blockers
2. **Prioritize Perpetuals testing** - Critical feature requiring thorough validation
3. **Advance referral programs** - Key growth mechanism for platform

## Blockers and Risks Identified

- **DNS records configuration** - Impact: Critical - Owner: Management - Needs resolution by: Immediate
- **Apple Account missing** - Impact: Critical - Owner: Management - Needs resolution by: Immediate
- **Mobile delivery delay** - Impact: High - Owner: Mobile Team - Risk communicated
- **Perpetuals testing blocked** - Impact: High - Owner: Backend Team - Blocked by DNS

## Parking Lot

- Advanced Perpetuals features
- Complete social login integration
- Mobile testing strategy

## Next Steps

- Resolve DNS configuration immediately
- Execute Perpetuals testing suite upon DNS resolution
- Continue referral program development
- Address mobile timeline with stakeholders
- Complete frontend bug fixes

## References

- Perpetuals feature specifications
- Referral program design document
- Mobile risk assessment
- Bug tracking system