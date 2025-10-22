---
title: Weekly Sync - 2025-10-20
date: 2025-10-20
type: meeting
meeting-type: weekly-sync
attendees:
  - Lucas Cufré (Project Lead)
  - Naji Osmat (Product)
  - Greg Chapman (Business)
  - Shak/Shakib (Development)
  - Martin Aranda (mentioned, not present)
duration: 25 minutes
status: completed
tags:
  - weekly-sync
  - production-deployment
  - roadmap-planning
  - infrastructure
  - onramper-integration
related-docs:
  - 03-active-work/_current-status.md
  - 04-knowledge-base/business/requirements/roadmap-q2-q3-2025.md
  - 02-decisions/2025-10-20-working-guards-on-call-rotation.md
  - 04-knowledge-base/operational/processes/2025-10-21-working-guards-24-7-support-proposal.md
summary: |
  Weekly sync meeting covering production deployment status, auto-priority fee feature launch,
  AWS infrastructure dependencies, OnRamper integration blockers, and Q4 roadmap confirmation.
  Key decisions on working guards implementation and indexer improvements project approval.
---

# Weekly Sync - October 20, 2025

## Executive Summary

Post-beta launch sync addressing production stability, new features deployment, and future roadmap planning. Team successfully deployed auto-priority fee feature to optimize transaction costs. Discussion of infrastructure resilience during AWS outage, proposal for working guards system to support beta users, and approval of 16-day indexer improvement project to reduce third-party dependencies.

**Key Highlights:**
- Auto-priority fee feature deployed to production (optimizes transaction costs)
- AWS outage occurred but did not affect Cooking's deployment region
- OnRamper integration blocked pending document approval (2 business days waiting)
- Working guards proposal for 24/7 developer coverage during beta
- Indexer improvements project approved (16 days, reduces Jupiter dependency)
- Q4 roadmap confirmed: dynamic fees, portfolio TP/SL, multi-language, token watchlist

## Meeting Details

**Date:** October 20, 2025
**Time:** Not specified
**Duration:** ~25 minutes
**Meeting Type:** Weekly Sync

**Attendees:**
- Lucas Cufré - Project Lead
- Naji Osmat - Product
- Greg Chapman - Business
- Shakib - Development
- Martin Aranda - Mentioned (not present)

## Topics Discussed

### 1. Production Deployment Status

**Context:**
Latest development pushed to production following beta launch.

**Discussion Points:**
- Latest features successfully deployed to production
- Team authorized to begin production testing
- Several UI issues identified and being fixed:
  - Button enabling issue when setting time intervals (e.g., 2 minutes)
  - Table sizing adjusted to provide more room for charts
- Auto-priority fee feature deployed successfully

**Current Status:**
- Production environment stable with minor UI fixes in progress
- Team actively hardening backend systems
- Continuous deployment of UI improvements

**Reference:** See [auto-adjusting-priority-fee.md](../../04-knowledge-base/business/requirements/auto-adjusting-priority-fee.md)

### 2. Auto-Priority Fee Feature

**Context:**
New feature to optimize transaction costs on Solana network.

**Feature Description:**
- Default setting: Auto-priority fee ENABLED
- System automatically selects optimal priority fee for each transaction
- Prevents overspending on network fees
- Fluctuating fees based on network conditions (not fixed per transaction)
- Users can disable and manually set priority fees if desired
- Example: Users could manually set to 1 SOL if they choose (for urgent transactions)

**Benefits:**
- Cost optimization for users
- Reduced fee waste
- Network-aware transaction processing
- Maintains transaction speed while minimizing costs

**Status:** Deployed to production, functioning as expected

### 3. AWS Infrastructure Outage

**Context:**
AWS reported outages/failures early morning of October 20, 2025.

**Discussion Points:**
- AWS experienced failures in certain regions
- Cooking's deployment region NOT affected
- All Cooking systems deployed on AWS:
  - Servers
  - Databases
  - Information handling systems
  - All infrastructure components

**Infrastructure Dependencies:**
- 100% AWS dependency accepted as calculated risk
- No viable safety net if AWS completely fails
- Migration to Azure or other providers possible but not a safety improvement
- AWS outages are rare (first remembered by team)
- Most fintech services (Revolut, crypto wallets, etc.) similarly dependent on AWS or Azure

**Mitigation Strategy:**
- Implementing Sentry and console notifications for faster issue detection
- Team working on rapid detection and response protocols
- Plan to deploy user notifications if critical infrastructure fails
- Accepted risk: If AWS fails, entire ecosystem affected equally

**Decision:** Maintain AWS deployment, focus on monitoring and rapid response rather than infrastructure diversification

### 4. OnRamper Integration Status

**Context:**
Fiat on-ramp integration pending for user onboarding.

**Current Blockers:**
- Successfully subscribed to OnRamper Essential plan
- Documents submitted but still "Pending Review"
- 2 business days elapsed since submission
- No approval or rejection received yet

