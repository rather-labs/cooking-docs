---
title: Cooking Weekly Sync - September 8, 2025
type: meeting-note
date: 2025-09-08
attendees: [Lucas Cufré, Greg Chapman, Zen, Martin Aranda, Naji Osmat, Shakiv]
meeting-type: technical
tags: [security, beta-release, turnkey, geo-blocking, mobile-app, account-management, bubble-maps, seo, monitoring]
summary: |
  Weekly sync focused on security considerations for the upcoming beta release, particularly regarding Turnkey integration and wallet management. The team decided against performing a security audit for the closed beta, agreed to remove geo-blocking restrictions, and discussed implementation of bubble maps, monitoring tools, and mobile app features for account management.
related-docs:
  - Bubble maps provider comparison document (to be shared)
  - Product metrics proposal document (to be shared)
---

# Cooking Weekly Sync - September 8, 2025

**Date:** 2025-09-08
**Time:** ~45 minutes
**Attendees:** Lucas Cufré, Greg Chapman, Zen, Martin Aranda, Naji Osmat, Shakiv
**Facilitator:** Lucas Cufré

## Executive Summary

The team conducted their weekly sync meeting focusing primarily on security preparations for the upcoming beta release. A significant portion of the discussion centered on the Turnkey integration and its implications for wallet security, with the team ultimately deciding that a security audit would not be necessary for the closed beta phase, though it should be reconsidered for the production go-to-market launch.

Key decisions included removing geo-blocking restrictions that currently prevent access to certain trading platforms like Hyperliquid, aligning with competitor practices. The team also discussed implementing bubble maps visualization, with a recommendation to go with bubblemaps.io as the provider. Technical infrastructure improvements were addressed, including the need for a dedicated Sentry monitoring plan for the beta release and SEO/accessibility considerations for future phases.

The mobile app's account management capabilities were extensively discussed, particularly around supporting multiple wallets. The team agreed that while the mobile app would initially support single wallet functionality for simplicity, users who have created multiple wallets on desktop should be able to access them on mobile in a future release. Several administrative items were addressed including Apple Developer account migration and the need to update various service subscriptions to the company email.

## Action Items

- [ ] **Send bubble maps provider comparison document** - Assigned to: Lucas - Due: 2025-09-09 - Priority: High
- [ ] **Send product metrics proposal for beta** - Assigned to: Lucas - Due: 2025-09-09 - Priority: High
- [ ] **Provide meta titles and descriptions for SEO** - Assigned to: Greg - Due: TBD - Priority: Medium
- [ ] **Send list of pages needing SEO work** - Assigned to: Lucas - Due: TBD - Priority: Medium
- [ ] **Implement API key rotation for Turnkey security** - Assigned to: Martin - Due: Before beta - Priority: High
- [ ] **Remove geo-blocking restrictions** - Assigned to: Development team - Due: Before beta - Priority: High
- [ ] **Seek legal counsel on geo-blocking implications** - Assigned to: Zen/Greg - Due: ASAP - Priority: High
- [ ] **Create cooking email Sentry account** - Assigned to: Naji - Due: This week - Priority: High
- [ ] **Migrate subscriptions to cooking email** - Assigned to: Greg/Naji - Due: This week - Priority: Medium
- [ ] **Verify Apple Developer account transfer** - Assigned to: Greg - Due: 2-3 days - Priority: High
- [ ] **Test platform and identify broken features** - Assigned to: Greg/Naji - Due: This week - Priority: High
- [ ] **Create demo video for partners** - Assigned to: Greg/Naji - Due: This week - Priority: Medium
- [ ] **Complete DevOps audit of platform** - Assigned to: DevOps engineer - Due: Next 2 weeks - Priority: High
- [ ] **Write order types mechanics document for Leo** - Assigned to: Lucas - Due: TBD - Priority: Low
- [ ] **Design mobile account management flows** - Assigned to: Lucas/Leo - Due: Next release - Priority: Low

## Index

1. Security Considerations for Beta Release
2. Geo-blocking Policy Change
3. Bubble Maps Integration
4. Monitoring and Infrastructure
5. SEO and Accessibility Planning
6. Mobile App Account Management
7. Administrative Updates

---

## Topics: Breakdown

### Topic 1: Security Considerations for Beta Release

#### Executive Summary
The team discussed security measures for the upcoming beta release, focusing on Turnkey's role in wallet management and whether a security audit is necessary. The consensus was to defer the security audit until the production launch while implementing API key rotation and encryption hardening measures.

#### Key Takeaways
- Turnkey integration is semi-custodial - they maintain signing rights for wallets even after users export private keys
- If Turnkey were compromised, all platforms using them (Cooking, Axiom, Bullex, Photo) would be affected equally
- Security audit not necessary for closed beta but should be considered for production launch
- API key rotation will be implemented to limit exposure if keys are compromised
- Decision against implementing a fallback provider (Leap) due to increased security surface area

