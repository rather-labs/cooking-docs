---
title: Cooking Mobile App - Product Requirements Document
type: requirements
date: 2025-10-02
updated: 2025-10-21
tags:
  - mobile-app
  - product-requirements
  - ios-development
  - user-experience
  - non-crypto-natives
  - biometric-authentication
summary: Comprehensive PRD for Cooking mobile app targeting non-crypto natives with simplified trading experience, including biometric authentication for trading security
source-decisions:
  - ADR-102: Auth0 for Social Authentication
  - ADR-400: Security Password for Wallet Operations
  - ADR-401: Biometric Authentication Required for Mobile Trading (2025-10-01)
---

# Cooking Mobile App - Product Requirements Document

## Overview

Cooking serves as the definitive entry point for non-crypto natives into the cryptocurrency ecosystem. This comprehensive mobile application provides an intuitive, educational platform that transforms complex cryptocurrency trading into an accessible experience for newcomers.

---

## 1. Sign Up, Log In, and Home

### Rationale

Establish Cooking as the primary gateway for non-crypto users by providing seamless authentication, integrated referral programs, and comprehensive token discovery. The Home screen functions as an educational hub with real-time token streams organized into intuitive categories.

### Technical Considerations

#### Authentication and User Onboarding

- Leverage existing Turnkey service integration for passwordless authentication
- Support: Google Mail, Apple ID, Twitter, Telegram, Solana Wallet
- Terms and Conditions acceptance with cross-platform persistence
- Account linking for multiple authentication methods per user
- Automatic single Solana wallet creation on first login

#### Integrated Referral System

- Mandatory referral choice after T&C acceptance
- Invite code validation with real-time feedback
- Post-registration referral joining via User Settings
- Integration with webapp referral infrastructure

#### Home Screen Token Discovery

- Real-time WebSocket connections for continuous updates
- Dynamic categorization:
  - **Stove**: Just Prepped, Simmering Nicely, Plated Up
  - **Specials**: Trending, Gainers, Losers
- Toggle and pause/resume capabilities
- Global search by name or contract address

#### Quick Buy Implementation

- Kitchen-exclusive functionality
- SOL as quote asset
- Default: 0.01 SOL order, 0.008 SOL priority fee, 30% slippage
- Immediate execution with balance validation
- Cross-platform preference synchronization

### Acceptance Criteria

#### A. User Authentication and Onboarding Flow

**A.1. Authentication Methods**
- Passwordless registration via all supported methods
- Automatic Solana wallet creation
- Additional authentication method linking

**A.2. Terms and Conditions and Referral Integration**
- Mandatory T&C acceptance
- Required referral choice (join or proceed independently)
- Valid invite code requirement for referral joining
- Later access via User Settings > Referral Program

#### B. Home Screen Token Discovery Hub

**B.1. Token Stream Organization**
- Real-time categorized streams
- Toggle between Stove and Specials sections
- Pause/resume functionality

**B.2. Search and Discovery**
- Name or contract address search
- Seamless integration with token stream UI
- Direct navigation to Token Details

#### C. Quick Buy Functionality

**C.1. Kitchen-Exclusive Quick Buy**
- Available only on Home screens
- 0.01 SOL default order size
- Immediate market order execution

**C.2. Configuration**
- Default settings application
- Balance validation
- Clear error messaging
- Immediate portfolio updates

#### D. Token Details Screen Integration

**D.1. Navigation**
- Access from Home stream, search, or wallet
- Essential token information display
- Expanded functionality in separate story

#### E. User Preferences and Settings

**E.1. Display Unit Configuration**
- SOL/USD toggle (display only)
- Priority fees remain in SOL
- Session persistence and webapp sync

**E.2. Settings Menu Integration**
- Dock menu navigation
- Referral Program access
- Invite code entry for existing users

#### F. Navigation and User Experience

**F.1. Clear Navigation System**
- Persistent location indicators
- iOS design standards
- Context-maintaining navigation paths

**F.2. Real-time Updates and Performance**
- Automatic data refresh
- Immediate operation reflection
- Graceful network error handling

### Permissions

**All Authenticated Users**:
- Register with any authentication method
- Make referral choices
- Access complete Home screen features
- Execute Quick Buy transactions
- Navigate to Token Details
- Customize UI preferences
- Access User Settings

---

## 2. Wallet Management and Portfolio Overview

### Rationale

