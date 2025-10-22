---
title: Sync Z <> Lucas - Indexer Issues & Ecosystem Challenges
type: meeting-note
date: 2025-09-29
attendees: [Lucas Cufré, Zen, Marcos Tacca, Federico Caccia]
meeting-type: weekly-sync
tags: [sync, indexer, solana-ecosystem, testing, quality-issues, root-cause-analysis]
summary: |
  Critical discussion addressing persistent product bugs and quality concerns with focus on root cause analysis. Lucas attributed issues to Solana ecosystem volatility - unexpected API changes from protocols (Radium, Moonshot) impacting indexer accuracy. Explained custom indexer approach provides independence but requires reverse-engineering competitors' black-box logic. Zen expressed serious concerns about obvious bugs, lack of apparent testing, and questioned team skill/seniority levels. Despite frustrations, meeting concluded with reaffirmed faith in Rather Labs for long-term partnership (3-6 year horizon).
related-docs:
  - Indexer architecture documentation
  - Solana protocol integration
  - Competitor analysis (Axium, Padre)
---

# Sync Z <> Lucas - Indexer Issues & Ecosystem Challenges

**Date:** 2025-09-29
**Duration:** ~25 minutes
**Attendees:** Lucas Cufré, Zen, Marcos Tacca, Federico Caccia
**Meeting Type:** Weekly Sync / Root Cause Analysis

## Executive Summary

**Intensive problem-solving session** focusing on persistent quality issues and their underlying causes. Lucas revealed that unexpected changes in Solana ecosystem APIs (Radium graduated tokens, Moonshot changes) are impacting the custom indexer, affecting wallet calculations and transaction data. Explained team is building independent indexer from scratch (unlike competitors who may have 2+ years head start or existing infrastructure). Zen pushed for root cause analysis beyond "trying our best" - questioned if issues stem from skill gaps, junior developers, or recruitment problems. Discussion revealed tension between generous timeline allocations (with embedded testing) and underwhelming results. Friday delivery target set with full regression testing. Despite serious concerns, Zen reaffirmed long-term partnership faith and vision for multi-year engagement.

## Discussion Topics

### Product Issues and Impact

**Greg's Friday Reports:**
- Multiple errors and bugs identified
- Visible impact on product functionality
- Concerns about demo readiness

**Root Cause - Indexer Filter:**
- Filter implemented in indexer affecting data accuracy
- **Impact Areas:**
  - Wallet calculations
  - Transaction data
  - Chart/bar data display
- **Unexpected:** Filter had broader impact than anticipated
- **Team Assessment:** "Completely on us," taking full responsibility

**Timeline:** 00:00:00 - 00:12:04

---

### Testing and Delivery Plans

**Immediate Actions:**
- Full regression testing in progress
- **First regression:** Currently running
- **Second regression:** Tomorrow
- Implementing new features in parallel
- All testing within next 48 hours

**Delivery Target:** Friday (Oct 3rd)

**Timeline:** 00:12:04

---

### Stakeholder Impact and Communication Issues

**VC Demo Situation:**
- Fidelity and other VCs requested demo
- Team had given green light for product readiness **3 weeks prior**
- **Current Reality:** 3 weeks later, still not demo-ready
- Attempted video production revealed "really poor obvious glaring mistakes and bugs"

**Weekend Response Delay:**
- Issues reported Friday
- No response over weekend
- **Impact on VCs:** "They're chasing us" (unusual/uncomfortable position)
- Team stalling and delaying while waiting for Monday response

**Zen's Concern:** When there's launch handover with problems, 2-3 day delayed response is "really crippling"

**Timeline:** 00:12:04 - 00:13:28

---

### Quality Assurance Deep Dive

**Nature of Bugs - Zen's Assessment:**
- **Not:** Penetration test level security bugs (hard to find)
- **Instead:** Obvious issues any user would notice immediately
- **No aggressive testing needed** - basic product use reveals them

**Alarming Pattern:**
- Many engineers on payroll
- Long development timeline
- **But:** "No one's using the product" internally
- First time client uses it, "all of these issues pop up"

**QA Resource Disconnect:**
- Two QA engineers supposedly assigned
- **Zen's Observation:** "It doesn't look like it"

**Timeline Generosity:**
- Extremely generous feature time allocations
- Example: If typically 5 days, team quotes 2 weeks
- **Client Acceptance Rationale:** Expecting "perfectly pristine and tested" results
- "Normal expectation" given extended timelines

**Current Pattern:**
- **Expectation:** Under-promise, over-deliver
- **Reality:** Opposite - underwhelming results

**Timeline:** 00:13:28 - 00:16:22

---

### Root Cause Analysis - Beyond Assurances

