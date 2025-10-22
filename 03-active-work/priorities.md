---
title: Current Priorities
type: priorities
date: 2025-10-22
last-updated: 2025-10-22
status: active
owner: Lucas Cufré (Project Lead)
tags: [priorities, planning, active-work, post-launch]
summary: |
  Post-beta launch priorities focused on internal testing support, stability monitoring,
  cookie-based authentication migration, and frontend polish. Platform successfully launched October 17
  with 99.9% uptime. Internal testing (5 users) ongoing October 21-27 determines October 27 full
  closed beta launch decision. Critical production bugs (CORS, custom order validation) identified
  October 22 with immediate fixes in progress.
related-docs:
  - _current-status.md
  - blockers-and-risks.md
  - ../01-foundation/objectives-and-scope.md
---

# Current Priorities

**Last Updated:** October 22, 2025
**Planning Period:** Post-Launch (October 21-27) & Q4 2025

## Priority Framework

- **P0 (Critical):** Blocks launch or causes severe impact; drop everything
- **P1 (High):** Must have for current milestone; schedule immediately
- **P2 (Medium):** Important but not blocking; schedule this sprint/month
- **P3 (Low):** Nice to have; schedule when capacity allows
- **P4 (Backlog):** Future consideration; not scheduled

---

## P0: Critical Priorities (Week of October 21-27)

### Production Bug Fixes (October 22)
**Why Critical:** Blocking user ability to create custom orders; cookie auth migration blocked by CORS
**Impact if Not Done:** Users cannot use custom order features; authentication migration delayed
**Owner:** Esteban Restrepo, Germán Derbes Catoni, Marko Jauregui
**Target Date:** October 22, 2025 (Same Day)
**Status:** 🟡 In Progress

**Critical Bugs:**
1. **CORS Configuration:** Transaction service wildcard CORS incompatible with cookies
   - Owner: Esteban
   - Fix: Use shared CORS utility from backend service
   - Impact: Batch operations affected, cookie auth migration blocked

2. **Custom Order Time Fields:** Average Holding Time and Price Change fields don't save
   - Owner: Germán/Marko
   - Fix: Add default values to time-based fields
   - Impact: Users cannot create custom orders with time-based conditions

**Success Criteria:**
- CORS configuration fixed and deployed (same day)
- Custom order form validation working (same day)
- No additional critical bugs blocking user workflows

**Related:** [Blockers & Risks](./blockers-and-risks.md)

---

### Internal Testing Support & Monitoring
**Why Critical:** 5 client users testing platform with real money; any critical bug blocks October 27 full launch
**Impact if Not Done:** Delayed launch, client dissatisfaction, missed October 27 deadline
**Owner:** Entire Team (Lucas coordinating)
**Target Date:** October 21-27, 2025
**Status:** 🟢 In Progress

**Activities:**
- Rapid response to any user-reported issues
- Real-time transaction success rate monitoring
- Daily check-ins with client users for feedback
- CloudWatch dashboard monitoring (uptime, errors, latency)
- Immediate bug fixes for critical issues

**Success Criteria:**
- Zero catastrophic bugs discovered
- Transaction success rate > 95%
- No security incidents or data loss
- Positive user feedback on core workflows

**Related:**  [Current Status](../_current-status.md) | [Blockers & Risks](./blockers-and-risks.md)

---

### Maintain 99.9% Uptime & Transaction Performance
**Why Critical:** Platform reputation depends on reliability during first user impressions
**Impact if Not Done:** User trust damaged, launch momentum lost, competitive disadvantage
**Owner:** Infrastructure Team (Eduardo, Darío, Marcos) + Martin Aranda
**Target Date:** Ongoing (October 21+)
**Status:** 🟢 On Track

**Key Metrics:**
- **Uptime:** 99.9% (current: 99.9% ✅)
- **Transaction completion:** < 5s p95 (current: 3s ✅)
- **ClickHouse queries:** < 2s p95 (current: < 1s ✅)
- **API error rate:** < 1% (current: < 0.1% ✅)

**Monitoring:**
- CloudWatch alarms for critical thresholds
- SNS alerts to Slack for immediate response
- Daily review of performance metrics
- Weekly infrastructure health check

**Related:** [ADR-500: Multi-AZ Deployment](../02-decisions/2025-09-04-multi-az-deployment-high-availability.md) | [ADR-502: ClickHouse Two-Client Architecture](../02-decisions/2025-10-06-clickhouse-two-client-architecture.md)

---

### Frontend Polish (Pixel-Perfect Design Alignment)
**Why Critical:** Most immediately visible to client and users; design agency intensive review
**Impact if Not Done:** Client dissatisfaction, perception of unpolished product, negative first impressions
**Owner:** Frontend Team (Luis, German, Marko, Santiago) + Lucas
**Target Date:** October 24-26, 2025
**Status:** 🟡 In Progress