Provide non-crypto natives with comprehensive yet simplified wallet management that serves as both portfolio overview and secure funds management. Single Solana wallet per user eliminates complexity while ensuring security through mandatory Security Password.

### Technical Considerations

#### Wallet Infrastructure and Security

- Integration with webapp wallet systems
- Automatic Solana wallet generation
- Security Password implementation
- Backend encryption and validation

#### Address Book and Withdrawal Systems

- Whitelisted address CRUD operations
- Solana address validation
- Transaction signing with Security Password
- Blockchain transaction broadcasting

#### Seed Phrase Security

- One-time export with permanent disable
- Secure generation and retrieval
- Security audit trail

#### Portfolio and Balance Management

- Real-time token balance aggregation
- PnL calculation engine
- SOL valuation and conversion
- Token metadata integration

### Acceptance Criteria

#### A. Security Password Management

**A.1. Mandatory Setup**
- Required before wallet access
- Persistent modal until completion
- Security waiver acknowledgment

**A.2. Requirements and Storage**
- Strong password requirements
- Encrypted backend storage
- Cross-platform sharing

**A.3. Validation**
- Required for sensitive operations
- Graceful failure handling

#### B. SOL Deposit Functionality

**B.1. Deposit Interface**
- Modal with address display
- QR code generation
- One-tap address copying

#### C. SOL Withdrawal Functionality

**C.1. Withdrawal Form**
- Address book or external selection
- Asset and amount specification
- Balance validation

**C.2. Security Validation**
- External transfers require password
- Pre-approved addresses exempt
- Transaction logging

#### D. Address Book Management

**D.1. Adding Withdraw Wallets**
- Name and address requirements
- Address validation
- Security Password verification
- Unlimited entries

**D.2. Management Operations**
- Name updates
- Address copying
- Deletion capability
- Immediate reflection

#### E. Seed Phrase Export

**E.1. One-Time Access**
- Single export allowed
- Permanent disable after use
- Clear disclaimers

**E.2. Security Verification**
- Password requirement
- Risk acknowledgment
- Non-copyable display

#### F. Portfolio and Positions Display

**F.1. Holdings Overview**
- Complete token list (Solana first)
- Images, names, valuations
- Automatic updates

**F.2. Performance Tracking**
- Minute-based PnL
- Color-coded gains/losses
- Direct Token Details navigation

### Permissions

**All Authenticated Users**:
- Must create Security Password
- View complete portfolio
- Deposit SOL
- Withdraw to any address
- Manage address book
- One-time seed phrase export
- Navigate to Token Details

---

## 3. OnRamper Integration for Fiat On-Ramp

### Rationale

Enable non-crypto initiates to seamlessly enter the web3/Solana ecosystem through familiar fiat-to-crypto onboarding, lowering barriers and increasing acquisition.

### Technical Considerations

- Onramper native widget via iframe
- Design coordination with Figma specs
- API error handling
- Connection issue mapping
- Widget theming
- Transaction logging
- Essentials plan scope (onramp only)

### Acceptance Criteria

#### Widget Access and Integration

- Wallet manager button access
- Iframe widget opening
- Cooking theme matching

#### Transaction Flow

- Onramper handles interactions
- Connection error messaging
- Automatic wallet redirect
- Result viewing

#### Transaction Tracking and History

- Attempt registration
- Status capture
- History appearance
- Internal reporting

#### Error Handling

- Connection issue mapping
- Internal payment error handling
- Clear status feedback

### Permissions

- **New Users**: First-time wallet funding
- **Existing Users**: Additional funding
- **All Users**: Transaction history viewing

---

## 4. Biometric Authentication for Trading Security

### Rationale

Protect user funds and ensure secure trading operations by requiring biometric authentication (Face ID/Touch ID on iOS, fingerprint/face unlock on Android) for all financial transactions. This industry-standard security measure protects against unauthorized access if device is lost, stolen, or accessed without permission.

### Technical Considerations

#### Biometric Integration
- Platform-native biometric systems (iOS: Face ID/Touch ID, Android: BiometricPrompt)
- React Native Biometrics library for cross-platform support
- Hardware-backed key protection (iOS Secure Enclave, Android KeyStore)
- Fallback to security password for devices without biometrics

#### Grace Period for User Experience
- 5-minute grace period after successful authentication
- Reduces friction for active trading sessions
- Grace period resets on app backgrounding, device lock, or logout

