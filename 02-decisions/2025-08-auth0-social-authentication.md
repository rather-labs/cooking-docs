---
title: Auth0 for Social Authentication
type: decision-record
decision-id: ADR-102
date: 2025-08-01
status: accepted
owner: Martin Lecam, Byron Chavarria
stakeholders: [Martin Lecam, Byron Chavarria, Marko Jauregui, Lucas Cufre, Martin Aranda]
tags: [technical, authentication, auth0, social-login, security, turnkey, wallet]
summary: |
  Decision to adopt Auth0 as the authentication platform for social login (Twitter, Google, Apple) to improve user onboarding experience and Turnkey wallet creation handling. Auth0 provides managed authentication infrastructure with custom callback support, OAuth provider integration, and session management, eliminating the complexity of building and maintaining social login integrations in-house.
related-docs:
  - ../06-meetings/2025-08/2025-08-01-daily-standup.md
  - ../06-meetings/2025-08/2025-08-08-daily-standup.md
  - ../06-meetings/2025-08/Weekly-Demo-2025-08-08.md
  - ADR-400: Security Password for Wallet Operations
---

# Auth0 for Social Authentication

## Context and Problem Statement

Cooking.gg requires user authentication to create accounts, manage wallets, and execute trading operations. The platform's user onboarding flow involves:

1. **User Authentication:** Verify user identity (email, social login)
2. **Turnkey Integration:** Create non-custodial wallet via Turnkey service
3. **Session Management:** Maintain secure authenticated sessions
4. **Account Linking:** Support multiple authentication methods per user

**Current Pain Points with In-House Authentication:**

1. **Social Login Complexity:**
   - Each provider (Twitter, Google, Apple) requires separate OAuth implementation
   - OAuth 2.0 protocol complexities (redirect flows, token management, refresh tokens)
   - Provider-specific quirks and edge cases
   - Redirect URL handling across web and mobile
   - Token validation and security best practices

2. **Turnkey Wallet Creation Issues:**
   - User creation flow requires authenticated identity before Turnkey API call
   - Managing user state between authentication and wallet creation
   - Handling failures mid-flow (authenticated but wallet creation fails)
   - Retry logic and error recovery

3. **Security Burden:**
   - Session token management (generation, validation, expiration, refresh)
   - Password hashing and storage (for email/password users)
   - Multi-factor authentication implementation
   - CSRF and XSS attack prevention
   - Secure token storage on client (web and mobile)

4. **Cross-Platform Consistency:**
   - Different auth flows for web vs mobile (WebView, deep links, universal links)
   - Apple Sign-In requires specific Apple Developer configuration
   - Twitter auth callback handling varies by platform
   - Session synchronization across devices

5. **Maintenance Burden:**
   - OAuth provider APIs change over time (breaking changes)
   - Security patches and vulnerability monitoring
   - Compliance requirements (GDPR, data privacy)
   - Audit logging for authentication events

**User Requirements:**

- **Social Login:** Users expect to sign in with Twitter, Google, or Apple (no password creation)
- **Fast Onboarding:** Minimal friction from signup to first trade (< 60 seconds ideal)
- **Secure:** Industry-standard security practices (no user credential exposure)
- **Cross-Platform:** Consistent experience on web and mobile
- **Account Linking:** Link multiple social accounts to single Cooking.gg account

**Business Requirements:**

- **Reduce Development Time:** Focus engineering on core platform features
- **Minimize Security Risk:** Delegate authentication security to specialists
- **Scalability:** Support growing user base without auth infrastructure bottlenecks
- **Reliability:** 99.9%+ uptime for authentication (users can't trade if can't log in)

## Decision

**Adopt Auth0 as the managed authentication platform for all social login and user authentication, with custom callback handling for Turnkey wallet creation integration.**

