---
title: Cooking Demo - Position Updates & Production Readiness
date: 2025-10-03
type: demo
attendees:
  - Lucas Cufré
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Martin Aranda
  - Naji Osmat
  - Marcos Tacca
  - Shakeib Shaida (shak@ember.app)
status: completed
tags:
  - demo
  - position-updates
  - performance-optimization
  - perpetuals
  - apple-account
  - onramper
related:
  - "[[2025-09-26-cooking-demo]]"
  - "[[2025-10-10-cooking-demo]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

Lucas reported a major improvement in position update times, reducing the delay from 5 minutes to 10-20 seconds through a quick fix, though a full refactoring remains in progress due to RPC downtime issues. Platform updates include user settings with social login methods, backup options, and completion of advanced orders refactoring. The team is finalizing perpetuals implementation, with only custom referral codes needed for production deployment. Critical blockers include Apple account issues (Gregory's personal account was disabled) and ongoing Onramper KYC investigation.

## Meeting Details

**Duration:** 27 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Position Update Performance Improvement

**Context:** The team addressed critical position update latency issues affecting user experience.

**Key Points:**
- **Previous state:** Position updates taking 5 minutes
- **Current state:** Reduced to 10-20 seconds (interim solution)
- **Target state:** Full refactoring pending for optimal performance
- **Root cause:** RPC downtime prevented implementation of complete refactor
- **Implementation:** Quick optimization deployed as temporary fix for video demonstration

**Technical Impact:**
- Database crash occurred during initial optimization attempt
- Changes rolled back and implemented more conservatively
- Data duplication issues resolved
- Full refactoring still in progress

**Key Quote:**
> "Yesterday I did an optimization to make the time faster and it took down the whole database. Yeah, it was a hell of a day yesterday." - Lucas Cufré

### 2. Platform Updates & User Interface

**User Settings Completed:**
- Social login methods fully tested and implemented
- User can create account with preferred social method (becomes default)
- Fallback methods available: Solana wallet or other listed options
- Detaching from one method makes it available for new account creation
- Keyboard shortcuts for platform navigation
- Security password feature for critical transactions

**Advanced Orders Refactoring:**
- Final refactoring being pushed to production
- Latest design implementation in progress

**Portfolio View Updates:**
- Pending latest design from Leo
- Current tables using legacy design
- Only awaiting design update to complete implementation

### 3. Kitchen Feature Updates

**Badge System Implementation:**
- New badge design across all token cards
- Token detail tables now display:
  - Wallet star status
  - Top 10 holders
  - Diamond hands designation
  - Sniper identification
  - Dev wallet tracking
  - Buy/sell timestamps for different wallet categories

**Performance Note:**
- Dev environment has lower resources than production to manage costs
- Vercel development environment is expensive if fully resourced
- Some rendering delays expected in dev but will be faster in production

### 4. Perpetuals Implementation Status

**Current State:** Nearly complete, production-ready pending referral codes

**Blocker:**
- Custom referral codes required for production deployment
- Referral code ensures all Hyperliquid accounts created through Cooking are tracked as Cooking referrals
- Code requires $10,000 volume transaction to obtain
- This requirement discussed with Zen several weeks ago

**Current Workaround:**
- Using personal MetaMask account funded by Lucas for dev testing
- Dummy account validates proper implementation
- Production deployment will swap in proper referral code via environment variable

**Features Implemented:**
- Market orders: Complete
- Limit orders: Complete
- Ready for production once referral code obtained

**Action Required:**
- Zen to provide referral code (Due: Monday or Tuesday, per Naji)

### 5. Portfolio & Wallet Manager Enhancements

**Portfolio Design:**
- Tables updated to sleeker design
- Transfer transactions now auto-populate sender/recipient names
- External wallet transfers clearly labeled
- Transaction history shows:
  - Cooking wallet-to-wallet transfers (with named wallets)
  - External wallet transfers (labeled as external)
  - Developer wallet transactions (team members identified)

**Other Updates:**
- Customers page revamped
- Referral page redesigned
- Position modal updated
- Quick search with updated parameters for token sorting/searching
- Search results ordered by liquidity (confirmed by Naji)

### 6. Apple Account Critical Issues

**Problem:**
- Gregory's phone number blacklisted by Apple
- Personal Apple account disabled
- Lost 10,000+ photos and videos
- Multiple support attempts (50+ emails) unsuccessful
- Apple Pay disabled
- All digital payment cards inaccessible

**Impact on Project:**
- Unable to create company Apple Developer account as planned
- Phone number updated to Naji's number
- Naji has not received verification text

**Proposed Solution:**
- Martin suggested using RLABS company account for initial test version
- Test version won't be published, so company branding acceptable
- Once ready, transfer application to proper company account

**Concern:**
- Zen prefers no historical record of previous developers after transfer
- Lucas to research if Apple shows previous developer history post-transfer

**Decision:** Lucas will investigate Apple's transfer policies and report back

### 7. Onramper Integration Status

**Current Situation:**
- Lucas has not had time to set up Onramper account
- Needs to investigate KYC requirements
- Gregory has connections with Onramper team

**Questions:**
- Does Onramper require KYC?
- Can existing Telegram group be leveraged?

**Action Items:**
- Lucas to set up Onramper account and determine KYC requirements
- Naji to check if old Telegram group with Inside X still accessible

### 8. Inside X Monthly Payment

**Payment Details:**
- Monthly fee: 1,200 USDC/USDT
- Payment method: On-chain transfers only (per current understanding)
- Gregory exploring card payment option

**Action:**
- Gregory to ask Inside X group if card payment accepted instead of crypto

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Deploy 10-20 second position update fix | Enable video demonstration despite incomplete refactor | Temporary solution, full optimization still needed |
| Use RLABS account for initial iOS testing | Gregory's Apple account disabled | Enables testing while resolving account issues |
| Investigate Apple Developer account transfer policies | Ensure no developer history shown post-transfer | Protects brand reputation |
| Continue with Onramper integration | Preferred on-ramp solution | Pending KYC investigation |
| Prioritize referral code acquisition | Blocks perpetuals production deployment | Critical for Monday/Tuesday timeline |

## Action Items

### High Priority

- [ ] **Zen** - Provide Hyperliquid referral code ($10k volume requirement) (Due: Monday or Tuesday, October 7-8, 2025)
- [ ] **Lucas** - Research Apple Developer account transfer policies regarding developer history (Due: October 5, 2025)
- [ ] **Lucas** - Complete full position update refactoring (Due: End of day October 3, 2025)
- [ ] **Development Team** - Deploy stable version to production by end of day (Due: October 3, 2025)

### Medium Priority

- [ ] **Lucas** - Set up Onramper account and determine KYC requirements (Due: October 5, 2025)
- [ ] **Naji** - Check if old Inside X Telegram group still accessible (Due: October 4, 2025)
- [ ] **Gregory** - Ask Inside X if monthly fee can be paid via card instead of crypto (Due: October 4, 2025)
- [ ] **Lucas** - Push advanced orders refactoring to production (Due: October 3, 2025)

### Low Priority

- [ ] **Team** - Obtain latest portfolio design from Leo (Due: TBD)

## Technical Notes

### Position Update Optimization
- Quick fix implemented: 5 minutes → 10-20 seconds
- Full refactoring blocked by RPC downtime
- Database crash during aggressive optimization
- Conservative rollback successful
- Data duplication resolved
- Stable solution targeted for end of day

### Development Environment Constraints
- Dev environment intentionally under-resourced vs production
- Cost management strategy for Vercel environment
- Some performance delays expected in dev
- Production will have full CPU allocation

### Perpetuals Integration
- Market and limit orders complete
- Referral code system tested with personal account
- Environment variable approach for production swap
- No functionality blockers aside from referral code

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| RPC downtime prevented full refactoring | Position updates still slower than ideal | Interim fix deployed, full solution by EOD |
| Gregory's Apple account disabled | Cannot create company developer account | Using RLABS account for testing |
| Apple account transfer may show developer history | Brand reputation concern | Lucas investigating policies |
| Referral code not yet obtained | Blocks perpetuals production launch | Zen providing by Monday/Tuesday |
| Onramper KYC requirements unknown | May delay on-ramp integration | Lucas investigating |
| Database instability during optimization | Risk of production downtime | Conservative approach adopted |

## Next Steps

1. **Immediate:** Complete position update refactoring by end of day (Lucas - October 3)
2. **This Week:** Deploy stable version to production (Team - October 3)
3. **Next Week:** Obtain Hyperliquid referral code (Zen - October 7-8)
4. **Next Week:** Resolve Apple Developer account situation (Lucas/Gregory - October 7)
5. **Next Week:** Complete Onramper KYC investigation (Lucas - October 5)

## Key Metrics & Numbers

- **Position update improvement:** 5 minutes → 10-20 seconds (90%+ reduction)
- **Target:** Complete real-time updates (pending full refactor)
- **Apple account impact:** 10,000+ photos/videos lost (Gregory)
- **Referral code requirement:** $10,000 volume transaction
- **Inside X monthly fee:** 1,200 USDC/USDT
- **Support emails sent:** 50+ (Gregory to Apple)

## References

- Hyperliquid - Perpetuals integration provider
- Onramper - On-ramp solution (KYC investigation pending)
- Inside X - Service provider ($1,200/month)
- RLABS - Company account for temporary iOS testing
- Vercel - Development environment

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
