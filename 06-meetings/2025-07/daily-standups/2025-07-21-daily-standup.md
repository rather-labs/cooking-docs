---
type: meeting-note
title: "Daily Standup - July 21, 2025"
meeting_type: "Daily Standup"
date: 2025-07-21
attendees: ["Eduardo Yuschuk", "Ramiro Carracedo", "Santiago Gimenez", "Luis Rivera", "Florencia Redondo", "Lucas Cufré", "Martin Aranda", "Mauricio Hernán Cabrera", "Marko Jauregui", "Federico Caffaro", "Angel Rangel"]
duration: "16 minutes"
language: "English (translated from Spanish)"
translation_date: "2025-10-20"
status: "Translated and Structured"
tags: ["daily-standup", "team-sync", "sprint", "july-2025"]
---

# Daily Standup - July 21, 2025

## Meeting Details
- **Date:** July 21, 2025
- **Time:** 09:29 - 09:45 (GMT-3)
- **Duration:** 16 minutes
- **Meeting Type:** Daily Standup
- **Attendees:** Eduardo Yuschuk, Ramiro Carracedo, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Angel Rangel
- **Language:** English (Translated from Spanish)

## Summary
Martin Aranda reported GitHub integrations are down. The team discussed component refactoring progress, Web Socket integration, Turnkey implementation completion, and plans for documentation and wallet management unification.

## Team Updates

### Martin Aranda
**Key Issues:**
- GitHub integrations down (lint checks, cloud, merge blocking)
- Made fixes to Wallet Manager validations
- Reviewed social login implementation

**In Progress:**
- Transaction optimization initiative planning
- Wallet Manager improvements

### Mauricio Hernán Cabrera
**Completed:**
- Form control component finished
- Mini refactor of components for form control adaptation
- Currency input component added
- Deprecation comments added to all old UI components

**In Progress:**
- Reorganizing component/B2 structure (UI and features folders)
- PR reviews pending

**Notes:**
- ~10,000 lines of code for review

### Luis Rivera
**Completed:**
- Closed Perpetual Stock work (almost complete)
- Color fill implementation based on order values
- Component height issues being resolved

**In Progress:**
- Table item component modifications
- Select component adjustments
- Orders and trades panel
- Integration with conversion services

**Blockers:**
- Waiting for services to test deposit functionality

### Federico Caffaro
**Completed:**
- Web Socket integration on Friday
- Server-sent events handling
- Single channel implementation for all users

**In Progress:**
- More thorough testing needed
- Last user closes the channel implementation

**Notes:**
- Appears to be working but needs verification

### Marko Jauregui
**Completed:**
- Turnkey implementation advancement
- PR corrections from previous work

**In Progress:**
- Google implementation review with Martin
- Unit tests completion

**Blockers:**
- None mentioned

### Ramiro Carracedo
**Completed:**
- Mints migration work
- PR sent but awaiting indexer data for testing

**In Progress:**
- Diamond Hands calculation analysis
- Formula optimization exploration
- Original formula document review

**Notes:**
- Looking to convert series calculation to direct formula

### Eduardo Yuschuk
**Completed:**
- Radium launchpad swap implementation for Let's Bonk

**In Progress:**
- PR review for ClickHouse information increase
- Waiting for funds to test execution

**Notes:**
- 4 items total, 2 remaining

### Angel Rangel
**Completed:**
- Telegram authentication screen
- Terms and conditions screen
- Some home screen components
- Security keychain for token storage

**In Progress:**
- Complete home UI assembly
- Refresh token automatic handling

**Notes:**
- Authentication flow working without re-login

### Santiago Gimenez
**Completed:**
- Settings screen review with Lucas
- Document created with functionality criteria

**In Progress:**
- Figma organization for pending items
- Private key configuration settings
- Login systems implementation

**Notes:**
- Meeting with Lucky to understand next phases

### Lucas Cufré
**Key Activities:**
- Extensive client meetings (6+ hours)
- External design team (Evil Martians) progress on mobile
- Documentation for trading methods (ebook for users)
- Take profit and exit portfolio feature work
- Wallet management and portfolio unification planning
- Referral screen conversion for sharing

**In Progress:**
- GitBook documentation creation
- Portfolio and Wallet Manager unification proposal
- Referral program page changes (visual only)

## Key Discussion Points

### GitHub Integration Issues
- All GitHub integrations currently down
- Affecting lint checks, cloud services, merge blocking
- Team to continue working despite limitations

### Component Organization
- Major refactoring of component structure
- Moving from root components to organized B2 folder
- Separation of UI components and features

### Transaction Optimization Initiative
- Internal dark initiative for transaction time optimization
- Mapping all tasks needed to speed up swaps
- High priority due to client pressure
- May include frontend balance validation changes

### Documentation and User Guides
- Creating GitBook documentation for users
- Will serve multiple purposes across platforms
- Documenting trading methods for ebook

### Mobile and Desktop Strategy
- External design team (Evil Martians) handling mobile wallet management
- Discussion about unifying portfolio and wallet management
- Referral page changes for social sharing capability

## Action Items
- [ ] Create transaction optimization initiative in project - @Martin
- [ ] Review form control PR (~10k lines) - @Martin
- [ ] Test Let's Bonk implementation once funded - @Eduardo
- [ ] Complete Diamond Hands formula analysis - @Ramiro
- [ ] Pass video of authentication flow - @Angel
- [ ] Work on wallet/portfolio unification - @Lucas & @Santiago

## Notes
- GitHub issues not blocking development but affecting CI/CD
- Roadmap remains unchanged despite client delays on mobile screens
- Focus on making referral page shareable for social media
- Transaction optimization is top priority for tangible results

---
*Meeting notes generated by Gemini AI and translated to English*
*Original meeting date: July 21, 2025*
*Translation completed: 2025-10-20*