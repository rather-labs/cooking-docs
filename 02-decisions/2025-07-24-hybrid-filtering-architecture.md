---
title: Hybrid Filtering Architecture (Server + Client)
type: decision-record
decision-id: ADR-004
date: 2025-07-24
status: accepted
owner: Martin Aranda, Lucas Cufre
stakeholders: [Martin Aranda, Lucas Cufre, Eduardo Yuschuk, Gregory Chapman, Mobile Team, Backend Team]
tags: [architecture, mobile, filtering, performance, user-experience, caching]
summary: |
  Decision to implement hybrid filtering architecture combining server-side initial data fetch with client-side filtering for mobile token discovery. Server handles heavy filtering and initial data reduction, while client provides instant (<100ms) filter application without additional API calls. Optimized for mobile constraints including limited bandwidth, touch interactions, and device performance.
related-docs:
  - ../06-meetings/2025-07/2025-07-24-mobile-filters.md
  - ../04-knowledge-base/business/requirements/mobile-app-prd.md
---

# Hybrid Filtering Architecture (Server + Client)

## Context and Problem Statement

Cooking.gg mobile application requires advanced token filtering and discovery capabilities to help users navigate 10,000+ tokens in real-time. Users need to filter by multiple dimensions including market stage, trading volume, price changes, risk indicators, and social metrics.

**Mobile-Specific Challenges:**

1. **Performance Constraints**:
   - Limited device processing power compared to desktop
   - Battery consumption concerns for intensive operations
   - Memory limitations (cannot load all token data at once)
   - Older devices with slower JavaScript execution

2. **Network Limitations**:
   - High latency on 3G/4G mobile networks
   - Bandwidth costs for users on metered data plans
   - Unreliable connectivity (subway, rural areas, poor signal)
   - Need for offline functionality

3. **User Experience Requirements**:
   - Instant feedback when applying filters (<100ms expectation)
   - Smooth scrolling through filtered results (60fps)
   - Touch-optimized interface (swipe, long-press, pull-to-refresh)
   - Limited screen space (maximize content, minimize UI chrome)

4. **Data Volume Challenge**:
   - 10,000+ tokens with real-time price updates
   - Each token has 50+ filterable attributes
   - Full dataset = ~50MB of JSON (too large to fetch entirely)
   - Filters can combine multiple dimensions (complex queries)

**Architectural Choices to Consider:**
- Pure server-side filtering (every filter change = API call)
- Pure client-side filtering (fetch all data upfront, filter locally)
- Hybrid approach (combine both strategies)
- Progressive loading with pagination
- Smart caching with delta updates

**Key Requirements:**
- Initial load: <3 seconds on 3G connection
- Filter application: <100ms UI response
- Search response: <500ms
- Support offline viewing of last fetched results
- Persist user filter preferences across sessions
- Real-time price updates for visible tokens only

## Decision

**Implement hybrid filtering architecture: server-side initial heavy filtering combined with client-side instant filter application, optimized with smart caching and virtualized rendering.**

### Architecture Components

**Server-Side Responsibilities:**
1. **Initial Heavy Filtering**:
   - Process complex queries on full 10,000+ token dataset
   - Apply baseline filters (market stage, liquidity thresholds)
   - Return optimized, reduced dataset (typically 500-2000 tokens)
   - Dedicated `/api/tokens/filter` endpoint optimized for mobile payloads

2. **Search Indexing**:
   - Elasticsearch integration for full-text search
   - Fuzzy matching for typo tolerance
   - Weighted results by volume, liquidity, social metrics
   - Prefetch top 20 results for common queries

3. **Data Optimization**:
   - Compress response payloads (gzip)
   - Return only necessary fields for initial view
   - Lazy load detailed data on-demand
   - Delta updates for price changes (not full object refresh)

**Client-Side Responsibilities:**
1. **Instant Filter Application**:
   - Apply filters to cached dataset without API call
   - Target: <100ms filter application time
   - Debounced search (300ms delay before API call)
   - Optimistic UI updates (apply immediately, fetch in background)

2. **Smart Caching**:
   - Memory cache: Up to 1000 tokens in-memory
   - Local storage: Persist last fetched dataset for offline viewing
   - Result caching: 60-second window for search results
   - Multi-tier caching: memory → local storage → API

3. **Performance Optimizations**:
   - Virtualized list rendering (react-window): render only 50 visible cards
   - Image lazy loading for token logos
   - Skeleton screens for perceived performance
   - React.memo and useCallback to minimize re-renders

