---
title: Bug Alignment - 2025-09-15
type: meeting-note
date: 2025-09-15
---# Bug Alignment Meeting

**Date:** September 15, 2025
**Time:** 15:59 GMT-03:00
**Duration:** ~43 minutes
**Meeting Type:** Bug Alignment Session
**Language:** Spanish (translated to English)

## Attendees
- **Lucas Cufré** - Project Lead
- **Javier Grajales** - QA Lead
- **Martín Aranda** - Tech Lead
- **Eduardo Yuschuk** - Backend Developer / Indexer Lead
- **Esteban Restrepo** - Backend Developer
- **Federico Caffaro** - Backend Developer (Perpetuals)
- **Germán Derbes Catoni** - Frontend Developer
- **Luis Rivera** - Frontend Developer (not present)
- **Byron Chavarria** - Mobile Developer
- **Santiago Giménez** - Design Lead
- **Marko Jauregui** - Team Member

## Meeting Context

Critical bug alignment session held three weeks before the October 3rd closed beta launch. Clients were concerned about production issues and the inability to deliver the promotional video on schedule. The team conducted a comprehensive bug triage and task reassignment to address quality concerns.

---

## Summary

Lucas Cufré reported that clients were intensely concerned about production problems and the impossibility of meeting the promotional video delivery deadline. Bug tasks were reassigned to Eduardo Yuschuk and Esteban Restrepo based on code familiarity and frontend/backend separation. Lucas requested each team member (like Germán Derbes Catoni) to take ownership of their own backlog. Technical problems were discussed including the PostgreSQL to ClickHouse data migration, outlier pricing challenges, and the need for a daily "Bags" status report for the client.

---

## Key Discussion Points

### 1. Client Context and Expectations (00:05:36)

**Situation:**
- Clients were "medio intensos" (quite intense) due to problems detected in the Production environment
- Expected to resolve issues by the previous Friday, but it wasn't possible
- Goal: Deliver a promotional video of the product for the beta
- Focus shifted to resolving bugs

**Leadership Changes:**
- Lucas Cufré assumed greater responsibility in managing the "Bags" backlog together with Javier Grajales
- Purpose: Free up capacity for Martín Aranda to code more with the team

### 2. Additional Support and Task Assignment (00:07:09)

**Team Additions:**
- **Martín Legam** will rejoin the team on Wednesdays until the end of the roadmap
- Will help resolve problems that don't require deep product knowledge
- Full-stack capabilities: can assist both frontend and backend

**Task Reassignment Strategy:**
- Javier Grajales listed a large number of "Bxs" (bugs)
- Tasks reassigned to different team members (Eduardo Yuschuk, Esteban Restrepo) based on:
  - Familiarity with the code
  - Distinction between frontend and backend

### 3. Backlog Management and Individual Responsibility (00:08:30, 00:16:19)

**Owner ship Requirements:**
- Lucas requested each team member to own their own backlog of tasks
- Update statuses proactively
- Example: Germán Derbes Catoni - many issues related to orders will be resolved with the "token details" refactor he's doing
- Expectation: Developers should proactively identify which "Bags" they can resolve with their current fixes

### 4. Technical Challenges and Data Migration (00:12:06)

**PostgreSQL to ClickHouse Migration Issues:**
- **Eduardo Yuschuk** explained that while indexer functionality is already implemented, the transition from PostgreSQL to ClickHouse caused the loss of some functionalities
- **Problem:** The client already considered these functionalities as resolved
- **Reality:** Clients are not aware of the enormous reconstruction effort involved in the reorganization and backend refactor over the last four months (00:13:33)

**Impact:**
- Features that previously worked are now broken from the client's perspective
- Significant perception gap between internal technical work and client expectations

### 5. Communication with the Client and Bug Priorities (00:12:06)

**Reporting Requirements:**
- Need for a daily "Bags" status report for the client
- Main objective: Demonstrate that the team is progressing on bug resolution

