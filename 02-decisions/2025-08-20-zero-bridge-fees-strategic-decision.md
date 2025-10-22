---
title: Zero Bridge Fees Strategic Decision
type: decision-record
decision-id: ADR-202
date: 2025-08-20
status: accepted
owner: Lucas Cufré
stakeholders: [Martin Aranda, Client Team, Product Team]
tags: [business, pricing, bridge-fees, competitiveness, revenue-model, user-acquisition]
summary: |
  Strategic decision to charge zero fees on cross-chain bridge operations for Hyperliquid
  perpetuals trading, prioritizing user acquisition and competitive positioning over
  short-term revenue generation during the beta launch phase.
related-docs:
  - ../04-knowledge-base/business/requirements/hyperliquid-perpetuals-integration.md
---

# ADR-202: Zero Bridge Fees Strategic Decision

## Context

As Cooking.gg prepared to launch Hyperliquid perpetuals trading integration, the team needed to determine the fee structure for cross-chain bridge operations. Specifically, users would need to bridge assets from Solana to USDC on Arbitrum (Hyperliquid's native chain) to access perpetuals trading. The platform had the technical capability to charge fees on these bridge operations both inbound (Solana → USDC) and outbound (USDC → Solana), with support for both percentage-based and flat fees in either fast mode (higher fees) or slow mode (lower fees, higher profit margin).

### Background

**Technical Context:**
- Hyperliquid perpetuals operate on Arbitrum network using USDC
- Users holding Solana-based assets need cross-chain bridge to access perpetuals
- Platform architecture requires routing through Cooking's bridge to track transactions
- Alternative: Direct USDC deposits bypass Cooking's system (no tracking or fees)

**Market Context:**
- Multiple competitors offering perpetuals trading with various fee structures
- Established platforms (Axiom, Phantom) offer perpetuals but see low adoption
- User behavior: Existing Hyperliquid users unlikely to migrate to new platform
- Bridge fees represent potential recurring revenue stream from all perpetuals users

**Product Strategy Context:**
- September 2025 beta launch approaching (5 weeks timeline)
- Team under pressure to deliver competitive, polished product
- Client concerns about platform competitiveness in crowded market
- Focus on user acquisition over immediate revenue generation

**Revenue Considerations:**
- Bridge fees represent "controllable" revenue (unlike Hyperliquid's base trading fees)
- Partner commission program would apply to bridge fees (reducing net revenue)
- Bidirectional fee opportunity (both deposit and withdrawal)
- Trade-off between revenue per user vs. number of users acquired

### Problem Statement

The platform needed to decide whether to:
1. **Charge bridge fees** to generate revenue from perpetuals users
2. **Waive bridge fees** to maximize competitiveness and user acquisition
3. **Implement tiered fees** based on user type, volume, or partnership status

Key considerations:
- **Revenue Impact**: How much revenue would bridge fees generate?
- **Competitive Positioning**: How do competitors price bridge operations?
- **User Acquisition**: Would fees create barrier to perpetuals adoption?
- **Market Reality**: Evidence suggested perpetuals see low adoption even without fees
- **Strategic Priority**: Should focus be on revenue or growth in beta phase?

---

## Decision

**Implement zero bridge fees for all bridge operations (both Solana → USDC and USDC → Solana) to maintain maximum competitiveness with other services.**

### Scope

**What is FREE:**
- Bridge operations from Solana to USDC (Arbitrum) for Hyperliquid access
- Bridge operations from USDC (Arbitrum) back to Solana
- No commission on conversions
- Both fast mode and slow mode bridge operations

**What is Still Charged:**
- Trading fees on Hyperliquid perpetuals (per Hyperliquid's base fee structure)
- Builder code surcharges (subject to partner commission program)
- Spot trading fees on Solana (separate from perpetuals)
- Other platform operations unrelated to bridge

**Technical Implementation:**
- Bridge fee configuration set to 0% for both directions
- No flat fees applied regardless of transaction size
- Fast mode and slow mode differentiation based on speed, not cost to user
- Direct USDC deposits enabled (technical simplification, no fee capture anyway)

---

## Rationale

### Primary Drivers

**1. Competitive Necessity**

The decision was explicitly framed as "strategy to be competitive with other services." In a crowded perpetuals trading market with established players, any friction in the onboarding process could prevent user acquisition.

**Competitive Landscape:**
- Axiom and Phantom already offer perpetuals with minimal fees
- Evidence: "Nobody" uses perpetuals on these platforms despite availability
- Low adoption suggests market is sensitive to friction, not just fees
- Zero fees remove one potential barrier to adoption

**Quote from meeting:** "No fees for bridge operations (in or out)... Strategy to be competitive with other services."

**2. Market Adoption Reality**

Discussion revealed skepticism about perpetuals adoption even without fees:

**Naji's Concern (Client Team):**
> "How many users will actually use Cooking for Hyperliquid trading? Users already on Hyperliquid likely won't switch. Evidence: Axiom and Phantom support perps, but low usage."

**Market Observation:**
> "Community feedback: Can trade perps on Axiom/Phantom, but 'nobody does'"

**Strategic Implication:**
If perpetuals face adoption challenges regardless of fees, charging bridge fees would:
- Further reduce already-low adoption likelihood
- Generate minimal revenue (low volume × fee rate)
- Create negative perception ("nickel and diming users")
- Fail to differentiate from competitors

Zero fees at least remove one adoption barrier, even if other challenges remain.

**3. Beta Phase Priorities**

The decision occurred during beta preparation (5 weeks to launch), a phase focused on:
- User acquisition and growth
- Product validation and feedback gathering
- Building community and momentum
- Establishing market presence

**Beta Phase Characteristics:**
- Revenue generation secondary to user acquisition
- Need to demonstrate traction to investors and partners
- Building network effects and community
- Proving product-market fit before optimizing monetization

Charging fees during beta would prioritize short-term revenue over long-term growth, inconsistent with typical SaaS/Web3 beta strategies.

**4. Revenue Model Complexity**

Bridge fees introduce revenue but also complexity:

**Partner Commission Impact:**
- Bridge fees subject to partner commission program
- Net revenue significantly reduced by partner payouts
- Added accounting and tracking complexity
- Potential disputes over fee attribution

**User Experience Impact:**
- Fee disclosure requirements
- User confusion about multiple fee types (gas, bridge, trading, priority)
- Comparison shopping complexity (users calculating total cost across platforms)
- Support load explaining fee structure

**Calculation:**
If bridge fees generate $X gross revenue but:
- Partner commissions reduce to $X * 0.55-0.70 (30-45% commission tiers)
- Support costs increase
- User acquisition decreases by Y%

The net impact may be negative compared to zero fees with higher acquisition.

**5. Simplified User Mental Model**

From discussion about fee complexity (transfer fee debate):

**Naji's Philosophy:**
> "What's a priority fee to someone who doesn't understand blockchains? Makes product less simple for target users."

This philosophy extends to bridge fees:
- Users already confused by: gas fees, trading fees, blockchain fees, network fees
- Adding bridge fees creates another concept to explain
- Competitors with zero bridge fees have simpler messaging: "Free to move your assets"
- Simplicity competitive advantage in crypto UX

**6. Technical Architecture Alignment**

Discussion revealed that **direct USDC deposits** were technically feasible:

**From meeting:**
> "Alternative: Enable direct USDC deposit (no fee for Cooking). Feasibility: Simple to implement if desired."

**Current architecture:**
> "Must bridge through Solana to USDC. Rationale: Ensures Cooking captures bridge fee."

**Implication:**
If charging fees, platform must force users through bridge route (adding friction).
With zero fees, can enable direct deposits (removing friction).

Zero fees align with technical simplification and better user experience.

---

## Alternatives Considered

### 1. Percentage-Based Bridge Fees (0.1-0.5%)

**Description:** Charge small percentage fee on bridge amount in both directions.

**Example Structure:**
- 0.1% on Solana → USDC bridging
- 0.1% on USDC → Solana bridging
- Applied to bridge amount (e.g., $10 on $10,000 bridge)

**Advantages:**
- Generates recurring revenue from perpetuals users
- Scales with transaction volume
- Industry-standard approach
- Relatively small impact per transaction

**Disadvantages:**
- ❌ Creates competitive disadvantage vs. free competitors
- ❌ Partner commissions reduce net revenue to 0.055-0.07% (55-70% after 30-45% commission)
- ❌ Low perpetuals adoption predicted regardless of fees
- ❌ Added complexity in user experience
- ❌ Psychological barrier even if small amount
- ❌ Support burden explaining fee structure

**Why Rejected:** Revenue potential (0.055-0.07% net after partner commissions) insufficient to justify competitive disadvantage and user friction.

### 2. Tiered Bridge Fees by User Segment

**Description:** Free for new users, charged for high-volume traders, or free for partner referrals.

**Example Structure:**
- First $10,000 bridged: Free
- $10,000-$100,000: 0.1%
- $100,000+: 0.05%
- Partner referrals: Always free

**Advantages:**
- Captures revenue from high-value users
- No barrier for small users or trial
- Incentivizes partner program participation
- Flexible, data-driven optimization potential

**Disadvantages:**
- ❌ Complex to explain and communicate
- ❌ Requires user tier tracking and enforcement
- ❌ Creates perception of "bait and switch" when fees kick in
- ❌ Implementation complexity (tier tracking, partner verification)
- ❌ Support burden managing tier questions and disputes
- ❌ Still creates competitive disadvantage for high-value users

**Why Rejected:** Complexity outweighs revenue potential, especially given low predicted adoption and competitive positioning needs.

### 3. Fast Mode Fees, Slow Mode Free

**Description:** Charge fees for fast bridge (minutes), free for slow bridge (hours).

**Example Structure:**
- Fast mode (5-10 minutes): 0.2% fee
- Slow mode (2-4 hours): Free
- User selects preferred mode based on urgency

**Advantages:**
- Revenue from users who value speed
- Free option maintains competitive positioning
- Aligns fee with value delivered (speed)
- Common pattern in bridge services

**Disadvantages:**
- ❌ Perpetuals traders likely need fast access (urgency-sensitive use case)
- ❌ Creates two-tier user experience
- ❌ Implementation complexity (two bridge paths)
- ❌ Support burden explaining difference
- ❌ May not generate significant revenue if most choose slow mode

**Why Rejected:** Perpetuals trading is time-sensitive; forcing users to wait hours undermines use case. Fast mode fees would affect most users, returning to competitive disadvantage problem.

### 4. Flat Fee Per Bridge Transaction

**Description:** Fixed fee (e.g., $1-5) per bridge operation regardless of amount.

**Example Structure:**
- Solana → USDC: $2 flat fee
- USDC → Solana: $2 flat fee
- Same fee regardless of $100 or $100,000 bridged

**Advantages:**
- Simple to understand and communicate
- Predictable revenue per transaction
- Favors high-value bridges (percentage decreases with amount)
- Easier accounting than percentage-based

**Disadvantages:**
- ❌ Disproportionately impacts small users (high percentage on small amounts)
- ❌ Creates barrier to trial/experimentation
- ❌ Inconsistent with percentage-based trading fees (user confusion)
- ❌ Competitive disadvantage vs. free competitors
- ❌ May discourage small users from trying perpetuals

**Why Rejected:** Creates barrier for small users and trial behavior, undermines beta-phase goal of maximizing user acquisition.

### 5. Subscription Model (Premium Users Bridge Free)

**Description:** Free bridge operations for premium/pro subscribers, fee for free-tier users.

**Example Structure:**
- Free tier: 0.2% bridge fee
- Premium ($10/month): Free bridge
- Pro ($50/month): Free bridge + other benefits

**Advantages:**
- Creates subscription revenue stream
- Incentivizes tier upgrades
- Aligns with SaaS revenue models
- Rewards engaged users

**Disadvantages:**
- ❌ Requires building subscription infrastructure
- ❌ Adds significant complexity to beta launch
- ❌ Free tier still has competitive disadvantage
- ❌ Subscription fees may exceed bridge fee cost (user calculation)
- ❌ Not aligned with Web3 "pay per use" culture
- ❌ Timeline constraint: 5 weeks to launch insufficient for subscription system

**Why Rejected:** Too complex for beta phase, requires infrastructure not yet built, and not aligned with immediate competitive needs.

---

## Consequences

### Positive Outcomes

**Competitive Positioning:**
- ✅ Maximum competitiveness vs. other perpetuals platforms
- ✅ Removes friction point in user acquisition funnel
- ✅ Simple messaging: "No bridge fees" clear value proposition
- ✅ Differentiation if competitors charge fees

**User Experience:**
- ✅ Simplified fee structure (fewer fee types to explain)
- ✅ Lower cognitive load for crypto newcomers
- ✅ Faster onboarding (no fee calculation or disclosure)
- ✅ Reduced support burden (one less fee type to explain)

**Technical Simplification:**
- ✅ Enables direct USDC deposits (no forced routing through bridge)
- ✅ Simpler transaction flow and architecture
- ✅ Less complex fee calculation and tracking
- ✅ Reduced partner commission accounting complexity

**Beta Phase Alignment:**
- ✅ Focuses on user acquisition over revenue
- ✅ Removes barrier to trial and experimentation
- ✅ Demonstrates platform generosity and user-centricity
- ✅ Aligns with network-effect growth strategy

**Strategic Optionality:**
- ✅ Can introduce fees later if adoption justifies
- ✅ Baseline for measuring adoption without fee variable
- ✅ Goodwill with early adopters
- ✅ Data collection on usage patterns without fee friction

### Negative Consequences

**Revenue Impact:**
- ⚠️ Zero direct revenue from bridge operations
- ⚠️ Foregone revenue opportunity (even if small)
- ⚠️ Missed chance to validate fee tolerance
- ⚠️ May never recapture opportunity if users expect free forever

**Mitigation:**
- Trading fees on Hyperliquid still generate revenue
- Builder code surcharges provide alternative revenue
- Can introduce fees in future if adoption validates demand
- Focus on volume growth over per-transaction revenue

**Competitive Dynamics:**
- ⚠️ If competitors charge fees, may create expectation of free forever
- ⚠️ Difficult to introduce fees later without user backlash
- ⚠️ May be perceived as "loss leader" or unsustainable

**Mitigation:**
- Communicate as "beta promotion" or "limited time" if needed
- Build loyalty and switching costs through product quality
- Introduce fees gradually if/when market leadership established

**Cost Structure:**
- ⚠️ Platform still incurs costs for bridge operations (infrastructure, gas fees on destination chain)
- ⚠️ No revenue to offset bridge infrastructure costs
- ⚠️ Negative margin on bridge operations (cost > $0, revenue = $0)

**Mitigation:**
- Bridge costs relatively low compared to overall infrastructure
- Trading volume fees offset infrastructure costs holistically
- User lifetime value exceeds bridge cost if perpetuals adopted

**Market Validation:**
- ⚠️ Zero fees means can't validate fee tolerance through beta
- ⚠️ No data on price elasticity of bridge demand
- ⚠️ Unknown whether fees would have materially impacted adoption

**Mitigation:**
- Can A/B test fees post-beta if needed
- Market research and competitor analysis provide proxy data
- Low predicted adoption suggests fees likely to harm, not help

### Trade-offs Accepted

**Revenue vs. Growth:**
- Chose growth and user acquisition over immediate revenue
- Rationale: Beta phase priorities, network effects value, competitive positioning

**Simplicity vs. Revenue Optimization:**
- Chose simple "zero fees" over complex tiered structures
- Rationale: User experience, support burden, implementation timeline

**Short-term vs. Long-term:**
- Sacrificed short-term bridge revenue for long-term user base growth
- Rationale: Lifetime value of user exceeds bridge fee revenue

**Competitive Positioning vs. Revenue Diversification:**
- Chose competitive parity over revenue stream diversification
- Rationale: Market evidence suggests adoption challenge, not fee optimization opportunity

---

## Implementation

### Technical Configuration

**Bridge Fee Settings:**
```
Solana → USDC (Arbitrum):
  - Percentage fee: 0%
  - Flat fee: $0
  - Fast mode: 0% fee
  - Slow mode: 0% fee

USDC (Arbitrum) → Solana:
  - Percentage fee: 0%
  - Flat fee: $0
  - Fast mode: 0% fee
  - Slow mode: 0% fee
```

**Direct Deposit Configuration:**
- Enable direct USDC deposits to Hyperliquid
- No forced routing through Solana bridge
- Simplified transaction flow for users with existing USDC

**Partner Commission Handling:**
- Bridge operations excluded from partner commission calculations (no fees = no commissions)
- Simplified accounting and reporting
- Trading fees on Hyperliquid still subject to partner program

### User Communication

**Messaging Framework:**
- "Zero bridge fees" highlighted in marketing materials
- Emphasize cost savings vs. competitors (if applicable)
- Transparent about what fees DO exist (trading fees, gas fees)
- Clear explanation of bridge process and timing

**UI/UX Updates:**
- Bridge fee display: "$0" or "Free" (not hidden)
- Gas fee disclosure still required (network costs distinct from platform fees)
- Fast mode vs. slow mode based on speed, not cost difference
- Transaction preview shows total cost (gas only, no platform fees)

### Monitoring and Metrics

**Adoption Metrics:**
- Bridge transaction volume (measure adoption without fee variable)
- User acquisition through perpetuals offering
- Conversion rate from spot traders to perpetuals traders
- Retention and engagement of perpetuals users

**Cost Metrics:**
- Bridge infrastructure costs per transaction
- Total bridge operating costs (monthly)
- Cost per user acquired through perpetuals offering
- Customer acquisition cost (CAC) comparison to other channels

**Competitive Benchmarking:**
- Competitor fee structures (track changes)
- Market share in perpetuals trading (if measurable)
- User feedback on fee structure vs. competitors

**Future Decision Support:**
- Baseline data for fee introduction decision (if needed)
- Volume elasticity estimates
- User segment analysis (who bridges, how much, how often)
- Lifetime value by acquisition channel

---

## Related Decisions

- **[ADR-200: Multilevel Referral Program Structure](ADR-200-multilevel-referral-program.md)** - Partner commission program that would have applied to bridge fees (now not applicable)
- **[ADR-201: Closed Beta via Referral-Only Access](2025-08-11-closed-beta-referral-only-access.md)** - Beta launch strategy prioritizing user acquisition over revenue (aligns with zero fees decision)

---

## References

### Source Meetings

**[Daily Standup (2025-08-20)](../06-meetings/2025-08/2025-08-20-daily-standup.md)**
- Lines 109-113: Zero Bridge Fees Decision
  > "No fees for bridge operations (in or out). No commission for Solana to USDC conversion on Arbitrum. Strategy to be competitive with other services. Plan to include builder codes logic in Perpetuals."

**[Cooking Demo (2025-08-15)](../06-meetings/2025-08/2025-08-15-cooking-demo.md)**
- Lines 139-147: Direct Deposit Discussion and Rationale
  > "Current: Must bridge through Solana to USDC. Rationale: Ensures Cooking captures bridge fee. Alternative: Enable direct USDC deposit (no fee for Cooking). Feasibility: Simple to implement if desired."

  > "Naji's Concern: How many users will actually use Cooking for Hyperliquid trading? Users already on Hyperliquid likely won't switch. Evidence: Axiom and Phantom support perps, but low usage."

- Lines 148-151: Market Observation
  > "Market Observation: Community feedback: Can trade perps on Axiom/Phantom, but 'nobody does'. Question whether perpetuals will see significant adoption."

**[August 2025 Summary](../06-meetings/2025-08/2025-08-summary.md)**
- Lines 64-67: Strategic Priority
  > "Feature Prioritization: 1. **Zero Bridge Fees**: Strategic decision for competitiveness"

### Key Quotes

**On Competitive Strategy:**
> "Strategy to be competitive with other services" - Daily Standup 2025-08-20

**On Market Reality:**
> "How many users will actually use Cooking for Hyperliquid trading? Users already on Hyperliquid likely won't switch." - Naji, Cooking Demo 2025-08-15

**On User Adoption:**
> "Community feedback: Can trade perps on Axiom/Phantom, but 'nobody does'" - Market observation, Cooking Demo 2025-08-15

### Business Context

This decision was made during a critical period:
- 5 weeks to beta launch deadline
- Team expansion to 11+ members
- Client pressure for competitive positioning
- Focus on user acquisition over monetization
- Market skepticism about perpetuals adoption

---

## Notes

### Strategic Context

This decision represents a clear prioritization of **growth over revenue** during the beta phase. It aligns with standard SaaS/Web3 playbook of removing friction during user acquisition, then optimizing monetization once product-market fit is validated.

The decision was particularly informed by market intelligence suggesting perpetuals adoption would be challenging regardless of fees - the "Axiom/Phantom effect" where availability doesn't guarantee usage.

### Product Philosophy

Zero bridge fees reflects a broader product philosophy emerging across multiple decisions:
1. **Simplicity over Optimization:** Simple fee structures over complex tiered models
2. **User-Centricity:** Remove friction even at cost to revenue
3. **Competitive Parity:** Match or beat competitors on key metrics (fees, speed, features)
4. **Growth Focus:** Beta phase prioritizes acquisition over monetization

This philosophy is consistent with:
- Referral-only beta access (scarcity for growth, not revenue)
- Debate about removing priority fees from transfers (simplicity over control)
- Address book renaming (newcomer-friendly terminology)

### Financial Implications

**Revenue Foregone (Hypothetical):**
If perpetuals saw moderate adoption:
- 1,000 users × $5,000 average bridge amount × 2 bridges (in + out) = $10M bridge volume
- 0.1% fee = $10,000 gross revenue
- 30-45% partner commissions = $5,500-$7,000 net revenue
- **Annual projection: $22,000-$28,000** (assuming quarterly bridge cycles)

**Cost-Benefit Analysis:**
If losing even **1 user** due to bridge fees, and that user would have:
- Generated $500/year in trading fees
- Referred 2 users (viral coefficient 2.0)
- 3-year lifetime value

Lost value: $500 × 3 years × (1 + 2 + 4) = $10,500 per lost user

**Break-even:** Bridge fees would need to NOT cost any user acquisition to be financially optimal.

Given market skepticism about adoption, **risk of losing users >> revenue from fees**.

### Future Considerations

**Fee Introduction Path:**
If perpetuals adoption validates demand, potential future fee structure:
1. **Grandfather early users:** Maintain zero fees for beta participants
2. **Introduce fees gradually:** Start at 0.05%, increase if no adoption impact
3. **Tier-based approach:** Free for low volume, fees for high volume
4. **Subscription alternative:** Premium tier with free bridge + other benefits

**Communication Strategy:**
- Present as "beta promotion" initially
- Set expectations that fees may be introduced post-beta
- Or: Commit to zero fees permanently as competitive differentiator

**Market Dynamics:**
If competitors maintain zero fees, Cooking.gg may be locked into zero fees to maintain parity. This decision may be irreversible from market positioning perspective.

### Lessons Learned

**Key Takeaways:**
1. **Revenue optimization premature in beta:** Growth > revenue during validation phase
2. **Market intelligence matters:** Axiom/Phantom data prevented over-optimizing for revenue
3. **Simplicity is competitive advantage:** Fee complexity creates friction
4. **Partner commissions reduce appeal of fees:** Net revenue after commissions often insufficient to justify user friction

**Application to Future Decisions:**
- Default to simplicity and user-centricity during growth phases
- Validate adoption before optimizing monetization
- Consider net revenue after partner commissions, not gross
- Market intelligence (competitive behavior, user feedback) should inform pricing

---

**Decision Status:** ✅ Accepted and Implemented
**Implementation Date:** August 2025
**Review Date:** Post-Beta (Q4 2025)
**Success Criteria:** Perpetuals adoption rate, user feedback on fee structure, competitive positioning maintained

---

*This ADR documents a strategic pricing decision prioritizing competitive positioning and user acquisition over immediate revenue generation during the beta launch phase.*
