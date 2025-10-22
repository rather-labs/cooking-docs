---
title: Cooking Demo - Final Sprint to Beta, Budget Constraints & Dubai Planning
date: 2025-09-26
type: demo
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Naji Osmat
  - Gregory Chapman (greg@ember.app)
  - Zen (z@ember.app)
  - Marcos Tacca
  - Shakeib Shaida (shak@ember.app)
status: completed
tags:
  - demo
  - beta-ready
  - budget
  - perpetuals
  - on-ramp
  - gitbook
  - dubai-planning
related:
  - "[[2025-09-19-cooking-demo]]"
  - "[[2025-10-03-cooking-demo]]"
original-language: Spanish
translated: true
translation-date: 2025-10-20
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team presented the near-final state of the platform before beta launch, with perpetuals testing in final stages and dramatic performance improvements demonstrated. Loading times for token details and charts improved from 30 seconds to 1-1.5 seconds. Most features are complete or in final testing, including social login, cooking tag, custom referral code, limit orders, and market cap implementation. The team is beginning On-Ramp integration on Monday as the final development piece. A successful video demo was planned for afternoon recording. Post-meeting discussions focused on budget constraints, with Zen proposing reduction to $25-30K while protecting key resources (Daniel and Ali), and planning for November Dubai coworking trip (November 5-15).

## Meeting Details

**Duration:** 31 minutes
**Platform:** Google Meet
**Recording:** Available

## Topics Discussed

### 1. Backend Development - Testing Phase

**Active Testing:**
- Perpetual side slow withdraw
- Perpetual side slow deposit
- Limit orders (primarily UI side)
- Support for externally created Solana wallets

**Completed & Fixed:**
- Internal errors when executing orders on certain providers (Pump, Raydium, Jupiter)
- Issue was intermittent, now fully resolved
- Pushed to testing environment

**Performance Breakthrough:**
- Significant improvement in loading times
- Significant improvement in chart population
- "If you've been testing in the dev environment, you'll notice the difference"

### 2. Social Login & User Features - Complete

**Finished Implementations:**
- Social login (fully tested and implemented)
- Cooking tag
- Custom referral code
- All three features production-ready

**Impact:**
- Referral program in finishing stages
- User onboarding significantly enhanced
- Multiple authentication methods supported

### 3. Frontend Development Updates

**Active Testing:**
- Limit orders UI for perpetuals
- Market cap implementation on charts
- Extended timeframes
- USD valuation on charts
- Advanced order UI alignment

**UI Fixes:**
- Resolving scroll issues on certain breakpoints
- Testing across different screen sizes

**Pending Deployment:**
- Advanced order UI alignment (being pushed to dev shortly)
- Import support for externally created Solana wallets

**Completed:**
- Fast deposit for perpetuals
- Fast withdraw for perpetuals
- Market close functionality
- Multiple UI bugs (too many to list individually)
- User settings model

### 4. Indexer Work - Critical Fixes

**Active Testing:**
- Bonding curve marking for newly minted tokens
  - Issue: Incorrectly marked as completed on Pump and Moonshot
  - Testing multiple implementations to find best solution
- Launchpad token tracking issue in portfolio (duplicate tracking problem)
- Tracking of token supply for bars
  - Critical for market cap calculations
  - Feeds into chart generation
- Price outlier filters for charts
- Pump fund trade filter (was being tracked incorrectly)

**Completed Fixes:**
- Holding amount duplication issue resolved
  - Example: $2 worth of Pengu showing as $4
  - Was double-accounting trades from indexer
  - Now shows correct amounts
- SOL balance for top traders

### 5. Mobile Development Status

**Finishing Today:**
- Trading operations
- Token history
- Pending orders

**Starting Monday:**
- On-Ramp solution implementation
- This is the final major development piece
- On-Ramper integration as agreed

### 6. Live Product Demonstration

**Performance Showcase:**

Lucas demonstrated significantly improved loading times:
- Token details page loading
- Chart rendering
- Smooth, fast interactions

**New Timeframes Available:**
- Multiple additional timeframe options
- More granular analysis capabilities

**Market Cap Display:**
- Can switch between Price and Market Cap on charts
- Display options: Solana valuation or USD valuation
- Example shown: $2.1 billion market cap
- Y-axis now supports market cap (major achievement)

**Naji's Feedback:**
- Market cap should be default view
- Price as secondary option
- Lucas agreed to make market cap default

**Technical Achievement:**
- Market cap tracking was significant challenge (Martin: "really fun challenge")
- Now implemented and functional

**Limit Orders UI:**
- Being tested for perpetuals
- Integration with open orders system
- Open orders display critical for functionality

