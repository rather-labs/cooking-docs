---
title: Cooking Demo - On-Ramp Integration & Mobile App Strategy
date: 2025-07-11
type: demo
attendees:
  - Lucas Cufré
  - Gregory Chapman (greg@ember.app)
  - Martin Aranda
  - Naji Osmat
  - Zen (z@ember.app)
status: completed
tags:
  - demo
  - on-ramp
  - crossmint
  - mobile-development
  - lets-bank-integration
  - social-login
  - kyc-requirements
related:
  - "[[2025-07-04-cooking-demo]]"
  - "[[04-knowledge-base/technical/integrations/crossmint]]"
  - "[[04-knowledge-base/technical/integrations/onramper]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team discussed critical decisions around on-ramping solutions, weighing Crossmint's checkout feature (no KYC for meme coins but creates dead-end without Solana for gas) against traditional KYC-based on-ramps. Development progress showed successful ClickHouse migration, Let's Bank integration nearing completion, and Telegram social login operational. A key strategic decision was made to deprioritize the Crossmint checkout feature in favor of focusing on core functionality to meet the September deadline, with checkout potentially added later. The mobile app will redirect web users rather than supporting responsive web design, and iOS App Store documentation via GitBook was initiated.

## Meeting Details

**Duration:** 48 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Development Progress Updates

**Backend Achievements:**
- Hyperliquid integration: Testing Solana deposit flow operational
- Core services integration progressing
- Turnkey integration on Hyperliquid side underway
- Trades database migration to new ClickHouse server completed
- System now live in production

**Indexer Progress:**
- Finished indexing Jupiter-supported tokens
- Expected to be tradable by mid-next week
- Working alongside backend on ClickHouse integration
- Connectivity issue with QuickNode resolved

**Frontend Updates:**
- Testing skeleton loaders for active positions, model portfolio page, and referrals
- New components for quick operations panel (forms, buttons, cards, icons)
- Started work on perpetuals screen
- Updated token details and custom orders with skeleton loaders

**Mobile Development:**
- Onboarded new mobile engineer successfully
- Infrastructure and native components ready
- Color alignment work continuing
- Signup, login, and home flows in progress
- **Social login milestone:** Telegram login achieved and working on web and mobile
- Backend work started on Google social login
- Twitter social login planned
- Apple social login deferred until business account access

### 2. Let's Bank AMM Integration

**Status:** Near completion (expected by following week)

**Technical Details:**
- Requires native integration similar to Pump.fun, Moonshot, and Radium
- Architecture compatible with existing structure (similar to Radium)
- Indexer portion nearly complete
- Tokens can be traded via Jupiter with direct fallbacks for supported providers

**Timeline:**
- Indexer work: Completed this week
- Full implementation: Expected by following week
- Integration benefited from architectural similarities with Radium

**Key Insight:** Lucky architectural alignment enabled faster progress than typical protocol integration

### 3. Crossmint On-Ramp Analysis

**The Core Problem:**
Lucas researched Crossmint's on-ramp solution and discovered it's actually a "checkout" feature - a direct fiat-to-meme-coin swap, not a traditional on-ramp.

**Two Distinct Features:**

1. **Checkout (No KYC Required):**
   - Direct purchase of specific items (NFTs, meme coins, products)
   - Seen as a selling operation, not requiring KYC
   - Available in non-OFAC sanctioned regions
   - Offers best conversion rate
   - Used by FOMO app that Riz shared

2. **On-Ramp (KYC Required):**
   - Traditional wallet funding with crypto
   - Supports Solana and other assets
   - Requires full KYC process
   - Standard on-ramp functionality

**The Dead-End Problem:**

**Scenario:** User buys meme coin via checkout without KYC
- **Result:** User owns meme coin but has no Solana for gas fees
- **Outcome:** Cannot sell or trade the meme coin (stuck position)
- **Solution:** Would still need to KYC to get Solana, defeating the purpose

**Key Quote from Lucas:**
> "Basically, if we want to buy Solana, we would have to go through the KYC itself."

**Why This Matters:**
- Target audience: "Normies" without existing crypto holdings
- These users won't have external wallets with Solana
- Without Solana, any meme coin purchase becomes unusable
- Cooking is a trading platform, not a wallet - users need to exit positions

**Additional Concerns:**
- No control over transaction routing
- Cannot ensure best price or collect platform fees
- Transaction takes several minutes (vs. couple seconds for regular Cooking trades)
- Violates the "speed mantra" of the platform

### 4. On-Ramp Decision: Crossmint vs. Standard KYC

**The Debate:**

**Greg's Initial Position:**
- Most users will fund from external wallets
- Checkout might be sufficient for edge cases (below minimum withdrawal)
- Minimal need for traditional on-ramp