**Action Items:**
- Greg Chapman to reach out to OnRamper contact
- Greg to check if email received regarding document status
- Greg setting up dedicated Telegram group with OnRamper (currently using personal Telegram)
- Expected resolution: Same day (October 20)

**Impact:**
Integration work cannot begin until documents approved and green light received.

**Reference:** OnRamper widget integration for fiat-to-crypto onboarding

### 5. Apple Developer Account Setup

**Context:**
Mobile app requires proper Apple organization account.

**Update:**
- Greg successfully obtained DUNS number for Cooking organization
- DUNS number enables creation of proper Apple organization account
- Previous blocker resolved
- Gmail access credentials clarified (separate from OnRamper credentials)

**Next Steps:**
- Greg to set up Apple organization account with DUNS
- Greg and Lucas to sync later same day on migration timeline
- Migrate mobile application to official Cooking Apple account

**Status:** Unblocked and in progress

### 6. Future Roadmap and Feature Prioritization

**Context:**
Planning Q4 development priorities and timeline.

**Proposed Features (Pending Confirmation):**
1. **Dynamic Fee Configuration** - Back office users can manage fee configurations for combinations of:
   - Mint address
   - Provider
   - Referral code
   - Other parameters
2. **Portfolio-Level Take Profit & Stop Loss** - Risk management at portfolio level
3. **Multi-Language Support** - Platform localization
4. **Token Watchlist** - User curated token tracking
5. **Wallet Tracker** - Enhanced wallet monitoring
6. **New Back Office Environment** - Account management merger:
   - Portfolio features
   - Wallet tracker
   - Current wallet management system
7. **System Hardening** - Ongoing stability improvements for 30-40 active beta users

**EVM Compatibility Discussion:**
- Not included in current Q4 roadmap
- Previously discussed feature (estimated 2 months development)
- More complex than Hyperliquid integration (requires full indexing vs proxy)
- Would require separate indexer instance per chain:
  - Ethereum (Layer 0)
  - Arbitrum (Layer 2)
  - Each chain needs its own indexing logic
- Deferred to future roadmap

**Metrics Confirmation:**
- Lucas requested Naji's confirmation on proposed metrics
- Critical for measuring success when beta users onboarded
- Need approval before next week's user introduction

**Action Items:**
- Naji to confirm roadmap features
- Naji to review and approve metrics
- Lucas to send consolidated product definition documents for review

**Reference:** See [roadmap-q2-q3-2025.md](../../04-knowledge-base/business/requirements/roadmap-q2-q3-2025.md)

### 7. Multi-Language Translation Tool

**Context:**
Naji sent translation tool information earlier.

**Discussion:**
- Tool evaluation deferred due to Lucas's back-to-back meetings
- Multi-language support is last item on current roadmap
- Request to add to roadmap scope for Q4

**Next Steps:**
- Lucas to review translation tool in detail after meeting
- Consider adding multi-language support to Q4 scope

**Status:** Under review

### 8. Working Guards Proposal

**Context:**
Need for 24/7 developer coverage once beta users are actively using platform.

**Proposal Structure:**

**Coverage:**
- 7-day rotation (Monday 9am - following Monday 8:59am)
- Dedicated developer on-call for entire week
- Coverage for off-hours incidents and critical issues

**Compensation Model:**
- **Base Fee:** Flat fee for entire week of availability
- **Hourly Charges:** Additional charges if actual work performed during off-hours
- Hourly rate: Standard development rate

**Responsibilities:**
- Available for critical/breaking issues affecting uptime
- Examples:
  - Indexer outages
  - Production-breaking bugs
  - System failures affecting trading
- Non-critical development work deferred to business hours

**Important Distinctions:**
- NOT for regular development time
- NOT for feature development
- ONLY for maintaining uptime and resolving critical issues
- Non-breaking issues deferred to next business day

**Example Scenario:**
- Indexer goes down preventing users from trading
- On-call developer works to restore service
- Time spent charged as regular hourly work
- Base fee covers availability, hourly fee covers actual work

**Next Steps:**
- Lucas to send detailed proposal via email
- Proposal includes base fee structure and hourly rates
- To be reviewed by Zane (primary stakeholder for dev operations)

**Rationale:**
Higher user density during beta requires rapid response capability to maintain quality and uptime.

### 9. Indexer Improvements Project

**Context:**
Proposal to enhance indexer capabilities and reduce third-party dependencies.

**Project Scope:**
- Index additional contracts from currently supported providers
- Reduce reliance on Jupiter's price indexing
- Improve data consistency across indexed data
- Estimated timeline: 16 days of development

**Expected Benefits:**
- More consistent/reliable data indexing
- Fewer chart outliers
- Better understanding of Solana network activity
- Improved price accuracy
- Reduced dependency on Jupiter as single source
- Solving multiple current data quality issues

**Current Issues Addressed:**
- Chart outliers and anomalies
- Price data inconsistencies
- Over-reliance on single provider (Jupiter)
- Limited visibility into Solana network events

**Approval Status:**
- Discussed with Zane via Telegram previously
- To be formally documented and sent for approval
- Recommended to complete before onboarding actual beta users
- Timeline: Next couple of weeks

