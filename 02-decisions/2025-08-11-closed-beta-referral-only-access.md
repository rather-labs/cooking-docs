---
title: Closed Beta via Referral-Only Access
type: decision-record
decision-id: ADR-201
date: 2025-08-11
status: accepted
owner: Lucas Cufré
stakeholders: [Zen (Client), Marcos Tacca, Development Team]
tags: [business, beta-launch, referral, user-acquisition, growth-strategy, viral-marketing]
summary: |
  Decision to implement closed beta with referral-only access as the launch strategy,
  creating controlled growth through viral mechanisms while maintaining platform stability
  and building a quality community of engaged users.
related-docs:
  - ../06-meetings/2025-08/2025-08-11-project-alignment.md
---

# ADR-201: Closed Beta via Referral-Only Access

## Context

As the platform approached its beta launch in late 2025, the team needed to decide on the access model for initial users. The decision was critical for balancing three key objectives: controlled rollout for stability testing, organic user growth through viral mechanisms, and building a cult community around the product. The choice of launch strategy would fundamentally shape user acquisition patterns, community dynamics, and early-stage growth trajectory.

### Background

**Timeline Context:**
- Beta launch planned for September 2025 (later moved to October 17, 2025)
- Platform development in final stages with core features complete
- Mobile app pending Apple App Store review (timing unpredictable)
- Team size expanded to 11+ members
- System stability validated at 99.9% uptime with 100+ concurrent users

**Business Context:**
- Katana network exclusivity agreement for gamified launchpad
- Pressure to launch first mover in category
- Need to start light marketing and community building
- Goal to speak with partners using live product
- Budget and timeline constraints after several months of development

**Traditional Launch Models Considered:**
1. **Friends and Family (Private Alpha)**: Invite-only to trusted inner circle
2. **Public Beta**: Open registration with no restrictions
3. **Waitlist Model**: Sign up and wait for invitation based on queue
4. **Closed Beta**: Limited access with manual approval process

**Market Observation:**
The team studied successful Web3 platform launches, particularly noting Bullex Neo's methodology, which dominated their market segment through an aggressive referral-only beta approach. This created scarcity, viral growth, and community engagement simultaneously.

### Problem Statement

The platform needed to:
1. **Control User Growth**: Prevent system overload while validating stability at scale
2. **Generate Organic Buzz**: Create marketing momentum without expensive campaigns
3. **Build Quality Community**: Attract engaged users, not passive registrations
4. **Validate Product-Market Fit**: Gather meaningful feedback from real traders
5. **Enable Partner Conversations**: Demonstrate traction with live user metrics

A traditional Friends and Family approach would be too restrictive, while a public beta risked infrastructure overload and diluted community quality. The team needed a mechanism that provided controlled access while enabling viral growth.

---

## Decision

**Implement closed beta with referral-only access, where the only entry point is through a unique referral code link.**

### Access Mechanism

**Entry Requirements:**
- Users can ONLY access the platform via `cooking.gg/login?referral=CODE`
- Direct login at `cooking.gg/login` without referral code will not work
- Each referral code has capped slots (25-50 slots per code, exact number TBD)
- Initial distribution to close partners, advisors, key stakeholders

**Viral Growth Mechanism:**
- Every referred user who joins receives their own referral code
- New users can immediately generate codes and invite others
- Creates exponential growth potential while maintaining gate control
- Scarcity through slot caps creates urgency and perceived value

**Initial Distribution Strategy:**
- First wave: Client team, advisors, strategic partners
- Second wave: Users referred by first wave
- Third wave: Organic expansion through existing users
- Expected initial user range: 200-2,000 users

**Launch Timeline:**
- Internal target: Wednesday, October 15, 2025
- Official launch: Friday, October 17, 2025
- Rationale: Internal Wednesday target avoids weekend on-call crisis management
- Actual launch: October 17, 2025 (closed beta successfully executed)

### What This Is NOT

**Not Friends and Family:**
- More aggressive than private alpha
- Designed for rapid expansion, not containment
- Open to anyone with a referral code, not just known contacts

**Not Public Beta:**
- No open registration
- Must "hunt out" a referral link to gain access
- Creates exclusivity and perceived value

