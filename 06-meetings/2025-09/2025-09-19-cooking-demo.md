---
title: Cooking Demo - Market Orders Complete, Video Demo & Hyperliquid Integration
date: 2025-09-19
type: demo
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Naji Osmat
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Marcos Tacca
  - Shakeib Shaida (shak@ember.app)
status: completed
tags:
  - demo
  - perpetuals
  - hyperliquid
  - market-orders
  - limit-orders
  - video-demo
  - performance
related:
  - "[[2025-09-12-cooking-demo]]"
  - "[[2025-09-26-cooking-demo]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team demonstrated major progress toward beta readiness, with perpetuals market orders 95% complete and comprehensive performance improvements implemented. Loading times improved dramatically from 30 seconds to 1-1.5 seconds through ClickHouse optimizations. Lucas provided a live demonstration of Hyperliquid perpetuals functionality, including opening/closing positions, position history, and trade history. Key discussions focused on addressing incorrect PNL and portfolio valuation data, implementing token supply tracking for market cap calculations, and preparing for video demo recording. A three-week timeline was established to complete all development work, with production deployment requiring a Hyperliquid referral code.

## Meeting Details

**Duration:** 38 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Backend Development Progress

**Hotkey Implementation:**
- Implementation complete (100%)
- Navigation hotkeys fully functional
- Not user-customizable in current version

**Bug Fixes Completed:**
- Search behavior errors resolved
- Jupiter token search errors fixed
- Bug when linking Solana account as fallback login method (when another method exists) - fixed
- Internal errors when executing orders on Jupiter and Moonshot - resolved

**Perpetuals Market Orders (95% Complete):**
- Order creation functionality
- Order closing functionality
- Leverage updating
- SOL to USDC conversion and deposit
- History tables: order history, funding history, position tables
- Bug fix: Incorrect data fetching when perpetual page kept open for extended time
- Remaining: Two incorrect values being actively fixed

**External Solana Wallet Support:**
- Importing external Solana wallets (Phantom, etc.) - backend complete
- Cooking tag implementation - backend complete
- Frontend work still in progress

### 2. Performance Optimization Achievements

**ClickHouse Improvements:**
- Testing improvements made to ClickHouse
- Initial bottleneck suspected in Redis
- Redis updated to resolve initial performance issues
- Load balancer issue resolved with update

**Query Optimization:**
- Actively fixing ClickHouse queries
- Focus: Bar data for charts
- Focus: Token metrics (market cap, liquidity calculations)
- Ensuring accurate processed data delivery

**Loading Time Improvements:**
- **Before:** ~30 seconds
- **After:** 1-1.5 seconds on average
- Martin: "Night and day difference"
- Required significant work from two engineers across multiple fronts

**Impact:**
- Dramatic user experience improvement
- Charts load quickly and smoothly
- Token details display rapidly

### 3. Frontend Development Updates

**Perpetuals UI:**
- Integrating and testing limit orders
- Will complete all perpetuals functionality

**Token Details:**
- Advanced orders integration in progress
- Closely linked with form components
- Testing ongoing

**Referral Program:**
- Page implementation in progress
- UI development for multi-level referral system

### 4. Indexer Improvements & Data Quality

**Token Supply Tracking:**
- Paramount for market cap calculation
- Paramount for chart metrics accuracy
- Algorithm previously only worked for new tokens (pre-Jupiter integration)
- Now modified to include Jupiter tokens
- Eliminates data discrepancies
- Enables market cap display on Y-axis of charts

**Critical Data Fixes:**
- Incorrect portfolio PNL calculation (raised by Naji) - being tested
- Incorrect portfolio invested valuation on Pengu and launchpad tokens - being tested
- Issue: Data indexing problem from Jupiter
- Solution: Making test purchases to track value movements over multiple days
- Verification: Ensuring accurate tracking before marking complete

**USDC/USDT Data:**
- Missing data issue resolved
- Now populating correctly

**ClickHouse Replica Improvements:**
- Performance enhancement as part of overall optimization work

### 5. Chart Data Anomalies Explanation

