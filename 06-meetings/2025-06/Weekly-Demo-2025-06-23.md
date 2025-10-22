---
title: Weekly Demo - June 23, 2025
type: meeting-note
date: 2025-06-23
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, performance, jupiter-swap, redis]
summary: |
  Weekly development progress review highlighting completed Jupiter Swap API integration testing, implementation of fallback swap aggregator strategy, significant performance improvements through query migrations and Redis implementation, and comprehensive frontend updates for wallet management and UI consistency. The team successfully tested critical features and delivered important UX improvements.
related-docs:
  - [Jupiter Swap API Integration]
  - [Swap Aggregator Fallback Strategy]
  - [Redis Implementation Documentation]
---

# Weekly Demo - June 23, 2025

**Date:** 2025-06-23
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week's development cycle achieved significant milestones in platform reliability and performance optimization. The backend team completed comprehensive testing of the Jupiter Swap API integration, a critical component for trading functionality. They also implemented a robust fallback strategy for swap aggregators with a defined priority order (Jupiter → HelloMoon → Cooking), ensuring trading continuity even if primary services experience issues. Performance improvements continued with the migration of userTrades queries and successful testing of wallet naming functionality.

The indexer team made substantial infrastructure improvements by implementing Redis for JSON block storage, significantly enhancing data handling performance. They also cleaned up the database by removing old tables, improving overall indexer efficiency, and continued advancing Jupiter token support capabilities.

Frontend development delivered a complete set of improvements for the Wallet Manager, including the full implementation of wallet naming and editing features, updated labeling for better clarity, and enhanced UI elements to handle edge cases. The team also resolved critical bugs affecting the Kitchen filter button and history title display, while updating the Transactions and Holders tables in Token Details for better data presentation.

## Action Items

- [ ] **Deploy Jupiter Swap API to production** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Monitor fallback aggregator performance** - Assigned to: Backend Team - Due: Ongoing - Priority: High
- [ ] **Complete Jupiter supported tokens implementation** - Assigned to: Indexer Team - Due: Next sprint - Priority: Medium
- [ ] **Roll out updated Wallet Manager to production** - Assigned to: Frontend Team - Due: Next week - Priority: Medium

## Index

1. Backend Integration and Performance
2. Indexer Infrastructure Improvements
3. Frontend Wallet Manager Enhancements
4. UI Bug Fixes and Improvements

---

## Topics: Breakdown

### Topic 1: Backend Integration and Performance

#### Executive Summary
Backend team completed critical integration testing and implemented strategic fallback mechanisms while continuing performance optimization efforts.

#### Key Takeaways
- Completed testing of Jupiter Swap API integration
- Migrated userTrades queries resulting in better performance
- Added MarketCap to transactions list in Token Details
- Implemented fallback strategy for swap aggregators (Jupiter → HelloMoon → Cooking)
- Successfully tested wallet naming and editing functionality

#### Discussion Details
The fallback strategy implementation is particularly important for platform reliability. The priority order ensures that if Jupiter (primary) fails, the system automatically falls back to HelloMoon, and then to Cooking's internal solution if needed. This three-tier approach guarantees trading continuity.

---

### Topic 2: Indexer Infrastructure Improvements

#### Executive Summary
Indexer team delivered significant performance improvements through Redis implementation and database optimization while advancing Jupiter integration.

#### Key Takeaways
- Implemented Redis for JSON block storage
- Achieved significant performance improvement in data handling
- Removed old tables reducing indexer size
- Continued development on Jupiter supported tokens

#### Discussion Details
The Redis implementation represents a major architectural improvement, moving from direct database storage to a high-performance caching layer for JSON blocks. This change significantly reduces database load and improves response times for data-intensive operations.

---

### Topic 3: Frontend Wallet Manager Enhancements

#### Executive Summary
Frontend team completed comprehensive improvements to the Wallet Manager, delivering full naming functionality and improving user interface consistency.

#### Key Takeaways
- Completed implementation of wallet naming functionality
- Completed implementation of wallet name editing
- Updated 'Export PK' label to 'Export Seed Phrase' for clarity
- Enhanced Primary wallet UI to handle edge cases
- Removed Security Password requirement for wallet name changes

#### Discussion Details
The decision to remove Security Password requirements for name changes improves user experience for this low-risk operation while maintaining security for sensitive actions like exports and transfers.

---

### Topic 4: UI Bug Fixes and Improvements

#### Executive Summary
Frontend team resolved multiple user interface bugs and updated critical data tables for better information presentation.

#### Key Takeaways
- Fixed bug where 'Filter' button disappears when active in Kitchen
- Fixed bug where 'History' title becomes scrollable and disappears
- Fixed wallet overflow issue with scrollbar
- Updated Transactions table in Token Details
- Updated Holders table in Token Details

---

## Decisions Made

1. **Implement three-tier swap aggregator fallback** - Ensure trading continuity with Jupiter → HelloMoon → Cooking
2. **Remove password for wallet renaming** - Improve UX for non-sensitive operations
3. **Adopt Redis for block storage** - Enhance performance for data-intensive operations

## Blockers and Risks Identified

None reported this week.

## Parking Lot

- Long-term Redis cluster scaling strategy
- Additional swap aggregator integrations
- Wallet Manager mobile optimization

## Next Steps

- Deploy Jupiter Swap API to production
- Monitor aggregator fallback mechanism performance
- Complete remaining Jupiter token support features
- Gather user feedback on Wallet Manager improvements

## References

- Jupiter Swap API documentation
- Redis implementation architecture
- Swap aggregator fallback testing results