**Focus Areas:**
- **Safari Compatibility:** Typography, alignment, image rendering (German)
- **Component Library Alignment:** C5 range tickets, design consistency (Luis, Santiago)
- **Toast Notifications:** Fix stuck behavior (Marko)
- **Referral Registration Page:** Final Figma comparison (Marko)
- **Number Display Standards:** Consistent formatting across platform (Luis + Lucas spec)

**Task Division:**
- **Javier Grajales:** Functionality testing only
- **Santiago Gimenez:** Design QA (Chrome + Safari)
- **Luis Rivera:** Prefi settings refactor (exclusive focus)
- **German Derbes:** Safari compatibility, login page
- **Marko Jauregui:** Referral page, toast fixes

**Rationale:** Frontend issues most immediately visible, highest client impact area

---

## P1: High Priorities

### Closed Beta Launch Decision (October 27 Go/No-Go)
**Business Value:** Determines whether full closed beta (30-40 users) launches October 27 or delayed
**Success Criteria:** Zero catastrophic bugs, transaction success > 95%, positive internal feedback
**Owner:** Lucas Cufré + Client (Sain, Ris)
**Target Date:** October 26, 2025 (decision deadline)
**Status:** ⏸️ Pending (awaiting internal testing results)
**Dependencies:** Internal testing week results (October 21-27)

**Decision Factors:**
- Transaction success rate during internal testing
- Severity of any discovered bugs
- Client user satisfaction with core workflows
- Infrastructure stability and performance
- Security incidents (target: zero)

**Outcomes:**
- **Go:** Launch October 27 with 30-40 whitelist users, referral viral growth begins
- **Delay:** Extend internal testing, fix critical issues, set new launch date
- **Partial:** Extend internal testing 3-5 days, limited launch with reduced users

**Related:** [ADR-201: Closed Beta via Referral-Only Access](../02-decisions/2025-08-11-closed-beta-referral-only-access.md) | [ADR-203: September Beta Launch Timeline](../02-decisions/2025-08-11-september-beta-launch-timeline.md)

---

### Mobile TestFlight Build & Client Review
**Business Value:** Enables client testing of iOS app, unblocks mobile launch preparation
**Success Criteria:** TestFlight build published, client feedback received, critical issues identified
**Owner:** Byron Chavarria
**Target Date:** October 24, 2025
**Status:** 🟡 In Progress
**Dependencies:** iOS navigation issues resolved ✅, L-Ramper integration complete ✅

**Activities:**
- Publish TestFlight version for client review
- Three schema setup (production, UAT, development)
- Limit order creation completion
- Client UI update incorporation (major work incoming)

**Known Challenges:**
- Major UI updates expected from client feedback
- Byron has "a ton of work ahead" based on client presentation
- App Store submission preparation (account deletion, GitBook help docs)

**Related:** [ADR-401: Biometric Authentication for Mobile](../02-decisions/ADR-401-biometric-authentication-mobile-trading.md) | Mobile App PRD

---

### Stress Testing Execution
**Business Value:** Validates platform performance under load before full closed beta
**Success Criteria:** Platform handles concurrent users, transaction volume, referral tree complexity
**Owner:** Federico Caffaro + Javier Grajales
**Target Date:** October 25-26, 2025
**Status:** 🟡 Planning Complete, Execution Pending
**Dependencies:** Test branch ready ✅, mass user creation endpoint implemented ✅

**Test Scope:**
- User and wallet creation (mass endpoint)
- Orders from multiple wallets with all providers
- Position verification and calculations
- WebSocket real-time updates
- Robust referral tree (multi-level testing)
- Perpetuals testing (Hyperliquid)
- Transaction mocking (exclude Solana submission, test providers)

**Method:**
- Apache AB for concurrency testing
- Custom scripts for specific scenarios
- Dev environment during low-usage times

---

## P2: Medium Priorities (Q4 2025)

### Transaction Fee Collection Implementation
**Business Value:** Unblocks revenue generation, enables referral commission distribution
**Owner:** Martin Aranda + Esteban Restrepo
**Target:** Q4 2025 (November-December)
**Status:** Planning

**Approach:**
- Separate linked transaction for fee collection
- Primary transaction: User trade execution
- Secondary transaction: Platform fees + referral commissions
- Phased implementation: Basic fees first, referral distribution second

**Challenges:**
- Solana linked transaction complexity
- Transaction ordering and atomicity
- Testing with actual fee structures

**Workaround Status:** Fee collection currently disabled (since October 1)

