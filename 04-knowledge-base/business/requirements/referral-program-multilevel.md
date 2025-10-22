---
title: Referral Program v2 - Multilevel System
type: feature-specification
status: active
priority: high
created: 2025-04-17
date: 2025-10-21
updated: 2025-10-21
tags: [referral-program, acquisition, commission, multi-level, affiliate]
related:
  - "[[referral-program-invite-codes]]"
  - "[[backoffice-platform]]"
  - "[[platform-vision-requirements]]"
  - "[[ADR-200-multilevel-referral-program]]"
  - "[[ADR-201-closed-beta-referral-only-access]]"
source-decisions:
  - ADR-200: Multilevel Referral Program Structure (2025-08-13)
  - ADR-201: Closed Beta via Referral-Only Access (2025-10-13)
---

# Referral Program v2 - Multilevel System

## Overview

In an effort to attract more users and engage with the masses, Cooking.gg will implement a multilevel system on its referral program, allowing the initial referrer to gain a higher commission based on the fees paid by second and third layer referred users stemming from their own referrals (first layer).

---

## Key Objectives

- **Reward high-performing affiliates** for their influence and trading activity
- **Encourage distribution** via multi-tier referral commissions
- **Reduce barriers** for new users through trading fee discounts
- **Align incentives** to support long-term, high-volume engagement

---

## Affiliate Structure

### Level Definitions

- **Level Zero**: Cooking Trader, a.k.a. 'Referrer' or 'Affiliate'
- **Level One**: Traders that joined the Referral Program using the Referrer's Invite Code
- **Level Two**: Traders that joined the Referral Program using Level One's Invite Code
- **Level Three**: Traders that joined the Referral Program using Level Two's Invite Code

### Referral Tree Example

```
Level Zero (Referrer)
  ├── Level One (Direct Referral)
  │     ├── Level Two (Indirect Referral)
  │     │     └── Level Three (Indirect Referral)
  │     └── Level Two (Indirect Referral)
  └── Level One (Direct Referral)
        └── Level Two (Indirect Referral)
```

---

## Fee Discount for Referrals

### Benefit for New Users

Users that join Cooking using an Invite Code receive a **10% discount** on the applied fees when trading **forever**.

**Example**:
- Standard fee: 1%
- Referral discount: 10% of 1% = 0.1%
- Effective fee for referral: 0.9%

---

## Commission Rates

**All commissions are payable to Level Zero (Referrer).**

### 1. Base Commission

Calculated on the **historical traded volume of Level One** (direct referrals).

Commission is taken on the **1% fee Cooking charges users** from every orderSize.
- Example: 1 SOL traded equals 0.01 SOL fee

**Rate**:
- **$0 to $99,999.99** → **30% commission**

### 2. Performance-Based Scaling

Calculated on the **30-day total traded volume of Level One**.

**Important**: If requirements aren't met it will **reset to Base Commission**.

**Rates**:
- **$100,000 to $499,999.99** → **35% commission**
- **$500,000 to $1,999,999.99** → **40% commission**
- **$2,000,000+** → **45% commission**

### 3. Own Volume Incentive

