---
title: Support for Externally Created Solana Wallets
type: feature-specification
status: planned
priority: medium
created: 2025-08-21
date: 2025-10-20
updated: 2025-10-20
tags: [wallet, import, external-wallet, turnkey, security]
related:
  - "[[security-password-wallet-manager]]"
  - "[[social-login-integration]]"
  - "[[mobile-app-prd]]"
---

# Support for Externally Created Solana Wallets

## Overview

In order to allow Cooking traders to better manage their funds and enable them to operate with wallets they already own, we will work to support Solana wallets not created within the platform.

## Solution Architecture

### Turnkey Integration

In order to provide a seamless transaction experience, these wallets will be encrypted with signing rights being surrendered to Turnkey, effectively transforming these self-custodial wallets into wallets shared with Turnkey.

### Operational Transparency

Once Turnkey has the signing rights for an externally created wallet, these will operate **exactly the same** as any other created within Cooking, making them virtually transparent for the user.

## Platform Availability

### Desktop Only

This feature will **only be available via desktop webapp**.

**Rationale**:
- Enhanced security for seed phrase entry
- Better user experience for lengthy input
- Reduced risk of mobile security vulnerabilities

### Mobile Considerations

Mobile users will see:
- Feature exists but requires desktop
- Explanation of security rationale
- Guidance to use desktop for import

## Import Process

### Entry Point

In order for the user to add an external wallet, they will be requested for their 12 word seed phrase in a modal in the **Wallet Manager** when accessing the **'New Wallet'** flow.

### User Flow

1. User clicks "New Wallet" in Wallet Manager
2. Modal displays two options:
   - **Create New Wallet** (default)
   - **Import Existing Wallet** (desktop only)
3. User selects "Import Existing Wallet"
4. Security password prompt appears
5. User enters security password
6. Seed phrase input form displayed
7. User enters 12-word seed phrase
8. System validates seed phrase format
9. Wallet imported and encrypted by Turnkey
10. Success confirmation displayed
11. Wallet appears in Wallet Manager

### Seed Phrase Input Form

**Design**:
- 12 individual input fields (one per word)
- Auto-focus next field on completion
- Paste support (split into 12 fields automatically)
- Real-time validation
- Word suggestions from BIP39 word list
- Copy-paste warning (security reminder)

**Validation**:
- Each word must be from BIP39 word list
- All 12 words required
- Checksum validation
- Duplicate detection

## Security Considerations

### Seed Phrase Handling

**Critical Security Rule**:
Once imported, this seed phrase **won't be exportable** on Cooking's UI since it will be encrypted and kept safe in a secret in Turnkey's server.

### Why Non-Exportable?

1. **Single Point of Entry**: External wallets already have seed phrase stored by user
2. **Security Best Practice**: Minimize seed phrase exposure
3. **Turnkey Architecture**: Encrypted storage in Turnkey's secure environment
4. **Consistency**: Align with platform's security model

### Security Password Requirement

Before accessing the import flow:
- User must enter security password
- Validates user authorization
- Adds friction to prevent accidental imports
- Audit trail for sensitive operations

## Asset Support

### Solana-Only

Cooking will **only read Solana based assets** from the wallet, hence making these the only approved assets to be used in the app.

**Implications**:
- Non-Solana tokens ignored
- No cross-chain functionality
- Simplified asset management
- Reduced complexity

### Asset Discovery

Upon import:
- Scan wallet for Solana tokens
- Display current holdings
- Calculate total portfolio value
- Integrate into existing portfolio view

## Wallet Behavior Post-Import

### Identical Functionality

Imported wallets function identically to Cooking-created wallets:

**Capabilities**:
- Send transactions
- Receive funds
- Trade on platform
- View transaction history
- Add to withdraw wallet list
- Set as active wallet
- Archive (except if primary)

### Turnkey Signing

**All transactions signed by Turnkey**:
- No direct access to private keys
- Secure key management
- Platform security maintained
- User experience preserved

## User Education

### Pre-Import Warning

Display before seed phrase entry:

