---
title: Cooking Demo - QA Issues, Performance & Infrastructure Scaling
date: 2025-09-12
type: demo
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Naji Osmat
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Marcos Tacca
  - Shakeib Shaida
status: completed
tags:
  - demo
  - qa
  - performance
  - infrastructure
  - scalability
  - load-balancer
  - clickhouse
related:
  - "[[2025-09-05-cooking-demo]]"
  - "[[2025-09-19-cooking-demo]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team demonstrated significant progress on backend and frontend development, including hotkey implementation, batch conversion for perpetuals, and UI updates aligned with Leo's designs. However, Zen raised serious concerns about QA quality after key partners (Fatality Capital) encountered bugs with charts and filters in the development environment. The discussion revealed critical infrastructure challenges: the load balancer cannot scale horizontally due to WebSocket sticky session issues, limiting the platform to a single backend instance until resolved. Performance improvements are targeted for completion before beta launch, with infrastructure costs being a key consideration for AWS scaling.

## Meeting Details

**Duration:** 27 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Backend Development Updates

**Navigation Hotkeys:**
- Many hotkeys implemented for navigation
- Not customizable by users in current version
- Designed for ease of use and testing

**Batch Conversion for Perpetuals:**
- Testing Solana to USDC batch conversion in progress
- Allows cost sharing among multiple users
- Core perpetuals functionality nearing completion

**Social Login:**
- Finishing minor bugs detected in QA
- Migration of security password flow to user settings
- Generally stable and functional

### 2. Frontend Development Updates

**UI Deployment:**
- Updated UI now deployed to development environment
- User settings deployed to dev
- Finishing minor testing and visual issues

**Token Details:**
- Updating to align with Leo's latest designs
- Consistent design language across platform

**Limit Orders & Perpetual Tables:**
- Active UI implementation in progress
- Missing some key parameters initially
- Now being fully implemented

### 3. Indexer & Performance Improvements

**Echo Access:**
- Zen provided access to Echo platform for research
- Team conducting deep dive into Echo's documentation
- Documentation described as "pretty obscure"
- Researching performance optimization techniques

**Performance Work:**
- Working on improvements discussed in previous goals
- Addressing bottlenecks identified earlier

**Chart Data Quality Issues:**
- Detected root cause of weird chart representations
- Issue: Low-volume bot transactions creating fictitious token values
- Bots trigger stop prices artificially
- Creates odd candles with extreme depths

**Industry Standard Solution:**
- Axium, GMGN, and Photon filter out these bot transactions
- Low volume, low order size transactions being filtered
- Working on fix to block them out
- Expected completion: End of day

### 4. Mobile Development Progress

**Implemented Features:**
- Charts
- Token history
- Position list
- Portfolio view

**Still Pending:**
- Twitter/X account link for social community
- Discord account link for social community
- Links needed for UI, landing page, and mobile app

### 5. Updated UI Demonstration

**Visual Updates:**
- Iconography implementation per Leo's standards
- Top 10 and Snipers icons changed during the week
- Leo making updates; icons to be refreshed today or Monday
- Settings redesigned with updated filters
- User settings page implemented with new design

**User Settings Features:**
- Connect to new login venues
- Link additional accounts to primary Cooking account
- Shortcuts display (Command F/Control F for search, Command K for kitchen)
- Security section for password creation/update

**Social Links Section:**
- Feedback form integration planned
- Product documentation links
- Social media links (once accounts provided)

### 6. Critical QA Discussion

**Zen's Concerns (via Gregory):**
- Key partner Fatality Capital experiencing issues
- Problems with charts and filters not caught by QA
- First impressions compromised with major partners
- Question: Why weren't these issues detected before partner demo?

**Lucas's Response:**
- Shared environment is development, not production
- Development environment expected to have bugs
- Some issues (like historical token charts) not fully tested
- Testing occurring in phases
- Historical tokens show more problems than new tokens

