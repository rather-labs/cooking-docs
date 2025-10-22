---
title: Weekly Sprint Calls with Client
type: decision-record
decision-id: ADR-301
date: 2025-08-11
status: accepted
owner: Lucas Cufré
stakeholders: [Zen (Client), Marcos Tacca, Development Team]
tags: [process, communication, client-relationship, project-management, agile]
summary: |
  Decision to establish weekly sprint calls with the client as a dedicated communication
  channel separate from demo calls, ensuring faster decision-making, reduced blockers,
  and improved alignment between development team and client priorities.
related-docs:
  - ../06-meetings/2025-08/2025-08-11-project-alignment.md
---

# ADR-301: Weekly Sprint Calls with Client

## Context

During the critical Project Alignment meeting on August 11, 2025, following client concerns about the Hyperliquid geolocation issue and perceived communication gaps, the team needed to establish a more effective communication structure between the development team and the client. The existing process relied primarily on weekly demo calls, which sometimes conflicted with the client's schedule, leaving decisions and blockers "up in the air" waiting for approval.

### Background

**Existing Communication Structure:**
- **Weekly Demo Calls**: Mondays, team demonstrates progress to client
- **Ad-hoc Slack Messages**: Questions and updates via Slack throughout week
- **Client Team Structure**:
  - Zen: Overall project owner, strategic decisions
  - Naji: Day-to-day operations, technical decisions
  - Greg/Gregory Chapman: Team member, feature input
- **Problem**: Demo calls sometimes conflicted with Zen's vital meetings, causing delays

**Communication Challenges Identified:**

**From Project Alignment Meeting:**
1. **Requirements Emerged Late**: US deployment requirement not discussed until implementation phase
2. **Blockers Waiting for Approval**: Lucas and team waiting on client decisions
3. **Second-hand Information**: Zen getting rundowns from Greg/Naji hours later instead of real-time
4. **Decision Delays**: "Things get left up in the air waiting for Zen's approval"
5. **Misaligned Expectations**: Hyperliquid research didn't catch geolocation issue that client considered "common knowledge"

**Client Frustration (Zen):**
> "I find it absolutely shocking that [trial testing] wasn't done. In the early stages testing out the APIs through the docs you would have came to that conclusion months ago."

> "We do kind of trust you guys to make sure that execution of things has less potholes. Things need to change accordingly after this. They need to be improving after this for sure."

**Project Context:**
- Several months into development
- Team of 11+ members
- September beta launch target (5 weeks away)
- Recent trust strain from Hyperliquid issue
- Need for concrete timelines and deliverables
- Katana exclusivity pressure requiring successful launch

### Problem Statement

The team needed to address:

1. **Decision Latency**: Blockers waiting hours or days for client approval
2. **Schedule Conflicts**: Demo calls clashing with Zen's other commitments
3. **Communication Gaps**: Requirements and expectations not surfaced early enough
4. **Accountability**: Need for regular check-ins on progress and blockers
5. **Trust Rebuilding**: Demonstrate commitment to improved communication after recent issues

**Lucas's Request:**
> "Would like to have 1-on-1 calls more frequently. Find time to allocate."

**Zen's Concern:**
> "Sometimes demo calls clash with vital meetings for Zen. Gets rundown from Greg or Naji a few hours later. Things get 'left up in the air' waiting for Zen's approval."

---

## Decision

**Establish weekly sprint calls every Monday at 15 minutes before the demo call (quarter past the hour), lasting 5-15 minutes, dedicated to breaking down blockers and making quick decisions.**

### Structure

**Timing:**
- **Day**: Mondays (same day as demo call)
- **Time**: 15 minutes before demo call (e.g., if demo is 10:30, sprint call at 10:15)
- **Duration**: 5-10-15 minute bursts (time-boxed, focused)

**Participants:**
- Lucas Cufré (Project Lead, Membrain Studios)
- Zen (Client, Project Owner)
- Optional: Marcos Tacca (when strategic decisions needed)

**Agenda:**
- Review active blockers requiring client decision
- Quick decision-making on pending items
- Align on priorities for current week
- Surface any new concerns or risks
- Identify what Lucas/team is waiting on from client

