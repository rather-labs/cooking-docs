---
type: meeting-note
title: "Daily Standup - July 30, 2025"
meeting_type: "Daily Standup"
date: 2025-07-30
attendees: ["Eduardo Yuschuk", "Ramiro Carracedo", "Santiago Gimenez", "Luis Rivera", "Florencia Redondo", "Lucas Cufré", "Martin Aranda", "Mauricio Hernán Cabrera", "Marko Jauregui", "Federico Caffaro", "Angel Rangel"]
duration: "30 minutes"
language: "English (translated from Spanish)"
translation_date: "2025-10-20"
status: "Translated and Structured"
tags: ["daily-standup", "team-sync", "sprint", "july-2025"]
---

# Daily Standup - July 30, 2025

## Meeting Details
- **Date:** July 30, 2025
- **Time:** 09:27 - 09:57 (GMT-3)
- **Duration:** 30 minutes
- **Meeting Type:** Daily Standup
- **Attendees:** Eduardo Yuschuk, Ramiro Carracedo, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Angel Rangel
- **Language:** English (Translated from Spanish)

## Summary
The team discussed Google integration progress with token validation issues, Hyperliquid legal considerations, ClickHouse migration advances, and UI/UX improvements. Key topics included chart interactivity requirements for mobile and production deployment considerations.

## Team Updates

### Federico Caffaro
**Completed:**
- Frontend and backend setup for Google integration
- Google login flow working

**Issues:**
- Token validation failing during callback
- Need to create Google provider before validating token

**In Progress:**
- Fixing token validation in Turnkey
- Wallet creation flow with Google

### Martin Aranda
**Clarification:**
- No need to create user/wallet if already logged in
- Should link accounts instead
- Separate user story for account linking

### Mauricio Hernán Cabrera
**Completed:**
- Dialog PR merged
- Moving components to B2 folder

**In Progress:**
- Component reorganization (may cause PR conflicts)
- Helping resolve PR conflicts

**Notes:**
- Luis offered to help with conflict resolution

### Luis Rivera
**Completed:**
- Three perpetual form cases (right side)
- Leverage change dialog
- Perpetual account and balance components
- Market close dialog for positions

**In Progress:**
- Code refactoring for optimization
- Fixing display issues at 1000px width
- Chart integration (final component)

**Notes:**
- Will reuse bar chart from normal order

### Lucas Cufré
**Key Discussion:**
- Legal concern isn't server change but future exposure
- Hyperliquid doesn't operate in US due to SEC/CFTC licensing
- Using Cooking as VPN for Hyperliquid access creates legal liability
- Business continues as usual until legal clarity

**Activities:**
- Working with external team on wallet management
- Documenting trading methods for user ebook
- Take profit and portfolio exit feature development
- Settings and referral screen updates

### Ramiro Carracedo
**Completed:**
- ClickHouse migration deployed and working
- Everything moved from Mins to ClickHouse
- Indexer resource consumption reduced

**Issues:**
- Total holders count problem (working with Eduardo)

**Notes:**
- Platform slightly slower but acceptable
- Can reduce instance size and costs
- Announcing departure from Rader next week

### Eduardo Yuschuk
**Completed:**
- Let's Bonk provider implementation
- Merging Radium minimal liquidity to ClickHouse

**In Progress:**
- Final ClickHouse data completion
- Ensuring Let's Bonk propagates same messages as Pump Fun

**Notes:**
- Let's Bonk becomes first-tier launcher
- Owner of indexer database after migration

### Angel Rangel
**Completed:**
- SCE integration bringing and encoding all data
- Stop screen integration complete
- Search integration with recent tokens

**In Progress:**
- Specials screen filter integration
- Icon corrections
- Security keychain development

**Notes:**
- Investigating chart library capabilities for iOS

### Santiago Gimenez
**Completed:**
- Settings screen review with Lucas
- Criteria document for settings functionality

**In Progress:**
- Component updates based on team needs
- Settings finalization

**Notes:**
- Created comprehensive settings behavior document

### Martin Aranda
**Questions:**
- Should Hyperliquid endpoints be hidden before production?
- Can chart component be reused for perpetuals?

**Concerns:**
- Need to add breaking changes for limits
- Feature flagging may be necessary

## Key Discussion Points

### Hyperliquid Legal Implications
- Not a technical issue but legal liability concern
- SEC/CFTC licensing required for leveraged contracts in US
- Acting as VPN bypass could result in legal action
- Team continuing development pending legal decision

### Chart Interactivity Requirements
- Real-time chart updates needed
- User interaction to identify specific price points
- Touch interaction for price identification on mobile
- Binance mobile app has this feature on Android
- iOS implementation needs investigation

### Production Deployment Considerations
- Need to hide Hyperliquid endpoints if deploying
- Breaking changes in backend need frontend updates
- Feature flagging being considered
- Funding flow currently active in staging

### ClickHouse Migration Success
- All data successfully migrated
- Performance acceptable with reduced resources
- Cost savings possible with smaller instances
- Some query optimization still needed

## Action Items
- [ ] Fix Google token validation - @Federico
- [ ] Investigate iOS chart interactivity libraries - @Angel
- [ ] Hide Hyperliquid endpoints before production - @Martin
- [ ] Fix total holders count issue - @Ramiro & @Eduardo
- [ ] Create account linking user story - @Martin
- [ ] Document chart requirements for external team - @Lucas

## Notes
- Last meeting before Ramiro's departure
- Team expressed gratitude for Ramiro's contributions
- External Evil Martians team progressing on mobile wallet
- Production deployment on hold pending Hyperliquid decision

---
*Meeting notes generated by Gemini AI and translated to English*
*Original meeting date: July 30, 2025*
*Translation completed: 2025-10-20*