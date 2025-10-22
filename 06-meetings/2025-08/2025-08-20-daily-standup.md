---
title: Daily Standup - 2025-08-20
type: meeting-note
meeting_type: Daily Standup
date: 2025-08-20
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca]
duration: 29 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_08_20 09_27 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-08-20

## Meeting Information
- **Type:** Daily Standup
- **Date:** August 20, 2025
- **Duration:** 29 minutes
- **Platform:** Google Meet
- **Language:** Spanish (translated to English)

## Attendees
- Eduardo Yuschuk
- Santiago Gimenez
- Luis Rivera
- Florencia Redondo
- Lucas Cufré
- Martin Aranda
- Mauricio Hernán Cabrera
- Marko Jauregui
- Federico Caffaro
- Javier Grajales
- Byron Chavarria
- Martin Lecam
- Esteban Restrepo
- German Derbes Catoni
- Marcos Tacca

## Summary
Lucas Cufré welcomed new team members Germán Derbes Catoni and Esteban Restrepo. Team discussed frontend development progress, authentication challenges, Perpetual infrastructure and fees, indexer updates, and bubble map integration concerns. Focus on approaching project deadline with multiple initiatives in progress.

## Team Updates

### Lucas Cufré
- **Status:** Team coordination and new member onboarding
- **Key Points:** Welcomed German (frontend) and Esteban (backend) to team
- **Current Work:** Bubble map investigation, user settings story
- **Concerns:** Bubble map integration complexity
- **Next Steps:** Research InsideX integration options

### Martin Lecam
- **Status:** Frontend development progress
- **Completed:** Released designs to Marko for backend
- **Current Work:** Frontend implementation nearly complete
- **Next Steps:** Review metrics with Martin Aranda, finalize PR

### Luis Rivera
- **Status:** Kitchen component migration
- **Completed:** Using v2 components, fixed screen length issues
- **Achievement:** Fixed columns instead of mobile tabs, horizontal scrolling per design
- **Next Steps:** Continue with remaining bug fixes

### Marko Jauregui
- **Status:** Custom referral codes and Auth0 integration
- **Progress:** Backend for custom referral codes advancing
- **Current Work:** Twitter authentication with Auth0
- **Blockers:** Bug when logging into Twitter using Google account
- **Next Steps:** Complete unit tests for backend

### German Derbes Catoni (New Member)
- **Status:** Onboarding and initial setup
- **Background:** Frontend developer from Nera (Banco Galicia platform)
- **Issues:** Authentication problems with Telegram, Google, Apple
- **Current Work:** Reviewing Figma, project structure, preparing for Dropdinium component
- **Next Steps:** Start working on assigned component once auth issues resolved

### Esteban Restrepo (New Member)
- **Status:** Backend onboarding and setup
- **Background:** From Colombia, worked at Coibanks (fintech/web3 factory)
- **Completed:** Local environment setup, identified auth bug
- **Finding:** Bug in user repository with refresh token transaction
- **Next Steps:** Continue familiarization with codebase

### Martin Aranda
- **Status:** Infrastructure and architecture oversight
- **Achievement:** Perpetual server operational (DNS pending)
- **Current Work:** DNS configuration with clients
- **Next Steps:** Review PRs and complete infrastructure setup

### Federico Caffaro
- **Status:** HyperLiquid stop-loss and take-profit implementation
- **Challenge:** Orders set through undocumented frontend-specific endpoint
- **Blockers:** Signature error preventing implementation
- **Current Work:** Trying to replicate frontend behavior in backend
- **Next Steps:** Continue debugging signature issues

### Eduardo Yuschuk
- **Status:** Indexer improvements and maintenance
- **Progress:** Version with multiple changes running well
- **Issues:** Some scam tokens not getting complete information
- **Current Work:** Tracking edge cases, parameter table for real-time control
- **Next Steps:** Continue monitoring and optimization

### Byron Chavarria
- **Status:** Mobile Auth0 integration
- **Progress:** Finalizing Auth0 integration
- **Current Work:** Authentication testing with Apple and Google
- **Next Steps:** Move to wallet management and portfolio overview

## Key Discussion Points

### Zero Bridge Fees Decision
- No fees for bridge operations (in or out)
- No commission for Solana to USDC conversion on Arbitrum
- Strategy to be competitive with other services
- Plan to include builder codes logic in Perpetuals

### Bubble Map Integration Challenge
- Most competitors use external product called "InsideX"
- Concern about complexity if not external service
- Would require significant ML work if built internally
- Cannot be postponed per requirements

### Authentication Issues
- Multiple team members experiencing auth problems
- Auth0 configuration issues identified
- Refresh token bug discovered and fix in PR
- Whitelist issues for some auth methods

### HyperLiquid API Challenges
- Undocumented frontend-specific endpoints
- Complex signature requirements
- Poor API quality acknowledged by team
- Considering participation in HyperLiquid improvement program

## Action Items
- [ ] Martin Aranda: Review PR and complete DNS configuration
- [ ] Marko Jauregui: Fix Twitter/Google auth bug and complete unit tests
- [ ] Federico Caffaro: Investigate builder codes inclusion in Perpetuals
- [ ] German/Esteban: Request necessary backend access for review
- [ ] Esteban: Send AWS questions internally
- [ ] Eduardo: Track and resolve token indexing corner cases
- [ ] Byron: Complete Auth0 testing with Apple and Google
- [ ] Lucas: Research InsideX integration and pricing

## Technical Details
- **Auth Bug:** Refresh token update before transaction commit in SQL
- **Perpetuals:** Infrastructure ready, awaiting DNS configuration
- **Indexer Performance:** Handling multiple protocol changes successfully
- **HyperLiquid Issues:** Signature validation problems with order types

## Blockers & Risks
- Bubble map integration complexity uncertain
- HyperLiquid API quality affecting implementation
- Authentication issues blocking some team members
- Timeline pressure with 5 weeks to delivery

## Decisions Made
- No bridge fees to maintain competitiveness
- Include builder codes logic in Perpetuals
- Research external solution for bubble map
- Prioritize functionality over perfect implementation

## Links & References
- Related Features: Auth0, HyperLiquid, Perpetuals, Bubble Map
- Related Meetings: Previous discussions on Q3 deliverables

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*