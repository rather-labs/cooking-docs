---
title: Biometric Authentication Required for Mobile Trading
type: decision-record
decision-id: ADR-401
date: 2025-10-01
status: accepted
owner: Martin Aranda, Mobile Team
stakeholders: [Martin Aranda, Gregory Chapman, Naji Osmat, Marcos Tacca, Lucas Cufre]
tags: [security, mobile, biometric, authentication, ios, android, face-id, touch-id]
summary: |
  Decision to require biometric authentication (Face ID/Touch ID on iOS, fingerprint/face unlock on Android) for all trading operations on mobile app to enhance security for financial transactions. Users must authenticate via biometrics before executing trades, withdrawals, or accessing sensitive wallet operations. Fallback to security password provided for devices without biometric capabilities. Implementation uses iOS Secure Enclave and Android KeyStore for cryptographic key protection.
related-docs:
  - ../06-meetings/2025-10/2025-10-01-mobile-app-sync.md
  - ADR-102: Auth0 for Social Authentication
  - ADR-400: Security Password for Wallet Operations
---

# Biometric Authentication Required for Mobile Trading

## Context and Problem Statement

Cooking.gg's mobile app (iOS and Android) enables users to execute financial transactions including:

- **Trading Operations:** Market orders, limit orders, swaps (potentially large amounts)
- **Wallet Operations:** Token withdrawals to external addresses
- **Sensitive Actions:** Seed phrase exports, wallet imports, security password changes

**Mobile Security Challenges:**

1. **Device Loss/Theft:**
   - User leaves phone unattended (coffee shop, gym)
   - Phone stolen with app already logged in
   - Attacker has physical access to unlocked device
   - **Risk:** Immediate financial loss (drain wallet, execute unauthorized trades)

2. **Session Persistence:**
   - Mobile apps maintain long-lived sessions (weeks/months)
   - Users don't log out (unlike web browsers)
   - Persistent session = persistent attack surface
   - **Risk:** Unauthorized access without re-authentication

3. **Shoulder Surfing:**
   - Password entry visible in public spaces
   - Attacker observes PIN/password input
   - **Risk:** Credential compromise without device access

4. **Regulatory Expectations:**
   - Financial apps expected to have strong authentication
   - App Store review guidelines emphasize security for financial transactions
   - Industry standard: biometric auth for banking/trading apps (Coinbase, Robinhood, Binance)

**Current Authentication State:**

Web App:
- Auth0 social login (session-based)
- Security password for sensitive operations (ADR-400)
- Session expires after period of inactivity

Mobile App (Initial Implementation):
- Auth0 social login (persistent session)
- No additional authentication for trades
- **Problem:** Once logged in, any person with physical device access can trade

**User Impact Scenarios:**

**Scenario 1: Lost Phone**
- User loses phone at airport
- Finder opens Cooking.gg app (still logged in)
- Executes trades, drains wallet
- User discovers loss hours later
- **Financial Loss:** Potentially thousands of dollars

**Scenario 2: Borrowed Device**
- User lets friend borrow phone briefly
- Friend opens Cooking.gg out of curiosity
- Sees portfolio balance, executes prank trade
- User discovers unauthorized trade after returning phone
- **Financial Loss + Trust Issue**

**Scenario 3: Coerced Trading**
- Attacker physically threatens user
- Forces user to unlock phone
- User opens Cooking.gg, attacker takes over
- Executes trades, transfers funds
- **Security Failure:** No secondary authentication prevents coercion

**Requirements for Solution:**

1. **Strong Authentication:** Biometric verification (Face ID, Touch ID, fingerprint)
2. **Minimal Friction:** Fast authentication (< 2 seconds)
3. **Universal Coverage:** All trading and sensitive operations protected
4. **Fallback Available:** Support devices without biometrics
5. **Platform Native:** Leverage iOS/Android built-in biometric systems
6. **Secure Storage:** Private keys protected by Secure Enclave/KeyStore
7. **User Control:** Allow users to configure sensitivity (always/periodic)

## Decision

**Require biometric authentication (Face ID/Touch ID on iOS, fingerprint/face unlock on Android) for all trading operations and sensitive actions in mobile app, with security password fallback for devices without biometric capabilities.**