**The "Strange Lines" Issue:**

**Root Cause (Lucas explanation):**
- Not errors in values
- Liquidity removals from AMM pools
- When dev mints token, receives authority over token
- Dev can remove liquidity from pool (e.g., from Pump)
- Chart bar records this removal as price value
- Creates extreme vertical spikes in charts

**Industry Solution Discovery:**
- Research of Axium, Photon, and other platforms
- Finding: They hide these liquidity removal values
- Effect: Smooths out price curve
- Trade-off: "Fakes" the actual valuations

**Implementation Decision:**
- Team working on filter for outliers in indexer
- Will emulate Axium's behavior
- Gregory's position: "If Axium doesn't care, we shouldn't care"
- Approach: Filter can be removed if issues arise
- One backend engineer fully focused on implementation
- Expected completion: End of day September 19

**Technical Note:**
- These are liquidity removals, NOT transactions
- Filtering could have detrimental effect on some users
- Unclear impact on users executing through Echo or similar platforms
- Implementing with ability to reverse if needed

### 6. Mobile Development Status

**Pending Testing:**
- Referral system implementation
- Portfolio and positions integration
- Token details
- Trading operations

**All pending Apple account access for mobile testing**

### 7. Hyperliquid Perpetuals Live Demonstration

**Context:**
- Lucas demonstrated live perpetuals trading on Hyperliquid
- Using test account for demonstration
- Note: User not linked to referral code (not paying fees)

**Opening a Long Position:**
- Demo: Opening long position on BTC
- Notional value: ~$100 USD
- Order hits Hyperliquid endpoint directly
- Position created successfully

**Position Display:**
- Shows BTC amount (e.g., 0.0086 BTC)
- Notional value: $99.73
- Entry price displayed
- PNL (Profit and Loss) calculation
- Liquidation price (calculated by Hyperliquid)

**Closing Positions:**
- Partial close capability (e.g., 50% of position)
- Full close capability
- Updates reflected immediately
- Freed margin available for new trades

**Position History Tab:**
- All positions created and closed
- Complete position tracking

**Funding History Tab:**
- Shows funding cycles
- Displays payments made/received
- Based on oracle vs mark price difference

**Order History Tab:**
- Shows all executed orders
- Per-position order tracking

**Trade History Tab:**
- Comprehensive trade log
- All transactions recorded

**Asset Selection:**
- Filter by specific tokens/contracts
- Order book per asset
- Example: Can trade SOL, other Hyperliquid-supported tokens

**Pending Implementation:**
- Open Orders tab (needed for limit orders testing)
- Shows orders waiting to hit market
- Critical for properly testing limit orders

### 8. Visual Updates Roadmap

**After Current Functionality Complete:**
- Update entire domain visual interface
- Modify selector components
- Update button designs
- Update form elements
- Implement quick and slow conversion flows

**Testing Remaining:**
- Quick conversion (fast mode)
- Slow conversion (batch mode)
- End-to-end perpetuals workflow

### 9. Hyperliquid Referral Code Requirements

**For Production Deployment:**
- Need referral code from Naji/Zen
- Required to link users to Cooking
- Currently testing without referral (no fees paid)

**Wallet Setup Discussion:**

**Naji's Question:**
- For cold wallet: Does it require Arbitrum bridge?
- Or can Hyperliquid wallet be cold wallet directly?

**Lucas's Explanation:**
- Hyperliquid operates on own Layer 2 (HyperVM)
- Must top up HyperVM account with USDC on Arbitrum
- Can also top up with other supported tokens on Arbitrum
- Supported tokens: USDC, USDT, ETH, and others shown in interface

**Zen's Question:**
- Can someone just send USDC directly to wallet?
- Answer: Yes, can top up with any supported token on Arbitrum

**Referral Code Volume Requirement:**
- Need 10,000 USD notional trading volume
- Can achieve with ~$70 USD at maximum leverage
- Example: $70 at 40x leverage on Bitcoin
- Process: Open and close position = 10,000 volume achieved

**Clarification (Naji):**
- Just need ~70 bucks with max leverage on Bitcoin
- Open position then close it
- Achieves required volume for referral code

