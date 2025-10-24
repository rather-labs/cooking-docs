---
title: Cooking Demo - October 24, 2025
type: meeting-note
date: 2025-10-24
attendees: [Lucas Cufré, Martin Aranda, Zen, Gregory Chapman, Naji Osmat, Shakeib Shaida (Shak), Marcos Tacca]
meeting-type: demo
tags: [demo, qa, bsc-integration, beta-launch, p&l-cards, onramper]
summary: |
  Weekly demo covering QA status update, BSC integration strategy discussion,
  P&L card requirements, and beta launch preparation. Major decision to pursue
  custom indexer route for BSC support. Most frontend issues expected resolved
  by Monday with 80-90% completion rate.
related-docs:
  - ../05-research/bsc-integration-strategy.md
  - 2025-10-24-daily-standup.md
---

# Cooking Demo - October 24, 2025

**Date:** 2025-10-24
**Time:** 11:27 AM GMT-03:00
**Attendees:** Lucas Cufré, Martin Aranda, Zen, Gregory Chapman, Naji Osmat, Shakeib Shaida (Shak), Marcos Tacca
**Facilitator:** Lucas Cufré

## Executive Summary

Lucas Cufré provided comprehensive updates on issue resolution efforts, noting that the majority of issues are minor frontend items with 80-90% expected to be resolved by Monday. A critical issue with linking social accounts was resolved the previous day and is already fixed in development. The team is preparing a batch of fixes for production deployment, including security password validation improvements.

The meeting included significant discussion on BNB (BSC) support strategy, prompted by Axiom's recent BNB chain integration. After evaluating options including The Graph and custom solutions, the team reached consensus to pursue a custom indexer route due to latency concerns and real-time data requirements. Martin Aranda and team will prepare a detailed document with research findings and time estimates by end of day.

Gregory Chapman raised concerns about missing P&L cards, which Leo is now working on, and Zen questioned the QA process given that basic items were not caught earlier despite QA reportedly finishing the previous Friday. Lucas explained that one QA engineer is on leave, requiring him to pick up additional QA responsibilities while balancing other work.

Additional topics covered included on-call engineer arrangements for 24/7 support once real users are onboarded, OnRamper approval delays despite charging for service, and agreement needed on initial metrics for PostHog integration.

## Action Items

- [x] **Resolve linking social accounts issue** - Assigned to: Backend Team - Due: 2025-10-23 - Priority: High - **Status: Completed**
- [ ] **Fix 80-90% of frontend issues** - Assigned to: Frontend Team - Due: 2025-10-28 (Monday) - Priority: High
- [ ] **Create BSC integration research document with time estimates** - Assigned to: Lucas Cufré, Martin Aranda - Due: 2025-10-24 EOD - Priority: High
- [ ] **Re-record and send video to Zen** - Assigned to: Lucas Cufré - Due: 2025-10-24 (within couple hours) - Priority: High
- [ ] **Send next roadmap information email** - Assigned to: Lucas Cufré - Due: 2025-10-24 - Priority: Medium
- [ ] **Resurface metrics integration email for PostHog approval** - Assigned to: Lucas Cufré - Due: 2025-10-24 - Priority: Medium
- [ ] **Contact OnRamper about approval and charges** - Assigned to: Gregory Chapman - Due: ASAP - Priority: High
- [ ] **Complete P&L card designs (proper desktop version)** - Assigned to: Leo - Due: ASAP - Priority: High
- [ ] **Deploy batch of fixes to production** - Assigned to: DevOps/Backend - Due: 2025-10-25 - Priority: High
- [ ] **Side-by-side speed comparison testing** - Assigned to: Zen - Due: 2025-10-29 (Tuesday) - Priority: Medium

## Index

1. Issue Resolution Status Update
2. Frontend and Backend Task Breakdown
3. QA Process and Resource Constraints
4. P&L Cards Missing Functionality
5. BNB/BSC Support Strategy Discussion
6. Indexer Solution Options and Decision
7. On-Call Engineers and 24/7 Support
8. OnRamper Integration Blockers
9. Metrics Integration (PostHog)
10. Testing Plans and Platform Comparisons

---

## Topics: Breakdown

### Topic 1: Issue Resolution Status Update

#### Executive Summary
Lucas provided a comprehensive update on current issues, noting that many are minor frontend items with most expected to be resolved by Monday. A major issue with linking social accounts was resolved the previous day and is already deployed to development environment.

