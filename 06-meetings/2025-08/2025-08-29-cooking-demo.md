---
title: Cooking Demo - AI Journal Development & TradingView Chart Demo
date: 2025-08-29
type: demo
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Naji Osmat
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Vadim Pleshkov
  - Varya Nekhina
  - Marcos Tacca
  - Shakeib Shaida (shakeib98@gmail.com)
status: completed
tags:
  - demo
  - ai-journal
  - tradingview-integration
  - bubble-maps
  - apple-account
  - drocks-collaboration
  - chart-performance
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

Team established collaboration framework with Drocks for AI journal development, with Shakib coordinating data access and communication. TradingView advanced charts successfully demonstrated pulling live Hyperliquid data with various timeframes and functionality. Inside X confirmed for bubble maps at $200/month but does not support Hyperliquid (not needed for perpetuals). Apple account issues resolved with plan to create new personal account and upgrade to organization. Team emphasized speed and performance optimization crucial for upcoming partner demos. Roadmap preparation requested for Monday excluding AI journal until timelines clarified.

## Meeting Details

**Duration:** 47 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. AI Journal Development Framework

**Context:** Offloading AI journal development to Drocks team to meet September deadline.

**Team Structure:**
- **Drocks:** External AI developers building journal features
- **Shakib:** Technical coordinator and research lead
- **Role:** Ensure compatibility, facilitate communication, provide data access

**Data Requirements:**
- **Shakib's Request:** Access to indexing data
  - Token prices
  - Candle data (OHLCV)
  - Protocol information
- **Purpose:** Accelerate AI journal development
- **Lucas's Response:** Will expose API with required data
- **Martin's Request:** Design document specifying exact requirements and interfaces

**Communication Setup:**
- Slack channel to be created for Drocks ↔ Cooking bilateral communication
- Shakib managing channel setup
- Clear interface documentation needed

**Strategic Rationale:**
- Reduce pressure on Lucas's development team
- Allow focus on core platform features
- Meet tight September deadline
- Shakib's prior experience makes him ideal coordinator

### 2. Apple Developer Account Resolution

**Persistent Problem:**
- Account locked in verification loop
- Cannot access developer portal
- Multiple email attempts failed (.com, cooking.gg, Gmail)
- "Unblock" → "Verify" → Email rejection → Loop repeats

**Proposed Solution:**
- **Gregory:** Create new personal Apple account (not business)
- **Process:**
  1. Set up personal developer account
  2. Publish app under personal name initially
  3. Upgrade to organizational account later
  4. Transfer to "Cooking" branding for App Store

**Considerations:**
- **Lucas:** Unsure if publisher can be changed after initial publication
- **Risk:** May need to go through Apple approval again
- **Gregory:** Acceptable risk; need to unblock testing immediately
- **Timeline:** End of day completion

**Alternative Attempts:**
- **Zen:** Try generating new email credentials
- **Status:** Will send new credentials to Greg after call for testing

**Critical Impact:**
- TestFlight deployment blocked for weeks
- QA testing cannot proceed
- September deadline at risk without resolution

### 3. Backend Development Progress

**Completed:**
- **Diamond Hands, Snipers, Insiders Badges:** Calculations migrated for table improvements
- **Inside X Research:** Identified as bubble maps provider
- **Referral Program:** Testing custom codes implementation
- **Referral Refactoring:** Multi-level tiering in progress

**Perpetuals Progress:**
- **Frontend Integration:** Finishing up
- **Active Testing:**
  - Builder code surcharges operational
  - Take profit / Stop loss configuration working
  - Full position closing functional
  - Partial position closing functional

**In Development:**
- **Slow Mode:** Batched deposit/withdrawal for Hyperliquid
- **Social Logins:** X (Twitter) and Solana wallet account linking/unlinking
- **Backend Testing:** All social login methods

**Frontend Updates:**
- **Bug Fixes:** Multiple issues resolved (not enumerated - "too many to list")
- **UI Updates Started:** Typography and color alignment with Leo's designs
- **Next:** Spacing and iconography (~80% completion target)
- **Heaviest Work:** Layout modifications (deferred)

