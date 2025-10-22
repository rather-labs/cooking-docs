---
type: meeting-note
title: "Daily Standup - July 14, 2025"
meeting_type: "Daily Standup"
date: 2025-07-14
attendees: ["Eduardo Yuschuk", "Ramiro Carracedo", "Santiago Gimenez", "Luis Rivera", "Florencia Redondo", "Lucas Cufré", "Martin Aranda", "Mauricio Hernán Cabrera", "Marko Jauregui", "Federico Caffaro", "Angel Rangel"]
duration: "23 minutes"
language: "English (translated from Spanish)"
translation_date: "2025-10-20"
status: "Translated and Structured"
tags: ["daily-standup", "team-sync", "sprint", "july-2025"]
---

# Daily Standup - July 14, 2025

## Meeting Details
- **Date:** July 14, 2025
- **Time:** 09:27 - 09:50 (GMT-3)
- **Duration:** 23 minutes
- **Meeting Type:** Daily Standup
- **Attendees:** Eduardo Yuschuk, Ramiro Carracedo, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Angel Rangel
- **Language:** English (Translated from Spanish)

## Summary
The team shared updates on project progress including Telegram integration completion, wallet security discussions, deposit and perpetual wallet implementation, and UI component development. Santi returned to the team and an external design team was onboarded for iOS expertise.

## Team Updates

### Angel Rangel
**Completed:**
- Telegram network integration ready and tested
- Working on UI components for home screen
- Exploring authentication flow with refresh tokens

**In Progress:**
- Authentication implementation with automatic refresh
- Biometric authentication investigation

**Notes:**
- Access tokens set to 1 day expiry
- Discussing biometric authentication vs security password for mobile

### Lucas Cufré
**Key Points:**
- External design team joining with iOS expertise
- Fund movements between user's own accounts won't require signature
- Funds in Hyperliquid can't be withdrawn elsewhere, must loop back through Cooking
- Clarified withdrawal requires whitelisted wallet or external signature

### Luis Rivera
**Completed:**
- Design details for popover and Perpetuals dashboard
- Convert modal designed and connected to UI

**In Progress:**
- Perpetual contract search component
- Waiting for service integration

**Questions:**
- Exchange rate for conversion modal (SOL to USD)

### Federico Caffaro
**Completed:**
- Deposit development including edge cases handling
- Unit fee deductions implementation
- Full flow from SOL deposit to Hyperliquid working

**In Progress:**
- Perpetual operations endpoints
- Wallet creation automation

**Notes:**
- Deposits leave small remainder due to decimal limitations
- Perpetual wallets created on first transfer/deposit

### Mauricio Hernán Cabrera
**Completed:**
- Input component finished
- Cancel button changes
- UI component structuring

**In Progress:**
- Form control adaptation for components
- Component organization in B2 folder structure

**Blockers:**
- None mentioned

### Ramiro Carracedo
**Completed:**
- Table design for mints migration
- Jupiter functionality working correctly

**In Progress:**
- Schema review with Eduardo
- Migration completion planning

**Notes:**
- Everything related to Jupiter should be functioning

### Eduardo Yuschuk
**Completed:**
- Failed Pump Swap transactions task progress

**In Progress:**
- Mint storage implementation with ClickHouse
- Data structure optimization

**Blockers:**
- None mentioned

### Marko Jauregui
**Completed:**
- Started Google login implementation
- Created Telegram strategy pattern
- Created Google strategy pattern

**In Progress:**
- General auth service development
- Provider abstraction

**Notes:**
- Building more generic authentication service

### Santiago Gimenez
**Completed:**
- Returned to team
- Caught up with project status

**In Progress:**
- Syncing with Lucky on next steps
- Private key configuration settings
- Login systems implementation

**Notes:**
- Back from absence, getting up to speed

## Key Discussion Points

### Wallet Security and Signatures
- Internal fund transfers won't require security password
- Funds remain within Hyperliquid ecosystem
- Export to whitelisted wallets doesn't require new signature
- External withdrawals require signature verification

### Biometric Authentication for Mobile
- Team discussing replacing security password with biometric auth
- Face ID/Touch ID implementation being evaluated
- Would improve user experience on mobile devices

### External Design Team
- New team with iOS expertise onboarded
- Will help with mobile-specific design challenges
- Language design changes expected this year

### Perpetual Wallet Creation
- Wallets created automatically on first deposit/transfer
- Separate database entries with different tags
- Balance queries return zero for unused accounts

## Action Items
- [ ] Document biometric authentication data requirements - @Angel
- [ ] Review Storybook components once merged - @Lucas
- [ ] Implement exchange rate approximation for conversion - @Luis
- [ ] Create withdrawal endpoint for remaining balances - @Federico
- [ ] Schedule schema review meeting - @Ramiro & @Eduardo

## Notes
- Team welcomed Santi back after absence
- iOS design expertise crucial for upcoming mobile development
- Decimal precision limitations in Hyperliquid operations noted
- Exchange rate can be approximate for conversion display

---
*Meeting notes generated by Gemini AI and translated to English*
*Original meeting date: July 14, 2025*
*Translation completed: 2025-10-20*