**Strategic Importance:**
- Better position to handle real user traffic
- Improved data quality for trading decisions
- Reduced single points of failure
- Foundation for future scaling

**Next Steps:**
- Lucas to send detailed project document
- Formal approval process
- Implementation over 16-day period

## Decisions Made

| Decision | Owner | Rationale | Impact |
|----------|-------|-----------|--------|
| Auto-priority fee enabled by default | Product Team | Optimize user costs while maintaining speed | Reduces fee waste for users, better UX |
| Maintain AWS infrastructure without diversification | Tech Team | AWS outages rare, migration doesn't improve resilience | Focus resources on monitoring vs migration |
| Implement working guards system | Lucas/Zane | Beta users require 24/7 coverage for critical issues | Ensures uptime and rapid incident response |
| Approve indexer improvements (16 days) | Naji/Zane (pending) | Reduce Jupiter dependency, improve data quality | Better foundation for user onboarding |
| Defer EVM compatibility | Product Team | Q4 roadmap already full, complex project | Focus on Solana optimization first |

## Action Items

| Action | Owner | Due Date | Priority | Status |
|--------|-------|----------|----------|--------|
| Follow up with OnRamper on document approval | Greg Chapman | 2025-10-20 | High | Open |
| Set up Telegram group with OnRamper | Greg Chapman | 2025-10-20 | Medium | In Progress |
| Set up Apple organization account with DUNS | Greg Chapman | 2025-10-20 | High | In Progress |
| Sync with Lucas on Apple account migration | Greg Chapman | 2025-10-20 | Medium | Scheduled |
| Send working guards proposal via email | Lucas Cufré | 2025-10-21 | High | Open |
| Send indexer improvement document | Lucas Cufré | 2025-10-21 | High | Open |
| Send consolidated product definition documents | Lucas Cufré | Week of 2025-10-20 | Medium | Open |
| Confirm Q4 roadmap features | Naji Osmat | 2025-10-27 | High | Open |
| Review and approve metrics | Naji Osmat | 2025-10-27 | High | Open |
| Review multi-language translation tool | Lucas Cufré | 2025-10-21 | Low | Open |

## Blockers & Risks

### Active Blockers
1. **OnRamper Integration** - Documents pending approval (2 business days elapsed)
   - Impact: Cannot begin fiat on-ramp integration
   - Mitigation: Greg reaching out directly to OnRamper contact

### Identified Risks
1. **AWS Infrastructure Dependency** - 100% reliance on AWS
   - Likelihood: Low (rare outages)
   - Impact: High (complete service disruption)
   - Mitigation: Monitoring, rapid detection, user communication plan

2. **Metrics Not Confirmed** - Need approval before user onboarding
   - Likelihood: Medium
   - Impact: Medium (delayed user insights)
   - Mitigation: Following up with Naji for confirmation

3. **Working Guards Not Approved** - Beta users without 24/7 coverage
   - Likelihood: Low
   - Impact: High (potential extended outages)
   - Mitigation: Formal proposal to be sent immediately

## Next Steps

### Immediate (This Week)
1. Resolve OnRamper document approval blocker
2. Complete Apple organization account setup
3. Send working guards and indexer improvement proposals
4. Continue UI bug fixes and backend hardening
5. Review translation tool for multi-language support

### Short Term (Next 1-2 Weeks)
1. Begin indexer improvements project (16 days)
2. Implement working guards rotation
3. Confirm Q4 roadmap and metrics with stakeholders
4. Begin OnRamper widget integration (once approved)
5. Migrate mobile app to official Apple account

### Medium Term (Next Month)
1. Onboard beta users with confirmed metrics tracking
2. Complete indexer improvements
3. Begin Q4 roadmap feature development
4. Monitor production stability with real user traffic

## Notes

- **Team Morale:** Good - Lucas mentioned getting needed rest over Mother's Day weekend
- **Naji's Status:** Mentioned feeling "a little sick" during meeting
- **Zane's Absence:** Not present, but involved in Telegram discussions on working guards and indexer
- **Meeting Efficiency:** 25 minutes, covered significant ground across multiple topics

## Related Documents

- [Current Status](../../03-active-work/_current-status.md)
- [Q2-Q3 2025 Roadmap](../../04-knowledge-base/business/requirements/roadmap-q2-q3-2025.md)
- [Auto-Adjusting Priority Fee](../../04-knowledge-base/business/requirements/auto-adjusting-priority-fee.md)
- [Portfolio-Wide TP/SL](../../04-knowledge-base/business/requirements/portfolio-wide-tpsl.md)
- [Token Watchlist](../../04-knowledge-base/business/requirements/token-watchlist.md)
- [ADR-303: Working Guards On-Call Rotation](../../02-decisions/2025-10-20-working-guards-on-call-rotation.md)
- [Working Guards 24/7 Support Proposal](../../04-knowledge-base/operational/processes/2025-10-21-working-guards-24-7-support-proposal.md)

---

**Meeting recorded and documented:** 2025-10-21
