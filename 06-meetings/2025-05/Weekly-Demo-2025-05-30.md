---
title: Weekly Demo - May 30, 2025
type: meeting-note
date: 2025-05-30
attendees: [RatherLabs Team, Cooking Team]
meeting-type: review
tags: [cooking, development, weekly-demo, backend, frontend, indexer, hyperliquid, third-party-integration, mobile-planning]
summary: |
  Weekly development progress review featuring performance improvements, security enhancements, and critical strategic discussions about third-party integrations. Key developments include Positions performance optimization, Referral Program volume calculation fixes, security password implementation for Wallet Manager, and initial technical assessments for Jupiter and HyperLiquid integrations. The meeting included important alignment discussions about third-party involvement in development processes and the associated impact on delivery timelines.
related-docs:
  - [Third-party Integration Strategy]
  - [Mobile Development Roadmap]
  - [HyperLiquid DEX Integration Assessment]
---

# Weekly Demo - May 30, 2025

**Date:** 2025-05-30
**Time:** Not specified
**Attendees:** RatherLabs Development Team, Cooking Team
**Facilitator:** Not specified

## Executive Summary

This week's demo showcased significant technical progress alongside crucial strategic discussions about the platform's development approach and third-party dependencies. The backend team delivered performance improvements for Positions and Token Data retrieval, fixed critical volume calculation errors in the Referral Program, and implemented comprehensive security password logic for the Wallet Manager. Technical assessments continued for two major integrations: Jupiter's aggregated tokens listing and HyperLiquid's DEX integration.

The indexer team made progress on unicode JSON parsing errors for Solana blocks while continuing their assessment of the Jupiter and HyperLiquid integrations. Frontend development successfully addressed multiple bugs including filter reset issues, security password implementation, empty state handling for filters, and wallet archiving problems.

A critical strategic discussion took place regarding the involvement of third-party agents in the development process. The team addressed concerns about delivery timeline impacts when external parties are involved in definition, design, or development phases. Clear alignment was established for both desktop and mobile development approaches, with RatherLabs maintaining primary responsibility while coordinating with external contractors as needed. The meeting also highlighted important considerations about growing platform dependencies on third-party solutions like Jupiter's swap API and HyperLiquid's perpetual trading system.

## Action Items

- [ ] **Establish public Slack channel for external contractor communication** - Assigned to: Project Management - Due: Immediate - Priority: High
- [ ] **Complete Jupiter aggregated tokens technical assessment** - Assigned to: Backend/Indexer Teams - Due: Next week - Priority: High
- [ ] **Complete HyperLiquid DEX integration assessment** - Assigned to: Backend/Indexer Teams - Due: Next week - Priority: High
- [ ] **Document dependency risk assessment for third-party integrations** - Assigned to: Technical Lead - Due: Next sprint - Priority: Medium

## Index

1. Backend Development Progress
2. Indexer Improvements
3. Frontend Updates
4. Third-Party Integration Strategy Discussion
5. Desktop Development Approach
6. Mobile Development Approach
7. Platform Dependencies and Risk Assessment

---

## Topics: Breakdown

### Topic 1: Backend Development Progress

#### Executive Summary
Backend team delivered critical performance improvements and security enhancements while advancing technical assessments for major platform integrations.

#### Key Takeaways
- Improved performance for Positions module
- Fixed volume calculation error in Referral Program
- Enhanced performance for Token Data retrieval
- Implemented comprehensive security password logic for Wallet Manager
- Continued technical assessment for Jupiter aggregated tokens listing
- Continued technical assessment for HyperLiquid DEX integration

---

### Topic 2: Indexer Improvements

#### Executive Summary
Indexer team resolved unicode parsing issues and continued supporting technical assessments for upcoming integrations.

#### Key Takeaways
- Fixed unicode JSON parsing error on Solana blocks
- Continued technical assessment for Jupiter aggregated tokens listing
- Continued technical assessment for HyperLiquid DEX integration

---

### Topic 3: Frontend Updates

#### Executive Summary
Frontend team successfully implemented security features and resolved multiple user interface bugs affecting filter functionality and wallet management.