### Implementation Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                     Mobile App (React Native)                 │
└─────────────────────────┬─────────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────────────┐
│              Trading/Sensitive Operation Triggered            │
│  - User taps "Buy" button                                     │
│  - User initiates withdrawal                                  │
│  - User exports seed phrase                                   │
└─────────────────────────┬─────────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────────────┐
│           Check Biometric Authentication Status               │
│  - Is biometric available on device?                          │
│  - Is biometric enrolled by user?                             │
│  - When was last successful authentication?                   │
└────┬──────────────────────────────────────────┬───────────────┘
     │                                          │
     │ Biometric Available                      │ No Biometric
     ▼                                          ▼
┌──────────────────────────┐      ┌───────────────────────────┐
│  Prompt Biometric Auth   │      │ Fallback: Security        │
│  - Face ID (iOS)         │      │ Password Prompt           │
│  - Touch ID (iOS)        │      │ - User enters password    │
│  - Fingerprint (Android) │      │ - Backend validates       │
│  - Face Unlock (Android) │      │                           │
└────┬─────────────────────┘      └────┬──────────────────────┘
     │                                  │
     │ Success                          │ Success
     ▼                                  ▼
┌───────────────────────────────────────────────────────────────┐
│               Execute Protected Operation                     │
│  - Proceed with trade                                         │
│  - Complete withdrawal                                        │
│  - Export seed phrase                                         │
│  - Store authentication timestamp (5-minute grace period)     │
└───────────────────────────────────────────────────────────────┘
```

### Protected Operations

**Always Require Biometric:**

1. **Trading Operations:**
   - Market buy/sell orders
   - Limit orders with TP/SL
   - Advanced orders (TWAP, DCA, VWAP)
   - Order cancellations (prevent accidental cancels)

2. **Wallet Withdrawals:**
   - Transfer tokens to external address
   - Bridge tokens to other chains
   - Any transaction moving value out of Cooking.gg

3. **Sensitive Wallet Operations:**
   - Export seed phrase
   - View private key
   - Import wallet
   - Delete wallet
   - Change security password

**Never Require Biometric:**

1. **Read-Only Operations:**
   - View portfolio
   - Browse token discovery
   - View price charts
   - Read transaction history

2. **Low-Risk Actions:**
   - Add token to watchlist
   - Change theme/settings
   - View referral code

### iOS Implementation

**Face ID/Touch ID Integration:**

```javascript
// React Native Biometrics library
import ReactNativeBiometrics from 'react-native-biometrics';

const rnBiometrics = new ReactNativeBiometrics();

// Check if biometrics available
async function isBiometricAvailable() {
  const { available, biometryType } = await rnBiometrics.isSensorAvailable();

  if (!available) {
    return { available: false };
  }

  // biometryType: 'FaceID', 'TouchID', 'Biometrics' (Android)
  return { available: true, type: biometryType };
}

// Authenticate user before trading
async function authenticateForTrade(operation) {
  try {
    const { success, error } = await rnBiometrics.simplePrompt({
      promptMessage: `Confirm ${operation}`,
      cancelButtonText: 'Cancel'
    });

    if (success) {
      console.log('Biometric authentication successful');
      // Store authentication timestamp (grace period)
      await AsyncStorage.setItem('last_biometric_auth', Date.now().toString());
      return { success: true };
    } else {
      console.log('Biometric authentication cancelled');
      return { success: false, reason: 'cancelled' };
    }
  } catch (error) {
    console.error('Biometric authentication failed:', error);
    return { success: false, reason: error.message };
  }
}

// Create signature with biometric-protected key (advanced security)
async function createBiometricSignature(payload) {
  try {
    // Create key protected by Secure Enclave
    const { publicKey } = await rnBiometrics.createKeys();

    // Sign payload (requires biometric auth)
    const { success, signature } = await rnBiometrics.createSignature({
      promptMessage: 'Confirm transaction',
      payload: payload
    });

    if (success) {
      return { signature, publicKey };
    }
  } catch (error) {
    console.error('Biometric signature creation failed:', error);
    throw error;
  }
}
```

**iOS Info.plist Configuration:**

```xml
<!-- Info.plist -->
<key>NSFaceIDUsageDescription</key>
<string>Cooking.gg requires Face ID to securely confirm trades and protect your wallet.</string>

<key>NSBiometricUsageDescription</key>
<string>Cooking.gg uses biometric authentication to secure your trading operations.</string>
```

**Secure Enclave Integration:**

iOS Secure Enclave provides hardware-backed cryptographic key protection:

- Private keys never leave Secure Enclave
- Biometric authentication required to use keys
- Keys deleted if biometric enrollment changes
- Protection against jailbreak and malware

### Android Implementation

**Fingerprint/Face Unlock Integration:**

```kotlin
// BiometricPrompt integration (Kotlin/Java)
import androidx.biometric.BiometricManager
import androidx.biometric.BiometricPrompt

