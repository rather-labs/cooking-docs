---
title: On-Ramp Solution Research and Integration
type: research
status: completed
priority: high
created: 2025-07-15
updated: 2025-10-20
date: 2025-10-20
tags: [onramp, offramp, fiat-to-crypto, crossmint, onramper, mobile, kyc]
related:
  - "[[mobile-app-prd]]"
  - "[[mobile-wallet]]"
decision: Onramper selected for initial integration
---

# On-Ramp Solution Research and Integration

## Executive Summary

To ensure that non-crypto initiates can look to Cooking as their first step into their web3/Solana journey, we researched and compared two potential ramp solutions: **Crossmint** and **Onramper**. This document presents the research findings, comparison, and final integration decision.

**Final Decision**: Onramper selected for initial mobile integration using their widget approach.

---

## Research: Crossmint

### Overview
Crossmint specializes in streamlined crypto purchasing experiences with their flagship "Checkout" functionality.

### Key Features

#### Checkout (No-KYC)
Supports functionality that allows users to execute a market swap from fiat to memecoin using:
- Google Wallet
- Apple Wallet
- Debit Card
- Credit Card

**KYC Requirement**: Not required for users initially. Certain transactions will require it when flagged as potential fraud.

**Unknown**: Available protocols for memecoin purchase (requires follow-up)

#### Geographic Restrictions
Per documentation, they are not operative in non-sanctioned OFAC regions. **Requires clarification**: Does this affect users not located in US soil as well?

#### Onramp Functionality
- Requires KYC for all users
- Payment methodologies shared with 'Checkout'
- Only method to top up SOL for Gas payments and general purpose on Cooking
- KYC handled by Crossmint
- AML certifications handled by Crossmint

### Integration Options

- **Embeddable Widget**: Custom theming possibilities
- **Headless API**: For personalized experience

### Limitations & Unknowns

**Offramp**:
- Doesn't document the ability to offramp Solana into fiat again, though it is advertised (requires follow-up)

**Fee Structure**:
- No documentation available regarding fee commissions that can be charged on top of transactions

**Pricing**:
- All features seem to be included in an 'Enterprise' plan
- Price is unknown
- **Requires contacting sales** for more information

### Advantages
✅ Unique no-KYC checkout experience
✅ AML certification (critical for App Store approval)
✅ Mobile-optimized
✅ Embeddable widget with theming

### Disadvantages
❌ Poor documentation
❌ No clear offramp support
❌ Unknown pricing (Enterprise plan)
❌ Unknown fee structure
❌ Geographic restrictions unclear
❌ Protocol support unclear

---

## Research: Onramper

### Overview
Onramper is an **onramp aggregator** that supports both onramp and offramp processes.

**Coverage**:
- 25+ onramps
- 7+ offramps

### Pricing Plans

#### Essentials Plan
- **Cost**: $2,000 USD annually
- **Includes**: 6 onramps
- **Does NOT include**: Offramp support

#### Premium Plan
- **Cost**: Requires conversation with sales team
- **Includes**: Offramp support + additional features

### KYC Approach

**Provider-Dependent**: KYC is dependent on the aggregator recommended for each operation.

**Smart Routing**:
- Not all aggregators have the same requirements
- Onramper recommends the best exchange rate AND best KYC experience (lowest friction)
- For smaller-value transactions, extensive KYC often not required (faster and simpler swaps)
- **Repeat users** sent to onramps they are already KYC'd with

**Official Statement**:
> "When a transaction occurs, our routing engine quickly assesses your customer's profile to identify the optimal onramp considering success rates, fees, and ease of transaction completion."

### Fee Structure

**Commission Capability**: Onramper allows developers to add a commission fee on top of each operation.

**Cost Savings**: Per their documentation, their "fee-based routing saves users 2.52%" which can be considered when assessing margins to charge for each transaction.

### Integration Options

Onramper provides both widgets and API setups.

**Widget Methods**:
1. **Button with link**: Opens browser with checkout experience (on/off ramp) hosted on Onramper
2. **Embedded iFrame**: Within the product itself, feels like part of the product

**Theming**: Widget has theming capabilities

### Geographic Restrictions

Documentation states there may be **certain restrictions due to geographic location**, though doesn't specifically state out-of-scope regions.

**Assumption**: Inherited limitation of each aggregated ramp
**Expected**: Changing provider should suffice (requires follow-up)

### Compliance

**AML Certifications**: Documentation doesn't state anything regarding AML certifications.
- Known to be a must for getting App Store approval
- **Requires follow-up**

### Legal Requirements

Documentation states that to start integration, Cooking must present:
- Documentation backing it as a **legally registered entity** already incorporated
- **Cannot be** in Gaming or Gambling industries

### Advantages
✅ Comprehensive service (25+ onramps, 7+ offramps)
✅ Clear pricing ($2,000/year Essentials)
✅ Revenue sharing (commission fee capabilities)
✅ Smart KYC routing (lower friction)
✅ Cost savings (2.52% on average)
✅ Easy integration (widget)
✅ Theming support

### Disadvantages
❌ AML certification status unclear (requires follow-up)
❌ Geographic restrictions (inherited from providers)
❌ Essentials plan lacks offramp support
❌ Premium plan requires sales consultation

---

## Solution Comparison Matrix

