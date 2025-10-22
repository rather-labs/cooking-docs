---
title: Weekly Demo - June 27, 2025
type: meeting-note
date: 2025-06-27
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, hyperliquid, clickhouse, whitelist, perpetuals]
summary: |
  Weekly development progress review featuring completion of whitelist access control, significant infrastructure improvements with Clickhouse integration, initial HyperLiquid Core integration work, and frontend standardization efforts. The team made important progress on platform security, performance optimization through new database architecture, and began implementation of the Perpetuals trading interface.
related-docs:
  - [Whitelist Access Control Implementation]
  - [Clickhouse Migration Strategy]
  - [HyperLiquid Integration Documentation]
---

# Weekly Demo - June 27, 2025

**Date:** 2025-06-27
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week marked significant progress in platform security, infrastructure modernization, and new feature development. The backend team successfully completed implementation and testing of the whitelist solution for controlling platform access, providing granular control over user onboarding. A major refactoring of the Statuses and cache service was completed to improve performance and ensure consistency across the platform. Initial integration work began with HyperLiquid Core, laying the foundation for perpetual trading capabilities, while Jupiter Supported Tokens work continued.

The indexer team achieved a major milestone by completing Clickhouse integration on a RatherLabs internal account, pending deployment to the Cooking AWS environment. This new database architecture promises significant performance improvements for data-intensive operations. Multiple critical components were migrated to the new Indexer Provider including Bars (supporting charts and price feeds), Token Details, and Positions tables.

Frontend development focused on standardization and consistency improvements, including normalized modal and table structures, skeleton loader implementation for better perceived performance, a new 404 error page for invalid token searches, and initial work on the Perpetuals trading screen. These improvements enhance user experience through consistent interface patterns and better loading state management.

## Action Items

- [ ] **Enable Clickhouse on Cooking AWS account** - Assigned to: DevOps Team - Due: Next week - Priority: High
- [ ] **Complete HyperLiquid Core integration** - Assigned to: Backend Team - Due: Next 2 weeks - Priority: High
- [ ] **Finalize Perpetuals screen implementation** - Assigned to: Frontend Team - Due: Next sprint - Priority: High
- [ ] **Deploy whitelist solution to production** - Assigned to: Backend Team - Due: Next week - Priority: Medium

## Index

1. Backend Security and Infrastructure
2. Indexer Database Migration
3. Frontend Standardization
4. New Feature Development

---

## Topics: Breakdown

### Topic 1: Backend Security and Infrastructure

#### Executive Summary
Backend team delivered critical security enhancements and infrastructure improvements while beginning integration with HyperLiquid for perpetual trading capabilities.

#### Key Takeaways
- Completed implementation and testing of whitelist access control
- Refactored Statuses and cache service for improved performance
- Ensured consistency across platform through cache improvements
- Continued work on Jupiter Supported Tokens
- Initiated HyperLiquid Core integration

#### Discussion Details
The whitelist solution provides essential access control capabilities, allowing the platform to manage user onboarding strategically. The cache service refactor addresses previous inconsistencies in data presentation across different platform components.

---

### Topic 2: Indexer Database Migration

#### Executive Summary
Indexer team achieved significant progress in migrating to Clickhouse architecture, promising substantial performance improvements for the platform.

#### Key Takeaways
- Completed Clickhouse integration on RatherLabs internal account
- Pending enablement on Cooking AWS account
- Migrated Bars to Indexer Provider (powers charts and last traded prices)
- Migrated Token Details to Indexer Provider
- Migrated Positions to Indexer Provider
- Continued development on Jupiter Supported Tokens

#### Discussion Details
The Clickhouse migration represents a fundamental infrastructure improvement, moving from traditional relational databases to a columnar database optimized for analytical queries. This change is expected to dramatically improve query performance for large datasets.

---

### Topic 3: Frontend Standardization

#### Executive Summary
Frontend team focused on creating consistent user interface patterns and improving loading state management across the platform.

#### Key Takeaways
- Normalized modal structure for consistency
- Added skeleton loader to Quick Operations panel
- Implemented 404 screen for invalid token address searches
- Normalized table structure across platform

#### Discussion Details
The standardization efforts ensure a consistent user experience across all platform features, reducing cognitive load and improving usability. Skeleton loaders provide better perceived performance during data fetching.

---

### Topic 4: New Feature Development

#### Executive Summary
Initial development work began on the Perpetuals trading interface, a major new feature for the platform.

#### Key Takeaways
- Started initial work on Perpetuals screen
- Laying groundwork for perpetual trading functionality
- Coordinating with backend HyperLiquid integration

---

## Decisions Made

1. **Proceed with Clickhouse migration** - Commit to new database architecture for performance
2. **Implement whitelist for controlled access** - Enable strategic user onboarding
3. **Standardize UI components** - Ensure consistency across platform

## Blockers and Risks Identified

- **Clickhouse AWS enablement pending** - Impact: High - Owner: DevOps Team - Needs resolution by: Next week

## Parking Lot

- Clickhouse optimization strategies
- Extended whitelist functionality
- Perpetuals trading risk management features

## Next Steps

- Enable Clickhouse on Cooking AWS account
- Continue HyperLiquid integration
- Complete Perpetuals UI implementation
- Deploy whitelist to production

## References

- Clickhouse migration documentation
- HyperLiquid API specifications
- Whitelist implementation guide