4. **Filter State Management**:
   - Redux store for centralized filter state
   - Local storage persistence across sessions
   - URL state encoding for shareability (web)
   - Saved filter presets for quick access

**Real-Time Updates:**
- Single WebSocket connection for price updates
- Selective subscriptions (only visible tokens)
- Batch updates every 1-2 seconds (reduce re-renders)
- Background sync every 30 seconds when app in foreground

### Filtering Strategy by Dimension

**Client-Side Filters (Instant Application):**
- Market stage (Kitchen, Graduated, Established)
- Price change ranges (1h, 24h, 7d)
- Volume ranges
- Holder count changes
- Liquidity depth
- Token age
- Sort order changes

**Server-Side Filters (Initial Fetch):**
- Full-text search (Elasticsearch)
- Complex multi-dimensional queries
- Trending calculations (requires full dataset analysis)
- Risk scoring (aggregated metrics)
- Social metrics (external API integrations)

**Hybrid Filters (Client First, Server Fallback):**
- Volume thresholds: Client filters cached data, server provides fresh data
- Liquidity: Client applies to cached, server ensures accuracy
- Verified tokens: Client filters, server validates contract status

### Mobile UI Pattern

**Bottom Sheet Filter Interface:**
- Slides up from bottom (maximizes screen space)
- Collapsible sections for filter categories
- Active filters displayed as dismissible chips
- Horizontal scrollable quick filters row
- Saved presets for common filter combinations