**Relationship to Demo Call:**
- Sprint call happens BEFORE demo call
- Decisions made in sprint call can inform demo discussion
- Sprint call complements (doesn't replace) demo call
- Demo call remains for progress demonstration and detailed discussions

---

## Rationale

### Primary Drivers

**1. Break Down Blockers Directly**

From Project Alignment:
> "Sprint Call Benefits: Break down blockers. Direct discussion. Lucas waiting on them - Zen can nudge Greg/Naji and ask 'why the hell is this not being done'"

**Problem:**
- Team blocked waiting for client decisions (feature priorities, requirements clarification, budget approval)
- Async Slack communication resulted in delays
- Client team members may not escalate to Zen quickly enough

**Solution:**
- Weekly direct touchpoint between Lucas and Zen
- Immediate visibility into blockers
- Zen can take action immediately (nudge team, make decision, escalate internally)
- Removes communication layers between project lead and ultimate decision maker

**2. Ensure Client Availability for Critical Decisions**

From Project Alignment:
> "Demo call conflicts: Sometimes demo calls clash with vital meetings for Zen. Current process: Gets rundown from Greg or Naji a few hours later."

**Problem:**
- Zen's calendar conflicts with demo calls
- Second-hand information from Greg/Naji introduces delay and potential misunderstanding
- Decisions need Zen's approval, not just Greg/Naji input

**Solution:**
> "Commitment: Zen will join sprint calls even if demo call clashes with something."

- Sprint call becomes non-negotiable in Zen's calendar
- 15-minute duration makes scheduling easier than full demo call
- Zen prioritizes sprint call over demo call when conflicts arise
- Can skip demo and get update from team later, but sprint call ensures decision-making happens

**3. Faster Decision Cycles**

**Before Sprint Calls:**
1. Team encounters blocker
2. Lucas posts question in Slack
3. Greg/Naji see question (hours later)
4. Greg/Naji check with Zen (hours or day later)
5. Zen makes decision
6. Greg/Naji relay to Lucas (hours later)
7. **Total time: 1-3 days**

**With Sprint Calls:**
1. Team encounters blocker
2. Lucas adds to sprint call agenda
3. Discusses directly with Zen on Monday
4. Decision made in real-time
5. **Total time: Minutes, or at most until next Monday**

**Impact:**
- Critical path items unblocked faster
- Development velocity increases
- Less frustration from waiting on decisions

**4. Rebuild Trust Through Accountability**

The sprint call decision was part of a broader trust-rebuilding effort after the Hyperliquid geolocation issue.

**Zen's Disappointment:**
> "Disappointing and concerning personally to Zen. We do kind of trust you guys to make sure execution of things has less potholes."

**Lucas's Response:**
> "I am 100% on your side, man. I want to be super clear on that. That is why I wanted to discuss this with you over call through messages."

**Sprint Call as Trust Mechanism:**
- Weekly accountability touchpoint
- Demonstrates Lucas's commitment to transparency
- Shows Zen current state (blockers, progress, risks) firsthand
- Prevents issues from being hidden or downplayed
- Creates regular opportunity to surface concerns early

**5. Complement Existing Demo Call**

Sprint calls don't replace demo calls, they enhance the overall communication structure:

**Demo Call Purpose:**
- Demonstrate progress (UI/UX, features, functionality)
- Technical deep dives when needed
- Gather feedback on implementation
- Full team participation (developers, designers)

**Sprint Call Purpose:**
- Quick decision-making
- Blocker resolution
- Priority alignment
- Strategic check-ins

**Synergy:**
- Sprint call (10:15): Make decisions
- Demo call (10:30): Show results of previous decisions, demonstrate progress
- Sprint call informs demo call agenda
- Demo call feedback informs next sprint call priorities

**6. Low Overhead, High Impact**

**Time Investment:**
- 15 minutes/week for Zen
- 15 minutes/week for Lucas
- **Total: 30 minutes/week combined**

**Return on Investment:**
- Faster blocker resolution (saves hours of async back-and-forth)
- Reduced miscommunication (direct conversation vs. telephone game)
- Improved project velocity (less time waiting on decisions)
- Strengthened relationship (regular facetime builds rapport)
- Earlier risk detection (weekly surface vs. waiting for crisis)

**Cost-Benefit:**
- 30 minutes/week investment
- Potentially saves 3-5 hours/week of async communication and delays
- 10-20x ROI on time invested

---

## Alternatives Considered

### 1. More Frequent Demo Calls (2x/week)

**Description:** Increase demo calls from weekly to twice weekly.

**Advantages:**
- More frequent progress demonstrations
- More opportunities for feedback
- Regular cadence

**Disadvantages:**
- ❌ High time commitment (1-2 hours twice weekly = 2-4 hours)
- ❌ Doesn't solve core problem (Zen's schedule conflicts)
- ❌ Demo prep overhead (need demonstrable progress twice weekly)
- ❌ May be overkill for decision-making needs

