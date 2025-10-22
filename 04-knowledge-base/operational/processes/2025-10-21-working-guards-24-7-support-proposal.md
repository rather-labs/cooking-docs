---
title: Working Guards 24/7 Maintenance Support Proposal
type: operational-process
category: incident-response
date: 2025-10-21
status: proposed
stakeholders:
  - Zane (Primary - Product/Operations)
  - Naji Osmat
  - Greg Chapman
  - Development Team
proposal-owner: Lucas Cufré (RatherLabs)
tags:
  - on-call
  - working-guards
  - incident-response
  - 24-7-support
  - maintenance
  - beta-operations
related-docs:
  - 02-decisions/2025-10-20-working-guards-on-call-rotation.md
  - 06-meetings/2025-10/2025-10-20-weekly-sync.md
  - 03-active-work/_current-status.md
summary: |
  Formal proposal for implementing RatherLabs' Working Guards system to provide
  24/7 maintenance coverage for Cooking.gg during live production phase. Two-developer
  rotation model (frontend + backend) with $300/week per developer base fee plus
  active development hours at standard rate.
---

# Working Guards 24/7 Maintenance Support Proposal

**Proposal Date:** October 21, 2025
**Proposed By:** RatherLabs / Lucas Cufré
**For:** Cooking.gg Production Operations
**Status:** Awaiting Stakeholder Approval

---

## Executive Summary

As Cooking.gg transitions into its live production phase with real users, we propose implementing RatherLabs' standard Working Guards system to provide around-the-clock maintenance coverage. This ensures consistent uptime, rapid incident response, and service reliability for all active users.

**Key Proposal Points:**
- **Coverage Model:** Two developers per week (1 frontend + 1 backend) for Month 1
- **Cost:** $600/week base fee ($300 per developer) + development hours at standard rate
- **Schedule:** Weekly rotations (Monday 09:00 UTC-3 to following Monday 08:59 UTC-3)
- **Scope:** Incident response and system maintenance only (not feature development)
- **Review:** Month 1 performance review to optimize coverage model

---

## Background and Context

### Current Situation

**Production Status:**
- Beta launched: October 17, 2025
- Active users: 30-40 beta users (growing)
- User expectation: High availability and professional support
- Current coverage: Business hours only (no after-hours support)

**Identified Risks:**
- Critical systems (indexer, trading engine, wallet infrastructure) can fail outside business hours
- AWS infrastructure dependencies require monitoring
- Solana network issues can impact trading functionality
- No mechanism for rapid response to after-hours incidents
- Reputation risk during critical beta phase

**Infrastructure Context:**
- **Recent AWS Outage:** October 20, 2025 - Although Cooking's region was unaffected, highlighted dependency on cloud infrastructure
- **Critical Systems:**
  - Solana Indexer (processes blockchain data)
  - Trading Engine (executes DCA, TWAP, limit orders)
  - Wallet Infrastructure (Turnkey integration)
  - Database Systems (ClickHouse, Redis)
  - RPC Providers (blockchain connectivity)

### Decision Context

This proposal implements [ADR-303: Working Guards On-Call Rotation for Beta Support](../../02-decisions/2025-10-20-working-guards-on-call-rotation.md), which was discussed during the [October 20, 2025 Weekly Sync](../../06-meetings/2025-10/2025-10-20-weekly-sync.md).

---

## What is Working Guards?

**Working Guards** is RatherLabs' standard practice for providing 24/7 maintenance coverage for production systems. The system ensures rapid and effective response to issues arising outside regular business hours through proper coordination and communication.

### Core Objectives

1. **Maintain System Operability:** Ensure platform remains functional 24/7
2. **Rapid Incident Response:** Fast and appropriate responses to emergencies
3. **Client Satisfaction:** Professional support experience for users
4. **Clear Communication:** Regular updates through designated channels

### Key Principle

**Working Guards are for incident response and system maintenance - NOT for implementing new features or enhancements.**

---

## Proposed Implementation

### Coverage Schedule

**Rotation Model:**
- **Duration:** 7-day rotations
- **Start Time:** Monday 09:00 UTC-3
- **End Time:** Following Monday 08:59 UTC-3
- **Handoff:** Seamless transition between teams each Monday morning

**Month 1 Coverage (Initial Period):**
- **Two developers per rotation:**
  - 1 Front-end Developer
  - 1 Back-end Developer