**Lucas's Initial Response:**
- Redoing all testing
- Reviewing known issues
- Rechecking previously fixed items
- Continuing feature delivery in parallel
- Promises of "best effort"

**Zen's Pushback - Need for Systemic Analysis:**

**Critical Questions:**
- Is this a skill issue on engineering side?
- Is this a recruitment problem?
- Were developers assigned too junior for actual scope?
- What is the actual root problem?

**Zen's Context:**
- Made clear from start: long-term engagement desired
- No price negotiation or haggling
- Not time-wasters
- Understand importance of "critical positive relationship"

**Intent:** "Trying to figure out how we can fix it rather than just trying our best"

**Timeline:** 00:16:22 - 00:17:40

---

### Technical Root Cause - Solana Ecosystem Volatility

**Lucas's Assessment: "Solana is a never evolving ecosystem"**

**Specific Recent Examples:**

**1. Radium Protocol:**
- Main DEX for most indexed AMMs
- "Graduated their tokens" with API change
- **Timing:** Between Wednesday and Thursday
- **Notice:** "Unannounced to anyone"

**2. Moonshot:**
- Another protocol with unannounced changes
- Similar impact on indexer

**Impact on Product:**
- These changes affect "core feature" (the indexer)
- Directly impact ability to accurately track data
- Affects comparisons with major competitors

**Lucas's Framing:**
- "Not an excuse"
- "Matter of fact assessment on what is happening in the ecosystem"
- Tool development for robust tracking "takes time"

**Timeline:** 00:17:40 - 00:19:17

---

### Competitor Comparison and Indexer Architecture

**Zen's Challenge:**
- "Our competitors like Axium and Padre... they don't go down when these things happen"
- Tool supposedly being developed to prevent this

**Lucas's Explanation - Competitor Advantages:**

**Axium Example:**
- ~2 years of development on their Solana indexer
- Mature infrastructure and tech stack
- Established pricing sources
- **Unknown:** Whether built from scratch or adapted existing indexer

**Cooking's Current State:**
- Indexing all known protocols:
  - Pump
  - Radium
  - All Jupiter indexers
- **Challenge:** Each has unique data schema and event interpretation
- Must account for each protocol's evolution
- Ongoing work, constantly adapting

**Cooking's Unique Approach - Independence:**

**Advantage:**
- "Completely independent" - not dependent on anyone
- Can interpret data however desired
- Not attached to larger provider logic
- Full control over data processing

**Trade-off:**
- Must reverse-engineer competitors' approaches
- Competitors' logic often "black box"
- Matching established players requires inferring their methods

**Timeline:** 00:19:17 - 00:24:45

---

### Long-term Partnership Reaffirmation

**Despite Frustrations - Zen's Commitments:**

**Faith Maintained:**
- "Lot of faith" in Rather Labs
- "High endorsements" given at executive level
- "Still remains unwavered"

**Long-term Vision:**
- **Not a short-term sprint**
- 3-6 year timeline ("three, four, five, six years")
- Post-launch: maintenance, new features, expansion
- Continuous development partnership

**Client Assurances:**
- Can provide longevity
- Stable long-term engagement

**Expectations:**
- "Best of the best team"
- "Best resources assigned"
- Need Rather Labs to "deliver on that faith"

**Lucas's Response:**
- "Deeply aware"
- "Doing the best that we can to make good on that promise"

**Timeline:** 00:20:57 - 00:24:45

---

## Action Items

| Owner | Action | Deadline | Status |
|-------|--------|----------|--------|
| Team | Complete first full regression test | Sept 29-30 | In Progress |
| Team | Run second full regression test | Sept 30 | Committed |
| Team | Resolve indexer filter issues | Before Friday | In Progress |
| Team | Fix wallet/transaction calculation impacts | Before Friday | In Progress |
| Lucas | Deliver product for handover | Friday, Oct 3 | Committed |
| Leadership | Evaluate team skill levels and assignments | Ongoing | Implied |

## Technical Deep Dive

### Solana Ecosystem Challenges
- **Volatility:** Protocols change APIs without notice
- **Examples:** Radium token graduation, Moonshot updates
- **Impact:** Core indexer functionality affected
- **Frequency:** Changes can happen mid-week unexpectedly

### Indexer Architecture Comparison

| Aspect | Competitors (e.g., Axium) | Cooking |
|--------|---------------------------|---------|
| Development Time | ~2 years | In progress |
| Starting Point | Possibly existing infra | Built from scratch |
| Dependency | May use larger providers | Fully independent |
| Data Control | Limited/unknown | Complete control |
| Reverse Engineering | Not needed | Required to match competitors |

