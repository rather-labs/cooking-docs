---
title: Cooking Weekly Sync - Feature Prioritization and Roadmap Planning
type: meeting-note
date: 2025-08-25
attendees: [Lucas Cufré, Gregory Chapman, Naji Osmat, Martin Aranda, Shakib, Zen]
meeting-type: planning
tags: [roadmap, feature-prioritization, AI-assistant, mobile-app, backend, web-app]
summary: |
  Weekly sync meeting focused on prioritizing features for the next development roadmap. The team discussed the implementation of key features including an AI Trading Journal, wallet tracking capabilities, watchlists, portfolio-wide take profit/stop loss functionality, and back office management tools. Major focus was placed on defining the scope and complexity of the AI assistant feature, which was identified as the highest priority but also the most complex undertaking. The team agreed on a phased approach to development with parallel workstreams for backend and frontend features.
related-docs:
  - Google Sheet prioritization document
  - Naji's AI Trading Journal specification document
---

# Cooking Weekly Sync - Feature Prioritization and Roadmap Planning

**Date:** 2025-08-25
**Time:** Duration approximately 58 minutes
**Attendees:** Lucas Cufré, Gregory Chapman, Naji Osmat, Martin Aranda, Shakib (joined late), Zen
**Facilitator:** Lucas Cufré

## Executive Summary

This weekly sync meeting focused on establishing priorities for the next development roadmap of the Cooking trading platform. Lucas Cufré presented a comprehensive breakdown of features from the prioritization document, with estimated effort levels for each. The discussion centered heavily on the AI Trading Journal feature, identified by Gregory and Naji as the highest priority differentiator from competitors like Axiom. The team acknowledged this feature's complexity, with Martin emphasizing it would require significant development effort and potentially custom model training.

The meeting resulted in a refined list of eight priority features for the upcoming roadmap: AI Trading Assistant, Wallet Tracker, Watch List, Portfolio TP/SL (at token level), Back Office management, Multi-language support, Advanced Filtering, and Account Management. The team agreed to parallelize development where possible, with backend and frontend work proceeding simultaneously. Mobile app development remains blocked due to Apple account issues, and a temporary production URL solution was proposed for accessing the web app.

Lucas committed to delivering a detailed timeline proposal by Friday, including a scoped approach to the AI assistant feature. The team emphasized the need for clear definition and phased implementation of complex features, particularly the AI components.

## Action Items

- [ ] **Create detailed timeline and roadmap proposal** - Assigned to: Lucas Cufré - Due: 2025-08-29 (Friday) - Priority: High
- [ ] **Consult AI expert for guidance on Trading Journal implementation** - Assigned to: Gregory Chapman - Due: ASAP - Priority: High
- [ ] **Update Figma designs and present to Leo for review** - Assigned to: Lucas Cufré - Due: 2025-08-26 - Priority: Medium
- [ ] **Define AI Assistant feature requirements and break into phases** - Assigned to: Naji Osmat - Due: TBD - Priority: High
- [ ] **Implement cooking.gg/login URL for production access** - Assigned to: Martin Aranda - Due: This week - Priority: Medium
- [ ] **Create Bitget account with referral code** - Assigned to: Lucas Cufré - Due: This week - Priority: Low
- [ ] **Send Fireflies recording to team** - Assigned to: Naji Osmat - Due: ASAP - Priority: Low
- [ ] **Define granular fee customization requirements for back office** - Assigned to: Martin Aranda - Due: Before referral system work - Priority: Medium

## Index

1. Feature Prioritization Overview
2. AI Trading Journal Discussion
3. Priority Feature Selection
4. Back Office Requirements
5. Mobile App Status and Blockers
6. Production Environment Access
7. Timeline and Next Steps

---

## Topics: Breakdown

### Topic 1: Feature Prioritization Overview

#### Executive Summary
Lucas presented a comprehensive Google Sheet documenting all features from the prioritization document shared by Naji and Andreas. Each feature was analyzed with perceived effort estimates ranging from 1-8 weeks. Notable exclusions from the current roadmap include copy trading, event calendar, SDK, yield offering, and multi-chain support.

#### Key Takeaways
- Advanced filtering capability estimated at 2 weeks effort
- Watch list feature (single list initially) estimated at 1 week, with multi-list support adding another week
- Saving filters requires 3 weeks due to backend integration needs
- Wallet tracker feature requires 4-6 weeks for full implementation
- Several features were explicitly excluded from current roadmap planning

#### Discussion Details
The team reviewed implementation complexity for various features. Advanced filtering would allow metadata consultation and filtering by keywords, boolean parameters, and DEX pair status. The watch list would initially support a single favorites list before expanding to multiple custom lists. Saving filters would require backend storage to maintain settings across sessions and devices.

---

### Topic 2: AI Trading Journal Discussion

#### Executive Summary
The AI Trading Journal emerged as the highest priority feature but also the most complex. Gregory emphasized this as a key differentiator from competitors. The team debated various implementation approaches, from simple P&L explanations to predictive modeling for trading recommendations. Concerns were raised about data requirements, model training costs, and the massive infrastructure undertaking required for comprehensive implementation.

#### Key Takeaways
- Identified as highest priority feature by leadership
- No ready-made solutions exist for Solana meme coin trading specifically
- Requires phased approach starting with simpler features
- Could require custom model training with significant costs
- Team suggested starting with P&L breakdown assistant (1-2 weeks) before advancing to predictive features
- Gregory to consult with AI expert for implementation guidance