**Testing Process:**
- Javier Grajales explained: Leave maximum information in tickets
- Move to "to test" when code is merged in "dev" and can be approved (00:14:39)

### 6. Testing and QA Process (00:16:19)

**Javier's Collaboration Offers:**
- Offered to collaborate on test planning for ClickHouse data migration
- Any other area the team needs
- Mentioned importance of testing multilayer referral (Federico Caffaro's responsibility)
- Highlighted complexity of doing beta on "mainnet" in Solana

**Luis's Clarity Needed:**
- Lucas emphasized the need for Luis to provide clarity on what can be tested to advance faster (00:30:16)

### 7. Design Modifications and Chart Functionalities (00:31:31)

**Token Display Changes:**
- Changes in definition of tokens shown in the interface:
  - Display "holding" and "PNL" instead of price and variation
  - Create a carousel

**Chart Requirements (00:34:13):**
- Need to show market capitalization and price on the chart axes
- **Blocker:** Requires the indexer to track the "total supply" of the token
- **Formula:** Market cap = Price × Total supply
- Without knowledge of one of these two values, can't calculate the third

### 8. Problems with Outlier Prices and Liquidity (00:18:41)

**Jupiter Indexing Issue:**
- **Eduardo Yuschuk** reactivated Jupiter indexing (had been temporarily disabled due to outlier prices)
- **Explanation:** These prices are real and due to liquidity removal, which distorts the charts
- **Solution:** Filter them from ClickHouse so they don't affect visualization
- **Reality:** Conceptually they have no fix - it's the nature of those markets

**Technical Reality:**
- Every time a user removes liquidity from an AMM, the equation is altered and everything gets distorted
- All protocols filter this to show a clean series
- Decision: Do what everyone else does, even though conceptually there's no perfect fix

### 9. Code Organization and Scalability (00:22:26)

**Limit Orders Refactor:**
- **Esteban Restrepo** and Lucas discussed bug resolution related to orders
- Esteban suggested many will be resolved with the "limit orders" refactor

**Microservices Architecture Discussion (00:25:18):**
- **Esteban's Argument:** Current microservices architecture by trading algorithms is scalable
- Unification is focusing on transaction logic
- Keep microservices by algorithm (DCA, limit orders, etc.)
- Centralize transaction execution logic

### 10. Task Assignment and Collaboration (00:26:32)

**Load Balancing:**
- Lucas offered to redistribute workload if Esteban feels overwhelmed
- Federico Caffaro could help with tasks not related to order execution
- **Principle:** If a refactor resolves several issues, prioritize that path

### 11. Chart Status and Component Implementation (00:38:13)

**Javier's Focus:**
- Will focus on reviewing charts while the team advances with tasks

**Design Consistency Strategy:**
- Large part of design work will be resolved once Germán Derbes Catoni implements corresponding components in the library
- Ensures interface design consistency
- Component library approach: Define behavior and styling once, reuse everywhere

---

## Recommended Next Steps

1. **Javier Grajales and Lucas Cufré** will define a new regression and determine focus areas for a general sweep over the next three weeks
2. **Eduardo Yuschuk** will work on the indexer to obtain the total supply of the token and calculate market cap
3. **Lucas Cufré** will test the hot keys on Mac
4. **Lucas Cufré** will handle the carousel and the quick operation panel

---

## Technical Insights

### Data Migration Challenges
The PostgreSQL → ClickHouse migration created significant regression in features that were previously working. This highlights the risk of major architectural changes close to release deadlines.

### Market Data Quality
The outlier price issue reveals a fundamental challenge in DeFi: liquidity removal events create real but visually problematic price spikes. The industry standard is to filter these, even though they represent actual market conditions.

### Architecture Strategy
The team is maintaining microservices by trading algorithm type (DCA, limit orders, perpetuals) while unifying the transaction execution layer. This provides scalability while reducing code duplication.

---

## Decisions Made

1. **Daily bug status reports** to be provided to the client
2. **Individual backlog ownership** - each developer manages their own bug list
3. **Refactor-first approach** - if a refactor resolves multiple bugs, prioritize the refactor
4. **Jupiter indexing reactivated** with ClickHouse filtering for outlier prices
5. **Market cap tracking** added to indexer requirements
6. **Component library strategy** maintained for design consistency

---

## Blockers and Risks

### Immediate Blockers
- Luis needs to clarify what can be tested (perpetuals)
- Total supply tracking not yet implemented (blocks market cap display)
- ClickHouse data migration causing feature regressions

### Timeline Risks
- Three weeks to launch (October 3rd target)
- Client expectations vs. technical reality gap
- Promotional video delivery delayed
- Mainnet Solana beta complexity (no testnet option)

---

## Team Dynamics

**Positive:**
- Proactive ownership mindset encouraged
- Cross-functional collaboration (Eduardo + Esteban on shared issues)
- Clear prioritization of refactors that resolve multiple bugs

**Concerns:**
- Martín Aranda needs more coding time (freed by Lucas taking backlog management)
- Luis not providing testing clarity
- Client pressure creating stress

---

## Transcript Highlights

**On Client Pressure (00:05:36):**
> "Los clientes están medio intensos con razón en algunos aspectos, con no tanta en otros... esperábamos poder tenerlas resueltas para el viernes, no pudimos..."

**On Migration Impact (00:13:33):**
> "El cliente no es consciente de todo el laburo de reconstrucción que hicimos en los 4 meses que pasaron desde que empezamos a reorganizar todo, desde que empezamos con todo el refactor del BAC, con la migración y demás."

**On Outlier Prices (00:18:41):**
> "Son precios reales, se deben a la remoción de liquidez, lo que distorsiona los gráficos. La solución es filtrarlos desde ClickHouse... conceptualmente no tienen arreglo."

**On Ownership (00:08:30):**
> "No quiero ser el micromanager de estar rompiendo, tocándole el hombro todo el tiempo... Lo que les voy a pedir a ustedes es ownership de su lado de estar mirando esto y activamente decir, 'Che, mira, esto, esto y esto, lo puedo resolver con este fix.'"

---

## Cross-References

**Related Requirements:**
- [Token Details Feature](../../04-knowledge-base/business/requirements/token-details.md) - Germán's refactor
- [Limit Orders Methodology](../../04-knowledge-base/business/requirements/limit-orders-methodology.md) - Esteban's refactor
- [Table Improvements and Bubble Maps](../../04-knowledge-base/business/requirements/table-improvements-bubblemaps.md)
- [Market Cap Variation Algorithm](../../04-knowledge-base/business/requirements/market-cap-variation-algorithm.md)

**Related Meetings:**
- [2025-09-12 Weekly Sync](Cooking%20Weekly%20Sync%2020250912.md) - Critical platform issues discussion
- [2025-09-12 Daily Standup](2025-09-12-daily-standup.md) - ClickHouse performance crisis
- [2025-09-15 Daily Standup](2025-09-15-daily-standup.md) - Same day standup
- [2025-09-15 Z & Lucas Sync](Sync-Z-Lucas-2025-09-15.md) - Client escalation context

**Related Technical Topics:**
- ClickHouse migration and data loss
- Jupiter indexing and outlier price filtering
- Component library implementation
- Microservices architecture for trading algorithms

---

## Notes

**Meeting Tone:** Serious and focused. Lucas established clear expectations for individual ownership while acknowledging the challenging situation with the client.

**Key Shift:** Moving from centralized task management (Lucas as bottleneck) to distributed ownership with daily reporting to maintain client confidence.

**Strategic Insight:** The team learned the hard lesson of maintaining QA/regression testing throughout major architectural changes rather than at the end.

---

**Meeting concluded at 00:43:16**

*Notes generated from Gemini transcription. This meeting was critical in establishing the bug resolution process for the final three-week sprint to the October 3rd closed beta launch.*
