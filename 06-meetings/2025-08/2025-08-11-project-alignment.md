---
title: Project Alignment - 2025-08-11
type: meeting-note
date: 2025-08-11
---# Project Alignment Meeting with Zen

**Date:** August 11, 2025
**Time:** 10:14 GMT-03:00
**Duration:** ~22 minutes
**Meeting Type:** Project Alignment / Crisis Management
**Language:** Spanish/English (translated to English)

## Attendees
- **Lucas Cufré** - Project Lead (Membrain Studios)
- **Marcos Tacca** - Head of Projects (Membrain Studios)
- **Zen** - Client Representative (Cooking.gg)

## Meeting Context

Critical escalation meeting to address timeline concerns and major technical blockers. The proposal and meeting minutes had been sent. The project was accelerated due to an exclusivity agreement with Katana for launching a gamified launchpad. Lucas's main concern was the roadmap and delivery date, as the Hyperliquid integration required an architectural change due to a US geolocation limitation, which generated confusion and disappointment from Zen for not having been considered previously.

---

## Summary

Lucas Cufré informed that the proposal and meeting minutes have been sent, and that the project has been accelerated due to an exclusivity agreement with Katana to launch a gamified launchpad. Lucas's main concern is the roadmap and delivery timeline, as the Hyperliquid integration required an architectural backend change due to a US geolocation limitation discovered when trying to move to mainnet. This generated confusion and disappointment from Zen, who questioned why this wasn't planned for previously since Hyperliquid's US ban is common knowledge. Both agreed to establish weekly meetings to discuss blockers and ensure progress.

---

## Key Discussion Points

### 1. Proposal and Project News (00:00:00, 00:01:46)

**Documentation Submitted:**
- Proposal has been sent by email
- Meeting minutes included (Lucas mentioned he tagged Marcos in the minutes)

**Project Acceleration:**
- **Katana Exclusivity Agreement:** Cooking.gg has an exclusivity deal with Katana network
- **Goal:** Be the first to launch this type of launchpad on their network
- **Unique Aspects:**
  - Gamified launchpad
  - Solving a failed product launch problem
- **Pressure:** Previous product launch failed, now Katana appears to be applying pressure

**Additional Context:**
- Meeting included Gonzalo from Impossible Finance (consulting firm working with them)
- Two people from Kensei present: "Fox" and "Deus"

### 2. Timeline Concerns and Hyperliquid Integration (00:03:29, 00:05:02)

**Lucas's Main Concern:**
- Roadmap and delivery date
- Committed to delivering on a timely schedule

**Critical Technical Blocker - Hyperliquid Geolocation:**
- **Problem:** Hyperliquid integration required changing the entire backend architecture
- **Discovery:** Geolocation limitation found when trying to move to mainnet
- **Impact:** Everything done until now had to be refactored to deploy perpetuals

**Features Pushed to Next Quarter:**
1. **Multi-language support** - Reset modes when going to production
2. **Portfolio-wide Take Profit/Stop Loss**
3. **Market Cap Variation Algorithm**

**Note:** These three features discussed and agreed with "Gre" (likely Greg) last Friday to be first-priority items for the next quarter.

### 3. Communication Challenges and Implementation Strategy (00:06:34, 00:08:10, 00:11:06)

**Zen's Concerns and Confusion:**
- **Common Knowledge:** Hyperliquid being banned in the US is well-known
- **VPN Requirement:** Traders use VPNs to access perpetuals on other platforms
- **Question:** Why wasn't this planned for after 1-2 months of research?
- **Expectation:** Research should have identified this blocker and limitation upfront

**Lucas's Explanation - Research Scope:**
- **Focus:** Initial research centered on implementation and how to monetize Hyperliquid
- **Timeline:** About a week and a half of research (compressed timeline)
- **Simultaneous Work:** Also working on many other features during this period

**Communication Gap:**
- **US Deployment Requirement:** Only discovered they were trying to go to market in the US "way after" the research
- **Never Discussed:** US deployment wasn't part of initial discussions
- **When It Emerged:** Rose to prominence when discussing go-to-market strategy for mobile
- **Acknowledgment:** Maybe should have discussed this earlier - difficulty of communication

