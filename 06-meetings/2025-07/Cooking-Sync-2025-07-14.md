---
title: Cooking Mobile App Design Kickoff
type: meeting-note
date: 2025-07-14
attendees: [Lucas Cufré, Naji Osmat, Greg Chapman, Vadim Pleshkov, Varya Nekhina]
meeting-type: planning
tags: [cooking, mobile, design, ux, evilmartians, ratherlabs]
summary: |
  Initial kickoff meeting between Cooking team and Evil Martians design team for mobile app development. Discussed project scope, timeline constraints, and design approach for creating a simplified mobile companion app to the existing web platform. Key decisions included using native iOS components with custom styling, targeting September beta launch, and focusing on simplified UX for non-crypto native users.
related-docs:
  - Login and Home Flow Design Document
  - Wallet Management and Portfolio Overview Initiative
  - User Settings and Account Management Document
---

# Cooking Mobile App Design Kickoff

**Date:** 2025-07-14
**Time:** 11:34 - (approximately 1 hour)
**Attendees:** Lucas Cufré (RatherLabs), Naji Osmat (Cooking), Greg Chapman (Cooking), Vadim Pleshkov (Evil Martians), Varya Nekhina (Evil Martians)
**Facilitator:** Lucas Cufré

## Executive Summary

This meeting served as the official kickoff between the Cooking team and Evil Martians design team for the mobile application development project. The primary focus was establishing the design direction, scope, and timeline for creating a simplified mobile companion app to Cooking's existing web trading platform.

The team aligned on creating a mobile experience that prioritizes simplicity and accessibility for non-crypto native users, contrasting with the advanced trading features of the web platform. The mobile app will leverage native iOS components with custom styling to meet an aggressive September beta deadline while maintaining a premium feel. Evil Martians was recommended by the previous design agency (Ooze Design) specifically for their UX expertise, which is critical for the mobile experience.

Key agreements included running two-week sprints for design work, creating a comprehensive screen map before detailed design, and maintaining close collaboration between design and development teams. The immediate next steps involve Vadim conducting a detailed scope review with Lucas, followed by initial design work on the Wallet Management and Portfolio Overview features while development continues on the login flow.

## Action Items

- [ ] **Schedule detailed scope review call with Lucas** - Assigned to: Vadim Pleshkov - Due: 2025-07-14 - Priority: High
- [ ] **Share previous wallet app UX examples and flows** - Assigned to: Greg Chapman/Naji Osmat - Due: 2025-07-15 - Priority: Medium
- [ ] **Check internal policy for Notion access and provide if possible** - Assigned to: Lucas Cufré - Due: 2025-07-15 - Priority: Medium
- [ ] **Send official reply email regarding VM discussion** - Assigned to: Naji Osmat - Due: 2025-07-14 - Priority: High
- [ ] **Share User Settings and Account Management document** - Assigned to: Lucas Cufré - Due: 2025-07-14 - Priority: High
- [ ] **Create comprehensive app screen map/flow** - Assigned to: Vadim Pleshkov - Due: 2025-07-21 - Priority: High
- [ ] **Prepare GitBook documentation site** - Assigned to: Lucas Cufré - Due: Ongoing - Priority: Medium
- [ ] **Begin design work on Wallet Management and Portfolio Overview** - Assigned to: Vadim Pleshkov - Due: 2025-07-21 - Priority: High

## Index

1. Project Structure and Team Introductions
2. Design Approach and Technology Decisions
3. Timeline and Deadline Constraints
4. User Experience Philosophy and Competitive Positioning
5. Working Process and Sprint Planning
6. Current Development Status and Roadmap

---

## Topics: Breakdown

### Topic 1: Project Structure and Team Introductions

#### Executive Summary
The meeting began with introductions and clarification of team structures. RatherLabs handles development and product design, while Cooking manages business stakeholders. Evil Martians was brought in specifically for mobile UX/UI expertise, as the previous agency (Ooze Design) only handles UI without UX capabilities.

#### Key Takeaways
- Weekly syncs on Mondays for product updates and roadmap adjustments
- Friday demos for development and design decisions
- Evil Martians team: Vadim (design lead) and Varya (coordination)
- Mobile engineer already working on initial login/home flow
- Backend APIs from web app will be reused for mobile

#### Discussion Details
The team clarified pronunciation of names and established communication protocols. Lucas explained that this is their regular weekly sync where product updates and task priorities are discussed. The existing development team includes blockchain specialists, backend/frontend developers, a mobile iOS engineer, and a tech lead.

---

### Topic 2: Design Approach and Technology Decisions

#### Executive Summary
The team aligned on using native iOS components with custom styling to balance performance, deadline constraints, and brand identity. The goal is to avoid looking like a stock application while leveraging native performance benefits.

#### Key Takeaways
- Use previous iOS component set (not new Liquid Glass design)
- Customize stock components to maintain Cooking brand identity
- Aim for Robinhood-like simplicity without full custom UI complexity
- Focus on performance through native components
- Progressive design approach starting with low-resolution screens