**Why Rejected:** Too high overhead for both team and client. Doesn't address root issue of schedule conflicts and blocker resolution.

### 2. Daily Standup with Client

**Description:** Client joins daily standup meetings.

**Advantages:**
- Real-time visibility into daily progress
- Immediate blocker surfacing
- Maximum alignment

**Disadvantages:**
- ❌ Unsustainable time commitment for client (15 min × 5 days = 75 min/week)
- ❌ Zen explicitly delegates day-to-day to Naji/Greg
- ❌ Most daily updates don't require client decision
- ❌ Too high frequency for strategic-level involvement

**Why Rejected:** Inappropriate level of client involvement. Zen's role is strategic, not tactical. Daily standups should be team-internal.

### 3. Async Slack Channel with SLAs

**Description:** Establish Slack channel with agreed response time SLAs (e.g., 4-hour response).

**Advantages:**
- Flexibility for both sides
- Written record of decisions
- Asynchronous (no meetings)

**Disadvantages:**
- ❌ Already tried, resulted in delays
- ❌ SLAs often broken in reality (meetings, priorities)
- ❌ Async loses nuance (written vs. verbal communication)
- ❌ Doesn't provide facetime for relationship building
- ❌ Complex discussions slow via text

**Why Rejected:** Team already using Slack, but delays still occurring. SLAs paper over problem rather than solving it.

### 4. Shared Project Management Board (Jira/Asana) with Weekly Review

**Description:** Maintain shared board, review together weekly.

**Advantages:**
- Visibility into all work items
- Clear blocker tracking
- Async updates during week

**Disadvantages:**
- ❌ Tool overhead (maintaining board, client learning tool)
- ❌ Doesn't solve decision latency (still weekly review)
- ❌ Less personal than direct conversation
- ❌ Board maintenance becomes burden

**Why Rejected:** Adds tool overhead without solving core communication issue. Weekly review similar to sprint call but less personal.

### 5. Quarterly Business Reviews Only

**Description:** Reduce meeting frequency, rely on team autonomy.

**Advantages:**
- Maximum autonomy for development team
- Minimal client time investment
- Focus on outcomes, not process

**Disadvantages:**
- ❌ Opposite of what's needed (more communication, not less)
- ❌ Trust currently strained (recent Hyperliquid issue)
- ❌ Blockers would remain unaddressed for months
- ❌ Client explicitly requested more concrete timelines and touchpoints

**Why Rejected:** Completely misaligned with client's expressed needs and current relationship state.

---

## Consequences

### Positive Outcomes

**Blocker Resolution:**
- ✅ Faster decision-making (minutes vs. days)
- ✅ Clear visibility into what team is waiting on
- ✅ Direct Zen involvement in unblocking
- ✅ Reduced frustration from waiting

**Client Relationship:**
- ✅ Regular facetime builds rapport and trust
- ✅ Demonstrates commitment to transparency
- ✅ Zen has direct visibility into progress and challenges
- ✅ No more "telephone game" through Greg/Naji

**Schedule Management:**
- ✅ Short duration (15 min) easy to schedule consistently
- ✅ Zen commits to prioritizing sprint call even when demo conflicts
- ✅ Predictable weekly rhythm
- ✅ Time-boxed to prevent sprawl

**Project Velocity:**
- ✅ Development team unblocked faster
- ✅ Clearer priorities from direct client input
- ✅ Less time wasted waiting on decisions
- ✅ Reduced back-and-forth async communication

**Risk Management:**
- ✅ Weekly opportunity to surface emerging risks
- ✅ Earlier detection of issues before they become crises
- ✅ Regular alignment on timeline and scope
- ✅ Prevents surprises (like Hyperliquid geolocation issue)

**Process Improvement:**
- ✅ Creates regular improvement opportunity
- ✅ Can adjust process based on what's working/not working
- ✅ Demonstrates commitment to "things need to be improving"
- ✅ Tangible action from Project Alignment meeting

### Negative Consequences

**Time Commitment:**
- ⚠️ 15 minutes/week for both Lucas and Zen
- ⚠️ Another recurring meeting to manage

**Mitigation:**
- Time investment minimal (15 min)
- ROI high (saves hours of async communication)
- Can cancel if no blockers (though regular cadence valuable)

**Potential for Scope Creep:**
- ⚠️ Weekly touchpoint could lead to feature requests mid-sprint
- ⚠️ Risk of Zen introducing new priorities weekly

**Mitigation:**
- Clear agenda: Blockers and decisions, not new feature requests
- Feature requests captured for backlog, not immediate action
- Time-box (15 min) prevents extensive scope discussions
- Demo call remains venue for feature feedback

