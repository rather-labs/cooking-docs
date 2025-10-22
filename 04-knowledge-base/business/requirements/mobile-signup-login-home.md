---
title: Mobile App - Sign Up, Login and Home Screen
type: feature-specification
status: in-development
priority: critical
created: 2025-06-30
date: 2025-10-20
updated: 2025-10-20
tags: [mobile, signup, login, home, discovery, ui-ux]
related:
  - "[[mobile-app-prd]]"
  - "[[social-login-integration]]"
  - "[[referral-program-invite-codes]]"
  - "[[mobile-token-details]]"
---

# Mobile App - Sign Up, Login and Home Screen

## Product Vision

Cooking Mobile app should be an **initial stepping stone for non-crypto natives** to start their journey. With this objective in mind we will focus on a **clean UI**, with a **clear navigation system** that makes it obvious where the user is standing at all times.

---

## Authentication

### Social Login Integration

To lower the initial friction for the non-crypto initiate, Cooking will allow sign-up with a plethora of social login methodologies as well as through a Solana Wallet.

**Supported Methods**:
- Google (Gmail)
- Apple ID
- Twitter
- Telegram
- Solana Wallet

**Provider**: Leveraging current integration with **Turnkey**

### Account Linking

Once signed up, all users should be able to **associate their account with another login methodology** in order to further protect their access since these are **passwordless methods**.

**Benefits**:
- Fallback access options
- Enhanced account security
- Multi-device flexibility

---

## Home Screen

### Purpose

The 'Home' screen serves as a **discovering hub** for tokens.

### Token Feed Structure

Users will find themselves with a stream of tokens sorted through **two main sections**:

#### 1. Stove (Lifecycle-Based)

Tokens categorized by their launch lifecycle:

- **Just Prepped**: Tokens just created, newly minted
- **Simmering Nicely**: Gaining traction, near migration point
- **Plated Up**: Completed the bonding curve

#### 2. Specials (Performance-Based)

Tokens categorized by market performance:

- **Trending**: Tokens with the highest trading volume
- **Gainers**: Tokens sorted by price increase percentage
- **Losers**: Tokens sorted by price decrease percentage

### Stream Controls

**Pause/Resume Button**:
- Dedicated button to pause/resume the continuous stream of tokens
- Allows users to review tokens without new ones flooding in

### Discovery Features

#### Search Functionality

Allows users to find tokens through:
- **Token name** (e.g., "ROOSTER")
- **Contract address** (full Solana address)

**Search Access**:
- Prominent search bar at top of Home screen
- Quick access from any screen

---

## Token Details Navigation

### From Home to Details

When clicking each token card, the user should be delivered into a **'Token Details' screen** where they'll be able to gain information regarding:

- Token's name
- Age
- Price history
- Market data
- PnL metrics
- And more (see [mobile-token-details.md](mobile-token-details.md))

---

## Quick Buy Feature

### Overview

Users will be able to execute **market swaps** on tokens right from the token details page by enabling the **'Quick Buy' feature**.

### Configuration

**Default Order Size**:
- User selects a default order size
- **Expressed in Solana**
- This value is used for every Quick Buy execution

**Example**:
- User sets Quick Buy to 0.5 SOL
- Each Quick Buy button press purchases 0.5 SOL worth of the token

### Trading Settings

Users can configure default trading parameters:

#### Priority Fee
- **Expressed in Solana**
- **Default**: 0.008 SOL
- **Validation**: Cannot be equal to or smaller than zero

#### Slippage
- **Expressed as percentage**
- **Default**: 30%
- **Validation**: Cannot be equal to or smaller than zero

---

## Currency Display

### Unit Toggle

Users can change the unit of expression on the UI:

**Options**:
- **Solana (SOL)** - Default
- **USD** - Alternative

**Affects**:
- Price displays
- Market cap
- Volume
- Liquidity
- Portfolio values

**Does NOT Affect**:
- Order size input (always in respective asset)
- Fee displays (shown in SOL)

---

## Referral Program Integration

### Signup Flow

When first signing up, **after accepting the terms and conditions**, users will be met with a choice:

