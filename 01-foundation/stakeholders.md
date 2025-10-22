---
title: Stakeholder Analysis
type: stakeholder-analysis
date: 2025-10-17
last-updated: 2025-10-19
status: active
owner: Lucas Cufré
tags: [foundation, stakeholders, governance, communication]
summary: |
  Comprehensive stakeholder analysis for Cooking.gg including team members,
  product stakeholders, and external partners based on meeting attendance
  and project engagement from June-October 2025.
related-docs:
  - project-charter.md
  - ../03-active-work/_current-status.md
  - ../06-meetings/_meetings-index.md
---

# Stakeholder Analysis - Cooking.gg

**Last Updated:** 2025-10-19
**Beta Launch Target:** October 27, 2025

## Stakeholder Overview

This document identifies all stakeholders based on meeting attendance and project engagement from June-October 2025. Stakeholders are categorized by their role, influence, and engagement patterns observed through 82+ team meetings.

## Stakeholder Matrix

### Power/Interest Grid

| High Power, High Interest | High Power, Low Interest |
|---------------------------|-------------------------|
| **Manage Closely** | **Keep Satisfied** |
| Z (Primary Stakeholder)<br>Lucas Cufré (Product Lead)<br>Martin Aranda (Tech Lead) | Marcos Tacca (Head of Projects) |

| Low Power, High Interest | Low Power, Low Interest |
|-------------------------|------------------------|
| **Keep Informed** | **Monitor** |
| Development Team<br>Gregory Chapman<br>Naji Osmat<br>Shakeib Shaida | External Partners<br>RatherLabs |

## Executive & Product Stakeholders

### Z (Zane) - Primary Product Stakeholder
**Role/Title:** Product Owner / Primary Stakeholder
**Interest:** Product vision, market fit, beta launch success, user acquisition
**Influence Level:** High
**Impact on Project:** Critical
**Meeting Attendance:** Weekly syncs, mobile planning, demo meetings

**Key Concerns:**
- Time to market and beta launch readiness
- Product stability and user experience
- Echo integration performance vs Jupiter reliability
- Competitive positioning and feature completeness

**Engagement Strategy:**
- **Frequency:** Weekly sync meetings (Z & Lucas Sync)
- **Method:** Direct meetings, mobile planning sessions, demo reviews
- **Key Messages:** Product progress, technical decisions, timeline updates, risk mitigation

**Success Criteria from Their Perspective:**
- Successful beta launch on October 27, 2025 with 30-40 users
- Stable, performant trading platform
- Positive user feedback and engagement
- Competitive mobile experience

**Recent Decisions:**
- Proceed with Jupiter-based engine over Echo for stability (Oct 16)
- Phased beta rollout strategy (Oct 16)
- Focus on Chrome + Safari for initial release (Oct 16)

---

### Gregory Chapman - Secondary Stakeholder
**Role/Title:** Product Stakeholder / Client Representative
**Interest:** Feature delivery, UI/UX quality, documentation, stakeholder communication
**Influence Level:** High
**Impact on Project:** High
**Meeting Attendance:** Weekly demos, mobile planning meetings

**Key Concerns:**
- Mobile app haptic design and interaction patterns
- Documentation for Ramper integration
- UI consistency and design fidelity
- Timeline adherence for stakeholder presentations

**Engagement Strategy:**
- **Frequency:** Weekly demo meetings
- **Method:** Product demonstrations, design reviews, documentation reviews
- **Key Messages:** Feature completion status, design decisions, integration progress

---

### Naji Osmat & Shakeib Shaida - Supporting Stakeholders
**Role/Title:** Product Team / Stakeholders
**Interest:** Design implementation, user experience, feature planning
**Influence Level:** Medium
**Impact on Project:** Medium
**Meeting Attendance:** Demo meetings, mobile planning sessions

**Engagement:** Participate in design reviews and mobile app planning

---

## Project Leadership

### Lucas Cufré - Product Lead & Project Manager
**Role/Title:** Product Lead
**Responsibility:** Overall delivery, client relations, coordination, decision-making
**Influence Level:** High
**Impact on Project:** Critical
**Meeting Attendance:** All meetings (daily standups, demos, syncs, technical discussions)

**Key Responsibilities:**
- Sprint planning and execution
- Client/stakeholder communication
- Risk management and decision-making
- Beta launch coordination
- Team coordination and prioritization

**Key Focus Areas:**
- Beta launch preparation (Oct 27 target)
- Echo integration challenges and mitigation
- Safari compatibility and UI polish
- Performance optimization
- Documentation and knowledge management

---

### Martin Aranda - Technical Lead
**Role/Title:** Tech Lead / Solutions Architect
**Responsibility:** Technical architecture, infrastructure, system design
**Influence Level:** High
**Impact on Project:** Critical
**Meeting Attendance:** All technical meetings, daily standups, demos

