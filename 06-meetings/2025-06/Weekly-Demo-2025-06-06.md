---
title: Weekly Demo - June 6, 2025
type: meeting-note
date: 2025-06-06
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, security, wallet-manager]
summary: |
  Weekly development progress review focusing on security enhancements and query migrations. Major accomplishments include implementation of secure password storage and verification for wallet operations, migration of critical queries for improved performance, and UI updates for the Wallet Manager. The indexer team added important attributes for tracking AMM migrations and developer/authority status.
related-docs:
  - [Wallet Manager Security Implementation]
  - [Query Migration Strategy]
---

# Weekly Demo - June 6, 2025

**Date:** 2025-06-06
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week's development efforts centered on strengthening security measures and optimizing platform performance through systematic query migrations. The backend team successfully implemented comprehensive security password functionality for the Wallet Manager, including secure storage, verification processes for sensitive operations, and a streamlined update mechanism. A significant improvement was made to user experience by removing password requirements for intra-Cooking wallet transfers, reducing friction for routine operations.

Query migration efforts continued with successful migrations of Limit Orders and Custom Orders queries, contributing to overall platform performance improvements. The indexer team resolved critical bugs related to blockchain transaction lookups and enhanced data tracking capabilities by adding attributes for AMM migration status and identifying developers and authorities in the Holders table.

Frontend development completed the security password implementation across all wallet operations, including creation, seed phrase export, and SOL withdrawals. The team also addressed UI improvements including alphabetical sorting for wallet selection and design updates for the Primary Wallet interface.

## Action Items

- [ ] **Test Update Security Password flow** - Assigned to: Frontend Team - Due: Next sprint - Priority: High
- [ ] **Complete remaining query migrations** - Assigned to: Backend Team - Due: Next sprint - Priority: Medium
- [ ] **Validate security password implementation in production** - Assigned to: QA Team - Due: Next week - Priority: High

## Index

1. Backend Security Implementation
2. Query Migration Progress
3. Indexer Improvements
4. Frontend Security and UI Updates

---

## Topics: Breakdown

### Topic 1: Backend Security Implementation

#### Executive Summary
Backend team delivered comprehensive security password functionality for wallet operations, balancing security needs with user experience by removing requirements for internal transfers.

#### Key Takeaways
- Implemented secure storage system for passwords
- Added password verification for adding/removing Withdraw Wallets
- Added password verification for exporting Seed Phrases
- Added password verification for withdrawing SOL
- Implemented Update Security Password process
- Removed password requirement for intra-Cooking wallet transfers to improve UX

#### Discussion Details
The team made a strategic decision to remove password verification for transfers between Cooking wallets, recognizing that these internal operations pose minimal security risk while the removal significantly improves user experience and task completion time.

---

### Topic 2: Query Migration Progress

#### Executive Summary
Continued systematic migration of queries to new architecture, improving platform performance and resource utilization.

#### Key Takeaways
- Successfully migrated queries for Limit Orders
- Successfully migrated queries for Custom Orders
- Performance improvements observed post-migration
- Reduced database load and improved response times

---

### Topic 3: Indexer Improvements

#### Executive Summary
Indexer team resolved critical bugs and enhanced data tracking capabilities for better platform intelligence and monitoring.

#### Key Takeaways
- Fixed bug for transactions not found on blockchain
- Added migrated AMM attribute to Mints table for tracking
- Added is_developer flag to Holders table
- Added is_authority flag to Holders table

#### Discussion Details
The addition of developer and authority flags to the Holders table enables better tracking of token ownership patterns and potential risk indicators, providing valuable intelligence for users.

---

### Topic 4: Frontend Security and UI Updates

#### Executive Summary
Frontend team completed comprehensive security password implementation and delivered important UI improvements for the Wallet Manager.

#### Key Takeaways
- Completed Security Password creation flow
- Implemented password checks for adding/removing Withdraw Wallets
- Implemented password checks for exporting Seed Phrases
- Implemented password checks for SOL withdrawals
- Implemented Update Security Password flow (currently in testing)
- Fixed wallet select menu sorting (now alphabetical)
- Updated Primary Wallet design for better user experience

---

## Decisions Made

1. **Remove password for internal transfers** - Improve UX for low-risk operations
2. **Prioritize security for external operations** - Maintain strict verification for withdrawals and exports

## Blockers and Risks Identified

None reported this week.

## Parking Lot

- Long-term password recovery mechanisms
- Two-factor authentication considerations
- Biometric authentication for mobile

## Next Steps

- Complete testing of Update Security Password flow
- Continue query migration efforts
- Monitor security implementation performance
- Gather user feedback on password requirements

## References

- Security implementation documentation
- Query migration performance metrics
- Wallet Manager user guide