#### Discussion Details
Discussion covered the trade-offs between fully custom UI (like Robinhood) and stock iOS components. The team agreed that while Robinhood's custom interactions are ideal, they're not achievable within the timeline. The compromise is to modify stock iOS components to look as custom and "Cooking-branded" as possible while maintaining native performance benefits.

---

### Topic 3: Timeline and Deadline Constraints

#### Executive Summary
September beta launch is a firm deadline with no flexibility due to commitments to high-profile partners and KOLs. The team needs designs completed by early September to allow 15-20 days for QA and testing before the beta release.

#### Key Takeaways
- September beta launch is non-negotiable
- Stepped release starting with 100 close partners
- Need 15-20 days for QA and testing
- Initial two-week sprint to establish scope and velocity
- Designs needed by early September for testing window

#### Discussion Details
Greg emphasized the importance of first impressions with their initial 100 users being close partners and influencers. The stepped release approach will gradually expand access. Varya explained Evil Martians' two-week sprint approach and need for initial days to understand scope before providing accurate estimates.

---

### Topic 4: User Experience Philosophy and Competitive Positioning

#### Executive Summary
The mobile app targets non-crypto native users with a simplified, intuitive experience contrasting with the complex web platform. The focus is on making crypto trading accessible to mainstream users through step-by-step flows and clear explanations.

#### Key Takeaways
- Mobile app is simplified companion to advanced web platform
- Target audience: normies/non-crypto natives
- Competitive edge: best UX in mobile crypto trading
- Need for educational elements (what is a seed phrase, meme coins, etc.)
- Step-by-step flow approach for complex operations

#### Discussion Details
The team discussed how current Web3 applications fail at UX, citing examples like Axiom which looks premium but assumes too much user knowledge. Greg shared examples of a previous wallet app that broke down complex operations into simple step-by-step flows. The approach should make it impossible for users to misunderstand what they're doing, similar to how Robinhood reimagined trading interfaces for mainstream users.

---

### Topic 5: Working Process and Sprint Planning

#### Executive Summary
Evil Martians will run two-week sprints with increased communication during the initial knowledge transfer phase. The team will create a comprehensive screen map before detailed design work to properly scope the project and identify potential cuts if needed.

#### Key Takeaways
- Two-week sprint cycles
- Daily/every-other-day check-ins initially
- Create full app map before detailed design
- Progressive refinement approach
- Potential NDA signing for documentation access

#### Discussion Details
Varya outlined their working methodology: starting with mapping all screens and flows, then progressively refining designs. This approach allows for better estimation and identification of features that may need to be postponed or simplified to meet deadlines. Initial weeks will require frequent communication for knowledge transfer.

---

### Topic 6: Current Development Status and Roadmap

#### Executive Summary
Development is already underway on the login/home flow based on existing designs. The roadmap prioritizes core features in sequence, with Wallet Management and Portfolio Overview as the next major initiative after login.

#### Key Takeaways
- Current work: Sign-up, login, and home flow
- Next priority: Wallet Management and Portfolio Overview
- Following: Token Detail Screen and Trading Operations
- User Settings and Account Management ready for sharing
- On-ramp feature still under discussion

#### Discussion Details
Lucas screen-shared the current development work including login flow, terms acceptance, referral system, and home screen with token filters. The mobile engineer is aware designs will change but is proceeding with implementation. The team will be blocked on further development once current designs are exhausted, expected by end of week.

---

## Decisions Made

1. **Use native iOS components with custom styling** - Balance between performance and brand identity - No ADR needed
2. **Two-week sprint cycles for design work** - Allows for iterative refinement and scope adjustment
3. **Create comprehensive screen map before detailed design** - Ensures full scope understanding before commitment
4. **Focus on Wallet Management after login flow** - Maintains development momentum while other features are designed
5. **Target simplified UX for non-crypto natives** - Clear differentiation from complex web platform

## Blockers and Risks Identified

- **Design dependency for development** - Impact: High - Owner: Vadim/Lucas - Needs resolution by: 2025-07-21
- **Tight timeline for September launch** - Impact: High - Owner: All - Ongoing monitoring required
- **Scope uncertainty requiring estimation** - Impact: Medium - Owner: Vadim/Varya - Needs resolution by: 2025-07-18

## Parking Lot

- On-ramp feature implementation details
- Specific integration requirements
- Academy/educational content scope
- Deployment and monitoring strategies

## Next Steps

- Immediate detailed scope review call between Vadim and Lucas
- Begin work on Wallet Management and Portfolio Overview designs
- Establish daily check-ins for first week of knowledge transfer
- Complete application screen mapping within first sprint
- Friday demo to include Evil Martians team going forward

## References

- Login and Home Flow Design Document
- Wallet Management and Portfolio Overview Initiative
- Previous wallet app UX examples (to be shared)
- Ooze Design website: [shared in meeting]
- GitBook documentation (in preparation)