---
title: Mobile Filters - 2025-07-24
type: meeting
meeting_type: technical_deep_dive
topic: Mobile Filters
date: 2025-07-24
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Gregory Chapman]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Mobile Filters Technical Discussion - Cooking.gg
**Date:** July 24, 2025
**Duration:** ~45 minutes
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Gregory Chapman

## Executive Summary
The team discussed implementing advanced token filtering and discovery features for the mobile application, focusing on performance optimization, search functionality, and user experience patterns specific to mobile devices. Key decisions included implementing client-side filtering with smart caching, designing mobile-specific filter UI patterns, and establishing search indexing strategies.

## Meeting Context
As Cooking.gg prepares to launch its mobile application, the team needed to design and implement efficient token filtering and search capabilities optimized for mobile constraints including limited screen space, touch interactions, network latency, and device performance considerations.

## Technical Discussion

### Mobile Filter Architecture
**Core Requirements**:
- Fast, responsive filtering even with 10,000+ tokens
- Low bandwidth consumption for mobile networks
- Intuitive touch-based interface
- Persistent filter state across app sessions

**Technical Approach Decided**:
1. **Hybrid Filtering Model**: Combine server-side initial data fetch with client-side filtering
2. **Smart Caching**: Cache token metadata locally with delta updates
3. **Lazy Loading**: Load token details on-demand as user scrolls
4. **Debounced Search**: Implement search query debouncing to reduce API calls

### Filter Categories & Dimensions
**Primary Filter Dimensions**:
1. **Market Stage**:
   - Kitchen (bonding curve < 100%)
   - Graduated (launched on DEX)
   - Established (high liquidity, >24hr volume threshold)

2. **Time-Based Metrics**:
   - Age (launch time)
   - Trading volume (1h, 24h, 7d)
   - Price change (1h, 24h, 7d)
   - Holder count change

3. **Risk Indicators**:
   - Liquidity depth
   - Holder concentration
   - Token age
   - Contract verification status

4. **Social Metrics**:
   - Twitter mentions
   - Telegram members
   - Website presence
   - Audit status

**Filter UI Patterns for Mobile**:
- **Bottom Sheet**: Primary filter interface slides up from bottom
- **Chips**: Active filters displayed as dismissible chips
- **Quick Filters**: Horizontal scrollable row for most common filters
- **Saved Filter Presets**: User can save and quickly apply favorite filter combinations

### Search Functionality Architecture
**Search Strategy**:
- **Elasticsearch Integration**: Full-text search index for token names, symbols, and descriptions
- **Fuzzy Matching**: Tolerate typos and partial matches
- **Weighted Results**: Prioritize by trading volume, liquidity, and social mentions
- **Search History**: Store last 10 searches locally for quick access

**Search Performance Optimizations**:
1. **Debouncing**: 300ms delay before triggering search query
2. **Minimum Character Threshold**: Require 2+ characters before searching
3. **Result Caching**: Cache search results for 60 seconds
4. **Prefetching**: Preload top 20 search results for common queries

**Search UI Components**:
- Persistent search bar at top of Explore screen
- Recent searches displayed when search bar focused
- Trending searches suggestions
- Clear visual indication of search filters applied

### Mobile-Specific UX Considerations
**Touch Interaction Patterns**:
- **Swipe Actions**: Swipe on token card to quickly add to watchlist or share
- **Long Press**: Long press to view token details preview sheet
- **Pull to Refresh**: Standard pull-down gesture to refresh token list
- **Infinite Scroll**: Load more tokens as user reaches bottom of list

**Screen Space Optimization**:
- **Collapsible Sections**: Chart, token details, and trade history collapsible
- **Tabs vs Scrolling**: Use tabs for major sections, vertical scroll within sections
- **Sticky Headers**: Keep key metrics visible while scrolling

**Performance Constraints**:
- Limit rendered token cards to 50 at a time with virtualization
- Use image lazy loading for token logos
- Implement skeleton screens for perceived performance
- Optimize re-renders with React.memo and useCallback