**Advanced Orders:**
- UI implementation being tested today
- Will be renamed from "Custom Orders" to "Advanced Orders"

**Referral Program:**
- Called "Referral" currently
- First attempt at UI alignment
- Backend actively being worked on
- Needs additional refinement

**Portfolio & Wallet Manager:**
- Final pages to be completed
- Last major UI pieces

### 7. User Settings & Features

**Cooking Tag:**
- Display name customization for users
- Future use: Recipe for Riches program
- Future use: Referral program social sharing
- Images for social media with Cooking branding
- Currently for display only

**Shortcuts:**
- Already implemented and functional
- Quick navigation throughout platform

**Security:**
- Password management functional
- Security settings accessible

### 8. Performance Metrics Discussion

**Naji's Question:** General loading times status?

**Lucas's Answer:**
- **Before:** ~30 seconds
- **After:** 1-1.5 seconds average
- Varies slightly depending on specific situations

**Martin's Perspective:**
- "Night and day" difference
- Required lot of work
- Two engineers completely focused on optimization
- Multiple fronts addressed simultaneously

### 9. Video Demo Planning

**Naji's Announcement:**
- He and Gregory testing product this afternoon
- Filming video demo this afternoon
- Will send bug report if anything found

**Lucas's Request:**
- Notify before starting video recording
- Team will pause dev deployments during filming
- Prevents breaking changes during recording
- Ensures smooth demo experience

**Naji Agreed:**
- Will message before starting
- Coordination to protect video recording

### 10. Documentation & Support Tools

**GitBook Implementation:**

**Naji's Update:**
- Sent GitBook account access to Lucas

**Lucas's Plan:**
- Access and pay for Pro plan (annual) this afternoon
- Include cost in next invoice
- Update all documentation today or Monday latest
- Share with team for review
- Update URL to "cooking-docs" instead of "gitbook.cooking"

**CRM for Customer Support:**

**Lucas's Question:**
- Feedback form and support links needed
- No CRM or survey service currently implemented
- Can redirect to survey service
- Or implement CS team's existing CRM

**Naji's Request:**
- Lucas to research and suggest CRM solution
- Provide recommendations

**Lucas Agreed:** Will research and suggest solution

### 11. Remaining Work Summary

**Lucas's Assessment:**
- Nothing else outstanding from his side
- Team on track for deadline
- Focus on completing final pieces

**Meeting Conclusion:**
- Next sync: Monday
- Video recording: This afternoon
- Development continues through weekend if needed

### 12. Post-Demo Discussion: Perpetuals & PPS Wireframes

**Participants:** Gregory, Zen, Naji (after Lucas and team left)

**Gregory's Update:**
- Video recording planned for afternoon
- PPS wireframes 70% complete
- Should finish tonight or over weekend
- Assumes Epic branding for On-Ramp

**Zen's Guidance for Designer:**
- Give designer website Figma that Ali used
- Reuse Epic Figma elements (loads of cool components)
- Avoid starting from basic elements
- Suggestion: Remove fireflies from design

**Wireframe Timeline:**
- If finished over weekend → early next week completion
- Allow 1-2 days for fixes (designer makes small mistakes frequently)
- Typically needs iteration for accuracy

### 13. Perpetuals Chain Discussion

**Zen's Question:**
- XRP-based perpetuals must use XRP EVM side chain
- Concern: Not many assets on that chain
- Need good workaround for demo

**Gregory's Typical Approach:**
- Say it's multi-chain
- Also includes XRP chain

**Zen's Alternative:**
- Say assets are on XRP chain but abstracted
- Supports liquidity on other chains
- Can settle on XRP
- Will figure out workaround

**Timeline:**
- Told perpetuals client next week
- Client eager to push forward

**Gregory's Confidence:**
- Should be ready for next week
- Flu today but manageable

### 14. Video Production Discussion

**Cooking Video Status:**

**Zen's Question:** When will cooking video be finished?

**Gregory's Response:**
- Recording tonight
- Send to Ann (video editor) over weekend
- Ann will return Monday or Tuesday

