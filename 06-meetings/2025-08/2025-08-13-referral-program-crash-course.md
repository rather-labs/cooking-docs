---
title: Referral Program Crash Course - 2025-08-13
type: meeting-note
date: 2025-08-13
---# Referral Program Crash Course

**Date:** August 13, 2025
**Time:** 12:28 GMT-03:00
**Duration:** ~25 minutes
**Meeting Type:** Technical Training / Feature Explanation
**Language:** Spanish (translated to English)

## Attendees
- **Lucas Cufré** - Project Lead
- **Martín Aranda** - Tech Lead / Backend Lead
- **Martín Lecam** - Developer (Willy)
- **Javier Grajales** - QA Lead
- **Marko Jauregui** - Team Member

## Meeting Context

Training session to explain Cooking's referral program implementation to the team. Lucas provided a detailed overview of two major initiatives: (1) custom referral codes for a smoother mobile experience, and (2) the introduction of a multilevel referral program that would allow initial referrers to earn profits from referrals up to the third level.

---

## Summary

Lucas Cufré provided a comprehensive overview of Cooking's referral program, detailing the implementation of custom codes for a smoother user experience and the introduction of a multilevel referral program that will allow initial referrers to earn profits from referrals up to the third level. Martín Aranda and Lucas discussed that users should have multiple referral codes rather than mutable ones. Martín Aranda clarified that the multilevel program involves a significant refactor of transactions and profit allocation calculations. Javier Grajales asked about commission visualization in the UI, and Martín Aranda reported that custom codes were expected for the following week, while the multilevel program had a deadline until the end of September.

---

## Key Discussion Points

### 1. Current Referral Program (00:02:35)

**How It Works Today:**
- Very simple implementation
- User clicks "Join" button (or "Join Referral Program")
- Automatically generates a referral link
- Works well for desktop version

**The Challenge:**
- **Mobile Integration Problem:** When building mobile version, need to allow users to log in and link to their referrer transparently and without friction
- **Desktop Assumption:** Works fine through browser
- **Multi-Environment Problem:** Android and iOS require dealing with respective app stores
- **Caching Issue:** Would need to cache the code and insert it at the correct moment - "a pain in the ass, basically"

### 2. Custom Codes Implementation (00:04:09, 00:05:36)

**The Solution - Custom Referral Codes:**

**Why Custom Codes:**
- Avoid the mobile caching complexity
- More user-friendly approach
- Easier to share and remember

**User Benefits:**
- Users can choose their own referral code
- Can use personal brand or tag
- Example: "Use my referral code on Cooking: it's LucasTrader"
- Easy to understand and share
- Continues personal brand

**URL Maintenance:**
- URL method is NOT being deprecated
- URL remains as an option
- Adding another method for mobile access

**Implementation Flow:**
- **Modal on First Login:** Instead of auto-generating code, show a modal
- **Pre-filled Code:** Modal comes pre-populated with auto-generated code
- **User Can Customize:** Allows user to input custom code
- **Restrictions Apply:**
  - No insults
  - No use of terminology related to the word "cooking"
  - List of reserved terms (in markdown file)

**Code Update Limitation:**
- Code update can only be done **once** in the referral lifecycle
- **Reason:** To avoid invalidating the previous code

### 3. Multiple Codes vs. Mutable Codes (00:07:11)

**Use Case Identified:**
- Common scenario: Person with access to many people in Solana ecosystem rebrands
- Would require a new code

**Two Possible Approaches:**

**Option 1: Mutable Codes**
- Allow changing the code
- Need to handle mapping and revalidation
- More complex

**Option 2: Multiple Codes (Preferred)**
- User can have several codes
- Create alias system
- Build a tree structure
- **Advantage:** No need to invalidate or re-link
- **Simpler implementation**

**Technical Implementation:**
- **Martín Aranda:** "It can be done"
- Change from one-to-one to one-to-many relationship
- During login, read entire list of codes

### 4. Beta Cap on Referrals (00:08:29)

**Client Request:**
- For beta, might want to cap the number of people who can log in per code
- **Question:** Can we programmatically cap this now?

**Martín's Answer:**
- Not currently available (not implemented yet)
- **When Refactor is Done:** Can be done perfectly
- **Example:** "All codes have 5 referrals for now, and eventually [change]"

### 5. UI Display with Multiple Codes (00:08:29)

**Willy's Question:**
- If user has N referrals, how would we show this in the current screen?

**Current Screen:**
- Shows referral code (e.g., "1J...")
- Shows count of referred users associated with that code

**Lucas's Answer:**
- Current screen doesn't have what's needed yet
- **Next Initiative:** Will add multilevel visualization
- Still work to be done on UI

### 6. Multilevel Referral Program (00:09:47, 00:11:19)

**The Next Initiative:**

**Current State (Two Layers Only):**
- Users can be referrers
- Earn profits only from direct referrals (Level 1)

