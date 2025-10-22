---
title: Mobile App Final Sync - 2025-10-16
type: meeting
meeting_type: technical_deep_dive
topic: Mobile
date: 2025-10-16
attendees: [Lucas Cufre, Martin Aranda, Gregory Chapman, Naji Osmat, Zen (Sain), Marcos Tacca]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Mobile App Final Sync - Pre-Beta Launch - Cooking.gg
**Date:** October 16, 2025, 10:59 GMT-03:00
**Duration:** ~1 hour 14 minutes
**Meeting Type:** Technical Deep Dive + Product Review
**Attendees:** Lucas Cufre, Martin Aranda, Gregory Chapman, Naji Osmat, Zen (Sain), Marcos Tacca

## Executive Summary
Final pre-launch synchronization covering haptic feedback implementation, mobile UX patterns, trading engine strategy decision (Jupiter vs Echo), beta rollout plan, and production readiness checklist. Critical decision made to proceed with improved Jupiter-based system and defer Echo integration to future iteration.

## Meeting Context
With beta launch imminent (target: Monday for internal testing, following Monday for 30-45 users), team finalized all mobile-specific features, resolved Echo integration debate, and established clear launch timeline and testing protocol.

## Technical Discussion

### Haptic Feedback Implementation (Gregory & Naji)
**Three Haptic Interaction Types**:

1. **Ding** (Light vibration):
   - **Use Cases**: Non-transactional confirmations
   - **Examples**: Wallet saved, logged out, rewards claimed, security password entered correctly
   - **iOS Implementation**: Very quick vibration (like text message notification)

2. **Vibrate** (Medium vibration):
   - **Use Cases**: Final actions with perceived risk
   - **Examples**: Buy/sell confirmation, delete account, cancel order
   - **iOS Implementation**: Slightly longer buzz, stronger feedback
   - **Trigger Point**: When user completes action (e.g., completes swipe-to-confirm)

3. **Glow** (Visual effect):
   - **Use Cases**: Draw attention to actionable elements
   - **Examples**: "+" button for adding buying power, top-up/cash-out/transfer buttons, referral program, claim rewards
   - **Implementation**: Shimmer or gloss effect over button/element

**Key Interaction Patterns**:

**Swipe-to-Buy / Swipe-to-Sell**:
- **Long Press**: Activates swipe mode, makes element "hypersensitive"
- **Haptic on Long Press**: Indicates swipe is now available
- **Swipe Left/Right**: Triggers buy or sell action
- **Haptic During Swipe**: Continuous feedback while swiping
- **Completion Vibrate**: When swipe threshold reached, before execution
- **Purpose**: Prevents accidental purchases, requires deliberate user action