#### Key Takeaways
- Major social account linking issue resolved within 24 hours (fixed in dev)
- Security password validation issue resolved and awaiting production deployment
- Backend issues are minimal compared to frontend
- Batch of fixes prepared for production deployment
- 80-90% of frontend issues expected fixed by end of Monday (October 28)
- Many issues are minor UI adjustments (pixel-perfect design compliance)

#### Discussion Details
**Issues Breakdown:**
- Most issues are frontend-related (backend nearly complete)
- Many flagged items are very minor (e.g., avatar size 34x34 pixels, column width adjustments)
- Some issues were already detected and in progress before latest review
- Current status: 8 in testing, 7 in progress, 23 reported, 5 already done

**Completed Fixes:**
- Hiding stable coins in specials mode
- DCA disclaimer implementation
- Indexer-related improvements

**Longer Timeline Items:**
- Error message normalization (requires new utility)
- Number representation definition updates (need to apply new rounding standards across all instances)

---

### Topic 2: QA Process and Resource Constraints

#### Executive Summary
Zen raised concerns about the QA process after basic issues were missed despite QA reportedly finishing the previous Friday. Lucas explained that one of two QA engineers is on leave due to family emergency, requiring him to cover QA tasks while managing other responsibilities.

#### Key Takeaways
- One QA engineer on leave (family member hospitalized)
- Lucas covering QA tasks in addition to other responsibilities
- Some issues were already detected but not all
- QA was reported complete on Friday but additional issues found Wednesday/Thursday
- Team acknowledges some items should have been caught earlier
- Gregory and Naji performing stringent testing to catch high-level issues

#### Discussion Details
**QA Team Status:**
- Two QA engineers total (down to one active)
- Lucas picking up slack but not full-time on QA
- Many issues from latest review overlap with already-flagged items
- Some genuinely new issues found that should have been caught

**Testing Strategy:**
- Gregory Chapman, Naji Osmat, Ali, and Shakib performing rigorous testing
- Focus on catching issues before wider release to Rob and other users
- Weekend testing planned to continue pressure on development team

---

### Topic 3: P&L Cards Missing Functionality

#### Executive Summary
Gregory Chapman identified missing P&L (Profit & Loss) cards as a critical gap, noting this is a basic feature users will notice. Leo's initial designs were incorrect (mobile-only, showing charts rather than P&L data), requiring redesign.

#### Key Takeaways
- P&L cards currently missing from platform
- Leo's designs were inappropriate (mobile-only, chart-focused rather than P&L data)
- P&L cards are standardized designs (not complex)
- Critical for basic functionality and user expectations
- Leo messaged this morning and should be working on corrections
- Need both desktop and mobile versions

#### Discussion Details
**Design Issues:**
- Leo only created mobile version
- Designs showed graphs and referral codes instead of profit/loss data
- P&L cards should display: profit/loss amounts, percentages, performance metrics
- Standard across industry, not complex design work

**Priority Rationale:**
- Basic feature users expect
- More noticeable than minor UI issues
- Essential for portfolio tracking
- Can't launch without it

---

### Topic 4: BNB/BSC Support Strategy Discussion

#### Executive Summary
Lucas initiated strategic discussion on BNB (Binance Smart Chain) support, prompted by Axiom's recent BNB integration and its massive memecoin ecosystem. Discussion identified three key technical points: indexer, wallet management, and routing service.

#### Key Takeaways
- Axiom integrated BNB, highlighting competitive need
- BNB has massive memecoin ecosystem (strategic opportunity)
- Three technical requirements: indexer (critical), wallet management (solved), routing service
- Wallet management already solved via Hyperliquid EVM integration (Turnkey)
- DEX aggregator options: 1inch (most mature), OpenOcean, PunkSwap, Rubik
- Indexer solution is most critical point requiring deep discussion
- Goal: Same level of support for BNB as Solana (all order types, bridging to Hyperliquid if supported)

#### Discussion Details
**Three Technical Requirements:**

1. **Indexer** (Most Critical)
   - Core discussion focus
   - Determines speed and reliability
   - Options: Custom vs ready-made solutions

2. **Wallet Management** (Solved)
   - Already handled via Turnkey integration
   - EVM compatibility proven with Hyperliquid (Arbitrum)
   - No expected issues

