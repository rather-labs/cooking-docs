---
title: Cooking Demo - Social Login, Performance & Perpetuals Development
date: 2025-09-05
type: demo
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Naji Osmat
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Marcos Tacca
  - Shakeib Shaida (shakeib98@gmail.com)
status: completed
tags:
  - demo
  - social-login
  - perpetuals
  - performance-optimization
  - trading-platform
  - tradingview
related:
  - "[[2025-08-27-cooking-demo]]"
  - "[[2025-09-12-cooking-demo]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team provided comprehensive updates on perpetuals development, focusing on slow mode deposit/withdrawal implementation, performance improvements, and social login testing. The advanced TradingView chart has been successfully implemented. A key discussion centered on whether the trading platform should be included in the September release, with the conclusion to focus on updating charts while deferring additional features. Visual updates aligned with Leo's latest design language are being implemented, though issues with Apple account access continue to block mobile testing.

## Meeting Details

**Duration:** 33 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Apple Account Payment Issues

**Context:** Gregory Chapman reported ongoing problems with Apple account payments affecting mobile development.

**Key Points:**
- Payment processed twice (Monday and Thursday) but orders remain in "processing" status
- Money has been debited from bank account but service not activated
- 48-hour processing window repeatedly exceeded
- Blocking mobile testing and QA processes

**Impact:**
- Mobile engineer cannot access Apple developer account
- Testing twice daily (morning and afternoon) to check for access
- Delaying mobile app development and testing workflows

### 2. AI Model Training Discussion

**Context:** Team discussing approach for AI model development.

**Updates from Shakeib Shaida:**
- Team discussing optimal training approaches for AI model
- Identifying data requirements for model training
- Martin Aranda creating document detailing currently available data
- Will facilitate cross-referencing and planning for AI implementation

### 3. Perpetuals Development Progress

**Backend Work (Lucas Cufré):**
- **Slow Mode Implementation:** Active development of batch deposit/withdrawal system
  - Allows multiple users to share transaction fees
  - Process: Solana → USDC → Perpetual wallets in Hyperliquid
  - Reduces individual transaction costs
- Backend implementation nearly complete
- Frontend implementation and testing to follow

**Performance Improvements:**
- Addressing loading time bottlenecks on main screens
- Optimizing service information exposure
- Preparing infrastructure for closed beta traffic
- Some screens (token details, charts) experiencing excessive loading times
- Active refactoring by backend team and DevOps engineer

**Timeline Status:**
- On track to meet all perpetuals commitments
- Ready for closed beta deployment

### 4. Social Login Implementation

**Status:** Successfully tested and implemented

**Features:**
- Multiple login method support (Twitter/X, Gmail, Telegram, Solana wallet)
- User can link multiple accounts to single Cooking account
- Can access same account from any linked login method
- Users can unlink accounts (one primary method must remain)

**Technical Implementation:**
- User settings model implemented in app
- Link/delink functionality for social accounts
- Primary account designation required
- Cannot remove primary account without designating new one

### 5. TradingView Advanced Chart Integration

**Status:** Successfully implemented

**Features:**
- Advanced chart functionality integrated
- Enhanced charting capabilities for traders
- Ready for production deployment

### 6. Trading Platform vs September Deadline

**Discussion:**
- Lucas requested clarification on whether trading platform needed by September
- Gregory confirmed platform was recently proposed (previous week)
- Decision: Trading platform NOT required for September release

**Agreed Approach:**
- Focus on updating charts for September release
- Defer trading platform bells and whistles to post-September
- Maintain feature list for future implementation
- Swap basic charts for advanced charts in current timeline

**From Joe's Documentation:**
- Simplest implementation: Swap existing charts for trading platform
- Extra features require additional implementation work
- Current manpower allocated to other priority features

### 7. Navigation and UI Updates

**Navigation Hotkeys:**
- Additional navigation shortcuts implemented
- Not user-customizable in initial release
- Provides quick access to common actions
- Visually accessible through user settings

**Visual Updates:**
- First iteration of Leo's latest visual language being tested
- Typography and color updates across all components
- First batch of design language updates nearing completion

### 8. New Login Screen Requirements

**Implemented Features:**
- New login screen with current token prices
- Clean, modern interface aligned with design system

**Blockers - Required Links:**
- Terms and Conditions document (iOS requirement)
- Privacy Policy document (iOS requirement)
- Twitter/X account link (community building)
- Discord account link (community building)

**Priority:**
- Terms and Conditions & Privacy Policy are blockers for iOS mobile app
- Social links essential for community building and engagement

### 9. TradingView Chart Data Quality

**Issues Identified:**
- Some tokens showing gaps between candles
- Vertical disconnections in bar data
- Data model being changed to improve TradingView information quality

**Root Causes:**
- Indexer data quality improvements needed
- SPL token burn events causing data pollution
- Some events providing inaccurate price information

**Solutions in Progress:**
- Updating query definitions in ClickHouse for better performance
- Improving block indexing to prefer higher quality prices
- Handling tricky events (like SPL token burn) more accurately
- Ensuring trader can operate on accurate information

### 10. Mobile Development Status

**Referral System:**
- Successfully implemented
- Pending testing (blocked by Apple account access)

**Security Password Creation:**
- Successfully implemented (receipts for login)
- Pending testing (blocked by Apple account access)

**Wallet Work:**
- Development continuing
- Apple account access remains blocker for mobile testing