**Lucas's Counter-Argument:**
> "If we're trying to go to the normies, to the person that doesn't actually own crypto or doesn't really know that much about crypto, which was the original user persona that we agreed on with this application, then that person wouldn't necessarily own Solana."

**Naji's Clarification:**
- Crossmint has both features (checkout and on-ramp)
- If using checkout, users don't KYC for meme coins but do for Solana
- Without Solana, users cannot sell meme coins
- Would feel like "trapping" users if only checkout offered

**Final Decision:**
- Proceed with standard KYC-based on-ramp
- Deprioritize Crossmint checkout feature
- Can revisit checkout later after core functionality delivered
- Focus on meeting September deadline with essential features

**Rationale:**
- Normie users need complete workflow (buy AND sell)
- Better to have working KYC flow than broken non-KYC flow
- Checkout is a "nice-to-have," not critical for launch
- Two-step process acceptable given timeline constraints

### 5. Mobile App Web Responsiveness Strategy

**Lucas's Proposal:**
- Block web app responsiveness on mobile devices
- Present redirect page recommending native app download
- Different redirect based on device (iOS App Store vs. Google Play Store)

**Reasoning:**
- Perpetuals UI too complex for responsive mobile web design
- Native app provides superior experience
- Complexity increasing, making mobile web impractical
- Simpler UX for users to use dedicated app

**Naji's Response:**
> "I don't see why we wouldn't [redirect], right? I don't see why we'd let them use a browser instead of the app."
> "I think that's the whole point of doing the app, right? It's making it all simpler."

**Decision:** Implement mobile redirect to native app once available

**Benefits:**
- Reduces web development scope
- Better user experience on mobile
- Allows focus on native app quality
- Standard practice for trading platforms

### 6. iOS App Store Requirements & Documentation

**iOS Compliance Requirements:**

1. **Account Deletion:**
   - Users must be able to delete their accounts
   - All cached information must be deletable
   - Implementation: Simple delete query

2. **Referral Chain Handling on Deletion:**

**Three Options Discussed:**