**Key Responsibilities:**
- Architecture decisions and technical direction
- Transaction routing optimization (Jupiter, Echo)
- Infrastructure and DevOps
- Performance optimization
- Technical problem-solving

**Key Technical Achievements:**
- Transaction time optimization: 5-6s → 2-3s
- Microservices refactoring
- Jupiter transaction optimization (7→3 hops)
- Nonce account implementation for offline signing

---

### Marcos Tacca - Head of Projects
**Role/Title:** Head of Projects
**Responsibility:** Project oversight, resource allocation
**Influence Level:** Medium-High
**Impact on Project:** Medium
**Meeting Attendance:** Demo meetings, strategic discussions

**Engagement:** Strategic oversight and resource management

---

## Development Team

### Backend & Blockchain Team

#### Eduardo Yuschuk - Backend/Indexer Lead
**Role/Title:** Backend Developer / Blockchain Specialist
**Responsibility:** Solana indexer, database optimization, blockchain integrations
**Influence Level:** High (Technical)
**Impact on Project:** Critical
**Meeting Attendance:** Daily standups, technical discussions

**Key Focus Areas:**
- Solana blockchain indexing (Jupiter, Raydium, Pump.fun, Launch Lab)
- ClickHouse performance optimization (2x improvement achieved)
- Liquidity pool indexing and multi-protocol support
- Transaction validation and security

**Technical Contributions:**
- Multi-protocol indexer architecture
- Query optimization and performance improvements
- Indexing latency management (<200ms target)

---

#### Ramiro Carracedo - Backend Developer
**Role/Title:** Backend Developer
**Responsibility:** Backend services, API development
**Influence Level:** Medium
**Meeting Attendance:** Daily standups

---

#### Federico Caffaro - Backend Developer
**Role/Title:** Backend Developer
**Responsibility:** Backend services, data management
**Influence Level:** Medium
**Meeting Attendance:** Daily standups

**Focus Areas:** Token supply data, holder tracking, wallet management

---

#### Esteban Restrepo - Backend Developer
**Role/Title:** Backend Developer
**Responsibility:** Transaction processing, referral system
**Influence Level:** Medium
**Meeting Attendance:** Daily standups

**Key Contributions:**
- Referral program implementation
- Transaction error handling and mapping
- Fee wallet management

---

#### Darío Balmaceda - Backend Developer
**Role/Title:** Backend Developer
**Responsibility:** Database queries, performance optimization
**Influence Level:** Medium
**Meeting Attendance:** Daily standups

**Key Achievement:** Mint and Kitchen query template improvements (2x performance)

---

### Frontend Team

#### Luis Rivera - Frontend Developer
**Role/Title:** Frontend Developer
**Responsibility:** UI implementation, advanced orders, settings
**Influence Level:** Medium
**Meeting Attendance:** Daily standups

**Key Focus Areas:**
- Advanced orders UI
- Settings refactoring
- Learn More modals
- UI component development

---

#### Germán Derbes Catoni - Frontend Developer
**Role/Title:** Frontend Developer
**Responsibility:** UI implementation, Safari compatibility
**Influence Level:** Medium
**Meeting Attendance:** Daily standups

**Key Focus:** Safari compatibility, typography fixes, alignment issues

---

#### Marko Jauregui - Fullstack Developer
**Role/Title:** Fullstack Developer
**Responsibility:** UI components, toast notifications, full-stack features
**Influence Level:** Medium
**Meeting Attendance:** Daily standups

**Focus Areas:** Toast notifications, UI components, bug fixes

---

#### Martín Lecam (Willy) - Fullstack Developer
**Role/Title:** Fullstack Developer
**Responsibility:** Order history, filters, full-stack features
**Influence Level:** Medium
**Meeting Attendance:** Daily standups

**Focus Areas:** Order filters, order history, data visualization

---

### Mobile Team

#### Byron Chavarria - Mobile Lead
**Role/Title:** iOS Developer / Mobile Lead
**Responsibility:** iOS app development, mobile features
**Influence Level:** High (Mobile)
**Impact on Project:** High
**Meeting Attendance:** Daily standups, mobile planning meetings

**Key Focus Areas:**
- iOS app development (iOS 16, 18.3 compatibility)
- Token detail screens
- Navigation and routing
- TestFlight deployment

**Recent Achievement:** Navigation issue resolution for iOS 16 and 18.3

---

### Design Team

#### Santiago Gimenez - UX Designer
**Role/Title:** UX Designer
**Responsibility:** UI/UX design, mobile design patterns
**Influence Level:** Medium
**Meeting Attendance:** Mobile planning, design reviews

**Key Contributions:**
- Mobile haptic design patterns
- Interaction design for trade actions
- Filter design (special mode)

