---
title: Multilevel Referral Program Structure
type: decision-record
decision-id: ADR-200
date: 2025-08-13
status: accepted
owner: Lucas Cufré, Martín Aranda
stakeholders: [Lucas Cufré, Martín Aranda, Martín Lecam, Javier Grajales, Marko Jauregui, Cooking Team]
tags: [business, referral, growth, monetization, viral-marketing, user-acquisition]
summary: |
  Decision to implement a 3-level multilevel referral program with tiered commission structure (30-45% base + up to 10% performance bonus) to incentivize viral user growth and create significant earning potential for top referrers. This program represents core profitability mechanism alongside trading limiters, with potential for $200,000+ monthly earnings for successful referrers.
related-docs:
  - ../06-meetings/2025-08/2025-08-13-referral-program-crash-course.md
  - ../06-meetings/2025-08/2025-08-11-project-alignment.md
  - ../04-knowledge-base/business/requirements/referral-program-multilevel.md
---

# Multilevel Referral Program Structure

## Context and Problem Statement

Cooking.gg needs a sustainable user acquisition strategy that:
1. Drives viral growth without large marketing budgets
2. Incentivizes quality user referrals over passive signups
3. Rewards top community builders and influencers proportionally
4. Creates competitive advantage over platforms like Photon, Bullx, and Pumpfun
5. Generates meaningful revenue sharing that motivates ongoing promotion

The platform's initial simple referral program (1-level, direct referrals only) was insufficient to compete with platforms like Pumpfun, where top referrers earn $1.5M+ monthly through multilevel structures.

**Key Requirements:**
- Must work seamlessly across web and mobile platforms
- Should scale from casual users (few referrals) to influencers (thousands of referrals)
- Needs clear, transparent commission structure
- Must integrate deeply with transaction fee collection
- Should prevent gaming while rewarding legitimate growth

## Decision

**Implement a 3-level multilevel referral program with tiered commission structure based on cumulative network trading volume.**

### Program Structure