#### Protected Operations
- All trading operations (market, limit, TWAP, DCA, VWAP, custom orders)
- Wallet withdrawals to external addresses
- Sensitive wallet operations (seed phrase export, private key viewing)
- Security password changes

### Acceptance Criteria

#### A. Biometric Authentication for Trading

**A.1. Authentication Flow**
- Biometric prompt appears before trade execution
- Native platform UI (Face ID/Touch ID/Fingerprint/Face Unlock)
- Clear operation description in prompt
- Cancel option available

**A.2. Grace Period**
- 5-minute window after successful authentication
- No re-authentication needed for subsequent trades within period
- Grace period invalidates on app background, device lock, or logout
- User can configure grace period duration (1, 5, 15, or 30 minutes)

**A.3. Fallback Authentication**
- Security password prompt for devices without biometrics
- Security password prompt on biometric failure
- Same grace period applies after password authentication

#### B. Protected Operations Requiring Biometric

**B.1. Trading Operations**
- Market buy/sell orders
- Limit orders with TP/SL
- Advanced trading methods (TWAP, DCA, VWAP, custom orders)
- Order cancellations

**B.2. Wallet Operations**
- Withdrawals to external addresses
- Bridge operations
- Seed phrase exports
- Private key viewing
- Security password updates

**B.3. Read-Only Operations (No Authentication Required)**
- Portfolio viewing
- Token discovery browsing
- Price chart viewing
- Transaction history viewing
- Settings access

#### C. Error Handling and Fallback

**C.1. Biometric Failures**
- Clear error messages for failed authentication
- Option to retry biometric
- Option to use security password instead
- Lockout handling (too many failed attempts)

**C.2. Device Compatibility**
- Automatic detection of biometric availability
- Graceful fallback to password on older devices
- Support for users who disable biometrics

#### D. User Configuration

**D.1. Settings Options**
- Enable/disable biometric authentication
- Grace period duration selection
- Biometric requirement toggles per operation type
- Clear explanation of security benefits

### Permissions

**All Authenticated Users**:
- Must authenticate via biometric or security password for trades
- Can configure grace period duration
- Can choose fallback authentication method
- Protected from unauthorized trades if device accessed

### Implementation Reference

See [ADR-401: Biometric Authentication Required for Mobile Trading](../../02-decisions/2025-10-01-biometric-authentication-mobile.md) for detailed implementation architecture, code examples, and security considerations.

---

## 5. Token Details Screen and Trading Operations

### Rationale

Provide non-crypto natives with comprehensive yet intuitive token analysis and trading interface serving as both educational tool and functional trading hub.

### Technical Considerations

#### Token Data Integration

- Real-time blockchain API integration
- Historical data aggregation (1m, 5m, 30m, 1h)
- Social links validation
- User-specific data aggregation

#### Trading Engine Integration

- Solana DEX protocol integration
- Limit order management system
- Real-time gas fee estimation
- Slippage protection mechanisms

#### Balance and Validation Systems

- Real-time balance retrieval
- 0.000001 SOL minimum validation
- Insufficient balance detection
- Pre-transaction cost estimation

### Acceptance Criteria

#### A. Token Information Display

**A.1. Basic Token Data**
- Name, address, age, protocol
- Real-time price updates
- Prominent balance display

**A.2. Performance and Market Data**
- Multi-timeframe PnL (1m, 5m, 30m, 1h)
- Holdings, sales, operations totals
- Volume split by buys/sells
- Unique address counts

**A.3. Additional Information**
- Clickable social links
- Automatic data refresh

#### B. User Balance and Portfolio Information

**B.1. Balance Display**
- SOL and token balances
- Automatic transaction updates
- Clear trading capacity

**B.2. Trading History**
- Chronological order (newest first)
- All operation types included
- Visual status distinction
- Detailed entry information

#### C. Market Trading Functionality

**C.1. Market Order Configuration**
- BUY/SELL direction
- Base/Quote asset assignment
- Minimum 0.000001 SOL validation

**C.2. Market Order Parameters**
- Automatic gas retrieval
- 0.008 SOL priority fee default
- 30% slippage default
- Total cost estimation

**C.3. Execution and Validation**
- Balance validation
- Clear error messaging
- Immediate execution
- Failure logging

#### D. Limit Trading Functionality

**D.1. Limit Order Configuration**
- BUY/SELL direction
- Market Cap OR Price triggers
- Directional trigger system

**D.2. Limit Order Parameters**
- Size validation matching market
- Variable gas calculation
- Standard fee defaults
- Trigger value validation