fun authenticateForTrade(activity: AppCompatActivity, callback: BiometricCallback) {
    val executor = ContextCompat.getMainExecutor(activity)

    val biometricPrompt = BiometricPrompt(activity, executor,
        object : BiometricPrompt.AuthenticationCallback() {
            override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) {
                super.onAuthenticationSucceeded(result)
                callback.onSuccess()
            }

            override fun onAuthenticationFailed() {
                super.onAuthenticationFailed()
                callback.onFailure("Authentication failed")
            }

            override fun onAuthenticationError(errorCode: Int, errString: CharSequence) {
                super.onAuthenticationError(errorCode, errString)
                callback.onError(errorCode, errString.toString())
            }
        })

    val promptInfo = BiometricPrompt.PromptInfo.Builder()
        .setTitle("Confirm Trade")
        .setSubtitle("Authenticate to complete this trade")
        .setNegativeButtonText("Cancel")
        .build()

    biometricPrompt.authenticate(promptInfo)
}
```

**Android Manifest Permissions:**

```xml
<!-- AndroidManifest.xml -->
<uses-permission android:name="android.permission.USE_BIOMETRIC" />
<uses-permission android:name="android.permission.USE_FINGERPRINT" />
```

**Android KeyStore Integration:**

Android KeyStore provides hardware-backed key protection:

- Keys stored in Trusted Execution Environment (TEE)
- Biometric authentication required for key access
- Protection against rooting and tampering

### Grace Period for User Experience

**Problem:** Requiring biometric for every single trade is friction-heavy.

**Solution:** 5-minute grace period after successful authentication.

```javascript
// Check if user recently authenticated
async function needsBiometricAuth() {
  const lastAuth = await AsyncStorage.getItem('last_biometric_auth');

  if (!lastAuth) {
    return true; // Never authenticated
  }

  const lastAuthTime = parseInt(lastAuth);
  const now = Date.now();
  const gracePeriod = 5 * 60 * 1000; // 5 minutes

  if (now - lastAuthTime < gracePeriod) {
    return false; // Within grace period, skip auth
  }

  return true; // Grace period expired, require auth
}

// Trading flow with grace period
async function executeTrade(order) {
  if (await needsBiometricAuth()) {
    const authResult = await authenticateForTrade('trade');

    if (!authResult.success) {
      // Authentication failed or cancelled
      return { success: false, error: 'Authentication required' };
    }
  }

  // Proceed with trade (authenticated or within grace period)
  const result = await api.executeTrade(order);
  return result;
}
```

**Grace Period Benefits:**

- User executes multiple trades without re-authenticating each time
- Reduces friction for active trading sessions
- Still protects against unauthorized access (5 minutes is short enough)

**Grace Period Invalidation:**

Grace period resets on:
- App backgrounded for > 1 minute
- Device locked
- App terminated
- User logs out

### Fallback to Security Password

**Devices Without Biometrics:**

Older devices or users who disabled biometrics:

```javascript
async function authenticateUser(operation) {
  // Check biometric availability
  const { available } = await isBiometricAvailable();

  if (available) {
    // Use biometric authentication
    return await authenticateForTrade(operation);
  } else {
    // Fallback: prompt security password
    return await promptSecurityPassword(operation);
  }
}