**Balance Requirement (Martin):**
- Need to maintain ~100 USDC balance on wallet
- Required for builder code

**Onboarding Options:**
- Any EVM wallet sufficient
- Need USDC + small amount of ETH for Arbitrum gas
- Can also transfer from Solana
- User's choice of method

**Weekend Action:**
- Zen requested steps from Naji
- Plans to complete Hyperliquid wallet setup over weekend

### 10. Development Timeline & Completion

**Three-Week Timeline:**
- Complete all development work
- Product will be testable end-to-end
- NOT ready for end users yet
- Testing and bug fixes will follow

**Gregory's Clarification:**
- Development done = ready for testing
- Not deployment-ready for users
- Testing phase to follow development completion

**Monday Video Demo Requirements:**

**Zen's Question:**
- Will ClickHouse improvements enable proper video recording?

**Gregory's Requirements:**
1. ClickHouse improvements (performance)
2. Incorrect PNL data fixed
3. Inverted portfolio data fixed
4. Token supply tracking functional (for chart demos)

**Lucas's Commitment:**
- Work to stabilize spot side
- Focus on perpetuals testing in parallel
- Target: Complete by Monday for video recording

**Production Environment:**
- No production environment available before end-of-month deadline
- Martin: Prefer to focus completely on finishing for deadline
- Production deployment will come after deadline met

### 11. Documentation & Remaining Items

**GitBook Documentation:**
- Lucas working on first version
- Will share with team today or Monday
- Need to update plan for custom URL
- Otherwise will be "gitbook-cooking" or similar

**Social Links Still Needed:**
- Hyperliquid Twitter account link
- Discord account link
- Needed for: login screen and navigation bar

### 12. Contract Updates Discussion (End of Meeting)

**Participants:** Zen, Gregory, Shakeib

**Context:**
- Changes needed in contract
- Low stakes weren't working
- Liquidity pool had low funds

**Zen's Concern:**
- Doesn't understand what changes are needed
- Role is custody and management, not development
- Needs to understand changes before implementing
- Not internal development, so extra scrutiny needed

**Action:**
- Call scheduled for that night
- Update contract values
- Continue testing after updates

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Implement liquidity removal filter | Industry standard approach (Axium, Photon) | Smoother charts, better UX |
| Filter can be removed if issues arise | Uncertain impact on some edge cases | Reversible decision |
| Video demo targeted for Tuesday | Monday completion of fixes | Need all items from Gregory's list |
| No production environment until end of month | Focus on deadline completion | Development environment only |
| Three-week development timeline | Realistic based on remaining work | Testing phase to follow |
| Cold wallet must bridge from Arbitrum | Hyperliquid architecture requirement | Additional user onboarding step |
| GitBook Pro plan annual subscription | Professional documentation platform | Cost to be invoiced |
| Update contract values tonight | Testing blocked by current issues | Shakeib and Zen call scheduled |

## Action Items

### High Priority

- [ ] **Backend Engineer** - Complete liquidity removal filter implementation (Due: September 19, 2025, EOD)
- [ ] **Lucas/Team** - Fix incorrect PNL data (Due: September 21, 2025)
- [ ] **Lucas/Team** - Fix inverted portfolio data (Due: September 21, 2025)
- [ ] **Lucas/Team** - Complete token supply tracking (Due: September 21, 2025)
- [ ] **Naji** - Send Hyperliquid wallet setup steps to Zen (Due: September 20, 2025)
- [ ] **Zen** - Complete Hyperliquid wallet setup over weekend (Due: September 21, 2025)
- [ ] **Naji/Zen** - Provide referral code for production (Due: September 26, 2025)
- [ ] **Zen/Shakeib** - Update contract values (Due: September 19, 2025 night)

### Medium Priority