**D.3. Optional Parameters**
- TTL in minutes/hours/days
- BUY orders: TP and SL
- SELL orders: SL only
- Post-execution activation

**D.4. Order Management**
- Cancellation capability
- Status alerts
- History tracking

### Permissions

**All Authenticated Users**:
- Access Token Details
- View comprehensive information
- Execute Market swaps
- Create/manage Limit orders
- Modify trading parameters
- View balance and costs
- Access trading history
- Receive status notifications

---

## 6. Comprehensive User Settings and Account Management

### Rationale

Provide streamlined account management through centralized User Settings accessible via dock navigation and contextual quick settings, with mandatory Security Password for fund protection and optional biometric authentication configuration.

### Technical Considerations

#### Security Password Infrastructure

- Client-side generation
- Backend encryption
- Cross-platform validation
- Update flow implementation

#### Settings Navigation Architecture

- Dock navigation integration
- Quick Settings in Kitchen
- Contextual access points
- Future-ready architecture

#### Referral Program Integration

- Consolidated referral system
- Invite code uniqueness validation
- Circular referral prevention
- Cross-platform synchronization

### Acceptance Criteria

#### A. Security Password Management

**A.1. Mandatory Setup**
- Required for wallet access
- Cannot be skipped
- Webapp password retention
- Complexity validation

**A.2. Protection**
- Blocks address copying
- Required for critical operations
- Complete operation blocking

**A.3. Updates**
- Current password verification
- New password confirmation
- Importance acknowledgment

#### B. Fee Settings and Trading Preferences

**B.1. Fee Configuration**
- Priority fee setting (0.008 SOL default)
- Slippage configuration (30% default)
- Greater than zero validation
- Dual access points

**B.2. Persistence**
- Cross-session retention
- Platform synchronization

#### C. Currency Display Management

**C.1. Currency Switch**
- SOL/USD toggle
- Visual presentation only
- Operation input unchanged
- Dual access points

**C.2. Display Scope**
- Rewards and volume display
- Fees remain in SOL

#### D. Comprehensive Referral Program

**D.1. Referrer Capabilities**
- 6-12 character custom codes
- One-time creation
- Link/code copying
- SOL/USD rewards display

**D.2. Referral Management**
- Referral list viewing
- Volume tracking
- Reward claiming

**D.3. Joining as Referral**
- Existing user entry
- Irreversibility acknowledgment
- Circular prevention
- Webapp synchronization

#### E. Account Deletion and Data Management

**E.1. Deletion Process**
- User-initiated deletion
- Irreversibility acknowledgment
- Security Password requirement
- 7-day grace period

**E.2. Grace Period and Recovery**
- Cancellation option
- Password verification
- No recovery after expiration

**E.3. Referral Impact**
- Relationship maintenance
- Unclaimable rewards
- Persistent benefits

#### F. Help and Documentation Access

**F.1. Documentation Integration**
- Settings > Help access
- Browser redirect

### Permissions

**All Authenticated Users**:
- Security Password generation required
- Fee configuration access
- Currency display switching
- Invite code creation
- Referral joining
- Reward viewing/claiming
- Password updates
- Account deletion initiation
- Documentation access

## Implementation Priorities

### Phase 1: Core Infrastructure ✅ Complete
1. Authentication and onboarding (Auth0 social login)
2. Security Password implementation
3. Basic wallet functionality
4. Home screen token discovery

### Phase 2: Trading Features ✅ Complete
1. Quick Buy functionality
2. Market orders
3. Basic limit orders
4. Token Details screens
5. **Biometric authentication for trading operations** (ADR-401, October 2025)

### Phase 3: Advanced Features ✅ Complete
1. Referral program
2. Address book management
3. Fiat on-ramp integration (Onramper)
4. Advanced trading options

### Phase 4: Polish and Optimization ✅ Complete (October 17, 2025 Beta Launch)
1. Performance optimization
2. Enhanced error handling
3. UI/UX refinements
4. Cross-platform synchronization
5. Biometric authentication grace period tuning

## Success Metrics

- New user conversion rate
- Time to first trade
- User retention (D1, D7, D30)
- Trading volume per user
- Referral program participation
- Security incident rate
- App Store ratings

## Cross-References

- Related to: [[platform-user-documentation]] - Comprehensive user guide
- Related to: [[beta-release-q3-2025]] - Beta release features
- Related to: [[gitbook-index]] - Documentation structure