**Consensus Decision** (Lucas's Recommendation):
- Consistent pattern: Swipe one direction = buy, opposite direction = sell
- Don't change interaction based on screen (long-press on one screen, swipe on another = confusing)
- Gregory initially proposed: Long-press-to-buy (fills loading bar), swipe-to-sell
- **Final Decision**: Swipe for both buy and sell (consistent UX pattern)

**Order Cancellation**:
- Swipe to reveal cancel button
- Vibrate when cancel action confirmed
- Visual feedback (red button, destructive action indicator)

**Transaction Success Notification**:
- After transaction confirmed: Ding notification
- Optional: Native OS notification if app in background
- Display in-app toast/popup with transaction details

### Mobile UI/UX Decisions
**Information Density**:
- Mobile shows less info than desktop (simplified for screen real estate)
- No bonding curve progress bar on mobile token view
- No detailed trader graph on mobile
- Focus on essential metrics: price, volume, change%

**Design Approval**: Riz approved simplified mobile designs with Neo

**Order Entry Flow**:
- Buy/Sell buttons open order form (not immediate execution)
- Order form shows: token, quantity, price (if limit order), estimated total, fees
- TP/SL toggles expand additional configuration section
- Final confirm button has vibrate feedback

**Asset Display Issue** (Lucas identified):
- Design shows order size in SOL but user balance in USDT
- **Problem**: Meme coins only trade against SOL, not USDT
- **Resolution**: Display both order size and balance in SOL for consistency (can show USD equivalent as secondary info)

**Wallet Name Truncation Issue** (Lucas):
- Saved wallet names may be longer than available space
- **Solution**: Show wallet address initially, long-press to reveal full name (to be workshopped with Leo)

**"Special Mode" Clarification**:
- Currently unclear what "Special Mode" button does on mobile
- Desktop has: Trending, Gainers, Losers
- Mobile design shows advanced filtering instead
- **Action**: Lucas to add comment in Figma for Leo to clarify intended behavior

**Destructive Actions Styling** (Lucas):
- Delete account button should be red (iOS standard for dangerous actions)
- Consistent with iOS Human Interface Guidelines
- **Action**: Lucas to comment for Leo to update design

### Trading Engine Decision: Jupiter vs Echo
**Echo Integration Update** (Lucas):
- Still waiting for Yumen (Echo dev) response on trading pair definition
- Transaction fallback system implemented and working
- Security checking for transactions implemented (internal, no added latency)
- Three possible paths for beta launch

**Performance Improvements to Current System** (Lucas):
- Refactored trading logic into microservices
- Transaction confirmation: 2-3 seconds (down from 5-6 seconds)
- Significantly faster than original implementation
- Uses Jupiter as primary router, Hello Moon as fallback, native system as final fallback

**Echo POC (Proof of Concept) Results** (Martin):
- Transaction build time: ~1800ms for established tokens (multiple pools)
- Transaction submit time: +2 seconds
- **Failure rate**: ~60%
- For single-pool tokens: ~2 seconds total
- **Conclusion**: Not faster than current Jupiter implementation in practice

**Client Concern (via Zen)**: Yumen said Cooking's indexer is "inadequate" and must work with Echo

**Lucas's Clarification**:
- Echo requires indexing entire Solana universe (all liquidity pools)
- This is exponentially complex, constantly growing scope
- Current indexer: Main protocol contracts + Jupiter (80% coverage)
- Echo approach: Every pool contract (impossible to maintain without massive team)

**Team Recommendation (Lucas to Zen)**:
> "We cannot recommend launching Echo for beta. Our current system works well, is stable, and is faster than our original implementation. Echo is still in development, has high failure rates, and requires architecture changes that would take months."

**Zen's Decision**:
> "Let's proceed with current trading engine (Jupiter-based). Continue working with Echo in parallel as future iteration. Priority is getting product live and stable ASAP to get feedback."

**Rationale**:
- Need user feedback quickly
- Current system is proven and reliable
- Echo can be added later if they resolve issues
- First impressions matter - can't launch unstable beta

**Security Node Confirmation**:
- Transaction security checking doesn't add latency (backend internal)
- Fallback system already implemented
- **Decision**: Keep security checks, they provide value without performance cost

### Jupiter Optimization Details (Martin)
**Recent Bug Fix**:
- Jupiter over-optimized transactions, conflicted with fee additions
- **Solution**: Target "second best" price instead of perfect optimization
- Reduces transaction hops from 7 to 3
- More reliable, slight price tradeoff is acceptable

**Indexing Clarification** (Lucas):
- Not only indexing Jupiter
- Also indexing: Radium, Pump.fun, Launch Lab, and other main protocol contracts
- Jupiter responsible for ~80% of Solana transaction volume
- Provides broad price coverage

**Dependency Risk** (Zen's Question):
- What if Jupiter has breaking changes or downtime?
- **Lucas**: Indexer less affected (we index protocols directly)
- **Martin**: Transaction routing falls back to Hello Moon (1 second vs Jupiter's 500ms)
- Impact is latency increase, not complete failure

### Beta Launch Strategy
**Timeline**:
- **Tomorrow**: Something ready for internal testing
- **Monday (5 days)**: Internal team testing begins (Zen, Naji, Greg, Shakib)
- **5-Day Internal Beta**: Team uses as primary trading app, identifies issues
- **Following Monday**: Expand to 30-45 external beta users
- **Beta Scope**: Invite-only, whitelist enabled, referral links disabled initially

**Beta User Management**:
- Whitelist system already implemented
- Add 30-45 users to whitelist
- If they try to share referral links, non-whitelisted users blocked
- Keeps beta group controlled and manageable
- Easier to gather focused feedback and track specific users

**Post-Internal-Testing Decision**:
- After 5-day team testing, determine if ready for external users
- Collect feedback on: stability, UX, missing features
- If overwhelmingly positive → proceed to 30-45 user beta
- If issues found → fix before broader rollout

**No Determination Yet on Full Launch**:
- Open vs restricted access TBD based on beta feedback
- Marketing campaign details TBD
- Referral link caps/limits TBD
- Will decide after beta data collected

### Production Readiness Checklist
**Remaining Technical Tasks**:
- ✅ Transaction engine optimization completed
- ✅ Security checks implemented
- ✅ ClickHouse query optimization deployed
- ⏳ Finalizing UI tests across transaction types
- ⏳ Seeking additional performance optimizations (milliseconds)
- ⏳ Final security check deployment (couple hours)
- ⏳ Bug fixes for transaction toast notifications
- **Target**: Ready for internal testing by tomorrow

**Front-End Design Tasks** (per Riz):
- Safari testing completed
- Chrome testing completed
- **Coverage**: Chrome + Safari = ~92-93% of market
- **Beta Decision**: Limit to Chrome + Safari
- **Future**: Full browser coverage for subsequent launches

**Browser Support Philosophy**:
- Safari is most different from Chrome
- Chromium-based browsers (Edge, Brave, Opera) similar to Chrome
- Safari compatibility hardest, if it works on Safari + Chrome, others likely fine
- For beta, acceptable to limit scope

### Dubai Trip Planning
**Dates**: March 11-13 (Monday-Wednesday)
**Coworking Space**: Alba Corp, Business Bay, Dubai Marina
**Attendees**:
- From Cooking team: Lucas, Martin, Marcos, (Franco mentioned)
- From client team: Zen (Sain), Shakib, Naji, Greg
- (Riz may join for some events, not full coworking)

**Lucas to Share**: Telegram message with coworking space details and dates

### Ramper Document Verification
**Status**: Documents submitted, under review (up to 1 business day)
**Submitted**: Wednesday (15th)
**Current Status** (as of meeting): Still being reviewed
**Action**: Check again Monday, follow up with Ramper on Telegram if needed

## Key Technical Decisions
- **Decision 1:** Proceed with Jupiter-based trading engine for beta - Proven stability, better performance in testing than Echo
- **Decision 2:** Defer Echo integration to post-beta iteration - Avoid launching unstable, untested system
- **Decision 3:** Swipe interaction for both buy and sell - Consistent UX pattern across all screens
- **Decision 4:** Whitelist-only beta (30-45 users) before broader launch - Controlled feedback gathering
- **Decision 5:** Chrome + Safari support only for beta - Covers 92% of market, manageable testing scope

## Architecture & Design Considerations
- **Mobile-First Performance**: Optimize for 3G networks, low-end devices
- **Haptic Feedback**: Enhance UX without overwhelming users
- **Error Handling**: Clear, actionable error messages for mobile
- **Offline Support**: Graceful degradation when connectivity lost
- **Platform Consistency**: Follow iOS and Android design guidelines

## Performance & Scalability Notes
- **Transaction Latency**: 2-3 seconds end-to-end (competitive with industry leaders)
- **UI Responsiveness**: All interactions < 100ms feedback
- **Memory Usage**: Optimized for phones with 2-3GB RAM
- **Bundle Size**: Target < 50MB app download size

## Action Items
- [ ] **Gregory & Naji**: Find glow effect references, share with development team
- [ ] **Lucas**: Add Figma comments for Leo (wallet name truncation, "special mode", red delete button)
- [ ] **Lucas**: Follow up with Yumen (Echo dev) on server location question
- [ ] **Lucas**: Set up whitelist with initial 20-30 beta users
- [ ] **Lucas**: Share Dubai coworking details (Alba Corp) and dates in Telegram
- [ ] **Martin**: Finalize transaction toast notifications (success/failure feedback)
- [ ] **Team**: Complete internal testing starting Monday
- [ ] **Gregory & Lucas**: Verify Ramper document status Monday, follow up if needed

## Follow-up Items
- Post-internal-beta feedback review
- Determine full launch strategy (open vs gated)
- Plan marketing campaign for broader launch
- Schedule Dubai trip logistics (flights, accommodations)

## Technical References
- iOS Human Interface Guidelines (Haptic Feedback): https://developer.apple.com/design/human-interface-guidelines/playing-haptics
- React Native Haptic Feedback: https://github.com/junina-de/react-native-haptic-feedback
- iOS Destructive Actions: https://developer.apple.com/design/human-interface-guidelines/buttons

---
**Recording:** Transcription available
**Related Documents:**
- Mobile App Beta Launch Plan (04-knowledge-base/business/)
- Haptic Feedback Design Spec (04-knowledge-base/design/)
- Trading Engine Architecture (04-knowledge-base/technical/)