#### Option 1: Join as Referral
- "Do you have an invite code?"
- User enters **Invite Code** from their referrer
- Receives **10% fee discount forever**

#### Option 2: Skip for Now
- User can join without referral
- Can join later through Settings > Referral Program

### Later Joining

For users who skipped during signup:
- Access through **Settings menu**
- Navigate to **Referral Program**
- Enter invite code
- Acknowledge irreversible choice

---

## User Interface Design

### Home Screen Layout

```
┌─────────────────────────────────────────┐
│ 🍳 Cooking          [🔍 Search] [👤]   │
├─────────────────────────────────────────┤
│                                         │
│ ⏸️ Pause Feed                           │
│                                         │
│ ┌───────────────────────────────────┐  │
││ STOVE                             ││  │
││                                   ││  │
││ Just Prepped (12)                 ││  │
││ ┌─────────────────────────────┐   ││  │
│││ 🐓 ROOSTER  $0.0037         │││ ││  │
│││ 2m ago  +5.2%               │││ ││  │
││└─────────────────────────────┘   ││  │
││ ...more tokens...                 ││  │
││                                   ││  │
││ Simmering Nicely (8)              ││  │
││ ...tokens...                      ││  │
││                                   ││  │
││ Plated Up (5)                     ││  │
││ ...tokens...                      ││  │
│└───────────────────────────────────┘  │
│                                         │
│ ┌───────────────────────────────────┐  │
││ SPECIALS                          ││  │
││                                   ││  │
││ Trending (10)                     ││  │
││ ...tokens...                      ││  │
││                                   ││  │
││ Gainers (10)                      ││  │
││ ...tokens...                      ││  │
││                                   ││  │
││ Losers (10)                       ││  │
││ ...tokens...                      ││  │
│└───────────────────────────────────┘  │
│                                         │
│ [🏠 Home] [💼 Wallet] [📊 Activity] [⚙️] │
└─────────────────────────────────────────┘
```

### Signup/Login Screen

```
┌─────────────────────────────────────────┐
│                                         │
│           🍳 Cooking                    │
│                                         │
│     Start Your Crypto Journey           │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ [🔵 Continue with Google]           ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ [🍎 Continue with Apple]            ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ [🐦 Continue with Twitter]          ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ [📱 Continue with Telegram]         ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ ┌─────────────────────────────────────┐ │
││ [👛 Continue with Solana Wallet]    ││ │
│└─────────────────────────────────────┘ │
│                                         │
│ By continuing, you agree to our         │
│ Terms of Service and Privacy Policy     │
│                                         │
└─────────────────────────────────────────┘
```

---

## Navigation Structure

### Bottom Tab Bar

**Primary Navigation**:
- **🏠 Home**: Token discovery feed
- **💼 Wallet**: Portfolio and wallet management
- **📊 Activity**: Trading history and orders
- **⚙️ Settings**: User preferences and account settings

---

## Technical Considerations

### Performance
- Lazy loading for token feed
- Virtual scrolling for large lists
- Image caching for token logos

### Real-time Updates
- WebSocket for live price updates
- Feed refresh on pull-down
- Background refresh when app returns to foreground

### Offline Support
- Cache last viewed tokens
- Queue actions for online execution
- Clear offline state indicators

---

## Analytics & Tracking

### Key Metrics
- Signup method distribution
- Home feed engagement (time spent, scrolls)
- Token clicks from each category
- Search usage and queries
- Quick Buy adoption rate
- Referral code entry success rate

---

## Future Enhancements

### Personalization
- Customizable feed preferences
- Follow specific tokens
- Price alerts

### Advanced Discovery
- Filters for feed (market cap range, age, etc.)
- Sorting options
- Watchlist integration

### Social Features
- Share tokens with friends
- Community sentiment indicators

---

**Status**: In development
**Priority**: Critical - Foundation of mobile experience
**Platform**: iOS & Android
**Dependencies**: Turnkey integration, token indexer, referral system
**Next Steps**:
1. Finalize UI/UX designs
2. Implement authentication flows
3. Build token feed with categorization
4. Integrate search functionality
5. Implement Quick Buy feature
6. Add referral signup flow
7. Test on multiple devices
8. Beta testing with target users
