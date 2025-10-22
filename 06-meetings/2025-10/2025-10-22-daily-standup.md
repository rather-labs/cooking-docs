---
title: Daily Standup - October 22, 2025
date: 2025-10-22
type: daily-standup
attendees:
  - Lucas Cufré
  - Martin Aranda
  - Luis Rivera
  - German Derbes Catoni
  - Marko Jauregui
  - Federico Caffaro
  - Esteban Restrepo
  - Eduardo Yuschuk
  - Byron Chavarria
  - Javier Grajales
  - Santiago Gimenez
status: completed
tags:
  - daily-standup
  - authentication
  - cookies
  - cors-configuration
  - knowledge-base
  - clickhouse
  - transaction-speed
  - limit-orders
related:
  - "[[2025-10-21-daily-standup]]"
  - "[[2025-06-27-clickhouse-time-series-data]]"
original-language: Spanish
translated: true
translation-date: 2025-10-22
---

> **Note:** This meeting was conducted in Spanish and has been translated to English for documentation purposes.

## Executive Summary

The team focused on critical production issues including CORS configuration for cookies, authentication migration to cookie-based system, and order form validation bugs. Lucas introduced a centralized knowledge base initiative for the project using Claude AI for documentation indexing. Multiple frontend improvements were completed including portfolio refactoring, watchlist features, and limit order UI. Backend work progressed on Pam Fun/Pam Swap protocol updates, transaction validator enhancements, and liquidity provider identification.

## Meeting Details

**Duration:** 38 minutes 50 seconds
**Platform:** Google Meet
**Recording:** Available
**Transcription:** Available

## Topics Discussed

### 1. Meeting Backgrounds Distribution

**Context:** Lucas shared new meeting backgrounds several days ago via the team channel.

**Issue:**

- Multiple team members (Federico, Marko, Luis, Germán) hadn't seen or changed their backgrounds
- Communication visibility concerns raised

**Key Points:**

- Lucas expressed frustration about unread messages
- Team acknowledged they missed the message from Monday
- Highlights ongoing challenge with internal communication

---

### 2. Frontend Updates - Luis Rivera

**Completed:**

- Removed outline from share button in token details ([00:04:14])
- Adjusted spacing issues in NB (navbar)
- Revised position list carousel based on Santiago's feedback
  - Fixed hover behavior overlapping separator
  - Resolved z-index and spacing issues

**In Progress:**

- Login screen visual effects ticket
- Token details rejected ticket - addressing review comments

**Bug Identified:**

- Image rendering inconsistency between Chrome and Safari
- Same monitor showing different image positioning/sizing
- Likely caused by improper container-based image resizing
- Luis to investigate and fix in login screen ticket

---

### 3. React Best Practices - Key Property

**Context:** Martin emphasized critical React development practice.

**Important Reminder:**

- Always use `key` property when using `.map()` for iterations
- Applies even to React Fragments
- Missing keys caused production bug yesterday that broke all carousels

**Incident Details:**

- Home carousel and Positions carousel broke in production
- Without keys, React was deduplicating items incorrectly
- Showed only one item instead of all items
- Bug appeared in production but not in local development
- Required immediate hotfix and redeployment

**Action:** All React developers must ensure keys are used in all iterations

---

### 4. Critical Production Bug - Custom Order Form

**Priority:** HIGH - Production critical

**Issue:**
Users cannot save values in optional fields for custom orders:

- Average Holding Time field
- Price Change field

**Investigation:**

- Javier confirmed issue occurs with Price Change and Average Holding Time
- Other fields (Holders Count, Liquidity Amount) work correctly
- Problem is related to fields with time frame references

**Root Cause:**

- Fields don't have default values
- Only activates when time unit is changed (minutes → hours)
- Changing the time frame selector enables the save button
- Fields should have pre-selected default values

**Assigned:** Germán, Marko (whoever is available)

**Technical Details:**

- Fields with time frame components fail validation
- Changing time unit (minutes/hours/days) triggers proper state update
- Main issue: lack of default/initial state for time-based fields

---

### 5. Portfolio Refactoring - German Derbes Catoni

