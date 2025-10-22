---
title: Security Password for Wallet Operations
type: decision-record
decision-id: ADR-400
date: 2025-06-06
status: accepted
owner: Lucas Cufré, Martin Aranda
stakeholders: [Lucas Cufré, Martin Aranda, Frontend Team, Backend Team, Security Team]
tags: [security, wallet, authentication, user-experience, password-protection]
summary: |
  Decision to implement mandatory security password for critical wallet operations (seed phrase export, withdraw wallet management, SOL withdrawals) while exempting low-risk internal transfers to balance security with user experience. Password is client-side generated, backend encrypted, and enforced before any interaction with Wallet Manager.
related-docs:
  - ../06-meetings/2025-06/Weekly-Demo-2025-06-06.md
  - ../07-archive/processed-source-docs/2025-10-20-project-documentation/C203 - Password in Wallet Manager.md
  - ../04-knowledge-base/technical/platform-user-documentation.md
---

# Security Password for Wallet Operations

## Context and Problem Statement

Cooking.gg manages user cryptocurrency wallets and private keys through integration with Turnkey wallet management service. This creates several critical security and usability concerns that required immediate resolution:

**Security Requirements:**
1. **Private Key Protection**: Must keep private keys secure and ideally offline
2. **One-Time Export**: Private keys can only be downloaded once (Turnkey limitation)
3. **Authorized Withdrawals**: Guarantee only account owner can create withdraw wallets
4. **Transaction Authorization**: Ensure transfers executed only by authorized user
5. **Access Control**: Prevent unauthorized access to wallet addresses or sensitive operations

**Usability Challenges:**
- Users need to perform frequent internal transfers (between Cooking wallets)
- Security shouldn't create friction for low-risk operations
- Password requirement must be mandatory but not overly burdensome
- Existing users must retroactively comply with new security requirements

**Technical Constraints:**
- Turnkey service: private keys can only be exported once
- Web and mobile platforms require consistent security model
- Client-side password generation for security
- Backend encrypted storage for verification

**Risk Scenarios Without Security Password:**
- Unauthorized seed phrase exports (unrecoverable key compromise)
- Malicious withdraw wallet additions (funds stolen)
- Session hijacking enabling unauthorized transfers
- Social engineering attacks bypassing standard authentication

## Decision

**Implement mandatory security password required for all critical wallet operations, with strategic exemptions for low-risk internal transfers to optimize user experience.**

### Security Password Requirements

**When Password Is Required:**
- **Wallet Manager First Access**: Blocking modal on first interaction - cannot be skipped
- **Seed Phrase Export**: Maximum security for irreversible operation
- **Add/Remove Withdraw Wallets**: Authorization checkpoint for external addresses
- **SOL Withdrawals**: Verification before value leaves platform
- **Update Security Password**: Re-authentication required for password changes
- **Copy Wallet Address**: Even viewing address requires password setup (if not yet created)

**When Password Is NOT Required:**
- **Internal Transfers**: Transfers between Cooking wallets (within platform)
- **Trading Operations**: Spot trading, algorithm execution (separate authorization)
- **Viewing Portfolio**: Read-only operations don't require password

### Password Lifecycle

**Creation (First-Time Users):**
1. User navigates to Wallet Manager
2. Blocking modal appears preventing any wallet interaction
3. User creates password with complexity requirements:
   - Minimum length (8+ characters recommended)
   - Complexity rules (uppercase, lowercase, numbers, symbols)
4. Password generated client-side
5. Encrypted and transmitted to backend
6. Securely stored in backend database
7. User can now access Wallet Manager

**Creation (Existing Users):**
- Retroactive requirement: existing users see same blocking modal
- No exemption - all users must comply before Wallet Manager access
- Ensures consistent security posture across entire user base

**Update Security Password:**
- User initiates update from Wallet Manager settings
- Must provide current password for verification
- Creates new password following same complexity rules
- Old password invalidated immediately
- Update process currently in testing phase

