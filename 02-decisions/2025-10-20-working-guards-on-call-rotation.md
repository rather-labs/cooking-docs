---
title: Working Guards On-Call Rotation for Beta Support
type: decision-record
decision-id: ADR-303
date: 2025-10-20
status: proposed
owner: Lucas Cufré
stakeholders: [Zane (Product/Operations), Development Team, Naji Osmat, Greg Chapman]
tags: [process, on-call, operations, beta-support, incident-response, devops]
summary: |
  Proposal to implement a Working Guards system providing 24/7 developer coverage
  during beta phase to ensure rapid incident response and maintain platform uptime
  for 30-40 active beta users. Two-developer rotation (frontend + backend) at $300/week
  per developer plus development hours.
related-docs:
  - 2025-08-11-september-beta-launch-timeline.md
  - 2025-08-11-feature-freeze-for-stability.md
  - ../06-meetings/2025-10/2025-10-20-weekly-sync.md
  - ../04-knowledge-base/operational/processes/2025-10-21-working-guards-24-7-support-proposal.md
  - ../03-active-work/_current-status.md
---

# ADR-303: Working Guards On-Call Rotation for Beta Support

## Context and Problem Statement

With the successful beta launch on October 17, 2025, and the anticipated onboarding of 30-40 active beta users, the platform requires 24/7 monitoring and rapid incident response capabilities. Currently, the development team operates during standard business hours, leaving potential gaps in coverage for critical incidents that could affect platform uptime, trading functionality, or user experience.

**Key Concerns:**
- Beta users expect high availability and rapid issue resolution
- Critical systems (indexer, trading engine, wallet infrastructure) can fail outside business hours
- Reputation risk during beta phase if incidents aren't addressed promptly
- No current mechanism for after-hours incident response
- Infrastructure dependencies (AWS, Solana network) can experience issues at any time

## Decision Drivers

1. **Platform Stability Requirements** - Beta users need reliable 24/7 access to trading functionality
2. **Rapid Incident Response** - Critical issues (indexer outages, trading failures) must be resolved quickly
3. **Reputation Management** - Beta phase is crucial for gathering positive feedback and referrals
4. **Fair Compensation** - Developers providing after-hours availability should be compensated appropriately
5. **Sustainable Operations** - Need scalable model that doesn't burn out team members
6. **Cost Efficiency** - Balance coverage needs with reasonable operational costs

## Considered Options

### Option 1: No Formal On-Call System (Status Quo)
**Description:** Continue with best-effort response during business hours only.

**Pros:**
- No additional costs
- No process changes required
- Team maintains work-life balance

**Cons:**
- Critical incidents outside business hours go unaddressed for 12-16 hours
- Risk of extended outages during evenings/weekends
- Poor user experience during beta phase
- Potential reputation damage
- No accountability for incident response

**Rejected:** Unacceptable risk for beta phase with active users.

### Option 2: Full 24/7 Staffing
**Description:** Hire additional developers to provide round-the-clock coverage.

**Pros:**
- Immediate response to all incidents
- No burden on existing team
- Professional operations model

**Cons:**
- Extremely high cost (3x current team size minimum)
- Complex coordination across time zones
- Overkill for beta phase user volumes
- Long hiring timeline

**Rejected:** Cost prohibitive and unnecessary for current scale.

### Option 3: Working Guards Rotation (PROPOSED)
**Description:** Implement weekly rotating on-call duty with base fee for availability plus hourly charges for actual incident work.

**Pros:**
- Balanced cost model (pay for availability + actual work)
- Sustainable for team (1 week rotation spreads burden)
- Rapid response capability for critical issues
- Clear compensation structure
- Scalable model as user base grows
- Maintains team work-life balance (most weeks off-duty)

**Cons:**
- Additional operational cost
- Requires coordination and scheduling
- Potential for developer fatigue during on-call week
- Need clear escalation and handoff procedures

**SELECTED:** Best balance of coverage, cost, and sustainability.

### Option 4: Incident Response Service/Outsourcing
**Description:** Contract with third-party incident response service.

**Pros:**
- Professional incident management
- No burden on development team

**Cons:**
- Requires detailed runbooks and documentation
- Third-party lacks deep product knowledge
- High cost for qualified Solana/crypto expertise
- Language barriers (Spanish-speaking team)
- Slower response due to knowledge gaps

**Rejected:** Insufficient product expertise available externally.

## Decision Outcome

**Chosen Option:** Option 3 - Working Guards Rotation System

### Implementation Details

**Coverage Model:**
- **Rotation Period:** 7 days (Monday 09:00 UTC-3 - following Monday 08:59 UTC-3)
- **Initial Coverage (Month 1):** Two developers per rotation
  - One front-end developer
  - One back-end developer
  - Ensures comprehensive coverage across all technical areas
- **Post-Month 1:** Coverage model to be reviewed and adjusted based on:
  - Actual incident reports and frequency
  - Usage patterns and traffic analysis
  - Required technical expertise per incident type
- **Continuous rotation** across development team

**Compensation Structure:**