### Data Synchronization Strategy
**Real-Time Updates**:
- **WebSocket Connection**: Maintain single WebSocket for price updates
- **Selective Subscriptions**: Only subscribe to visible token price feeds
- **Batch Updates**: Aggregate updates and apply every 1-2 seconds to reduce re-renders
- **Background Sync**: Refresh token list data every 30 seconds when app in foreground

**Offline Handling**:
- Cache last fetched token list for offline viewing
- Display clear "offline mode" indicator
- Queue filter/search actions to execute when connection restored
- Graceful degradation of real-time features

### Filter Persistence & State Management
**State Architecture**:
- **Local Storage**: Persist active filters, search history, and view preferences
- **URL State (Web)**: Encode filters in URL for shareability
- **Redux Store**: Centralized state management for filters, search, and token list
- **Optimistic Updates**: Apply filters immediately to UI while background fetching occurs

**Filter State Schema**:
```json
{
  "filters": {
    "marketStage": ["kitchen", "graduated"],
    "volumeRange": {"min": 1000, "max": null},
    "priceChange24h": {"min": 5, "max": null},
    "liquidityMin": 5000,
    "verified": true
  },
  "sort": {
    "field": "volume24h",
    "direction": "desc"
  },
  "searchQuery": "pepe",
  "savedPresets": [...]
}
```

## Key Technical Decisions
- **Decision 1:** Hybrid filtering (server + client) - Balances performance with flexibility; server handles initial heavy filtering, client provides instant responsiveness
- **Decision 2:** Elasticsearch for search - Provides powerful full-text search with fuzzy matching and weighting capabilities
- **Decision 3:** Bottom sheet filter UI - Most intuitive mobile pattern, maximizes screen space, familiar to users
- **Decision 4:** Virtualized list rendering - Essential for performance with large token lists on mobile devices
- **Decision 5:** Filter state persistence in local storage - Improves UX by remembering user preferences across sessions

## Architecture & Design Considerations
- **Component Reusability**: Design filter components to work across mobile and web with responsive adaptations
- **API Design**: Create dedicated `/tokens/filter` endpoint optimized for mobile payloads
- **Caching Strategy**: Implement multi-tier caching (memory, local storage, service worker)
- **Progressive Enhancement**: Core functionality works without JavaScript, enhanced with interactive features
- **Accessibility**: Ensure filter controls work with screen readers and keyboard navigation

## Performance & Scalability Notes
- **Initial Load Target**: < 3 seconds to display first 20 tokens on 3G connection
- **Filter Application**: < 100ms to apply filters and update UI
- **Search Response**: < 500ms for search results to appear
- **Memory Management**: Limit in-memory token cache to 1000 items
- **Bundle Size**: Filter/search features should add < 50KB to bundle

## Action Items
- [ ] **Eduardo**: Set up Elasticsearch index for token search with appropriate field mappings
- [ ] **Martin**: Implement virtualized list component using react-window or similar
- [ ] **Gregory**: Design bottom sheet filter UI with all filter categories
- [ ] **Lucas**: Define API contracts for filter and search endpoints
- [ ] **Martin**: Implement client-side filter logic with debouncing and caching
- [ ] **Team**: Create filter preset templates for common use cases (e.g., "New Launches", "High Volume", "Low Risk")

## Follow-up Items
- Determine analytics events to track for filter usage patterns
- Plan A/B test for different filter UI layouts
- Evaluate adding ML-powered "Recommended for You" filter
- Design export functionality for filtered token lists

## Technical References
- React Window Documentation: https://github.com/bvaughn/react-window
- Elasticsearch Mobile Best Practices: https://www.elastic.co/guide/en/elasticsearch/reference/current/tune-for-search-speed.html
- Mobile Filter UI Patterns: https://www.nngroup.com/articles/mobile-filtering/
- Redux Toolkit Best Practices: https://redux-toolkit.js.org/usage/usage-guide

---
**Recording:** Transcription available
**Related Documents:**
- Mobile App Architecture Doc (04-knowledge-base/technical/)
- Token Data Schema (04-knowledge-base/technical/)
- Mobile UX Guidelines (04-knowledge-base/design/)