**Filter State Schema:**
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
  "savedPresets": [
    {"name": "New Launches", "filters": {...}},
    {"name": "High Volume", "filters": {...}}
  ]
}
```

## Rationale

### Why Hybrid Over Pure Server-Side

**Pure Server-Side Problems:**
- Every filter change requires API call (latency: 200-1000ms on mobile)
- High server load for filter experimentation (users try multiple filter combinations)
- Poor user experience (loading spinners, delayed feedback)
- Wasted bandwidth for similar queries
- Difficult to provide instant feedback for UI interactions

**Hybrid Advantages:**
- Initial server filtering reduces dataset to manageable size
- Client filtering provides instant feedback (<100ms)
- Reduced API calls (only when necessary)
- Better offline experience (last results cached)
- Lower server costs (fewer requests)

**Team Decision Context:**
> "Hybrid filtering (server + client) - Balances performance with flexibility; server handles initial heavy filtering, client provides instant responsiveness"

### Why Hybrid Over Pure Client-Side

**Pure Client-Side Problems:**
- Initial data fetch too large (~50MB for all tokens)
- Mobile bandwidth costs for users
- Cannot handle 10,000+ tokens efficiently on low-end devices
- Search requires full-text indexing (complex client-side)
- Real-time updates expensive (all token prices)

**Hybrid Advantages:**
- Server reduces initial data transfer (500-2000 tokens vs. 10,000)
- Elasticsearch provides superior search (fuzzy matching, weighting)
- Fresh data on each API call (no stale cache issues)
- Complex calculations offloaded to server
- Can leverage server-side caching (Redis)

### Mobile Performance Targets Met

**Performance Metrics:**
- ✅ Initial load: <3 seconds on 3G (server pre-filtering reduces payload)
- ✅ Filter application: <100ms (client-side instant filtering)
- ✅ Search response: <500ms (Elasticsearch + result caching)
- ✅ Bundle size: <50KB for filter features (virtualized lists prevent bloat)
- ✅ Memory management: 1000 token limit (prevents device crashes)

**Battery & Resource Optimization:**
- Virtualized rendering: Only 50 DOM nodes instead of 10,000+
- Batched updates: 1-2 second intervals (not every price tick)
- Selective WebSocket subscriptions: Only visible tokens
- Debounced search: 300ms delay prevents API spam

### User Experience Benefits

**Instant Feedback:**
- User changes filter → UI updates immediately (<100ms)
- No loading spinners for filter changes
- Smooth 60fps scrolling (virtualized rendering)
- Optimistic updates (apply filter, fetch fresh data in background)

**Offline Capability:**
- Last fetched results cached in local storage
- Users can browse previously loaded tokens offline
- Clear "offline mode" indicator
- Graceful degradation of real-time features

**Progressive Enhancement:**
- Works with poor network (server filtering reduces data)
- Works offline (client filtering on cached data)
- Works on slow devices (virtualized rendering)
- Touch-optimized (bottom sheet, swipe actions)

### Elasticsearch for Search

**Why Elasticsearch:**
- Full-text search across token names, symbols, descriptions
- Fuzzy matching (tolerates typos: "shib" finds "shiba")
- Weighted results (prioritize by volume, liquidity, social metrics)
- Fast (sub-100ms search on indexed data)
- Scalable (handles growing token database)

**Alternatives Rejected:**
- Client-side search: Limited capabilities, no fuzzy matching
- PostgreSQL full-text search: Slower, less sophisticated
- Third-party search APIs: Vendor lock-in, latency

**Optimization:**
- Prefetch top 20 results for common queries ("pepe", "doge", "solana")
- 60-second result caching
- Minimum 2 characters before triggering search
- 300ms debounce to batch keystrokes

## Consequences

### Positive

**User Experience:**
- Instant filter application creates responsive, native-app feel
- No loading spinners for filter changes (feels fast)
- Offline viewing of last results (works in subway, poor signal)
- Saved presets speed up common workflows
- Touch-optimized bottom sheet interface (mobile best practice)

**Performance:**
- <100ms filter application (instant feedback)
- Virtualized rendering handles 10,000+ tokens smoothly
- Reduced API calls (lower bandwidth consumption)
- Battery-efficient (batched updates, selective subscriptions)
- Works well on low-end devices (server does heavy lifting)

**Scalability:**
- Server caching (Redis) benefits all users
- Client caching reduces server load
- Elasticsearch scales independently
- Can add more filter dimensions without client-side complexity
- Progressive enhancement handles growing token database

**Development Velocity:**
- Clear separation of concerns (server vs. client filtering)
- Can optimize each layer independently
- Easier to A/B test filter UI (client-side changes)
- Reusable filter components across web and mobile

**Cost Efficiency:**
- Reduced API calls (fewer server resources)
- Client-side filtering offloads computation
- Elasticsearch more efficient than complex SQL queries
- Lower bandwidth costs for users (smaller payloads)

### Negative

**Implementation Complexity:**
- Two filtering systems to maintain (server + client)
- Cache invalidation challenges (when to refresh?)
- State synchronization between server and client
- Need to handle edge cases (stale cache, offline mode)
- More complex testing (integration tests across layers)

**Cache Staleness Risk:**
- Client cache may have outdated data (60-second window)
- User might filter on stale prices
- Mitigation: Background sync every 30 seconds, visual freshness indicator

**Initial Load Still Required:**
- First visit requires server call (cannot avoid)
- 3-second target on 3G (acceptable but not instant)
- Subsequent filter changes fast, but initial experience slower

**Memory Management:**
- Must limit in-memory cache to 1000 tokens
- Garbage collection needed for old cached data
- Memory leaks possible if not managed carefully
- Testing required across device tiers

**Offline Limitations:**
- Can only browse last fetched results offline
- No search offline (Elasticsearch server-side)
- No fresh data offline (obviously)
- Must communicate limitations clearly to users

**Dual Codebase:**
- Filter logic exists in both server (initial) and client (instant)
- Risk of inconsistencies between implementations
- Must keep filter schemas in sync
- More code to maintain and test

### Neutral

- Bottom sheet UI pattern (standard on mobile, but desktop needs modal)
- WebSocket for real-time updates (aligns with SSE migration - see ADR-003)
- Redux for state management (team already using Redux)
- Local storage persistence (privacy implications, but useful)
- Elasticsearch adds infrastructure dependency (but powerful)

## Alternatives Considered

### Option 1: Pure Server-Side Filtering
**Description:** Every filter change triggers API call, all filtering happens server-side

**Pros:**
- Simplest client code (just send filter params, render results)
- Always fresh data (no cache staleness)
- Complex queries easy (full database access)
- No client-side memory concerns
- Single source of truth

**Cons:**
- Poor mobile UX (200-1000ms latency per filter change)
- High server load (users experiment with filters)
- Wasted bandwidth (repeated similar queries)
- Loading spinners everywhere (feels slow)
- Cannot work offline at all

**Why Rejected:** User experience unacceptable. Instant filter feedback critical for mobile discovery experience. Competitors using client-side filtering would feel much faster.

### Option 2: Pure Client-Side Filtering
**Description:** Fetch all 10,000+ tokens upfront, do all filtering in JavaScript

**Pros:**
- Instant filter application (no network latency)
- Works fully offline after initial load
- No API calls after first fetch (lower server costs)
- Simpler architecture (single filtering system)
- Can implement complex client-side analytics

**Cons:**
- Initial fetch too large (~50MB JSON for all tokens)
- Bandwidth cost for mobile users on metered data
- Cannot run on low-end devices (memory constraints)
- Search limited (no Elasticsearch fuzzy matching)
- Real-time updates expensive (10,000+ price subscriptions)
- Stale data problem (when to refresh entire dataset?)

**Why Rejected:** Initial payload too large for mobile. 50MB download on 3G connection unacceptable. Low-end devices cannot handle 10,000 tokens in memory. Team prioritized fast initial load over pure offline capability.

### Option 3: Pagination-Only (No Filtering)
**Description:** Simple pagination, no advanced filtering, search only

**Pros:**
- Simplest to implement
- Predictable performance (fixed page size)
- Low bandwidth (only 20 tokens per page)
- Standard mobile pattern

**Cons:**
- Poor discovery experience (can't filter by volume, price change, etc.)
- Users must scroll through pages to find tokens
- Competitive disadvantage (other platforms have filtering)
- Doesn't meet product requirements

**Why Rejected:** Product requirement to have advanced filtering. Users need to discover tokens by multiple dimensions (volume, price change, liquidity). Pagination alone insufficient for trading platform.

### Option 4: Progressive Web App with Service Worker
**Description:** Use service worker for background caching and filtering

**Pros:**
- Advanced offline capabilities
- Background sync possible
- Can cache intelligently
- Progressive enhancement

**Cons:**
- Complex service worker logic
- Limited browser support on iOS (at time)
- Debugging difficulty
- Team unfamiliar with service worker patterns
- Overkill for this use case

**Why Rejected:** Unnecessary complexity for problem at hand. Hybrid client/server filtering achieves offline goals without service worker complexity. Team prefers simpler solutions.

### Option 5: GraphQL with Client-Side Caching (Apollo, Relay)
**Description:** Use GraphQL subscriptions and client-side cache management

**Pros:**
- Sophisticated caching built-in (Apollo Cache)
- Subscriptions for real-time updates
- Type-safe queries
- Developer-friendly

**Cons:**
- Team using REST APIs (GraphQL migration significant)
- Apollo Client adds bundle size (~50KB)
- Learning curve for team
- Overkill for filtering use case
- Still doesn't solve server vs. client filtering decision

**Why Rejected:** Team standardized on REST APIs. GraphQL migration too large for this feature. Hybrid REST approach achieves same goals with existing stack.

## Implementation Notes

### API Endpoint Design

**Filter Endpoint:**
```
POST /api/tokens/filter
Content-Type: application/json