1. Keep tree intact, commissions apply as before, minus reward claiming
2. Lose chain entirely (rejected - doesn't make sense)
3. **Chosen approach:** Cooking takes unclaimed rewards, referral structure remains

**Example:** If User A invited B, B invited C, C invited D, and A deletes account:
- Unclaimed rewards from A's network go to Cooking treasury
- B, C, D referral chain remains intact
- Discount structure continues working for remaining users

3. **Help Documentation:**
   - iOS requires help link for users
   - Lucas to create GitBook documentation
   - Will use existing crypto trading Gmail account
   - Essential for App Store approval

**Decision:** GitBook will be primary documentation strategy

### 7. Go-to-Market Strategy & Geoblocking Issues

**The Challenge:**
- Hyperliquid is geoblocked in the United States
- North America is primary iOS market
- Legal complexity around perpetuals trading

**Comparison Example:**
- Naji used Bullx in UAE
- Pump.fun was blocked in UAE
- Still able to trade through Bullx
- Different mechanism than Hyperliquid situation

**Key Concerns:**

1. **Hyperliquid Availability:**
   - Not operating on US soil
   - Self-imposed US restriction
   - May require business licenses

2. **CFTC Requirements:**
   - Precedent exists for crypto sites integrating perpetuals/derivatives
   - May need CFTC certifications
   - Required for providing third-party integrated services

**Two Critical Questions:**
1. Will Hyperliquid work in the US at any point?
2. Do we need business licenses to operate perpetuals services?

**Action Required:**
- Legal team consultation essential
- Outside Ratherlab's scope
- Must investigate before US launch

**Lucas's Guidance:**
> "That is something that you guys should inquire your legal team because that is way out of our scope."

### 8. Let's Bank Integration Priority

**Context:** Naji asked about two-week timeline for Let's Bank integration mentioned previously.

**Current Status:**
- Already being worked on (not waiting for decision)
- Indexer engineer working on it proactively during available time
- Progress made throughout the week
- Expected completion: Following week

**Why Fast Progress:**
- Lucky architectural compatibility with Radium
- Ground work already laid
- Similar core structure to existing integrations
- Not representative of typical new protocol integration time

**Scope:**
- Indexer: Nearly complete
- Backend fallbacks: In progress
- Trading via Jupiter: Will be supported
- Native support: Full integration like other protocols

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Deprioritize Crossmint checkout | Creates dead-end for users without Solana | Can be added later post-launch |
| Proceed with KYC-based on-ramp | Normie users need complete buy/sell workflow | Better UX despite KYC friction |
| Redirect mobile web to native app | Perpetuals too complex for responsive design | Reduces web scope, better mobile UX |
| Use GitBook for documentation | iOS requires help link, quick to implement | Faster than building in-app help center |
| Cooking takes rewards on account deletion | Maintains referral chain integrity | Fair approach to abandoned accounts |
| Continue Let's Bank integration | Already in progress, architecturally compatible | Native support for growing platform |
| Defer Apple social login | Requires business account access | Google, Telegram, Twitter sufficient for launch |

## Action Items

### High Priority

- [ ] **Naji** - Confirm Crossmint checkout deprioritization with Riz (Due: Before Monday, July 14, 2025)
- [ ] **Lucas** - Create GitBook documentation for mobile app help center (Due: Ongoing, completion by July 25, 2025)
- [ ] **Legal Team** - Investigate Hyperliquid US geoblocking implications (Due: ASAP)
- [ ] **Legal Team** - Research CFTC requirements for perpetuals integration (Due: ASAP)

### Medium Priority

- [ ] **Backend Team** - Complete Let's Bank native integration (Due: Week of July 14, 2025)
- [ ] **Frontend Team** - Implement mobile web redirect to app download (Due: When mobile app available)
- [ ] **Backend Team** - Implement account deletion functionality per iOS requirements (Due: Before iOS submission)
- [ ] **Martin & Team** - Complete Google social login integration (Due: July 18, 2025)

### Low Priority

- [ ] **Team** - Research Crossmint checkout for potential future integration (Due: Post-launch)
- [ ] **Lucas** - Send weekly minutes email (Due: July 11, 2025)

## Technical Notes

### Crossmint Integration Options

**Widget Integration:**
- Embeddable web view within app
- Appears native to users
- Customizable styling (limited)
- Two options: hosted URL or embedded web view

**Headless API:**
- Full custom UI control
- Requires handling all edge cases:
  - Network errors
  - Bank approval failures
  - KYC issues
  - Multiple verification flows
- Significant development time
- Not feasible for September deadline

**Commercial Structure:**
- Premium plan required for needed customization
- Pricing not publicly available (requires sales call)
- Similar to Jupiter's approach

### Let's Bank Architecture

**Compatibility:**
- Similar to Radium protocol structure
- Database schema already compatible
- Faster integration than typical protocol

**Integration Scope:**
- Indexer: Token discovery and tracking
- Backend: Direct trading fallbacks
- Jupiter: Aggregated trading support
- Full native support planned

### Social Login Status

**Completed:**
- Telegram: Working on web and mobile

**In Progress:**
- Google: Backend work started

**Planned:**
- Twitter: Queued after Google
- Apple: Deferred until business account access

### Performance Considerations

**Crossmint Checkout Speed:**
- Traditional Cooking trade: 2-3 seconds
- Crossmint checkout: Several minutes
- Conflicts with platform's speed focus

**ClickHouse Performance:**
- Migration successful
- Significant performance improvement
- Production stable

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Hyperliquid US geoblocking | Cannot serve US market for perpetuals | Legal team investigation, potential licensing |
| CFTC certification requirements | Market access delays | Early legal consultation |
| Crossmint checkout creates user dead-ends | Poor UX without Solana | Deprioritize, focus on KYC on-ramp |
| September deadline pressure | Quality vs. speed trade-offs | Focus on core features, defer nice-to-haves |
| Apple business account delays | Cannot implement Apple social login | Use other providers, add Apple later |
| Mobile web complexity | Development time drain | Redirect to native app instead |

## Next Steps

1. **Immediate:** Naji to confirm Crossmint decision with Riz
2. **This Week:** Complete Let's Bank integration
3. **This Week:** Lucas begins GitBook documentation
4. **Next Week:** Legal team provides guidance on Hyperliquid/CFTC
5. **Ongoing:** Continue mobile app development
6. **Before iOS Launch:** Implement account deletion and help documentation

## Key Metrics & Numbers

- **Timeline to deadline:** ~11 weeks to end of September
- **Social login providers:** 4 planned (Telegram ✓, Google in progress, Twitter, Apple deferred)
- **Let's Bank integration:** ~1 week (accelerated due to architecture compatibility)
- **Crossmint transaction time:** Several minutes (vs. 2-3 seconds for Cooking)
- **Jupiter tokens:** Tradable by mid-next week

## References

- Crossmint - On-ramp/checkout provider
- FOMO app - Example using Crossmint checkout
- Let's Bank - New AMM being integrated
- Hyperliquid - Perpetuals provider (US geoblocked)
- CFTC - Commodity Futures Trading Commission
- Bullx - Competitor platform reference
- GitBook - Documentation platform choice

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