**API vs. UI Assumption (00:08:10):**
- **Hyperliquid T&C:** Explicitly state Hyperliquid is not accessible via interface/UI
- **Says Nothing About API:** Terms don't mention API restrictions
- **Assumption:** Through APIs, could access from US locations without problem
- **Discovery:** When switching to deployment, found out servers were geolocated in the US
- **Timing:** "Way too late" - couldn't have found out until integration work was done

### 4. Disappointment and Resource Allocation (00:09:43, 00:12:32)

**Zen's Strong Concerns:**

**Testing Expectations:**
- When integrating any third party, should always do a trial run
- Test in smaller capacity first
- **Shock:** That this wasn't done

**Early Stage Testing:**
- Testing APIs through docs early on should have revealed this months ago
- **Research Purpose:** Find potential blockers and limitations, and overcome them
- **Very Popular Topic:** US being blocked should have set alarm bells
- **VPN Usage:** People using VPNs means traffic filtering from different locations
- **Logical Conclusion:** "Hang on, maybe servers can't be US-based"

**Resource Investment Concerns:**
- **Team Capacity:** Significant team capacity allocated
- **Budget:** Enormous budget for this integration
- **Time Given:** "Enormous amount of time" allocated
- **Comparison:** Other teams have done Hyperliquid integration with "much smaller lower budget team"
- **Result:** Still hiccups months later

**Not Overnight Pressure:**
- This isn't a weekend/all-night pressure situation
- Team has been "enormously patient" with time and expense
- Not pressuring on weekends or giving tight unrealistic deadlines
- **Context:** Kensei is an engineering studio themselves in parallel

**Trust and Disappointment:**
- "Disappointing" and "concerning" personally to Zen
- **Trust Factor:** "We do kind of trust you guys to make sure execution of things has less potholes"
- **Expectation:** Things need to change accordingly after this
- **Requirements:** Need to be improving after this for sure

### 5. Delivery Timeline and Mobile Blocker (00:13:59, 00:15:36)

**Lucas's Acknowledgment:**
- "I am 100% on your side, man"
- Wanted to discuss through call, not messages
- At the very least, owes this level of transparency

**Other Technical Improvements:**
- Working on making transactions as fast as possible
- Found a way to optimize transaction speed without dedicated exclusively-built RPC
- Making improvements on other sides

**Mobile (MOV) Additional Blocker:**
- **Apple Store Review Process:** Cannot guarantee delivery by end of September
- **Tied to:** Apple store review process timing
- **Previous Discussion:** Discussed with Greg and "NI" (likely Naji) last Friday
- **Communication:** Not sure if they conveyed this properly

**Everything Else On Track:**
- All other items working along nicely

### 6. Launch Timelines and Concrete Deliverables (00:15:36, 00:17:14)

**Zen's Strategic Shift - Concrete Timelines:**

**The Gray Area Problem:**
- Long marathon build (several months)
- Gets gray when it comes to "beta launch," "V1," "V2"
- Need more concrete timelines

**September Beta Requirements:**
- **Super Important:** Beta in September
- **Not an MVP:** An actual product people can use day-to-day
- **Purpose:**
  - Get people's feedback
  - Start very light marketing
  - Start to build cult community
  - Speak to partners
- **As It's Live:** Can add additional features to it

**Request from Lucas:**
- **After the Call:** Send a message on Slack
- **Content Needed:**
  1. Everything that WILL be part of beta launch
  2. Things that WERE planned but have been dropped due to timeline issues (like Hyperliquid)
- **Purpose:** External review and feedback to get everyone on the same page

**Roadmap with Time Allocations:**
- **Not Done Yet:** Roadmap needs allocated time slots for all features
- **Month Ago Discussion:** Discussed need for time estimates
- **Competitor Analysis:** Naji and Zen proposed features after looking at competitors
- **Planning Needs:**
  - How long each feature will take
  - Plan V1, V2, and future iterations
  - Which features are more important