3. **Routing Service** (Multiple Options)
   - 1inch: Most mature, proven reliability
   - OpenOcean: Extensive coverage (second to 1inch)
   - PunkSwap, Rubik: Alternative options
   - Need to understand pricing and integration architecture

**Strategic Context:**
- Competitive pressure from Axiom
- Large market opportunity in BNB memecoin ecosystem
- Need feature parity with Solana support

---

### Topic 5: Indexer Solution Options and Decision

#### Executive Summary
Team evaluated two indexer approaches: custom-built vs The Graph. After discussion of latency concerns and real-time requirements, team reached consensus to pursue custom indexer route using a mature EVM indexer framework as foundation.

#### Key Takeaways
- **Decision: Custom indexer route chosen** (unanimous agreement)
- The Graph has latency issues unsuitable for real-time trading
- The Graph still requires custom work (subgraph building, maintenance)
- Martin researching mature EVM indexer framework for hybrid solution
- Hybrid approach: custom design on proven framework foundation
- Can integrate with ClickHouse (consistent with Solana architecture)
- Shak strongly favored custom route due to speed requirements
- Lucas and Martin to deliver research document with time estimates by EOD

#### Discussion Details
**Option 1: Custom Indexer (CHOSEN)**

*Pros:*
- Complete ownership and understanding
- Optimal performance for real-time requirements
- No external dependencies or outages
- Can optimize for specific use cases
- Consistent architecture with Solana (ClickHouse integration)

*Cons:*
- More development time
- Ongoing maintenance responsibility
- Must build from foundation (mitigated by using framework)

*Hybrid Strategy:*
- Use mature EVM indexer framework (not starting from scratch)
- Custom transaction interpretation
- ClickHouse integration (proven pattern from Solana)
- Fastest development route while meeting speed requirements

**Option 2: The Graph (REJECTED)**

*Pros:*
- Established solution for EVM indexing
- Handles storage infrastructure
- Some maintenance offloaded

*Cons:*
- **Latency issues** (deal-breaker for real-time trading)
- Good for dashboards/analytics, not high-speed trading
- Still requires custom work (subgraph building)
- Manual protocol support needed
- External dependency/potential outages
- Subscription costs
- Tied to their indexing speed and maintenance schedule

**Key Arguments:**
- Shak: "Latency issue... good for dashboard or analytics type tool but not good for the purpose we have right now"
- Martin: "The Graph is not an out-of-the-box solution... still need to do maintenance and support new protocols manually"
- Consensus: Speed requirements dictate custom solution

---

### Topic 6: On-Call Engineers and 24/7 Support

#### Executive Summary
Naji inquired about on-call engineer arrangements. Lucas confirmed agreement reached to implement 24/7 support with rotating on-call engineers once actual users are added to the platform.

#### Key Takeaways
- Agreement reached to add 24/7 on-call engineering support
- Will be implemented once actual users onboarded to platform
- "Working cards around the clock" to maintain uptime
- Proactive preparation for real user load

---

### Topic 7: OnRamper Integration Blockers

#### Executive Summary
Lucas raised critical blocker: OnRamper has charged $200 for essential plan but has not yet approved the integration, preventing end-to-end testing.

#### Key Takeaways
- OnRamper charged $200 for essential plan but hasn't given approval
- Blocking end-to-end testing capability
- Gregory Chapman to contact OnRamper directly (has direct channel)
- Critical for completing integration testing before beta launch

---

### Topic 8: Metrics Integration (PostHog)

#### Executive Summary
Lucas raised need for approval on initial metrics integration, proposing PostHog as an inexpensive solution. Will resurface previous email for team review and approval.

#### Key Takeaways
- PostHog proposed as metrics tracking solution
- Described as "pretty good solution that is pretty much inexpensive"
- Needs approval from Zen, Gregory, and Naji
- Lucas to resurface original email with follow-up for decision
- Important for tracking user behavior and platform performance post-launch

---

### Topic 9: Testing Plans and Platform Comparisons

#### Executive Summary
Zen and Gregory discussed ongoing testing efforts and plans for comprehensive platform comparisons. Zen returning Monday and will conduct side-by-side testing against competitors.