**Related:** Solana Byte Limit Crisis (resolved blocker)

---

### Architecture Hardening for Scalability
**Business Value:** Prepares platform for growth beyond 30-40 beta users
**Owner:** Lucas Cufré + Technical Team
**Target:** Begin Q4 2025
**Status:** Not Started (Post-Launch Priority)

**Lucas's Guidance (Oct 17):**
> "Next quarter we'll begin architecture hardening for scalability, indexer improvements, contract completion, price series separation. I don't say we'll close it, but we'll begin working on it systematically."

**Focus Areas:**
- Indexer optimization and scalability
- Contract completion (Radium, Meteora)
- Price series separation for better accuracy
- ClickHouse knowledge decentralization
- Performance optimization beyond current state

**Approach:** Systematic improvements, prioritized by impact, not "closing everything"

---

### ClickHouse Knowledge Decentralization
**Business Value:** Reduces single-point-of-failure risk (Eduardo expertise)
**Owner:** Eduardo Yuschuk + Darío Balmaceda + Lucas Cufré
**Target:** Q4 2025
**Status:** In Progress (Darío partnership established October 2025)

**Activities:**
- Knowledge sharing sessions (Eduardo teaching team)
- Runbook documentation for common issues
- Repository documentation (persist all changes)
- External consultant relationship for emergency support

**Progress:**
- 🟢 Darío now contributing to ClickHouse optimization
- 🟡 Documentation efforts ongoing
- 🔴 Formal knowledge transfer sessions not scheduled

**Related:** [Risk: ClickHouse Knowledge Centralization](./blockers-and-risks.md)

---

### Mobile App Store Submission Preparation
**Business Value:** Enables iOS public launch, reaches significant user segment
**Owner:** Byron Chavarria + Lucas Cufré
**Target:** Late Q4 2025
**Status:** Requirements Complete, Awaiting TestFlight Feedback
**Dependencies:** Client TestFlight review, UI updates incorporated

**iOS Requirements (Complete ✅):**
- Account deletion functionality implemented
- Biometric authentication (Face ID/Touch ID) - ADR-401
- Security password for wallet operations - ADR-400
- GitBook help documentation (Lucas TODO)

**Next Steps:**
- Complete TestFlight testing cycle
- Incorporate client UI feedback
- Create GitBook help documentation
- Final App Store guidelines review
- Submit for App Store review

**Related:** [Risk: Apple App Store Review Rejection](./blockers-and-risks.md)

---

## P3: Low Priorities (When Capacity Allows)

### Provider-Discriminated Pricing Strategy Decision
**Business Value:** Addresses competitive gap ("zero predictability" vs competitors)
**Owner:** Eduardo Yuschuk + Client Decision Makers
**Status:** Research & Evaluation
**Target:** Q1 2026 (if client approves)

**Eduardo's Assessment:**
> "To compete, you have to index this. I don't see a path for the application if we don't eventually index that."

**Options:**
- **Short-term:** Improved price filtering (Eduardo implementing now)
- **Medium-term:** Provider discrimination via Jupiter API
- **Long-term:** Full pool indexing (Orca, Meteora, etc.) - Q1 2026+

**Decision Required:** Client must choose between accepting current model or committing to major restructuring

**Trade-off:** Transparency vs development time vs competitive positioning

---

### Eco Router Re-evaluation
**Business Value:** Potential performance improvement if architectural reconciliation possible
**Owner:** Lucas Cufré + Client
**Status:** Deprioritized (Client Satisfied with Jupiter)

**Current State:**
- Eco integration rejected due to architectural incompatibility
- Jupiter demonstrating competitive performance (3s transactions)
- Client satisfied after October 17 demo

**Future Consideration:**
- Only if Eco resolves architectural issues (requires pool addresses)
- Only if competitive pressure increases
- Only if Jupiter performance degrades significantly

**Related:** [ADR-100: Jupiter as Primary Router (Rejecting Echo)](../02-decisions/ADR-100-jupiter-primary-router-eco-rejection.md)

---

### Full Marketing Campaign Preparation
**Business Value:** Drives user acquisition for public launch
**Owner:** Client Marketing (Nashi) + Lucas Cufré
**Status:** Backlog (Post-Closed Beta)
**Target:** Q1 2026

**Lucas's Note:** "Fulera" (intense/significant) marketing campaign planned for full public launch

**Dependencies:**
- Closed beta success and feedback integration
- Fee collection implemented (revenue model validated)
- Mobile app available on both iOS and Android
- Platform stability proven at 500+ user scale

---

## Recently Completed Priorities

### Beta Launch Execution (October 17, 2025)
**Completed:** October 17, 2025
**Outcome:** 99.9% uptime, 3s transaction performance, zero security incidents ✅
**Original Priority:** P0 - Critical
**Related:** All 27 ADRs, 6 months intensive development (May-October 2025)

