---
title: Stakeholder Requirements & Conversations
type: requirements
date: 2025-04-07
tags:
  - stakeholder-management
  - product-requirements
  - admin-panel
  - roadmap
  - prioritization
summary: Comprehensive documentation of stakeholder conversations, requirements, and feature prioritization decisions
---

# Stakeholder Requirements & Conversations

## April 7, 2025 - Initial Requirements

### Immediate Deliverables
- Time estimates needed for:
  - New pricing algorithm
  - Referral Program v2

### Key Decisions
- Admin Panel prioritization session scheduled
- Requirement for comprehensive audits before production
- Cannot have a month of QA before production release
- **Hard deadline**: End of Q2 for production delivery
- **Required for production**: Admin Panel and Referral Program v2

### Security Focus
- Naji emphasized strong focus on application security
- Fund security as top priority

## April 8, 2025 - Admin Panel Prioritization

### Admin Panel Overview

**Purpose**: Internal backoffice for Cooking team (business + support)

**Primary Objectives**:
1. Provide insights on user/token/order behavior to business team
2. Enable dynamic fee adjustment at multiple levels
3. Support existing users

**User Roles**:
- Business team role
- Support team role
- Roles should have separated access (implement role-based access control)

**Security Requirements**:
- Greg emphasizes strong security layer for access
- URL should not be easily accessible
- Consider 2FA or passkey authentication

### Prioritized Features

#### High Priority (Must Have)

1. **Authentication System**
   - Secure login with role management
   - 2FA/Passkey implementation

2. **User Management - Basic**
   - User CRUD operations (Create, Read, Update, Delete)
   - Basic user administration

3. **Fee Management - Basic**
   - Custom fee at platform level
   - Custom fee at order level
   - Custom fee at token level

4. **Platform Analytics**
   - Commissions paid tracking
   - Token behavior analysis
   - Order business intelligence (basic scope per documentation)

5. **Support Features**
   - List of deployed contracts by environment (mainnet, testnet)
   - Contract addresses and verification status
   - Upgrade/migration tools for proxy patterns
   - Real-time event logs (Swaps, Settlements, Errors)
   - Chain-specific configurations:
     - Gas optimization settings
     - Relayer options
     - Oracle fallback rules

6. **User Management - Advanced**
   - Create user cohorts through 'Invite Code'
   - Assign custom fees to users/cohorts
   - Assign commissions to users/cohorts

#### Future Features

- **Notification System**
  - Telegram notifications from backoffice
  - Scalable to other communication channels

- **User Feedback**
  - Feedback form integration

## April 21, 2025 - Q2 Roadmap Review

### Strategic Shifts

**Backoffice Deprioritization**
- Zain indicates backoffice should be last priority
- Preference for feature development first
- Integration to backoffice comes after feature completion

### Vision Evolution

**Non-Crypto Native Focus**
- Product should be suitable for users without existing wallets
- Modularization to hide non-priority information
- Simplified flows for new users

### Timeline Update

**Production Release Postponed**
- New target: **September (End of Q3)**
- No specific date within September confirmed

### Pending Decisions

Features requiring prioritization:
- Referral Program v2 ([[C301 - Referral Program v2 - Multilevel]])
- Market Cap Percentage Variation Algorithm ([[C201 - Market Cap Percentage Variation Algorithm]])

### Discussed Verticals

#### Multi-Chain Support
- **Objective**: Enable flexible transactions on high-volume networks
- Generate commissions from cross-chain activity

#### Perpetuals Trading
- **Recommendation**: HyperLiquid (per Naji and Greg)
- Requires technical discovery and assessment

#### Wallet Integrations
- Import Solana wallets from other venues (Phantom, Rabby, Rainbow, Trust)
- EVM support to follow
- **Technical Considerations**:
  - Handle entryPrice in PnL calculations for imported wallets with existing balances
  - Permission management for transaction signing

#### Security Enhancements
- 2FA/Passkey for account security
- Password reset functionality evaluation
- User parameter configuration capabilities

#### Authentication Expansion
- Current: Telegram (Web3-friendly but not optimal for non-natives)
- Planned: X (Twitter), Apple ID, Gmail, email, phone, wallet direct

#### UI Modifications (The Kitchen)
- Hide/expand columns
- Create, save, delete custom filters based on token information

### Additional Considerations

#### User Onboarding
- Critical first interactions for B2C success
- Evaluate current process for both crypto-native and non-native users
- Focus on adoption curve optimization

#### Help Center
- Initial: GitBook linked in UI
- Future: Evaluate scaling to other support methods

#### Technical Refactoring
- Services not designed for dynamic alteration (e.g., fees)
- Allocate resources for refactoring before backoffice construction

### Long-term Verticals (Unprioritized)

1. **Yield Offering**
   - Integration through Jupiter
   - Leverage ecosystem for additional user options
   - Commission on yield generation

2. **Native Mobile App**
   - OS not specified
   - Low-friction entry for everyday users
   - Simplified environment with core web terminal features

3. **SDK**
   - Scope undefined

4. **Backoffice**
   - Scope to be defined

## April 22, 2025 - Development Team Meeting

**Participant**: Ali Khalouf (Frontend Developer)

*Note: Meeting details incomplete in original document*

## Cross-References

- Related to: [[roadmap-q2-q3-2025]] - Detailed roadmap based on these requirements
- Related to: [[beta-release-q3-2025]] - Beta release specifications
- Related to: [[referral-program-v2-multilevel]] - Detailed referral program specifications
- Related to: [[market-cap-percentage-variation-algorithm]] - Algorithm requirements