async function promptSecurityPassword(operation) {
  // Show modal with password input
  const password = await showSecurityPasswordModal({
    title: `Confirm ${operation}`,
    message: 'Enter your security password'
  });

  // Validate with backend (ADR-400)
  const isValid = await api.validateSecurityPassword(password);

  if (isValid) {
    // Store authentication timestamp
    await AsyncStorage.setItem('last_biometric_auth', Date.now().toString());
    return { success: true };
  }

  return { success: false, reason: 'invalid_password' };
}
```

### User Configuration

**Settings Panel:**

Allow users to customize biometric behavior:

```javascript
// User preferences
const biometricSettings = {
  enabled: true,              // Enable/disable biometric auth
  gracePeriod: 5,             // Minutes (1, 5, 15, or 30)
  requireForTrades: true,     // Always require for trades
  requireForWithdrawals: true, // Always require for withdrawals
  requireForSeedPhrase: true  // Always require for seed phrase export
};
```

**Settings UI:**

```
┌────────────────────────────────────────┐
│ Security Settings                      │
├────────────────────────────────────────┤
│ ☑ Use Face ID for trades              │
│   (Disable to use security password)   │
│                                        │
│ Grace Period: [5 minutes ▾]           │
│   (Time before re-authentication)      │
│                                        │
│ Always Require Biometric:              │
│ ☑ Trading operations                   │
│ ☑ Wallet withdrawals                   │
│ ☑ Seed phrase exports                  │
└────────────────────────────────────────┘
```

### Error Handling

**Common Biometric Errors:**

```javascript
const BiometricError = {
  NOT_AVAILABLE: 'Biometric authentication not available on this device',
  NOT_ENROLLED: 'No biometric credentials enrolled. Please set up Face ID/Touch ID in Settings.',
  AUTHENTICATION_FAILED: 'Biometric authentication failed. Try again or use security password.',
  CANCELLED: 'Authentication cancelled',
  LOCKOUT: 'Too many failed attempts. Please try again later or use security password.',
  SYSTEM_ERROR: 'System error occurred. Please restart the app.'
};

