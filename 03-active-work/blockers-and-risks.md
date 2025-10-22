---
title: Blockers and Risks
type: risk-register
date: 2025-10-22
last-updated: 2025-10-22
status: active
owner: Lucas Cufré (Project Lead)
tags: [risks, blockers, issues, active-work, post-launch]
summary: |
  Post-beta launch risk register tracking resolved blockers, active risks, and mitigation strategies.
  Major blockers from October 2025 (ClickHouse crisis, Solana byte limit, DNS management) successfully
  resolved prior to October 17 launch. Minor production issues (CORS, custom order validation) identified
  October 22 with immediate mitigation in progress. Current focus on internal testing success and October 27
  launch decision.
related-docs:
  - _current-status.md
  - priorities.md
  - ../01-foundation/constraints-and-assumptions.md
---

# Blockers and Risks

**Last Updated:** October 22, 2025
**Project Phase:** Post-Beta Launch (Internal Testing)

---

## Active Blockers

**Current Status:** 🟡 Minor Issues (Non-Blocking)

### Production Issues Identified October 22:

#### Issue 1: CORS Configuration for Cookie Authentication
**Blocked Since:** October 22, 2025
**Impact:** Medium - Production batch operations affected
**Severity:** Non-blocking (workaround available)
**Owner:** Esteban Restrepo
**Description:**
- Transaction service configured with wildcard CORS
- Incompatible with cookie-based authentication (requires exact origins)
- Affects batch operations in dev and production

**Mitigation:**
- Use shared CORS utility from backend service (immediate)
- Duplicate proper CORS setup to transaction service
- Priority: Same day resolution

**Status:** 🟡 In Progress (fixes being deployed)

---

#### Issue 2: Custom Order Form Validation Bug
**Blocked Since:** October 22, 2025 (Production)
**Impact:** High - Users cannot create custom orders with time-based fields
**Severity:** Production critical
**Owner:** Germán Derbes Catoni / Marko Jauregui
**Description:**
- Average Holding Time and Price Change fields don't save values
- Fields with time frame references fail validation
- Only activates when time unit manually changed (minutes → hours)

**Root Cause:**
- Fields lack default/initial state values
- Changing time frame selector triggers proper state update
- Should have pre-selected default values

**Mitigation:**
- Add default values to all time-based custom order fields
- Priority: Same day fix

**Status:** 🟡 In Progress (assigned to Germán/Marko)

---

#### Issue 3: React Key Property Missing in Iterations
**Resolved:** October 22, 2025
**Impact:** High - Production carousel breakage
**Description:**
- Missing `key` property in `.map()` iterations caused carousel deduplication
- Showed only one item instead of all items
- Bug appeared in production but not local development
- Affected home carousel and positions carousel

**Resolution:** ✅ Immediate hotfix deployed with keys added to all iterations
**Lesson:** Always use `key` property in React iterations, even for Fragments

---

## Recently Resolved Blockers

### ClickHouse Merge Saturation Crisis
**Blocked From:** October 6-13, 2025 (7 days)
**Impact:** Portfolio queries 12-14 seconds, 1,000+ queries stuck
**Resolution:** Two-client architecture + projection optimization
**Outcome:** < 1s query latency, 10x rows reduction ✅
**Documentation:** [ADR-502](../02-decisions/2025-10-06-clickhouse-two-client-architecture.md)

### Solana Transaction Byte Limit
**Blocked From:** October 1-8, 2025 (7 days)
**Impact:** 50% transaction failure rate
**Resolution:** Disabled fee collection (temp), iterative max hops reduction (permanent)
**Outcome:** Transactions functional, fee collection deferred Q4 ✅

### DNS Management (Japan Time Zone)
**Blocked From:** October 6-10, 2025 (4 days)
**Impact:** Transaction microservice deployment blocked
**Resolution:** Screen-share workshop, DNS changes completed
**Outcome:** Transaction microservice deployed successfully ✅

### Refresh Token Cookie Not Setting
**Blocked From:** October 15-17, 2025 (2 days)
**Impact:** Authentication breaking after expiration
**Resolution:** Switched from Axios to Fetch, extended token to 10min
**Outcome:** Authentication reliable across Chrome/Safari ✅