**Previous Video Feedback:**
- Kept saying "and more and more and more"
- Should specifically mention: VWAP, TWAP, features
- Should mention more login methods (wasn't in previous video)
- Started inside app (should show full user journey)

**Zen's Agreement:**
- Video should be more specific about features
- Better feature callouts needed

**Zen's Question:** Is app quick and smooth now?

**Gregory:** Yes, testing tonight to confirm

**Action:** Gregory to update Zen on video quality after testing

### 15. AI Journal Tuesday Calls

**Gregory's Addition:**
- Added Zen to recurring Tuesday 12:30 UK calls
- AI journal discussions
- Zen confirmed: Perfect timing, will join

**Clarification:**
- Daniel calls are Thursdays
- AI journal is Tuesdays

**Zen's Request:**
- Remind him on Tuesday before call
- Thought it was Daniel call, didn't join previously

**Token Terminal & DRX:**
- Gregory saw Token Terminal or DRX anyway on LinkedIn
- Daniel and Kamal involved
- Ali sent Gregory the link
- Meets token terminal Sept 1-2, 9am-6pm (assumes Daniel and Kamal)

### 16. Budget Reduction Discussion

**Zen's Question:** Has Gregory spoken to Daniel about budget cut?

**Gregory's Update:**
- Told Daniel NOT increasing budget (Daniel had requested increase)
- Told Daniel may need to decrease

**Zen's Direction:**
- Talked to Daniel on call
- Told him budget dropping to $25-30K range

**Gregory's Status:**
- Daniel said waiting for update from Zen after Zen spoke to respective parties

**Current State Analysis:**

**Zen's Question:** Can we actually get down to $25K based on resources?

**Gregory's Assessment:**
- Already cut down quite a lot
- Only unused resources are those done with "besties"
- Daniel will be "very funny" about cutting those

**Zen's Position:**
- Cut down a bit more
- Give ultimatum: it's $30K
- If comes out of salaries, so be it
- Other than AI journal, nothing else for them to work on

**Gregory's Note:**
- Stashed super low priority
- Done by October 15th
- Being submitted to App Store
- After that, only AI dollar journal

**Next Steps:**
- Gregory to have call with Daniel next week
- Communicate: This is budget, these are resources to keep
- Daniel will figure out distribution

**Protected Resources (Non-negotiables per Zen):**
- **Daniel:** Cannot reduce
- **Ali:** Cannot reduce
- **Gandola:** Potentially protected (implied)
- **Shakeib:** Covered separately by Zen/Gregory

**Budget Math:**
- $30K total
- Ali and Gandola: ~$10K
- Leaves $20K for rest of team
- Room for approximately 8 people

**Zen's Rationale:**
- Other resources haven't really proven themselves
- Don't use too much
- Make clear to Daniel: Cannot decrease protected resources
- Don't want Daniel to then supplement after cutting key people
- Defeats purpose of budget reduction

**Strict Guidelines for Daniel:**
- Cannot decrease Daniel's salary
- Cannot decrease Ali's salary
- Non-negotiables must be clear

### 17. Dubai Trip Planning

**Timeline:** November 5-15, 2025

**Gregory's Note:**
- One month away, should start planning

**Zen's Timeline:**
- R the Labs: November 2nd or 1st (approximate)
- Thinks November 5-15 correct (was thinking 13th)

**Accommodation:**
- Gregory asks if Naji wants to share accommodation again
- Naji agrees

**Shakeib Consideration:**
- Zen wants to bring Shakeib
- Visa issues currently
- Working with visa immigration representatives
- Waiting for Shakeib to get attested documents
- Looking 50/50 right now

**Purpose:**
- Be together every day
- Brainstorming sessions
- Look at improvement opportunities
- More productive than last time

**Gregory's Memory:**
- Last Dubai trip: Planned longer, then Zen had to leave suddenly
- This one should be more productive

**Zen's Arrival:**
- Will be there few days before 5th
- Likely arriving November 3rd or 4th

**Gregory:** Will double-check dates (thought it was 5th-13th)

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Market cap as default chart view | Better metric for traders | Price becomes secondary view |
| GitBook Pro annual subscription | Professional documentation needed | Cost in next invoice |
| Record video demo this afternoon | Platform ready for showcase | Pause deployments during recording |
| Budget reduction to $25-30K range | Financial constraints | Team restructuring needed |
| Protect Daniel and Ali salaries | Critical team members | Non-negotiable in budget cuts |
| On-Ramp implementation starts Monday | Final major development piece | Last feature before beta |
| Dubai trip November 5-15 | Coworking and collaboration | All key team members invited |
| Share accommodation in Dubai | Cost efficiency | Naji and Gregory confirmed |
| Try to bring Shakeib to Dubai | Team collaboration benefit | Pending visa resolution (50/50) |

## Action Items

### High Priority

- [ ] **Lucas** - Access and pay GitBook Pro plan (annual) this afternoon (Due: September 26, 2025)
- [ ] **Lucas** - Update GitBook documentation (Due: September 26-28, 2025)
- [ ] **Lucas** - Share GitBook with team for review (Due: September 28, 2025)
- [ ] **Lucas** - Research and suggest CRM solution for CS team (Due: October 3, 2025)
- [ ] **Naji** - Notify Lucas before starting video recording (Due: September 26, 2025)
- [ ] **Naji/Gregory** - Test product and record video demo this afternoon (Due: September 26, 2025)
- [ ] **Team** - Begin On-Ramp (On-Ramper) implementation (Due: September 29, 2025)

### Medium Priority

- [ ] **Gregory** - Complete PPS wireframes (Due: September 27-28, 2025)
- [ ] **Gregory** - Have budget discussion call with Daniel next week (Due: October 3, 2025)
- [ ] **Gregory** - Communicate budget is $30K, identify resources to keep (Due: October 3, 2025)
- [ ] **Gregory** - Send completed video to Ann for editing over weekend (Due: September 28, 2025)
- [ ] **Gregory** - Remind Zen before Tuesday AI journal call (Due: October 1, 2025)
- [ ] **Zen** - Join Tuesday AI journal calls at 12:30 UK (Due: Recurring, starting October 1)

### Low Priority

- [ ] **Team** - Plan Dubai trip logistics for November 5-15 (Due: October 26, 2025)
- [ ] **Gregory** - Double-check Dubai trip dates (Due: October 1, 2025)
- [ ] **Naji** - Coordinate Dubai accommodation with Gregory (Due: October 26, 2025)
- [ ] **Zen** - Work on Shakeib visa for Dubai trip (Due: October 26, 2025)
- [ ] **Shakeib** - Get attested documents for visa (Due: October 15, 2025)

## Technical Notes

### Performance Achievements (Final)
- **Loading times:** 30 seconds → 1-1.5 seconds
- **Chart population:** Dramatically improved
- **Market cap tracking:** Complex implementation completed
- **Two engineers dedicated:** Multiple optimization fronts

### Market Cap Implementation
- Critical for trader decision-making
- Complex technical challenge solved
- Y-axis now supports market cap display
- Can toggle between price and market cap
- Supports Solana and USD valuation

### Indexer Fixes
- Bonding curve marking accuracy
- Duplicate tracking elimination (double-counting resolved)
- Token supply tracking for bars
- Price outlier filtering
- Pump fund trade filtering

### On-Ramp Integration
- Final major development piece
- On-Ramper solution as agreed
- Implementation starts Monday (September 29)
- Critical for user onboarding

### GitBook Documentation
- Pro plan required for custom URL
- Annual subscription for cost efficiency
- Professional documentation platform
- Custom domain: cooking-docs

## Risks & Blockers

| Risk/Blocker | Impact | Mitigation |
|--------------|--------|------------|
| Budget reduction to $25-30K | Team restructuring required | Protect key resources (Daniel, Ali) |
| Some resources may be cut | Reduced capacity | Only cutting unproven/unused resources |
| Shakeib Dubai visa uncertain | May miss collaboration opportunity | Working with immigration reps (50/50 chance) |
| Video demo this afternoon | Risk of bugs appearing | Team has tested thoroughly |
| On-Ramp implementation starting | Last major piece before beta | Clear requirements, proven solution |
| Bonding curve marking issues | Incorrect token status | Testing multiple implementations |
| Portfolio duplicate tracking | Incorrect valuations shown | Fix in progress |

## Next Steps

1. **Today (Sept 26):** Purchase GitBook Pro, record video demo
2. **This Weekend:** Complete PPS wireframes, video editing begins
3. **Monday (Sept 29):** Begin On-Ramp implementation, GitBook documentation update
4. **Next Week:** Budget discussion with Daniel, video completed
5. **Early October:** Complete On-Ramp integration
6. **Mid-October:** Stashed submitted to App Store (October 15)
7. **November 5-15:** Dubai coworking trip with team

## Key Metrics & Numbers

- **Loading time improvement:** 30 seconds → 1-1.5 seconds (95% reduction)
- **Engineers on performance:** 2 dedicated full-time
- **PPS wireframes completion:** 70% (finishing this weekend)
- **Budget target:** $25-30K (reduction from current)
- **Protected salaries:** Daniel + Ali = ~$10K
- **Remaining budget:** ~$20K for ~8 people
- **Dubai trip dates:** November 5-15, 2025 (potentially 3-15 for Zen)
- **Shakeib visa probability:** 50/50
- **Stashed submission date:** October 15, 2025
- **Video editing turnaround:** Weekend → Monday/Tuesday

## References

- On-Ramper (on-ramp solution)
- GitBook Pro (documentation platform)
- Epic Figma (design reference for PPS)
- Token Terminal / DRX (Daniel and Kamal meeting)
- R the Labs (November 1-2, Dubai event)
- Ann (video editor)

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-20