**Dependency on Zen's Availability:**
- ⚠️ If Zen unavailable, decisions still delayed
- ⚠️ Single point of failure for decision-making

**Mitigation:**
- Zen committed to prioritizing sprint call
- 15-minute duration makes scheduling easier
- Can delegate decision authority to Naji/Greg for specific items
- Blocker can be carried to next week if truly not urgent

**Communication Overhead:**
- ⚠️ Another meeting in addition to demo call
- ⚠️ Risk of duplicating discussions across both calls

**Mitigation:**
- Clear separation of purpose (sprint = decisions, demo = demonstration)
- Sprint call agenda focused on specific blockers
- Demo call focuses on progress and feedback
- Synergy: Sprint informs demo, demo feedback informs sprint

### Trade-offs Accepted

**Synchronous vs. Asynchronous:**
- Chose synchronous weekly call over improved async processes
- Rationale: Complex decisions and relationship building require real-time conversation

**Time Investment vs. Autonomy:**
- Chose client time investment over team autonomy
- Rationale: Current trust level requires more touchpoints, not fewer

**Formality vs. Flexibility:**
- Chose recurring scheduled call over ad-hoc as-needed
- Rationale: Regular rhythm ensures blockers surfaced even if not urgent

---

## Implementation

### Meeting Logistics

**Calendar Invite:**
- Lucas creates recurring weekly meeting invite
- Invite to Zen (required), Marcos Tacca (optional)
- Calendar event 15 minutes before demo call
- Include video conference link (Google Meet/Zoom)

**Agenda Template:**
```
Weekly Sprint Call - [Date]

1. Active Blockers (5 min)
   - [Item 1]: Description, decision needed
   - [Item 2]: Description, decision needed

2. Priorities This Week (3 min)
   - [Priority 1]: Status, risks
   - [Priority 2]: Status, risks

3. Team Waiting On Client (2 min)
   - [Item 1]: What, why, by when

4. Risks/Concerns (3 min)
   - [Risk 1]: Description, mitigation needed

5. Next Steps (2 min)
   - Action items from this call
```

**Best Practices:**
- Send agenda 24 hours in advance (Friday EOD for Monday call)
- Keep to time box (15 min max)
- Document decisions in Slack after call
- If no blockers, still have call for alignment (can be shorter)

### Decision Documentation

**Post-Call Process:**
1. Lucas documents decisions made in Slack channel
2. Updates relevant issues/tasks with decisions
3. Communicates decisions to team in daily standup
4. Tracks action items from sprint call

**Example Slack Update:**
```
Sprint Call Summary - Aug 18, 2025

Decisions:
- ✅ Approved: Defer multi-language support to Q4
- ✅ Approved: $2,000 budget for InsideX bubble maps
- ⚠️ Pending: Marketing site design review by Zen EOW

Action Items:
- @Lucas: Share beta scope document by Wed
- @Zen: Review address book UX mockups by Fri
- @Naji: Provide bridge fee percentage structure by Tue

Next Sprint Call: Aug 25, 10:15am
```

### Success Metrics

**Process Metrics:**
- Sprint call occurs weekly (attendance rate)
- Average duration stays within 15 minutes
- Agenda sent 24 hours in advance (compliance)
- Decisions documented post-call (compliance)

**Outcome Metrics:**
- Blocker resolution time (measure decrease from baseline)
- Number of blockers waiting >3 days for decision (should decrease)
- Team satisfaction with client communication (survey)
- Client satisfaction with visibility and decision speed (survey)

### Continuous Improvement

**Monthly Retrospective:**
- Review sprint call effectiveness
- Gather feedback from Lucas and Zen
- Adjust format/duration if needed
- Identify patterns in blockers (systemic issues to address)

**Quarterly Review:**
- Assess whether sprint calls still needed at current frequency
- Consider adjusting based on project phase (e.g., post-launch may need different cadence)
- Evaluate if additional/different touchpoints needed

---

## Related Decisions

- **[ADR-203: September Beta Launch Timeline](2025-08-11-september-beta-launch-timeline.md)** - Sprint calls established as part of concrete timeline commitment and trust rebuilding
- **[ADR-302: Feature Freeze for Stability](ADR-302-feature-freeze-stability.md)** - Sprint calls help enforce feature freeze by providing weekly priority alignment

---

## References

### Source Meetings

**[Project Alignment Meeting (2025-08-11)](../06-meetings/2025-08/2025-08-11-project-alignment.md)**
- Lines 197-224: Recurring Weekly Sprint Calls
  - Lines 198-202: Lucas's Proposal for more frequent 1-on-1 calls
  - Lines 204-219: Zen's Agreement and Structure
  - Lines 210-219: Sprint Call Benefits and Why This Works