```
⚠️ Important Security Information

About to import an existing wallet:

• You are sharing control of this wallet with Cooking/Turnkey
• Cooking will be able to sign transactions on your behalf
• Your seed phrase will be encrypted and stored securely
• You CANNOT export this seed phrase from Cooking later
• Keep your original seed phrase in a safe location

This is a ONE-WAY operation. Proceed only if you understand and accept these terms.

☑️ I understand and accept these conditions
```

### Post-Import Guidance

After successful import:

```
✅ Wallet Imported Successfully

Your external wallet is now integrated with Cooking:

• Wallet address: [display address]
• Solana assets detected: [count]
• Current balance: [value]

Remember:
• Your original seed phrase remains valid
• Keep it in a secure location
• Use Cooking for trading these assets
• Your wallet operates normally within Cooking

[View My Wallet]  [Close]
```

## Error Handling

### Invalid Seed Phrase

**Scenarios**:
- Invalid word(s) from BIP39 list
- Incorrect word count (not 12)
- Failed checksum validation
- Already imported wallet

**User Feedback**:
- Clear error message
- Specific guidance for resolution
- Option to retry
- Link to support if needed

### Import Failures

**Possible Causes**:
- Network issues
- Turnkey service unavailable
- Encryption failure
- Database error

**User Experience**:
- Graceful error handling
- Preserve entered data (securely)
- Retry option
- Support contact information

## Technical Implementation

### Encryption Flow

1. Seed phrase entered client-side
2. Validate format and checksum
3. Derive Solana public key
4. Check for duplicates
5. Send to backend (HTTPS only)
6. Backend sends to Turnkey API
7. Turnkey encrypts and stores
8. Returns wallet ID
9. Store wallet metadata in database
10. Return success to frontend

### Data Storage

**Turnkey**:
- Encrypted seed phrase
- Signing capabilities

**Cooking Database**:
- Wallet ID (Turnkey reference)
- Public address
- Wallet metadata
- User association
- Import timestamp
- Is imported (boolean flag)

### API Endpoints

```
POST /api/wallet/import
  Request:
    - security_password (encrypted)
    - seed_phrase (encrypted in transit)
  Response:
    - wallet_id
    - public_address
    - detected_assets[]

GET /api/wallet/{id}/assets
  Response:
    - assets[]
    - total_value
```

## Limitations

### What You CAN Do

✅ Import 12-word Solana wallet seed phrases
✅ Trade with imported wallet
✅ Send/receive Solana assets
✅ View transaction history
✅ Use all platform features

### What You CANNOT Do

❌ Export imported seed phrase from Cooking
❌ Import non-Solana wallets
❌ Import 24-word seed phrases (future consideration)
❌ Import wallet without security password
❌ Import on mobile devices

## Future Enhancements

### Planned Features

- **24-word seed phrase support**
- **Hardware wallet integration** (Ledger, Trezor)
- **Multi-signature wallet support**
- **Mobile import** (with enhanced security)
- **Watch-only wallet mode** (no key import)

### Potential Improvements

- **Wallet labeling** (custom names)
- **Import history** (audit log)
- **Bulk import** (multiple wallets)
- **Cross-chain support** (if platform expands)

## Testing Considerations

### Test Cases

- Valid 12-word seed phrase import
- Invalid seed phrase rejection
- Duplicate wallet detection
- Security password validation
- Asset discovery accuracy
- Transaction signing functionality
- Error recovery flows

### Security Testing

- Seed phrase encryption validation
- Secure transmission verification
- Access control testing
- Audit logging verification

---

**Status**: Planned
**Priority**: Medium - Enhances user flexibility
**Platform**: Desktop web only
**Dependencies**: Turnkey integration, Security Password feature
**Next Steps**:
1. Finalize Turnkey integration for external wallet encryption
2. Design import UI/UX flow
3. Implement seed phrase validation
4. Build secure import pipeline
5. Test thoroughly (security focus)
6. Document user guidelines
7. Deploy to desktop web
8. Monitor adoption and issues
