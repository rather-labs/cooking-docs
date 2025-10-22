---
title: Spot Fee Customization
type: feature-specification
status: planned
priority: high
created: 2025-09-23
date: 2025-10-20
updated: 2025-10-20
tags: [fees, backoffice, business-rules, incentives]
related:
  - "[[backoffice-platform]]"
  - "[[platform-vision-requirements]]"
---

# Spot Fee Customization

## Overview

The focus of this initiative is to allow the Cooking business team to leverage different incentives through modification of trading parameters such as the cooking fee that every transaction has set.

## Scope

This manipulation should be done on the **backoffice** and be extensive to **all venues** (desktop and mobile).

---

## Base Fee Structure

### Default Configuration

**All spot transactions will have an adjustable base fee**, currently set as **1%**.

### Administrative Control

The admin user will have the ability to exclude a specific set of variables from this universe and assign them a different fee parameter which will **not be added to the base fee**.

---

## Fee Customization Rules

### Variable-Based Rules

This set of variables can be declared as:
1. **Stand-alone constant**: Single variable rule
2. **Combination**: Multiple variables combined

### Available Variables

- **Token Contract Address**: Specific token
- **Order Type**: Market, DCA, Limit, TWAP, VWAP, Custom
- **Provider**: Pump.fun, Raydium, etc.
- **Referral Code**: Specific referral code
- **Array of Variables**: Combination of above

---

## Rule Examples

### Single Variable Rules

**Example 1: Order Type**
```
DCA transactions will have a 0.75% fee
```
- Variable: Order Type = DCA
- Fee: 0.75%
- Applies to: All DCA orders regardless of other factors

**Example 2: Provider**
```
Pump.fun tokens will have a 0.5% fee
```
- Variable: Provider = Pump.fun
- Fee: 0.5%
- Applies to: All Pump.fun tokens regardless of order type

### Multi-Variable Rules

**Example 3: Combination**
```
DCA transactions from pump.fun tokens and users signed under 'PROMO2025' referral code will have a 0.5% fee
```
- Variables:
  - Order Type = DCA
  - Provider = Pump.fun
  - Referral Code = PROMO2025
- Fee: 0.5%
- Applies to: Only when ALL conditions are met

---

## Rule Management

### Creation

**Immediate Impact**:
Once the rule is declared, it is expected to **impact immediately** in the platform.

**No Caching Delay**: Rules should apply to next transaction

### Deletion

**Immediate Removal**:
Same happens with its deletion - immediate impact.

**Graceful Handling**: In-progress transactions complete with original fee

---

## Backoffice Interface

### Fee Rules Management Page

```
┌─────────────────────────────────────────────────────────────┐
│ Spot Fee Customization                        [+ New Rule]  │
├─────────────────────────────────────────────────────────────┤
│ Base Fee: [1.0]%                              [Update]      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Active Fee Rules (3)                                        │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐    │
││ Rule #1                                    [Edit] [✕]││    │
││ DCA Orders                                           ││    │
││ Fee: 0.75%                                           ││    │
││ Priority: 1                                          ││    │
││ Created: 2025-09-15                                  ││    │
││ Transactions: 1,242                                  ││    │
│└─────────────────────────────────────────────────────┘    │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐    │
││ Rule #2                                    [Edit] [✕]││    │
││ Provider: Pump.fun                                   ││    │
││ Fee: 0.5%                                            ││    │
││ Priority: 2                                          ││    │
││ Created: 2025-09-20                                  ││    │
││ Transactions: 3,456                                  ││    │
│└─────────────────────────────────────────────────────┘    │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐    │
││ Rule #3                                    [Edit] [✕]││    │
││ DCA + Pump.fun + PROMO2025                           ││    │
││ Fee: 0.5%                                            ││    │
││ Priority: 3                                          ││    │
││ Created: 2025-09-22                                  ││    │
││ Transactions: 89                                     ││    │
│└─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Create/Edit Rule Form

```
┌─────────────────────────────────────────────────────────────┐
│ Create Fee Rule                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Rule Name: [DCA Promotion           ]                      │
│                                                             │
│ Conditions (All must match):                                │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐    │
││ Order Type:      [DCA            ▼]        [Remove] ││    │
│└─────────────────────────────────────────────────────┘    │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐    │
││ Provider:        [Pump.fun       ▼]        [Remove] ││    │
│└─────────────────────────────────────────────────────┘    │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐    │
││ Referral Code:   [PROMO2025      ]         [Remove] ││    │
│└─────────────────────────────────────────────────────┘    │
│                                                             │
│ [+ Add Condition]                                           │
│                                                             │
│ Custom Fee: [0.5]%                                          │
│                                                             │
│ Priority: [3]  (Higher = evaluated first)                   │
│                                                             │
│ [Create Rule]  [Cancel]                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Rule Evaluation Logic

