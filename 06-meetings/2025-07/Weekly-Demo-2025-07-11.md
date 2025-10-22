---
title: Weekly Demo - July 11, 2025
type: meeting-note
date: 2025-07-11
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, hyperliquid, turnkey, clickhouse, perpetuals, mobile]
summary: |
  Weekly development progress review featuring completion of HyperLiquid Core integration, Turnkey wallet infrastructure for perpetuals, significant Clickhouse migration progress, and advancement in frontend component systems. Mobile development continued with progress on authentication flows despite ongoing infrastructure challenges.
related-docs:
  - [HyperLiquid Core Integration Complete]
  - [Perpetuals Infrastructure Documentation]
  - [Clickhouse Migration Status]
---

# Weekly Demo - July 11, 2025

**Date:** 2025-07-11
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week marked the successful completion of critical infrastructure components for perpetual trading capabilities. The backend team achieved a major milestone by finishing the HyperLiquid Core Integration and completing the Turnkey and wallet infrastructure necessary for perpetuals trading. This establishes the foundation for users to engage in perpetual futures trading on the platform. The Trades database migration to Clickhouse was also completed, continuing the systematic performance improvement initiative.

The indexer team collaborated on the Clickhouse migration efforts and successfully resolved QuickNode connectivity issues that were impacting data reliability. These connectivity improvements ensure more stable and consistent blockchain data indexing. Frontend development made significant progress with skeleton loaders now integrated across multiple critical screens including Positions modal, Portfolio page, Token Details, and Custom Orders, greatly improving the user experience during data loading states.

The team also completed new component systems for Quick Order Panel forms, buttons, cards, and icons, establishing a consistent design language across the platform. Work began on the Perpetuals screens, translating the backend capabilities into user-facing interfaces. Mobile development continued despite challenges, with ongoing work on color alignment and authentication flows.

## Action Items

- [ ] **Deploy HyperLiquid integration to staging** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Complete Perpetuals UI screens** - Assigned to: Frontend Team - Due: Next sprint - Priority: High
- [ ] **Resolve remaining QuickNode issues** - Assigned to: Indexer Team - Due: Ongoing - Priority: Medium
- [ ] **Continue mobile authentication implementation** - Assigned to: Mobile Team - Due: Next sprint - Priority: Medium

## Index

1. Backend Perpetuals Infrastructure
2. Database Migration and Indexer Updates
3. Frontend Component Systems
4. Mobile Development Progress

---

## Topics: Breakdown

### Topic 1: Backend Perpetuals Infrastructure

#### Executive Summary
Backend team completed critical infrastructure for perpetual trading, establishing the foundation for this major new platform feature.

#### Key Takeaways
- Completed HyperLiquid Core Integration
- Finished Turnkey and Wallet Infrastructure for Perpetuals
- Established secure wallet generation for perpetual trading
- Completed Trades database migration to Clickhouse

#### Discussion Details
The completion of HyperLiquid Core Integration represents a major technical achievement, enabling the platform to offer perpetual futures trading. The Turnkey integration ensures secure wallet management for these high-stakes trading operations.

---

### Topic 2: Database Migration and Indexer Updates

#### Executive Summary
Continued progress on Clickhouse migration and resolution of connectivity issues improved platform reliability and performance.

#### Key Takeaways
- Successfully migrated Trades database to Clickhouse
- Collaborated with backend on Clickhouse optimization
- Resolved QuickNode connectivity issues affecting data indexing

#### Discussion Details
The QuickNode connectivity resolution was critical for maintaining reliable blockchain data feeds. The Trades database migration to Clickhouse continues the pattern of significant performance improvements seen with previous migrations.

---

### Topic 3: Frontend Component Systems

#### Executive Summary
Frontend team expanded skeleton loader implementation and completed multiple component systems, significantly improving UI consistency and loading experiences.

#### Key Takeaways
- Implemented skeleton loaders in Positions modal
- Implemented skeleton loaders in Portfolio Page
- Implemented skeleton loaders in Token Details
- Implemented skeleton loaders in Custom Orders
- Completed QoP (Quick Order Panel) form components
- Completed button component system
- Completed card component system
- Completed icon component system
- Started development on Perpetuals screens

#### Discussion Details
The widespread implementation of skeleton loaders addresses a critical UX issue where users previously faced blank screens during data loading. The completion of component systems ensures consistent design patterns for future development.

---

### Topic 4: Mobile Development Progress

#### Executive Summary
Mobile team continued progress on foundational features despite ongoing challenges with development infrastructure.

#### Key Takeaways
- Continued work on color alignment with brand
- Ongoing development of Signup/Login flows
- Progressing on Home screen implementation

---

## Decisions Made

1. **Prioritize Perpetuals UI completion** - Match frontend with completed backend capabilities
2. **Continue aggressive Clickhouse migration** - Performance benefits justify continued effort

## Blockers and Risks Identified

- **Mobile development infrastructure** - Impact: Medium - Owner: Mobile Team - Needs resolution by: Ongoing

## Parking Lot

- Perpetuals trading risk management features
- Advanced charting for perpetuals
- Mobile testing infrastructure

## Next Steps

- Deploy HyperLiquid integration to staging environment
- Complete Perpetuals UI implementation
- Continue Clickhouse migration for remaining tables
- Resolve mobile development infrastructure issues

## References

- HyperLiquid Core integration documentation
- Turnkey wallet infrastructure guide
- Perpetuals UI design specifications