---

### ClickHouse Performance Crisis Resolution
**Completed:** October 13, 2025
**Outcome:** < 1s query latency (down from 12-14s), zero query backlog ✅
**Original Priority:** P0 - Critical (emerged October 6)
**Related:** [ADR-502: ClickHouse Two-Client Architecture](../02-decisions/2025-10-06-clickhouse-two-client-architecture.md)

---

### Eco Router Evaluation & Client Communication
**Completed:** October 17, 2025
**Outcome:** Client satisfied with Jupiter, Eco deprioritized ✅
**Original Priority:** P0 - Critical (client pressure September-October)
**Related:** [ADR-100: Jupiter as Primary Router](../02-decisions/ADR-100-jupiter-primary-router-eco-rejection.md)

---

### Feature Freeze Adherence (August-October 17)
**Completed:** October 17, 2025
**Outcome:** 100% adherence, 50% performance improvement (6s → 3s transactions) ✅
**Original Priority:** P1 - High
**Related:** [ADR-302: Feature Freeze for Stability](../02-decisions/2025-08-11-feature-freeze-for-stability.md)

---

## Priority Changes This Period

| Date | Item | Old Priority | New Priority | Reason |
|------|------|-------------|--------------|--------|
| Oct 6 | ClickHouse Crisis | P2 | P0 | System unresponsive, 1,000+ queries stuck |
| Oct 17 | Eco Integration | P0 | P4 | Client satisfied after performance demo |
| Oct 17 | Internal Testing | P1 | P0 | Launch gate decision depends on results |
| Oct 21 | Frontend Polish | P2 | P0 | Client design agency intensive review |

---

## Alignment with Objectives

### Objective: Successful Closed Beta Launch (October 2025)
**Priority Alignment:** ✅ Achieved October 17, now focusing on internal testing success
**Progress:** 🟢 On Track for October 27 full launch (pending internal testing)

**Supporting Priorities:**
- P0: Internal testing support
- P0: Maintain 99.9% uptime
- P0: Frontend polish
- P1: Closed beta launch decision

---

### Objective: Platform Stability & Performance
**Priority Alignment:** All infrastructure and monitoring priorities support this
**Progress:** 🟢 On Track (99.9% uptime, 3s transactions, < 1s queries)

**Supporting Priorities:**
- P0: Transaction performance monitoring
- P2: Architecture hardening
- P2: ClickHouse knowledge decentralization

---

### Objective: Revenue Generation (Q4 2025)
**Priority Alignment:** Fee collection implementation critical for business model
**Progress:** 🟡 Delayed (Solana byte limit workaround, Q4 implementation planned)

**Supporting Priorities:**
- P2: Transaction fee collection implementation
- Related: Referral commission distribution

---

## Capacity vs Demand

**Team Capacity:** Transitioning from crisis mode (Aug-Oct) to sustainable pace
**Current Utilization:** ~90% (sustainable post-launch)

**Status:** 🟢 At Capacity (Healthy)

**Post-Launch Shift:**
- From "drop everything" launch mode to systematic Q4 improvements
- From bug fixing/polish to architecture hardening
- From feature freeze to selective feature additions based on feedback

**Lucas's Commitment (Oct 17):**
> "I promise we'll make it more comfortable, calmer from here on."

---

## Deferred Items

### Hyperliquid US Geolocation Legal Review
**Was:** P2 (Medium)
**Deferred To:** Q1 2026
**Reason:** Workaround implemented, not blocking current closed beta

---

### Pool Liquidity Indexing (Orca, Meteora)
**Was:** P2 (Medium)
**Deferred To:** Q1 2026
**Reason:** Eduardo's assessment requires major restructuring, need client decision first

---

### Apple Social Login Integration
**Was:** P2 (Medium)
**Deferred To:** Q1 2026
**Reason:** Google, Twitter, Telegram sufficient for launch; requires business account access

---

## Next Priority Review

**Scheduled:** October 28, 2025 (Post-Closed Beta Launch Decision)
**Participants:** Lucas Cufré, Martin Aranda, Client Team
**Agenda:**
- Review October 27 launch decision
- Adjust priorities based on closed beta feedback
- Finalize Q4 roadmap
- Address any emerging blockers or risks

---

**Maintenance:**
- Update weekly during team sync
- Review P0/P1 items daily during internal testing (Oct 21-27)
- Adjust based on blockers and new information
- Archive completed items monthly

---

**Priorities Owner:** Lucas Cufré (Project Lead)
**Last Updated:** October 22, 2025
**Next Review:** October 28, 2025
