---
title: Weekly Demo - June 13, 2025
type: meeting-note
date: 2025-06-13
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, performance, jupiter-integration, database-migration]
summary: |
  Weekly development progress review showcasing significant performance improvements through query migrations, database architecture updates, and bug fixes. Key achievements include fixing VWAP order loading issues, migrating critical queries for improved performance, beginning Jupiter token support design, and identifying need for data warehouse migration due to stress testing results. Frontend improvements focused on UI consistency and bug fixes across multiple components.
related-docs:
  - [Jupiter Token Support Design]
  - [Database Migration Strategy]
  - [Performance Optimization Metrics]
---

# Weekly Demo - June 13, 2025

**Date:** 2025-06-13
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week marked significant progress in platform optimization and stability improvements across all components. The backend team successfully resolved a critical bug affecting VWAP order loading and implemented a user experience enhancement by remembering the last selected primary wallet across login sessions. Query migration efforts accelerated with successful migrations of Specials, Cover, and Token Data queries, directly impacting loading times and overall platform performance. The team also initiated high-level technical design work for Jupiter token support, a key integration for expanding trading capabilities.

The indexer team achieved major architectural improvements by migrating Positions, Token Details, and Bars tables to the new architecture, resulting in better performance and reduced AWS resource consumption. Stress testing revealed important insights about database scalability, identifying the need for certain heavy-usage tables to migrate to a data warehouse solution. Progress continued on Jupiter transaction support with partial implementation completed.

Frontend development addressed multiple user interface issues including counter overflow in Kitchen cards, label improvements in filters, standardization of numerical input formats to use decimal commas, and various bug fixes in Custom Orders and wallet management features. The team also implemented wallet name editing functionality and improved labeling consistency across the platform.

## Action Items

- [ ] **Plan data warehouse migration for heavy-usage tables** - Assigned to: Backend/Indexer Teams - Due: Next sprint - Priority: High
- [ ] **Complete Jupiter token support implementation** - Assigned to: Backend/Indexer Teams - Due: Next 2 weeks - Priority: High
- [ ] **Finalize and test wallet name editing feature** - Assigned to: Frontend Team - Due: Next week - Priority: Medium
- [ ] **Address remaining partial Jupiter transaction support** - Assigned to: Indexer Team - Due: Next sprint - Priority: High

## Index

1. Backend Performance and Features
2. Indexer Architecture Improvements
3. Frontend UI/UX Enhancements
4. Database Scalability Findings

---

## Topics: Breakdown

### Topic 1: Backend Performance and Features

#### Executive Summary
Backend team delivered critical bug fixes, user experience improvements, and significant performance optimizations through query migrations while beginning design work for Jupiter integration.

#### Key Takeaways
- Fixed critical bug where VWAP orders failed to load
- Implemented primary wallet persistence across login sessions
- Migrated Specials queries for improved performance
- Migrated Cover queries for improved performance
- Migrated Token Data queries for improved performance
- Initiated high-level technical design for Jupiter token support

#### Discussion Details
The query migrations have shown measurable improvements in loading times and overall platform responsiveness. The primary wallet persistence feature addresses a common user complaint about having to reselect their wallet after each login.

---

### Topic 2: Indexer Architecture Improvements

#### Executive Summary
Indexer team completed major table migrations to new architecture and identified critical scalability requirements through comprehensive stress testing.

#### Key Takeaways
- Migrated Positions table to new architecture
- Migrated Token Details table to new architecture
- Migrated Bars table to new architecture (affects charts and last traded prices)
- Improved overall performance and reduced AWS resource consumption
- Initiated high-level technical design for Jupiter token support
- Achieved partial implementation of Jupiter transaction indexing
- Stress testing revealed need for data warehouse migration for heavy-usage tables

#### Discussion Details
The stress testing results are particularly significant, revealing that certain tables with heavy usage patterns require migration to a data warehouse architecture to maintain performance at scale. This finding will drive infrastructure decisions in the coming sprints.

---

### Topic 3: Frontend UI/UX Enhancements

#### Executive Summary
Frontend team focused on improving consistency, fixing bugs, and enhancing user experience across multiple platform components.

#### Key Takeaways
- Fixed counter display bugs in Kitchen cards (incorrect values and overflow)
- Updated filter labels from 'Hide Pump.Fun/Moonshot' to 'Hide Pump.Swap/Raydium'
- Standardized numerical input format to decimal comma (100,000.00)
- Fixed Custom Orders search input requiring 2 clicks for focus
- Fixed bug allowing NULL value for Limit Price in Custom Orders
- Standardized date format in DCA table for consistency
- Fixed data persistence in 'Add Withdraw Wallet' modal
- Implemented wallet name editing functionality
- Simplified 'Transfer' modal label from 'Sign and Transfer' to 'Transfer'

#### Discussion Details
The numerical format standardization (100,000.00) improves readability for large numbers, a critical feature for a trading platform. The various bug fixes address pain points that were affecting daily user workflows.

---

### Topic 4: Database Scalability Findings

#### Executive Summary
Comprehensive stress testing revealed critical insights about platform scalability, identifying specific tables requiring architectural changes to support growth.

#### Key Takeaways
- Stress testing completed on current database architecture
- Heavy-usage tables identified for migration
- Data warehouse solution recommended for specific workloads
- Migration planning initiated for affected tables

---

## Decisions Made

1. **Standardize numerical format** - Use decimal comma format (100,000.00) across platform
2. **Migrate heavy-usage tables** - Move to data warehouse architecture based on stress test results
3. **Prioritize Jupiter integration** - Begin technical implementation following design completion

## Blockers and Risks Identified

- **Database scalability limits** - Impact: High - Owner: Infrastructure Team - Needs resolution by: Before scaling

## Parking Lot

- Long-term data warehouse architecture design
- Complete Jupiter token listing strategy
- Performance monitoring dashboard implementation

## Next Steps

- Complete data warehouse migration planning
- Finish Jupiter token support implementation
- Continue stress testing and performance optimization
- Deploy and test wallet editing features

## References

- Stress testing results documentation
- Jupiter integration technical specification
- Database migration architecture proposal