**Martin's Clarification:**
- Charts for new tokens work better than old tokens
- Historical tokens (like Pengu) have more issues
- Issue related to Jupiter data indexing
- Different behavior between newly minted vs. existing tokens

**Environment Context:**
- No staging environment for code freeze testing
- Production environment is de facto "last stable version"
- Development environment constantly receiving updates
- Product size makes maintaining multiple environments challenging

**Partner Impact:**
- Showing development link to partners creates poor first impression
- Fatality Capital is "massive name" partnership
- Need to ensure demos show platform at best quality
- Should only share production links with partners

### 7. Load Balancer & Scalability Challenges

**Current Limitation:**
- Load balancer not functioning effectively for backend
- Only one backend instance running
- Cannot run multiple instances due to technical constraint

**Root Cause:**
- WebSocket sticky connections issue
- Load balancer switching between instances constantly
- Causes connection problems with persistent WebSocket connections
- Limits horizontal scaling capability

**Impact:**
- Single instance may have insufficient resources
- Performance degradation under load
- Cannot scale horizontally at present

**Resolution Plan:**
- Issue mapped and being fixed in next two weeks (before beta)
- Increased resources for single instance as temporary measure
- Testing configuration tweaks for better performance without horizontal scaling
- Horizontal scaling planned but not for immediate implementation

**Architectural Changes:**
- Several changes made to architecture in recent months
- Designed to handle load efficiently
- Should work same with 1 user or 2,000 users
- Need stress testing beyond 2,000 users for validation

### 8. User Capacity & Beta Planning

**Historical Context:**
- Previous closed betas: maximum 500 users
- Headless testing conducted for ~2,000 users
- Current known capacity: 2,000 users

**Beta User Expectations:**
- Gregory/Zen: Expect internal KOLs and partners primarily
- Don't anticipate massive user influx during beta
- Should aim for most optimal performance possible

**Unknown Territory:**
- If expecting 1,000 but receiving 3,000 users
- Scaling beyond tested limits is uncharted

**Scaling Considerations:**
- Auto-scaling will increase AWS infrastructure costs
- Currently keeping infrastructure lean for development
- Horizontal auto-scaling will significantly increase monthly AWS bill
- Cost implications need to be considered for financial planning

### 9. AWS Funding & Cost Management

**Current Status:**
- AWS account up to date
- New card being added to AWS account
- Zen pre-funding the card for AWS costs

**Monthly Monitoring:**
- Will ensure sufficient balance each month
- Need to monitor costs as scaling occurs
- Auto-scaling will increase costs significantly

### 10. Dubai Travel Plans

**Dates:** November 5-13, 2025

**Attendees:**
- Lucas Cufré (confirmed)
- Martin Aranda (confirmed)
- Gregory Chapman (likely same timeframe)

**Plans:**
- Lucas and Martin will cowork during that week
- Potential meetup with Gregory
- Opportunity for in-person collaboration

### 11. Next Steps & Video Demo Plans

**Chart & Filter Fixes:**
- Lucas to notify Gregory when resolved
- Target: Complete by end of day or Monday
- Required for video recording

**Social Accounts:**
- Naji to follow up on Twitter/X and Discord community accounts
- Needed for UI completion

**Testing & Video:**
- Naji and Gregory planning to test product
- Video recording planned for that afternoon
- Lucas requested advance notice before recording
- Team will pause deployments to dev during video recording

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Prioritize fixing chart and filter issues | Required for partner demos and video | End of day completion target |
| Block deployments during video recording | Prevent breaking changes during demo | Coordination required with Lucas |
| Focus on completing work before beta | Limited timeframe for infrastructure fixes | Two-week sprint to beta |
| No production environment until end of month | Focus resources on completing development | Development environment only until deadline |
| Increase single instance resources temporarily | Cannot scale horizontally yet | Improved performance without horizontal scaling |
| Only share production links with partners | Development environment too unstable | Better first impressions |
| Pre-fund AWS card | Ensure sufficient infrastructure budget | Zen handling pre-funding |
| Plan Dubai coworking week | Collaboration opportunity | November 5-13, 2025 |