**Referral Levels:**
- **Level 1**: Direct referrals (user's immediate referrals)
- **Level 2**: Referrals of referrals (second degree)
- **Level 3**: Referrals of referrals of referrals (third degree)

Initial referrer earns commission on trading fees from all three levels.

### Commission Tiers (Based on Cumulative Network Volume)

**Base Commission Rates:**

| Tier | Volume Range | Commission Rate |
|------|--------------|----------------|
| Tier 1 | $0 - $100,000 | 30% |
| Tier 2 | $100,000 - $500,000 | 35% |
| Tier 3 | $500,000 - $2,000,000 | 40% |
| Tier 4 | Over $2,000,000 | 45% |

**What these percentages mean:**
- Commission is paid as a percentage of the 1% trading fee Cooking charges
- Example: User's network trades $100,000 → Cooking earns $1,000 in fees → Referrer gets $300 (30%)

**Performance Bonus:**
- **Threshold**: Personal trading volume exceeds $10,000 in 30-day period
- **Bonus**: Additional 10% on top of base commission rate
- **Maximum Possible**: 55% total (45% tier 4 + 10% bonus)

### Calculation Method

**Volume Aggregation:**
- Sum of all trading volume across all three referral levels
- Calculated over 30-day rolling window
- Measured in USD equivalent
- All trading pairs included (Solana tokens, perpetuals)

**Example Scenario:**
```
Referrer: Alice
├─ Level 1 (5 direct referrals): $60,000 volume
├─ Level 2 (15 indirect referrals): $80,000 volume
└─ Level 3 (40 third-degree referrals): $30,000 volume

Total Network Volume: $170,000
Tier: 2 (35% commission)
Alice's Personal Volume: $15,000 (exceeds $10k threshold)
Performance Bonus: +10%
Total Commission Rate: 45%

Cooking Fees Collected: $170,000 × 1% = $1,700
Alice's Earnings: $1,700 × 45% = $765/month
```

### Technical Implementation

**Custom Referral Codes:**
- Users can create custom memorable codes (e.g., "LucasTrader")
- Auto-generated default code provided
- One-time customization allowed (prevents code gaming)
- Multiple codes per user supported (alias system for rebranding)
- Reserved terms list (no insults, no "cooking" terminology variations)

**Transaction Refactoring:**
- Complete refactor of fee extraction logic
- Profit allocation calculations across 3 levels
- Real-time commission tracking and attribution
- Transparent commission visibility in user dashboard

**Beta Phase Controls:**
- Programmatic cap on referrals per code
- Example: 5-50 referrals per code during closed beta
- Adjustable parameters for growth management

## Rationale

### Business Model Validation

**Competitor Analysis - Pumpfun:**
- Top earner makes $1.5M per month
- $100K from personal trading
- $1.4M from referral commissions
- Demonstrates viability of multilevel model in crypto trading space

**Revenue Potential:**
- Top referrer potential: $200,000+ monthly earnings
- Creates strong incentive for influencers and community builders
- Platform benefits from increased trading volume and user acquisition
- Win-win: Users get valuable service, referrers get meaningful compensation

### Growth Strategy Alignment

**Viral Mechanics:**
- 3-level structure creates compounding network effects
- Users incentivized to not just refer, but help their referrals succeed (and refer others)
- Performance bonus encourages referrers to be active traders (product engagement)
- Custom codes enable personal branding and marketing

**Competitive Positioning:**
- Matches or exceeds competitor commission rates
- More transparent than many existing programs
- Mobile-friendly with custom codes (no URL complexity)
- Clear tier progression motivates growth

### Platform Profitability

**Core Business Logic:**
- Multilevel referrals + trading limiters = core profitability mechanisms
- Even at 55% commission sharing, platform retains 45% of fees
- Increased volume from viral growth more than compensates for revenue sharing
- User acquisition cost near zero (community-driven)

**Sustainable Economics:**
```
Scenario: $10M monthly trading volume from referral program

Platform Fees: $10M × 1% = $100,000
Average Commission Paid: 40% = $40,000
Platform Retention: 60% = $60,000

Without Referral Program:
- Marketing cost for equivalent volume: $50,000+
- Net retention: $50,000 or less
- Slower growth trajectory

With Referral Program:
- Marketing cost: $0 (community-driven)
- Net retention: $60,000
- Accelerated viral growth
- Engaged community of advocates
```

### Mobile Experience Optimization

**Why Custom Codes Matter:**
- App store flow complexity makes URL-based referrals difficult
- Caching issues between store and app
- Custom codes memorable and shareable (social media, word of mouth)
- Supports personal branding (influencers can use their brand names)
- Lucas: "Easier to understand and share. Continues personal brand."

## Consequences

### Positive

**User Acquisition:**
- Viral growth mechanism without marketing spend
- Influencers and community builders financially motivated to promote
- Quality referrals (referrers help their network succeed to maximize earnings)
- Scalable from small users to major influencers

**Revenue Generation:**
- Creates income opportunity for engaged users
- Top referrers can earn life-changing amounts ($200K+/month)
- Transparent, fair compensation structure
- Performance bonus rewards active platform engagement

**Competitive Advantage:**
- Matches best-in-class programs (Pumpfun, etc.)
- Custom codes more user-friendly than competitors
- Clear tier progression and commission visibility
- Multi-platform (web + mobile) support

**Platform Growth:**
- Accelerated user acquisition
- Increased trading volume (more users + performance bonus incentive)
- Engaged community of advocates
- Network effects compound over time

**Technical Benefits:**
- Tree structure enables powerful analytics
- Can track referral chain effectiveness
- A/B testing opportunities by referrer
- Data-driven growth optimization

### Negative

**Implementation Complexity:**
- Complete transaction fee extraction refactor required
- Complex profit allocation across 3 levels
- Real-time calculation overhead on every trade
- Testing complexity (need to verify commission accuracy)
- Martin: "Much more complex than custom codes"

**Revenue Sharing:**
- Platform gives up 30-55% of transaction fees
- Lower margin per transaction
- Must maintain high volume to compensate
- Risk of commission gaming or abuse

**Support Burden:**
- Users will have commission-related questions
- Disputes over commission calculations
- Need clear dashboard and transparency tools
- Customer support training required

**Gaming Risks:**
- Users creating fake referral chains
- Sybil attacks (one person, multiple accounts)
- Wash trading to inflate volumes
- Requires monitoring and fraud detection

**Operational Complexity:**
- Commission payout logistics
- Tax implications (1099 reporting for large earners)
- Terms of service for referral program
- Compliance considerations

### Neutral

- Multiple referral codes per user (adds flexibility but complexity)
- One-time code customization (prevents gaming but limits flexibility)
- Beta caps on referrals per code (growth control vs. user frustration)
- Performance bonus threshold ($10K personal volume) creates engagement requirement

## Alternatives Considered

### Option 1: Simple 1-Level Referral (Status Quo)
**Description:** Continue with direct referrals only, no multi-level structure

**Pros:**
- Much simpler implementation
- Easier to calculate and track
- Lower commission payout
- Minimal technical changes

**Cons:**
- Weak viral mechanics (no compounding growth)
- Lower incentive for top referrers
- Can't compete with platforms offering multi-level
- Limited earning potential reduces influencer interest
- Slower user acquisition

**Why Rejected:** Insufficient to compete with platforms like Pumpfun where top earners make $1.5M/month. Platform needs aggressive growth strategy for market penetration.

### Option 2: 2-Level Structure
**Description:** Limit to just 2 levels (direct + second degree)

**Pros:**
- Simpler than 3-level
- Still creates some viral mechanics
- Lower commission payout obligation
- Easier commission calculation

**Cons:**
- Weaker network effects than 3-level
- Lower earning potential for top referrers
- Less competitive with industry standard (Pumpfun uses multiple levels)
- Marginal simplicity gain doesn't justify reduced growth potential

**Why Rejected:** 3-level is industry standard in crypto trading platforms. Marginal complexity reduction doesn't justify significantly reduced viral growth potential.

### Option 3: Flat Commission Rate (No Tiers)
**Description:** Single commission percentage regardless of volume

**Pros:**
- Simpler to understand
- Easier to calculate
- Predictable for all referrers
- No tier boundary gaming

**Cons:**
- Doesn't reward top performers proportionally
- No progression incentive (can't "level up")
- Less exciting for growth-oriented referrers
- Higher commission rate needed for top referrers, expensive for small referrers
- Lower commission rate affordable for platform, but unmotivating for influencers

**Why Rejected:** Tiered structure creates progression incentive that motivates continued growth. Psychology of "leveling up" important for engagement.

### Option 4: Pure Performance-Based (No Volume Tiers)
**Description:** Commission based only on personal trading activity, not network volume

**Pros:**
- Rewards platform engagement directly
- Harder to game (must actually trade)
- Encourages product usage
- Simpler calculation

**Cons:**
- Doesn't incentivize user acquisition (defeats referral purpose)
- Limits earning potential (personal volume capped by individual capacity)
- No viral mechanics
- Influencers with audiences but lower personal volume excluded

**Why Rejected:** Core purpose is user acquisition. Must reward network building, not just personal trading.

### Option 5: Higher Commission Rates, Fewer Levels
**Description:** 70-80% commission on 1-2 levels

**Pros:**
- Very attractive to potential referrers
- Strong marketing message
- Simpler level structure

**Cons:**
- Platform profitability at risk (gives up too much revenue)
- Unsustainable at scale
- May attract commission hunters vs. quality community builders
- Harder to reduce rates later (bad optics)

**Why Rejected:** 30-55% range provides strong incentive while maintaining platform viability. Competitor analysis shows this range is competitive and sustainable.

## Implementation Notes

### Phased Rollout

**Phase 1: Custom Codes (Week of August 18, 2025)**
- Modal on first login with pre-filled auto-generated code
- User can customize (one-time update)
- Multiple codes support (alias system)
- Reserved terms list enforcement

**Phase 2: Multilevel Commission Structure (Deadline: September 30, 2025)**
- Transaction fee extraction refactor
- 3-level profit allocation logic
- Commission calculation engine
- Real-time attribution tracking
- Dashboard visualization

**Phase 3: Beta Testing (October 2025)**
- Referral caps per code (5-50 slots)
- Closed beta via referral-only access
- Monitor for gaming and abuse
- Validate commission calculations

### Technical Architecture

**Data Model:**
- One-to-many relationship: User → Referral Codes
- Tree structure: Referral chains up to 3 levels deep
- 30-day rolling window for volume calculations
- Real-time commission tracking

**Commission Calculation:**
```
For each transaction:
1. Extract 1% platform fee
2. Identify transaction user
3. Walk up referral tree (3 levels)
4. For each level, calculate user's network volume (30-day)
5. Determine tier (1-4) based on volume
6. Apply commission rate (30-45%)
7. Check performance bonus (personal volume > $10K)
8. Allocate commission to referrer's balance
9. Update running totals
```

**UI Requirements:**
- Referral dashboard showing:
  - Current tier and progress to next tier
  - Network trading volume (30-day)
  - Commission earnings (current period)
  - Referral count by level
  - Performance bonus status
- Commission breakdown on trades (future enhancement)
- Referral code management interface

### Beta Controls

**Referral Caps:**
- Programmatically limit referrals per code
- Adjustable parameters: `max_referrals_per_code`
- Example beta settings: 25-50 slots per code
- Enables controlled growth and quality assurance

### Fraud Prevention

**Monitoring:**
- Flag suspicious referral patterns (rapid account creation)
- Volume anomaly detection (wash trading)
- Geographic distribution analysis
- Transaction pattern analysis

**Mitigation:**
- Commission payout review before distribution
- Minimum holding periods
- KYC requirements for large earners
- Terms of service violations = commission forfeiture

### Reserved Terms

**Prohibited Code Patterns:**
- Insults and offensive language
- Variations of "cooking" (brand protection)
- Impersonation of team members
- Misleading terms (e.g., "official", "admin")

## References

### Meeting Notes
- [Referral Program Crash Course 2025-08-13](../06-meetings/2025-08/2025-08-13-referral-program-crash-course.md) - Comprehensive program design discussion
- [Project Alignment 2025-08-11](../06-meetings/2025-08/2025-08-11-project-alignment.md) - Strategic context

### Requirements Documents
- [Referral Program Multilevel](../04-knowledge-base/business/requirements/referral-program-multilevel.md)
- [Referral Program Invite Codes](../04-knowledge-base/business/requirements/referral-program-invite-codes.md)

### Competitor Analysis
- **Pumpfun**: Top earner $1.5M/month (validated model)
- **Photon**: Referral program details (competitive intelligence)
- **Bullx**: Commission structure analysis

### Related Decisions
- ADR-201: Closed Beta via Referral-Only Access
- ADR-401: Security requirements for wallet operations
- Transaction fee collection architecture

## Revision History
- 2025-08-13: Initial design and commission structure defined
- 2025-08-18: Custom codes implementation (Phase 1)
- 2025-09-30: Multilevel commission logic implementation deadline (Phase 2)
- 2025-10-21: Formal ADR documented from meeting notes
