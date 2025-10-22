---
title: Sync Z <> Lucas - UX Testing Setup & QA Resources
type: meeting-note
date: 2025-09-22
attendees: [Lucas Cufré, Zen, Marcos Tacca]
meeting-type: weekly-sync
tags: [sync, ux-testing, qa, development-progress, slack-channel, staging-environment]
summary: |
  Development progress update with chart filter testing nearly complete, outlier solutions implemented, and perpetuals limit orders testing underway. Main focus on setting up UX testing framework for Zen's involvement - established dev URL as testing environment, created dedicated Slack channel for findings, and whitelisted Chef account via Telegram. Confirmed additional permanent QA resource allocation and dedicated staging environment for continuous testing going forward.
related-docs:
  - QA testing procedures
  - UX testing framework
  - Staging environment setup
---

# Sync Z <> Lucas - UX Testing Setup & QA Resources

**Date:** 2025-09-22
**Duration:** ~18 minutes
**Attendees:** Lucas Cufré, Zen, Marcos Tacca
**Meeting Type:** Weekly Sync / UX Testing Setup

## Executive Summary

Progress-focused sync with key developments across multiple workstreams. Lucas reported chart filter testing completion, outlier identification/fixes, and market cap/liquidity calculation corrections - all expected complete same day. Main agenda item was establishing framework for Zen's direct UX testing involvement using dev URL, dedicated Slack communication channel, and Chef account whitelist access. Discussion confirmed that additional QA resource will remain permanently (not just for beta) and dedicated staging environment being planned to support ongoing development and parallel feature/bug management.

## Discussion Topics

### Development Progress Updates

**Chart and Filter Testing:**
- Token chart bar filter testing nearly complete
- Outlier causes identified
- Market cap and liquidity calculation errors being fixed
- **Expected completion:** End of day (Sept 22)
- **Impact:** Ready for video production

**Additional QA Engineer Status:**
- Retesting all execution methods (third iteration)
- Internal server endpoint error identified for Pump Swap tokens
- Backend engineer actively fixing
- Full regression testing from ground up
- Covering all edge cases

**Perpetuals Development:**
- Charts implementation finishing
- Limit orders testing next
- Frontend work expected complete by end of week

**Advanced Orders:**
- Deploying to dev environment same day

**Remaining Major Components:**
- Wallet manager
- Partner program (referral)
- Portfolio (two tables + one chart)

**Timeline:** 00:00:00 - 00:07:43

---

### UX Testing Framework Setup

**Zen's Request:**
- More direct involvement in product UX testing
- Daily product usage testing
- Skip early-stage QA (not resource-efficient for him)
- Focus on user-side experience as approaching launch
- Experience with this process in past product launches

**Testing Environment:**

**Lucas Recommendation:**
- **Dev URL** as primary testing environment
- Initial testing and iteration on dev
- Production for stable versions (end-user environment)

**Communication Channel Setup:**

**Proposed Structure:**
- Dedicated Slack testing channel
- **Members:** Zen, Greg, Nji, Martin, Lucas
- **Purpose:** Report findings and issues
- Resource allocation coordination
- User-focused communication
- Can expand membership as needed

**Timeline to Start:** Tomorrow (Sept 23)

**Timeline:** 00:07:43 - 00:09:14

---

### Account Access Management

**Chef Account Whitelist:**

