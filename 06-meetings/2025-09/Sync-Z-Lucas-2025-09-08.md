---
title: Sync Z <> Lucas - Roadmap Review & Security Planning
type: meeting-note
date: 2025-09-08
attendees: [Lucas Cufré, Zen, Marcos Tacca]
meeting-type: weekly-sync
tags: [sync, roadmap, security-audits, feature-parallelization, dubai-trip, billing]
summary: |
  Roadmap review session confirming priority features (1-8) already included in current timeline. Discussion of feature parallelization opportunities, MEV protection complexity, and security audit requirements for beta launch. Lucas clarified testing approach includes QA, stress testing (500 concurrent users), and security password protection. Dubai office still under construction - November trip will use cafe workspaces. Invoice sent with $8K refund for Hyperliquid refactor time.
related-docs:
  - Project roadmap Gantt chart
  - Feature prioritization spreadsheet
  - Security audit requirements
---

# Sync Z <> Lucas - Roadmap Review & Security Planning

**Date:** 2025-09-08
**Duration:** ~22 minutes
**Attendees:** Lucas Cufré, Zen, Marcos Tacca
**Meeting Type:** Weekly Sync / Roadmap Review

## Executive Summary

Detailed roadmap and feature prioritization review ahead of executive presentation. Lucas clarified that priority items 1-8 (AI trading journal, wallet tracker, backoffice) are already included in current roadmap. Discussion revealed opportunities for feature parallelization (saving filters, trading presets) and complexity of XFeed/MEV protection integration. Security audit planning emerged as key topic - Lucas outlined current testing approach (internal QA, stress testing, security password layer) but acknowledged need for external security audits before beta launch. Dubai trip logistics updated: office under construction, November sessions will be in cafes with full office ready by January.

## Discussion Topics

### Current Roadmap Status and Priority Features

**Context:** Zen preparing for executive call to review Gantt chart and feature spreadsheet

**Lucas Clarification on Included Features (Priority 1-8):**
- ✅ AI-assisted trading journal
- ✅ Watchlist
- ✅ Wallet tracker
- ✅ Backoffice
- ✅ All priority items through #8

**Not Yet in Roadmap:**
- Items after "Advanced Filtering" onward

**Timeline:** 00:00:00 - 00:04:37

---

### Feature Parallelization Opportunities

**Parallelizable Features (Similar Implementation):**
- Saving filters
- Trading presets
- Other user settings storage features

**Rationale:** Same underlying functionality, just applied to different use cases

**Quick Implementation Items:**
- **PNL Screenshots:** "Few days with testing"
- **Holder Table Charts:** "Can be included fairly quickly"

**Market Cap Variation Algorithm:**
- **Status:** Extensively considered over past months
- **Implementation Time:** ~2 days coding
- **Testing Time:** Majority of effort (involves user money)
- **Total Estimate:** ~2 weeks including comprehensive testing

**Timeline:** 00:04:37 - 00:08:07

---

### XFeed and MEV Protection Complexity

**Research Findings:**
- More complex than initially assessed
- Requires interaction with X platform
- Bribe feature is critical component

**MEV Protection Details:**
- **Smart MEV Protection and Bribe are linked**
- **Bribe acts as priority fee for private mempools**
- **Without private mempool:** Bribe only increases transaction cost without providing edge
- **Requirement:** Both features must be implemented together

**Lucas Assessment:** These two features are interconnected and cannot be separated

**Timeline:** 00:04:37 - 00:06:21

---

### Testing, Quality Assurance, and Timeline

**Current Roadmap (Gantt Chart):**
- Extends through mid-December
- **All testing included** in time estimates
- "Perceived effort" column includes testing time
- Upon completion: feature should be production-ready and deployed

**Testing Approach:**

**1. Bug Detection:**
- Developers testing internally
- Dedicated QA engineer
- Simulating actual user workflows

**2. Stress Testing:**
- Headless browser automation
- Concurrent user simulation
- **Current Capacity:** 500 concurrent sessions
- **Assessment:** Sufficient for beta, not ideal for full production

**3. Performance Optimization:**
- DevOps engineer working on improvements
- Focus areas: Screen loading times, identified bottlenecks

**Timeline:** 00:08:07 - 00:11:38

---

### Security Measures and Audit Planning

**Current Security Implementation:**

**Security Password Layer:**
- **Purpose:** Protect against credential compromise
- **Trigger Actions:** Withdrawing funds, transferring to saved/external wallets
- **Protection Scope:** Even if attacker gains Gmail/Telegram access, cannot withdraw funds without security code
- **Trade-off:** Adds friction but prevents unauthorized fund movement

**Phishing Attack Research:**
- Most reported attacks come from phishing situations
- Security code mitigates this attack vector

**External Security Audits:**

**Zen's Questions:**
- Plans for security analysis beyond pen testing/stress testing
- Code base verification
- Ensuring no vulnerabilities for beta launch
- Audit requirements (unusual since not smart contract/marketplace/staking)
- Backend and account management security

**Lucas Response:**
- Currently following best practices in design and coding
- Can engage external firms for security audits
- **Not previously discussed** in roadmap scope
- **Willing to add** security audit phase

**Zen's Clarification:**
- R Rather Labs should suggest required audits
- Part of delivering "functional secure product"
- Should be proactive recommendation, not client request