**Storage and Verification:**
- **Client-side**: Password hashed before transmission (never sent plaintext)
- **Backend**: Encrypted storage using industry-standard encryption
- **Verification**: Backend validates encrypted password on protected operations
- **Recovery**: (Parking lot item - not yet implemented)

### Primary Wallet vs Active Wallet Concept

**Future Security Enhancement (Not Yet Implemented):**
- **Primary Wallet**: First wallet created (cannot be archived)
- **Active Wallet**: Currently selected wallet for operations
- **Future Use Case**: Primary wallet's private keys could sign high-security operations
- **Benefit**: Enable multi-export of private keys using primary wallet signature
- **Current State**: Concept documented but not implemented

### Withdraw Wallets Management

**Address Book Security:**
- Adding withdraw wallet requires security password
- Password requirement serves as acknowledgment and security check
- Validated addresses marked immediately (no separate validation step)
- User can now transfer to validated withdraw wallets without re-entering password

**Expanded Withdraw Functionality:**
- Previously: Could only transfer to pre-validated Withdraw Wallets
- Now: Can transfer to any Solana address with security password
- Rationale: Password barrier guarantees authorized access
- Trade-off: More flexibility with maintained security

### Security Waiver for Seed Phrase Export

**One-Time Export Protection:**
- User must explicitly acknowledge security waiver
- Waiver text emphasizes:
  - Importance of keeping private keys secure
  - Private keys can only be exported ONCE (Turnkey limitation)
  - Responsibility for key security after export
- User must actively confirm understanding
- Export proceeds only after acknowledgment

**Why This Matters:**
- Turnkey's one-time export is irreversible security constraint
- Users must understand severity before export
- Legal/liability protection for platform
- Educational moment for security best practices

## Rationale

### Security First, UX Second (But Smartly)

**Critical Operations Protected:**
- Seed phrase export is irreversible and unrecoverable if compromised
- Withdraw wallets enable fund exfiltration - must verify authorization
- SOL withdrawals represent value leaving platform - require verification
- Security password creates defense-in-depth layer beyond session authentication

**Strategic UX Exemption:**
- Internal transfers between Cooking wallets pose minimal risk (funds stay in platform)
- High-frequency operation - password every time creates friction
- Session authentication already validates user identity
- Strategic trade-off: security where it matters, speed where it doesn't

**Team Decision (Weekly Demo 2025-06-06):**
> "Remove password requirement for intra-Cooking wallet transfers to improve UX. Recognizing that these internal operations pose minimal security risk while the removal significantly improves user experience and task completion time."

### Mandatory Setup Prevents Future Vulnerabilities

**Blocking Modal Approach:**
- Users cannot access Wallet Manager without security password
- Prevents scenario where user has wallet but no password protection
- Ensures consistent security posture from first wallet interaction
- Even wallet address viewing requires password setup (prevents information leakage)

**Existing User Retrofit:**
- No grandfather clause - all users must comply
- Prevents two-tier security system (legacy vs. new users)
- Single security audit surface
- Future features can assume security password exists

### Client-Side Generation, Backend Verification

**Security Model:**
- Password never transmitted in plaintext
- Client-side hashing before transmission
- Backend receives only encrypted form
- Backend stores encrypted password for future verification
- Verification happens backend-side for protected operations

**Why This Architecture:**
- Zero-knowledge principle: backend never sees plaintext password
- Prevents backend compromise from exposing passwords
- Client-side hashing reduces attack surface
- Backend verification prevents client-side bypass

### Parking Lot Items (Future Considerations)

**Not Implemented, But Documented:**
- **Password Recovery**: Mechanism for lost passwords (complex - tied to Turnkey)
- **Two-Factor Authentication**: Additional security layer beyond password
- **Biometric Authentication**: Mobile-specific (Face ID, Touch ID) - see ADR-401

**Why Deferred:**
- Beta launch timeline prioritized core functionality
- Password recovery complexity (Turnkey constraints)
- Biometric authentication requires mobile app (separate ADR)
- 2FA adds complexity - assess need based on beta feedback

## Consequences

### Positive

