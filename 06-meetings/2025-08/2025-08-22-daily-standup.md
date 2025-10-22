---
title: Daily Standup - 2025-08-22
type: meeting-note
meeting_type: Daily Standup
date: 2025-08-22
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca]
duration: 42 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_08_22 09_29 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-08-22

## Meeting Information
- **Type:** Daily Standup
- **Date:** August 22, 2025
- **Duration:** 42 minutes
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
Team discussed frontend improvements, HyperLiquid functionality including slow mode for fee optimization, infrastructure updates, and AWS memory usage concerns. Marcos Tacca joined to welcome new members and encourage the team for the final project phase.

## Team Updates

### Luis Rivera
- **Status:** Bug fixes and component migration
- **Completed:** Fixed assigned bugs
- **Current Work:** Migrating filter modal to v2 components, redoing custom orders component
- **Next Steps:** Implement limiters and ensure proper functionality

### German Derbes Catoni
- **Status:** Dropdinium component development
- **Progress:** Started working on component, collaborated with Luis on workflow
- **Current Work:** Understanding component library and Figma organization
- **Next Steps:** Send PR for Dropdinium component today

### Martin Lecam
- **Status:** Custom code and wallet connect
- **Completed:** Custom code integrated and merged with backend fixes
- **Current Work:** Implementing wallet connect functionality
- **Next Steps:** Complete wallet connect by end of day

### Marko Jauregui
- **Status:** Account linking implementation
- **Progress:** Investigated account linking for different providers
- **Blockers:** Waiting for user table issue resolution
- **Next Steps:** Continue with backend account linking once unblocked

### Federico Caffaro
- **Status:** HyperLiquid orders implementation
- **Completed:** Take profit and stop loss orders, builder codes
- **Current Work:** PR review and adjustments
- **Next Steps:** Review HyperLiquid module for improvements and testing

### Esteban Restrepo
- **Status:** Clickhouse migration and improvements
- **Completed:** PR review, helped German with backend setup
- **Current Work:** Migrating trading microservices to Clickhouse (BWAP focus)
- **Achievements:** Implemented request logging interceptor, mock transaction function
- **Next Steps:** Send PR for BWAP Clickhouse migration

### Eduardo Yuschuk
- **Status:** Indexer optimization and maintenance
- **Progress:** Version with many changes running well
- **Issues:** Some scam tokens missing URL and metadata
- **Current Work:** Tracking corner cases from continuous indexer operation
- **Next Steps:** Clean PostgreSQL replicas when ready

### Byron Chavarria
- **Status:** Mobile Auth0 integration
- **Completed:** A0 authentication for Google, Twitter, Apple
- **Current Work:** Referral code implementation
- **Next Steps:** Focus on referral code UI and integration

### Javier Grajales
- **Status:** Testing and monitoring
- **Focus:** Bug resolution and AWS memory monitoring
- **Findings:** Progressive memory increase since recent deployment
- **Next Steps:** Continue monitoring and testing

### Santiago Gimenez
- **Status:** Kitchen refactor with updated design system
- **Progress:** Most components ready except token card
- **Next Steps:** Complete token card implementation

### Lucas Cufré
- **Status:** Documentation and strategic planning
- **Current Work:** Bubble Maps research (InsideX integration)
- **Key Findings:** Free plan available, paid plan ~$360-370 for map generation
- **Concerns:** Bubble map integration complexity
- **Next Steps:** Complete user settings story and external wallet support

### Martin Aranda
- **Status:** Infrastructure and architecture oversight
- **Focus:** Transaction service unification, Cloudwatch monitoring
- **Decisions:** Implement monitoring alarms for memory issues
- **Next Steps:** Cost estimation for Cloudwatch implementation

## Key Discussion Points

### HyperLiquid Slow Mode
- Intermediate Solana wallet for multiple users to deposit funds
- Funds converted and bridged from intermediate wallet
- Users share gas fees for transactions
- Amounts reassigned on the other side
- Allows for more competitive fee structure

### Transaction Service Unification
- BWAP not currently using transaction service
- Plan to unify with Quick Operations service
- Benefits for stress testing and maintenance
- Mock functionality for local testing without spending funds

### AWS Memory and Monitoring
- Progressive memory increase observed
- Need for Cloudwatch alarms implementation
- Cost estimation required for client approval
- Sentry limitations due to shared account with other projects

### Bubble Maps Integration
- InsideX identified as primary provider
- Free tier available but limited
- Paid tier allows map generation (~$360-370)
- Cannot be postponed despite not being core feature

### External Wallet Support
- Allow users to import existing Solana wallets
- Encrypt and store keys securely in Turnkey
- Convert external wallets to centralized Turnkey wallets
- Enable transaction signing through Turnkey

## Action Items
- [ ] Martin Aranda: Add user validation endpoint for account linking
- [ ] Esteban: Unify BWAP with transaction service
- [ ] Eduardo: Experiment with moving blocks back to PostgreSQL
- [ ] Javier & Martin: Discuss Cloudwatch alarm cost estimates
- [ ] Lucas: Write slow mode documentation for HyperLiquid
- [ ] Lucas: Document On Ramper integration for mobile
- [ ] Team: Prepare for final sprint push

## Technical Details
- **Memory Issues:** Progressive increase requiring monitoring
- **Clickhouse Migration:** BWAP service being migrated
- **Structured Logging:** JSON format for easier debugging in Cloudwatch
- **Mock Transactions:** Local testing without blockchain costs
- **Builder Codes:** Successfully implemented in HyperLiquid

## Blockers & Risks
- Memory consumption trending upward
- Bubble map complexity if not external service
- Timeline pressure for September deliverables
- Sentry log limits due to shared account

## Decisions Made
- Implement Cloudwatch monitoring
- Use InsideX for bubble maps
- Unify transaction services
- Support external wallet imports

## Team Announcements
- Marcos Tacca welcomed new team members
- Acknowledged approaching project finish line
- Emphasized upcoming "entertaining" weeks
- Offered support and availability via Slack

## Links & References
- Related Features: HyperLiquid slow mode, Bubble maps, External wallets
- Related Meetings: Previous discussions on monitoring and performance

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*