| Feature | Crossmint | Onramper |
|---------|-----------|----------|
| **No-KYC Purchase** | ✅ Checkout feature | ⚠️ Limited (small amounts) |
| **Onramp Support** | ✅ With KYC | ✅ 25+ providers |
| **Offramp Support** | ❌ Not documented | ✅ 7+ providers (Premium) |
| **AML Certification** | ✅ Documented | ❓ Requires clarification |
| **Mobile Optimization** | ✅ Designed for mobile | ✅ Widget & API options |
| **Annual Cost** | ❓ Enterprise pricing | $2,000+ (tiered) |
| **Geographic Coverage** | ⚠️ OFAC restrictions | ✅ Multi-provider coverage |
| **Integration Complexity** | Low-Medium | Low |
| **Provider Redundancy** | ❌ Single provider | ✅ 25+ providers |
| **Revenue Sharing** | ❓ Undocumented | ✅ Clear commission model |
| **Documentation Quality** | ❌ Poor | ✅ Good |

---

## Conclusion & Decision

### Analysis

Though Crossmint provides the unique Checkout experience without KYC requirement, and this is a valuable addition to the mobile product, their documentation is **lacking in many key areas**:
- They do not clearly document offramp support
- Accessing pricing information requires contact with a sales team, which could **delay schedules**

Onramper provides:
- **Proven** onramp and offramp solutions
- **Clear commission strategy** that Cooking can leverage
- **Easy-to-integrate widgets**
- **Comprehensive provider coverage**

### Missing Information Requiring Follow-up

**Crossmint**:
- Enterprise plan pricing and fee structure
- Memecoin protocol support details
- Offramp capabilities confirmation
- Geographic restrictions impact on target markets

**Onramper**:
- AML certification status for App Store compliance
- Geographic restrictions for EU, North America, and GCC regions

### Final Recommendation

**SELECTED: Onramper** for initial mobile implementation

**Rationale**:
1. Clear pricing structure ($2,000/year)
2. Comprehensive documentation
3. Provider redundancy (25+ options)
4. Lower implementation risk
5. Faster time to market

---

## Integration Plan - Onramper

### Selected Approach

**Widget Integration** (iFrame method)

### Implementation Details

#### Deployment
- Widget deployed on an **iframe**
- Launched from a button on the **wallet manager screen**

#### User Flow
1. User navigates to Wallet Manager
2. User taps "Buy SOL" button
3. Onramper widget opens in iframe
4. **Onramper's logic takes over**, handling:
   - KYC process
   - Payment processing
   - Edge cases
   - Errors

#### Tracking & Analytics
If possible, Cooking should register:
- Attempts to top up wallet using onramp
- Resulting status (success, error, etc.)
- **Source**: Should come back from Onramper's API

#### Initial Scope
For this initial phase:
- **Will NOT be adding** offramp capability
- **Scoping**: Features included in Essentials plan ($2,000/year)

#### Theming
We expect to **theme the widget** to match Cooking's look-and-feel

### Why Widget Approach?

For mobile implementation, we recommend integrating the widget approach initially because:

1. **End-to-end flow** already designed and implemented by the provider
2. **Checkout and KYC processes** handled by Onramper
3. Theming can be applied to achieve Cooking's look and feel
4. **Faster implementation** while gathering additional information
5. **Lower maintenance** burden on Cooking team

**Trade-off**: Form functionality determined by provider, but overall experience still branded

---

## Future Considerations

### Potential Upgrades

**Upgrade to Premium Plan**:
- Enables offramp support (7+ providers)
- Allows users to convert crypto back to fiat
- Completes the full on/off ramp cycle

**Custom Integration**:
- If widget limitations become apparent
- Use API for full customization
- More development effort required

### Competitive Analysis

Continue monitoring:
- **Crossmint** pricing and feature updates
- New entrants in ramp aggregation space
- User feedback on Onramper experience

### Metrics to Track

**User Adoption**:
- % of users attempting to buy SOL
- Conversion rate (attempt → success)
- Average transaction size

**User Experience**:
- Time to complete onramp
- Drop-off points
- Error rates by provider

**Revenue**:
- Commission earned per transaction
- Total volume through onramp
- Cost per acquisition via onramp

---

## Technical Requirements

### Pre-Integration Checklist

- [ ] Legal entity documentation prepared
- [ ] Business registration verified
- [ ] Industry compliance verified (not Gaming/Gambling)
- [ ] Onramper account created
- [ ] API keys obtained
- [ ] Theming configuration prepared

### Integration Steps

1. **Account Setup**:
   - Submit legal documentation to Onramper
   - Await account approval
   - Receive API credentials

2. **Widget Configuration**:
   - Configure widget theme (colors, fonts)
   - Set commission rates
   - Configure supported currencies

3. **Mobile Implementation**:
   - Add iframe support in Wallet Manager
   - Implement button trigger
   - Handle widget callbacks

4. **Testing**:
   - Test across various amounts
   - Test with different payment methods
   - Verify commission calculations
   - Test error handling

5. **Launch**:
   - Soft launch to beta users
   - Monitor metrics
   - Gather feedback
   - Iterate and optimize

---

**Status**: Research complete, integration in progress
**Decision**: Onramper selected
**Priority**: High - Enables fiat on-ramp for mobile
**Next Steps**: Complete legal documentation, begin Onramper integration, implement widget in Wallet Manager