#### Key Takeaways
- Fixed bug where 'At least 1 social' filter wouldn't reset after unchecking
- Implemented Security Password creation modal for Wallet Manager
- Implemented Security Password check for exporting private keys
- Implemented Security Password check for creating transfers
- Added empty state display when no data available in filters
- Fixed issue with archiving more than maximum available wallets

---

### Topic 4: Third-Party Integration Strategy Discussion

#### Executive Summary
Critical discussion about the impact of third-party involvement on delivery timelines and the need for clear alignment on development responsibilities and communication channels.

#### Key Takeaways
- Third-party involvement in definition, design, or development impacts delivery dates
- RatherLabs estimates are based solely on internal team effort
- Time is of the essence for feature delivery
- Need for realignment on working agreements
- Agile communication channels required with external contractors

#### Discussion Details
The team raised concerns about delivery timeline impacts when third parties are involved in the development process. RatherLabs clarified that their time estimates assume they are the sole actors in end-to-end delivery. When external parties are involved, additional coordination time must be factored into project timelines.

---

### Topic 5: Desktop Development Approach

#### Executive Summary
Clear alignment established for desktop development with RatherLabs providing initial designs based on third-party style guides while maintaining product and UX responsibility.

#### Key Takeaways
- RatherLabs will provide initial designs using third-party designer's style guides
- Designs will follow product and UX definitions
- Visual language alignment is the objective, not functionality changes
- Agile communication channel needed with external contractor
- Public Slack channel recommended for transparency
- Time dilation from external interactions not included in contract estimates

---

### Topic 6: Mobile Development Approach

#### Executive Summary
Mobile development strategy defined with RatherLabs leading iOS app development and external agencies providing consultancy support.

#### Key Takeaways
- RatherLabs will define, design, and develop initial iOS app version
- External agencies (Evil Martians or replacement) act as consultants only
- External suggestions to be prioritized after initial development
- Clear separation of development and consultation responsibilities

---

### Topic 7: Platform Dependencies and Risk Assessment

#### Executive Summary
Important discussion about growing dependencies on third-party solutions and the associated risks, particularly regarding Jupiter's swap API and HyperLiquid's perpetual trading solution.

#### Key Takeaways
- Every third-party integration creates a dependency trade-off
- Jupiter's swap API is an industry standard (lower risk)
- HyperLiquid is cutting-edge with frequent updates (higher risk)
- Breaking changes could affect all integrated platforms simultaneously
- Risk includes potential downtime and vulnerabilities
- Team must be aware of risk/reward trade-offs

#### Discussion Details
The team highlighted that while Jupiter's swap API has become an industry standard and presents lower risk, HyperLiquid's DEX is a rapidly evolving platform that deploys features and updates regularly without advance warning. Any breaking changes, downtime, or vulnerabilities in HyperLiquid would affect all integrated platforms simultaneously, creating a shared risk scenario.

---

## Decisions Made

1. **Maintain RatherLabs ownership of development** - With external parties in consultancy roles only
2. **Establish public Slack channel** - For transparent communication with external contractors
3. **Accept third-party dependency risks** - With full awareness of trade-offs
4. **Separate mobile consultation from development** - External input after initial version complete

## Blockers and Risks Identified

- **Third-party coordination overhead** - Impact: High - Owner: Project Management - Needs resolution by: Ongoing
- **HyperLiquid integration risks** - Impact: High - Owner: Technical Team - Needs resolution by: Before integration
- **External contractor communication gaps** - Impact: Medium - Owner: Project Management - Needs resolution by: Immediate

## Parking Lot

- Long-term strategy for reducing third-party dependencies
- Backup plans for critical third-party service failures
- Documentation of all external dependencies

## Next Steps

- Set up public Slack channel for external coordination
- Complete technical assessments for Jupiter and HyperLiquid
- Document all third-party dependency risks
- Continue with planned development sprints

## References

- Third-party integration risk assessment document
- Jupiter API documentation
- HyperLiquid DEX technical specifications
- Mobile development roadmap