## Action Items

### High Priority

- [ ] **Lucas/Team** - Fix chart display issues by end of day (Due: September 12, 2025, URGENT)
- [ ] **Lucas/Team** - Fix filter issues for token details (Due: September 14, 2025)
- [ ] **Lucas** - Notify Gregory when chart and filter issues resolved (Due: September 12-14, 2025)
- [ ] **Martin/DevOps** - Complete load balancer WebSocket fix before beta (Due: September 26, 2025)
- [ ] **Naji/Gregory** - Test product and record demo video (Due: September 12, 2025)

### Medium Priority

- [ ] **Naji** - Follow up on Twitter/X community account creation (Due: September 19, 2025)
- [ ] **Naji** - Follow up on Discord community account creation (Due: September 19, 2025)
- [ ] **Naji** - Notify Lucas before starting video recording (Due: September 12, 2025)
- [ ] **Gregory** - Update Vercel members list for cost reduction (Due: September 19, 2025)

### Low Priority

- [ ] **Team** - Plan logistics for Dubai coworking (Due: November 1, 2025)
- [ ] **Gregory** - Monitor AWS costs as scaling increases (Due: Ongoing)

## Technical Notes

### Bot Transaction Filtering
- Low-volume, low-order-size bot transactions creating price anomalies
- Industry standard: Filter these transactions (Axium, GMGN, Photon approach)
- Implementation: Backend engineer working on filter
- Expected completion: End of day September 12

### Load Balancer Architecture Challenge
- **Problem:** WebSocket sticky connections incompatible with current load balancer setup
- **Impact:** Limited to single backend instance
- **Temporary Solution:** Increased resources on single instance
- **Permanent Solution:** Fix WebSocket handling before beta (2-week timeline)
- **Future State:** Horizontal auto-scaling enabled

### Echo Research
- Team researching Echo's performance optimization techniques
- Documentation noted as "obscure"
- Goal: Learn from fastest competitor in space

### Environment Strategy
- **Development:** Active development, expect bugs
- **Production:** Stable releases only, not available until end of month
- **Staging:** Not currently available due to product size
- **Partner Demos:** Should only use production environment

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Load balancer cannot scale horizontally | Performance degraded with high user load | Fix planned before beta (2 weeks) |
| Single backend instance limitation | Cannot handle unexpected traffic spikes | Increased instance resources temporarily |
| QA not catching issues before partner demos | Poor first impressions with key partners | Focus on thorough testing before sharing |
| No staging environment | Cannot test stable releases before production | Plan to implement proper release flow |
| Chart data quality issues | User experience degradation | Filter implementation by end of day |
| Unknown user capacity beyond 2,000 | Potential system failure with traffic spike | Stress testing planned; auto-scaling ready |
| AWS cost escalation | Budget overruns with auto-scaling | Pre-funding and monitoring in place |
| Social account links still missing | Mobile UI cannot be completed | Naji following up |

## Next Steps

1. **Today:** Fix chart and filter issues (Lucas/Team)
2. **Today:** Record demo video with Naji and Gregory
3. **This Week:** Complete load balancer WebSocket fix (Martin/DevOps)
4. **This Week:** Implement proper staging/production workflow
5. **Before Beta:** Ensure horizontal scaling capability functional
6. **Before Beta:** Complete stress testing beyond 2,000 users
7. **Ongoing:** Continue performance optimization work

## Key Metrics & Numbers

- **Previous closed beta max users:** 500
- **Current stress test capacity:** 2,000 users
- **Backend instances currently running:** 1 (cannot scale to multiple)
- **Target completion for load balancer fix:** 2 weeks (before beta)
- **Chart fix completion:** End of day September 12
- **Filter fix completion:** Monday September 14
- **Dubai travel dates:** November 5-13, 2025

## References

- Echo platform (performance benchmark)
- Axium, GMGN, Photon (bot filtering approach)
- Leo's Design Language Updates
- Fatality Capital (key partner experiencing issues)

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