**Not Traditional Waitlist:**
- No passive queue waiting
- Active referral mechanism required
- Immediate access upon receiving valid code

---

## Rationale

### Primary Drivers

**1. Viral Growth Mechanics**
- **Bullex Neo Precedent**: Successfully dominated market using referral-only approach
- **Network Effects**: Each user becomes acquisition channel for 25-50 more users
- **Exponential Potential**: 10 initial users → 250-500 → 6,250-25,000 (3 levels deep)
- **Cost Efficiency**: Zero marketing spend while creating organic buzz

**2. Controlled Scale Validation**
- **Infrastructure Testing**: Gradual ramp-up validates system stability
- **Predictable Growth**: Slot caps provide growth rate control
- **Rollback Capability**: Can pause by stopping new code generation
- **Performance Monitoring**: Identify bottlenecks before mass adoption

**3. Quality User Acquisition**
- **Self-Selection**: Users motivated to find codes are more engaged
- **Social Proof**: Referral implies endorsement from trusted source
- **Community Seeding**: Early users invested in platform success
- **Feedback Quality**: Engaged users provide better product insights

**4. Marketing and Positioning**
- **Scarcity Creates Value**: Limited access increases perceived platform value
- **FOMO (Fear of Missing Out)**: Slot caps drive urgency to join
- **Organic Buzz**: "How do I get access?" conversations create awareness
- **Partner Conversations**: Live metrics and user activity validate traction

### Strategic Alignment

**Mission Execution:**
From meeting transcript: "Making sure the entire mission is executed" - Zen's focus on timelines for beta and first full launch. Referral-only provides controlled path to validate mission before full launch.

**Not an MVP - Actual Product:**
Client requirement: "Not an MVP. An actual product people can use day-to-day." Referral-only ensures initial users are serious about daily usage, not casual browsers.

**Building Cult Community:**
Explicit goal from Project Alignment meeting: "Start to build cult community." Referral-only creates insider feeling and community identity from day one.

**Light Marketing Start:**
Client goal: "Start very light marketing." Referral mechanism IS the marketing - organic, low-cost, high-impact.

### Risk Mitigation

**Infrastructure Risks:**
- Gradual ramp-up prevents sudden load spikes
- Slot caps provide circuit breaker mechanism
- Wednesday internal target provides buffer before weekend

**User Experience Risks:**
- Controlled rollout allows rapid bug fixing before mass exposure
- Engaged early users more forgiving of rough edges
- Feedback loop faster with smaller, invested community

**Market Risks:**
- Creates buzz without expensive marketing spend
- Scarcity positioning differentiates from competitor launches
- Viral mechanics provide growth insurance if initial traction slow

---

## Alternatives Considered

### 1. Friends and Family (Private Alpha)

**Description:** Invite-only to ~50 trusted contacts, no expansion mechanism.

**Advantages:**
- Maximum control over user base
- High-quality feedback from known contacts
- Low infrastructure risk
- Easy to manage

**Disadvantages:**
- ❌ Too restrictive - doesn't validate market demand
- ❌ No viral growth mechanics
- ❌ Can't demonstrate traction to partners
- ❌ Doesn't build community at scale
- ❌ Requires transition to broader beta later (two launches)

**Why Rejected:** Client explicitly stated "Not Friends and Family" - this was explicitly ruled out as insufficient for beta objectives.

### 2. Public Beta (Open Registration)

**Description:** Open registration at cooking.gg with no restrictions.

**Advantages:**
- Maximum user acquisition potential
- Simplest user experience
- No artificial barriers
- Fast growth

**Disadvantages:**
- ❌ Risk of infrastructure overload
- ❌ No growth control mechanisms
- ❌ Diluted community quality (passive browsers)
- ❌ No scarcity or perceived value creation
- ❌ Difficult to roll back if issues emerge

**Why Rejected:** Too risky for infrastructure validation, doesn't create scarcity value, and provides no control over growth rate.

### 3. Traditional Waitlist Model

**Description:** Users sign up, join queue, receive invitation when capacity allows.

**Advantages:**
- Predictable growth rate
- Good user communication mechanism
- Builds anticipation
- Email capture for marketing