**Zen's Personal Role:**
- Delegates day-to-day to Naji and Greg
- **Personal Focus:** Making sure the entire mission is executed
- **Needs:** Timelines for beta and first full launch

**Beta Access Model:**
- **Referral Links:** Beta access only through referral links
- **Capped Access:** Each referral link limited to ~25-50 slots (exact numbers TBD)
- **Invite-Only:** Must "hunt out" for a link to get access
- **Links for:** Close partners, advisors, etc.

**V1 Planning:**
- Need to know how long features shared ~a month ago will take
- Then choose priorities
- Determine if V1 is December, January, etc.

### 7. Recurring Weekly Sprint Calls (00:18:24)

**Lucas's Proposal:**
- Would like to have 1-on-1 calls more frequently
- Find time to allocate

**Zen's Agreement and Structure:**

**Weekly Sprint Calls:**
- **Timing:** Mondays at quarter past (15 minutes prior to demo call)
- **Duration:** 5-10-15 minute bursts
- **Lucas to Create:** Running weekly meeting invite to Zen

**Why This Works:**
- **Demo Call Conflicts:** Sometimes demo calls clash with vital meetings for Zen
- **Current Process:** Gets rundown from Greg or Naji a few hours later
- **Problem:** Things get "left up in the air" waiting for Zen's approval

**Sprint Call Benefits:**
- **Break Down Blockers:** Direct discussion
- **Lucas Waiting on Them:** Zen can nudge Greg/Naji and ask "why the hell is this not being done"
- **Commitment:** Zen will join sprint calls even if demo call clashes with something

**Pending Items:**
- Invoice pending
- Co-work situation discussed a couple months ago (left hanging)
- Zen: "Leave that with me"

---

## Decisions Made

1. **Weekly sprint calls** established - Mondays 15 minutes before demo call
2. **Three features pushed to Q4:**
   - Multi-language support
   - Portfolio-wide TP/SL
   - Market Cap variation algorithm
3. **Beta timeline:** September launch (date TBD)
4. **Mobile delivery:** Cannot guarantee end of September due to Apple review process
5. **Beta access model:** Referral-only with capped slots per link
6. **Lucas to provide:** Slack message with beta scope (in vs. out)
7. **Roadmap to be updated:** With time allocations for all features

---

## Action Items

### Lucas Cufré
1. Create weekly recurring meeting invite to Zen (Mondays, 15 min before demo)
2. Send Slack message after call with:
   - Everything included in beta launch
   - Everything dropped from beta due to timeline issues
3. Update roadmap with time allocations for all features
4. Follow up on pending invoice
5. Follow up on co-work situation

### Zen
1. Review beta scope message from Lucas
2. Provide external feedback on beta scope
3. Work with Naji/Greg on feature prioritization
4. Handle invoice situation
5. Handle co-work situation

### Team
1. Continue Hyperliquid refactor to work around US geolocation
2. Everything else on track - maintain momentum

---

## Blockers Identified

### Immediate Blockers
1. **Hyperliquid US Geolocation** - Requires full backend architecture refactor
2. **Apple Store Review Process** - Cannot control mobile launch timeline
3. **Feature Scope Clarity** - Need to document what's in/out of beta

### Process Blockers
1. **Research Depth** - Need better third-party integration validation upfront
2. **Communication** - Requirements (US deployment) emerged too late in process
3. **Testing Approach** - Should have trial-tested API access earlier

---

## Technical Insights

### Hyperliquid Integration Challenges

**The Problem:**
- Terms & Conditions: Explicitly state no UI access
- Terms & Conditions: **Silent on API access**
- Assumption: API access would work from US
- Reality: Servers geolocated and blocked from US
- Discovery: Only found out when deploying to production servers

**Research Scope Gap:**
- Research focused on: Implementation and monetization
- Research duration: ~1.5 weeks (compressed)
- Missing: Deployment geography requirements
- Missing: Early trial/testing of API access

**The Lessons:**
1. Always trial-test third-party integrations early
2. Don't assume Terms of Service silence means permission
3. Discuss deployment geography upfront
4. Research should include blockers/limitations, not just implementation

---

## Team Dynamics