**QA Status:**
- Mobile engineer attempting access twice daily
- Cannot begin mobile testing until Apple account accessible

### 11. Documentation Requirements

**Outstanding Needs:**
- Terms and Conditions document
- Privacy Policy document
- Active Twitter/X account link
- Active Discord account link

**Purpose:**
- iOS App Store compliance (Terms & Privacy Policy)
- Social community building (Twitter & Discord)
- Mobile app launch requirements

### 12. Visual Language Alignment

**Status:** On track for end-of-month deadline

**Scope:**
- Latest updates to Leo's visual language
- Colors, chart visualizations, form creation, tables
- Biggest change: Wallet manager screen (complete layout redesign)

**Agreement:**
- Document shared August 27th with full team access
- Leo has access to same document, no comments received
- Assuming approval by silence
- Naji requested formal specification document for additional verification

**Perpetuals Updates:**
- Updated to Leo's latest definitions
- Mostly same layout with minor detail changes

**Referral Program:**
- Design updates in progress
- Multi-level referral system design being finalized

### 13. Trading Terminal Discussion

**Decision:** Deferred to future development

**Rationale:**
- Focus on implementing updated charts for September
- Leave additional functionalities for later phases
- Was always considered future development item
- Lucas to review documentation for better understanding of requirements

**Action:**
- Lucas to read trading terminal documentation
- Provide feature list and implementation requirements estimate by Monday

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Trading platform NOT required for September | Recently proposed, short timeline | Focus on chart updates instead |
| Defer trading platform bells and whistles | Current manpower allocated elsewhere | Maintain feature list for future |
| Update charts only for September | Achievable with current timeline | Better features can come later |
| Social login priority | Support mobile app development | Enable parallel development |
| One primary login method required | Account security and access | Users cannot remove all login methods |
| Terms & Privacy Policy blockers for iOS | Apple App Store requirements | Must provide before mobile launch |
| Create formal specification document | Additional verification for Leo | Reduce risk of design misalignment |
| Trading terminal is future work | Was always planned for later | Document requirements for planning |

## Action Items

### High Priority

- [ ] **Gregory/Zen** - Resolve Apple account payment processing issue (URGENT)
- [ ] **Gregory/Zen** - Provide Terms and Conditions document (Due: ASAP, iOS blocker)
- [ ] **Gregory/Zen** - Provide Privacy Policy document (Due: ASAP, iOS blocker)
- [ ] **Gregory/Zen** - Provide Twitter/X account link for social integration (Due: ASAP)
- [ ] **Gregory/Zen** - Provide Discord account link for social integration (Due: ASAP)
- [ ] **Naji** - Follow up with Zen on Apple account status (Due: Ongoing)

### Medium Priority

- [ ] **Lucas** - Create formal specification document for Leo's design updates (Due: September 8, 2025)
- [ ] **Lucas** - Review trading terminal documentation and provide feature list/requirements (Due: September 8, 2025)
- [ ] **Lucas** - Share document link with Naji for Riz verification (Due: September 6, 2025)
- [ ] **Martin** - Complete data availability document for AI team (Due: September 12, 2025)

### Low Priority

- [ ] **Gregory** - Attempt to contact Apple support via email (Due: Ongoing)
- [ ] **Lucas** - Send meeting minutes via email (Due: September 6, 2025)

## Technical Notes

### Social Login Architecture
- Cooking account as central hub
- Multiple login methods link to single account
- Primary method designation system
- Link/delink functionality with constraints

### Performance Optimization
- Bottleneck identification in progress
- DevOps engineer working on refactors
- Focus areas: main screens, service information exposure
- Target: Handle closed beta traffic efficiently

### Data Quality Improvements
- ClickHouse query optimization
- Block indexing preference refinements
- Event handling improvements (SPL token burn, etc.)
- Ensuring accurate price information for traders

### TradingView Integration
- Advanced chart successfully implemented
- Data quality issues being addressed
- Gap/disconnection fixes in progress

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Apple account access blocked | Mobile testing completely blocked | Attempting access twice daily; Gregory contacting support |
| Terms & Privacy Policy missing | iOS app cannot be submitted | Urgent request to Gregory/Zen |
| Social account links missing | Cannot complete mobile UI | Requested from Gregory/Zen |
| Chart data quality issues | User experience degradation | Data model improvements in progress |
| Design alignment uncertainty | Potential rework required | Creating formal specification document |
| Leo's design feedback unclear | Assumption of approval risky | Naji requesting double-verification with Riz |

## Next Steps

1. **Immediate:** Resolve Apple account payment issue (Gregory/Zen)
2. **This Week:** Provide Terms, Privacy Policy, and social links (Gregory/Zen)
3. **This Week:** Complete formal specification document (Lucas)
4. **Next Week:** Review trading terminal requirements (Lucas)
5. **Ongoing:** Continue perpetuals development and performance optimization
6. **Ongoing:** Attempt Apple account access twice daily for mobile testing

## Key Metrics & Numbers

- **Apple payment attempts:** 2 (Monday and Thursday)
- **Mobile testing attempts:** 2 per day (morning and afternoon)
- **Document sharing date:** August 27, 2025
- **Referral program sharing date:** August 19, 2025
- **Days without Leo feedback:** ~9 days (since August 27)

## References

- Leo's Visual Language Document (shared August 27)
- Referral Program Design (shared August 19)
- Joe's Trading Platform Documentation
- TradingView Advanced Chart Integration

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