- **Rationale:** Maximum coverage across all technical areas during initial beta phase
- **Cost:** $600/week base fee ($300 per developer)

**Post-Month 1:**
- Coverage model reviewed based on:
  - Actual incident reports and frequency
  - Usage patterns and traffic analysis
  - Required technical expertise per incident type
- Potential adjustment to single developer if data supports optimization
- Cost optimization: Potentially $300/week base fee

### Responsibilities and Scope

#### IN SCOPE: Incident Response and System Maintenance

**Primary Responsibilities:**
1. **System Monitoring**
   - Monitor system alerts and dashboards
   - Ensure appropriate and fast responses to emergencies
   - Proactive identification of potential issues

2. **Communication**
   - Maintain communication via Telegram or other agreed-upon channels
   - Provide regular updates to client and team
   - Document all incidents and responses

3. **Operational Issue Resolution**
   - RPC (Remote Procedure Call) failures
   - Indexer outages preventing trading
   - Trading engine failures
   - Wallet system failures
   - Database/infrastructure outages
   - Problems arising from system updates
   - Security incidents
   - Data corruption issues
   - Critical bugs breaking core functionality

#### OUT OF SCOPE: Explicitly Excluded

- ❌ New features or enhancements
- ❌ Feature development work
- ❌ Non-critical bug fixes (deferred to business hours)
- ❌ UI/UX improvements
- ❌ Performance optimizations (unless causing outages)
- ❌ Routine scheduled maintenance
- ❌ Documentation updates
- ❌ Code reviews
- ❌ Planning and design work

---

## Pricing Structure

### Base Fee (Availability Charge)

**$300 USD per assigned developer per week**

**What This Covers:**
- 24/7 availability throughout the assigned week
- Monitoring and responding to system alerts
- Communication availability via Telegram and designated channels
- Responsibility for rapid incident response
- Lifestyle restrictions during on-call period (must remain available)

**Billing:**
- Charged regardless of whether incidents occur
- Flat weekly fee per developer
- Month 1: $600/week (2 developers)
- Post-Month 1: $300-$600/week (based on optimized coverage model)

### Active Development Time

**Billed at standard development hourly rate**

**When This Applies:**
- Only when the Working Guard must actively develop code to resolve an incident
- Coding solutions for system failures
- Implementing hotfixes for critical bugs
- Developing failover mechanisms
- Database recovery operations requiring code changes

**What This Does NOT Include:**
- Restarting services (covered by base fee)
- Monitoring and alerting (covered by base fee)
- Communication and updates (covered by base fee)
- Investigation without coding (covered by base fee)

**Billing:**
- Charged in addition to the flat fee
- Only actual development hours billed
- Standard hourly development rate applies
- Transparent time tracking and reporting

---

## Cost Examples and Scenarios

### Scenario 1: Quiet Week (Monitoring Only)

**Situation:**
- System alerts monitored throughout week
- All issues auto-resolved
- No incidents requiring manual intervention
- Both developers available but no coding needed

**Billing:**
- Base Fee: $600 (2 developers × $300)
- Development Hours: $0 (no active development required)
- **Total: $600**

### Scenario 2: Single Incident Requiring Code Fix

**Situation:**
- RPC provider fails on Wednesday at 11 PM
- Backend developer investigates and develops failover mechanism
- Development time: 3 hours
- Deploy, test, and monitor recovery

**Billing:**
- Base Fee: $600 (2 developers × $300)
- Development Hours: 3 hours × standard rate
- **Total: $600 + (3 × hourly rate)**

### Scenario 3: Multiple Incidents Throughout Week

**Situation:**
- Monday: Indexer restart (no code) - backend dev
- Wednesday: RPC failover fix (3 hours code) - backend dev
- Friday: UI critical bug fix (2 hours code) - frontend dev
- Total development time: 5 hours

**Billing:**
- Base Fee: $600 (2 developers × $300)
- Development Hours: 5 hours × standard rate
- **Total: $600 + (5 × hourly rate)**

### Scenario 4: Major Incident Requiring Extended Response

**Situation:**
- Saturday: Trading engine failure during system update
- Backend developer debugs, develops hotfix, tests, deploys
- Monitoring and communication throughout
- Development time: 6 hours