**Client Relationship Strain:**
- Zen expressed disappointment and concern
- Trust has been impacted ("we do kind of trust you guys...")
- Comparison to other teams (smaller budget, faster results)
- **However:** Commitment to work together and improve

**Positive Aspects:**
- Lucas's transparency and willingness to discuss directly
- Zen's patience (not giving unrealistic deadlines, no weekend pressure)
- Agreement on weekly touchpoints
- Understanding that improvements need to happen

**Power Dynamic:**
- Zen is engineering studio themselves - understands technical complexity
- Marcos Tacca (Lucas's boss) present but mostly observing
- Zen needs to ensure "entire mission is executed"

---

## Business Context

### Katana Exclusivity Deal
- First gamified launchpad on Katana network
- Previous product launch failed
- Katana applying pressure
- Timing is critical for exclusivity

### Beta Strategy
- Referral-only access (viral growth model)
- Capped slots per link (scarcity)
- Must be functional product, not MVP
- Foundation for marketing and partnerships

### Resource Investment
- Large team allocated
- Significant budget
- Several months of development
- Client's patience wearing thin

---

## Transcript Highlights

**On Trust and Expectations (00:12:32):**
> "We do kind of trust you guys to make sure that execution of things has less, you know, potholes. We don't pressure you guys on weekends and really give you tight unrealistic deadlines because we are an engineering studio ourselves in parallel. I think this is worrying so I just want to make sure things need to change accordingly after this. They need to be improving after this for sure."

**On Research Oversight (00:09:43):**
> "I find it absolutely shocking that [trial testing] wasn't done. In the early stages testing out the APIs through the docs you would have came to that conclusion months ago. I think the whole purpose of research is to find out potential blockers and find out limitations and how we can overcome them."

**On Common Knowledge (00:06:34):**
> "It's well-known that [Hyperliquid is] banned in the US. Traders are having to use VPNs to access perpetuals on other platforms. I'm not sure why this wasn't already planned around if we're doing research tied up with two months of research on Hyperliquid."

**On Lucas's Accountability (00:13:59):**
> "I am 100% on your side, man. I want to be super clear on that. That is why I wanted to discuss this with you over call through messages."

---

## Cross-References

**Related Requirements:**
- [Hyperliquid Perpetuals Integration](../../04-knowledge-base/business/requirements/hyperliquid-perpetuals-integration.md)
- [Multi-Language Support](../../04-knowledge-base/business/requirements/multi-language-support.md)
- [Portfolio Wide TP/SL](../../04-knowledge-base/business/requirements/portfolio-wide-tpsl.md)
- [Market Cap Variation Algorithm](../../04-knowledge-base/business/requirements/market-cap-variation-algorithm.md)

**Related Meetings:**
- [2025-07-24 Hyperliquid Integration](../2025-07/2025-07-24-hyperliquid-integration.md) - Initial integration discussion
- [2025-08-18 Z & Lucas Sync](Sync-Z-Lucas-2025-08-18.md) - Previous sync meeting
- [2025-08-18 Weekly Sync](../Cooking%20Weekly%20Sync%2020250818.md) - Hyperliquid issues discussed
- [2025-08-25 Z & Lucas Sync](Sync-Z-Lucas-2025-08-25.md) - Follow-up sync

**Related Technical Topics:**
- Hyperliquid geolocation restrictions
- Backend architecture refactoring
- Third-party integration testing
- Apple App Store review process

---

## Notes

**Meeting Tone:** Professional but tense. Zen expressed clear disappointment while remaining constructive. Lucas was transparent and accountable.

**Critical Lesson:** This meeting represents a key learning moment about the importance of early integration testing and clear communication of deployment requirements.

**Relationship Status:** Strained but committed to improvement. Weekly sprint calls established as a mechanism to prevent future issues.

**Strategic Impact:** Three features pushed to Q4, but overall mission remains on track with improved communication structure.

---

**Meeting concluded at 00:21:54**

*Notes generated from Gemini transcription. This meeting marked a turning point in project communication and established the weekly sprint call cadence that would continue through the beta launch.*