Request Body:
{
  "filters": {
    "marketStage": ["kitchen", "graduated"],
    "volumeRange": {"min": 1000, "max": null},
    "priceChange24h": {"min": 5},
    "liquidityMin": 5000,
    "verified": true
  },
  "sort": {
    "field": "volume24h",
    "direction": "desc"
  },
  "limit": 100
}

Response:
{
  "tokens": [...],  // Array of token objects
  "total": 1547,    // Total matching tokens
  "cached": true,   // Server cache hit
  "timestamp": 1234567890
}
```

**Search Endpoint:**
```
GET /api/tokens/search?q=pepe&limit=20

Response:
{
  "results": [...],  // Elasticsearch weighted results
  "suggestions": ["pepe", "pepecoin", "pepe2.0"],
  "timestamp": 1234567890
}
```

### Client-Side Filter Implementation

**Filter Application Pattern:**
```javascript
// Instant client-side filtering
const applyFilters = (tokens, filters) => {
  return tokens.filter(token => {
    // Market stage filter
    if (filters.marketStage && !filters.marketStage.includes(token.stage)) {
      return false;
    }

    // Volume range filter
    if (filters.volumeRange) {
      if (filters.volumeRange.min && token.volume24h < filters.volumeRange.min) {
        return false;
      }
      if (filters.volumeRange.max && token.volume24h > filters.volumeRange.max) {
        return false;
      }
    }

    // Price change filter
    if (filters.priceChange24h && token.priceChange24h < filters.priceChange24h.min) {
      return false;
    }

    return true;
  });
};

// Debounced search
const debouncedSearch = debounce(async (query) => {
  const results = await fetch(`/api/tokens/search?q=${query}`);
  updateUI(results);
}, 300);
```

### Virtualized List Implementation

**React Window Example:**
```javascript
import { FixedSizeList } from 'react-window';

const TokenList = ({ tokens }) => (
  <FixedSizeList
    height={600}
    itemCount={tokens.length}
    itemSize={80}  // Token card height
    width="100%"
  >
    {({ index, style }) => (
      <TokenCard token={tokens[index]} style={style} />
    )}
  </FixedSizeList>
);
```

### Caching Strategy

**Multi-Tier Caching:**
```javascript
// 1. Check memory cache
let tokens = memoryCache.get('filtered_tokens');