1. **Base Fee (Availability Charge)**
   - **$300 USD per developer per week**
   - Flat fee regardless of whether incidents occur
   - Compensates for:
     - Need to remain available 24/7 during on-call week
     - Lifestyle restrictions during on-call week
     - Responsibility for monitoring and readiness
     - Communication availability via Telegram and other channels

2. **Active Development Charges**
   - Standard development hourly rate (billed separately)
   - Applied when active development/coding is required to resolve incidents
   - Charged only for time actively developing solutions
   - Billed in addition to the flat fee
   - Examples:
     - Developing fixes for production-breaking bugs
     - Coding solutions for RPC failures
     - Implementing hotfixes for system failures
     - Database recovery operations requiring code changes

**Scope of Responsibilities:**

**IN SCOPE (Incident Response and System Maintenance):**
- **System Monitoring:** Monitor and respond to system alerts
- **Incident Response:** Fast and appropriate responses to emergencies
- **Communication:** Maintain updates through designated client and team channels (Telegram, etc.)
- **Operational Issues Resolution:**
  - RPC (Remote Procedure Call) failures
  - Indexer outages preventing trading
  - Trading engine failures
  - Wallet system failures
  - Database/infrastructure outages
  - Problems arising from system updates
  - Security incidents
  - Data corruption issues
  - System failures affecting user access
  - Critical bugs breaking core functionality

**OUT OF SCOPE (Explicitly Excluded):**
- **New features or enhancements**
- Feature development work
- Non-critical bug fixes
- UI/UX improvements
- Performance optimizations (unless causing outages)
- Routine maintenance (scheduled work)
- Documentation updates
- Code reviews
- Planning and design work

**Key Principles:**
- On-call developer focuses solely on maintaining uptime
- Non-breaking issues documented and deferred to next business day
- Clear communication of incidents to team and stakeholders
- Handoff documentation for complex multi-day incidents

### Expected Scenarios

**Scenario 1: RPC Failure Requiring Code Fix**
- Issue: RPC provider fails, breaking all blockchain interactions at 11 PM
- Impact: Critical - users cannot execute trades or see wallet balances
- Response: On-call backend developer investigates, develops failover mechanism, deploys fix
- Billing: $300 base fee + 3 hours of development time at standard rate
- Total Cost: $300 + (3 × hourly rate)

**Scenario 2: System Alert Monitoring (No Development)**
- Issue: Multiple system alerts throughout the week, all auto-resolved
- Impact: None - systems functioning normally
- Response: On-call developers monitor, verify auto-resolution, no coding required
- Billing: Base fee only ($300 × 2 developers = $600)
- Total Cost: $600 (no additional development hours)

**Scenario 3: Indexer Outage Requiring Restart Only**
- Issue: Indexer stops processing Solana transactions at 2 AM
- Impact: Critical - users cannot see current prices or execute trades
- Response: On-call backend developer restarts service, monitors recovery (no code changes)
- Billing: $300 base fee (no development hours since only operational restart)
- Total Cost: $300

**Scenario 4: Trading Engine Failure Requiring Hotfix**
- Issue: DCA orders failing due to system update introducing bug at 10 PM Saturday
- Impact: Critical - automated trading strategies not functioning
- Response: On-call backend developer debugs, develops hotfix, tests, deploys, monitors
- Billing: $300 base fee + 4 hours of development time at standard rate
- Total Cost: $300 + (4 × hourly rate)

### Positive Consequences

- **Improved Uptime:** Critical incidents addressed within minutes/hours instead of 12-16 hours
- **Better User Experience:** Beta users receive professional support experience
- **Risk Mitigation:** Reduced exposure to extended outages and reputation damage
- **Team Fairness:** Burden distributed evenly, with fair compensation
- **Incident Learning:** Every incident response improves documentation and stability
- **Scalable Model:** Can extend to 24/7 follow-the-sun coverage as user base grows
- **Clear Expectations:** Developers know exactly what's expected during on-call week

### Negative Consequences

- **Increased Operational Cost:** Additional weekly expense for base fee + potential incident hours
- **Developer Stress:** On-call developers may experience anxiety or lifestyle disruption
- **Coordination Overhead:** Requires scheduling, handoffs, and clear escalation procedures
- **Potential for Fatigue:** Busy on-call week could impact developer productivity the following week
- **Documentation Burden:** Requires comprehensive runbooks and incident response procedures

### Formal Proposal Status

**Proposal Sent:** October 21, 2025
**Sent To:** Stakeholders (Zane, Naji, Greg, et al.)
**Sent By:** RatherLabs/Lucas Cufré

**Proposal Details:**
- Subject: "Implementation of 24/7 Maintenance Support for Cooking.gg"
- Coverage Model: Two developers (front-end + back-end) for Month 1
- Pricing: $300 USD per developer per week (flat fee) + development hours at standard rate
- Schedule: Weekly rotations (Monday 09:00 UTC-3 to following Monday 08:59 UTC-3)
- Review Period: Month 1 performance review to optimize coverage model

### Confirmation Criteria