**Security Improvements:**
- Defense-in-depth: Security password layer beyond session authentication
- Prevents unauthorized seed phrase exports (irreversible compromise protection)
- Blocks malicious withdraw wallet additions (fund theft prevention)
- Verifies withdrawal authorization (value exfiltration protection)
- Consistent security posture across all users (no legacy vulnerabilities)

**User Protection:**
- Security waiver educates users on key security importance
- One-time export warning prevents accidental key exposure
- Withdraw wallet verification prevents destination address errors
- Password complexity requirements enforce strong passwords

**Operational Benefits:**
- Audit trail: password verification logged for security operations
- Compliance-ready: demonstrates security controls for financial operations
- Liability protection: users acknowledge risks for critical operations
- Platform reputation: security-first approach builds trust

**Flexibility:**
- Can transfer to any Solana address (not just pre-validated)
- Primary wallet concept enables future advanced features
- Update password mechanism allows users to rotate credentials

### Negative

**User Experience Friction:**
- Additional step before accessing Wallet Manager (blocking modal)
- Must create and remember another password
- No recovery mechanism (currently) - lost password = major issue
- Existing users forced to retroactively create password

**Password Management Burden:**
- Users already manage multiple passwords (platform login, email, etc.)
- Password fatigue reduces likelihood of strong unique passwords
- Users may reuse passwords across services (security risk)
- No password manager integration (users must manually copy)

**Support Burden:**
- Users will forget security passwords
- No recovery mechanism creates support tickets
- Must explain difference between login password and security password
- Confusion over when password is required vs. not required

**Implementation Complexity:**
- Client-side hashing implementation
- Backend encrypted storage and verification
- Update password flow testing
- Retroactive enforcement for existing users
- Multiple verification points throughout application

**Incomplete Features:**
- Password recovery not implemented (critical gap)
- Primary wallet advanced features not implemented (future promise)
- 2FA not available (users may expect it)
- Biometric authentication pending mobile app (ADR-401)

### Neutral

- Internal transfers exempted (balances security and UX)
- Withdraw wallets validated immediately on add (no separate step)
- Security waiver required (legal protection vs. user annoyance)
- Password complexity requirements (security vs. memorability)

## Alternatives Considered

### Option 1: No Security Password (Session Authentication Only)
**Description:** Rely solely on platform login authentication for all wallet operations

**Pros:**
- Simplest user experience (no additional password)
- Faster task completion
- No password management burden
- No support burden for forgotten passwords

**Cons:**
- Single point of failure (session hijacking compromises everything)
- No defense-in-depth for critical operations
- Seed phrase export vulnerable to XSS or session theft
- Cannot demonstrate security controls for compliance
- Higher liability risk for platform

**Why Rejected:** Insufficient security for managing cryptocurrency private keys. Session authentication alone inadequate for operations with irreversible consequences (seed phrase export). Industry best practice requires additional verification for critical financial operations.

### Option 2: Password for All Operations (Including Internal Transfers)
**Description:** Require security password for every wallet operation without exemptions

**Pros:**
- Maximum security (no operation without verification)
- Simplest security model (no exemption logic)
- Consistent user experience (always prompted)
- Easiest to audit (all operations protected equally)

**Cons:**
- Poor user experience for high-frequency internal transfers
- Password fatigue increases risk of weak passwords or reuse
- Competitive disadvantage (other platforms more user-friendly)
- Users may abandon platform due to friction