**Completed:**

- Refactored portfolio section to match token Details and advance order structure
- Standardized column distribution across all three views
- Wider layout implemented

**Bug Fixes:**

- Removed unwanted animation effect from Kitchen filter modals
  - Modals were appearing from top with strange animation
  - Animation removed for cleaner UX
- Fixed visual bug in Dev environment
  - Batch cards (particularly Depol) appearing too large
  - Fix included in upcoming PR

**Future Plan:**

- Create unified layout component for all similar sections
- Each new section would simply define: sidebar content, top content, bottom content
- Standardizes screen structure across platform
- Improves maintainability and consistency

**Blocked:** Waiting for Santiago consultation on title text

---

### 6. Transaction Visualization Issues

**Issue Identified:**
Activity breakdown section not displaying sold assets correctly

- Shows empty state when user has no current holdings of an asset
- Historical sales data not displayed
- Appears "broken" or empty when it shouldn't

**Investigation:**

- User sells entire position of token
- Activity breakdown for that token shows nothing
- Should show historical data or proper empty state

**Proposed Solutions:**

1. Add proper empty state component
2. Display chart in grayscale/empty mode to indicate no current holdings
3. Clarify that view shows only current positions, not historical

**Consideration:**

- Chart behavior existed before Martin's changes
- Need to review with Luis (original chart implementer)
- Decide on appropriate UX for "no current holdings" state

---

### 7. CORS Configuration Issue - CRITICAL

**Priority:** URGENT - Production breaking

**Issue:**
CORS in transaction service configured with wildcard, incompatible with cookie-based authentication

- Affects batch operations in dev and production
- Breaking since cookies are now being sent

**Discussion:**

- Martin: Is CORS in transaction service using general utility or manually configured?
- Esteban: Likely manually configured
- Martin: Need to use same CORS utility as backend and Hyperliquid services

**Action Items:**

- Esteban to verify CORS configuration in backend service
- Duplicate proper CORS setup to transaction service
- Use shared CORS utility if possible
- Priority: Immediate (blocking production batch operations)

**Technical Context:**

- Moving to cookie-based auth (more secure, prevents XSS)
- Wildcard origins incompatible with credentials: 'include'
- Must specify exact origins when sending cookies

---

### 8. Backend Updates - Marko Jauregui

**Completed:**

- Liquidity provider batch processing implementation

**Learning Initiative:**

- Dedicating extra time to learn more backend concepts
- Goal: Assist backend team when needed
- Building full-stack capabilities

**Availability:**

- Open to helping on any tasks (frontend or backend)
- Martin requested PR review on frontend draft

---

### 9. Clickhouse & Transaction Validator - Federico Caffaro

**Hyperliquid Chart:**

- Confirmed no more hanging issues
- Working correctly in production

**Liquidity Provider Identification:**

- Added wallet identification for liquidity providers
- Uses AMMs table in Clickhouse
- Checks if wallet belongs to Mint's Market Maker
- Marks wallets as "Liquidity Provider" or "Not"

**Technical Decision:**

- Initially attempted JOIN in main query
- JOIN caused significant performance degradation
- Split into separate query - much faster
- Query performance prioritized over single-query elegance

**Transaction Validator Enhancements:**

- Added validation: Fee percentage cannot exceed 1%
- Added validation: Solana egress cannot exceed 1%
- Tests written for mock transactions
- Validation rules:
  1. Programs must be whitelisted
  2. Solana only goes to Cooking Fee Wallet Address
  3. Fee and egress amount limits enforced

**Next Steps:**

- Complete tests
- Martin and Eduardo to review PR
- Federico will share PR link after final checks

---

### 10. Fee Division Discussion - Esteban Restrepo

**Original Task:**

- Divide fees into two wallets: platform fees and referral fees
- Separate hot wallets for each fee type

**Martin's Reconsideration:**

- Making two transactions per user operation adds complexity
- Performance and reliability concerns
- Alternative: Use cron job to move funds from hot wallet to cold wallet when threshold reached
- Keep single transaction flow for users

**Decision:**

