---
title: Daily Standup - October 24, 2025
type: meeting-notes
date: 2025-10-24
meeting-type: daily-standup
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Eduardo Yuschuk
  - Byron Chavarria
  - Javier Grajales
  - Esteban Restrepo
  - Federico Caffaro
  - Marko Jauregui
  - German Derbes Catoni
  - Luis Rivera
  - Santiago Gimenez
  - Dario Balmaceda
  - Marcos Tacca
  - Florencia Redondo
  - Martin Lecam
  - Luciano Copado
status: completed
summary: Daily standup covering Designer's Day celebration, advance orders testing, SPL Token 2022 integration, blockchain indexer implementation, UI improvements, perpetuals trading features, and error message standardization discussion.
tags:
  - daily-standup
  - advance-orders
  - spl-token-2022
  - blockchain-indexer
  - perpetuals
  - error-handling
  - mobile-ios
  - ui-improvements
related_documents:
  - 03-active-work/_current-status.md
  - 04-knowledge-base/business/requirements/hyperliquid-perpetuals-integration.md
  - 04-knowledge-base/technical/backend-error-handling-guide.md
---

# Daily Standup - October 24, 2025

**Meeting Type:** Daily Standup
**Date:** October 24, 2025
**Duration:** ~45 minutes
**Facilitator:** Martin Aranda

## Key Highlights

🎉 **Designer's Day Celebration** - Team celebrated Designer's Day
🔧 **SPL Token 2022 Support** - Integration completed for new token standard
🚀 **Perpetuals Trading** - Multiple features implemented (USDC values, Open Interest, ROE calculations)
🐛 **Error Standardization** - Discussion about creating unified error message system
📱 **iOS Modal Limitations** - Identified iOS 16/Swift 5 compatibility issues with sheet overlays

---

## Attendance

**Present (16):**
- Lucas Cufré (Project Lead)
- Martin Aranda (Tech Lead)
- Eduardo Yuschuk (Backend/Indexer Lead)
- Byron Chavarria (Mobile Lead)
- Javier Grajales (QA)
- Esteban Restrepo (Backend Developer)
- Federico Caffaro (Backend Developer)
- Marko Jauregui (Frontend Developer)
- German Derbes Catoni (Frontend Developer)
- Luis Rivera (Frontend Developer)
- Santiago Gimenez (Developer)
- Dario Balmaceda
- Marcos Tacca
- Florencia Redondo
- Martin Lecam
- Luciano Copado

---

## Individual Updates

### Javier Grajales (QA)

**Completed:**
- Configured "top percentage holder" feature for advance orders
- Configured "auto priority fee" for future order execution
- Created threads for various design topics
- Deep dive into order testing
- Identified missing frontend data: average percentage time holding
- Organizing order regression testing

**In Progress:**
- Reviewing Advance Orders tables
- Finalizing regression test cases list

**Next Steps:**
- Polish format and decide display location for regression test cases (with Lucas)
- Continue testing advance orders with different states

**Notes:**
- Tables without history show only active or paused orders
- Historical view shows different columns (e.g., order size in TWAP unknown until execution)
- Historical = transactions tracking, Non-historical = orders tracking

---

### Byron Chavarria (Mobile - iOS)

**Completed:**
- Integrated access token handling via cookies (PR submitted)

**In Progress:**
- Working on limit orders creation and sell functionality
- Dealing with iOS modal overlay limitations

**Blockers:**
- iOS 16 + Swift 5 doesn't support sheet-over-sheet (modal on modal)
- Newer iOS versions support it, but maintaining backward compatibility
- Need alternative solution: hide and show modals sequentially

**Technical Context:**
- Issue is retrocompatibility with iOS 16 and Swift 5
- Newer Swift versions support "sheet over sheet" natively

---

### Eduardo Yuschuk (Backend/Indexer Lead)

**Completed:**
- Integrated SPL Token 2022 standard support
- Supported in Raydium Launchpad for pool creation
- Working on fixing initial amounts in order creation to prevent mismatches