### Eco Router Integration Pressure
**Blocked From:** September-October 2025 (~6 weeks)
**Impact:** Client pushing for Eco despite incompatibility
**Resolution:** Demonstrated 3s transaction performance, architectural incompatibility explained
**Outcome:** Client satisfied, Eco deprioritized ✅
**Documentation:** [ADR-100](../02-decisions/ADR-100-jupiter-primary-router-eco-rejection.md)

---

## Active Risks

### High-Priority Risks

#### Risk 1: Internal Testing Uncovers Catastrophic Bug
**Risk Score:** 🟡 Medium
**Probability:** Medium (20-30%) | **Impact:** High
**Owner:** Lucas Cufré + Team

**Description:**
5 client users testing October 21-27. Risk of discovering critical bug preventing October 27 full closed beta launch.

**Trigger Events:**
- Transaction failure rate > 5%
- Data loss or security incident
- Critical UX blocker preventing core workflows

**Impact if Realized:**
- Delay October 27 launch by 1-4 weeks
- Damages client confidence
- Further delays revenue generation

**Mitigation:**
- ✅ Extensive pre-launch testing completed
- ✅ Comprehensive monitoring (CloudWatch, SNS alerts)
- ✅ Rapid response team on standby
- [ ] Documented rollback procedures

**Contingency:**
- Minor: Fix rapidly, continue testing
- Moderate: Extend testing 3-5 days
- Critical: Delay October 27, transparent communication
- Catastrophic: Roll back, full architecture review

---

#### Risk 2: ClickHouse Knowledge Centralization
**Risk Score:** 🟡 Medium
**Probability:** Low (15-20%) | **Impact:** High
**Owner:** Lucas Cufré + Eduardo Yuschuk + Darío Balmaceda

**Description:**
Eduardo single expert on ClickHouse. If unavailable, performance could degrade without optimization expertise.

**Impact if Realized:**
- Query latency could return to 12-14s
- Slower incident response
- Development velocity reduced

**Mitigation:**
- ✅ Darío partnership (October 2025)
- ✅ Repository documentation for all changes
- [ ] Knowledge sharing sessions
- [ ] Runbook documentation
- [ ] External consultant relationship

**Progress:** 🟢 Improving (Darío reducing single-point-of-failure)

---

### Medium-Priority Risks

#### Risk 3: Transaction Fee Collection Architecture Delayed
**Risk Score:** 🟡 Medium
**Probability:** Medium (30-40%) | **Impact:** Medium
**Owner:** Martin Aranda + Esteban Restrepo

**Description:**
Linked transaction implementation could exceed Q4 timeline, further delaying revenue generation.

**Mitigation:**
- Q4 priority status ensures focused time
- Martin + Esteban collaboration
- Phased approach: Basic fees first, referral distribution second

**Contingency:**
- Accept Q1 2026 timeline if needed
- Simplified fee collection as interim solution

---

#### Risk 4: Apple App Store Review Rejection
**Risk Score:** 🟡 Medium
**Probability:** Medium (25-35%) | **Impact:** Medium
**Owner:** Byron Chavarria + Lucas Cufré

**Description:**
Mobile app could be rejected, delaying iOS launch.

**Mitigation:**
- ✅ Account deletion implemented
- ✅ Biometric authentication (ADR-401)
- ✅ Security password (ADR-400)
- [ ] GitBook help documentation (Lucas)
- [ ] TestFlight extensive testing

**Contingency:**
- Address rejection feedback (1-2 week turnaround)
- Fall back to web app during review

---

#### Risk 5: Provider-Discriminated Pricing Requires Major Restructuring
**Risk Score:** 🟡 Medium
**Probability:** Medium (40-50%) | **Impact:** Medium
**Owner:** Eduardo Yuschuk + Client

**Description:**
Competitive platforms show provider-specific pricing. Addressing this may require major indexer restructuring.

**Eduardo's Assessment:**
> "To compete, you have to index this. I don't see a path for the application if we don't eventually index that."

**Decision Required:**
Client must choose: Accept current model or commit to Q1 2026 restructuring

**Mitigation:**
- Short-term: Improved price filtering (Eduardo implementing)
- Medium-term: Provider discrimination via Jupiter API
- Long-term: Full pool indexing (Q1 2026+)

---

### Low-Priority Risks (Monitoring Only)