- Pause fee division implementation
- Keep current single-wallet fee structure
- Explore cron-based cold wallet transfer solution
- Avoid refactoring fee calculation logic (currently in transaction confirmation)

**Other Work - Esteban:**

- Auto-priority fee fixes from Lucas's report
- VWAP bug investigation and fixes
- Closing minor tickets in Notion
- Working through backlog cleanup

**Status Update Note:**

- Notion shows VWAP bug as "not started" but Esteban marked as in progress
- Martin to reload and verify

---

### 11. Transaction Speed Comparison

**Context:**
Lucas shared video of transaction speed

**Clarification:**

- Video recorded in development environment
- Should mirror production performance now

**Current Status:**

- Martin: "Decent" speed, but still behind competition
- Frontend optimizations implemented (somewhat "deceptive")
- Belief: Competition using similar tricks

**Competitive Analysis:**
Lucas observed Axiom's behavior:

- Toast notification shows countdown from 16 seconds
- Transaction confirms almost immediately
- Likely confirming on "submitted" status instead of "confirmed"
- Martin confirmed: Frontend now listens for "submitted" status to show toast

**Technical Implementation:**

- System continues listening for batches
- Shows toast when status reaches "submitted" or higher
- Balances perceived speed with actual confirmation tracking

---

### 12. Protocol Updates - Eduardo Yuschuk

**Pam Fun & Pam Swap Updates:**

**Context:**

- Protocols added new purchase operation
- Now two possible sources for purchase events
- Old IDL still in use alongside new IDL
- Old function remains available but event structure changed

**Challenge:**

- New optional parameter added to event structure
- Borsh (serialization library) in JavaScript doesn't handle optional attributes safely
- Rust Borsh handles this correctly, but JavaScript implementation is limited
- Cannot use "safe serialize" approach that works in Rust

**Current Solution:**

- Manually trimming last parameter (not needed for our use case)
- Will deploy updates today
- Testing thoroughly to avoid breaking existing functionality

**Technical Limitations:**

- JavaScript/TypeScript Borsh less capable than Rust version
- Manual parsing required for optional fields
- Cannot safely handle incomplete byte vectors

**Alternative Rejected:**

- Using two different IDLs would work
- Catching parsing exceptions with old IDL, retry with new IDL
- BUT: Exceptions are expensive for indexer targeting 100ms performance
- Manual parsing is faster despite being less elegant

**Future Considerations:**

- May need to abandon Borsh-based parsing for more complex protocols
- Most other protocols already use manual parsing
- Borsh useful for lightweight protocols, but hitting limitations
- Failed transaction parsing requires manual approach anyway (Borsh ignores failed txs)

**Status:**

- Both Pam Fun and Pam Swap will be updated today
- Functionality preserved, edge cases handled
- Not fully satisfied with JavaScript parsing limitations but acceptable solution

---

### 13. Limit Order Integration - Byron Chavarria

**Completed:**

- UI integration for Limit Order feature complete
- Mapped all services, requests, and responses
- PR already approved by Martin

**Clarification Needed:**

- How to show SELL limit order flow vs BUY
- When/where to display sell limit functionality
- Needs 5-minute sync with Martin and Lucas to define flow

**User Settings Progress:**

- Main user settings view implemented
- Subsections being created for each option
- Building out navigation structure

**Mobile App Considerations:**

- Martin reminded Byron about pending mobile app discussion
- Cookie authentication implications for mobile
- Quick orders endpoint changes not communicated yet
- Backend endpoint changes for quick operations and transfer
- Listening method for responses also changed

**Action:**

- Martin and Byron to meet in 20 minutes to discuss:
  1. Limit order sell flow
  2. Mobile cookie authentication strategy
  3. Quick orders API changes
  4. Response listening pattern updates

---

### 14. QA & Testing - Javier Grajales

**MCP Google Integration Research:**

- Investigating MCP (Model Context Protocol) from Google
- Integrates with Dev Tools
- Looks promising for testing automation
- Will test with Juli before project implementation
- Could streamline testing workflows

**Order Regression Testing:**