**New Multilevel Logic:**
- Initial referrer earns profits from:
  - **Level 1:** Direct referral
  - **Level 2:** Referral of their referral
  - **Level 3:** Referral of the referral of their referral

**Scope Difference - Important Note (00:11:19):**

**Custom Codes Task:**
- Affects: Code creation moment
- Affects: User creation that references the code
- **Does NOT affect:** Transactions

**Multilevel Task:**
- **Complete Refactor** of transactions
- **Affects:** Fee extraction and profit allocation calculations
- **Much more complex**
- **Core Business Logic:** This together with limiters is the core of what makes the product truly profitable

### 7. Commission Structure (00:11:19, 00:13:02)

**Base Commission:**

**Tier 1: $0 - $100,000 traded volume**
- 30% of Level 0 commissions
- **Calculation:** Referrer has 5 people below
- Those 5 people: Sum of traded volume calculated in dollars from $0 to $100,000
- **30% of the 1%** transaction fee that Cooking charges goes to the initial referrer
- **Cap:** Once reaching $100,000, no extra charge
- **Maximum:** The cap is $100,000

**Tier 2: $100,000 - $500,000**
- 35% commission rate

**Tier 3: $500,000 - $2,000,000**
- 40% commission rate

**Tier 4: Over $2,000,000**
- 45% commission rate

**Important Note:**
- This is a tree structure
- More referrals in Layer 1 = easier to reach higher values

**Performance-Based Bonus (00:14:56):**

**Personal Volume Incentive:**
- Calculated over 30 days
- Based on personal traded volume
- **Threshold:** If personal traded volume exceeds $10,000 in a 30-day period
- **Bonus:** Pay an additional 5% on top of the base commission

**Maximum Scenario:**
- If user "blows everything up" (maximum scenario)
- Can earn up to **55%** of the 1% commission
- **Calculation:** 45% (tier 4) + 10% (performance bonus) = 55% total

**Potential Earnings:**
- Could easily be $200,000+ in a month
- "We're talking about a lot of money"

### 8. Comparison with Other Platforms (00:14:56)

**Martín's Research - Pumpfun Example:**
- Similar multilevel referral program
- **Top Earner:** Makes $1.5 million per month (number one)
- **Common Question:** "How does he make so much money, such good trades?"
- **Reality:** Makes ~$100,000+ per month from own trades
- **Rest:** All from referrals
- **Success Factor:** Became famous as a Meme Coin trader

### 9. UI and Commission Visibility (00:16:31)

**Javier's Question:**
- When making purchases, doesn't see commission expressed in the amount
- Should each operation show which commission corresponds?

**Lucas's Answer:**
- **Not Currently Shown:** Commission not displayed in UI
- **Also Missing:** Gas fee (Gasfi) not shown either
- **Needs to be Mapped:** Something that needs to be added

**Future Improvement:**
- Lucas will create an initiative to map potential UI improvements
- Including: Commission visualization and Gasfi

**Current UI Limitations:**
- Shows: Priority fee and slippage
- **Doesn't Show:**
  - Gas fee
  - Commission breakdown
  - Exact purchase amount calculation

**Technical Challenge:**
- **Slippage is Large:** Already significant
- **Priority Fee Varies:** Can vary enormously
- **Estimation Difficulty:** No way to estimate exactly how much will be bought and what fee will come out of that
- **Possible:** Can make an approximation

### 10. Withdrawal Flow Unification (00:21:35)

**Mobile Feature Proposal:**
- Unify withdrawal with creating a new address in the withdrawal wallet (address book)

**Current State:**
- Today: Two separate endpoints
- Flow 1: Withdraw to external wallet
- Flow 2: Register this wallet

**Proposed Flow:**
- "Send to external and save it"
- Since it's external, save it in the address book

**Martín's Response:**
- Two calls to the endpoint
- **Not necessary to unify** into one
- Can be done transparently for the user
- Automated backend handling

### 11. Face ID and Security (00:23:04)

**Security Password Requirement:**
- Withdrawals require security password
- Must be mapped somewhere in the flow

**Face ID Discussion:**

**Lucas's Question:**
- How annoying is it to include Face ID?
- Apple is somewhat insistent on this for certain things

**Backend Limitation:**
- **Martín:** "Our backend doesn't support Face ID or anything related"

**Possible Workaround:**
- When creating security password or registering Face ID:
  - Store security password in **keychain protected with Face ID**
  - App requests Face ID to retrieve password and auto-complete it
- This CAN be done

**Apple Concern:**
- Lucas needs to understand if Apple will block the app release for not having Face ID
- Needs to discuss with Byron (mobile developer)

### 12. Implementation Timelines (00:21:35)

**Marko's Question:** What are the timelines/deadlines?

**Martín's Response:**

**Custom Codes:**
- Expected: **Next week** (week of August 18-25)