**Billing:**
- Base Fee: $600 (2 developers × $300)
- Development Hours: 6 hours × standard rate
- **Total: $600 + (6 × hourly rate)**

---

## Monthly Cost Projections

### Month 1 (Two-Developer Model)

**Base Costs:**
- Weekly Base Fee: $600
- Monthly Base Fee (4 weeks): $2,400

**Variable Costs (Development Hours):**
- **Low Activity:** 0-5 hours/month = $0-500 (at $100/hr avg)
- **Moderate Activity:** 5-15 hours/month = $500-1,500
- **High Activity:** 15-25 hours/month = $1,500-2,500

**Estimated Monthly Total:**
- **Best Case:** $2,400 (base only, no incidents requiring coding)
- **Expected Case:** $2,900-3,400 (base + 5-10 development hours)
- **High Activity Case:** $3,900-4,900 (base + 15-25 development hours)

### Post-Month 1 (Optimized Model - TBD)

Based on Month 1 data, coverage may be adjusted:

**Potential Single-Developer Model:**
- Weekly Base Fee: $300
- Monthly Base Fee (4 weeks): $1,200
- Variable Development Hours: As needed
- Estimated Monthly Total: $1,200-2,200

**Decision Factors:**
- Incident frequency and severity
- Required technical expertise (frontend vs backend split)
- User growth and traffic patterns
- System stability improvements

---

## Success Metrics and Performance Monitoring

### Key Performance Indicators (KPIs)

1. **Response Time**
   - **MTTA (Mean Time to Acknowledge):** < 15 minutes for P0 incidents
   - **MTTR (Mean Time to Resolve):** < 2 hours for P0, < 4 hours for P1

2. **Uptime**
   - **Target:** 99.5% uptime including off-hours
   - **Measurement:** AWS CloudWatch, Sentry monitoring

3. **Incident Volume**
   - Track frequency and severity of incidents
   - Goal: Decreasing trend as stability improves

4. **Cost Efficiency**
   - Development hours per incident
   - Monthly cost trends
   - Preventive measures implemented

### Monitoring and Reporting

**Weekly:**
- Incident summary from previous rotation
- Development hours logged
- Issues identified for improvement

**Monthly:**
- Comprehensive incident analysis
- Cost analysis and trends
- Coverage model effectiveness review
- Recommendations for optimization

**Month 1 Review (Critical):**
- Full performance assessment
- Coverage model optimization decision
- Cost-benefit analysis
- Go/No-Go decision for continued service

---

## Implementation Timeline

### Immediate (Week of October 21, 2025)

- ✅ Formal proposal sent to stakeholders
- ⏳ Stakeholder review and approval
- ⏳ Budget allocation confirmation
- ⏳ Team selection (frontend + backend developers)

### Week 2-3 (Pre-Launch Preparation)

- ⏳ Create incident response runbooks
- ⏳ Set up monitoring and alerting systems
- ⏳ Establish communication channels (Telegram groups, etc.)
- ⏳ Define escalation procedures
- ⏳ Create rotation schedule for Month 1
- ⏳ Team training on Working Guards procedures

### Week 4 (Launch)

- ⏳ First rotation begins (Monday 09:00 UTC-3)
- ⏳ Active monitoring and incident response
- ⏳ Daily check-ins with on-call team
- ⏳ Weekly handoffs between rotations

### Month 1 (November 2025)

- ⏳ Four complete rotation cycles
- ⏳ Incident tracking and analysis
- ⏳ Cost tracking and reporting
- ⏳ Performance measurement against KPIs

### End of Month 1

- ⏳ Comprehensive review meeting
- ⏳ Coverage model optimization decision
- ⏳ Budget adjustment if needed
- ⏳ Renewal decision for Month 2+

---

## Risk Mitigation

### Identified Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Developer Burnout** | Medium | Weekly rotation distributes burden; Month 1 review to adjust |
| **High Incident Volume** | High | Invest in preventive measures; track and address root causes |
| **Cost Overruns** | Medium | Monthly budget tracking; escalation for >8 hour incidents |
| **Inadequate Coverage** | High | Two-developer model in Month 1; adjust based on data |
| **Communication Gaps** | Medium | Clear escalation procedures; designated channels; daily updates |
| **False Escalations** | Low | Clear scope definition; training; post-incident reviews |

---