- Defining test suite format and structure
- Evaluating best tools for regression testing
- Preference: Keep everything in Notion for unification
- Need to verify Notion's suitability for test case management

**Other Activities:**

- Closed several tickets
- Extensive conversations with Lucho
- Bringing Lucho up to speed on recent work
- Knowledge transfer sessions

---

### 15. Design Updates - Santiago Gimenez

**Filter Improvements:**

- Conducted research on filter enhancements
- Near-final version ready
- Improved UX and functionality

**Watchlist Feature:**

- Complete and ready for review
- Available in Exploration section
- Awaiting Martin's review

**Status:**

- Watchlist: Ready for PR review
- Filters: Final touches, will be ready shortly

---

### 16. Knowledge Base Centralization - Lucas Cufré

**Context:**
Lucas discussing with clients about Guardians feature

**Major Initiative Announced:**

**Problem:**

- Project knowledge scattered across meetings, threads, Slack
- Difficult to onboard new team members
- Information loss when people leave project
- No single source of truth for decisions and context

**Solution: Centralized Knowledge Base**

**Structure:**

- Foundation: Project glossary, stakeholders, tech stack
- Decisions: ADRs (Architecture Decision Records) with dates, owners, rationale
- Active Work: Current status, priorities, blockers
- Knowledge Base: Technical and business documentation
- Meetings: Structured meeting notes
- Documents to Parse: Staging area for new content

**Implementation:**

- Refactored all content from May 2025 to present
- Organized by category and date
- Markdown-based, stored in Git repository
- Will live within project repository

**AI Integration:**

- Claude AI can index and query the entire knowledge base
- Demonstrated live: Asked "When did we decide to integrate Clickhouse?"
- Claude searched meetings, decisions, and documentation
- Returned: June 27, 2025, with full context, owners, stakeholders, and rationale
- Response included problem context, decision details, and timeline

**Benefits:**

1. **Instant Knowledge Access:** Ask questions, get sourced answers
2. **Onboarding:** New team members can query project history
3. **Decision Tracking:** All major decisions documented with rationale
4. **Context Preservation:** Why decisions were made, not just what was decided
5. **Exit Documentation:** Easier team transitions

