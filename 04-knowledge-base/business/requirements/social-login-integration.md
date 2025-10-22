---
title: Social Login Integration
type: feature-specification
status: active
priority: high
created: 2025-06-28
date: 2025-10-21
updated: 2025-10-21
tags: [authentication, login, turnkey, social-auth, user-experience, auth0, oauth]
related:
  - "[[mobile-app-prd]]"
  - "[[settings-feature]]"
  - "[[platform-vision-requirements]]"
source-decisions:
  - ADR-102: Auth0 for Social Authentication (2025-08-01)
  - ADR-400: Security Password for Wallet Operations
  - ADR-501: Turnkey for Wallet Management
---

# Social Login Integration

## Overview

In order to lower the access barrier for new potential users, and allow Cooking to catch a wider market share, we will integrate Turnkey's expanded capabilities for authentication.

## Objectives

- Reduce friction in user registration
- Increase market share by supporting multiple auth methods
- Provide fallback access strategies
- Enhance account security through multiple authentication options

## Supported Authentication Methods

### For New Users

New users should be able to register into the platform by choosing to sign up through:

1. **Google Mail**
2. **Apple ID**
3. **Twitter Account**
4. **Telegram**
5. **Solana Wallet**

### For Existing Users

Existing users should be able to link their accounts with other login methodologies for fallback access strategies.

## Authentication Architecture

### Passwordless Design

It is important to understand that these methodologies are **devoid of passwords** since all submit to an external oracle for authenticating identity.

**Security Implications**:
- No password to forget or reset
- Reduced attack surface (no password database)
- Dependency on external authentication providers
- Requires additional security layers

### Enhanced Security

This is why we promote the use of:
- **Passkeys**: For enhanced security
- **Secondary login methodologies**: For account recovery and fallback access

## Future Enhancements

Eventually we will expand security into passkey as well to further protect Cooking trader's accounts.

### Passkey Integration (Planned)

- WebAuthn/FIDO2 standard support
- Biometric authentication
- Hardware key support
- Enhanced phishing protection

## Integration Providers

### Auth0 - Authentication Platform

**Technology**: Auth0 (Implemented August 2025)
- **Purpose**: Managed authentication platform for all social login and user authentication
- **Features**:
  - Universal Login (hosted login page)
  - OAuth 2.0 / OpenID Connect support for all providers
  - Session management and token handling
  - Custom callback for Turnkey wallet creation
  - Multi-factor authentication support
  - Cross-platform support (web and mobile SDKs)
- **Cost Savings**: $96,000 first-year savings vs. in-house implementation
- **Security**: Enterprise-grade authentication infrastructure
- **Uptime**: 99.99% SLA for authentication services

### Turnkey - Wallet Management

**Technology**: Turnkey (Integrated with Auth0)
- **Purpose**: Non-custodial wallet creation and transaction signing
- **Integration**: Custom Auth0 callback triggers Turnkey wallet creation after successful social authentication
- **Multi-chain Support**: Solana + EVM chains (for Hyperliquid)
- **User Experience**: Seamless onboarding without seed phrase management
- **Cost Savings**: $250,000-$500,000 vs. in-house wallet infrastructure development

## User Flows

### New User Registration

1. User visits registration page
2. User selects preferred authentication method
3. User redirected to external provider (Google, Apple, Twitter, Telegram) or connects wallet
4. Provider validates identity
5. User redirected back to Cooking
6. Account created and user logged in

### Linking Additional Methods (Existing Users)

1. User navigates to Settings > Account > Login Methodologies
2. User views currently linked methods
3. User selects "Add Login Method"
4. User chooses new provider
5. Provider validates identity
6. New method linked to existing account

### Account Recovery

1. User attempts login with primary method (unavailable)
2. User selects "Use different method"
3. User authenticates with linked secondary method
4. Access granted to account

## Security Considerations

### Multi-Method Authentication

- **Primary Method**: Initial registration method
- **Secondary Methods**: Linked fallback options
- **Recommendation**: Users should link at least 2 methods

### Account Takeover Prevention

- Email verification for method linking
- Security password required for sensitive operations
- Audit log of authentication events
- Anomaly detection for unusual login patterns

### Provider Security

- Rely on OAuth 2.0 / OpenID Connect standards
- No storage of provider credentials
- Token-based authentication
- Automatic token refresh

## Technical Implementation

### Provider Configuration

**Google**:
- OAuth 2.0 integration
- Scopes: email, profile

**Apple ID**:
- Sign in with Apple
- Email relay support (optional)

**Twitter**:
- OAuth 2.0 integration
- Scopes: users.read, tweet.read

**Telegram**:
- Telegram Login Widget
- Bot integration for verification

**Solana Wallet**:
- Wallet adapter integration
- Message signing for verification
- Support for major wallets (Phantom, Solflare, etc.)

### Turnkey Integration

- Unified authentication flow
- Provider abstraction layer
- Secure token management
- Cross-platform support (web + mobile)

## User Experience

### Registration Flow

- Clear presentation of all options
- Visual branding for each provider
- "Continue with..." buttons
- Fallback to wallet connection

### Account Linking

- Easy-to-access settings interface
- Visual indication of linked methods
- One-click linking process
- Confirmation notifications

### Error Handling

- Clear error messages for failed authentications
- Guidance for resolution
- Alternative method suggestions
- Support contact information

## Privacy Considerations

- Minimal data collection from providers
- Clear privacy policy communication
- User consent for data usage
- GDPR/CCPA compliance

## Monitoring and Analytics

Track key metrics:
- Registration method distribution
- Login success rates by provider
- Account linking adoption
- Authentication failure reasons
- Provider availability/downtime

---

## Implementation Status

**Status**: ✅ Active - Deployed with October 17, 2025 beta launch
**Priority**: High - Core user acquisition and onboarding feature

### Implementation Timeline

**August 2025**: ✅ Complete
- Auth0 integration configured
- All social providers (Google, Apple, Twitter, Telegram, Solana Wallet) implemented
- Custom callback for Turnkey wallet creation
- Session management and token handling
- Universal Login UI customized with Cooking branding

**September-October 2025**: ✅ Complete
- Account linking functionality in Settings
- Cross-platform testing (web + mobile)
- Error handling and fallback flows
- Successfully deployed for October 17 beta launch

### Current Features

✅ **Implemented**:
- Twitter, Google, Apple, Telegram, Solana Wallet authentication
- Auth0 Universal Login with custom branding
- Turnkey wallet automatic creation on first login
- Account linking for multiple authentication methods
- Cross-platform support (web and mobile)
- Session management and automatic token refresh
- 95% registration completion rate (vs. 20-30% with wallet-connection only)

🔄 **Future Enhancements**:
- Passkey/WebAuthn support
- Additional social providers as needed
- Enhanced MFA options

### Key Metrics

- **Registration Completion**: 95% (vs. 20-30% wallet-connection baseline)
- **Cost Savings**: $96,000/year vs. in-house implementation
- **Uptime**: 99.99% (Auth0 SLA)
- **Time to First Login**: < 30 seconds average

### Technical References

- See [ADR-102: Auth0 for Social Authentication](../../02-decisions/2025-08-auth0-social-authentication.md) for detailed implementation architecture and decision rationale
- See [ADR-501: Turnkey for Wallet Management](../../02-decisions/2025-07-04-turnkey-wallet-management.md) for wallet integration details
