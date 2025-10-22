---
title: Cooking Sync - Mobile App Development Planning
type: meeting-note
date: 2025-07-07
attendees: [Lucas Cufré, Naji Osmat, Gregory Chapman, Zane]
meeting-type: planning
tags: [Cooking, Product, Mobile, iOS, App Store, SDK, Design, Evil Martians]
summary: |
  Planning session focused on critical mobile app development decisions including App Store account type selection, native vs hybrid app architecture, and design system alignment. The team decided to pursue a business account for the App Store and agreed on a hybrid approach combining native performance with customized UI components. Key discussions covered liquidity calculation challenges, Evil Martians onboarding, and timeline constraints for Q3 delivery.
related-docs:
  - Mobile App Development Scope Document (pending)
  - App Store Account Requirements Document (pending)
---

# Cooking Sync - Mobile App Development Planning

**Date:** 2025-07-07
**Time:** ~11:57 AM (Duration: approximately 30 minutes)
**Attendees:** Lucas Cufré, Naji Osmat, Gregory Chapman, Zane (joined later)
**Facilitator:** Lucas Cufré (leading technical discussion)

## Executive Summary

The team convened to address critical decisions for the Cooking mobile app development, with a primary focus on two blockers: App Store account type selection and the architectural approach for the iOS application. The meeting established that a business account would be pursued for App Store deployment despite additional documentation requirements, as it provides better credibility and compliance for financial applications.

A significant portion of the discussion centered on balancing native iOS performance with custom design requirements. The team agreed on a hybrid approach that leverages native performance capabilities while allowing for UI customization based on Leo's design system, with Evil Martians providing initial designs and Leo reviewing for final touches. This decision impacts the development timeline but was deemed necessary to avoid doubling work later.

The team also addressed ongoing technical challenges with liquidity calculation for tokens, particularly the lack of industry standards for tracking metrics across different protocols. A solution involving protocol-specific indexing was proposed, with research ongoing to determine the best implementation approach. The meeting concluded with alignment on next steps, including documentation preparation for the App Store account and coordination with Evil Martians for design delivery by the following Monday.

## Action Items

- [ ] **Prepare and send App Store business account requirements documentation** - Assigned to: Lucas Cufré - Due: 2025-07-07 (same day) - Priority: High
- [ ] **Prepare legal documentation for business account setup** - Assigned to: Zane - Due: As needed - Priority: High
- [ ] **Deliver initial mobile app designs** - Assigned to: Evil Martians - Due: 2025-07-14 (next Monday) - Priority: High
- [ ] **Research liquidity indexing implementation for protocols** - Assigned to: Development team - Due: Ongoing - Priority: Medium
- [ ] **Create scope document with wireframes and UX flows for sign-off** - Assigned to: Lucas Cufré - Due: Before development proceeds - Priority: High
- [ ] **Follow up meeting with Martin regarding SDK and go-to-market strategy** - Assigned to: Team - Due: 2025-07-12 (Friday) - Priority: Medium

## Index

1. App Store Account Type Selection
2. Native vs Hybrid App Architecture
3. Design System and UI Customization
4. Liquidity Calculation Challenges
5. SDK and API Strategy (deferred)

---

## Topics: Breakdown

### Topic 1: App Store Account Type Selection

#### Executive Summary
The team evaluated business versus personal App Store accounts and concluded that a business account is necessary despite additional setup complexity. This decision ensures proper credibility, regulatory compliance, and team access management for a financial trading application.

#### Key Takeaways
- Business account costs same as personal ($99/year) but requires more documentation
- Business account provides better credibility with "Cooking" or "Ember" as publisher vs individual name
- Better suited for financial applications and regulatory compliance
- Allows multiple team members with different roles to access the account
- Legal team needs to prepare business registration documents and tax IDs
- Decision made to proceed with business account despite longer setup time

#### Discussion Details
Lucas presented a comprehensive comparison of both account types. The personal account would offer faster setup with minimal documentation but would display an individual's name as the publisher and face harder approval for financial services. The business account requires business registration documentation, tax IDs, and verification processes but provides essential benefits for scaling, team collaboration, and credibility. Gregory immediately recognized the necessity of the business route for a financial application, and Zane confirmed legal would prepare necessary documentation.

---

### Topic 2: Native vs Hybrid App Architecture