### Protocol Coverage
- **Pump:** Supported
- **Radium:** Supported (with adaptation for changes)
- **Jupiter indexers:** All supported
- **Challenge:** Each has unique schema and event interpretation

### Custom Indexer Benefits
1. **Independence:** No reliance on third-party providers
2. **Flexibility:** Interpret data as desired
3. **Control:** Full logic ownership
4. **Customization:** Can build unique features

### Custom Indexer Challenges
1. **Development Time:** Building from scratch takes longer
2. **Maintenance:** Must track all protocol changes
3. **Competitive Parity:** Must reverse-engineer black-box competitors
4. **Resource Intensive:** Each protocol requires dedicated integration work

## Meeting Conclusion

**Duration:** 00:24:45
**Tone:** Tense but constructive, focused on solutions
**Outcome:** Root cause identified (ecosystem volatility + custom indexer immaturity), Friday delivery target, long-term partnership reaffirmed

---

## Transcript Highlights

### Taking Responsibility (00:00:00 - 00:12:04)
```
Lucas: "The situation is as the filter that we are implementing for the chart
it rises from the from a filter that we are implementing on the indexer that is
impacting the way that we show data on the on the charts on the bars and it had
an unexpected impact on the calculations on the portfolios on trades and
everything of the sort that is something that we did not catch before the guys
so that is completely on us and we are trying to solve that at the moment so we
take full responsibility for that."
```

### VC Demo Impact (00:12:04 - 00:13:28)
```
Zen: "We had the meeting with Fidelity and other VCs and they wanted demo. We
had a green light from you guys that the product will be ready for demo 3 weeks
ago. It's three weeks later. We tried to do the video and it's still still
really poor obvious glaring mistakes and bugs."

Zen: "We're in a position where they're chasing us which isn't the norm and
we're just stalling stalling stalling throughout the weekend and now only on
Monday the you know response has been given."
```

### Quality Concerns (00:13:28 - 00:14:55)
```
Zen: "These aren't like penetration test level security books that are very hard
to find with a you know fine toothc. These are things that if anyone just use
the product like they don't even need to be you know a very aggressive tester.
If they just use the product they would notice. So what's scary is that we have
so many engineers on the payroll and we've had this for so long but for so long
it's still like no one's using the product because the first time we use it all
of these issues pop up."
```

### Root Cause Question (00:16:22 - 00:17:40)
```
Zen: "What do you think the problem the root the root problem is... Do you think
the problem here is that It's a skill issue on the engineering side. Do you think
it's a recruitment issue? Um, do you think it's, you know, developers sign maybe
were a little bit more junior because of the scope of work initially was thought
to be?"

Zen: "I'm just trying to figure out how we can fix it rather than just trying
our best."
```

### Ecosystem Volatility (00:17:40)
```
Lucas: "Solana is a never evolving ecosystem... the radium pral that is the main
dex to towards most of the AMMs that we are indexing uh graduate their tokens
towards an aning change in their API just uh between Wednesday and Thursday and
that was on to anyone. So that is one of the changes that happened. Moon shot
had another one that was not shown for anyone."
```

### Competitive Landscape (00:19:17)
```
Zen: "You know our competitors like Axium and Padre and all these others like
they don't go down when these things happen."

Lucas: "Action has had about let's say two years or so in development for the
Rone indexer. We are we we are in the in the in the shadows regarding to their
infrastructure or the tech side of their own their own algorithm."
```

### Independent Architecture (00:20:57)
```
Lucas: "The way our indexer is is built the cooking indexer is built completely
independent. So basically we can do whatever we want and we are not attached to
to the logic of any other uh bigger provider. So we can basically interpret our
data whichever way we want. That is a big bigger plus on our side. But on another
on another level if we want to match what other players are doing we have to try
to do the inverse engineering to try to understand how they process data which is
usually a black box."
```

### Long-term Partnership (00:20:57 - 00:24:45)
```
Zen: "Let's see how this week goes in. Um, I've got a lot of faith and put a lot
of um high endorsements on Rather Labs and you guys um on the exact level. So,
you know, that still remains unwavered, but we just need to make sure like cuz
remember guys that this isn't a short-term sprint. Once we're live, we're not
walking away. We want to continue this for three, four, five, six years as long
as it takes to, you know, keep maintenance, keep new features rolling, keep new
expansion."

Lucas: "We are aware we are deeply aware and doing the best that we can to make
good on that promise."
```

## Notes
- Most technical deep-dive meeting in the series
- Reveals fundamental challenge: building competitive indexer from scratch
- Trade-off between independence (flexibility) and maturity (stability)
- Ecosystem volatility as external factor complicating development
- Despite serious concerns, both parties committed to long-term success
- Friday delivery represents critical milestone for partnership trust
