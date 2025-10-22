---
type: meeting-note
title: "Daily Standup - July 11, 2025"
meeting_type: "Daily Standup"
date: 2025-07-11
attendees: ["Eduardo Yuschuk", "Ramiro Carracedo", "Santiago Gimenez", "Luis Rivera", "Florencia Redondo", "Lucas Cufré", "Martin Aranda", "Mauricio Hernán Cabrera", "Marko Jauregui", "Federico Caffaro", "Angel Rangel"]
duration: "38 minutes"
language: "English (translated from Spanish)"
translation_date: "2025-10-20"
status: "Translated and Structured"
tags: ["daily-standup", "team-sync", "sprint", "july-2025"]
---

# Daily Standup - July 11, 2025

## Meeting Details
- **Date:** July 11, 2025
- **Time:** 09:26 - 10:04 (GMT-3)
- **Duration:** 38 minutes
- **Meeting Type:** Daily Standup
- **Attendees:** Eduardo Yuschuk, Ramiro Carracedo, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Angel Rangel
- **Language:** English (Translated from Spanish)

## Summary
The team discussed Fireflies.ai Notetaker usage, Claude Pro subscription limits, ClickHouse database optimization, and various technical updates including deposit processes, UI component development, and social login implementation.

## Team Updates

### Lucas Cufré
**Key Points:**
- Cannot use Gemini for transcription in some Cooking meetings
- Using Fireflies.ai Notetaker as alternative
- Claude Pro hit rate limit during work session
- Confirmed Argentina weather forecasts are quite accurate

### Martin Aranda
**Completed:**
- Explained Claude Pro subscription limits (5-hour sessions, 14M tokens in Sonnet)
- Working on transaction management improvements

**In Progress:**
- Backend transaction confirmation optimization

**Notes:**
- Up to 50 sessions per month (~$8 API usage)

### Ramiro Carracedo
**Completed:**
- Optimized ClickHouse database
- Achieved constant complexity queries regardless of table growth
- Platform running smoothly with 150M trades

**In Progress:**
- Migration planning for mints
- Database infrastructure optimization

**Notes:**
- ClickHouse is columnar database designed for big data
- All queries maintaining constant performance

### Federico Caffaro
**Completed:**
- Extended library for Hyper Liquid orders
- Full flow from unit request to perpetuals working
- Implemented three cron jobs for deposit state management

**In Progress:**
- Testing deposit flows
- Handling edge cases (order failures, Unit fees)

**Blockers:**
- None mentioned

### Mauricio Hernán Cabrera
**Completed:**
- Tab Animation component
- Alert, radio button, checkbox, switch components
- Input component work

**In Progress:**
- Toast component development
- Keyboard navigation for forms

**Notes:**
- Issue with close button color visibility in toast component

### Luis Rivera
**Completed:**
- Popover design details
- Perpetuals dashboard top section
- Convert modal design and UI connection

**In Progress:**
- Perpetual contract search component
- Integration with services

**Notes:**
- Wallet Selector hidden on small screens
- Mobile transition for Cooking deemed impossible due to complexity

### Marko Jauregui
**Completed:**
- Studying wallet creation and account registration

**In Progress:**
- Social login implementation
- Abstracting Telegram login to be generic for Google implementation

**Blockers:**
- None mentioned

### Eduardo Yuschuk
**Completed:**
- Working on failed Pump Swap transactions
- Understanding ClickHouse data flow

**In Progress:**
- Mint storage with ClickHouse
- Transaction failure handling

**Notes:**
- Failed transactions in Jupiter lack complete information

## Key Discussion Points

### ClickHouse Database Optimization
- Ramiro achieved significant performance improvements
- Platform running smoothly with constant query complexity
- 150M trades handled efficiently
- Database designed for big data with columnar storage

### Deposit Process and States
- Federico implemented complete deposit flow
- Three intermediate states: pending, arrived at Unit, sold in spot, transferred to perpetuals
- User notification via toast when process completes
- Process takes approximately 5 minutes

### Transaction Signature Management
- Discussion about pre-calculating signatures before sending transactions
- Need to handle communication failures and backend crashes
- Proposal to create central agnostic service for transaction management

### Mobile Support Discussion
- Lucas Cufré proposed deprecating mobile version
- Product too complex for mobile breakpoints
- Suggestion to redirect users to desktop or native mobile apps
- Team agreement on focusing on desktop experience

## Action Items
- [ ] Create feature in Notion for transaction queue implementation - @Martin
- [ ] Implement signature pre-calculation for all transactions - @Federico
- [ ] Review and fix toast component close button visibility - @Mauricio
- [ ] Discuss mobile deprecation with Cooking stakeholders - @Lucas
- [ ] Set up meeting to explain ClickHouse table strategy - @Ramiro & @Eduardo

## Notes
- Weather forecast accuracy varies by city and satellite coverage
- Team exploring RabbitMQ for transaction confirmation notifications
- Keyboard navigation considered important but can be postponed if complex
- Mobile version deprecation would simplify development significantly

---
*Meeting notes generated by Gemini AI and translated to English*
*Original meeting date: July 11, 2025*
*Translation completed: 2025-10-20*