### Implementation Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                        User (Web/Mobile)                       │
└───────────────────────┬────────────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────────────┐
│                   Cooking.gg Frontend                          │
│  - Auth0 SDK integration (web: auth0-js, mobile: Auth0.swift) │
│  - Login button triggers Auth0 Universal Login                 │
└───────────────────────┬────────────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────────────┐
│                     Auth0 Platform                             │
│  - Universal Login (hosted login page)                         │
│  - Social OAuth providers (Twitter, Google, Apple)             │
│  - Session management and token issuance                       │
│  - Custom callback to Cooking.gg backend                       │
└───────────────────────┬────────────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────────────┐
│              Cooking.gg Backend (Auth Service)                 │
│  - Validate Auth0 tokens (JWT verification)                    │
│  - Create/retrieve user account                                │
│  - Trigger Turnkey wallet creation (if new user)               │
│  - Issue session token (JWT) for API access                    │
└───────────────────────┬────────────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────────────┐
│                     Turnkey API                                │
│  - Create non-custodial wallet for user                        │
│  - Return wallet address and signing credentials               │
└────────────────────────────────────────────────────────────────┘
```

### Supported Social Providers

**Initial Support:**

1. **Twitter (X):**
   - Primary provider for crypto community
   - OAuth 2.0 with custom callback
   - User profile: username, profile image
   - Challenge: Twitter API redirect handling (resolved with custom callback)

2. **Google:**
   - Broadest user base
   - OAuth 2.0 with Google Identity Services
   - User profile: email, name, profile image
   - Mature provider: minimal configuration issues

3. **Apple Sign In:**
   - Required for iOS App Store approval
   - OAuth 2.0 with Apple ID
   - User profile: email (optional name)
   - Privacy-focused: email relay support

**Future Consideration:**
- Facebook (if user demand warrants)
- Discord (crypto community presence)
- Email/Password (for users preferring traditional auth)

### Auth0 Configuration

**Auth0 Application Setup:**

```javascript
// Auth0 Application Configuration
{
  "name": "Cooking.gg Production",
  "app_type": "spa",  // Single Page Application
  "callbacks": [
    "https://cooking.gg/auth/callback",
    "https://cooking.gg/auth/silent-callback",
    "cookinggg://auth/callback"  // Mobile deep link
  ],
  "allowed_logout_urls": [
    "https://cooking.gg/",
    "cookinggg://logout"
  ],
  "allowed_web_origins": [
    "https://cooking.gg"
  ],
  "jwt_configuration": {
    "lifetime_in_seconds": 36000,  // 10 hours
    "alg": "RS256"
  },
  "refresh_token": {
    "rotation_type": "rotating",
    "expiration_type": "expiring",
    "leeway": 30,
    "token_lifetime": 2592000,  // 30 days
    "infinite_token_lifetime": false,
    "infinite_idle_token_lifetime": false,
    "idle_token_lifetime": 1296000  // 15 days
  }
}
```

**Social Connection Configuration:**

```javascript
// Twitter (X) Connection
{
  "name": "twitter",
  "strategy": "twitter",
  "enabled_clients": ["cooking-gg-production"],
  "options": {
    "client_id": "${TWITTER_CLIENT_ID}",
    "client_secret": "${TWITTER_CLIENT_SECRET}",
    "scope": "email profile"
  }
}

// Google Connection
{
  "name": "google-oauth2",
  "strategy": "google-oauth2",
  "enabled_clients": ["cooking-gg-production"],
  "options": {
    "client_id": "${GOOGLE_CLIENT_ID}",
    "client_secret": "${GOOGLE_CLIENT_SECRET}",
    "scope": "email profile",
    "allowed_audiences": ["https://cooking.gg"]
  }
}

// Apple Connection
{
  "name": "apple",
  "strategy": "apple",
  "enabled_clients": ["cooking-gg-production"],
  "options": {
    "client_id": "${APPLE_CLIENT_ID}",
    "team_id": "${APPLE_TEAM_ID}",
    "key_id": "${APPLE_KEY_ID}",
    "scope": "email name"
  }
}
```

### Frontend Integration

**Web Application (React):**

```javascript
import { Auth0Provider, useAuth0 } from '@auth0/auth0-react';