**Access Methods (Martin's addition):**

1. **Local IDE:** Developers with Claude Code can query directly
2. **GitHub Issues:** AI can investigate and comment on issues automatically
3. **Web Interface:** Claude subscription users can link repository and query online

**Content Examples:**

- ClickHouse two-client architecture decision
- Multilevel referral program requirements
- Indexer microservices protocol
- Microservices by algorithm approach
- Jupiter vs Echo comparison and decisions
- All feature requirements and specifications

**Maintenance:**

- Lucas will primarily maintain organization and structure
- Content sourced from ongoing meetings and decisions
- Standardized format for consistency
- Git-based for version control and collaboration

**Status:**

- System functional and tested
- Ready for team use
- Will continue evolving as project progresses

---

### 17. Cookie-Based Authentication Migration - Martin Aranda

**Context:**
Previously discussed moving authorization to cookies for improved security

**Security Goals:**

- Prevent XSS (Cross-Site Scripting) attacks
- More secure than localStorage/header-based tokens
- Industry best practice for authentication

**Implementation Challenges:**

**Multi-Service Architecture:**

- Frontend on one domain
- Multiple backend microservices on different domains
- Must work cross-domain
- Cookies must be secure and http-only

**Local Development Complexity:**

- Developers need to hit some backends locally, others remotely
- Cookie restrictions make this difficult
- Cannot simply configure backend URLs via environment variables

**Solution: Next.js Proxy**

**Architecture:**

- Proxy server running in Next.js
- Acts as intermediary between frontend and backends
- Handles cookie parsing and forwarding
- Backends can be local or remote

**Configuration:**

- Same environment variables as before
- But WITHOUT `NEXT_PUBLIC_` prefix (server-side only)
- Proxy handles cross-domain cookie complexities
- Developers configure which backends are local vs remote

**Current Status:**

- Working for normal backend and Hyperliquid service
- Still testing with transaction service
- Found CORS issues (Esteban addressing)
- Will merge once transaction service confirmed working

**Transition Plan:**

1. **Current:** Backend supports both methods (cookies AND headers)
2. **Phase 1:** Remove body-based access/refresh tokens
3. **Phase 2:** Remove header-based tokens
4. **Final:** Cookie-only authentication

**Cookie Details:**

- Set for all subdomains of cooking.gg
- Secure flag enabled
- HttpOnly flag enabled
- Cross-domain capable

**Mobile Considerations:**

- Byron needs separate discussion
- Mobile auth patterns different from web
- Will address in dedicated meeting

**Next Steps:**

- Complete transaction service testing
- Merge cookie authentication PR
- Share environment variable configuration with team
- Document proxy setup for local development

---

### 18. API Endpoint Changes - Mobile Impact

**Martin to Byron:**

**Backend Changes:**

- Quick orders endpoint modified
- Transfer endpoint modified
- Response listening pattern changed

**Impact:**

- Mobile app needs updates to match new endpoints
- Frontend already updated and working
- Byron was not notified (Martin's oversight)

**Action:**

- Scheduled sync meeting in ~20 minutes
- Will review all backend changes
- Define mobile implementation strategy

---

### 19. Service Cleanup - Esteban Restrepo

**Endpoint Removal Plan:**

**Production Security:**

- Transaction microservice has test endpoint that sends transactions
- Cannot exist in production environment
- Will be removed immediately

**Deprecated Endpoints:**

- Quick Operation v1 endpoint still exists
- Byron currently using it in mobile app
- Can remove once Byron migrates to v2
- Martin confirmed safe to remove after Byron's update

**Service Communication Refactor:**

**Current Issue:**

- Some services communicate via HTTP requests
- Not ideal for internal service communication

**Preferred Approach:**

- Use shared library for inter-service communication
- Martin demonstrated this pattern with recent backend work
- More efficient and type-safe

**Esteban's Plan:**

- Replicate Martin's library-based communication pattern
- Replace HTTP endpoints with shared library calls
- Remove exposed endpoints that are internal-only
- Cleaner, more maintainable service architecture

**Timeline:**

- Quick Operation v1 removal: After Byron's migration
- Test endpoint removal: Immediate
- Library-based communication: Gradual refactor

---

## Decisions Made

| Decision                                              | Rationale                                                                           | Owner           | Impact                                                  |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------- |
| Pause fee division implementation                     | Two transactions per operation adds complexity; explore cron-based solution instead | Martin, Esteban | Avoids major refactoring; maintains current performance |
| Use shared CORS utility for transaction service       | Wildcard CORS incompatible with cookies; must match other services                  | Esteban         | Fixes production-blocking cookie authentication         |
| Move authentication to cookie-based system            | Improved security; prevents XSS attacks                                             | Martin          | Better security posture; requires proxy for development |
| Implement Next.js proxy for local development         | Allows mixing local/remote backends while using cookies                             | Martin          | Maintains developer flexibility with secure auth        |
| Add default values to custom order time fields        | Fields without defaults cause validation failures                                   | Germán/Marko    | Fixes production bug preventing order creation          |
| Knowledge base centralization with Claude AI indexing | Improves onboarding, preserves context, enables knowledge queries                   | Lucas           | Faster knowledge access; better documentation           |

---

## Action Items

### Critical Priority (Today)

- [x] **Esteban Restrepo** - Fix CORS configuration in transaction service to support cookies (Due: Immediate - BLOCKING)
- [ ] **Germán/Marko** - Fix custom order form validation for time-based fields (Due: Today)
- [ ] **Martin & Byron** - Sync on limit order sell flow and mobile API changes (Due: 20 minutes from meeting end)

### High Priority (This Week)

- [ ] **Luis Rivera** - Fix image rendering inconsistency between Chrome and Safari (Due: With login screen ticket)
- [ ] **Luis Rivera** - Address token details rejected ticket comments (Due: This week)
- [ ] **Germán Derbes Catoni** - Consult with Santiago on portfolio refactor title (Due: Before PR)
- [ ] **Federico Caffaro** - Complete transaction validator tests and share PR with Martin & Eduardo (Due: This week)
- [ ] **Eduardo Yuschuk** - Complete Pam Fun and Pam Swap protocol updates (Due: Today)
- [ ] **Marko Jauregui** - Review Martin's frontend draft PR (Due: This week)

### Medium Priority

- [ ] **Martin Aranda** - Complete cookie authentication testing with transaction service (Due: This week)
- [ ] **Martin Aranda** - Document environment variable configuration for proxy setup (Due: After merge)
- [ ] **Byron Chavarria** - Migrate mobile app to Quick Operation v2 endpoint (Due: This week)
- [ ] **Esteban Restrepo** - Refactor service communication to use shared library instead of HTTP (Due: Ongoing)
- [ ] **Esteban Restrepo** - Remove test endpoints from transaction microservice (Due: This week)
- [ ] **Santiago Gimenez** - Finalize filter improvements (Due: This week)
- [ ] **Javier Grajales** - Complete order regression testing plan (Due: This week)

### Low Priority / Ongoing

- [ ] **Lucas Cufré** - Continue knowledge base maintenance and organization (Due: Ongoing)
- [ ] **Team** - Always use `key` property in React `.map()` iterations (Due: Ongoing practice)
- [ ] **German/Luis** - Decide on empty state UX for activity breakdown with no holdings (Due: Future)

---

## Blockers & Risks

| Blocker/Risk                                | Impact                                          | Owner        | Mitigation                                |
| ------------------------------------------- | ----------------------------------------------- | ------------ | ----------------------------------------- |
| CORS wildcard blocking cookie auth          | Production batch operations broken              | Esteban      | Fix in progress - use shared utility      |
| Custom order form validation bug            | Users cannot create certain custom orders       | Germán/Marko | High priority fix today                   |
| Byron not notified of backend changes       | Mobile app may break with new endpoints         | Martin/Byron | Immediate sync meeting scheduled          |
| Borsh JavaScript limitations                | Complex protocol updates require manual parsing | Eduardo      | Using manual parsing; acceptable solution |
| Image rendering Chrome/Safari inconsistency | Visual quality issues on Safari                 | Luis         | Investigating container-based resizing    |
| Activity breakdown empty state confusion    | Appears broken when no current holdings         | German/Luis  | UX decision needed                        |

---

## Technical Notes

### React Development Reminder

- **ALWAYS** use `key` prop in `.map()` iterations
- Applies to all components, including Fragments
- Missing keys can cause silent deduplication bugs
- Bug may not appear in development but breaks in production

### Cookie Authentication Architecture

- Cookies set for all `*.cooking.gg` subdomains
- Secure and HttpOnly flags enabled
- Next.js proxy handles cross-domain complexity
- Backend supports dual auth during transition (cookies + headers)
- Environment variables now server-side only (no `NEXT_PUBLIC_`)

### Clickhouse Performance Patterns

- Separate queries often faster than complex JOINs
- Query performance prioritized over query elegance
- Use AMMs table for liquidity provider identification

### Protocol Parsing Challenges

- JavaScript Borsh less capable than Rust Borsh
- Optional parameters require manual parsing
- Exception handling expensive for high-performance indexers
- Manual parsing provides more flexibility for edge cases

---

## Key Metrics & Numbers

- **Transaction Speed:** Current performance "decent" but behind competition
- **Fee Limits:** Max 1% for fees and Solana egress in transaction validator
- **Meeting Duration:** 38 minutes 50 seconds
- **Knowledge Base Coverage:** May 2025 to present
- **Team Size:** 15+ active developers

---

## References

- [ClickHouse Migration Decision (2025-06-27)](../../02-decisions/2025-06-27-clickhouse-time-series-data.md)
- [ClickHouse Two-Client Architecture](../../02-decisions/2025-10-06-clickhouse-two-client-architecture.md)
- Previous Daily: [2025-10-21 Daily Standup](2025-10-21-daily-standup.md)
- Next.js Proxy Documentation: (To be created by Martin)
- Transaction Validator Specification: (PR pending)

---

**Meeting recorded and transcribed by Google Gemini**
**Structured documentation created:** 2025-10-22