async function handleBiometricError(error) {
  switch (error.code) {
    case 'NOT_AVAILABLE':
    case 'NOT_ENROLLED':
      // Fallback to security password
      return await promptSecurityPassword('trade');

    case 'LOCKOUT':
      // Temporary lockout, force password fallback
      Alert.alert(
        'Too Many Attempts',
        'Biometric authentication temporarily locked. Use security password instead.',
        [{ text: 'OK', onPress: () => promptSecurityPassword('trade') }]
      );
      break;

    case 'CANCELLED':
      // User cancelled, don't proceed
      return { success: false, reason: 'cancelled' };

    default:
      // Unknown error, offer retry or fallback
      Alert.alert(
        'Authentication Error',
        'Would you like to try again or use security password?',
        [
          { text: 'Try Again', onPress: () => authenticateForTrade('trade') },
          { text: 'Use Password', onPress: () => promptSecurityPassword('trade') }
        ]
      );
  }
}
```

## Rationale

### Security Benefits

**Protection Against Physical Device Access:**

Without biometric auth:
- Attacker finds unlocked phone → immediate wallet access

With biometric auth:
- Attacker finds unlocked phone → cannot execute trades (requires Face ID)
- **Attack Window:** Reduced from "until session expires" to "0 seconds"

**Protection Against Coercion (Limited):**

While biometric can't prevent forced authentication under duress, it:
- Raises the bar for attackers (must physically coerce user)
- Eliminates remote attacks (can't trade without physical presence)
- Creates audit trail (biometric attempts logged)

**Regulatory Compliance:**

Financial apps expected to have strong authentication:
- Apple App Store guidelines: "Apps that facilitate financial transactions must secure sensitive user data"
- Google Play policies: "Financial apps should implement appropriate security measures"
- Industry standard: Coinbase, Binance, Robinhood all require biometric

### User Experience Balance

**Friction vs Security Trade-off:**

Too strict:
- Require biometric for every tap → users frustrated
- No grace period → cannot execute rapid trades

Too loose:
- No biometric → wallet drained if phone lost
- Long grace period (30 min) → attack window too large

**Optimal Balance:**
- Biometric required for trades/withdrawals
- 5-minute grace period (reasonable for trading session)
- Read-only operations unrestricted (browse freely)

**User Research Insight:**

Mobile banking apps (Chase, Bank of America) use similar approach:
- Biometric required for transfers
- Grace period for multiple transfers
- Balance viewing doesn't require biometric

Users familiar with this pattern → low learning curve.

### Platform Native Benefits

**Why Not Custom Biometric Implementation:**

Custom implementation risks:
- Reinvent security primitives (high risk of vulnerabilities)
- No hardware-backed key protection
- Poor user experience (inconsistent with system)
- App Store rejection risk (security concerns)

**Platform Native Advantages:**

- **Hardware Backed:** Secure Enclave (iOS) / KeyStore (Android)
- **OS Integration:** System biometric UI (familiar to users)
- **Automatic Updates:** OS security patches apply automatically
- **User Trust:** Users trust system biometric more than app-specific

### Cost-Benefit Analysis

**Implementation Cost:**

- React Native Biometrics library: Free, open-source
- Development time: 1-2 weeks (iOS + Android implementation, testing)
- No ongoing operational cost

**Security Benefit:**

- Eliminated risk: Wallet drain from lost/stolen device
- Reduced attack surface: Physical access required (eliminates remote attacks)
- User confidence: Professional security practices → higher user trust → more users

**Alternatives (Cost Comparison):**

1. **No biometric (status quo):**
   - Cost: $0
   - Risk: High (unauthorized trades if device accessed)
   - User Trust: Low (financial app without strong auth)

2. **SMS 2FA:**
   - Cost: ~$0.01/SMS (~$500/month for 50,000 trades)
   - Risk: Medium (SIM swap attacks, SMS interception)
   - Friction: High (wait for SMS, type code)

3. **TOTP (Google Authenticator):**
   - Cost: $0
   - Risk: Low
   - Friction: Medium (open authenticator app, type code)

4. **Biometric Authentication:**
   - Cost: $0 (after initial development)
   - Risk: Low (hardware-backed, coercion risk remains)
   - Friction: Low (< 2 seconds, native UI)

**Winner: Biometric** - Lowest friction, lowest cost, sufficiently secure.

## Consequences

### Positive

**Security Improvements:**
- Unauthorized trades prevented (requires Face ID/Touch ID)
- Physical device access insufficient (biometric required)
- Hardware-backed key protection (Secure Enclave/KeyStore)
- Industry-standard security (matches Coinbase, Robinhood)

**User Experience:**
- Fast authentication (< 2 seconds typical)
- Native platform UI (familiar interaction)
- Grace period reduces friction (5-minute window)
- Fallback available (security password for older devices)

**Compliance & Trust:**
- App Store approval (meets financial app security requirements)
- User confidence (professional-grade security)
- Reduced liability (demonstrable security measures)

**Operational Benefits:**
- No ongoing costs (platform native, no SMS fees)
- Automatic OS security updates
- Audit trail (biometric attempts logged)

### Negative

**Device Compatibility:**
- Older devices without biometric require password fallback
- Some users disable biometrics (privacy concerns)
- Biometric failure rate ~2-5% (lighting, wet fingers, etc.)

**User Friction:**
- Additional step for trades (biometric prompt)
- Grace period can expire mid-trading session (re-authenticate)
- Users with biometric enrollment issues (injuries, accessibility)

**Implementation Complexity:**
- Platform-specific code (iOS vs Android)
- Error handling for biometric failures
- Testing across device types (iPhone X+, Android variants)
- Fallback flows increase code complexity

**Edge Cases:**
- Device settings change (biometric disabled after enrollment)
- Biometric hardware failure
- OS permission revoked by user
- Developer mode / rooted devices (security bypass concerns)

**User Confusion:**
- Some users may not understand why biometric required
- "Why does portfolio view not need Face ID but trading does?" (education needed)
- Grace period expiration mid-session (unexpected re-auth)

### Neutral

**Platform Dependency:**
- Tied to iOS/Android biometric APIs (cannot easily migrate)
- API changes in future OS versions (maintenance required)

**Security Trade-offs:**
- Biometric doesn't prevent coerced trading (physical threat)
- Grace period creates small attack window (acceptable risk)

## Alternatives Considered

### Option 1: No Additional Authentication (Status Quo)

**Description:** Rely solely on Auth0 session authentication

**Pros:**
- Zero friction (no additional authentication)
- Simple implementation (no biometric code)
- Fast trading experience

**Cons:**
- High security risk (unauthorized trades if device accessed)
- Does not meet financial app standards
- Potential App Store rejection
- User trust issues (no protection for financial transactions)

**Why Rejected:** Unacceptable security risk for financial application. Industry standard requires strong authentication for trading.

### Option 2: SMS Two-Factor Authentication (2FA)

**Description:** Send SMS code before each trade

**Pros:**
- Works on all devices (no biometric requirement)
- Familiar pattern (banking apps use SMS 2FA)

**Cons:**
- High friction (wait for SMS, type 6-digit code)
- Ongoing cost (~$0.01/SMS = $500/month for 50,000 trades)
- SIM swap attack vector (attacker can intercept SMS)
- Unreliable (SMS delivery delays, international travel)
- Poor UX for rapid trading (multiple trades = multiple SMS codes)

**Why Rejected:** High friction kills trading experience. Ongoing costs add up. SIM swap attacks well-documented.

### Option 3: TOTP (Time-Based One-Time Password)

**Description:** Require Google Authenticator-style code

**Pros:**
- No ongoing cost (app-based)
- More secure than SMS (no SIM swap risk)
- Works offline

**Cons:**
- High friction (open authenticator app, type 6-digit code)
- Poor UX for rapid trading
- Requires separate authenticator app install
- Users must back up TOTP secret (complexity)

**Why Rejected:** Friction too high for mobile trading. Users expect seamless mobile experience.

### Option 4: Security Password Only (No Biometric)

**Description:** Prompt security password for trades (ADR-400)

**Pros:**
- Works on all devices
- No platform-specific code
- User already has security password

**Cons:**
- Slower than biometric (type password vs Face ID)
- Shoulder surfing risk (password visible when typed)
- Password fatigue (users choose weak passwords to reduce friction)
- Accessibility issues (typing difficult for some users)

**Why Rejected:** Biometric faster and more secure. Security password retained as fallback only.

### Option 5: Hardware Security Keys (YubiKey, etc.)

**Description:** Require physical security key for trades

**Pros:**
- Strongest security (physical token required)
- Phishing resistant

**Cons:**
- Requires separate hardware purchase ($50+)
- Poor mobile UX (plug USB key into phone?)
- Most users won't buy/carry hardware key
- NFC-based keys have compatibility issues

**Why Rejected:** Not practical for mobile app. Users won't adopt.

## Implementation Notes

### React Native Biometrics Library

**Installation:**

```bash
npm install react-native-biometrics
cd ios && pod install
```

**Configuration:**

```javascript
// biometricAuth.ts
import ReactNativeBiometrics from 'react-native-biometrics';

