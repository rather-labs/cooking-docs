---
title: Daily Standup - 2025-09-22
type: meeting-note
meeting_type: Daily Standup
date: 2025-09-22
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
duration: 44 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_09_22 09_25 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-09-22

## Meeting Information
- **Type:** Daily Standup
- **Date:** September 22, 2025
- **Duration:** 44 minutes
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
- Martin Lecam
- Esteban Restrepo
- German Derbes Catoni
- Marcos Tacca
- Darío Balmaceda

## Summary
Luis Rivera continues working on complex table resolution and liquidation price review. Eduardo Yuschuk explained price discrepancies from data filters and is implementing outlier filtering. Martin Aranda identified 5-7 second delays when opening token details due to ClickHouse. Darío Balmaceda found performance issues with ClickHouse showing 2.5x slower queries and degrading backend performance. German Derbes Catoni completed frontend updates and advance orders development. Federico Caffaro finished slow withdrawals work. Esteban Restrepo converted transactions module to microservice and fixed bar data issues. Byron Chavarria completed user settings screen. Team identified open connections issues in ClickHouse and need for horizontal backend scaling.

## Team Updates

### Luis Rivera
- **Status:** Table resolution and price review ongoing
- **Progress:** Changed approach to use Get Token Bars and SC LastB functions
- **Blockers:** Strange price display in charts, especially DUSD token
- **Next Steps:** Review PR from German, complete table fixes, add Open Orders

### Eduardo Yuschuk
- **Status:** Price normalization and filtering
- **Progress:** Reduced price oscillations, filter implemented but not active
- **Blockers:** Outlier detection complexity
- **Next Steps:** Complete Total Supply table, activate outlier filter

### Martin Aranda
- **Status:** Backend optimization and patching
- **Progress:** Working on Total Supply patch from backend
- **Blockers:** Query taking 5-7 seconds during insertions
- **Next Steps:** Replace WebSocket with historical endpoint

### Darío Balmaceda
- **Status:** ClickHouse performance analysis
- **Progress:** Identified dual performance curves, quantified delays
- **Blockers:** Performance 2.5x slower in production vs local
- **Next Steps:** Test workload segregation and read replicas

### German Derbes Catoni
- **Status:** Frontend completion push
- **Progress:** Added Token Details, completed Advance Order buy section
- **Blockers:** None reported
- **Next Steps:** Complete sell orders, aim to finish this week

### Federico Caffaro
- **Status:** Slow withdrawals complete
- **Progress:** Thoroughly tested, PR ready for submission
- **Blockers:** None reported
- **Next Steps:** Begin multilevel referral work

### Esteban Restrepo
- **Status:** Microservice conversion and bar fixes
- **Progress:** Transactions as microservice, fixed zero-value bars
- **Blockers:** None reported
- **Next Steps:** Complete microservice deployment today/tomorrow

### Byron Chavarria
- **Status:** Mobile app finalization
- **Progress:** User settings complete, working on order cancellation
- **Blockers:** Unclear cancellation behavior spec
- **Next Steps:** Add confirmation modal, send PR

### Santiago Gimenez
- **Status:** Wallet manager and legal modals
- **Progress:** Wallet manager ready, working on privacy/terms modals
- **Blockers:** None reported
- **Next Steps:** Complete modals today

### Marko Jauregui
- **Status:** Frontend fixes and testing
- **Progress:** Completed Cooking Tag frontend, resolved Luis's bugs
- **Blockers:** None reported
- **Next Steps:** Continue bug fixes and testing

### Javier Grajales
- **Status:** Testing and PNL verification
- **Progress:** Working on tickets, focusing on PNL accuracy
- **Blockers:** Incorrect holdings and investment amounts displayed
- **Next Steps:** Continue testing, document issues

## Key Discussion Points

### Chart Display Issues
- Strange price visualization in charts, particularly DUSD token
- Possible delay in data rendering or incorrect timeframe filtering
- Luis investigating potential date mapping issues
- Need to verify bar timestamp accuracy

### ClickHouse Performance Root Causes
- Two distinct performance patterns identified
- Queries consistently slow during data insertions
- Backend performance degrading over time
- Local environments outperforming production significantly

### Backend Connection Management
- Possible connection leak issues with ClickHouse
- Need to monitor open connections
- Horizontal scaling blocked by WebSocket dependency
- Plan to remove WebSocket to enable auto-scaling

### Production Readiness
- Friday marked as critical for issue updates
- Important presentation requiring up-to-date Notion issues
- Team stressed importance of updating all tickets
- Focus on stability for upcoming week

## Action Items
- [ ] Luis Rivera: Review German's Token Details PR, fix table and charts
- [ ] Martin Aranda: Complete Total Supply backend patch
- [ ] Federico Caffaro: Test slow withdrawals thoroughly, submit PR
- [ ] Esteban Restrepo: Finish microservice conversion by tomorrow morning
- [ ] Luis Rivera: Add new timeframes up to 1 day, test implementation
- [ ] Byron Chavarria: Include cancellation modal, complete PR submission
- [ ] Santiago Gimenez: Complete terms and privacy policy modals today
- [ ] Martin Aranda: Replace WebSocket with historical endpoint
- [ ] Darío Balmaceda: Test resource segregation for ClickHouse
- [ ] All Team: Update Notion issues for Friday presentation

## Technical Details
- **ClickHouse Performance:** Queries 2.5x slower during insertions
- **Backend Degradation:** Performance decay over time despite stable resources
- **WebSocket Removal:** Critical for enabling horizontal scaling
- **Connection Management:** Potential connection pooling issues

## Links & References
- ClickHouse Performance Analysis: Histogram data showing dual curves
- WebSocket Migration: Plan for historical endpoint replacement
- iOS 18 Compatibility: Required updates for next 6 months

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*