- [ ] **Lucas** - Share GitBook documentation with team (Due: September 19-21, 2025)
- [ ] **Lucas** - Update plan for GitBook custom URL (Due: September 26, 2025)
- [ ] **Gregory/Zen** - Provide Hyperliquid Twitter account link (Due: September 26, 2025)
- [ ] **Gregory/Zen** - Provide Discord account link (Due: September 26, 2025)
- [ ] **Lucas** - Research and suggest CRM solution for CS team (Due: September 21, 2025)
- [ ] **Gregory** - Message Zen about video demo coordination (Due: September 21, 2025)
- [ ] **Naji/Gregory** - Record cooking video demo (Due: September 23, 2025)

### Low Priority

- [ ] **Team** - Complete remaining perpetuals visual updates (Due: September 26, 2025)
- [ ] **Team** - Test quick and slow conversion flows (Due: September 26, 2025)

## Technical Notes

### Performance Achievements
- Loading time reduction: 30 seconds → 1-1.5 seconds
- ClickHouse query optimization
- Redis bottleneck resolution
- Load balancer update
- Multi-front optimization by two engineers

### Hyperliquid Architecture
- **Layer 2:** HyperVM (proprietary)
- **Top-up Required:** USDC on Arbitrum (or other supported tokens)
- **Supported Tokens:** USDC, USDT, ETH, and others
- **Gas:** Small ETH amount needed for Arbitrum transactions
- **Alternative:** Can transfer from Solana

### Referral Code Requirements
- **Volume:** 10,000 USD notional trading required
- **Method:** ~$70 at maximum leverage (40x on Bitcoin)
- **Process:** Open position → Close position = volume achieved
- **Balance:** Maintain ~100 USDC for builder code

### Token Supply Tracking Algorithm
- Previous: Only worked for new tokens
- Updated: Includes Jupiter tokens
- Impact: Accurate market cap calculations
- Enables: Market cap display on chart Y-axis

### Liquidity Removal Filtering
- Source: AMM pool liquidity removals by devs
- Problem: Creates extreme price spikes
- Solution: Filter outliers (Axium method)
- Implementation: Backend engineer dedicated
- Risk: Potential impact on some user scenarios
- Mitigation: Reversible implementation

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Incorrect PNL/portfolio data | Video demo blocked | Priority fix by Monday |
| Token supply tracking incomplete | Cannot demo charts properly | Priority fix by Monday |
| No production environment | Cannot share stable link to partners | Focus on deadline completion |
| Liquidity removal filter impact unknown | May affect some user experiences | Reversible implementation |
| Apple account access still blocked | Mobile testing delayed | Ongoing issue |
| Referral code not yet provided | Cannot deploy to production | Requested from Naji/Zen |
| Contract values causing test failures | Testing blocked | Night call scheduled to fix |
| Three-week timeline aggressive | Risk of deadline slip | Team focused, extra resources added |

## Next Steps

1. **Today (Sept 19):** Complete liquidity removal filter implementation
2. **Weekend:** Zen completes Hyperliquid wallet setup
3. **Monday (Sept 21):** Complete PNL, portfolio data, and token supply fixes
4. **Monday (Sept 21):** Share GitBook documentation
5. **Tuesday (Sept 23):** Record video demo (Naji and Gregory)
6. **This Week:** Stabilize spot functionality for demo
7. **Ongoing:** Continue perpetuals limit orders implementation
8. **Three Weeks:** Complete all development work for testing phase
9. **End of Month:** Production deployment with referral code

## Key Metrics & Numbers

- **Performance improvement:** 30 seconds → 1-1.5 seconds (95% reduction)
- **Market orders completion:** 95%
- **Development timeline:** 3 weeks to completion
- **Engineers on performance:** 2 dedicated resources
- **Hyperliquid referral volume required:** 10,000 USD notional
- **Minimum for referral volume:** ~$70 at max leverage
- **Builder code balance requirement:** ~100 USDC
- **Token supply tracking:** Now includes Jupiter tokens
- **Expected liquidity filter completion:** September 19, 2025 EOD

## References

- Axium, Photon (liquidity removal filtering approach)
- Hyperliquid (perpetuals integration)
- HyperVM (Hyperliquid Layer 2)
- ClickHouse (database optimization)
- GitBook (documentation platform)
- Arbitrum (Hyperliquid bridging chain)

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