## Benefits and Value Proposition

### For Cooking.gg

1. **Enhanced Reliability:** 24/7 coverage ensures rapid response to critical issues
2. **User Satisfaction:** Professional support experience builds trust during beta
3. **Risk Mitigation:** Reduced exposure to extended outages and reputation damage
4. **Competitive Advantage:** Higher uptime than competitors in crypto trading space
5. **Data-Driven Optimization:** Month 1 review enables cost optimization

### For RatherLabs

1. **Standard Practice:** Proven Working Guards system with established processes
2. **Fair Compensation:** Team compensated appropriately for availability and work
3. **Sustainable Model:** Rotation prevents burnout; scalable as project grows
4. **Professional Operations:** Demonstrates enterprise-grade support capabilities

### For End Users

1. **High Availability:** Trading platform accessible when needed
2. **Rapid Issue Resolution:** Problems addressed within hours, not days
3. **Confidence:** Professional support enhances trust in platform
4. **Competitive Edge:** Users can trade 24/7 without concern about platform issues

---

## Terms and Conditions

### Billing and Payment

- Base fees billed weekly
- Development hours billed monthly with detailed time tracking
- Invoices provided with incident summaries
- Standard payment terms apply

### Service Level Agreement (SLA)

- P0 Incidents: 15-minute acknowledgment, 2-hour resolution target
- P1 Incidents: 30-minute acknowledgment, 4-hour resolution target
- P2 Incidents: 2-hour acknowledgment, next business day resolution
- Uptime Target: 99.5% including off-hours

### Scope Changes

- Coverage model may be adjusted after Month 1 review
- Pricing adjustments only with mutual agreement
- 2-week notice for termination of service

### Escalation

- Critical incidents requiring >8 hours will be escalated to Lucas Cufré
- Budget concerns escalated to stakeholders
- Coverage adequacy concerns addressed in weekly reviews

---

## Next Steps and Approval Process

### Required Approvals

1. **Primary Stakeholder Approval:** Zane (Product/Operations)
2. **Budget Approval:** Naji Osmat, Greg Chapman
3. **Technical Review:** Development team leads
4. **Contract Terms:** RatherLabs and Cooking.gg legal/operations

### Decision Timeline

- **Proposal Sent:** October 21, 2025
- **Review Period:** October 21-25, 2025
- **Expected Decision:** Week of October 21-25, 2025
- **Implementation Preparation:** 1-2 weeks if approved
- **Service Start:** TBD (pending approval and preparation)

### Contact for Questions

**Primary Contact:**
Lucas Cufré
Project Lead, RatherLabs
Communication: Telegram, Email

**Technical Questions:**
Development Team Leads

**Budget/Contract Questions:**
RatherLabs Operations Team

---

## Conclusion

The Working Guards system provides Cooking.gg with professional-grade 24/7 maintenance coverage during the critical beta phase. The two-developer model for Month 1 ensures comprehensive coverage while gathering data to optimize the long-term approach.

**Key Advantages:**
- ✅ Industry-standard practice (RatherLabs proven model)
- ✅ Fair and transparent pricing structure
- ✅ Data-driven optimization after Month 1
- ✅ Clear scope preventing feature creep
- ✅ Scalable as user base grows
- ✅ Protects platform reputation and user trust

**Investment Context:**
- Base cost: $2,400/month (Month 1)
- Variable cost: Based on actual incidents
- Expected total: $2,900-3,400/month initially
- Potential optimization: ~$1,500-2,200/month after Month 1
- Value: Platform uptime, user satisfaction, competitive advantage

We recommend approval to begin implementation preparation, with service launch targeted for early November 2025.

---

## References

- [ADR-303: Working Guards On-Call Rotation for Beta Support](../../02-decisions/2025-10-20-working-guards-on-call-rotation.md)
- [October 20, 2025 Weekly Sync Meeting Notes](../../06-meetings/2025-10/2025-10-20-weekly-sync.md)
- [Current Project Status](../../03-active-work/_current-status.md)
- [Beta Launch Timeline - ADR-203](../../02-decisions/2025-08-11-september-beta-launch-timeline.md)

---

**Document Status:** Proposal - Awaiting Stakeholder Approval
**Last Updated:** October 21, 2025
**Version:** 1.0
**Owner:** Lucas Cufré (RatherLabs)