#### Key Takeaways
- Zen traveling, returning Monday midday
- Gregory and Naji also testing through weekend
- Initial impression: speed is good, overall feel slightly clunky but acceptable
- Not significantly slower than competitors (GMGN reference)
- Zen plans Tuesday side-by-side comparisons: Padre, GMGN, Axiom, Blex
- Testing focus: trade speed, chart loading, overall first impressions
- Important for Rob and new users who haven't seen product before
- Performance good until high user load (can't simulate yet)

#### Discussion Details
**Speed Assessment:**
- Current speed "quite quick" according to Gregory
- "Fractions of a second" differences vs competitors
- Not noticeably slower than GMGN
- Need side-by-side testing to quantify precisely

**Testing Methodology:**
- Side-by-side comparisons across multiple platforms
- Assess: trade settlement speed, chart load times, UI responsiveness
- Focus on first-time user experience
- Rob and team will provide fresh perspective (haven't used product before)

**Weekend Testing:**
- Gregory continuing to press Lucas and team through weekend
- Lucas previously committed to weekend work during handover
- Gregory will maintain pressure and report if unresponsive

---

## Decisions Made

1. **Custom Indexer for BSC Support** - Team unanimously agreed to pursue custom indexer route over The Graph due to latency requirements and real-time trading needs. Martin researching mature EVM framework for hybrid solution. - [Research document to be created EOD]

2. **P&L Cards Required Before Beta** - P&L cards identified as critical missing feature that must be implemented before wider beta release. Leo to complete proper desktop and mobile designs ASAP.

3. **24/7 On-Call Engineers** - Agreed to implement rotating on-call engineer support once actual users are onboarded to platform for uptime maintenance.

4. **PostHog for Metrics** - Pending formal approval, PostHog proposed as metrics tracking solution (decision needed from Zen, Gregory, Naji).

## Blockers and Risks Identified

- **OnRamper Approval Delay** - Impact: High - Owner: Gregory Chapman - OnRamper has charged for service but not approved integration, blocking end-to-end testing. Needs immediate resolution.

- **QA Resource Constraint** - Impact: Medium - Owner: Lucas Cufré - One QA engineer on leave due to family emergency, reducing QA coverage during critical beta preparation period.

- **P&L Cards Missing** - Impact: High - Owner: Leo (Design) - Basic feature missing that users will notice. Required before beta launch to Rob's team.

- **BSC Integration Timeline** - Impact: Medium - Owner: Lucas Cufré, Martin Aranda - Need time estimates for custom indexer development to assess impact on roadmap. Research document due EOD.

## Parking Lot

- Hyperliquid BNB bridging support (need to verify if supported)
- Detailed DEX aggregator pricing comparisons (1inch, OpenOcean, etc.)
- Error message normalization implementation timeline
- Number representation standard rollout across all instances

## Next Steps

**Immediate (Today - October 24):**
- Lucas to re-record and send video to Zen (within hours)
- Lucas and Martin to deliver BSC integration research document with time estimates (EOD)
- Lucas to send next roadmap information email
- Lucas to resurface PostHog metrics email for approval
- Gregory to contact OnRamper about approval delay

**Short-term (By Monday, October 28):**
- Deploy batch of fixes to production
- Complete 80-90% of frontend issues
- Leo to complete P&L card designs (desktop + mobile)
- Zen returns from travel and begins testing

**Next Week:**
- Zen conducts side-by-side platform comparisons (Tuesday, October 29)
- Continue stringent testing before wider beta release
- Evaluate BSC integration timeline based on research findings
- PostHog metrics integration pending approval

**Next Demo:** Expected following week (date TBD)

## References

- Notion QA Issue Tracker (access granted to Shak and Zen as guests)
- [BSC Integration Strategy Research](../05-research/bsc-integration-strategy.md) (created based on this discussion)
- OnRamper Essential Plan ($200/month)
- PostHog Metrics Platform (proposal pending approval)
- [Daily Standup - October 24, 2025](2025-10-24-daily-standup.md)

---

## Meeting Recording

**Transcript:** Available via Google Meet
**Notes Generated:** Gemini AI (reviewed and formatted)
**Recording Link:** [Google Calendar Event](https://www.google.com/calendar/event?eid=MzgzOGRjYmJhMDg5NGIxMWFkNjI3ZGRmOTc5YzI0M2ZfMjAyNTEwMjRUMTQzMDAwWiBsdWNhc2N1ZnJlQHJhdGhlcmxhYnMuY29t)