// App.tsx - Wrap app with Auth0 provider
function App() {
  return (
    <Auth0Provider
      domain="cooking.auth0.com"
      clientId={process.env.REACT_APP_AUTH0_CLIENT_ID}
      redirectUri={window.location.origin + '/auth/callback'}
      audience="https://api.cooking.gg"
      scope="openid profile email"
      useRefreshTokens={true}
      cacheLocation="localstorage"
    >
      <AppRoutes />
    </Auth0Provider>
  );
}

// LoginButton.tsx - Trigger social login
function LoginButton({ provider }: { provider: 'google' | 'twitter' | 'apple' }) {
  const { loginWithRedirect } = useAuth0();

  const handleLogin = () => {
    loginWithRedirect({
      connection: provider === 'google' ? 'google-oauth2' : provider,
      appState: { returnTo: '/dashboard' }
    });
  };

  return (
    <button onClick={handleLogin}>
      Continue with {provider.charAt(0).toUpperCase() + provider.slice(1)}
    </button>
  );
}

// AuthCallback.tsx - Handle redirect after Auth0 login
function AuthCallback() {
  const { isLoading, isAuthenticated, user, getAccessTokenSilently } = useAuth0();
  const navigate = useNavigate();

  useEffect(() => {
    async function handleCallback() {
      if (isAuthenticated && user) {
        // Get Auth0 access token
        const accessToken = await getAccessTokenSilently();

        // Exchange Auth0 token for Cooking.gg session
        const session = await fetch('/api/auth/callback', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ auth0UserId: user.sub })
        }).then(res => res.json());

        // Store Cooking.gg session token
        localStorage.setItem('cooking_session', session.token);

        // Redirect to dashboard
        navigate('/dashboard');
      }
    }

    handleCallback();
  }, [isAuthenticated, user]);

  if (isLoading) return <LoadingSpinner />;
  return null;
}
```

**Mobile Application (React Native / iOS):**

```swift
import Auth0

// LoginViewController.swift
class LoginViewController: UIViewController {
  func loginWithProvider(_ provider: String) {
    Auth0
      .webAuth()
      .connection(provider)
      .scope("openid profile email")
      .audience("https://api.cooking.gg")
      .start { result in
        switch result {
        case .success(let credentials):
          // Exchange Auth0 credentials for Cooking.gg session
          self.exchangeTokenForSession(credentials.accessToken)
        case .failure(let error):
          print("Auth0 login failed: \\(error)")
        }
      }
  }

  func exchangeTokenForSession(_ accessToken: String) {
    let url = URL(string: "https://api.cooking.gg/auth/callback")!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("Bearer \\(accessToken)", forHTTPHeaderField: "Authorization")

    URLSession.shared.dataTask(with: request) { data, response, error in
      // Handle session creation
      if let data = data {
        let session = try? JSONDecoder().decode(Session.self, from: data)
        // Store session and navigate to app
      }
    }.resume()
  }
}
```

### Backend Integration (Custom Callback)

**Auth0 Token Validation & User Creation:**

```javascript
// auth.controller.ts
import { expressjwt } from 'express-jwt';
import jwksRsa from 'jwks-rsa';

// Middleware: Validate Auth0 JWT token
const checkAuth0Token = expressjwt({
  secret: jwksRsa.expressJwtSecret({
    cache: true,
    rateLimit: true,
    jwksRequestsPerMinute: 5,
    jwksUri: `https://cooking.auth0.com/.well-known/jwks.json`
  }),
  audience: 'https://api.cooking.gg',
  issuer: `https://cooking.auth0.com/`,
  algorithms: ['RS256']
});