#### Executive Summary
The team aligned on developing a hybrid application that prioritizes native performance while allowing UI customization. This approach balances the Q3 deadline constraints with the need for brand-consistent design elements and avoids future rework.

#### Key Takeaways
- Native performance is the priority, not necessarily native UI components
- Hybrid approach allows customization while maintaining fluid performance
- Design will differ from desktop version due to iOS constraints
- Custom components like Robinhood's slider would add significant development time
- iOS 18 will bring major design language changes (liquid glass aesthetic)
- Team agreed to find middle ground between out-of-box and fully custom solutions

#### Discussion Details
Lucas clarified the distinction between native performance and native UI, explaining that fully native apps use Apple's default design system components with limited customization options. The discussion revealed tension between meeting the Q3 deadline and implementing Leo's custom designs. Zane emphasized the importance of avoiding double work by not building a simple version first only to rebuild it later with customizations. The compromise reached was to focus on native performance capabilities while allowing for UI customization as needed.

---

### Topic 3: Design System and UI Customization

#### Executive Summary
The team established a design workflow involving Evil Martians for initial designs, followed by Leo's review and refinements. This multi-stage process adds complexity but ensures design consistency with the Cooking brand while managing timeline constraints.

#### Key Takeaways
- Evil Martians to deliver initial designs by next Monday (July 14)
- Leo will review and make minor touches rather than structural changes
- Development can proceed with Evil Martians' designs to avoid delays
- Multiple stakeholder involvement extends timeline but deemed necessary
- Scope document with wireframes needed for formal sign-off
- iOS 18's new liquid glass design language will impact component choices

#### Discussion Details
The discussion revealed concerns about timeline impact with multiple design stakeholders. Lucas emphasized that each additional reviewer extends the deadline and increases iterations needed. Naji suggested that Leo's changes would likely be minor touches rather than structural modifications, allowing development to proceed with Evil Martians' designs while Leo reviews in parallel. The team acknowledged the risk but agreed it was necessary to ensure design quality and brand consistency.

---

### Topic 4: Liquidity Calculation Challenges

#### Executive Summary
The team discussed technical challenges in calculating accurate liquidity metrics for tokens across different protocols, with no industry standard currently available. A solution involving protocol-specific indexing was proposed to aggregate TVL (Total Value Locked) data.

#### Key Takeaways
- No industry standard exists for calculating token metrics across protocols
- Tokens restart metrics when graduating from bonding curves to DEXs
- Holistic lifecycle tracking needed for accurate market data
- Jupiter's liquidity updates are slower than other data updates
- Solution involves indexing supported protocols (primarily Raydium)
- Approximation approach accepted given technical constraints

#### Discussion Details
Lucas explained the fundamental issue: when tokens graduate from platforms like Pump.fun to Pump Swap, metrics reset to zero rather than maintaining historical data. This creates misleading information for potential investors who cannot see the full price discovery history. The proposed solution involves creating a separate indexer feature to track liquidity values across all supported protocols. The team acknowledged that while not perfect, aggregating liquidity from major exchanges like Raydium would provide a "good enough" approximation, similar to what competitors like Axiom are doing.

---

## Decisions Made

1. **Pursue business account for App Store** - Provides necessary credibility and compliance for financial app
2. **Adopt hybrid app architecture** - Native performance with customized UI components
3. **Implement multi-stage design process** - Evil Martians first, then Leo review
4. **Proceed with liquidity approximation approach** - Index supported protocols for TVL aggregation

## Blockers and Risks Identified

- **Design iteration timeline risk** - Impact: High - Owner: Lucas/Naji - Multiple stakeholders could extend deadline beyond Q3
- **App Store approval uncertainty** - Impact: Medium - Owner: Zane - Business account documentation and financial app requirements
- **Liquidity calculation accuracy** - Impact: Medium - Owner: Development team - No perfect solution without industry standard

## Parking Lot

- SDK and go-to-market strategy discussion (deferred to Friday meeting with Martin)
- Specific API endpoint exposure for third-party integrations

## Next Steps

- Lucas to send App Store account requirements documentation today
- Monitor Evil Martians Slack channel for design progress
- Friday follow-up meeting to discuss SDK strategy with Martin
- Continue research on liquidity indexing implementation
- Prepare scope document with wireframes for stakeholder sign-off

## References

- Evil Martians Slack channel (team collaboration)
- WWDC updates on iOS 18 design language changes
- Robinhood app (reference for custom slider component)