**In Progress:**
- Investigating "timestamp zero" issue in trade logs
- Proposed solution: Add traceability column in PostgreSQL to identify malformed block sources

**Technical Details - Blockchain Data Collection:**
- Uses two concurrent implementations:
  1. **WebSockets** - Real-time blockchain data
  2. **Geyser protocol** - Alternative data source
- Both try to insert next block into PostgreSQL table (only one succeeds due to unique constraint)
- Indexer polls PostgreSQL to process the data

**Architecture:**
```
Blockchain → WebSockets ↘
                          → PostgreSQL (unique block constraint) → Indexer (polling)
Blockchain → Geyser    ↗
```

---

### Esteban Restrepo (Backend Developer)

**Completed:**
- Worked on "Your Orders" section within "Token Details"
- Enabled CORS for transaction microservices
- Adjusted priority fee for automated trading algorithms

**In Progress:**
- Understanding "conditions" card for custom orders

**Questions Resolved:**
- Conditions refer to JSON field within limit orders (explained by Martin)

**Next Steps:**
- Test with balance and upload all order fixes

---

### Federico Caffaro (Backend Developer)

**Completed:**
- Approved Transactionator PR
- Fixed "top 10 holders" issue

**Next Steps:**
- Decide where to place/deploy the Transactionator

---

### Marko Jauregui (Frontend Developer)

**Completed:**
- Multiple ticket fixes:
  - Improved wallet manager
  - Added Solscan links to transaction receipts
  - Hide tokens with zero liquidity

**Next Steps:**
- Review withdraw and transfer modals to pre-select active wallet by default

---

### German Derbes Catoni (Frontend Developer)

**Completed:**
- Updated portfolio with skeleton loaders
- Fixed token images display
- Fixed "Not Found" page
- Standardized number formatting across app

**In Progress:**
- Continuing number formatting fixes across different screens

**Next Steps:**
- Fix remaining number formatting issues throughout the application

---

### Luis Rivera (Frontend Developer)

**Completed - Perpetuals Trading Features:**
- Implemented USDC value display
- Implemented Open Interest calculation
- Implemented ROE (Return on Equity) calculation for PNL
- Working on various perpetuals-related tickets

**Questions Resolved:**
- **Available Balance in Perpetuals:**
  - PNL (Profit and Loss) should NOT affect available balance
  - Whether PNL is positive or negative, it doesn't change available balance
  - Margin is paid specifically for this purpose

**Next Steps:**
- Continue working on pending tickets
- Remove addition/subtraction from available balance in Perpetuals

---

### Santiago Gimenez (Developer)

**Assigned:**
- Review Hyperliquid pattern for editing take profit and stop loss in transactions

---

## Key Discussions

### 1. Advance Orders Table Display

**Context:** Understanding what to show in historical vs. non-historical views

**Decisions:**
- Non-historical tables show only active or paused orders
- Historical tables may show additional columns
- Example: TWAP order size is unknown until execution time
- Historical = transactions, Non-historical = orders (different entities)

---

### 2. iOS Modal Limitations

**Problem:** iOS 16 + Swift 5 doesn't support sheet-over-sheet (modal on modal)

**Impact:** Affects limit order creation/sell flows on mobile

**Solution:**
- Use alternative approach: hide and show modals sequentially
- Maintain backward compatibility with iOS 16

**Technical Note:** Newer iOS versions support this natively, but can't drop iOS 16 support yet

---

### 3. Blockchain Indexer Architecture

**Question:** How does the indexer collect blockchain data?

**Answer (Eduardo):**
- Two concurrent implementations: WebSockets + Geyser protocol
- Both attempt to insert next block into PostgreSQL
- Table has unique constraint - only one insertion succeeds
- Indexer polls PostgreSQL to process blocks
- Martin clarified the polling mechanism

---

### 4. Perpetuals Available Balance Calculation

**Question:** Should PNL affect available balance in Perpetuals?