**Disadvantages:**
- ❌ Passive experience (no user involvement in growth)
- ❌ Requires manual invitation management
- ❌ No viral mechanics
- ❌ Slower growth curve
- ❌ Users may lose interest during wait

**Why Rejected:** Lacks viral growth component and creates passive waiting experience instead of active engagement.

### 4. Token-Gated Access (NFT/Wallet Holdings)

**Description:** Require holding specific NFT or token balance to access.

**Advantages:**
- Creates immediate value for token/NFT
- Aligns with Web3 ethos
- Automatic access control
- Revenue generation potential

**Disadvantages:**
- ❌ Creates financial barrier to entry
- ❌ Limits user base to existing token holders
- ❌ Adds complexity to onboarding
- ❌ May not align with "trading for everyone" vision
- ❌ Requires token/NFT infrastructure

**Why Rejected:** Too restrictive and adds unnecessary complexity for beta phase.

### 5. Hybrid: Open Beta with Referral Bonuses

**Description:** Open registration but incentivize referrals with rewards.

**Advantages:**
- No artificial access barriers
- Growth incentives preserved
- Flexible approach

**Disadvantages:**
- ❌ Loses scarcity value
- ❌ No growth rate control
- ❌ Infrastructure risk remains
- ❌ Incentives may attract low-quality users (gamification abuse)

**Why Rejected:** Loses key benefits of scarcity and controlled growth while adding incentive management complexity.

---

## Consequences

### Positive Outcomes

**Growth and Acquisition:**
- ✅ Viral growth mechanism built into access model
- ✅ Zero marketing spend while creating organic buzz
- ✅ Each user becomes acquisition channel (25-50x multiplier)
- ✅ Exponential growth potential with control mechanisms

**User Quality:**
- ✅ Self-selected engaged users (motivated to find access)
- ✅ Social proof from referral source increases commitment
- ✅ Early adopters invested in platform success
- ✅ Better feedback quality from serious users

**Infrastructure and Stability:**
- ✅ Controlled rollout validates system under increasing load
- ✅ Slot caps provide growth rate control
- ✅ Time to fix critical bugs before mass exposure
- ✅ Predictable resource planning

**Marketing and Positioning:**
- ✅ Scarcity creates perceived value and desirability
- ✅ "How do I get in?" conversations create awareness
- ✅ FOMO drives urgency and engagement
- ✅ Success story: Bullex Neo model validated in market

**Community Building:**
- ✅ Insider feeling creates community identity
- ✅ Early users become platform advocates
- ✅ Shared "exclusive access" experience bonds users
- ✅ Foundation for cult community goal

**Business Validation:**
- ✅ Live metrics demonstrate traction to partners
- ✅ Real user activity validates product-market fit
- ✅ Feedback loop informs V1 feature prioritization
- ✅ Partner conversations backed by real usage data

**Actual Results (Post-Launch):**
- ✅ October 17, 2025 closed beta launch successful
- ✅ Initial users: 5 on Oct 20, ramping to 30-40 on Oct 27
- ✅ 99.9% uptime maintained
- ✅ Transaction completion time: 3s (down from 5-6s)
- ✅ ClickHouse delivering 15x query performance improvement
- ✅ Referral-only access model validated and operational

### Negative Consequences

**User Experience:**
- ⚠️ Friction in access process ("hunt out" a link)
- ⚠️ Users without network connections excluded
- ⚠️ Potential frustration if slots filled when user tries to join
- **Mitigation:** Clear communication about access model, regular slot availability

**Growth Constraints:**
- ⚠️ Slot caps may limit growth below potential
- ⚠️ Requires manual code generation and distribution initially
- ⚠️ Growth depends on user referral behavior (not guaranteed)
- **Mitigation:** Adjustable slot caps, automated code generation for users, monitoring growth metrics

**Technical Complexity:**
- ⚠️ Referral code validation logic required
- ⚠️ Slot tracking and cap enforcement needed
- ⚠️ URL parameter handling for referral codes
- ⚠️ Analytics to track referral chains
- **Mitigation:** Implemented in authentication flow, minimal added complexity vs waitlist

