---
title: Daily Standup - 2025-09-05
type: meeting-note
meeting_type: Daily Standup
date: 2025-09-05
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Esteban Restrepo, German Derbes Catoni, Marcos Tacca]
duration: 56 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_09_05 09_29 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-09-05

## Meeting Information
- **Type:** Daily Standup
- **Date:** September 5, 2025
- **Duration:** 56 minutes
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
Luis Rivera reported issues with TradingView and SSE connection problems. Martin Aranda confirmed WebSocket removal is complete but facing SSE stability issues. Federico Caffaro worked on Perpetuals integration and fixed token filtering. German Derbes Catoni completed Token Details with new advanced orders UI. Santiago Gimenez finished icon library updates and started on terms & conditions modal. Esteban Restrepo implemented Redis caching for improved performance. Eduardo Yuschuk resolved price tracking issues and improved data accuracy. Byron Chavarria completed user settings screens and portfolio integration. Javier Grajales identified critical bugs in perpetuals and conducted extensive testing. The team discussed SSE connection stability, TradingView integration challenges, and performance optimization strategies.

## Team Updates

### Luis Rivera
- **Status:** Working on TradingView integration and SSE issues
- **Progress:** Identified connection problems with SSE, working on fixes
- **Blockers:** SSE connections dropping frequently, TradingView data sync issues
- **Next Steps:** Implement connection retry logic, fix data synchronization

### Martin Aranda
- **Status:** WebSocket removal complete, SSE implementation
- **Progress:** Successfully removed all WebSocket dependencies, SSE partially working
- **Blockers:** SSE stability issues in production environment
- **Next Steps:** Debug SSE issues, implement fallback mechanisms

### Federico Caffaro
- **Status:** Perpetuals integration and token filtering
- **Progress:** Fixed token filtering logic, improved Perpetuals UI
- **Blockers:** None reported
- **Next Steps:** Complete Perpetuals testing, optimize performance

### German Derbes Catoni
- **Status:** Token Details and advanced orders
- **Progress:** Completed Token Details page, new UI for advanced orders ready
- **Blockers:** None reported
- **Next Steps:** Integration testing with backend

### Santiago Gimenez
- **Status:** UI updates and legal documents
- **Progress:** Icon library updated, working on terms & conditions modal
- **Blockers:** Waiting for final legal text
- **Next Steps:** Complete modal implementation

### Esteban Restrepo
- **Status:** Redis caching implementation
- **Progress:** Implemented caching layer, 50% performance improvement
- **Blockers:** None reported
- **Next Steps:** Extend caching to more endpoints

### Eduardo Yuschuk
- **Status:** Price tracking and data accuracy
- **Progress:** Fixed price deviation issues, improved tracking accuracy
- **Blockers:** None reported
- **Next Steps:** Implement real-time price alerts

### Byron Chavarria
- **Status:** Mobile app user settings
- **Progress:** Completed settings screens, portfolio integration working
- **Blockers:** None reported
- **Next Steps:** Polish UI and fix minor bugs

### Javier Grajales
- **Status:** QA and bug tracking
- **Progress:** Found critical bugs in perpetuals, documented test cases
- **Blockers:** None reported
- **Next Steps:** Regression testing for fixed issues

## Key Discussion Points

### SSE Connection Stability
- Major issue with Server-Sent Events connections dropping
- Martin Aranda implementing reconnection logic
- Discussion about using long-polling as fallback
- Need for better error handling and recovery mechanisms

### TradingView Integration Challenges
- Data synchronization issues between backend and TradingView
- Luis Rivera working on custom data adapter
- Performance concerns with real-time updates
- Planning to implement data batching

### Performance Optimization
- Redis caching showing significant improvements
- Discussion about database query optimization
- Planning to implement CDN for static assets
- Monitoring tools being set up for production

### Perpetuals Feature Launch
- Feature nearly complete, entering final testing phase
- Federico Caffaro addressing last UI issues
- Planning soft launch with limited users
- Risk management features being validated

## Action Items
- [ ] Luis Rivera: Fix SSE connection issues and TradingView sync
- [ ] Martin Aranda: Implement SSE reconnection logic and fallbacks
- [ ] Federico Caffaro: Complete Perpetuals testing suite
- [ ] German Derbes Catoni: Integrate advanced orders with backend
- [ ] Santiago Gimenez: Finish legal modals once content received
- [ ] Esteban Restrepo: Extend Redis caching coverage
- [ ] Eduardo Yuschuk: Deploy real-time price alert system
- [ ] Byron Chavarria: Polish mobile app UI
- [ ] Javier Grajales: Complete regression testing cycle

## Technical Details
- **SSE Issues:** Connections dropping after 30 seconds, need keepalive implementation
- **Redis Performance:** 50% reduction in API response times
- **TradingView:** Custom adapter needed for data format compatibility
- **Database:** Query optimization reduced load by 30%

## Links & References
- SSE Implementation Guide: Best practices for connection management
- Redis Caching Strategy: Documentation for cache invalidation
- TradingView API: Custom adapter specifications

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*