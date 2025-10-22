---
title: Daily Standup - 2025-08-08
type: meeting-note
meeting_type: Daily Standup
date: 2025-08-08
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca]
duration: 42 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_08_08 09_29 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-08-08

## Meeting Information
- **Type:** Daily Standup
- **Date:** August 8, 2025
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
Team discussed progress on trading features, mobile app development, indexer improvements, and upcoming strategic decisions. Key highlights include successful Auth0 integration completion, trading operations functionality, and preparation for strategic feature prioritization meeting.

## Team Updates

### Luis Rivera
- **Status:** Implementing trading interfaces and quick operations
- **Completed:** Quick buy/sell panels functional
- **Current Work:** Token detail views and advanced trading interfaces
- **Next Steps:** Complete trading view integration

### German Derbes Catoni
- **Status:** Component library standardization
- **Progress:** 80% of components updated to new design system
- **Current Work:** Final component validations
- **Next Steps:** Complete remaining component updates

### Martin Lecam
- **Status:** Auth0 integration complete
- **Achievement:** All social logins working (Twitter, Google, Apple)
- **Current Work:** Performance optimizations
- **Next Steps:** Support other team members with integration

### Marko Jauregui
- **Status:** Account linking backend complete
- **Completed:** User account linking functionality
- **Current Work:** Testing and edge case handling
- **Next Steps:** Frontend integration support

### Federico Caffaro
- **Status:** Advanced trading operations
- **Progress:** TWAP implementation complete
- **Current Work:** DCA (Dollar Cost Averaging) features
- **Blockers:** Need clarification on some business logic
- **Next Steps:** Complete DCA and begin limit order improvements

### Esteban Restrepo
- **Status:** Clickhouse migration progressing
- **Resolution:** Connection issues resolved with connection pool optimization
- **Current Work:** Data migration scripts
- **Next Steps:** Complete migration and performance testing

### Eduardo Yuschuk
- **Status:** Indexer running stably
- **Metrics:** Processing 100k+ transactions daily without issues
- **Current Work:** Monitoring and optimization
- **Next Steps:** Implement additional token support

### Byron Chavarria
- **Status:** Mobile app authentication complete
- **Achievement:** Auth0 fully integrated on mobile
- **Current Work:** Portfolio views and wallet management
- **Next Steps:** Trading operations for mobile

### Santiago Gimenez
- **Status:** Design system migration
- **Progress:** Kitchen page fully updated
- **Current Work:** Token detail pages
- **Next Steps:** Portfolio and settings pages

### Javier Grajales
- **Status:** Comprehensive testing ongoing
- **Issues Found:** Minor UI bugs, mostly resolved
- **Current Focus:** Trading operations testing
- **Next Steps:** Performance and stress testing

### Lucas Cufré
- **Status:** Strategic planning and coordination
- **Key Decision:** Feature prioritization meeting scheduled
- **Current Work:** Preparing roadmap adjustments
- **Next Steps:** Client meeting for final priorities

### Martin Aranda
- **Status:** Architecture and technical decisions
- **Focus:** Performance optimization strategies
- **Decisions:** Approved Clickhouse migration approach
- **Next Steps:** Review system architecture for scale

## Key Discussion Points

### Feature Prioritization
- Need to decide between advanced trading features vs. social features
- Client meeting scheduled to finalize priorities
- Impact on Q3 deliverables discussed

### Performance Optimization
- Clickhouse migration showing positive results
- Connection pooling improvements implemented
- Planning for high-load scenarios

### Mobile Feature Parity
- Decision to maintain feature parity between web and mobile
- Timeline adjustments may be needed
- Focus on core trading features first

### Design System Implementation
- Successfully migrating to new design system
- Improved consistency across application
- Some custom components still need updates

## Action Items
- [ ] Lucas Cufré: Conduct feature prioritization meeting with client
- [ ] Federico Caffaro: Complete DCA implementation
- [ ] Esteban Restrepo: Finish Clickhouse migration
- [ ] Byron Chavarria: Implement mobile trading operations
- [ ] Santiago Gimenez: Complete design system migration
- [ ] Martin Aranda: Review and optimize system architecture
- [ ] Team: Prepare for Q3 deliverable review

## Technical Details
- **Clickhouse Performance:** 10x improvement in query performance observed
- **Auth0 Integration:** All providers working with custom callbacks
- **Trading Operations:** TWAP complete, DCA in progress, limit orders next
- **Mobile Development:** Authentication complete, trading features in progress

## Blockers & Risks
- Feature scope vs. timeline concerns
- Need client decision on priorities
- Some business logic clarifications needed

## Decisions Made
- Proceed with Clickhouse migration
- Maintain feature parity between platforms
- Focus on core trading features for Q3

## Links & References
- Related Features: Trading operations, Mobile app, Design system
- Related Meetings: Upcoming feature prioritization meeting

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*