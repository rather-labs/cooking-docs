---
type: meeting-note
title: "Daily Standup - July 18, 2025"
meeting_type: "Daily Standup"
date: 2025-07-18
attendees: ["Eduardo Yuschuk", "Ramiro Carracedo", "Santiago Gimenez", "Luis Rivera", "Florencia Redondo", "Lucas Cufré", "Martin Aranda", "Mauricio Hernán Cabrera", "Marko Jauregui", "Federico Caffaro", "Angel Rangel"]
duration: "15 minutes"
language: "English (translated from Spanish)"
translation_date: "2025-10-20"
status: "Translated and Structured"
tags: ["daily-standup", "team-sync", "sprint", "july-2025"]
---

# Daily Standup - July 18, 2025

## Meeting Details
- **Date:** July 18, 2025
- **Time:** 09:16 - 09:31 (GMT-3)
- **Duration:** 15 minutes
- **Meeting Type:** Daily Standup
- **Attendees:** Eduardo Yuschuk, Ramiro Carracedo, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Angel Rangel
- **Language:** English (Translated from Spanish)

## Summary
The team discussed frontend and backend updates, including UI component fixes, Perpetual implementation progress, data migration completion, and Metaplex indexing for token metadata extraction.

## Team Updates

### Mauricio Hernán Cabrera
**Completed:**
- Fixed visual errors on the site
- Adapted inputs for form controls
- Moved old UI components to B2 folder
- Enabled cancel button on toast without hover

**In Progress:**
- Form control component refinements
- Reviewing Claude suggestions
- Improving folder structure for B2 components

**Notes:**
- Site had broken colors and styling issues (fixed)
- Working on better organization of UI components

### Luis Rivera
**Completed:**
- Perpetual Swap height solution
- Added skeletons to components for loading states
- Integrated conversion functionality
- Balance reading in wallet popover and conversion section

**In Progress:**
- Perpetual Book panel with orders and trades tabs
- Testing deposit functionality

**Questions:**
- Should perpetual fee affect "total to receive" field in conversion modal?

### Marko Jauregui
**Completed:**
- Turnkey implementation finished
- Unit tests completed

**In Progress:**
- Social login continuation
- TR proxy integration
- Frontend implementation study

**Blockers:**
- None mentioned

### Federico Caffaro
**Completed:**
- Live candles update implementation
- Websocket connections for perpetuals data

**In Progress:**
- Evaluating initial candles delivery method
- Optimizing streaming vs endpoint approach

**Notes:**
- Considering streaming or direct endpoint fetch for initial data

### Ramiro Carracedo
**Completed:**
- Backend cleanup of Postgres database dependencies
- Migration nearly complete
- Liquidity and transaction functions working

**In Progress:**
- Diamond Hands decoupling exploration
- PR preparation for replica removal

**Notes:**
- Diamond Hands is only thing coupling sequential block processing

### Eduardo Yuschuk
**Completed:**
- Metaplex indexing for metadata extraction
- Mints data sending functionality

**In Progress:**
- ClickHouse data updates discussion with Ramiro
- Let's Bank mint function assistance
- Fixing decimal-related errors

**Notes:**
- Metaplex indexing allows metadata extraction for any token regardless of protocol

### Angel Rangel
**Completed:**
- iOS 15 compatibility changes
- Home UI components
- Security keychain logic for tokens

**In Progress:**
- Home screen UI construction
- Access and refresh token storage

**Issues:**
- Navigation coordinator incompatible with iOS 15
- Minimum iOS 16 required for navigation features

### Santiago Gimenez
**Completed:**
- Settings exploration
- Components list updates

**In Progress:**
- Component reviews and adjustments
- Coordination with Lucky on next steps

**Notes:**
- Updating based on team needs

### Lucas Cufré
**Key Points:**
- Referral B2 issue resolved
- Many meetings reducing work output
- External designer progressing on Wallet Manager
- Plans to guide Santiago on library ownership
- Need to update task statuses for client report

### Martin Aranda
**Notes:**
- Reminded team about mandatory one-on-one meetings
- Deadline at noon for feedback call

## Key Discussion Points

### iOS Version Compatibility
- iOS 15 navigation incompatibility discovered
- Team decided to increase minimum version to iOS 16
- Only affects ~10% of market (iPhone 7/8 users)
- Deprecation justified for better navigation architecture

### Form Control and Error Handling
- Generic form control implementation like MUI
- External state management in parent component
- Supports disabled state, errors, and hints

### Task Status Updates
- Lucas requested all team members update task statuses
- Needed for client status report
- Move tasks to testing/done as appropriate

### Diamond Hands Optimization
- Last remaining coupling for sequential processing
- Ramiro exploring ways to decouple next week
- Would simplify indexer significantly

## Action Items
- [ ] Update all task statuses in project management - @Everyone
- [ ] Complete one-on-one meetings by noon - @Everyone
- [ ] Assist with Let's Bank mint function - @Eduardo
- [ ] Explore Diamond Hands decoupling - @Ramiro
- [ ] Guide Santiago on library ownership - @Lucas

## Notes
- Short meeting with focused updates
- iOS minimum version change will be communicated to client
- Metaplex indexing provides comprehensive metadata solution
- Team preparing for client status report

---
*Meeting notes generated by Gemini AI and translated to English*
*Original meeting date: July 18, 2025*
*Translation completed: 2025-10-20*