**Why Rejected:** Team explicitly decided to remove password requirement for internal transfers after recognizing minimal security risk vs. significant UX cost. Strategic trade-off aligned with industry norms (e.g., banking apps don't require password for viewing balance but do for transfers).

### Option 3: Biometric Authentication Only
**Description:** Use biometric authentication (Face ID, Touch ID) instead of passwords

**Pros:**
- Better user experience (no password to remember)
- Faster authentication (face scan vs. typing)
- Stronger security (biometrics harder to steal than passwords)
- Modern user expectation (common in mobile banking)

**Cons:**
- Web platform cannot access biometrics reliably
- Not all devices support biometrics (excludes users)
- Biometric spoofing risk (though rare)
- Requires device-specific implementation

**Why Rejected:** Web platform primary focus at time of decision. Biometric authentication requires mobile app (see ADR-401 for mobile-specific biometric decision). Password works across all platforms - biometrics would create platform-specific security models.

### Option 4: Two-Factor Authentication (2FA)
**Description:** Require 2FA (SMS, authenticator app, email) for critical operations

**Pros:**
- Strong security (something you know + something you have)
- Industry standard for financial operations
- Familiar to users from banking apps
- Protects against password theft

**Cons:**
- Additional implementation complexity
- SMS 2FA vulnerable to SIM swapping
- Authenticator app requires user setup
- Email 2FA slow (latency for code delivery)
- Extra step every time (UX friction)

**Why Rejected:** Deferred to parking lot. Security password provides sufficient protection for beta launch. 2FA complexity not justified for initial rollout - can add based on beta feedback and security incidents. Many crypto platforms don't require 2FA for basic operations.

### Option 5: Hardware Security Key (e.g., YubiKey)
**Description:** Require physical hardware security key for critical wallet operations

**Pros:**
- Maximum security (cannot be remotely stolen)
- Phishing-resistant authentication
- Industry best practice for high-value accounts
- Protects against session hijacking

**Cons:**
- Requires users to purchase hardware ($20-$50)
- Excludes users unwilling to buy key
- Lost key = account recovery nightmare
- Not mobile-friendly
- Overkill for beta phase

**Why Rejected:** Too high barrier to entry for general users. Appropriate for institutional accounts or high-value users, but prevents mainstream adoption. Could offer as optional upgrade for power users in future.

### Option 6: Email Confirmation for Critical Operations
**Description:** Send email confirmation link for seed exports and withdrawals

**Pros:**
- No password to remember
- Familiar pattern (common in web apps)
- Email already verified during signup
- Provides audit trail (email record)

**Cons:**
- Slow (email latency)
- Email account compromise = wallet compromise
- Email delivery failures block operations
- Poor UX for frequent operations
- Still need password for offline scenarios

**Why Rejected:** Latency unacceptable for trading platform. Email compromise single point of failure. Doesn't provide real-time verification. Users expect immediate confirmation for wallet operations.

## Implementation Notes

### Password Complexity Requirements

**Minimum Requirements:**
- Length: 8+ characters (industry standard minimum)
- Complexity: Must include mix of character types
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*, etc.)

**Validation:**
- Client-side validation with real-time feedback
- Backend validation as defense-in-depth
- Clear error messages for failed requirements
- Password strength indicator (weak/medium/strong)

### Client-Side Implementation

**Password Hashing:**
```javascript
// Pseudocode - actual implementation uses secure hashing
const clientSideHash = await bcrypt.hash(userPassword, SALT_ROUNDS);
const encrypted = await encryptForTransmission(clientSideHash);
await sendToBackend(encrypted);
```

**Blocking Modal Flow:**
1. User navigates to Wallet Manager
2. Check backend: Does user have security password?
3. If NO: Show blocking modal (cannot dismiss)
4. User creates password with complexity validation
5. Submit to backend with encryption
6. On success: Unlock Wallet Manager access
7. If YES: Skip modal, proceed to Wallet Manager

**Verification Flow (Protected Operation):**
1. User attempts protected operation (e.g., export seed)
2. Password prompt modal appears
3. User enters security password
4. Client hashes and encrypts password
5. Sends to backend for verification
6. Backend responds: approved/denied
7. If approved: Operation proceeds
8. If denied: Error message, retry allowed

### Backend Implementation

**Storage Schema:**
```sql
-- Simplified schema
CREATE TABLE user_security_passwords (
  user_id UUID PRIMARY KEY,
  encrypted_password TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP,
  last_verified_at TIMESTAMP
);
```

**Verification Endpoint:**
- `POST /api/wallet/verify-security-password`
- Request: `{ encrypted_password: string }`
- Response: `{ verified: boolean }`
- Logged for audit trail

