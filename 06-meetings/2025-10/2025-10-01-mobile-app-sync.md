---
title: Mobile App Sync - 2025-10-01
type: meeting
meeting_type: technical_deep_dive
topic: Mobile
date: 2025-10-01
attendees: [Lucas Cufre, Martin Aranda, Gregory Chapman, Naji Osmat, Marcos Tacca]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Mobile App Sync Technical Discussion - Cooking.gg
**Date:** October 1, 2025, 11:29 GMT-03:00
**Duration:** ~55 minutes
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Gregory Chapman, Naji Osmat, Marcos Tacca

## Executive Summary
Synchronization meeting for mobile app development progress, covering React Native implementation status, iOS-specific features, state management, API integration, and pre-launch testing requirements. Team aligned on final UI/UX details and identified remaining technical blockers before beta launch.

## Meeting Context
With beta launch approaching, the team needed to ensure mobile app feature parity with web, address platform-specific implementation challenges, finalize UI/UX decisions, and establish testing protocols for both iOS and Android platforms.

## Technical Discussion

### React Native Implementation Status
**Completed Features**:
- Token discovery and search
- Market orders (buy/sell)
- Portfolio view with P&L tracking
- Price charts (basic candlestick)
- Wallet integration (Phantom, Solflare)
- Push notifications setup
- Deep linking for referrals

**In Progress**:
- Limit orders with TP/SL
- TradingView chart integration
- Haptic feedback implementation
- Offline mode caching
- Biometric authentication

**Blocked/Pending**:
- App store submission materials
- TestFlight beta distribution setup
- Performance optimization for Android

### iOS-Specific Implementation Challenges
**Face ID / Touch ID Integration**:
- Using `react-native-biometrics` library
- Secure Enclave for private key storage
- Fallback to PIN/password if biometrics unavailable
- User preference persistence

**Push Notifications**:
- APNs (Apple Push Notification service) configuration
- Certificate management in Apple Developer account
- Notification categories: price alerts, order fills, system announcements
- Grouped notifications to avoid spam

**App Store Requirements**:
- Privacy policy and terms of service URLs
- App Store Connect metadata (screenshots, description)
- Age rating (17+ due to financial trading)
- Export compliance documentation

### State Management Architecture
**Redux Toolkit Implementation**:
- Centralized state for user data, portfolio, orders, tokens
- Persist key state to AsyncStorage (watchlists, preferences)
- Optimistic updates for better perceived performance
- RTK Query for API caching and automatic refetching

**State Slices**:
```javascript
{
  user: { authenticated, walletAddress, preferences },
  portfolio: { tokens, totalValue, pnl },
  orders: { active, history },
  markets: { tokens, prices, charts },
  ui: { theme, notifications, modals }
}
```

### API Integration & Caching
**API Client Architecture**:
- Axios with request/response interceptors
- JWT token refresh logic
- Retry mechanism for failed requests
- Request deduplication for concurrent calls

**Caching Strategy**:
- Cache static data (token metadata, logos) indefinitely
- Cache prices for 2 seconds
- Cache portfolio for 5 seconds
- Cache order history for 30 seconds
- Invalidate on user actions (trades, orders)

### Offline Mode Support
**Offline Capabilities**:
- View cached portfolio and token list
- Access saved watchlists
- View historical charts (last fetched data)
- Queue actions for when connection restored

**Sync Strategy**:
- Detect network status with `@react-native-community/netinfo`
- Display offline indicator in UI
- Show last updated timestamp
- Automatic sync when connection restored

### Performance Optimization
**React Native Performance Best Practices**:
- FlatList with `windowSize` optimization for long lists
- Image lazy loading and caching
- Memoization of expensive components
- Debounced search input
- Virtualized lists for token discovery

**Bundle Size Optimization**:
- Code splitting per screen (lazy loading)
- Remove unused dependencies
- Optimize images (WebP format, compressed)
- Tree-shaking for unused code

**Startup Time**:
- Target: < 3 seconds from tap to usable
- Splash screen while loading initial data
- Skeleton screens for perceived performance
- Lazy load non-critical screens

### Testing Strategy
**Unit Tests**:
- Jest for business logic and utilities
- Test Redux reducers and selectors
- Mock API responses

**Integration Tests**:
- Test navigation flows
- Test API integration with mock server
- Test state management across screens

**E2E Tests**:
- Detox for automated UI testing
- Critical user flows: login, trade, view portfolio
- Run on both iOS and Android simulators

**Beta Testing**:
- TestFlight for iOS (invite-only, 30-40 users)
- Google Play Internal Testing for Android
- Crash reporting with Sentry
- Analytics with Mixpanel/Amplitude

## Key Technical Decisions
- **Decision 1:** Redux Toolkit for state management - Developer experience and debugging tools
- **Decision 2:** AsyncStorage for persistence - Simple, reliable, sufficient for current needs
- **Decision 3:** Offline-first architecture with sync - Better UX, works on poor connections
- **Decision 4:** Biometric authentication required for trading - Enhanced security for financial app
- **Decision 5:** TestFlight beta before public launch - Gather feedback, catch bugs early

## Architecture & Design Considerations
- **Platform Parity**: Ensure iOS and Android have identical features
- **Responsive Design**: Support all device sizes (small phones to tablets)
- **Accessibility**: VoiceOver/TalkBack support for core features
- **Error Handling**: User-friendly error messages, fallback UIs
- **Analytics**: Track key events for product insights

## Performance & Scalability Notes
- **Memory Management**: Monitor memory usage, prevent leaks in long sessions
- **Network Efficiency**: Minimize API calls, batch requests where possible
- **Battery Impact**: Optimize background tasks, use efficient polling intervals
- **App Size**: Target < 50MB download size

## Action Items
- [ ] **Martin**: Implement biometric authentication for iOS and Android
- [ ] **Gregory**: Finalize App Store Connect metadata and screenshots
- [ ] **Naji**: Complete haptic feedback implementation per design spec
- [ ] **Lucas**: Write privacy policy and terms of service
- [ ] **Team**: Set up TestFlight and invite beta testers
- [ ] **Martin**: Implement crash reporting with Sentry

## Follow-up Items
- Plan Android-specific testing (various device manufacturers)
- Evaluate performance on low-end devices
- Determine analytics events to track
- Plan for app store review process and timeline

---
**Recording:** Transcription available
**Related Documents:**
- Mobile App Architecture (04-knowledge-base/technical/)
- React Native Best Practices (04-knowledge-base/technical/)
