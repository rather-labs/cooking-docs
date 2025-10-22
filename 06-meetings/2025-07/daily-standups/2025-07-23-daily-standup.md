---
type: meeting-note
title: "Daily Standup - July 23, 2025"
meeting_type: "Daily Standup"
date: 2025-07-23
attendees: ["Eduardo Yuschuk", "Ramiro Carracedo", "Santiago Gimenez", "Luis Rivera", "Florencia Redondo", "Lucas Cufré", "Martin Aranda", "Mauricio Hernán Cabrera", "Marko Jauregui", "Federico Caffaro", "Angel Rangel"]
duration: "29 minutes"
language: "English (translated from Spanish)"
translation_date: "2025-10-20"
status: "Translated and Structured"
tags: ["daily-standup", "team-sync", "sprint", "july-2025"]
---

# Daily Standup - July 23, 2025

## Meeting Details
- **Date:** July 23, 2025
- **Time:** 09:29 - 09:58 (GMT-3)
- **Duration:** 29 minutes
- **Meeting Type:** Daily Standup
- **Attendees:** Eduardo Yuschuk, Ramiro Carracedo, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Angel Rangel
- **Language:** English (Translated from Spanish)

## Summary
Lucas transferred funds with a backend error and experienced token purchase operation failures. The team discussed UI updates, backend improvements, Hyperliquid integration challenges, and Ramiro Carracedo announced his departure from Rader.

## Team Updates

### Lucas Cufré
**Issues:**
- Fund transfer errors with backend
- Purchase operations failing for Jupiter-supported tokens
- Currency switch not working properly in token details screen

**In Progress:**
- Testing Jupiter token operations
- Working with external mobile design team
- Settings changes with Santiago
- Keyboard shortcuts implementation planning

**Notes:**
- Detected quick operations failure with Jupiter tokens
- Price/market cap display issues when switching SOL/USD

### Luis Rivera
**Completed:**
- Perpetual Swap height solution
- Skeleton additions to components
- Conversion integration including balance reading

**In Progress:**
- Perpetual contract selector integration
- Testing deposit functionality
- Table components for positions, order history, funding history, trade history

**Questions:**
- Should perpetual fee affect "total to receive" field?

### Mauricio Hernán Cabrera
**Completed:**
- UI V2 and Widgets folder restructuring
- Dialog component work

**In Progress:**
- SSE mocking issues
- Buffer error in modal history
- Moving modals to widgets folder

**Blockers:**
- SSE mocking not working with ChatGPT attempts

### Marko Jauregui
**Completed:**
- Turnkey implementation finalized
- Unit tests completed

**In Progress:**
- Frontend implementation study
- Google integration

**Notes:**
- Ready to implement in frontend

### Federico Caffaro
**Completed:**
- Live candles update implementation
- Initial candles delivery evaluation

**In Progress:**
- Testing streaming vs endpoint approach
- Deposit error recovery (0.2 SOL stuck in Devnet)

**Notes:**
- Unit address generated in Devnet, sent from Mainnet

### Ramiro Carracedo
**Completed:**
- PR sent for limits refactoring (aesthetic changes)
- Schematization of limits system

**In Progress:**
- BWAP, TWAP, DCA review
- Mins migration completion
- Infrastructure cleanup

**Announcement:**
- Leaving Rader after next week
- Expressed pleasure working with team

### Eduardo Yuschuk
**Completed:**
- Let's Bonk buy/sell operations branch ready
- Failed Pump Swap transactions handling

**In Progress:**
- ClickHouse information completion
- Bank Fan provider investigation
- Mints storage implementation

**Notes:**
- Failed Jupiter transactions lack source token info

### Angel Rangel
**Completed:**
- iOS 15 to iOS 16 migration
- Authentication screens and terms
- Home UI components
- Security keychain implementation

**In Progress:**
- Home screen complete assembly
- Filters and sleep configurations refinement

**Notes:**
- Navigation architecture refactoring required for iOS 16

### Santiago Gimenez
**Completed:**
- Settings page progress
- Login and user profile resolution

**In Progress:**
- Shortcuts and help center mapping
- Settings finalization

**Notes:**
- Working on web app settings

## Key Discussion Points

### Backend Transaction Errors
- Lucas experiencing failures with Jupiter-supported token operations
- Error: "Failed to sign version transaction B gateway"
- Environment variable issue identified in backend

### Hyperliquid Legal Concerns
- Not about server location but future legal exposure
- Hyperliquid doesn't operate in US due to SEC/CFTC licensing requirements
- Using Cooking as VPN for Hyperliquid access could create legal liability
- Team continuing implementation pending legal clarity

### Ramiro's Departure
- Announced departure from Rader
- Will remain for current and next week
- Team expressed gratitude for contributions
- Knowledge transfer ongoing

### UI/UX Issues
- Currency switch not updating all values properly in token details
- Need utility functions for formatting large numbers
- Liquidity showing zero for Jupiter tokens should be hidden
- Perpetuals view breaks at 1180px width

### Keyboard Shortcuts Implementation
- Discussing command+K pattern for token search
- Simpler to register hotkey directly vs full command list
- Would dispatch action to Zustand store

## Action Items
- [ ] Fix currency switch display issues - @Mauricio
- [ ] Create number formatting utilities - @Team
- [ ] Hide zero liquidity for Jupiter tokens - @Team
- [ ] Investigate backend transaction errors - @Martin
- [ ] Document keyboard shortcut requirements - @Lucas & @Santiago
- [ ] Complete knowledge transfer - @Ramiro

## Notes
- Team continuing Hyperliquid work despite legal uncertainties
- External Evil Martians team progressing on mobile wallet management
- Focus on optimizing transaction times as top priority
- Ramiro's departure will impact database and infrastructure work

---
*Meeting notes generated by Gemini AI and translated to English*
*Original meeting date: July 23, 2025*
*Translation completed: 2025-10-20*