**Protected Endpoints:**
- `POST /api/wallet/export-seed-phrase` (requires password)
- `POST /api/wallet/add-withdraw-wallet` (requires password)
- `POST /api/wallet/remove-withdraw-wallet` (requires password)
- `POST /api/wallet/withdraw-sol` (requires password)
- `PUT /api/wallet/update-security-password` (requires current password)

### Security Waiver Implementation

**Waiver Text (Seed Export):**
```
⚠️ SECURITY WARNING ⚠️

You are about to export your wallet's private keys (seed phrase).

IMPORTANT - READ CAREFULLY:
• Private keys can only be exported ONCE
• Anyone with your seed phrase can access your funds
• Store your seed phrase offline in a secure location
• Never share your seed phrase with anyone
• Cooking.gg will never ask for your seed phrase

By clicking "I Understand", you acknowledge:
✓ You understand the security risks
✓ You are responsible for securing your seed phrase
✓ This is a one-time export (cannot be repeated)
✓ Lost seed phrases cannot be recovered

[Cancel] [I Understand and Export]
```

**Implementation:**
- Modal appears after password verification
- Must click "I Understand and Export" (not just "OK")
- Checkbox: "I have read and understand the security risks"
- Export button disabled until checkbox checked
- Waiver acceptance logged to backend

### Testing Requirements

**Unit Tests:**
- Password complexity validation
- Client-side hashing
- Encryption/decryption
- Backend verification logic

**Integration Tests:**
- Full password creation flow
- Password verification for each protected operation
- Update password flow
- Existing user retroactive enforcement

**Security Tests:**
- Password transmitted encrypted (never plaintext)
- Backend stores encrypted (not reversible to plaintext)
- Verification endpoint rate-limited (prevent brute force)
- Session timeout doesn't bypass password requirement

**User Acceptance Testing:**
- First-time user creates password successfully
- Existing user prompted to create password
- Update password flow works end-to-end
- Internal transfers work without password
- External operations require password

### Migration Strategy (Existing Users)

**Phase 1: Backend Deployment**
- Deploy encrypted password storage
- Deploy verification endpoints
- Do not enforce yet (graceful degradation)

**Phase 2: Frontend Deployment**
- Deploy blocking modal code
- Deploy password creation flow
- Deploy verification prompts
- Feature flag: OFF (not enforced)

**Phase 3: Enforcement**
- Enable feature flag
- All users see blocking modal on next Wallet Manager access
- Monitor support volume for forgotten passwords
- Communicate to users via email/notification before enforcement

**Phase 4: Validation**
- Verify all users have security password
- Monitor verification success rates
- Address support issues
- Plan password recovery mechanism

## References

### Meeting Notes
- [Weekly Demo 2025-06-06](../06-meetings/2025-06/Weekly-Demo-2025-06-06.md) - Security password implementation review
- [Weekly Demo 2025-06-13](../06-meetings/2025-06/Weekly-Demo-2025-06-13.md) - Testing and validation

### Requirements Documents
- [C203 - Password in Wallet Manager](../07-archive/processed-source-docs/2025-10-20-project-documentation/C203 - Password in Wallet Manager.md) - Original requirements document
- [Cooking Platform User Documentation](../04-knowledge-base/technical/platform-user-documentation.md) - User-facing documentation

### Related Decisions
- ADR-401: Biometric Authentication Required for Mobile Trading (mobile-specific security)
- ADR-501: Turnkey for Wallet Management (wallet service provider)
- Auth0 Social Login (session authentication - separate from security password)

### Technical References
- Turnkey wallet management service documentation
- Industry standards: NIST password guidelines
- Crypto wallet best practices (MetaMask, Coinbase Wallet)

### Parking Lot Items
- Password recovery mechanism (future implementation)
- Two-factor authentication (2FA) integration
- Hardware security key support (optional for high-value accounts)
- Biometric authentication for web (WebAuthn API)

## Revision History
- 2025-05-13: Initial requirements documented (C203)
- 2025-06-06: Implementation completed and reviewed in Weekly Demo
- 2025-06-13: Update password flow testing
- 2025-10-21: Formal ADR documented from meeting notes and requirements
