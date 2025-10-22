---
title: Weekly Demo - May 23, 2025
type: meeting-note
date: 2025-05-23
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, jupiter-integration]
summary: |
  Weekly development progress review showcasing completion of Jupiter Swap API integration, resolution of filtering errors, performance improvements for Wallets and Referrals, and significant query optimizations across trading features. Frontend team standardized date/time formats, improved error messaging, and completed the token stream pause feature. Indexer resolved critical h2 protocol errors and continued enhancing launchpad support.
related-docs:
  - [Jupiter Swap API Integration Documentation]
---

# Weekly Demo - May 23, 2025

**Date:** 2025-05-23
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week marked significant progress in platform stability and performance improvements across all components. The backend team successfully completed the finishing touches on the Jupiter Swap API integration, a critical component for trading functionality. They also resolved filtering errors that were impacting user experience and implemented a solution for sending full wallet balances in transactions, addressing a common user pain point.

Performance optimization was a key focus, with improvements delivered for Wallets and Referrals modules, along with the implementation of a 'Recent Search' feature to enhance user experience. The team continued their systematic improvement of query performance for all major trading features including Specials, Limit Orders, DCA, TWAP, and VWAP operations.

The indexer team successfully resolved a critical h2 protocol error that was affecting connection reliability and continued enhancing support for emerging platforms with improvements to pump.fun and moonshot minting capabilities, bonding curves, and Raydium AMM functionality. Frontend development focused on user experience improvements including the successful implementation of the token stream pause feature, fixing Referral Program reward displays, standardizing date/time formats across the platform, and improving error message communication in the wallet manager.

## Action Items

- [ ] **Deploy and monitor Jupiter Swap API in production** - Assigned to: Backend Team - Due: Next sprint - Priority: High
- [ ] **Validate performance improvements in production** - Assigned to: Backend Team - Due: Next week - Priority: High
- [ ] **Complete testing of indexer improvements** - Assigned to: Indexer Team - Due: Next sprint - Priority: Medium
- [ ] **Roll out standardized date/time format to all screens** - Assigned to: Frontend Team - Due: Next sprint - Priority: Low

## Index

1. Backend Development Progress
2. Indexer Improvements
3. Frontend Updates
4. Performance Optimizations

---

## Topics: Breakdown

### Topic 1: Backend Development Progress

#### Executive Summary
Backend team completed Jupiter Swap API integration, resolved critical filtering errors, and implemented significant performance improvements across multiple modules while adding new user-requested features.

#### Key Takeaways
- Jupiter Swap API integration finalized with finishing touches
- Fixed errors occurring during filtering operations
- Resolved issue with sending full wallet balance in transactions
- Implemented 'Recent Search' feature for improved user experience
- Delivered performance improvements for Wallets module
- Delivered performance improvements for Referrals module
- Continued query optimization for Specials
- Continued query optimization for Limit Orders
- Continued query optimization for DCA operations
- Continued query optimization for TWAP operations
- Continued query optimization for VWAP operations
- Continued query optimization for Wallet operations

---

### Topic 2: Indexer Improvements

#### Executive Summary
Indexer team resolved a critical protocol error and continued enhancing platform support for various launchpads and AMMs, improving overall system reliability.

#### Key Takeaways
- Fixed h2 protocol error when reading body from connection
- Enhanced mint support for pump.fun platform
- Enhanced mint support for moonshot platform
- Improved bonding curves implementation for pump.fun
- Improved bonding curves implementation for moonshot
- Enhanced AMM functionality for Raydium

#### Discussion Details
The h2 protocol error was a critical issue affecting connection stability and data retrieval. Its resolution significantly improves the reliability of the indexer service.

---

### Topic 3: Frontend Updates

#### Executive Summary
Frontend team successfully delivered multiple user experience improvements including the completion of the token stream pause feature, fixing reward display issues, and standardizing the platform's date/time formatting.

#### Key Takeaways
- Successfully implemented pause token stream on hover in Kitchen
- Fixed total rewards display issue in Referral Program
- Added success toast notification for Referral Program reward retrieval
- Resolved filtering errors affecting user experience
- Improved error message communication in wallet manager
- Enhanced sorting functionality for PnL % column in Custom Orders/Positions
- Normalized date and time format across entire product

---

### Topic 4: Performance Optimizations

#### Executive Summary
Significant performance improvements were delivered across multiple platform components, focusing on query optimization and user experience enhancements.

#### Key Takeaways
- Wallet operations now perform significantly faster
- Referral Program module shows improved response times
- Query optimizations continue across all trading features
- Recent Search feature reduces repeated lookup times

---

## Decisions Made

1. **Standardize date/time format platform-wide** - Improve consistency and user experience
2. **Prioritize Jupiter Swap API deployment** - Critical for trading functionality

## Blockers and Risks Identified

None reported this week - previous AWS deployment issues appear to be resolved.

## Parking Lot

- Long-term performance monitoring strategy
- Additional launchpad integrations to consider

## Next Steps

- Monitor Jupiter Swap API performance in production
- Continue query optimization efforts
- Complete testing of all indexer improvements
- Roll out remaining frontend improvements

## References

- Jupiter Swap API documentation
- Performance improvement metrics dashboard