if (!tokens) {
  // 2. Check local storage cache
  tokens = JSON.parse(localStorage.getItem('filtered_tokens'));

  if (!tokens || isCacheStale(tokens.timestamp)) {
    // 3. Fetch from API
    tokens = await fetchFilteredTokens(filters);

    // Update caches
    memoryCache.set('filtered_tokens', tokens);
    localStorage.setItem('filtered_tokens', JSON.stringify(tokens));
  } else {
    // Cache hit from local storage
    memoryCache.set('filtered_tokens', tokens);
  }
}

return tokens;
```

### Filter Preset System

**Saved Presets:**
```javascript
const PRESET_FILTERS = {
  "new_launches": {
    name: "New Launches",
    filters: {
      age: { max: 24 },  // Last 24 hours
      marketStage: ["kitchen"],
      sort: { field: "age", direction: "desc" }
    }
  },
  "high_volume": {
    name: "High Volume",
    filters: {
      volumeRange: { min: 100000 },
      sort: { field: "volume24h", direction: "desc" }
    }
  },
  "low_risk": {
    name: "Low Risk",
    filters: {
      verified: true,
      liquidityMin: 50000,
      holderCount: { min: 100 }
    }
  }
};
```

### Elasticsearch Index Configuration

**Token Search Index:**
```json
{
  "mappings": {
    "properties": {
      "name": {
        "type": "text",
        "analyzer": "standard",
        "fields": {
          "keyword": { "type": "keyword" }
        }
      },
      "symbol": {
        "type": "text",
        "analyzer": "standard",
        "fields": {
          "keyword": { "type": "keyword" }
        }
      },
      "description": { "type": "text" },
      "volume24h": { "type": "long" },
      "liquidity": { "type": "long" },
      "socialScore": { "type": "integer" }
    }
  }
}
```

**Weighted Search Query:**
```javascript
{
  "query": {
    "multi_match": {
      "query": "pepe",
      "fields": ["name^3", "symbol^2", "description"],
      "fuzziness": "AUTO"
    }
  },
  "sort": [
    { "_score": "desc" },
    { "volume24h": "desc" }
  ]
}
```

### Performance Monitoring

**Key Metrics to Track:**
- Filter application time (client-side)
- API response time for filter endpoint
- Cache hit rate (memory, local storage, server)
- Search response time
- WebSocket subscription count
- Memory usage (token cache size)
- Re-render frequency

**Performance Budget:**
```javascript
const PERFORMANCE_TARGETS = {
  filterApplicationTime: 100,     // ms
  apiResponseTime: 500,            // ms
  searchResponseTime: 500,         // ms
  initialLoadTime: 3000,           // ms (3G)
  virtualizedListFPS: 60,          // frames per second
  maxMemoryCacheSize: 1000,        // tokens
  bundleSizeIncrease: 50000        // bytes (50KB)
};
```

### Testing Strategy

**Unit Tests:**
- Filter logic (client-side filtering functions)
- Cache management (invalidation, TTL)
- Virtualized list rendering
- State management (Redux actions/reducers)

**Integration Tests:**
- Server + client filtering consistency
- Cache synchronization
- Offline behavior
- Real-time WebSocket updates

**Performance Tests:**
- Render 10,000 tokens without lag
- Filter application under 100ms
- Memory usage within limits
- Network throttling (3G simulation)

**User Acceptance Tests:**
- Bottom sheet filter UI usability
- Saved preset workflow
- Offline mode graceful degradation
- Cross-device compatibility

## References

### Meeting Notes
- [Mobile Filters Technical Deep Dive 2025-07-24](../06-meetings/2025-07/2025-07-24-mobile-filters.md) - Comprehensive filtering architecture discussion

### Related Decisions
- ADR-003: WebSocket to SSE Migration (real-time price updates)
- ADR-002: Microservices Architecture (backend filter endpoint design)
- Mobile App PRD (product requirements for token discovery)

### Technical Documentation
- React Window: https://github.com/bvaughn/react-window
- Elasticsearch Mobile Best Practices
- Mobile Filter UI Patterns (Nielsen Norman Group)
- Redux Toolkit Usage Guide

### External References
- Mobile filtering patterns and best practices
- Touch interaction design principles
- Progressive enhancement strategies
- Service worker alternatives

## Revision History
- 2025-07-24: Hybrid filtering architecture decision made
- 2025-07-24: Elasticsearch chosen for search indexing
- 2025-07-24: Bottom sheet UI pattern selected
- 2025-10-21: Formal ADR documented from meeting notes
