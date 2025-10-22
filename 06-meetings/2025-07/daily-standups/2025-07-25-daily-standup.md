---
type: meeting-note
title: "Daily Standup - July 25, 2025"
meeting_type: "Daily Standup"
date: 2025-07-25
attendees: ["Eduardo Yuschuk", "Ramiro Carracedo", "Santiago Gimenez", "Luis Rivera", "Florencia Redondo", "Lucas Cufré", "Martin Aranda", "Mauricio Hernán Cabrera", "Marko Jauregui", "Federico Caffaro", "Angel Rangel"]
duration: "17 minutes"
language: "English (translated from Spanish)"
translation_date: "2025-10-20"
status: "Translated and Structured"
tags: ["daily-standup", "team-sync", "sprint", "july-2025"]
---

# Daily Standup - July 25, 2025

## Meeting Details
- **Date:** July 25, 2025
- **Time:** 09:26 - 09:43 (GMT-3)
- **Duration:** 17 minutes
- **Meeting Type:** Daily Standup
- **Attendees:** Eduardo Yuschuk, Ramiro Carracedo, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Angel Rangel
- **Language:** English (Translated from Spanish)

## Summary
Federico reported Hyper Liquid API restrictions in the US leading to legal considerations. The team discussed system improvements including limiters refactoring, ClickHouse event implementation, and UI component development progress.

## Team Updates

### Federico Caffaro
**Issues:**
- Hyper Liquid API returns error 500 due to US geographic restrictions

**In Progress:**
- Awaiting decision on Hyper Liquid feature continuation
- Order book implementation pending

**Notes:**
- Legal team evaluating proxy service implications

### Martin Aranda
**Key Points:**
- Exploring separate European service with geo-restrictions
- Legal concerns about being used as proxy for restricted operations
- Meeting with Rader C-level to evaluate risks
- May implement with geo-restrictions or drop feature entirely

### Ramiro Carracedo
**Completed:**
- Schematizing limiters requirements
- API and typing improvements

**In Progress:**
- PR for limiters refactor (no functionality changes)
- Vulnerability and concurrency issue analysis
- Heavy changes planning

**Notes:**
- Found vulnerabilities in fund blocking
- Concurrency problems identified

### Eduardo Yuschuk
**Completed:**
- Let's Bonk operations branch ready
- Bonding curves discovery implementation

**In Progress:**
- Sending all ClickHouse events for protocols
- Event capture experimentation
- Launchpad tagging strategy

**Notes:**
- Avoiding re-indexing sensitivity
- Tokens identifiable as "launchpad operating Let's Bonk tokens"

### Angel Rangel
**Completed:**
- All Highway component themes finished

**In Progress:**
- Waiting for API explanation from Martin
- Integration planning

**Notes:**
- Ready for API integration

### Marko Jauregui
**Completed:**
- Frontend Google implementation almost complete

**In Progress:**
- Fine-tuning and testing
- TR proxy integration

**Notes:**
- Implementation nearly ready

### Mauricio Hernán Cabrera
**Completed:**
- Dialog modals for Storybook

**In Progress:**
- Operation modal implementation
- Token search modal
- Position modal mocking

**Notes:**
- Working on Storybook visualization

### Luis Rivera
**Completed:**
- Dashboard preparation with mocked data
- Perpetual components with mocked data
- Tables ready (positions, order history, funding history, trade history)

**In Progress:**
- Right panel for order creation
- Service integration preparation

**Notes:**
- Everything ready for quick integration when services available

### Santiago Gimenez
**Completed:**
- Settings screen solid version
- New navigation icons for Angel
- Select component for Luis

**In Progress:**
- Settings review with Lucky
- Help center implementation

**Notes:**
- Using modified input version in Figma (no select component)

## Key Discussion Points

### Hyper Liquid Geographic Restrictions
- API blocked in United States territory
- Legal evaluation ongoing for proxy service setup
- Two options: implement with restrictions or cancel feature
- Decision pending from Rader C-level and client

### Limiters System Refactoring
- Major vulnerabilities discovered in fund blocking
- Concurrency issues need addressing
- Refactor maintaining current functionality while fixing issues
- Heavy changes required for proper implementation

### ClickHouse Migration Progress
- Event sending for all protocols underway
- Focus on avoiding duplicate data from re-indexing
- Table design allows parallel data sending
- Migration script planned for minimal Postgres data

### Frontend Preparation Strategy
- Luis preparing all components with mocked data
- Enables quick integration once backend services ready
- Stress testing revealed sequential processing bottleneck
- All perpetual-related UI ready for integration

## Action Items
- [ ] C-level meeting for Hyper Liquid decision - @Martin
- [ ] Complete limiters vulnerability documentation - @Ramiro
- [ ] Test Let's Bonk integration - @Eduardo
- [ ] Explain APIs to Angel for integration - @Martin
- [ ] Review settings with Lucky - @Santiago
- [ ] Complete position modal mocking - @Mauricio

## Notes
- Lucas absent from this meeting
- Legal implications of proxy service being carefully evaluated
- Team prepared to pivot if Hyper Liquid feature cancelled
- Strong focus on having frontend ready for backend integration

---
*Meeting notes generated by Gemini AI and translated to English*
*Original meeting date: July 25, 2025*
*Translation completed: 2025-10-20*