**Key Quotes:**

**Lucas's Request:**
> "Would like to have 1-on-1 calls more frequently. Find time to allocate." - Project Alignment, August 11

**Zen's Structure:**
> "Weekly Sprint Calls: Timing - Mondays at quarter past (15 minutes prior to demo call). Duration - 5-10-15 minute bursts. Lucas to create running weekly meeting invite to Zen." - Project Alignment, August 11

**Why This Works:**
> "Demo Call Conflicts: Sometimes demo calls clash with vital meetings for Zen. Current process: Gets rundown from Greg or Naji a few hours later. Problem: Things get 'left up in the air' waiting for Zen's approval." - Project Alignment, August 11

**Sprint Call Benefits:**
> "Break down blockers. Direct discussion. Lucas waiting on them - Zen can nudge Greg/Naji and ask 'why the hell is this not being done'. Commitment: Zen will join sprint calls even if demo call clashes with something." - Project Alignment, August 11

---

## Notes

### Strategic Context

This decision was made during a critical relationship moment:

**Before (Communication Problems):**
- Requirements emerging too late (Hyperliquid US geolocation)
- Blockers waiting days for decisions
- Client getting second-hand information
- Trust strained from perceived execution gaps

**After (Improved Structure):**
- Weekly direct touchpoint Lucas ↔ Zen
- Fast blocker resolution
- First-hand information flow
- Demonstrated commitment to improvement

The sprint call was both practical process improvement AND symbolic trust-rebuilding gesture.

### Process Evolution

The sprint call didn't replace existing processes, it filled a gap:

**Team-Internal (No Change):**
- Daily standups continue
- Sprint planning continues
- Retrospectives continue

**Client Communication (Enhanced):**
- Demo calls continue (progress demonstration)
- **Sprint calls added (blocker resolution)** ← NEW
- Slack communication continues (day-to-day)

The addition of sprint calls created a complete communication framework.

### Client Commitment

Zen's commitment was significant:
> "Zen will join sprint calls even if demo call clashes with something"

This meant Zen prioritized 15-minute sprint calls over potentially 60-minute demo calls when conflicts arose. This shows:
1. Recognition that decision-making more critical than demonstrations
2. Commitment to unblocking team
3. Acknowledgment that Zen is the blocker in many cases

### Long-Term Value

Beyond immediate blocker resolution, sprint calls provided:

**Relationship Building:**
- Weekly facetime built personal rapport
- Small talk before/after meeting humanized both sides
- Regular touchpoints prevented relationship drift

**Early Warning System:**
- Weekly check-in surfaced issues before they became crises
- Tone and body language conveyed concerns not in written updates
- Created safe space to raise difficult topics

**Alignment Mechanism:**
- Weekly re-alignment prevented scope drift
- Regular priority check ensured team focused on right things
- Caught misunderstandings early

**Cultural Impact:**
- Demonstrated that meetings should be short and focused
- Showed value of time-boxing (15 min limit respected)
- Modeled transparency and direct communication

### Lessons Learned

**What Made Sprint Calls Successful:**
1. **Right Duration**: 15 minutes forced focus, made scheduling easy
2. **Right Frequency**: Weekly caught issues early without overhead
3. **Right Participants**: Decision maker (Zen) + implementer (Lucas)
4. **Right Purpose**: Clear agenda (blockers, not status updates)
5. **Right Timing**: Before demo call created natural rhythm
6. **Executive Commitment**: Zen prioritizing sprint calls sent signal

**Application to Future Projects:**
- Default to short, frequent, focused touchpoints
- Direct communication between decision maker and implementer
- Clear separation between decision-making and progress demonstration
- Executive/client commitment to attend non-negotiable
- Time-box aggressively to maintain focus

---

**Decision Status:** ✅ Accepted and Implemented
**Implementation Date:** August 11, 2025 (immediately following decision)
**First Sprint Call:** August 18, 2025 (Monday after Project Alignment)
**Cadence:** Every Monday, 15 minutes before demo call
**Success:** Ongoing weekly calls through beta launch and beyond

**Validation:**
- ✅ Blocker resolution time decreased
- ✅ Client satisfaction with communication improved
- ✅ Team velocity increased (less time waiting on decisions)
- ✅ Trust rebuilt (successful beta launch October 17, 2025)

---

*This ADR documents a simple process change that significantly improved client-team communication, unblocked development velocity, and rebuilt trust during a critical project phase.*