---

## End User Groups

### Solana Meme Coin Traders
**Description:** Crypto traders focused on Solana-based meme coins and tokens, particularly early-stage tokens on bonding curves
**Size:** Beta launch: 30-40 users (Oct 27, 2025 target), post-launch: thousands
**Influence Level:** Low (indirect, through feedback)
**Impact:** High (primary users we're building for)

**Needs and Expectations:**
- Fast transaction execution (2-3 second confirmations)
- Reliable trading platform with minimal failures
- Mobile-first experience with intuitive UI
- Access to new tokens (Pump.fun, Raydium, etc.)
- Competitive pricing and low fees
- Real-time portfolio tracking

**Engagement Strategy:**
- **Frequency:** Beta testing phase (ongoing feedback)
- **Method:** Beta program, user feedback, analytics, referral program
- **Representation:** Product team voices user needs in planning

**Success Criteria from Their Perspective:**
- Trades execute quickly and reliably
- Easy to discover and trade new meme coins
- Mobile app feels responsive and polished
- Competitive with or better than alternatives

---

## External Partners & Integrations

### Ramper - KYB/Compliance Partner
**Role:** Know Your Business (KYB) compliance and documentation
**Interest:** Compliance standards, documentation review
**Influence Level:** Medium
**Impact on Project:** Medium (required for launch)

**Status:** KYB for Don Ramper completed, awaiting documentation approval (as of Oct 17)

**Engagement:** Documentation reviews, compliance checkpoints

---

### RatherLabs / Kensei - Potential Partner
**Role:** External development partner discussions
**Interest:** Partnership opportunities
**Influence Level:** Low
**Meeting History:** Aug 8, Aug 11, 2025

**Status:** Past discussions, not currently active

---

## Third-Party Technology Partners

### Echo - Trading Router Provider
**Role:** Advanced trading router technology
**Status:** Integration evaluated but not deployed (Oct 2025)
**Influence Level:** Low (vendor)
**Impact:** Medium (alternative technology option)

**Key Issues Identified:**
- Performance concerns (60% failure rate in testing)
- Architectural incompatibilities
- Decision: Not using for initial launch, Jupiter chosen instead

---

### Jupiter - DEX Aggregator
**Role:** Primary transaction routing provider
**Status:** Active integration, primary trading engine
**Influence Level:** Medium (critical vendor)
**Impact:** Critical (core functionality)

**Engagement:** API integration, optimization partnership

---

## Stakeholder Communication Plan

### Regular Updates

| Stakeholder Group | Frequency | Method | Content | Owner |
|------------------|-----------|--------|---------|-------|
| Z (Primary Stakeholder) | Weekly | Sync Meeting | Strategic decisions, progress, risks | Lucas Cufré |
| Product Stakeholders (Greg, Naji, Shakib) | Weekly | Demo Meeting | Feature demos, UI reviews, progress | Lucas Cufré |
| Development Team | Daily | Stand-up | Sprint progress, blockers, coordination | Lucas Cufré / Martin Aranda |
| Project Leadership | Daily | Stand-up + Ad-hoc | Technical decisions, architecture, problem-solving | Martin Aranda |
| Beta Users | As needed | In-app + Feedback | Beta testing, user experience feedback | Product Team |

### Escalation Paths

| Issue Type | First Contact | Escalation Level 1 | Escalation Level 2 |
|-----------|---------------|-------------------|-------------------|
| Technical blocker | Martin Aranda (Tech Lead) | Lucas Cufré (Product Lead) | Z (Primary Stakeholder) |
| Scope question | Lucas Cufré | Z (Primary Stakeholder) | Marcos Tacca |
| Resource constraint | Lucas Cufré | Marcos Tacca | Z |
| External dependency (Echo, Jupiter, etc.) | Martin Aranda | Lucas Cufré | Z |
| Performance/quality issues | Eduardo Yuschuk / Martin Aranda | Lucas Cufré | Z |

## Stakeholder Risks

### High-Risk Stakeholder Situations

**Risk:** Echo integration pressure from stakeholder vs technical reality
- **Likelihood:** Medium (occurred Oct 2025)
- **Impact:** High (could delay launch or compromise quality)
- **Mitigation:** Clear documentation of technical limitations, professional recommendations documented, chose Jupiter for stability
- **Status:** Resolved - proceeded with Jupiter-based engine

**Risk:** Beta launch timeline pressure (Oct 27 target)
- **Likelihood:** Medium
- **Impact:** High (stakeholder expectations, market timing)
- **Mitigation:** Phased rollout strategy (5 internal → 30-40 beta → full launch), clear communication of risks, Safari + Chrome focus for initial release
- **Status:** Active monitoring

**Risk:** Competing priorities across development team
- **Likelihood:** Medium
- **Impact:** Medium (could slow velocity)
- **Mitigation:** Daily standups, clear prioritization from Lucas, focus on frontend polish for stakeholder reviews

## Stakeholder Engagement Tracking

### Recent Key Engagements (October 2025)

| Date | Stakeholder | Activity | Outcome | Impact |
|------|-------------|----------|---------|--------|
| Oct 17 | Z, Greg, Naji | Demo Meeting | Product progress shown, Dubai travel coordinated | Positive feedback on performance improvements |
| Oct 16 | Z, Greg, Naji | Mobile Planning | Haptic design approved, beta strategy confirmed | Decision to proceed with Jupiter engine |
| Oct 15 | Internal | Indexer Discussion | Echo integration issues documented | Professional recommendation not to launch Echo |
| Oct 14 | Internal | Liquidity Pools Discussion | Multi-protocol strategy clarified | Decision to limit Echo to Pump.fun and Launchlab only |
| Oct 13 | Z, Lucas | Sync Meeting | Strategic alignment | Limited notes available |
| Oct 11 | Internal | Echo Integration | Nonce account optimization discussed | 15k CU reduction achieved |
| Oct 10 | Z, Greg, Naji | Demo Meeting | Echo challenges and backup system reviewed | Positive on redundancy approach |

### Current Engagement Cadence

| Stakeholder | Meeting Type | Frequency | Last Meeting |
|-------------|-------------|-----------|--------------|
| Z | Sync Meeting | Weekly (Sundays) | Oct 13, 2025 |
| Z, Greg, Naji, Shakib | Demo Meeting | Weekly (Thursdays) | Oct 17, 2025 |
| Development Team | Daily Standup | Daily (weekdays) | Oct 17, 2025 |
| Mobile Planning | As needed | Bi-weekly | Oct 16, 2025 |
| Technical Discussions | As needed | Weekly | Oct 15, 2025 |

## Stakeholder Feedback and Sentiment

### Current Sentiment Analysis (as of Oct 19, 2025)

- **Z (Primary Stakeholder):** Positive - Satisfied with Jupiter decision and performance improvements, confident in beta timeline
- **Product Stakeholders (Greg, Naji, Shakib):** Positive - Appreciative of mobile design work and UI improvements
- **Development Team:** Neutral to Positive - Engaged but under pressure with Oct 27 deadline
- **Technical Leadership:** Positive - Confident in architecture decisions and performance gains

### Recent Feedback Themes (Oct 2025)

**Positive:**
- Performance improvements appreciated (5-6s to 2-3s transaction times)
- Mobile app design and haptics well-received
- ClickHouse optimizations delivering results (2x improvement)
- Team responsiveness to blockers

**Concerns:**
- Timeline pressure for Oct 27 beta launch
- Echo integration stability (led to decision not to use)
- Safari compatibility issues (being addressed)
- Documentation pending review from Ramper

**Requests:**
- UI polish and Safari compatibility completion
- TestFlight build for iOS testing
- GitBook documentation published under cooking.gg DNS
- Clear communication of technical limitations

## Project Champions & Influencers

### Active Champions

- **Z (Zane)** - Primary champion, drives product vision, approves strategic decisions, provides stakeholder alignment
- **Lucas Cufré** - Internal champion, manages stakeholder expectations, coordinates team, communicates progress
- **Martin Aranda** - Technical champion, makes architecture decisions, solves complex problems, mentors team

### Key Influencers

- **Gregory Chapman** - Influences product stakeholder group, represents client perspective in design decisions
- **Eduardo Yuschuk** - Technical influencer, indexer expertise shapes architecture decisions
- **Marcos Tacca** - Organizational influencer, resource allocation and strategic oversight

**Engagement Strategy for Champions:**
- Keep Z informed of all major decisions and risks early
- Involve Greg, Naji in design and UX reviews
- Leverage Martin and Eduardo for technical advocacy
- Maintain transparent communication on timeline and risks

## Team Dynamics Observations

Based on meeting patterns June-October 2025:

- **High Collaboration:** Daily standups show strong team coordination
- **Clear Leadership:** Lucas provides clear prioritization, Martin drives technical decisions
- **Proactive Problem-Solving:** Team raises blockers early and works collaboratively
- **Quality Focus:** Emphasis on testing, performance, and user experience
- **Transparent Communication:** Technical limitations clearly communicated to stakeholders

## Revision History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2025-10-17 | 1.0 | Initial stakeholder analysis template | Project Team |
| 2025-10-19 | 2.0 | Comprehensive update with actual team members and roles from 82+ meetings | Claude Code |

---

**Maintenance Notes:**
- Review stakeholder list monthly
- Update sentiment quarterly
- Revisit engagement strategies when project phase changes
- Add new stakeholders as they are identified