**Multilevel Program:**
- Deadline: **End of September** (by September 30)
- Needs to be completely closed and tested

---

## Recommended Next Steps

1. **Lucas Cufré** will create an initiative to map potential UI improvements, including commission visualization and Gasfi
2. **Lucas Cufré** will talk to Santi to get access to the Figma screen for referral design
3. **Martín Aranda** will assign the charts task to Germán

---

## Technical Insights

### Architecture Decisions

**Why Multiple Codes Over Mutable:**
- Simpler data model (one-to-many vs complex mutation tracking)
- No need to invalidate previous codes
- Easier alias system
- Tree structure naturally forms

**Transaction Refactor Complexity:**
- Custom codes: Cosmetic, affects user creation
- Multilevel: Core business logic, affects every transaction
- Fee extraction needs complete rework
- Profit allocation calculations need rebuilding

**Face ID Implementation:**
- Backend can't directly support Face ID
- Workaround: Store password in keychain, unlock with Face ID
- Need to check if Apple requires native Face ID support

### Business Model

**Why This Matters:**
- Multilevel referrals + limiters = Core profitability
- Can generate $200,000+ monthly for top referrers
- Competitive with platforms like Pumpfun ($1.5M/month top earner)

### Mobile Strategy

**Why Custom Codes:**
- App store flow complexity
- Caching issues between store and app
- User experience (memorable codes)
- Personal branding opportunity

---

## Decisions Made

1. **Multiple codes** preferred over mutable codes
2. **Custom codes** implementation for next week
3. **Multilevel program** deadline: end of September
4. **Commission structure** finalized: 30%-45% base + 10% performance bonus
5. **Withdrawal + address book** can be unified via two API calls
6. **Face ID workaround** approved (keychain-based)
7. **UI improvements** to be mapped in separate initiative

---

## Action Items

### Lucas Cufré
1. Create initiative for UI improvements (commission display, Gasfi)
2. Talk to Santi about Figma access for referral design
3. Discuss Face ID requirements with Byron (mobile)

### Martín Aranda
1. Implement custom codes (deadline: next week)
2. Assign charts task to Germán
3. Begin multilevel transaction refactor (deadline: end of September)

### Martín Lecam (Willy)
1. Review custom codes implementation once Figma is available
2. Implement UI changes for referral code selection

### Javier Grajales
1. Test custom codes when ready
2. Create test plan for multilevel commission calculations

---

## Commission Calculation Examples

**Example 1: Small Referrer**
- 5 direct referrals
- Combined volume: $80,000 in 30 days
- **Earnings:** 30% of 1% of $80,000 = $240

**Example 2: Growing Referrer**
- 20 referrals across 3 levels
- Level 1 volume: $400,000
- Level 2 volume: $150,000
- Level 3 volume: $50,000
- **Level 1:** 35% of 1% of $400,000 = $1,400
- **Level 2 & 3:** Additional earnings
- **Plus 10% bonus** if personal volume > $10,000

**Example 3: Top Referrer (Like Pumpfun)**
- Massive referral network
- Multi-million monthly volume
- **Can earn:** $1,500,000/month (proven by competitor data)
- **Personal trades:** ~$100,000/month
- **Referral earnings:** ~$1,400,000/month

---

## Cross-References

**Related Requirements:**
- [Referral Program Multilevel](../../04-knowledge-base/business/requirements/referral-program-multilevel.md)
- [Referral Program Invite Codes](../../04-knowledge-base/business/requirements/referral-program-invite-codes.md)
- [Mobile Signup/Login/Home](../../04-knowledge-base/business/requirements/mobile-signup-login-home.md)
- [External Wallet Support](../../04-knowledge-base/business/requirements/external-wallet-support.md)

**Related Meetings:**
- [2025-08-18 Weekly Sync](Cooking%20Weekly%20Sync%2020250818.md) - Referral program in context
- [2025-08-25 Limit Orders](2025-08-25-limit-orders.md) - Related backend refactor
- [2025-10-01 Mobile App Sync](../2025-10/2025-10-01-mobile-app-sync.md) - Mobile implementation

**Related Technical Topics:**
- Transaction fee extraction
- Commission calculation algorithms
- Mobile deep linking
- Keychain and Face ID integration
- One-to-many data relationships

---

## Notes

**Meeting Style:** Educational and collaborative. Lucas took time to explain both the business logic and technical implementation in detail.

**Key Teaching Moment:** Clear distinction between cosmetic changes (custom codes) and core business logic changes (multilevel commissions).

**Competitive Intelligence:** Reference to Pumpfun's $1.5M/month top earner validates the business model.

**Strategic Importance:** This feature is explicitly called out as "core" to profitability alongside limiters.

---

**Meeting concluded at 00:25:31**

*Notes generated from Gemini transcription. This crash course provided the entire team with a comprehensive understanding of the referral program's business model and technical requirements.*
