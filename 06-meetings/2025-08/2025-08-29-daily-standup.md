---
title: Daily Standup - 2025-08-29
type: meeting-note
meeting_type: Daily Standup
date: 2025-08-29
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Esteban Restrepo, German Derbes Catoni, Marcos Tacca]
duration: 49 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_08_29 09_28 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-08-29

## Meeting Information
- **Type:** Daily Standup
- **Date:** August 29, 2025
- **Duration:** 49 minutes
- **Platform:** Google Meet
- **Language:** Spanish (translated to English)

## Attendees
- Eduardo Yuschuk
- Santiago Gimenez
- Luis Rivera
- Florencia Redondo
- Lucas Cufré
- Martin Aranda
- Marko Jauregui
- Federico Caffaro
- Javier Grajales
- Byron Chavarria
- Esteban Restrepo
- German Derbes Catoni
- Marcos Tacca

## Summary
Luis Rivera reported working on Market Orders functionality, fixing issues with API calls, and successfully implementing order management in TypeScript. German Derbes Catoni shared progress on aligning Token Details with Figma design and refactoring Wallet Manager with success/error states. Federico Caffaro resolved several bugs and API issues, while Santiago Gimenez updated the icon library and worked on new provider logos. Esteban Restrepo experienced memory issues during data processing and Eduardo Yuschuk implemented transaction tracking. Martin Aranda discussed removing WebSocket dependencies and backend migration plans. Byron Chavarria made significant progress on portfolio screens and authentication. The team discussed ClickHouse performance issues, planning for migration to PostgreSQL, and UI consistency improvements.

## Team Updates

### Luis Rivera
- **Status:** Working on Market Orders functionality and fixing API issues
- **Progress:** Successfully implemented market order management in TypeScript, fixed issues with 404 errors in API calls
- **Blockers:** Some API endpoints returning unexpected errors
- **Next Steps:** Continue with Market Orders implementation and testing

### German Derbes Catoni
- **Status:** Aligning Token Details page with Figma design v2.1
- **Progress:** Refactored Wallet Manager, added empty states and error handling
- **Blockers:** None reported
- **Next Steps:** Continue with UI alignment and component updates

### Federico Caffaro
- **Status:** Bug fixing and working on Perpetuals integration
- **Progress:** Fixed several bugs, resolved API connection issues
- **Blockers:** None reported
- **Next Steps:** Continue with Perpetuals development

### Santiago Gimenez
- **Status:** Updating design library and icons
- **Progress:** Added new provider logos, updated icon library
- **Blockers:** None reported
- **Next Steps:** Continue with UI updates and component library maintenance

### Esteban Restrepo
- **Status:** Working on data indexing and processing
- **Progress:** Implementing data processing pipeline
- **Blockers:** Memory issues during large data processing
- **Next Steps:** Optimize memory usage and continue with indexing

### Eduardo Yuschuk
- **Status:** Implementing transaction tracking and position monitoring
- **Progress:** Successfully tracking transactions, improving data accuracy
- **Blockers:** None reported
- **Next Steps:** Continue with transaction monitoring improvements

### Byron Chavarria
- **Status:** Working on portfolio screens for mobile app
- **Progress:** Advanced significantly on portfolio views, implemented authentication flows
- **Blockers:** None reported
- **Next Steps:** Complete portfolio screens and begin testing

### Martin Aranda
- **Status:** Backend architecture and infrastructure work
- **Progress:** Planning WebSocket removal, preparing database migration
- **Blockers:** ClickHouse performance issues
- **Next Steps:** Complete WebSocket removal and begin PostgreSQL migration

## Key Discussion Points

### ClickHouse Performance Issues
- Team experiencing significant performance problems with ClickHouse
- Martin Aranda proposed migration to PostgreSQL for better performance
- Discussion about optimizing queries and caching strategies
- Plan to implement Redis caching layer for frequently accessed data

### WebSocket Dependency Removal
- Decision to remove WebSocket dependencies to improve scalability
- Martin Aranda leading the effort to replace with REST endpoints
- Impact on real-time data updates being evaluated

### UI/UX Consistency
- Lucas Cufré emphasized importance of maintaining consistency with Figma designs
- Discussion about implementing proper empty states and loading indicators
- Need to standardize error handling across the application

### Market Orders Implementation
- Luis Rivera demonstrating progress on market orders functionality
- Discussion about order validation and error handling
- Integration with existing trading engine

## Action Items
- [ ] Luis Rivera: Complete market orders implementation and resolve remaining API issues
- [ ] German Derbes Catoni: Finish Token Details alignment with Figma v2.1
- [ ] Federico Caffaro: Continue Perpetuals development and testing
- [ ] Martin Aranda: Complete WebSocket removal and prepare PostgreSQL migration plan
- [ ] Esteban Restrepo: Optimize memory usage in data processing pipeline
- [ ] Eduardo Yuschuk: Improve transaction tracking accuracy
- [ ] Santiago Gimenez: Update remaining icons and UI components
- [ ] Byron Chavarria: Complete portfolio screens and begin integration testing

## Technical Details
- **Database Migration:** Planning move from ClickHouse to PostgreSQL for improved performance
- **WebSocket Removal:** Replacing WebSocket connections with REST endpoints for better scalability
- **Memory Optimization:** Addressing memory issues in data processing pipeline
- **API Improvements:** Fixing 404 errors and improving error handling in API endpoints

## Links & References
- Figma Design v2.1: Reference for UI alignment
- ClickHouse Documentation: For performance optimization strategies
- PostgreSQL Migration Guide: Planning database transition

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*