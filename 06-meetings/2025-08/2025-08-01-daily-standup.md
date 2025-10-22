---
title: Daily Standup - 2025-08-01
type: meeting-note
meeting_type: Daily Standup
date: 2025-08-01
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Mauricio Hernán Cabrera, Marko Jauregui, Federico Caffaro, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni]
duration: 9 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_08_01 09_29 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-08-01

## Meeting Information
- **Type:** Daily Standup
- **Date:** August 1, 2025
- **Duration:** 9 minutes
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
- Byron Chavarria
- Martin Lecam
- Esteban Restrepo
- German Derbes Catoni

## Summary
Martin Aranda led the daily sync, discussing the successful integration of Auth0, TradingView widget improvements, progress on trading functionalities, indexer development, and migration to Clickhouse. Lucas Cufré shared API definition requirements and task priorities, while the team collectively reviewed status and upcoming goals for the quarter-end objectives.

## Team Updates

### Martin Aranda
- **Status:** Monitoring multiple areas of progress
- **Focus:** Leading team coordination and technical decisions
- **Next Steps:** Continue overseeing integration efforts

### Luis Rivera
- **Status:** Completed Wallet Manager functionality following design specifications
- **Completed:** Finished bug fixes assigned by Javier
- **Next Steps:** Working on TradingView widget chart implementation

### Martin Lecam
- **Status:** Working on Auth0 integration for Twitter authentication
- **Completed:** Almost finished with Twitter auth using custom callback
- **Blockers:** Twitter auth redirect issues with Auth0
- **Next Steps:** Continue troubleshooting Auth0 Twitter integration

### Marko Jauregui
- **Status:** Resolved Redis issues and working on Auth0 functionality
- **Completed:** Fixed Redis serialization/deserialization issues
- **Next Steps:** Complete Auth0 support tasks and unit testing

### Federico Caffaro
- **Status:** Working on order services and TWD functionality
- **Progress:** Created sell, buy, and close position orders for spot
- **Next Steps:** Continue with order cancellation and TWD implementation

### Eduardo Yuschuk
- **Status:** Achieved significant indexer improvements
- **Achievement:** 50x performance improvement in indexing operations
- **Technical Details:** Reduced processing time from 30 minutes to 30 seconds for full token indexing
- **Next Steps:** Monitor corner cases and continue optimization

### Byron Chavarria
- **Status:** Progressing with Auth0 implementation
- **Progress:** Halfway through Auth0 integration
- **Next Steps:** Complete Auth0 setup and prepare for demo

### Esteban Restrepo & German Derbes Catoni
- **Status:** New team members onboarding
- **Focus:** Getting familiar with codebase and project structure
- **Next Steps:** Begin contributing to assigned tasks

### Lucas Cufré
- **Status:** Defining API specifications and requirements
- **Focus:** Establishing conventions for response formats and error handling
- **Key Points:** Standardizing API responses with data/error structure
- **Next Steps:** Complete API documentation and share with team

## Key Discussion Points

### Auth0 Integration Challenges
- Twitter authentication experiencing redirect issues
- Team working on custom callback implementation
- Need to resolve Auth0 configuration for social logins

### Indexer Performance Breakthrough
- Eduardo achieved 50x performance improvement
- Processing time reduced from 30 minutes to 30 seconds
- Significant milestone for system scalability

### API Standardization
- Lucas emphasized need for consistent API responses
- Established data/error response structure
- Working on comprehensive API documentation

### Migration to Clickhouse
- Team preparing for Clickhouse migration
- Focusing on data consistency and performance
- Planning phased transition approach

## Action Items
- [ ] Martin Lecam: Resolve Twitter Auth0 redirect issues
- [ ] Luis Rivera: Complete TradingView widget integration
- [ ] Federico Caffaro: Finish order cancellation functionality
- [ ] Eduardo Yuschuk: Monitor indexer corner cases
- [ ] Lucas Cufré: Finalize and share API documentation
- [ ] Byron Chavarria: Complete Auth0 implementation
- [ ] Team: Prepare for end-of-quarter demo

## Technical Details
- **Redis Issues:** Resolved serialization/deserialization problems affecting system stability
- **Indexer Optimization:** Achieved 50x performance improvement through algorithm optimization
- **API Standards:** Implementing consistent data/error response format across all endpoints
- **Auth0 Setup:** Configuring social login providers with custom callbacks

## Links & References
- Related Features: Auth0 integration, TradingView widgets, Order management
- Related Meetings: Previous discussions on Q3 objectives

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*