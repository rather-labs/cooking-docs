---
title: Security Password in Wallet Manager
type: feature-specification
status: active
priority: critical
created: 2025-05-13
date: 2025-10-21
updated: 2025-10-21
tags: [security, wallet-manager, authentication, private-keys, wallet-operations]
related:
  - "[[settings-feature]]"
  - "[[external-wallet-support]]"
  - "[[mobile-app-prd]]"
source-decisions:
  - ADR-400: Security Password for Wallet Operations (2025-06-06)
  - ADR-401: Biometric Authentication Required for Mobile Trading (2025-10-01)
---

# Security Password in Wallet Manager

## Problem Statement

We've identified certain security and usability concerns that require immediate resolution to help guarantee a good and safe experience for the end-user:

- The importance of keeping private keys secure and, ideally offline
- The impossibility of downloading said keys more than one time
- Guaranteeing that only the owner of the account can generate withdraw wallets
- Guaranteeing that transfers are executed only by the authorized user

## Solution Overview

To address these concerns we will implement certain security features such as a mandatory security password to sign critical operations within the Cooking trading terminal.

## Security Password Requirements

### Creation Process

The security password should be generated through user input whenever they access the Wallet Manager for the first time:

- This procedure should **not be skipped** and should block the user of any interaction with the Wallet Manager until completion
- **Existing users** should not be exempt from this requirement
- These security password should follow best practices regarding **length and complexity**

### Storage and Validation

- Password generated **client-side**
- Encrypted and stored safely in the backend
- Used to validate key operations:
  - Exporting private keys
  - Adding or removing withdraw wallets
  - Signing transfers

### Access Restriction

It is important to note that if the user has not generated the security password, they should not be able to copy the wallet's address, even from the wallet menu selector.

## Security Waiver and Acknowledgment

When exporting private keys, the user should have to acknowledge a security waiver, explicitly manifesting their understanding of:

- The importance of keeping the private keys secure
- The inability to export them more than once

## Wallet Architecture

### Primary Wallet vs Active Wallet

In the future, we plan to use the first wallet's private keys to sign key transactions, allowing high security operations like exporting private keys more than once.

**Key Concepts**:

- **Primary Wallet**: The first wallet created (cannot be archived)
- **Active Wallet**: The currently selected wallet for executing operations
- Users can toggle focus to any available wallet, making it the selected one for executing operations

### Withdraw Wallets

With the addition of this security layer, we will now add the ability to transfer funds outwards to wallets not necessarily listed as Withdraw Wallets.

**Security Model**:
Having the security password barrier guarantees that only those with access to this credential will be able to interact with the transfer feature.

### Adding Withdraw Wallets and Validation

When including a Withdraw Wallet in the address book:

- User will be forced to sign the operation with the security password
- This action represents an acknowledgment and security check of the address
- The address becomes immediately validated upon successful password entry

## Protected Operations

The security password is required for:

1. **Private Key Operations**:
   - Exporting private keys (one-time only)
   - Viewing seed phrases

2. **Wallet Management**:
   - Adding withdraw wallets
   - Removing withdraw wallets
   - Importing external wallets

3. **Transfer Operations**:
   - Signing transfers to new addresses
   - Transferring to non-validated withdraw wallets

## Password Requirements

**Complexity Rules**:
- Minimum 8 characters long
- Include at least one uppercase letter
- Include at least one number
- Include at least one symbol (@&$!#?)

**Security Best Practices**:
- Generated client-side
- Encrypted before transmission
- Stored securely in backend
- Never logged or displayed in plain text

## User Experience Flow

### First-Time Setup

1. User accesses Wallet Manager
2. Modal blocks all interactions
3. User creates security password
4. User confirms password by re-entering
5. User acknowledges security responsibility
6. Access granted to Wallet Manager

### Subsequent Use

1. User attempts protected operation
2. Security password prompt appears
3. User enters password
4. Operation executes if password correct
5. Error message if password incorrect

## Integration Points

- **Settings**: Co-exists with Settings security password creation flow
- **Wallet Manager**: Primary enforcement point
- **Transfer Feature**: Validates all outbound transfers
- **Mobile App**: Shared password across web and mobile

## Security Considerations

- Password reset flow required (future consideration)
- Account recovery mechanism needed
- Brute force protection required
- Session timeout after password entry

## Future Enhancements

- Biometric authentication as alternative
- Hardware key support (YubiKey, etc.)
- Multi-signature wallet support
- Recovery phrase backup for password reset

---

## Implementation Status

**Status**: ✅ Active - Deployed with June 2025 implementation
**Priority**: Critical - Core security feature for wallet operations

### Scope of Protection (ADR-400)

**Wallet Operations Protected**:
1. **Critical Wallet Operations**:
   - Exporting private keys (one-time only)
   - Viewing seed phrases
   - Adding/removing withdraw wallets
   - Importing external wallets

2. **Transfer Operations**:
   - Signing transfers to new addresses (not in withdraw wallet list)
   - Transferring to non-validated withdraw wallets
   - Bridge operations (cross-chain transfers)

3. **Security Configuration**:
   - Updating security password
   - Wallet management operations
   - Account deletion (7-day grace period)

**Operations NOT Requiring Security Password**:
- Trading operations on mobile (use biometric authentication per ADR-401)
- Portfolio viewing
- Read-only wallet operations
- Deposit operations (receiving funds)

### Cross-Platform Implementation

**Web Application**:
- Security password required for all wallet operations
- Client-side hashing before backend transmission
- Session persistence with timeout

**Mobile Application**:
- Biometric authentication (Face ID/Touch ID) for trading operations (ADR-401)
- Security password fallback for devices without biometrics
- Security password required for wallet management operations
- Same encrypted password shared across platforms

### Implementation Timeline

**June 2025**: ✅ Complete
- Mandatory security password creation on first Wallet Manager access
- Backend encryption and storage infrastructure
- Password validation for critical operations
- One-time seed phrase export functionality

**October 2025**: ✅ Complete
- Mobile biometric integration (ADR-401)
- Cross-platform security password synchronization
- Successfully deployed for October 17 beta launch

### Key Metrics

- **Adoption**: 100% (mandatory on first wallet access)
- **User Education**: Security waiver and acknowledgment required
- **Password Complexity**: Enforced (min 8 chars, uppercase, number, symbol)
- **Cross-Platform**: Shared encrypted password between web and mobile

### Technical References

- See [ADR-400: Security Password for Wallet Operations](../../02-decisions/2025-06-06-security-password-wallet.md) for implementation details and security architecture
- See [ADR-401: Biometric Authentication for Mobile Trading](../../02-decisions/2025-10-01-biometric-authentication-mobile.md) for mobile-specific authentication
- See [Mobile App PRD](mobile-app-prd.md) for mobile security password integration
