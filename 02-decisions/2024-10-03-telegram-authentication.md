---
title: Use Telegram for User Authentication
type: decision-record
decision-id: ADR-001
date: 2024-10-03
status: accepted
owner: Project Lead
stakeholders: Development Team, UX/UI Designer, Backend Engineer
tags: [authentication, telegram, user-experience, onboarding]
summary: |
  Decision to use Telegram authentication as the primary login method for Cooking.gg,
  providing seamless onboarding and automatic custodial wallet creation for users.
related-docs:
  - ../01-foundation/project-charter.md
  - 2024-10-03-custodial-wallets.md
---

# Use Telegram for User Authentication

## Context and Problem Statement
Cooking.gg needs a user authentication system that is simple, secure, and accessible to both experienced traders and crypto newcomers. Traditional wallet-based authentication creates friction for users unfamiliar with cryptocurrency, while email/password systems add complexity and security concerns.

The platform targets meme token traders who value speed and simplicity, and many are already active in Telegram communities where meme tokens are discussed and promoted.

## Decision
We will use Telegram as the primary authentication method for Cooking.gg. Users will authenticate through their existing Telegram accounts using Telegram's OAuth flow.

**Implementation:**
- "Login with Telegram" button as main entry point
- Redirect to Telegram bot for authentication
- Return to app with login link for seamless access
- Automatic custodial wallet creation upon first login
- One-time login page shown only on first access

## Rationale
1. **Familiar Interface** - Most target users already have Telegram accounts and are comfortable with the platform
2. **Reduced Friction** - No need to create new accounts or remember passwords
3. **Fast Onboarding** - Single-click authentication gets users trading quickly
4. **Security** - Telegram handles authentication security, reducing attack surface
5. **Bot Integration** - Enables future Telegram Trading Bot functionality with unified authentication
6. **Community Alignment** - Telegram is where meme token communities gather, creating natural ecosystem fit

## Consequences

### Positive
- Extremely low friction onboarding - users can start trading in seconds
- No password management or email verification needed
- Natural integration with planned Telegram Trading Bot
- Familiar UX for target audience already using Telegram
- Reduced security responsibilities (Telegram handles auth)
- Enables easy notification system via Telegram

### Negative
- Dependence on Telegram platform and API availability
- Users without Telegram accounts must create one first (small barrier)
- Less control over authentication flow compared to custom solution
- Potential privacy concerns for users wanting platform anonymity
- Rate limiting constraints from Telegram API

### Neutral
- Telegram account required (most target users already have)
- Authentication tied to single platform
- May need backup authentication method in future

## Alternatives Considered

### Option 1: Traditional Wallet Connection (MetaMask, Phantom)
**Pros:**
- Standard in crypto applications
- Users maintain full control
- No dependency on third-party platform

**Cons:**
- High friction for crypto newcomers
- Requires users to have existing wallet
- Each transaction requires signature
- Slower trading experience

**Why Rejected:** Conflicts with goal of accessibility for newcomers and fast trading experience. Custodial wallet approach provides better UX.

### Option 2: Email/Password Authentication
**Pros:**
- Universal - everyone has email
- Full control over auth system
- No third-party dependencies

**Cons:**
- Adds registration friction
- Password management burden
- Email verification delays
- Security responsibilities (password storage, reset flows)
- Doesn't integrate with Telegram bot plans

**Why Rejected:** Adds unnecessary complexity and doesn't support Telegram bot integration, which is a key differentiator.

### Option 3: Social OAuth (Google, Twitter, etc.)
**Pros:**
- Low friction like Telegram
- Multiple options for users
- Widely adopted

**Cons:**
- Doesn't align with crypto community norms
- No integration with Telegram bot
- Multiple providers to maintain
- Less alignment with target user base

**Why Rejected:** Telegram is more aligned with crypto/meme token communities and enables bot integration.

## Implementation Notes
1. Use Telegram Login Widget or Telegram Bot API for authentication
2. Store Telegram user ID as primary identifier
3. Generate custodial wallet automatically on first login
4. Implement session management with secure tokens
5. Plan for Telegram bot to share authentication context
6. Consider backup authentication method for future (optional)
7. Implement rate limiting and abuse prevention
8. Handle Telegram API downtime gracefully

**Security Considerations:**
- Validate Telegram authentication tokens server-side
- Implement session expiration and refresh mechanisms
- Store minimal user data from Telegram
- Encrypt sensitive data at rest
- Monitor for suspicious authentication patterns

## References
- Telegram Login Widget Documentation: https://core.telegram.org/widgets/login
- Telegram Bot API: https://core.telegram.org/bots/api
- [Project Charter](../01-foundation/project-charter.md) - User-Friendly Experience objective
- [Custodial Wallet Decision](2024-10-03-custodial-wallets.md) - Complementary authentication approach

## Revision History
- 2024-10-03: Initial decision based on inception document analysis