**Login Methods Available (5 total):**
- Social login (already implemented)
- Telegram
- Google
- Twitter
- Apple
- Solana wallet (doesn't require whitelist)

**Process:**
1. Whitelist Telegram handle for "chef"
2. Initial login via Telegram
3. Link account with backup methods (Google, Twitter, Apple, Solana wallet)
4. Flexibility to use multiple authentication methods

**Zen's Choice:**
- Username (Telegram) for now
- Plan to add Solana account later

**Timeline:** 00:09:14 - 00:10:49

---

### Remaining Blockers and Infrastructure

**Current Blockers (from Friday discussion):**

1. **GitHub Plan Update**
   - Needed for custom URL deployment
   - **Resolution:** Lucas will cover costs, bill in next invoice
   - Avoids issues on Zen's side

2. **Hyperliquid Accounts**
   - Required for referral code creation
   - **Status:** Zen traveling, will handle this week
   - **Owner:** Zen

3. **Social Accounts**
   - Twitter account
   - Discord account
   - **Status:** Greg reaching out to contacts at Bul

4. **DNS Configuration**
   - For custom URL via Nji console
   - End-stage work item

**Chart Enhancements:**
- More timeframes being added
- Frontend engineer currently implementing

**Timeline:** 00:10:49 - 00:13:34

---

### Long-term QA Strategy

**Zen's Concerns:**
- Initial QA quality issues concerning
- Need for continuous QA resource, not just beta phase
- Parallel workload management: new features + existing bugs
- Post-launch scenario: Telegram/Discord user complaints + bug fixes + new development

**Lucas's Response - Permanent QA Solution:**

**Recognition:**
- Cooking has become bigger than initially anticipated
- Single QA engineer insufficient for product scope

**Commitment:**
- **Additional dedicated QA resource** allocated
- **Permanent assignment** (not temporary for beta)
- Cooking expected to continue growing
- Constant deployment anticipated

**Infrastructure Plan:**
- **Dedicated staging environment** (pre-production)
- Continuously test latest versions and builds
- Validate before production deployment
- Support active user base

**Rationale:** Product will only get bigger, more moving parts, ongoing deployment needs

**Timeline:** 00:13:34 - end

---

## Action Items

| Owner | Action | Deadline | Status |
|-------|--------|----------|--------|
| Lucas | Create dedicated Slack testing channel (Zen, Greg, Nji, Martin, Lucas) | ASAP | Committed |
| Lucas | Whitelist Chef Telegram username | Before Sept 23 | Committed |
| Lucas | Cover GitHub plan costs and add to next invoice | Next billing cycle | Committed |
| Lucas | Allocate permanent additional QA resource | Ongoing | Committed |
| Lucas | Plan dedicated staging environment setup | TBD | Committed |
| Zen | Provide Chef Telegram username for whitelist | Sept 22 | Pending |
| Zen | Create Hyperliquid accounts for referral codes | This week | Committed |
| Greg | Reach out to Bul contacts for Twitter/Discord accounts | Ongoing | In Progress |

## Technical Details

### Testing Infrastructure
- **Primary Environment:** Dev URL
- **Production Use:** Stable versions only
- **Communication:** Dedicated Slack channel
- **Access Control:** Whitelist-based for social logins

### QA Resources
- **Current:** 2 QA engineers (1 original + 1 recent addition)
- **Future:** Permanent dual-QA model
- **Testing Approach:** Full regression, edge case coverage
- **Infrastructure:** Staging environment for continuous validation

### Authentication Architecture
- **Methods:** 5 login options (Telegram, Google, Twitter, Apple, Solana wallet)
- **Whitelist Required:** All except Solana wallet
- **Account Linking:** Multiple backup methods supported
- **Flexibility:** Users can link multiple auth methods

### Development Status
| Component | Status | Target |
|-----------|--------|--------|
| Chart Filters | Testing complete | Same day |
| Market Cap Calculations | Fix in progress | Same day |
| Outlier Handling | Solution implemented | Same day |
| Perpetuals Charts | Finishing | End of week |
| Perpetuals Limit Orders | Testing next | End of week |
| Advanced Orders | Deploying to dev | Same day |
| Wallet Manager | In progress | TBD |
| Partner Program | In progress | TBD |
| Portfolio | In progress | TBD |

## Meeting Conclusion

**Duration:** 00:18:13
**Next Steps:** UX testing begins tomorrow (Sept 23) with Zen using dev environment and dedicated Slack channel

---

## Transcript Highlights

### Development Progress (00:00:00)
```
Lucas: "We are finishing the testing for the filter on the on the token on the
chart bars. Uh weve identified the the reason for the outliers. And we are as
well implementing a fix for the market cap and liquidity calculation error. We
expect to have all of that done by end of day today."
```

### UX Testing Setup (00:09:14)
```
Zen: "I want to involve myself more in the testing of the product UX um and
just in general on a day today just using the product... I've done this many
times um in the past usually around this stage as well as we're closing in on
launch."

Lucas: "Right now the best place for us to to test uh and iterate and
everything would be dev because that is the the go-to place... What we could
do is make a dedicated testing uh testing channel on on Slack with you Greg N
Martin and I. So we can we can uh loop everyone involved in everything and
allocate resources accordingly."
```

### Authentication Options (00:10:49)
```
Lucas: "At the moment we have five uh five methods for you to login... we have
the social login already done. So what we will do is uh wi list the the handle
the telegram handle for chef. With that you will be able to login if you want
to uh to link your login account with another fallback method like a Google
account, Twitter, Apple or whatever or Solana wallet."
```

### Long-term QA Commitment (00:13:34 - end)
```
Zen: "The additional QA resource if you notice an impact on it perhaps that's
um something that Ratherlabs needs to provide going forward to make sure that
the delivery is a lot better and a lot faster... There needs to be a way where
we're fight we're building, you know, new features and at the same time we're
dealing with existing bugs and existing user complaints or user issues."

Lucas: "We had we had only one one QA working on the product and I recognized
that cooking has become a bigger product that we initially anticipated for for
one engineer for one QA engineer. So we will be allocating an extra dedicated
resource for for testing purposes... This is so I'm talking about moving forward
because to be to be quite honest I don't expect cooking to be anything else
rather than bigger... we are thinking about a dedicated staging environment like
a preprodu or something like that where we can actively test the latest versions."
```

## Notes
- Transition from pure development to user-focused testing phase
- Recognition that product scope has exceeded initial estimates
- Permanent infrastructure improvements (QA, staging) being established
- Collaborative testing approach with executive involvement
- Multiple authentication methods provide user flexibility and redundancy