const rnBiometrics = new ReactNativeBiometrics();

export async function isBiometricSupported() {
  const { available, biometryType } = await rnBiometrics.isSensorAvailable();
  return { available, type: biometryType };
}

export async function authenticateUser(operation: string) {
  const { success } = await rnBiometrics.simplePrompt({
    promptMessage: `Confirm ${operation}`,
    cancelButtonText: 'Cancel'
  });

  return success;
}
```

### Testing Strategy

**Unit Tests:**
- Mock biometric responses (success, failure, unavailable)
- Test grace period logic
- Test fallback to security password

**Integration Tests:**
- Test biometric flow on real devices
- Test each operation (trade, withdrawal, seed export)
- Test error scenarios (cancelled, lockout)

**E2E Tests (Detox):**
- Automated biometric authentication (simulator only)
- Manual testing on physical devices (Face ID cannot be automated)

**Device Coverage:**
- iOS: iPhone X+ (Face ID), iPhone 8 (Touch ID), older (no biometric)
- Android: Pixel (fingerprint), Samsung (face unlock), older devices

### Analytics Events

```javascript
// Track biometric authentication events
analytics.track('biometric_auth_attempted', {
  operation: 'trade', // or 'withdrawal', 'seed_export'
  biometric_type: 'FaceID', // or 'TouchID', 'Fingerprint'
  device_model: 'iPhone 14 Pro'
});

analytics.track('biometric_auth_succeeded', {
  operation: 'trade',
  duration_ms: 1234
});

analytics.track('biometric_auth_failed', {
  operation: 'trade',
  reason: 'cancelled', // or 'lockout', 'not_enrolled'
  fallback_used: 'security_password'
});
```

## References

### Meeting Notes
- [Mobile App Sync 2025-10-01](../06-meetings/2025-10/2025-10-01-mobile-app-sync.md) - Biometric authentication decision

### Related Decisions
- ADR-102: Auth0 for Social Authentication (initial login)
- ADR-400: Security Password for Wallet Operations (fallback authentication)

### Technical References
- React Native Biometrics: https://github.com/SelfLender/react-native-biometrics
- Apple Face ID/Touch ID: https://developer.apple.com/documentation/localauthentication
- Android BiometricPrompt: https://developer.android.com/training/sign-in/biometric-auth
- iOS Secure Enclave: https://support.apple.com/guide/security/secure-enclave-sec59b0b31ff/web
- Android KeyStore: https://developer.android.com/training/articles/keystore

### Industry Examples
- Coinbase Mobile Security: https://www.coinbase.com/security
- Robinhood Security Features: https://robinhood.com/us/en/support/articles/security/
- Binance Biometric Authentication: https://www.binance.com/en/support/faq/biometric-authentication

## Revision History
- 2025-10-01: Biometric authentication required for mobile trading decision made
- 2025-10-01: React Native Biometrics library selected for implementation
- 2025-10-21: Formal ADR documented from meeting notes