**Equity Concerns:**
- ⚠️ "Access by who you know" may exclude talented users
- ⚠️ Network effects favor well-connected individuals
- ⚠️ Could create exclusive club perception
- **Mitigation:** Viral nature means network expands rapidly, anyone eventually gains access

**Support and Operations:**
- ⚠️ Users requesting access codes (support load)
- ⚠️ Abuse prevention (code selling, multiple accounts)
- ⚠️ Monitoring referral quality and patterns
- **Mitigation:** Clear communication, abuse detection systems, community guidelines

### Trade-offs Accepted

**Control vs. Accessibility:**
- Chose controlled growth over open accessibility
- Rationale: Infrastructure stability and community quality paramount in beta

**Simplicity vs. Virality:**
- Added referral code complexity over simple registration
- Rationale: Viral growth mechanism worth the implementation effort

**Immediate Size vs. Quality:**
- Chose smaller, engaged community over larger, passive user base
- Rationale: Quality feedback more valuable in beta than quantity

**Inclusivity vs. Scarcity:**
- Chose scarcity value over immediate full inclusivity
- Rationale: Scarcity creates positioning value; full access comes post-beta

---

## Implementation

### Technical Requirements

**Authentication Flow:**
```
1. User visits cooking.gg/login?referral=UNIQUE_CODE
2. System validates referral code exists and has available slots
3. If valid: User proceeds to Auth0 social login
4. Upon successful authentication, user account linked to referral code
5. User assigned their own referral code for distribution
6. Referral code slot count decremented
```

**Database Schema:**
- Referral codes table: code, slots_total, slots_used, created_by, created_at
- User-referral mapping: user_id, referral_code_used, referral_code_owned
- Analytics: referral chain tracking, conversion metrics

**URL Structure:**
- Entry point: `cooking.gg/login?referral=CODE`
- Validation: Redirect to error page if no referral parameter or invalid code
- Success: Proceed to Auth0 login flow

**Slot Management:**
- Initial codes: 25-50 slots (configurable)
- Auto-generation: User receives code upon successful signup
- Admin panel: Create codes, adjust slot counts, monitor usage

### Launch Sequence

**Phase 1: Initial Distribution (Day 0)**
- Generate 10-20 referral codes for client team, advisors, partners
- Document codes and assigned owners
- Communications to code holders explaining beta access model

**Phase 2: First Wave (Days 1-3)**
- Initial users join via distributed codes
- Expected: 200-500 users (10 codes × 25-50 slots)
- Monitor: System performance, user feedback, referral activation rate

**Phase 3: Viral Expansion (Week 1)**
- First wave users generate and distribute codes
- Expected: 5,000-25,000 potential users (200-500 × 25-50 slots)
- Monitor: Growth rate, infrastructure scaling, community engagement

**Phase 4: Steady State (Weeks 2-4)**
- Organic expansion through user referrals
- Adjust slot counts based on system capacity
- Gather feedback for V1 feature prioritization

**Actual Launch (October 17, 2025):**
- Closed beta launched successfully
- Initial controlled rollout: 5 users Oct 20, 30-40 users Oct 27
- Infrastructure validated at 99.9% uptime
- Transaction speed optimized to 3s completion time

### Monitoring and Metrics

**Growth Metrics:**
- Daily active users (DAU)
- Referral code usage rate
- Average slots used per code
- Referral chain depth (degrees of separation from origin)
- Growth rate (users per day)

**Quality Metrics:**
- User engagement (session length, frequency)
- Feature adoption rates
- Feedback submission rates
- Community participation (if forums/Discord)

**Infrastructure Metrics:**
- System performance under load
- Error rates
- Response times
- Resource utilization

**Business Metrics:**
- Partner conversation outcomes
- Investor interest indicators
- Press mentions and social media buzz
- Waitlist growth (for post-beta public launch)

### Risk Management

**Abuse Prevention:**
- Rate limiting on code validation attempts
- Detection of account farming patterns
- Manual review of suspicious referral chains
- Community guidelines enforcement

**Capacity Management:**
- Real-time monitoring of infrastructure load
- Auto-scaling triggers
- Emergency slot cap reduction capability
- Pause new code generation if needed