Decision will be confirmed when:
- ✅ Formal proposal document sent to stakeholders
- ⏳ Base fee ($300/developer/week) and hourly rates approved
- ⏳ On-call rotation schedule created
- ⏳ Incident response procedures documented
- ⏳ Team agreement on scope and expectations
- ⏳ Stakeholder sign-off received

Expected approval: Week of October 21-25, 2025

## Compliance and Monitoring

### Success Metrics

1. **Response Time:** Mean time to acknowledge (MTTA) for critical incidents
   - Target: < 15 minutes for P0 incidents
   - Measurement: Incident tracking system timestamps

2. **Resolution Time:** Mean time to resolve (MTTR) for critical incidents
   - Target: < 2 hours for P0 incidents (restore service)
   - Target: < 4 hours for P1 incidents
   - Measurement: Incident tracking system

3. **Uptime Improvement:** Platform availability during off-hours
   - Target: 99.5% uptime including off-hours
   - Measurement: Monitoring dashboards (Sentry, AWS CloudWatch)

4. **Incident Volume:** Number of after-hours incidents requiring response
   - Track to identify patterns and invest in preventive measures
   - Target: Decreasing trend over time as stability improves

5. **False Escalations:** Incidents escalated but not requiring immediate action
   - Track to refine escalation criteria
   - Target: < 20% of escalations are false alarms

### Review Points

- **Weekly:** Review incidents from previous on-call rotation
- **Monthly:** Analyze trends, costs, and effectiveness
- **Quarterly:** Assess whether to continue, modify, or expand coverage model

### Cost Structure Summary

**Month 1 (Two-Developer Model):**
- Base Cost per Week: $600 ($300 × 2 developers)
- Base Cost per Month: ~$2,400 (4 weeks)
- Variable Cost: Development hours at standard rate (as needed)
- Estimated Total Monthly Range: $2,400 - $4,000 (assuming 0-20 hours of active development)

**Post-Month 1 (Adjusted Model - TBD):**
- Coverage model to be optimized based on actual incident data
- Potential reduction to single developer if incident patterns support it
- Base Cost per Week: $300-$600 (depending on coverage model)

### Cost Controls

- Monthly budget tracking for on-call expenses
- Escalation for incidents requiring > 8 hours of continuous work
- Regular review of incident patterns to invest in preventive measures
- Goal: Reduce incident frequency through improved monitoring and stability
- Month 1 review to optimize coverage model and reduce costs

## Pros and Cons of the Chosen Option

### Pros

- ✅ Provides necessary 24/7 coverage for beta phase
- ✅ Fair and transparent compensation model
- ✅ Sustainable and scalable approach
- ✅ Distributes responsibility across team
- ✅ Enables rapid incident response
- ✅ Protects platform reputation during critical beta phase
- ✅ Clear scope prevents scope creep into non-critical work
- ✅ Cost-effective compared to full 24/7 staffing

### Cons

- ❌ Additional operational expense
- ❌ Potential developer stress during on-call weeks
- ❌ Requires discipline to avoid scope creep
- ❌ Coordination and scheduling overhead
- ❌ May be unnecessary if incident volume is very low
- ❌ Could impact developer productivity during/after on-call weeks

## Links and References

### Related Meetings
- [2025-10-20 Weekly Sync](../../06-meetings/2025-10/2025-10-20-weekly-sync.md) - Initial proposal discussion

### Related ADRs
- [ADR-203: September Beta Launch Timeline](2025-08-11-september-beta-launch-timeline.md) - Context on beta user expectations
- [ADR-302: Feature Freeze for Stability](2025-08-11-feature-freeze-for-stability.md) - Related stability focus

### Related Requirements
- Beta user onboarding and support expectations
- Platform SLA targets (99.5%+ uptime)

### Technical Context
- AWS infrastructure dependencies (see [2025-10-20 Weekly Sync](../../06-meetings/2025-10/2025-10-20-weekly-sync.md))
- Indexer reliability and common failure modes
- Trading engine and wallet infrastructure dependencies

### Next Steps

1. **Document Formal Proposal** (Lucas Cufré)
   - Detailed compensation structure
   - Base fee amounts
   - Hourly rate confirmation
   - Rotation schedule template
   - Due: October 21, 2025

2. **Create Incident Response Runbooks** (Development Team)
   - Indexer recovery procedures
   - Trading engine troubleshooting
   - Common failure scenarios
   - Escalation matrix
   - Due: Before first on-call rotation

3. **Set Up Incident Tracking** (DevOps/Lucas)
   - Incident logging system
   - Paging/alerting mechanism
   - On-call schedule visibility
   - Due: Before first on-call rotation

4. **Stakeholder Approval** (Zane)
   - Review proposal
   - Approve budget
   - Confirm start date
   - Target: Week of October 21, 2025

5. **Team Training** (All Developers)
   - On-call responsibilities review
   - Runbook walkthrough
   - Practice incident scenarios
   - Target: Before first rotation

---

**Status:** Proposed (awaiting formal approval from Zane)
**Next Review:** Upon approval and after first 4-week trial period
**Owner:** Lucas Cufré (Project Lead)
