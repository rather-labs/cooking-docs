---
title: Mobile App - Wallet Management
type: feature-specification
status: in-development
priority: critical
created: 2025-07-01
date: 2025-10-20
updated: 2025-10-20
tags: [mobile, wallet, security, portfolio, deposits, withdrawals]
related:
  - "[[mobile-signup-login-home]]"
  - "[[security-password-wallet-manager]]"
  - "[[mobile-settings]]"
---

# Mobile App - Wallet Management

## Overview

The mobile Cooking wallet should serve as:
- **Portfolio view** for understanding whole exposure to spot positions
- **Pathway to acquire SOL** easily
- **Wallet management** interface

## Simplification for Target Audience

To expedite delivery and suit the target audience (non-initiate web3 users), we will only enable them to create a **single Solana wallet** - the one automatically created when they first login.

---

## Security Password Requirement

### Mandatory Creation

All Cooking users must have a **Security Password enabled** in order to make use of the Wallet.

### Enforcement

In case they haven't generated it, users will be met with a **persistent modal requesting said generation**.

### Required For

- Accessing the deposit address
- Viewing seed phrase
- Generation of withdraw wallets
- Execution of any transfer

### Security Waiver

Users must **acknowledge a security waiver** before generating their security password, emphasizing the importance of keeping it secure.

### Storage & Validation

- Password stored securely and encrypted in the backend
- Validated before any critical operations
- Follows requirements already defined for webapp feature
- **Cross-platform**: If generated on web, works on mobile and vice versa

---

## Core Wallet Functions

### Deposit SOL

**Purpose**: Receive SOL from external sources

**Flow**:
1. User taps "Deposit SOL"
2. Modal displays:
   - Wallet's Solana address (with copy button)
   - QR code for deposits
   - Instructions

```
┌─────────────────────────────────────────┐
│ Deposit SOL                        [✕]  │
├─────────────────────────────────────────┤
│                                         │
│ Send SOL to this address:               │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ abc123...xyz789        [📋 Copy]    ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
││                                     ││ │
││         [QR CODE]                   ││ │
││                                     ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ⚠️ Only send Solana (SOL) to this      │
│ address. Other tokens may be lost.     │
│                                         │
│ [Done]                                  │
└─────────────────────────────────────────┘
```

### Withdraw SOL

**Purpose**: Send SOL/tokens to external addresses

**Flow**:
1. User taps "Withdraw SOL"
2. Form displays:
   - Select wallet from address book OR one-time address
   - Recipient address field
   - Asset selector (Solana pre-selected, any held coin could be sent)
   - Amount field (cannot exceed available balance)
3. **Security requirement**: Sign with security password (for external wallets)

```
┌─────────────────────────────────────────┐
│ Withdraw                           [✕]  │
├─────────────────────────────────────────┤
│                                         │
│ Send To                                 │
│ ○ Address Book                          │
│ ● New Address                           │
│                                         │
│ Recipient Address                       │
│ [____________________________] [📋]    │
│                                         │
│ Asset                                   │
│ [SOL                          ▼]       │
│ Balance: 5.23 SOL                       │
│                                         │
│ Amount                                  │
│ [____________________________] [Max]   │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ Network Fee: 0.000005 SOL           ││ │
││ You will send: 1.0 SOL              ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ [Continue]                              │
│                                         │
└─────────────────────────────────────────┘
```

---

## Address Book Management

### Overview

Cooking users have a list of **whitelisted addresses** ready and pre-approved to send funds to easily.

### Adding a Withdraw Wallet

**Flow**:
1. Access 'Add Withdraw Wallet' form
2. Fill fields:
   - Name (label for the wallet)
   - Solana wallet address
3. **Sign with security password** to save

### Address Book Actions

For each pre-approved wallet:
- **Update name**: Edit the label
- **Copy address**: Quick copy to clipboard
- **Delete**: Remove from list (requires security password)

**Effect of Deletion**: Removed from the list of accepted wallets to withdraw funds to

---

## Seed Phrase Export

### One-Time Only Export

Though not mandatory, the user will be able to export their cooking wallet's seed phrase **only one time**.

**After export**:
- User becomes sole custodian of recovery key
- Takes full responsibility for keeping it safe
- Cannot export again through Cooking UI

### Access Requirements

1. **Security password** required
2. **Acknowledgment** of importance of this action
3. **Security waiver** acceptance

**Warning Display**:
```
⚠️ CRITICAL SECURITY WARNING

Your seed phrase is the master key to your wallet.

• Write it down on paper only
• Never store digitally
• Never share with anyone
• Anyone with this phrase can access your funds
• You can only view this ONCE

This action cannot be undone.

[I Understand - Show Seed Phrase]
```

---

## Portfolio / Positions View

### Display

The mobile app will display a list of all the user's token holdings.

**Sort Order**: Solana always first, then other tokens

### Token Card Display

Each item contains:
- Token image/logo
- Token name and symbol
- Current valuation in SOL
- PnL for the last minute
- Total amount held (expressed in token and in SOL)

```
┌─────────────────────────────────────────┐
│ Portfolio                               │
│ Total Value: 5.45 SOL ($229.45)         │
├─────────────────────────────────────────┤
│                                         │
│ ┌─────────────────────────────────────┐ │
││ ◎ SOL                               ││ │
││ 3.25 SOL                            ││ │
││ $136.88                             ││ │
││ +0.2% (1m)                          ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ 🐓 ROOSTER                          ││ │
││ 54,421 ROOSTER                      ││ │
││ 0.201 SOL ($8.45)                   ││ │
││ +5.2% (1m)  PnL: +10.8%             ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ 🦊 DOGE                             ││ │
││ 125,000 DOGE                        ││ │
││ 2.02 SOL ($85.12)                   ││ │
││ -1.2% (1m)  PnL: -5.3%              ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ [+ Buy SOL]                             │
│                                         │
└─────────────────────────────────────────┘
```

---

## Mobile UI Considerations

### Touch Optimization
- Large buttons for common actions
- Swipe gestures for quick actions
- Easy access to security-critical functions

### Quick Actions
- Swipe left on token: Sell
- Swipe right on token: Buy more
- Long press: View details

### Visual Hierarchy
- Portfolio value prominent at top
- Color-coded PnL (green/red)
- Clear separation between assets

---

## Security Best Practices

### Biometric Integration (Future)
- Use Face ID / Touch ID for security password
- Quick access while maintaining security

### Session Management
- Auto-lock after inactivity
- Require re-authentication for sensitive ops

### Warnings & Education
- Clear warnings before irreversible actions
- Educational tooltips for first-time users
- Link to security best practices guide

---

## Technical Considerations

### Performance
- Fast portfolio valuation updates
- Efficient balance queries
- Cached token metadata

### Offline Capability
- Display last known balances
- Queue withdrawals for when online
- Clear offline indicators

### Error Handling
- Network errors gracefully handled
- Transaction failure recovery
- Clear error messages with next steps

---

## Analytics & Tracking

### Key Metrics
- Portfolio view frequency
- Deposit/withdraw success rates
- Address book usage
- Seed phrase export rate
- Security password creation rate
- Average time to complete actions

---

**Status**: In development
**Priority**: Critical - Core wallet functionality
**Platform**: iOS & Android
**Dependencies**: Security password system, Turnkey integration, blockchain node access
**Next Steps**:
1. Design wallet UI/UX
2. Implement security password flow
3. Build deposit/withdraw interfaces
4. Create address book management
5. Implement seed phrase export (one-time)
6. Add portfolio view with real-time updates
7. Test security flows thoroughly
8. Beta test with target users