// POST /api/auth/callback
router.post('/callback', checkAuth0Token, async (req, res) => {
  try {
    const auth0UserId = req.body.auth0UserId;
    const auth0Token = req.auth;  // Validated JWT payload

    // Check if user exists
    let user = await User.findOne({ auth0_id: auth0UserId });

    if (!user) {
      // New user: create account and Turnkey wallet
      user = await createNewUser(auth0UserId, auth0Token);
    } else {
      // Existing user: update last login
      await user.update({ last_login: new Date() });
    }

    // Issue Cooking.gg session token
    const sessionToken = jwt.sign(
      { userId: user.id, walletAddress: user.wallet_address },
      process.env.JWT_SECRET,
      { expiresIn: '10h' }
    );

    res.json({
      token: sessionToken,
      user: {
        id: user.id,
        wallet_address: user.wallet_address,
        profile: user.profile
      }
    });
  } catch (error) {
    console.error('Auth callback error:', error);
    res.status(500).json({ error: 'Authentication failed' });
  }
});

// Create new user with Turnkey wallet
async function createNewUser(auth0UserId, auth0Token) {
  // Extract user profile from Auth0 token
  const profile = {
    name: auth0Token.name,
    email: auth0Token.email,
    picture: auth0Token.picture,
    provider: auth0Token.sub.split('|')[0]  // 'google-oauth2', 'twitter', 'apple'
  };

  // Create Turnkey wallet for user
  const wallet = await turnkey.createWallet({
    organizationId: process.env.TURNKEY_ORG_ID,
    walletName: `user-${auth0UserId}`,
    accounts: [{ curve: 'CURVE_SECP256K1', pathFormat: 'PATH_FORMAT_BIP32' }]
  });

  // Create user in database
  const user = await User.create({
    auth0_id: auth0UserId,
    wallet_address: wallet.address,
    turnkey_wallet_id: wallet.walletId,
    profile: profile,
    created_at: new Date()
  });

  return user;
}
```

### Custom Callback for Twitter Redirect Issues

**Problem:** Twitter OAuth redirects were failing with Auth0's default callback handling.

**Solution:** Custom callback URL configuration with manual state verification.

```javascript
// Twitter-specific callback handling
router.get('/auth/twitter/callback', async (req, res) => {
  const { code, state } = req.query;

  // Verify state parameter (CSRF protection)
  const storedState = req.session.auth_state;
  if (state !== storedState) {
    return res.status(400).json({ error: 'Invalid state parameter' });
  }

  try {
    // Exchange code for Auth0 token
    const tokenResponse = await fetch(`https://cooking.auth0.com/oauth/token`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        grant_type: 'authorization_code',
        client_id: process.env.AUTH0_CLIENT_ID,
        client_secret: process.env.AUTH0_CLIENT_SECRET,
        code: code,
        redirect_uri: `${process.env.API_URL}/auth/twitter/callback`
      })
    });

    const tokens = await tokenResponse.json();

    // Continue with user creation flow...
    // (same as generic callback above)

  } catch (error) {
    console.error('Twitter callback error:', error);
    res.redirect('/login?error=twitter_auth_failed');
  }
});
```

### Account Linking

**Allow users to link multiple social accounts to single Cooking.gg account:**

```javascript
// POST /api/auth/link-account
router.post('/link-account', authenticateUser, checkAuth0Token, async (req, res) => {
  const currentUserId = req.user.id;  // From existing session
  const newAuth0Id = req.body.auth0UserId;  // From new social login

  // Check if new Auth0 ID already linked to different user
  const existingUser = await User.findOne({ auth0_id: newAuth0Id });
  if (existingUser && existingUser.id !== currentUserId) {
    return res.status(400).json({
      error: 'This social account is already linked to another user'
    });
  }

  // Link new Auth0 ID to current user
  await UserAuth.create({
    user_id: currentUserId,
    auth0_id: newAuth0Id,
    provider: newAuth0Id.split('|')[0],
    linked_at: new Date()
  });

  res.json({ success: true, message: 'Account linked successfully' });
});
```

### Session Management

**Refresh Token Rotation:**

Auth0 configured with rotating refresh tokens for enhanced security:

```javascript
// Refresh access token using refresh token
async function refreshAccessToken(refreshToken) {
  const response = await fetch(`https://cooking.auth0.com/oauth/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      grant_type: 'refresh_token',
      client_id: process.env.AUTH0_CLIENT_ID,
      client_secret: process.env.AUTH0_CLIENT_SECRET,
      refresh_token: refreshToken
    })
  });

  const tokens = await response.json();
  return {
    accessToken: tokens.access_token,
    refreshToken: tokens.refresh_token,  // New refresh token
    expiresIn: tokens.expires_in
  };
}
```

**Frontend Refresh Logic:**

```javascript
// Auto-refresh access token before expiration
const { getAccessTokenSilently } = useAuth0();

useEffect(() => {
  const refreshInterval = setInterval(async () => {
    try {
      // Auth0 SDK handles refresh automatically
      await getAccessTokenSilently({ ignoreCache: true });
    } catch (error) {
      console.error('Token refresh failed:', error);
      // Redirect to login if refresh fails
      logout({ returnTo: window.location.origin });
    }
  }, 9 * 60 * 60 * 1000);  // Refresh every 9 hours (before 10h expiration)

  return () => clearInterval(refreshInterval);
}, []);
```

### Security Considerations

**Token Storage:**
- **Web:** LocalStorage for access token (XSS protection via Content Security Policy)
- **Mobile:** Keychain (iOS) / Keystore (Android) for secure credential storage
- **Refresh Tokens:** HttpOnly cookies (CSRF protection via SameSite attribute)

**CSRF Protection:**
- Auth0 state parameter validation
- SameSite=Strict cookies for refresh tokens
- Origin validation on backend

**Token Expiration:**
- Access tokens: 10 hours
- Refresh tokens: 30 days (rotating)
- Idle token lifetime: 15 days (session expires if inactive)

## Rationale

### Auth0 Over In-House Authentication

**Development Time Savings:**

In-house implementation estimate:
- OAuth 2.0 protocol implementation: 2-3 weeks per provider
- Session management and refresh tokens: 2 weeks
- Security hardening and testing: 2-3 weeks
- Cross-platform compatibility (web + mobile): 2 weeks
- **Total: 10-13 weeks (2.5-3 months) for basic functionality**

Auth0 implementation:
- Initial setup and configuration: 1 week
- Frontend integration: 1 week
- Backend custom callback: 1 week
- **Total: 3 weeks**

**Time saved: 7-10 weeks = 2-2.5 months of development effort**

**Security Benefits:**

- **Managed Infrastructure:** Auth0 handles security patches, vulnerability monitoring
- **Industry Best Practices:** OAuth 2.0, OpenID Connect, JWT standards compliance
- **Penetration Testing:** Auth0 platform regularly tested by security experts
- **Compliance:** SOC 2, ISO 27001, GDPR-compliant out-of-the-box
- **Rate Limiting:** Built-in DDoS protection and brute-force prevention
- **Anomaly Detection:** Suspicious login attempts flagged automatically

In-house approach requires:
- Dedicated security expertise
- Regular security audits
- Compliance certifications
- Ongoing vulnerability patching

**Scalability:**

- Auth0 handles millions of authentications per day (proven scale)
- No infrastructure scaling required (fully managed)
- Global CDN for low-latency login worldwide
- 99.9% uptime SLA

In-house approach requires:
- Scaling authentication servers as user base grows
- Geographic distribution for global users
- High-availability architecture

**Maintenance Burden:**

Auth0 handles:
- OAuth provider API changes (Twitter, Google, Apple update APIs regularly)
- Security vulnerability patches
- Protocol updates (OAuth 2.0 → OAuth 2.1 transition)
- Compliance requirement changes

In-house approach requires:
- Monitoring provider API changes
- Updating integration code when providers change APIs
- Ongoing security maintenance

### Turnkey Integration

**Improved User Creation Flow:**

Before Auth0:
1. User provides email/social login
2. Backend authenticates user
3. **Problem:** If Turnkey wallet creation fails, user is authenticated but has no wallet
4. Manual retry logic required
5. Edge cases: user refreshes page mid-creation

With Auth0:
1. User authenticates via Auth0 (proven reliable)
2. Backend receives validated Auth0 token
3. Create user and Turnkey wallet atomically
4. If Turnkey fails, transaction rolls back (no partial user state)
5. Auth0 session remains valid for retry

**Atomic User Creation:**

```javascript
// Transactional user creation with Auth0
async function createNewUser(auth0UserId, auth0Token) {
  const transaction = await database.beginTransaction();

  try {
    // Step 1: Create Turnkey wallet
    const wallet = await turnkey.createWallet({...});

    // Step 2: Create user in database
    const user = await User.create({
      auth0_id: auth0UserId,
      wallet_address: wallet.address,
      turnkey_wallet_id: wallet.walletId
    }, { transaction });

    // Commit transaction (all or nothing)
    await transaction.commit();
    return user;

  } catch (error) {
    // Rollback on any failure
    await transaction.rollback();
    throw error;
  }
}
```

### Cost-Benefit Analysis

**Auth0 Pricing:**
- Free tier: 7,500 monthly active users
- Essentials: ~$0.023/monthly active user (beyond free tier)
- Professional: ~$0.28/monthly active user (advanced features)

**Estimated Cost:**
- Launch (< 1,000 users): $0/month (free tier)
- Growth (10,000 users): ~$230/month (Essentials tier)
- Scale (100,000 users): ~$2,300/month (Essentials tier)

**Alternative (In-House) Cost:**
- Development: 2.5 months × $10,000/month (developer salary) = $25,000
- Infrastructure: ~$500/month (authentication servers, load balancers)
- Security audits: $10,000-$20,000/year
- Ongoing maintenance: 0.5 FTE developer (~$5,000/month)
- **First year total: $25,000 + $6,000 + $15,000 + $60,000 = $106,000**

**Auth0 vs In-House (First Year):**
- Auth0: ~$10,000 (assuming 25,000 average monthly active users)
- In-House: ~$106,000
- **Savings: $96,000 in first year**

**ROI:** Auth0 pays for itself immediately. Development time saved deployed to core features.

## Consequences

### Positive

**Development Velocity:**
- 2-2.5 months saved vs in-house implementation
- Engineers focus on core trading platform features
- Faster time-to-market for user onboarding

**Security:**
- Industry-leading security practices (OAuth 2.0, OpenID Connect)
- Managed vulnerability patching and monitoring
- SOC 2, ISO 27001, GDPR compliance out-of-the-box
- Anomaly detection and brute-force protection

**User Experience:**
- Familiar social login flow (users expect Twitter/Google/Apple)
- Fast authentication (< 2 seconds typical)
- Cross-device session synchronization
- Account linking for flexibility

**Scalability:**
- Proven to handle millions of users (Auth0 customer base)
- No infrastructure scaling required
- Global CDN for low latency worldwide
- 99.9% uptime SLA

**Turnkey Integration:**
- Improved user creation flow (atomic transactions)
- Better error handling and retry logic
- Reduced edge cases in wallet creation

**Maintenance:**
- OAuth provider API updates handled by Auth0
- Security patches applied automatically
- No ongoing authentication infrastructure maintenance

### Negative

**Vendor Lock-In:**
- Migration away from Auth0 costly (user session disruption)
- Custom integrations (Turnkey callback) may not transfer to alternative
- Dependent on Auth0's pricing and roadmap

**Cost at Scale:**
- Free tier limited to 7,500 monthly active users
- Cost grows linearly with user base ($0.023/user on Essentials)
- At 100,000 users: ~$2,300/month ($27,600/year)
- At 1,000,000 users: ~$23,000/month ($276,000/year)

**Limited Customization:**
- Universal Login UI customization limited (Auth0-hosted page)
- Cannot fully white-label authentication flow
- Some branding constraints

**Third-Party Dependency:**
- Auth0 outages block user logins (mitigated by 99.9% SLA)
- API rate limits (normally generous, but exist)
- Auth0 policy changes may affect service

**Privacy Concerns:**
- User authentication data flows through Auth0 servers
- Subject to Auth0's data retention policies
- May require additional privacy policy disclosures

**Learning Curve:**
- Team must learn Auth0 concepts (connections, rules, hooks)
- Debugging auth issues requires Auth0 dashboard familiarity
- Custom callback logic adds complexity

**Twitter Integration Challenges:**
- Required custom callback workaround for redirect issues
- Twitter API changes may require integration updates
- Additional configuration complexity

### Neutral

**Custom Callback Complexity:**
- Required for Twitter integration (adds backend code)
- Flexibility benefit (can customize user creation flow)
- Trade-off: more control vs more code to maintain

**Account Linking:**
- Feature complexity (multiple auth methods per user)
- Flexibility benefit (users prefer choice)
- Requires careful UX design (avoid confusion)

## Alternatives Considered

### Option 1: In-House OAuth 2.0 Implementation

**Description:** Build custom OAuth 2.0 integration for each social provider

**Pros:**
- Full control over authentication flow
- No per-user cost
- No vendor lock-in
- Complete customization of UI/UX
- User data remains entirely internal

**Cons:**
- 2-3 months development time (vs 3 weeks with Auth0)
- Security burden (vulnerabilities, patches, compliance)
- Ongoing maintenance (OAuth provider API changes)
- Scaling infrastructure costs
- No proven track record (Auth0 handles millions of auths)

**Why Rejected:** Development time and security risk outweigh cost savings. Core team should focus on trading platform features, not authentication infrastructure.

### Option 2: Firebase Authentication

**Description:** Use Google's Firebase Authentication service

**Pros:**
- Managed authentication (similar to Auth0)
- Free tier: 50,000 monthly active users
- Good mobile SDK support
- Integrated with Google Cloud Platform

**Cons:**
- Less flexible than Auth0 (fewer customization options)
- Custom callback handling more difficult
- Limited enterprise features (no anomaly detection, advanced rules)
- Google ecosystem lock-in
- Less mature OAuth provider support (Twitter issues reported)

**Why Rejected:** Auth0 more flexible for Turnkey integration custom callback. Firebase better for simple use cases, but Cooking.gg requires custom user creation flow.

### Option 3: AWS Cognito

**Description:** Use Amazon's Cognito user authentication service

**Pros:**
- Integrated with AWS ecosystem (Cooking.gg uses AWS)
- Competitive pricing (~$0.0055/monthly active user beyond free tier)
- Supports social login providers
- No vendor lock-in (open standards: OAuth, OpenID)

**Cons:**
- More complex configuration than Auth0
- Less polished developer experience (steeper learning curve)
- Limited customization of login UI
- Custom OAuth flows more difficult
- Weaker documentation and community support

**Why Rejected:** Developer experience significantly worse than Auth0. Time-to-implement longer, higher risk of configuration errors. Cost savings (~$0.018/user vs Auth0's $0.023/user) not worth complexity increase.

### Option 4: Supabase Auth

**Description:** Use Supabase's open-source authentication service

**Pros:**
- Open-source (can self-host if needed)
- No vendor lock-in
- Generous free tier
- Modern developer experience
- Built-in Row Level Security

**Cons:**
- Less mature than Auth0 (newer platform)
- Smaller community and ecosystem
- Limited enterprise features
- Self-hosting requires infrastructure management
- Less proven at scale

**Why Rejected:** Maturity concerns. Auth0's proven track record at scale more important than open-source benefits. Supabase better for startups prioritizing cost over features.

### Option 5: Clerk

**Description:** Modern authentication platform (Auth0 competitor)

**Pros:**
- Modern developer experience
- Better UI customization than Auth0
- Good documentation
- Supports social login providers

**Cons:**
- Less mature than Auth0 (founded 2020 vs Auth0 2013)
- Smaller customer base (less proven at scale)
- Higher pricing ($0.02/user on free tier limit vs Auth0 Essentials)
- Smaller ecosystem (fewer integrations)

**Why Rejected:** Auth0 more established and proven. Clerk's UI advantages not critical for Cooking.gg (users expect standard social login flow).

## Implementation Notes

### Auth0 Tenant Configuration

**Production Tenant:**
- Domain: `cooking.auth0.com`
- Region: US (closest to AWS us-east-1 backend)
- Environment tag: `production`

**Development Tenant:**
- Domain: `cooking-dev.auth0.com`
- Separate tenant for testing (avoid polluting production user base)

### Monitoring and Alerting

**Key Metrics:**

```javascript
// Track authentication success/failure rates
metrics.counter('auth.login.success', 1, {
  provider: 'twitter' | 'google' | 'apple'
});

metrics.counter('auth.login.failure', 1, {
  provider: 'twitter' | 'google' | 'apple',
  error: error.code
});

// Track token refresh success/failure
metrics.counter('auth.refresh.success', 1);
metrics.counter('auth.refresh.failure', 1);

// Track Turnkey wallet creation
metrics.counter('auth.wallet.creation.success', 1);
metrics.counter('auth.wallet.creation.failure', 1, {
  error: error.code
});

// Track authentication latency
metrics.histogram('auth.callback.duration', durationMs);
```

**Alerts:**

- Auth failure rate > 5%: Warning (may indicate provider outage)
- Auth failure rate > 20%: Critical (Auth0 or provider issue)
- Turnkey wallet creation failure rate > 10%: Warning (Turnkey API issue)
- Token refresh failure rate > 5%: Warning (session management issue)

### Testing Strategy

**Unit Tests:**
- JWT token validation logic
- User creation flow (mock Turnkey API)
- Account linking logic

**Integration Tests:**
- Full auth flow with Auth0 test environment
- Turnkey wallet creation (using Turnkey sandbox)
- Token refresh flow

**E2E Tests:**
- Social login flow (Twitter, Google, Apple) in staging
- Account linking across providers
- Session persistence across page refreshes

## References

### Meeting Notes
- [Daily Standup 2025-08-01](../06-meetings/2025-08/2025-08-01-daily-standup.md) - Auth0 integration kickoff, Twitter redirect issues
- [Daily Standup 2025-08-08](../06-meetings/2025-08/2025-08-08-daily-standup.md) - Auth0 integration completion
- [Weekly Demo 2025-08-08](../06-meetings/2025-08/Weekly-Demo-2025-08-08.md) - Auth0 and Turnkey integration

### Related Decisions
- ADR-400: Security Password for Wallet Operations (additional security layer)

### Technical References
- Auth0 Documentation: https://auth0.com/docs
- Auth0 React SDK: https://auth0.com/docs/libraries/auth0-react
- Auth0 iOS SDK: https://auth0.com/docs/libraries/auth0-swift
- OAuth 2.0 Specification: https://datatracker.ietf.org/doc/html/rfc6749
- OpenID Connect: https://openid.net/connect/
- Turnkey API Documentation: https://docs.turnkey.com

### Security References
- OAuth 2.0 Security Best Practices: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics
- JWT Best Practices: https://datatracker.ietf.org/doc/html/rfc8725

## Revision History
- 2025-08-01: Auth0 integration decision made, Twitter custom callback required
- 2025-08-08: Auth0 fully operational (all social providers working)
- 2025-08-11: Auth0 integration complete, performance optimizations applied
- 2025-10-21: Formal ADR documented from meeting notes