**Indexer:**
- **Creator Badges:** Data migration in progress
- **Pump.fun Outage:** Addressed and resolved
- **Strategy Shift:** Direct protocol routing with Jupiter as fallback (not vice versa)

### 4. Transaction Routing Strategy Change

**Previous Approach:**
- Route to Jupiter first
- Fallback to direct protocol if Jupiter fails

**New Approach:**
- Route directly to protocol first
- Fallback to Jupiter if protocol fails

**Rationale:**
- **Jupiter Priority:** Launchpads prioritize Jupiter uptime over forked bots
- **Volume Concentration:** Jupiter represents ~80% of Solana transaction volume
- **Business Alignment:** Protocols notify Jupiter of breaking changes proactively
- **Reliability:** Jupiter more likely to stay operational during protocol issues
- **Pricing:** Direct protocol offers best pricing except for graduated tokens (100% bonding curve)

**Key Insight:**
- Having Jupiter as fallback (not primary) better for platform stability
- Aligns with launchpad business interests

### 5. Mobile App Referral Program Integration

**Status:** Active integration in progress

**Features:**
- Custom code creation
- QR code scanning
- Visible during login phase (high user visibility)
- Security password creation (forced during onboarding)
- Notification permissions request

**Flow:**
- User login → Referral program → Security password → Notifications → Welcome → Home

**Next Steps:**
- Wallet page development continuing
- Vadim completing referral program designs next week

### 6. TradingView Chart Demonstration

**Martin's Demo:**
- **Data Source:** Hyperliquid pricing data
- **Backend Flow:** Hyperliquid → Cooking backend → Frontend
- **Chart Type:** Advanced TradingView integration

**Functionality Shown:**
- Multiple timeframes (1m, 5m, 15m, 30m, 1h, etc.)
- All standard TradingView features
- Live data updates
- Asset switching (SOL/USD, ETH/USD, BTC/USD)
- Drawing tools and indicators

