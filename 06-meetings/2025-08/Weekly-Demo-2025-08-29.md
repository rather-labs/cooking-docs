---
title: Weekly Demo - August 29, 2025
type: meeting-note
date: 2025-08-29
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, perpetuals, referrals, pump-fun, mobile]
summary: |
  Weekly development progress review highlighting significant database migrations for performance optimization, active testing of Perpetuals and referral features, resolution of TradingView chart implementation, and progress on social login capabilities. Critical work addressing Pump.Fun outage and continued mobile development with referral system integration despite ongoing TestFlight blocking.
related-docs:
  - [Diamond Hands Badge Implementation]
  - [Perpetuals Testing Results]
  - [Social Login Integration]
  - [Pump.Fun Outage Response]
---

# Weekly Demo - August 29, 2025

**Date:** 2025-08-29
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week marked significant progress in platform optimization and feature testing despite ongoing challenges. The backend team completed crucial migrations for badge calculations (Diamond Hands, Snipers, Insiders) and marketplace metrics (Mints, Bonding Curve, AMMs) in preparation for showing maker badges in tables. Custom referral codes entered testing phase while the multi-level referral program continues development. Active testing of Perpetuals functionality progressed across multiple features including surcharge application, position management, and order execution, with slow mode deposits and withdrawals now in active development.

Social login capabilities advanced significantly with X (Twitter) and Solana Wallet login entering testing phase, along with account linking and de-linking functionality. The indexer team worked to address a Pump.Fun outage while completing the same badge calculation migrations as the backend. Frontend successfully implemented and tested Advanced TradingView Charts across multiple interfaces (Perpetuals, Token Details, Quick Operations, Advanced Orders) and began UI typography and color alignment updates.

Mobile development achieved a major milestone with referral program integration despite the continued absence of TestFlight access for testing. The persistent Apple Account blocker continues to threaten delivery timelines, though development proceeds in parallel.

## Action Items

- [ ] **Complete Perpetuals slow mode testing** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Resolve Pump.Fun outage issues** - Assigned to: Indexer Team - Due: Ongoing - Priority: High
- [ ] **Finalize social login testing** - Assigned to: Backend Team - Due: Next sprint - Priority: Medium
- [ ] **Deploy UI updates after testing** - Assigned to: Frontend Team - Due: Next week - Priority: Medium
- [ ] **Obtain Apple Account for mobile testing** - Assigned to: Management - Due: Critical - Priority: Critical

## Index

1. Backend Testing and Development
2. Indexer Migrations and Outage Response
3. Frontend Chart Implementation and UI Updates
4. Mobile Referral Integration
5. Active Testing Summary

---

## Topics: Breakdown

### Topic 1: Backend Testing and Development

#### Executive Summary
Backend team progressed through extensive testing of critical features while developing new capabilities for enhanced platform functionality.

#### Key Takeaways
Migrations completed:
- Diamond Hands calculations
- Snipers calculations
- Insiders calculations
- Mints calculations
- Bonding Curve calculations
- AMMs calculations

Testing phase:
- Custom referral codes implementation
- Multi-level referral program (in development)

Perpetuals testing (active):
- Surcharge application with builder codes
- TP/SL settings
- Position closing (full and partial)
- Limit and market order creation
- Position/order/funding/trade data retrieval

Perpetuals development (active):
- Slow mode for deposits and withdrawals

Social login testing (active):
- X (Twitter) login integration
- Solana Wallet login
- Account linking functionality
- Account de-linking functionality

#### Discussion Details
The badge calculation migrations enable the platform to display maker badges in tables, providing users with important signals about token creators and early participants. The slow mode development for Perpetuals addresses high-value transactions requiring additional security.

---

### Topic 2: Indexer Migrations and Outage Response

#### Executive Summary
Indexer team completed critical migrations while actively addressing platform reliability issues from external dependencies.

#### Key Takeaways
- Completed same badge calculations as backend
- Actively working on Pump.Fun outage issues
- Ensuring data consistency across migrated metrics

#### Discussion Details
The Pump.Fun outage represents a critical issue as it's a major source of new token launches. The team is implementing fallback mechanisms to maintain platform functionality during provider outages.

---

### Topic 3: Frontend Chart Implementation and UI Updates

#### Executive Summary
Frontend team successfully deployed advanced charting capabilities and began comprehensive UI standardization efforts.

#### Key Takeaways
- Advanced TradingView Charts successfully implemented
- Deployed across Perpetuals, Token Details, Quick Operations, Advanced Orders
- Resolved various visual bugs
- Started UI updates for typography and color alignment
- Testing first iteration of visual alignment to Ooze's design language

---

### Topic 4: Mobile Referral Integration

#### Executive Summary
Mobile team achieved referral system integration despite continued testing infrastructure challenges.

#### Key Takeaways
- Referral system successfully integrated into mobile app
- Continued Apple Account blocker preventing testing
- Development proceeding despite inability to validate

---

### Topic 5: Active Testing Summary

#### Executive Summary
Multiple critical features are in various stages of testing, indicating imminent production deployments.

#### Key Takeaways
Backend actively testing:
- Perpetuals full feature set
- Social login with multiple providers
- Custom referral codes

Frontend actively testing:
- Advanced TradingView Charts (completed)
- UI visual updates
- Typography and color alignment

Mobile pending testing:
- Referral system integration
- Entire first initiative

---

## Decisions Made

1. **Prioritize badge display features** - Enhance user intelligence about token creators
2. **Implement Pump.Fun fallbacks** - Ensure platform resilience
3. **Proceed with UI standardization** - Improve visual consistency

## Blockers and Risks Identified

- **Apple Account missing** - Impact: Critical - Owner: Management - Needs resolution by: Immediate
- **Pump.Fun outage** - Impact: High - Owner: Indexer Team - Active mitigation ongoing
- **Mobile testing impossible** - Impact: High - Owner: Mobile Team - Blocked by Apple Account

## Parking Lot

- Advanced badge analytics
- Multi-provider outage handling
- Mobile beta distribution strategy

## Next Steps

- Complete Perpetuals slow mode implementation
- Finalize social login testing and deployment
- Continue Pump.Fun outage mitigation
- Deploy UI updates after testing
- Urgently resolve Apple Account issue

## References

- Badge calculation specifications
- Perpetuals testing documentation
- Social login integration guide
- Pump.Fun API status