**Answer (Lucas):**
- NO - PNL should not affect available balance
- Applies whether PNL is positive or negative
- Margin is paid specifically to cover this
- Available balance remains constant regardless of unrealized PNL

**Action:** Luis to remove PNL addition/subtraction from available balance

---

### 5. Perpetuals Take Profit / Stop Loss Editing

**Requirement:** Need ability to edit TP/SL on open positions

**Current State:** Cannot edit TP/SL after position is created

**Action:** Santiago to review Hyperliquid's pattern for implementing this feature

---

### 6. Error Message Standardization

**Problem:** Inconsistent error messages between backend and frontend

**Discussion (Martin & Lucas):**
- Need to standardize error messages across the platform
- Suggestion: Create error dictionary system for backend and frontend
- Should assign someone to lead this initiative
- Related to recently completed error documentation work

**Note:** This aligns with the Backend Error Handling Guide created earlier this week

---

## Action Items

### High Priority

- [ ] **Javier Grajales:** Finalize regression test cases format and display location (collaborate with Lucas)
- [ ] **German Derbes Catoni:** Fix number formatting issues across all screens
- [ ] **Luis Rivera:** Remove PNL addition/subtraction from Perpetuals available balance
- [ ] **Santiago Gimenez:** Research Hyperliquid's TP/SL editing pattern

### Medium Priority

- [ ] **Esteban Restrepo:** Test order fixes with balance and upload changes
- [ ] **Federico Caffaro:** Decide Transactionator deployment location
- [ ] **Marko Jauregui:** Update withdraw/transfer modals to pre-select active wallet
- [ ] **Byron Chavarria:** Implement iOS modal workaround for sheet-over-sheet limitation

### Future Discussion

- [ ] **Team:** Assign owner for error message standardization initiative
- [ ] **Team:** Create error dictionary system for backend/frontend

---

## Technical Notes

### SPL Token 2022 Integration

- New token standard now supported
- Already working in Raydium Launchpad
- Allows handling of new token types with extended features

### Blockchain Indexer Design Pattern

**Dual-Source Architecture:**
```
WebSockets + Geyser → PostgreSQL (unique constraint) → Indexer (polling)
```

**Benefits:**
- Redundancy: Two data sources
- Consistency: Unique constraint prevents duplicates
- Reliability: If one source fails, other continues

### iOS Compatibility Constraint

**Issue:** Sheet-over-sheet not supported in iOS 16 + Swift 5
**Workaround:** Sequential modal display (hide/show)
**Long-term:** Will be resolved when iOS 16 support is dropped

---

## Decisions Made

1. ✅ **Perpetuals PNL Calculation:** PNL does not affect available balance (positive or negative)
2. ✅ **Historical vs Non-Historical Tables:** Different entities - transactions vs orders
3. ✅ **iOS Modal Strategy:** Use sequential display workaround for backward compatibility

---

## Client Feedback

**Positive Note (Lucas):** Client is requesting many small frontend adjustments, which indicates the team is doing good work and the platform is being actively used and tested.

---

## Follow-up Required

### Error Standardization Initiative
- Needs owner assignment
- Should create comprehensive error dictionary
- Frontend and backend alignment needed
- Reference: Backend Error Handling Guide (recently created)

### Perpetuals Feature Enhancement
- Need TP/SL editing capability
- Research Hyperliquid implementation
- Design and implement solution

### Number Formatting Consistency
- Multiple screens need fixes
- German working through them systematically
- Should be completed soon

---

## Meeting Notes

- Meeting started with Designer's Day celebration
- Productive discussion about various technical topics
- Good cross-team collaboration (backend, frontend, mobile, QA)
- Several technical clarifications provided by leads
- Multiple action items identified and assigned

---

**Next Daily Standup:** October 25, 2025 (Friday)
**Meeting Duration:** Approximately 45 minutes
**Notes Captured By:** Gemini AI Meeting Notes
**Processed By:** Claude Code Documentation System