**Performance:**
- Some initial loading delay (~10 seconds on Martin's screen)
- Skeleton loading timeout issue identified
- **Critical:** Speed and performance must improve for partner demos
- **Gregory's Emphasis:** First impressions crucial with partners next week

**Naji's UI Suggestion:**
- Replace timeframe dropdown with tabs
- Easier toggling between timeframes
- Standard pattern in centralized exchanges
- **Team Response:** Will check if TradingView library supports tab layout
- Cooking embeds TradingView library (limited customization)

### 7. Advanced Orders UI Review

**Lucas's Screen Share:**
- Advanced orders form with multiple order types
- **Problem:** Leo's tab design doesn't scale to 5+ order types
- **Current Solution:** Dropdown selector for order types
  - Market
  - Limit
  - DCA (Dollar Cost Averaging)
  - TWAP (Time-Weighted Average Price)
  - VWAP (Volume-Weighted Average Price)
  - Custom

**Custom Orders Complexity:**
- Most complex scenario: All parameters possible simultaneously
- **Parameters:**
  - Holding period
  - Average holding time
  - Price change percentage
  - Liquidity amount
  - Holders count
  - 10 holders percentage
  - Limit/Market selection
  - TTL (Time To Live)
  - Take Profit
  - Stop Loss

**Design Challenge:**
- Infinite tabs not practical for traders
- Dropdown more efficient for quick selection
- Leo's proposal doesn't accommodate all scenarios

**Additional Context:**
- Chart data for token being traded shown (important for decision-making)
- Users need chart visibility while setting up orders
- Split-screen workaround if no chart: Poor UX

### 8. Bubble Maps Pricing & Support

**Shakib's Clarification:**
- **Integration Pricing:** $200/month fixed for unlimited access
- **Consumer Pricing:** $25k/year (different tier)
- **Lucas's Confusion:** Initially saw token-based pricing ($300/month)
- **Resolution:** $200/month correct for integration

**Supported Protocols:**
- **Solana:** Yes ✅
- **Hyperliquid:** No ❌ (on roadmap)

**Gregory's Question:**
- Does lack of Hyperliquid support block anything?

**Team Response:**
- **No:** Bubble maps only for spot trading
- **Perpetuals:** Don't need bubble maps
  - Order book system
  - Central counterparty
  - No holder distribution to visualize
- **Naji:** Not important for perpetuals at all

**Decision:** Proceed with Inside X at $200/month for spot trading only.

### 9. TradingView Paid Version Upgrade

**Decision:** Upgrade immediately (don't wait for go-live)

**Reasoning:**
- **Cost:** $25k/year
- **By September:** Maximum ~$6k spent
- **Benefit:** Eliminate unknowns and potential "fuckups"
- **Gregory:** Rather pay $5-6k now than face issues later

**Action Items:**
- **Lucas:** Contact TradingView rep (Joe) to schedule upgrade call
- **Naji:** Attend call to ask questions directly
- **Zen:** Coordinate payment with Riz
- **Naji:** Provide payment addresses to Zen

**Joe (TradingView Rep) Context:**
- Has been "pushy" about seeing integration
- Wants to verify proper implementation
- May showcase if high quality
- Team delaying showing until satisfied with quality

### 10. Design Communication with Leo

**Gregory's Direction:**
- Identify design elements not aligning with product logic
- Communicate to Leo urgently (Figma comments or separate file)
- Fast communication essential (Leo working on mobile simultaneously)

**Rizvi's Addition:**
- Quick, clear communication critical to avoid rework
- Leo building mobile from scratch
- Sooner he knows issues, sooner adjustments made

**Lucas's Plan:**
- Update internal library to Leo's latest design decisions
- Clone Leo's version for modifications
- Show proposal screen with modifications
- Communicate misalignments to Leo
- Send minutes with latest agreements and roadmap

### 11. Roadmap Preparation

**For Monday Call:**
- Prepare next roadmap
- **Exclude AI journal for now** (timelines still being defined)
- Team has mutual understanding AI journal in parallel
- Not included in main roadmap until scope/timeline clear

**Gregory's Note:**
- Hard deadlines set with AI developers
- Still working to original September timeline
- Provides leeway for Lucas's team

### 12. AWS CPU Usage Monitoring

**Issue:** CPU usage spikes identified on AWS

**Solution:**
- Implement developer console alerts
- **Cost:** ~$80/month
- **Purpose:** Debug performance issues
- **Timeline:** Expect resolution within one month

**Team Approval:** Zen approved; proceed with implementation

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Drocks develops AI journal features | Meet September deadline; reduce pressure on Lucas's team | Shakib coordinates; API exposure needed |
| Create new personal Apple account | Unblock TestFlight testing after weeks of issues | Gregory to complete by end of day |
| Upgrade to TradingView paid version now | Eliminate unknowns (~$6k by Sept vs $25k/year) | Lucas to schedule call with Joe; Zen coordinates payment |
| Inside X for bubble maps ($200/month) | Spot trading only; Hyperliquid not needed | Solana support sufficient for beta |
| Direct protocol routing with Jupiter fallback | Better reliability; aligns with launchpad priorities | More stable transaction routing |
| Communicate design misalignments to Leo urgently | Avoid rework; Leo building mobile concurrently | Lucas to update library and show proposal |
| Implement AWS CPU monitoring ($80/month) | Debug performance issues | Expected resolution within one month |
| Exclude AI journal from Monday roadmap | Timelines not yet finalized | Mutual understanding it's in parallel |

## Action Items

### High Priority

- [ ] **Shakib** - Set up Slack channel for Drocks/Cooking communication (Due: August 30, 2025, immediately after call)
- [ ] **Lucas** - Expose indexer API for Drocks (token prices, candles, protocols) (Due: August 31, 2025)
- [ ] **Martin** - Send design document requirements to Shakib for API interface (Due: August 31, 2025)
- [ ] **Gregory** - Create new personal Apple developer account (Due: August 29, 2025, end of day)
- [ ] **Zen** - Send new Apple account email credentials to Gregory (Due: August 29, 2025, after call)
- [ ] **Lucas** - Contact TradingView rep (Joe) to schedule paid upgrade call (Due: August 30, 2025)
- [ ] **Naji** - Attend TradingView call to ask questions directly (Due: Scheduled TBD)
- [ ] **Zen** - Coordinate TradingView payment with Riz (Due: September 2, 2025)
- [ ] **Naji** - Provide payment addresses to Zen (Due: August 30, 2025)
- [ ] **Lucas & Team** - Optimize chart speed and loading for partner demos (Due: September 5, 2025, CRITICAL)

### Medium Priority

- [ ] **Lucas** - Update library to Leo's latest designs and show modified proposal (Due: September 2, 2025)
- [ ] **Lucas** - Communicate design misalignments to Leo (Due: September 2, 2025)
- [ ] **Lucas** - Send meeting minutes and roadmap to Leo (Due: August 30, 2025)
- [ ] **Lucas** - Prepare next roadmap excluding AI journal (Due: September 2, 2025, for Monday call)
- [ ] **Vadim** - Complete referral program designs (Due: September 5, 2025)
- [ ] **Team** - Implement AWS CPU usage alerts ($80/month) (Due: September 5, 2025)

### Low Priority

- [ ] **Team** - Check if TradingView supports tab layout for timeframes (Due: September 5, 2025)
- [ ] **Lucas** - Explore Inside X Hyperliquid support timeline (Due: Q4 - if needed)

## Technical Notes

### API Exposure for Drocks
- Shakib needs: Token prices, candle data, protocol info
- Indexer already has all data
- Design document required for explicit interface specification
- Accelerates AI journal development

### Transaction Routing Strategy
- **New:** Direct protocol → Jupiter fallback
- **Old:** Jupiter → Direct protocol fallback
- **Reason:** Jupiter represents 80% Solana volume; launchpads prioritize Jupiter uptime
- **Pricing:** Direct best except graduated tokens (100% bonding curve)

### TradingView Embedding
- Limited customization (embedded library)
- Team hostage to TradingView's allowed features
- Tab vs. dropdown for timeframes needs library support verification
- Performance critical for partner demos

### Advanced Orders Architecture
- 5+ order types (Market, Limit, DCA, TWAP, VWAP, Custom)
- Dropdown selector more practical than tabs
- Custom orders most complex (10+ parameters possible)
- Chart visibility essential while setting orders

### Bubble Maps Scope
- Inside X: $200/month unlimited
- Solana only (Hyperliquid on roadmap)
- Not needed for perpetuals (order book system)
- Spot trading visualization only

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Apple account verification loop | TestFlight testing blocked for weeks | New personal account being created today |
| Chart performance issues | Poor first impression with partners next week | Team prioritizing speed optimization |
| AI journal timeline uncertainty | Roadmap planning difficulty | Excluded from Monday roadmap; parallel development |
| TradingView customization limits | UX limitations (e.g., timeframe tabs) | Verify library capabilities; may need workarounds |
| AWS CPU spikes | Performance degradation | Implementing $80/month monitoring/alerts |
| Leo design misalignment | Rework if caught late | Fast communication; Lucas identifying issues ASAP |

## Next Steps

1. **Immediate:** Create Apple account; set up Drocks Slack channel; contact TradingView
2. **This Weekend:** Gregory follow-up call with Shakib on custody/security focus
3. **Next Week:** Optimize chart performance; complete referral program; expose API for Drocks
4. **Monday Call:** Review next roadmap (excluding AI journal)
5. **Ongoing:** AI journal development by Drocks; visual alignment with Leo's designs

## Key Metrics & Numbers

- **Time to deadline:** ~4 weeks (late August to end September)
- **TradingView paid version:** $25,000/year (~$6k by September)
- **Inside X bubble maps:** $200/month unlimited access
- **AWS monitoring alerts:** $80/month
- **Jupiter Solana volume:** ~80% of total Solana transactions
- **Chart loading time:** ~10 seconds (needs optimization)
- **Visual alignment target:** 80% match to Leo's designs
- **Order types supported:** 5+ (Market, Limit, DCA, TWAP, VWAP, Custom)

## References

- Drocks - External AI journal development team
- Shakib Shaida - Technical coordinator for AI features
- Inside X - Bubble maps provider (Solana only)
- TradingView - Advanced charting library
- Joe - TradingView sales representative
- Jupiter - Solana transaction aggregator (~80% volume)
- Leo - Lead designer (Cooking web and mobile)

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