**Action:** Bring up with Shakib in next call for his technical perspective

**Timeline:** 00:09:43 - 00:15:40

---

### Dubai Trip Planning and Office Status

**Travel Party:**
- Martin
- Lucas
- F
- Franco

**Purpose:** Understand workspace and expected work session outcomes

**Dubai Office Status:**
- **Current:** Under construction
- **Space:** Warehouse being converted to 2-level office
- **Timeline:** May not be ready for November trip
- **November Plan:** Brainstorm sessions in cafes/co-working spaces
- **January:** Full office ready with all teams (operating, marketing, etc.)
- **Team Members in Dubai:** Shakib, Zen, Greg

**Zen's Perspective on In-Person Work:**
- Strongly prefers in-person collaboration
- "Really good way of building trust"
- Important for long-term venture success
- Dislikes remote work personally
- Crucial for team chemistry development

**Trip Decisions:**
- **November Trip:** Proceed as planned (first week)
- **Future Trip:** Early-to-mid next year when office complete
- **Benefits:** Own workspace, meet full team

**Timeline:** 00:15:40 - 00:18:33

---

### Billing and Financial

**Invoice Status:**
- Sent previous week
- **Refund Included:** $8,000 for Hyperliquid refactor timeline
- Lucas requested confirmation if Zen has questions

**Timeline:** 00:18:33

---

## Action Items

| Owner | Action | Deadline | Status |
|-------|--------|----------|--------|
| Lucas & Team | Investigate security audit firms | Before next call | Committed |
| Lucas | Suggest required security audits/penetration testing | Before beta launch | Committed |
| Lucas | Discuss security audit with Shakib | Start of next call | Committed |
| Lucas | Confirm November Dubai trip details with team | First week November | Committed |
| Zen | Review invoice and confirm receipt | ASAP | Pending |

## Technical Details

### Roadmap Timeline
- **Current End Date:** Mid-December
- **Beta Launch Target:** End of September (discussed in context)
- **Features Included:** Priority 1-8, with parallelizable items identified
- **Testing:** Fully integrated into timeline estimates

### Performance Metrics
- **Stress Test Capacity:** 500 concurrent users
- **Assessment:** Beta-ready, production scaling needed
- **Optimization Focus:** Loading times, identified bottlenecks

### Security Architecture
- **Layer 1:** Turnkey integration for account management
- **Layer 2:** Security password for fund movements
- **Layer 3:** (Proposed) External security audit
- **Attack Vectors:** Phishing protection via security code

### Feature Complexity Assessment
| Feature | Complexity | Timeline | Notes |
|---------|-----------|----------|-------|
| PNL Screenshots | Low | Few days | Quick win |
| Holder Table Charts | Low | Quick | Easy addition |
| Market Cap Algorithm | Medium | 2 weeks | Mostly testing |
| Saving Filters/Presets | Low | Parallelizable | Similar implementation |
| XFeed + MEV Protection | High | TBD | Linked features, complex |

## Meeting Conclusion

**Duration:** 00:21:54
**Key Outcomes:**
- Roadmap clarity for executive presentation
- Security audit requirements identified
- Dubai trip confirmed with workspace expectations set
- Feature parallelization opportunities mapped

---

## Transcript Highlights

### Feature Parallelization (00:04:37)
```
Lucas: "There are some of these that can be parallelized are all of the things
that require vacant saving of the user settings. For instance, the saving filters,
the trading presets, all of those are things that can be done in parallel because
they are pretty much the same feature, just aimed at different situations."
```

### MEV Protection Complexity (00:06:21)
```
Lucas: "The brive acts as the priority fee of the private mle. So yeah, those
two are linked together [Smart MEV protection and bribe]."

Zen: "So you're saying smart MEV protection and briber the same thing"

Lucas: "The PR [bribe] is a requirement... the brive acts as the priority fee
of the private mle."
```

### Security Password Protection (00:11:38)
```
Lucas: "If somebody were to have access to your account by way of acquiring your
credentials uh like your Gmail credentials or your Telegram account that is
something that we cannot we can do nothing about without harming the the speed
of execution but nobody could take your funds out of cooking without the security
code. So that is an extra step."
```

### Security Audit Discussion (00:14:38)
```
Zen: "It's a bit unusual because it's not um it's not like a smart contract type
of product. It's not like a marketplace or a staking product, but there is an
enormous backend and there is um obviously the account management for the users
and the turn key integration and stuff like this."

Lucas: "So security external security audits were not part of this discussion.
We can include them. No worries."

Zen: "On R lab side it's not just building the code it's making sure we have a
functional secure product so anything that's you know required whether it's
security audits or penetration testing or anything like this needs to be suggested
from R the lab side."
```

### In-Person Work Philosophy (00:17:05)
```
Zen: "For me, meeting in person and stuff is like a really good way of building
trust especially because this is a very longterm venture for us all and we're all
part of it. So, I don't really like the whole remote working thing for me personally.
I'm I'm very against it. I prefer working in person or meeting people in person,
spending time in person, and kind of like building bonds that way. Um, and I think
it's super crucial for something like this."
```

## Notes
- First detailed roadmap review with executive presentation context
- Security audit emerged as new requirement not in original scope
- Dubai office construction timeline impacts November visit format
- $8K refund reflects accurate time tracking for Hyperliquid work
- Shakib to be consulted on security audit approach (technical expertise)