#### Discussion Details
The team explored the possibility of using Leap as a fallback provider if Turnkey experiences downtime. However, this approach was rejected as it would duplicate costs and increase security risks by cloning private keys across providers. The team acknowledged that while they cannot control Turnkey's security, they can harden their own infrastructure through better encryption practices and regular API key rotation.

---

### Topic 2: Geo-blocking Policy Change

#### Executive Summary
Following competitor analysis showing platforms like Axiom allow US users to access Hyperliquid without VPN, the team decided to remove geo-blocking restrictions while maintaining the ability to re-enable them if legal issues arise.

#### Key Takeaways
- Competitors (Axiom) are not geo-blocking US users from accessing Hyperliquid
- Decision to remove geo-blocking to maintain competitive parity
- Geo-blocking capability will remain in the system but be disabled by default
- Legal counsel should be sought to understand implications
- Back-office toggle for geo-blocking may be implemented for quick response if needed

---

### Topic 3: Bubble Maps Integration

#### Executive Summary
Lucas presented research on three bubble map providers for visualizing token holdings and transactions, recommending bubblemaps.io based on price and integration ease.

#### Key Takeaways
- Three providers evaluated: Inside X, bubblemaps.io, and Faster 100x
- Bubblemaps.io recommended for best price and integration documentation
- Will improve tables by adding badges to transaction types
- Comparison document with pricing to be shared with team for final approval

---

### Topic 4: Monitoring and Infrastructure

#### Executive Summary
The team identified critical infrastructure needs for the beta release, including dedicated monitoring through Sentry and performance improvements based on DevOps audits.

#### Key Takeaways
- Current Sentry plan is consumed by TARS project, leaving Cooking without proper monitoring
- Dedicated Sentry plan needed for beta to track user issues and errors
- DevOps engineer conducting end-to-end audit to identify performance bottlenecks
- Performance improvements expected over next two weeks

---

### Topic 5: SEO and Accessibility Planning

#### Executive Summary
SEO and accessibility features will not be included in the beta but are planned for the go-to-market phase, with Greg taking responsibility for meta descriptions and titles.

#### Key Takeaways
- SEO implementation deferred to go-to-market phase
- Greg will provide meta titles and descriptions for all pages
- Basic accessibility features (tab navigation, color contrast) could be implemented easily
- Advanced accessibility (screen readers) would require more significant effort
- Decision on accessibility features to be based on user demographics discovered during beta

---

### Topic 6: Mobile App Account Management

#### Executive Summary
Extended discussion on how to handle multiple wallet support in the mobile app, balancing simplicity for new users with functionality for power users who manage multiple wallets on desktop.

#### Key Takeaways
- Mobile app will initially support single wallet only for simplicity
- Users cannot create additional wallets on mobile (desktop only)
- Future release will allow viewing/switching between wallets created on desktop
- Account management page design for mobile deferred to next release
- Target audience is newcomers to Solana, but app should also serve as companion for desktop users

#### Discussion Details
The team debated whether to expose wallet creation functionality on mobile. Lucas argued for keeping it simple for newcomers ("my grandmother wants to start trading Solana"), while Greg and Naji emphasized the need to support existing desktop users who expect to access their multiple wallets on mobile. The compromise was to allow wallet switching on mobile for those who have multiple wallets, but not allow creation of new wallets on mobile.

---

### Topic 7: Administrative Updates

#### Executive Summary
Several administrative items were addressed including Apple Developer account migration, service subscription management, and creation of partner demo videos.

#### Key Takeaways
- Apple Developer account transfer pending KYC verification (2-3 days)
- All service subscriptions should migrate to cooking email for centralized management
- Partner video creation needed due to issues with external team's attempt
- AI Journal project will have separate Tuesday calls for progress monitoring
- Team members potentially traveling to Dubai in November for Ryder Labs meeting

---

## Decisions Made

1. **No security audit for beta release** - Team will rely on Turnkey's security and implement API key rotation - Consider audit for production launch
2. **Remove geo-blocking restrictions** - Align with competitor practices while maintaining ability to re-enable if needed
3. **Select bubblemaps.io as provider** - Best price and documentation for beta needs
4. **Defer mobile wallet creation** - Keep mobile app simple for newcomers, add multi-wallet support in next release
5. **Create dedicated Sentry account** - Essential for beta monitoring and debugging

## Blockers and Risks Identified

- **Turnkey dependency** - Impact: High - Owner: Team - If Turnkey is compromised, all user wallets are at risk with no mitigation available
- **Legal implications of removing geo-blocking** - Impact: Medium - Owner: Zen/Greg - Needs resolution by: Before beta launch
- **Apple Developer account migration** - Impact: High - Owner: Greg - Blocking app deployment

## Parking Lot

- Accessibility features implementation timeline
- Detailed mobile account management design
- Perpetuals support on mobile

## Next Steps

- Next meeting scheduled for: Following week (date TBD)
- Complete all high-priority action items before beta launch
- Legal counsel consultation on geo-blocking
- Begin implementation of bubble maps and monitoring infrastructure

## References

- Bubble maps provider comparison (to be shared by Lucas)
- Product metrics proposal (to be shared by Lucas)
- Partner video requirements (from external team's failed attempt)