**Communication Strategy:**
- Clear messaging about beta nature and potential issues
- Regular updates on system status
- Transparent roadmap sharing
- Active community engagement

---

## Related Decisions

- **[ADR-200: Multilevel Referral Program Structure](ADR-200-multilevel-referral-program.md)** - 3-tier commission structure for viral growth (related growth mechanism for post-beta)
- **[ADR-203: September Beta Launch Timeline](2025-08-11-september-beta-launch-timeline.md)** - Beta launch timing and phasing (directly implements this access model)
- **[ADR-102: Auth0 for Social Authentication](ADR-102-auth0-social-authentication.md)** - Authentication provider for referral-code-gated access

---

## References

### Source Meetings
- **[Project Alignment Meeting (2025-08-11)](../06-meetings/2025-08/2025-08-11-project-alignment.md)**
  - Lines 122-130: Launch strategy discussion
  - Lines 186-191: Beta access model details (referral links, capped slots)
  - Lines 156-164: Beta requirements (actual product, feedback gathering, community building)

- **[Daily Standup (2025-10-13)](../06-meetings/2025-10/2025-10-13-daily-standup.md)**
  - Lines 122-130: Explicit "Not Friends and Family" - referral-only open beta
  - Lines 124-129: Access mechanism, viral mechanism, Bullex Neo precedent
  - Lines 298-305: Launch timing and access model summary

### Key Quotes

**From Project Alignment Meeting (Zen):**
> "Beta access only through referral links. Each referral link limited to ~25-50 slots (exact numbers TBD). Must 'hunt out' for a link to get access."

**From Daily Standup (Lucas):**
> "Not Friends and Family - open beta approach. Only via referral code link (cooking.com/login won't work without code). Replicating Bullex Neo methodology (dominated market via referral-only beta)."

### Market Research
- **Bullex Neo Case Study**: Successfully dominated market segment using referral-only beta launch
- **Web3 Platform Launches**: Pattern of scarcity-based access creating higher perceived value and community engagement

---

## Notes

### Strategic Context

This decision was made during a critical period in the project timeline, following the Hyperliquid integration challenges that strained the client relationship. The referral-only beta represented a carefully balanced approach to:

1. **Rebuild Trust**: Demonstrate controlled, thoughtful launch vs. rushing to public beta
2. **Validate Infrastructure**: Prove system stability after architectural changes
3. **Create Momentum**: Generate organic marketing buzz without additional budget
4. **Enable Partnership Conversations**: Show live traction metrics to potential partners

### Client Relationship Impact

The Project Alignment meeting (August 11) was tense, with Zen expressing disappointment about the Hyperliquid geolocation issue. The agreement on referral-only beta was part of rebuilding trust through:
- Weekly sprint calls for better communication
- Clear, concrete timelines and deliverables
- Thoughtful launch strategy balancing risk and growth

### Product Philosophy Tension

This decision exists in tension with the stated "for everyone" vision. The October 13 standup notes Lucas questioning: "Need to understand target trader - memecoins require knowledge, contradicts 'for everyone' vision."

The referral-only approach implicitly acknowledges the platform targets experienced traders, not mass market, at least initially. This represents a pragmatic business decision that may inform future product strategy.

### Implementation Learnings

Key considerations for future launches:
1. Viral mechanics can replace paid acquisition in Web3 space
2. Scarcity creates value and buzz even for free products
3. Controlled rollout provides invaluable infrastructure validation
4. Community quality matters more than quantity in beta
5. Access model itself can be marketing strategy

### Post-Launch Validation

The October 17, 2025 closed beta launch successfully validated this decision:
- Controlled rollout allowed infrastructure testing (99.9% uptime achieved)
- Initial user cohorts (5 → 30-40) provided manageable feedback volume
- System performance optimizations validated under real load (3s transactions)
- Referral-only access model proved operationally feasible
- Foundation established for subsequent growth phases

---

**Decision Status:** ✅ Accepted and Implemented
**Implementation Date:** October 17, 2025
**Review Date:** Post-Beta (Q1 2026)
**Success Criteria:** 200-2,000 users in first month, 99%+ uptime, positive user feedback, partner engagement

---

*This ADR documents a critical business decision that shaped the platform's go-to-market strategy and community building approach.*