### Priority System

**Order of Evaluation**:
1. Rules evaluated by **priority** (highest first)
2. First matching rule applies
3. If no rule matches, use base fee

**Example Scenario**:

```
Base Fee: 1.0%

Rules:
  Priority 1: Order Type = DCA → 0.75%
  Priority 2: Provider = Pump.fun → 0.5%
  Priority 3: DCA + Pump.fun + PROMO2025 → 0.3%

Transaction: DCA order on Pump.fun with PROMO2025

Evaluation:
  - Check Priority 1: Order Type = DCA ✓ → Apply 0.75%
  - (Stop here, first match found)

Result: 0.75% fee applied
```

### Specificity Consideration (Future)

To make more specific rules take precedence:

**Most specific rule wins** (rule with most conditions):
- 3 conditions > 2 conditions > 1 condition

**Revised Example**:
```
Transaction: DCA order on Pump.fun with PROMO2025

Evaluation:
  - Rule #1: 1 condition (DCA)
  - Rule #2: 1 condition (Pump.fun)
  - Rule #3: 3 conditions (DCA + Pump.fun + PROMO2025)

Result: Rule #3 applies → 0.3% fee
```

---

## Technical Implementation

### Database Schema

```sql
CREATE TABLE fee_rules (
  id BIGINT PRIMARY KEY,
  name VARCHAR(255),
  custom_fee DECIMAL(5,2),
  priority INT,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  created_by_user_id BIGINT
);

CREATE TABLE fee_rule_conditions (
  id BIGINT PRIMARY KEY,
  fee_rule_id BIGINT,
  variable_type VARCHAR(50),  -- 'order_type', 'provider', 'referral_code', 'token_address'
  variable_value VARCHAR(255),
  FOREIGN KEY (fee_rule_id) REFERENCES fee_rules(id)
);

CREATE TABLE fee_rule_audit_log (
  id BIGINT PRIMARY KEY,
  fee_rule_id BIGINT,
  action VARCHAR(50),  -- 'created', 'updated', 'deleted'
  performed_by_user_id BIGINT,
  performed_at TIMESTAMP
);
```

### Fee Calculation API

```pseudo
function calculateFee(transaction):
  rules = fetchActiveRules()  # Ordered by priority DESC

  for rule in rules:
    if evaluateRule(rule, transaction):
      return rule.custom_fee

  return BASE_FEE  # Default 1.0%

function evaluateRule(rule, transaction):
  conditions = rule.conditions

  for condition in conditions:
    if not matchesCondition(condition, transaction):
      return false

  return true  # All conditions matched
```

### Caching Strategy

**To ensure immediate impact**:
- Cache rules in memory
- Invalidate cache on rule create/update/delete
- Broadcast to all application instances (Redis Pub/Sub)

---

## Analytics & Reporting

### Fee Rule Performance

Track per rule:
- Total transactions matched
- Total fee collected
- Total fee waived (compared to base fee)
- ROI (if promotional)

### Dashboard Metrics

```
┌─────────────────────────────────────────────────────────────┐
│ Fee Rule Analytics                                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ DCA Promotion (0.75%)                                       │
│ Transactions: 1,242                                         │
│ Fees Collected: $9,315                                      │
│ Discount Given: $3,105 (-25% vs base)                      │
│                                                             │
│ ┌─────────────────────────────────────────────────────┐    │
││ Daily Transactions                                   ││    │
││ ▁▂▃▅▆▇█▇▆▅▃▂▁                                      ││    │
│└─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## User-Facing Impact

### Fee Display

On order creation, clearly show applied fee:

```
Order Summary:
  Amount: 10 SOL
  Cooking Fee: 0.075 SOL (0.75%)  ✨ DCA Discount Applied
  ...
```

### Transparency

Users should understand:
- What fee they're paying
- Why (if discount applied)
- How to qualify for better fees

---

## Future Enhancements

### Time-Based Rules
- Promotional periods (e.g., weekends)
- Happy hour discounts

### User-Tier Rules
- VIP users get lower fees
- Volume-based tiers

### Dynamic Fees
- Based on market conditions
- Based on token volatility

### A/B Testing
- Test different fee structures
- Measure impact on user behavior

---

**Status**: Planned
**Priority**: High - Business revenue and incentive tool
**Access**: Backoffice only
**Next Steps**:
1. Design backoffice UI for rule management
2. Implement rule evaluation engine
3. Build caching and invalidation system
4. Create analytics dashboard
5. Test rule precedence logic
6. Deploy with initial promotional rules
7. Monitor performance and optimize