#### Discussion Details
Martin suggested both external MCP integration and internal agent development. Lucas found existing solutions for TradFi and EVM environments but nothing specific to Solana meme coins' high volatility. The team discussed various complexity levels, from simple natural language processing to complex predictive models. Zen emphasized focusing on user-specific patterns rather than general market predictions. Cost considerations included expensive API usage for foundation models versus high training costs for custom models.

---

### Topic 3: Priority Feature Selection

#### Executive Summary
Naji outlined the five most critical features for the roadmap: AI Assistant, Wallet Tracker, Portfolio TP/SL, Back Office, and Multi-language support. The team refined portfolio TP/SL to operate at the token level rather than portfolio-wide, significantly reducing complexity from 6 weeks to approximately 2 weeks.

#### Key Takeaways
- Eight features selected for next roadmap cycle
- Portfolio TP/SL simplified to token-level implementation
- Back office and multi-language support needed by end of roadmap
- Most features can be parallelized between backend and frontend teams
- Watch list and wallet tracker identified as important for mobile as well

#### Discussion Details
The team decided against portfolio-wide TP/SL due to complexity of determining which positions to sell. Token-level implementation was deemed more practical and useful. Naji emphasized the importance of allowing users to set multiple partial TPs and SLs on holdings. The discussion clarified that features like watch list could integrate into mobile user profiles similar to CoinGecko's implementation.

---

### Topic 4: Back Office Requirements

#### Executive Summary
Back office functionality was discussed in detail, focusing on fee management, referral systems, and analytics integration. The team explored requirements for granular fee customization at various levels - platform-wide, per-token, and per-user. Martin confirmed technical feasibility but emphasized the need for clear specifications before implementation.

#### Key Takeaways
- Dynamic fee management at platform level already solved
- Custom referral codes and multi-level systems in development
- Analytics integration possible through Amplitude with dashboard views
- Granular fee customization feasible for promotions and specific tokens
- Customer support to be handled through third-party CRM integration
- Estimated 8 weeks for complete implementation

#### Discussion Details
The team discussed enabling promotions like "0% fees on specific tokens this weekend" and affiliate-specific discounts. Martin suggested pattern recognition for token addresses or contract lists. The back office would include fee management, referral tree creation, security password management, and analytics monitoring. Customer support ticketing was identified as requiring separate CRM integration rather than custom development.

---

### Topic 5: Mobile App Status and Blockers

#### Executive Summary
Lucas raised awareness about mobile app delays due to Apple account issues. The timeline remains uncertain given Apple's unpredictable approval process. Several features including higher/lower functionality, multiple wallet support, and UI updates per Leo's designs are pending for mobile implementation.

#### Key Takeaways
- Mobile development blocked by Apple account approval
- Cannot provide specific delivery date due to Apple uncertainty
- Multiple features pending including wallet management and limit orders
- UI updates needed based on Leo's latest designs
- May need to adjust multiple wallet feature for initial release

---

### Topic 6: Production Environment Access

#### Executive Summary
The team identified an issue where the production URL now shows only a landing page with no access to the application. A solution was proposed to create a cooking.gg/login URL for accessing the production environment, with whitelist management for authorized users.

#### Key Takeaways
- Production environment currently inaccessible via main URL
- Proposed solution: cooking.gg/login for app access
- Whitelist required for user access control
- Martin to implement this week

---

### Topic 7: Timeline and Next Steps

#### Executive Summary
Lucas committed to preparing a detailed timeline and roadmap proposal by Friday, including specific approaches to the AI assistant feature. The team agreed to reconvene after Gregory's consultation with his AI expert to refine the AI feature scope. Design updates and component library synchronization will proceed immediately.

#### Key Takeaways
- Timeline proposal due Friday
- AI assistant to be scoped into phases
- Design synchronization 80% complete
- Focus on September deliverables
- Parallel development tracks for backend and frontend features

---

## Decisions Made

1. **Simplify Portfolio TP/SL to token-level implementation** - Reduces complexity from 6 to 2 weeks while maintaining user value
2. **Prioritize AI Assistant despite complexity** - Acknowledged as key differentiator, will approach in phases
3. **Implement cooking.gg/login for production access** - Temporary solution for accessing production environment
4. **Parallelize development efforts** - Backend and frontend work to proceed simultaneously where possible
5. **Focus initial AI implementation on P&L analysis** - Start with simpler features before advancing to predictive capabilities

## Blockers and Risks Identified

- **Apple Developer Account Approval** - Impact: High - Owner: Lucas Cufré - Needs resolution by: ASAP
- **AI Assistant Complexity and Costs** - Impact: High - Owner: Team - Needs resolution by: Friday planning session
- **Lack of Solana-specific AI solutions** - Impact: Medium - Owner: Martin/Lucas - Needs resolution by: Ongoing research
- **Design synchronization incomplete** - Impact: Low - Owner: Lucas Cufré - Needs resolution by: This week

## Parking Lot

- Copy trading feature implementation
- Event calendar functionality
- SDK development
- Yield offering features
- Multi-chain support expansion
- Customer support integration details

## Next Steps

- Friday roadmap review with detailed timeline from Lucas
- Gregory to provide AI expert feedback
- Continue mobile development preparation despite Apple blocker
- Begin parallel development on prioritized features
- Next weekly sync scheduled for following Monday

## References

- Google Sheet prioritization document (shared with team)
- Naji's AI specification document
- Leo's updated design files
- Previous roadmap documentation from April