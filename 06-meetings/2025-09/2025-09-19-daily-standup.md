---
title: Daily Standup - 2025-09-19
type: meeting-note
meeting_type: Daily Standup
date: 2025-09-19
attendees: [Eduardo Yuschuk, Santiago Gimenez, Luis Rivera, Florencia Redondo, Lucas Cufré, Martin Aranda, Marko Jauregui, Federico Caffaro, Javier Grajales, Byron Chavarria, Martin Lecam, Esteban Restrepo, German Derbes Catoni, Marcos Tacca, Darío Balmaceda]
duration: 67 minutes
language: Spanish (translated to English)
source_file: Daily - Cooking.gg_ 2025_09_19 09_27 GMT-03_00 - Notas de Gemini.md
---

# Daily Standup - 2025-09-19

## Meeting Information
- **Type:** Daily Standup
- **Date:** September 19, 2025
- **Duration:** 67 minutes
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
Luis Rivera reported complexity in table resolution and liquidation price review. Eduardo Yuschuk explained price discrepancies due to Radium and Pump.fun data filters. Martin Aranda addressed slow token details loading (5-7 seconds during inserts). Darío Balmaceda identified ClickHouse performance issues with 2.5x slower queries. German Derbes Catoni updated frontend with advance orders development. Federico Caffaro completed slow withdrawals work. Esteban Restrepo converted transactions module to microservice for auto-scaling. Byron Chavarria finalized user settings screen. Critical discussions included Available to Trade/Withdrawable discrepancies, PNL calculation issues in shorts, and liquidation price formula problems.

## Team Updates

### Luis Rivera
- **Status:** Complex table resolution and price calculations
- **Progress:** Slow mode integrated, limit orders partially functional
- **Blockers:** Liquidation price formula discrepancies with Hyperliquid
- **Next Steps:** Resolve table issues, add Open Orders to panel

### Eduardo Yuschuk
- **Status:** Price filtering and Total Supply implementation
- **Progress:** Identified and fixed trade interpretation issues in Radium/Pump.fun
- **Blockers:** Outlier filtering complexity
- **Next Steps:** Generate Real Total Supply table, implement outlier filter

### Martin Aranda
- **Status:** Performance optimization and backend stability
- **Progress:** Identified token details query slowness (5-7 seconds)
- **Blockers:** ClickHouse performance during insertions
- **Next Steps:** Implement caching patches, optimize query performance

### Darío Balmaceda
- **Status:** ClickHouse optimization analysis
- **Progress:** Quantified performance issues, found 2.5x slowdown pattern
- **Blockers:** Complex optimization requirements
- **Next Steps:** Investigate view materialization parallelization

### German Derbes Catoni
- **Status:** Frontend updates and advance orders
- **Progress:** Token Details additions, Advance Order buy section complete
- **Blockers:** None reported
- **Next Steps:** Complete sell orders, finish implementation this week

### Federico Caffaro
- **Status:** Slow withdrawals completion
- **Progress:** Feature tested and ready for PR submission
- **Blockers:** Decimal precision issues in orders
- **Next Steps:** Start multilevel referral system

### Esteban Restrepo
- **Status:** Microservice architecture conversion
- **Progress:** Transactions module converted, decorators implemented for Hyperliquid
- **Blockers:** None reported
- **Next Steps:** Complete microservice deployment, add bar calculations

### Byron Chavarria
- **Status:** Mobile app finalization
- **Progress:** User settings complete, portfolio integration working
- **Blockers:** iOS 18 compatibility requirements
- **Next Steps:** Submit PR, address iOS 18 changes

### Santiago Gimenez
- **Status:** Wallet manager completion
- **Progress:** Feature ready with import modifications
- **Blockers:** None reported
- **Next Steps:** Work on terms and privacy policy modals

### Marko Jauregui
- **Status:** Security password and bug fixes
- **Progress:** Security password settings complete, multiple bugs resolved
- **Blockers:** None reported
- **Next Steps:** Test with virgin accounts, continue bug fixes

### Javier Grajales
- **Status:** Testing and PNL verification
- **Progress:** PNL behaving correctly, identified holdings amount issues
- **Blockers:** 404 errors for users without Perpetual Wallet
- **Next Steps:** Continue testing, verify cross-margin calculations

## Key Discussion Points

### Available to Trade vs Withdrawable Discrepancy
- Major discussion about conflicting values between endpoints
- Cross-margin mode uses single money pool for all positions
- Withdrawable not accounting for open position values
- Team decided to export Hyperliquid wallet private key for testing

### PNL Calculation in Short Positions
- PNL appearing reversed for short positions
- Discussion about sign conventions (negative for shorts)
- Decision to keep absolute values with red coloring for losses
- Need to align with Hyperliquid's display conventions

### Liquidation Price Formula Issues
- Using Hyperliquid formula but getting different results
- Uncertainty about "maintenance leverage" variable
- Martin suggested price where margin equals zero
- Need to account for existing positions in calculation

### ClickHouse Performance Crisis
- Queries 2.5x slower with concurrent insertions
- Backend performance degrading over time
- Local environments performing better than production
- Considering read replicas and workload segregation

## Action Items
- [ ] Luis Rivera: Compare code with latest Figma, complete Open Orders tables
- [ ] German Derbes Catoni: Finish Token Details, review PR with Luis/Martin
- [ ] Marko Jauregui & Javier Grajales: Test security password creation with virgin account
- [ ] Esteban Restrepo: Add market cap calculation to bar cache
- [ ] Eduardo Yuschuk: Generate Real Total Supply table, work on outlier filter
- [ ] Federico Caffaro: Review Active Asset Data endpoint, export Hyperliquid wallet private key
- [ ] Luis Rivera: Use cross margin endpoint for front display, adjust position sizing
- [ ] Darío Balmaceda: Investigate ClickHouse parallelization options
- [ ] Byron Chavarria: Include cancellation modal and order behavior
- [ ] Santiago Gimenez: Complete terms and privacy policy modals

## Technical Details
- **Performance Issues:** Token details taking 5-7 seconds to load
- **ClickHouse:** Materialized views causing 2.5x query slowdown
- **Cross Margin:** Single collateral pool affecting calculations
- **Decimal Precision:** System allowing more decimals than Hyperliquid supports (5-6)

## Links & References
- Hyperliquid Documentation: Liquidation price formulas
- Cross Margin Explanation: Single pool collateral system
- ClickHouse Optimization: Parallelization strategies

---
*Source: Daily standup meeting notes auto-generated by Gemini and translated to English*