| Risk | Probability | Impact | Owner |
|------|------------|--------|-------|
| **Third-Party Service Outages** (Turnkey, Auth0, Jupiter) | Low | Medium | Infrastructure Team |
| **Hyperliquid US Geolocation** | Low | Medium | Legal + Lucas |
| **Mobile UI Updates Volume** | Medium | Low | Byron + Lucas |
| **Design Agency Review Delays** | Medium | Low | Frontend Team |
| **QuickNode RPC Rate Limits** (70M/month) | Low | Medium | Eduardo + Infrastructure |

---

## Risk Trends

### New Risks (Post-Launch)
- Internal Testing Uncovers Catastrophic Bug (October 21)
- Mobile UI Updates Volume (October 17)

### Escalated Risks
- Fee Collection Architecture: Low → Medium (Q4 timeline pressure)

### De-escalated Risks
- ClickHouse Knowledge: High → Medium (Darío partnership)
- Eco Integration: High → Resolved (client satisfied)

---

## Realized Risks (Now Resolved)

### ClickHouse Merge Saturation
**Materialized:** October 6, 2025
**Impact:** 7 days critical performance
**Outcome:** ✅ Resolved, < 1s latency
**Lesson:** Proactive monitoring essential, knowledge centralization risky

### Solana Byte Limit
**Materialized:** October 1, 2025
**Impact:** 50% failure rate, revenue blocked
**Outcome:** ✅ Transactions functional, fee collection deferred
**Lesson:** Transaction size validation needed in testing

### Client Performance Dissatisfaction
**Prevention:** October 17 demo (3s transactions)
**Outcome:** ✅ Client satisfied, Eco deprioritized
**Lesson:** Demonstrating performance > architecture explanations

---

## Issues (Non-Blocking)

| Issue | Severity | Owner | Target | Status |
|-------|----------|-------|--------|--------|
| CORS Configuration Cookie Auth | Medium | Esteban | Oct 22 | In Progress |
| Custom Order Time Fields | High | Germán/Marko | Oct 22 | In Progress |
| Safari Typography Differences | Low | German | Oct 24 | In Progress |
| Safari Image Rendering Inconsistency | Low | Luis | Oct 24 | Investigating |
| Toast Stuck Behavior | Low | Marko | Oct 24 | In Progress |
| Activity Breakdown Empty State | Low | German/Luis | Oct 25 | Discussion Needed |
| Number Display Standards | Low | Luis + Lucas | Oct 25 | Pending |
| Holders List Shows Incinerator | Low | Eduardo | Oct 25 | In Progress |
| Transaction Visualization Sold Assets | Low | Luis/Martin | Oct 26 | Identified |
| Referral Code Edit Button Missing | Low | Santiago | Oct 27 | Identified |

---

## Key Risk Indicators (KRIs)

| KRI | Threshold | Current | Status |
|-----|-----------|---------|--------|
| **Transaction Success Rate** | < 95% | ~98% | 🟢 |
| **API Error Rate** | > 1% | < 0.1% | 🟢 |
| **ClickHouse Query p95** | > 2s | < 1s | 🟢 |
| **System Uptime** | < 99.9% | 99.9% | 🟢 |
| **Client Complaints (Critical)** | > 1 | 0 | 🟢 |
| **Team Capacity** | > 100% | ~90% | 🟢 |

---

## Action Items Summary

### Immediate (This Week)
- [ ] Eduardo: Knowledge sharing with Darío on ClickHouse
- [ ] Lucas: Create GitBook help documentation
- [ ] Team: Monitor internal testing closely
- [ ] Martin + Esteban: Plan linked transaction architecture

### This Month
- [ ] Team: October 27 launch decision (go/no-go)
- [ ] Byron: TestFlight build and client review
- [ ] Frontend: Complete pixel-perfect alignment
- [ ] Infrastructure: Document ClickHouse runbooks

### Q4 2025
- [ ] Martin + Esteban: Implement linked transaction fees
- [ ] Eduardo + Darío: Decentralize ClickHouse knowledge
- [ ] Team: Begin architecture hardening
- [ ] Eduardo + Client: Provider pricing strategy decision

---

**Risk Register Owner:** Lucas Cufré
**Last Review:** October 22, 2025
**Next Review:** October 28, 2025
