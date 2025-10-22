---
type: meeting-note
title: "Daily Standup - July 16, 2025"
meeting_type: "Daily Standup"
date: 2025-07-16
attendees: ["Eduardo Yuschuk", "Ramiro Carracedo", "Santiago Gimenez", "Luis Rivera", "Florencia Redondo", "Lucas Cufré", "Martin Aranda", "Mauricio Hernán Cabrera", "Marko Jauregui", "Federico Caffaro", "Angel Rangel"]
duration: "29 minutes"
language: "English (translated from Spanish)"
translation_date: "2025-10-20"
status: "Translated and Structured"
tags: ["daily-standup", "team-sync", "sprint", "july-2025"]
---

# Daily Standup - July 16, 2025

## Meeting Details
- **Date:** July 16, 2025
- **Time:** 08:33 - 09:02 (GMT-3)
- **Duration:** 29 minutes
- **Meeting Type:** Daily Standup
- **Attendees:** Eduardo Yuschuk, Ramiro Carracedo, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Angel Rangel
- **Language:** English (Translated from Spanish)

## Summary
The team provided updates on UI component progress, backend deposit handling improvements with RabbitMQ and server-sent events, challenges with failed Jupiter transactions, and evaluation of on-ramp/off-ramp solutions. Key discussions included Ramper vs Crossmint comparison and indexer updates for data migration.

## Team Updates

### Luis Rivera
**Completed:**
- Connected convert popover components
- Completed Search Perpetuals Popover UI
- Added skeletons to components for better loading UX

**In Progress:**
- Fixing component heights and display issues
- Table item component (70% complete)
- Orders and trades panel

**Notes:**
- Perpetuals view looks bad starting at 1180 pixels
- Proposed warning screen for mobile functionality

### Mauricio Hernán Cabrera
**Completed:**
- Form control component
- Mini refactoring of other components for adaptation
- Added currency input component
- Added deprecation comments to all UI components

**In Progress:**
- Reorganizing B2 components (moving UI to separate folder)
- SSE mocking issues
- Buffer error in modal history component

**Blockers:**
- SSE mocking not working with ChatGPT attempts

### Marko Jauregui
**Completed:**
- Progress on Turnkey implementation

**In Progress:**
- Social login with Google implementation
- Martin's corrections review
- Unit tests and integration tests

**Notes:**
- No integration test framework available yet

### Federico Caffaro
**Completed:**
- Added RabbitMQ queue to prevent deposit loss
- Implemented server-sent events for frontend
- Stress tested with 1000 simultaneous deposits (10 minutes processing)

**In Progress:**
- Idempotency key implementation
- Dead letter queue handling for performance

**Notes:**
- Bottleneck identified in cron processing (one by one)

### Ramiro Carracedo
**Completed:**
- Created all tables for migration
- Sent PR with table definition to indexer

**In Progress:**
- Query efficiency optimization
- Migration script for minimal data from Postgres
- Testing and finalization

**Notes:**
- Parallel data sending now possible

### Eduardo Yuschuk
**Completed:**
- Analysis of failed Jupiter transactions

**In Progress:**
- Adding missing data to ClickHouse events
- Metaplex indexing for metadata extraction

**Issues:**
- Failed Jupiter transactions lack source token information
- SDK fails with failed transactions

### Lucas Cufré
**Key Points:**
- Reviewing OnRamper and Crossmint as ramp solutions
- Preparing comparison document for technical review
- Recommends Ramper for robustness and transparency
- Clients prefer Crossmint due to no-KYC swap capability
- Crossmint lacks off-ramp functionality currently

### Angel Rangel
**Completed:**
- Telegram authentication screen
- Terms and conditions screen
- Some home screen components

**In Progress:**
- Remaining home screen components
- Security keychain implementation

**Notes:**
- Working on refresh token handling

### Santiago Gimenez
**Completed:**
- Figma review for pending items
- Meeting with Lucky about next phases

**In Progress:**
- Settings configuration
- Login systems
- Component updates in design system

**Notes:**
- Need to update transaction history examples

## Key Discussion Points

### UI Component Migration
- Martin emphasized B2 components should use new design
- Migration complicated due to multiple UI versions
- Need thread in Slack for missing components tracking

### Deposit Handling Improvements
- RabbitMQ implementation prevents deposit loss
- Server-sent events eliminate need for frontend polling
- Stress test revealed bottleneck in sequential cron processing

### Failed Transaction Handling
- Jupiter failed transactions missing critical information
- Difficult to show complete history without source token data
- May need to link to block explorer for details

### OnRamp/OffRamp Solutions
- Ramper: More robust, better documentation, transparent pricing
- Crossmint: Client preference, no-KYC swap, but lacks off-ramp
- Need enterprise plan pricing from Crossmint
- Compliance and geographic restrictions unclear

### Bank Fan Implementation
- Client insistence increasing for Let's Bank Fan support
- Eduardo to investigate provider implementation
- Direct backend implementation preferred over Jupiter-only

## Action Items
- [ ] Create Slack thread for missing components - @Team
- [ ] Send comparison document for ramp solutions - @Lucas
- [ ] Implement idempotency key for deposits - @Federico
- [ ] Investigate Bank Fan provider - @Eduardo
- [ ] Update transaction history examples in Wallet Manager - @Santiago
- [ ] Fix SSE mocking issues - @Mauricio

## Notes
- GitHub integrations currently down affecting lint checks and merge blocks
- Mobile compatibility issues need strategic decision
- Metaplex indexing enables metadata extraction for all tokens
- Performance optimizations needed for slow queries

---
*Meeting notes generated by Gemini AI and translated to English*
*Original meeting date: July 16, 2025*
*Translation completed: 2025-10-20*