Calculated on the **30-day total traded volume of Level Zero** (the referrer's own trading).

**Important**: If requirements aren't met it will reset.

**Bonus**:
- **Total Own Traded Volume > $50,000 (30 days)** → **+5% bonus** on top of allocated commission tier

### 4. Tiered Downline Commissions

Payable to Level Zero from indirect referrals:

- **Level Two** → **3%** of their trading fee
- **Level Three** → **2%** of their trading fee

---

## Maximum Possible Commission

### Maximum: 55% Total Commission

**Breakdown**:
- **45%** from Performance-Based Scaling (Level One)
- **+5%** from Own Volume Incentive
- **+3%** from Level Two
- **+2%** from Level Three

### Example Calculation

**Scenario**:
- Level One: $2.5M volume (30 days) → 45% commission
- Level Zero: $60K own volume (30 days) → +5% bonus
- Level Two: $100K volume → 3% commission
- Level Three: $50K volume → 2% commission

**Fees Generated**:
- Level One: $2,500,000 * 1% = $25,000 (after discount)
- Level Two: $100,000 * 1% = $1,000 (after discount)
- Level Three: $50,000 * 1% = $500 (after discount)

**Commission Earned by Level Zero**:
- From Level One: $25,000 * 50% (45% + 5%) = $12,500
- From Level Two: $1,000 * 3% = $30
- From Level Three: $500 * 2% = $10
- **Total: $12,540**

---

## Configuration & Management

### Backend Configuration

These percentages are expected to be set through the **backend**, not editable through the interface initially.

### Future Enhancement

Eventually we aim to enable a customization functionality in the [Backoffice](backoffice-platform.md), allowing administrators to:
- Adjust commission rates
- Create promotional tiers
- Set custom commission structures for specific users/cohorts

---

## Payout Structure

### Commission Calculation
- Commissions are calculated in **real-time**

### Rewards Distribution
- Rewards are **credited to Level Zero's active wallet**
- Minimum claim threshold may apply (to reduce transaction costs)

### Account Deletion Handling
- Should a user delete their account, the **referral tree will remain the same**
- Their commissions become **un-claimable**
- Effectively 'paid' to Cooking

---

## Dashboard and Tracking

### Referrer Dashboard (Level Zero)

Level Zero can view and manage:

#### Referral Overview
- **Number of Level One referrals** and their traded volume
- **Volume and commissions** for Level Two and Three
- Visual referral tree

#### Earnings Management
- **Total unclaimed rewards** (claimable balance)
- **Claim rewards** button
- **Claimed rewards history**
- **Cumulative lifetime earnings**

#### Performance Metrics
- **Current commission rate** and tier
- **Eligible bonuses** (own volume incentive)
- Progress toward next tier
- **Referrals trading fee discount value** (total savings provided to referrals)

### Dashboard UI Example

```
┌──────────────────────────────────────────────────────────────┐
│ Referral Dashboard                                           │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ Your Invite Code: CRYPTO2025       [📋 Copy] [🔗 Share]    │
│                                                              │
│ ─────────────────────────────────────────────────────────── │
│                                                              │
│ Earnings Summary                                             │
│ ┌────────────────────────────────────────────────────────┐  │
││ Unclaimed Rewards: 12.54 SOL                          ││  │
││ [Claim Now]                                            ││  │
││                                                         ││  │
││ Lifetime Earnings: 145.23 SOL                          ││  │
││ This Month: 12.54 SOL                                  ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
│ ─────────────────────────────────────────────────────────── │
│                                                              │
│ Commission Breakdown (30 days)                               │
│                                                              │
│ Level One (Direct Referrals)                                 │
│ • Referrals: 15                                              │
│ • Trading Volume: $2,500,000                                 │
│ • Commission Rate: 50% (45% tier + 5% own volume)           │
│ • Earned: 12.50 SOL                                          │
│                                                              │
│ Level Two (Indirect Referrals)                               │
│ • Referrals: 8                                               │
│ • Trading Volume: $100,000                                   │
│ • Commission Rate: 3%                                        │
│ • Earned: 0.03 SOL                                           │
│                                                              │
│ Level Three (Indirect Referrals)                             │
│ • Referrals: 3                                               │
│ • Trading Volume: $50,000                                    │
│ • Commission Rate: 2%                                        │
│ • Earned: 0.01 SOL                                           │
│                                                              │
│ ─────────────────────────────────────────────────────────── │
│                                                              │
│ Performance Status                                           │
│ ┌────────────────────────────────────────────────────────┐  │
││ Your Trading Volume (30d): $60,000                     ││  │
││ ✓ Own Volume Bonus Unlocked (+5%)                      ││  │
││                                                         ││  │
││ Level One Volume (30d): $2,500,000                     ││  │
││ Current Tier: 45%                                      ││  │
││ ✓ Maximum tier reached!                                ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
│ [View Referral Tree] [View History] [Share Program]         │
└──────────────────────────────────────────────────────────────┘
```

---

## Technical Implementation

### Database Schema

```sql
CREATE TABLE referral_relationships (
  id BIGINT PRIMARY KEY,
  referrer_id BIGINT,  -- Level Zero
  referral_id BIGINT,  -- User being referred
  level INT,  -- 1, 2, or 3
  created_at TIMESTAMP,
  FOREIGN KEY (referrer_id) REFERENCES users(id),
  FOREIGN KEY (referral_id) REFERENCES users(id)
);

CREATE TABLE referral_commissions (
  id BIGINT PRIMARY KEY,
  referrer_id BIGINT,
  transaction_id BIGINT,
  referral_level INT,  -- 1, 2, or 3
  commission_rate DECIMAL(5,2),  -- e.g., 45.00 for 45%
  commission_amount DECIMAL(18,9),  -- In SOL
  claimed BOOLEAN DEFAULT FALSE,
  claimed_at TIMESTAMP NULL,
  created_at TIMESTAMP
);

CREATE TABLE referral_tiers (
  id BIGINT PRIMARY KEY,
  user_id BIGINT,
  current_tier VARCHAR(20),  -- 'base', 'tier1', 'tier2', 'tier3'
  commission_rate DECIMAL(5,2),
  own_volume_bonus BOOLEAN,
  calculated_at TIMESTAMP,
  valid_until TIMESTAMP  -- 30 days from calculated_at
);
```

### Commission Calculation Service

```pseudo
function calculateCommission(transaction):
  referrer = getReferrer(transaction.user_id)

  if not referrer:
    return 0  # No referral relationship

  # Determine referral level
  level = getReferralLevel(referrer.id, transaction.user_id)

  # Get commission rate based on level
  if level == 1:
    tier = getCurrentTier(referrer.id)
    rate = tier.commission_rate

    # Add own volume bonus if applicable
    if hasOwnVolumeBonus(referrer.id):
      rate += 5

  elif level == 2:
    rate = 3

  elif level == 3:
    rate = 2

  # Calculate commission
  fee = transaction.amount * 0.01  # 1% trading fee
  commission = fee * (rate / 100)

  # Record commission
  recordCommission(referrer.id, transaction.id, level, rate, commission)

  return commission
```

---

## Analytics & Reporting

### Track Metrics
- Total referrers (Level Zero users)
- Total referrals by level
- Commission distribution by tier
- Average commission per referrer
- Top performing referrers
- Referral conversion rates
- Cost of acquisition vs. lifetime value

---

## Future Enhancements

### Dynamic Tier System
- Real-time tier updates
- Progress notifications

### Gamification
- Leaderboards
- Badges and achievements
- Special rewards for milestones

### Advanced Analytics
- Referral performance insights
- Optimization recommendations
- Predictive earnings projections

---

## Implementation Timeline

**Phase 1: Custom Codes (August 2025)** - ✅ Complete
- Modal on first login with pre-filled auto-generated code
- User customization capability (one-time update)
- Multiple codes support (alias system)
- Reserved terms list enforcement

**Phase 2: Multilevel Commission Structure (September 2025)** - ✅ Complete
- Transaction fee extraction refactor
- 3-level profit allocation logic
- Commission calculation engine
- Real-time attribution tracking
- Dashboard visualization

**Phase 3: Beta Launch (October 17, 2025)** - ✅ Complete
- Referral caps per code (25-50 slots during closed beta)
- Closed beta via referral-only access mechanism
- Commission monitoring and validation
- Successfully deployed with October 17 beta launch

## Current Status

**Status**: ✅ Active - Deployed with October 17, 2025 beta launch
**Priority**: High - Core growth and acquisition feature
**Implementation**: Complete across web and mobile platforms
**Performance**: Integrated with closed beta referral-only access model

## Related Documentation

- See [ADR-200](../../02-decisions/2025-08-13-multilevel-referral-program.md) for the architectural decision rationale
- See [ADR-201](../../02-decisions/2025-08-11-closed-beta-referral-only-access.md) for closed beta integration
- See [referral-program-invite-codes.md](referral-program-invite-codes.md) for custom code implementation details
