---
title: TradingView Charting Library Integration
type: decision-record
decision-id: ADR-101
date: 2025-09-02
status: accepted
owner: Lucas Cufre, Martin Aranda
stakeholders: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk]
tags: [technical, charting, tradingview, ui, frontend, data-feed]
summary: |
  Decision to integrate TradingView's commercial Charting Library rather than lightweight alternatives to provide professional-grade technical analysis tools for traders. Implementation includes custom UDF (Universal Data Feed) adapter, pre-computed OHLCV materialized views in ClickHouse, real-time WebSocket candle updates, and chart-based trading interactions. The solution supports timeframes from 1-minute to 1-week with full technical indicator library access.
related-docs:
  - ../06-meetings/2025-09/2025-09-02-tradingview-integration.md
  - ADR-001: ClickHouse Migration for Time-Series Data
  - ADR-003: WebSocket to SSE Migration
  - ADR-005: Indexer Microservices by Protocol
---

# TradingView Charting Library Integration

## Context and Problem Statement

Cooking.gg users require professional-grade charting and technical analysis tools to make informed trading decisions on Solana DEX tokens. Basic price charts are insufficient for serious traders who rely on technical indicators, drawing tools, and customizable chart layouts to analyze market trends and execute strategies.

**User Requirements:**

1. **Technical Analysis Tools:**
   - Moving averages (SMA, EMA, WMA)
   - Momentum indicators (RSI, MACD, Stochastic)
   - Volume analysis and overlays
   - Bollinger Bands, Fibonacci retracements
   - 100+ industry-standard indicators

2. **Chart Interaction:**
   - Multiple timeframes (1-minute to 1-week)
   - Drawing tools (trendlines, support/resistance levels)
   - Pattern recognition capabilities
   - Zoom, pan, and crosshair navigation
   - Save chart layouts and preferences

3. **Trading Integration:**
   - Place orders directly from chart interface
   - Visualize active orders as horizontal lines
   - Display TP/SL levels on chart
   - Mark execution prices visually

4. **Performance Requirements:**
   - Chart load time < 2 seconds
   - Real-time updates latency < 500ms
   - Support 1000+ concurrent chart viewers
   - Smooth interaction on mobile devices

**Key Challenges:**

1. **Data Volume:** OHLCV (Open/High/Low/Close/Volume) aggregation from raw trades requires significant processing
2. **Real-Time Updates:** Live candles must update smoothly without flickering or lag
3. **Mobile Performance:** Full charting library can be heavy for mobile devices
4. **Data Feed Protocol:** Must implement TradingView's UDF (Universal Data Feed) specification
5. **Licensing Costs:** Commercial charting libraries require paid licenses

**Industry Standard:** TradingView is the de-facto standard for trading charts, used by Binance, Coinbase, Kraken, and virtually all major exchanges. Users expect TradingView-level functionality.

## Decision

**Integrate TradingView's commercial Charting Library with custom UDF adapter, pre-computed ClickHouse OHLCV materialized views, WebSocket real-time candle updates, and chart-based trading interface.**

### Implementation Architecture

**Charting Library Choice:**

Selected **TradingView Charting Library** (commercial license) over alternatives:
- **Lightweight Charts** (free, limited features)
- **Advanced Charts** (premium tier with social features)

Justification: Professional features (100+ indicators, drawing tools, customization) justify license cost. User expectations set by industry leaders require full-featured solution.

**Component Architecture:**

```
┌─────────────────────────────────────────────────────────────┐
│                    TradingView Chart Widget                 │
│  (Embedded via JavaScript integration, custom theme)        │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│               Custom UDF Datafeed Adapter                   │
│  - onReady: chart configuration                             │
│  - resolveSymbol: token metadata                            │
│  - getBars: historical OHLCV data                           │
│  - subscribeBars: real-time candle updates                  │
└──────────┬──────────────────────────────────┬───────────────┘
           │                                  │
           ▼                                  ▼
┌──────────────────────────┐    ┌───────────────────────────┐
│  ClickHouse OHLCV Views  │    │   WebSocket Candle Stream │
│  - Materialized views    │    │   - Real-time tick updates│
│  - Pre-aggregated candles│    │   - Current candle updates│
│  - Multiple timeframes   │    │   - Low latency streaming │
└──────────────────────────┘    └───────────────────────────┘
```

### UDF (Universal Data Feed) Implementation

**Required API Endpoints:**

TradingView's UDF protocol expects the following endpoints:

**1. /config - Chart Configuration**
```json
{
  "supported_resolutions": ["1", "5", "15", "60", "240", "D", "W"],
  "supports_marks": true,
  "supports_timescale_marks": true,
  "supports_time": true
}
```

**2. /symbols?query=... - Symbol Search**
Returns matching tokens based on search query

**3. /symbol_info?symbol=... - Token Metadata**
```json
{
  "name": "BONK/SOL",
  "ticker": "BONK",
  "description": "Bonk Token",
  "type": "crypto",
  "session": "24x7",
  "exchange": "Solana",
  "listed_exchange": "Raydium",
  "timezone": "Etc/UTC",
  "minmov": 1,
  "pricescale": 100000000,
  "has_intraday": true,
  "supported_resolutions": ["1", "5", "15", "60", "240", "D", "W"],
  "volume_precision": 2,
  "data_status": "streaming"
}
```

**4. /history - Historical OHLCV Bars**
Query parameters: symbol, resolution, from (timestamp), to (timestamp)

Returns array of bars:
```json
{
  "s": "ok",
  "t": [1695123460, 1695123520, ...],  // timestamps
  "o": [0.0000005, 0.0000006, ...],    // open
  "h": [0.0000007, 0.0000008, ...],    // high
  "l": [0.0000004, 0.0000005, ...],    // low
  "c": [0.0000006, 0.0000007, ...],    // close
  "v": [1000000, 1500000, ...]         // volume
}
```

**5. /marks (Optional) - Custom Chart Markers**
Display significant events (token launch, major trades, etc.)

### ClickHouse OHLCV Materialized Views

**Challenge:** Aggregating raw trade data into OHLCV candles on-demand is too slow for real-time charting.

**Solution:** Pre-compute OHLCV data using ClickHouse materialized views for each timeframe:

```sql
-- 1-minute OHLCV view
CREATE MATERIALIZED VIEW ohlcv_1m
ENGINE = AggregatingMergeTree()
PARTITION BY (token_address, toYYYYMMDD(time))
ORDER BY (token_address, time)
AS SELECT
  token_address,
  toStartOfMinute(timestamp) AS time,
  argMin(price, timestamp) AS open,      -- First price in minute
  max(price) AS high,                    -- Highest price in minute
  min(price) AS low,                     -- Lowest price in minute
  argMax(price, timestamp) AS close,     -- Last price in minute
  sum(volume_usd) AS volume              -- Total volume in minute
FROM trades
GROUP BY token_address, time
ORDER BY token_address, time;

-- Similar views for 5m, 15m, 1h, 4h, 1d, 1w
CREATE MATERIALIZED VIEW ohlcv_5m AS ...
CREATE MATERIALIZED VIEW ohlcv_15m AS ...
CREATE MATERIALIZED VIEW ohlcv_1h AS ...
CREATE MATERIALIZED VIEW ohlcv_4h AS ...
CREATE MATERIALIZED VIEW ohlcv_1d AS ...
CREATE MATERIALIZED VIEW ohlcv_1w AS ...
```

**Query Performance:**
- Raw trade aggregation: 2-3 seconds (unacceptable for charts)
- Materialized view query: < 200ms (acceptable)
- Improvement: 10x-15x faster

**Storage Overhead:**
- Materialized views require additional storage (~10-15% of raw trade data)
- Justified by dramatic performance improvement
- Aligns with ClickHouse strengths (pre-aggregation)

### Real-Time Candle Updates

**WebSocket Subscription Pattern:**

```javascript
// Datafeed adapter subscribeBars implementation
subscribeBars: (symbolInfo, resolution, onTick, listenerGuid) => {
  const tokenAddress = symbolInfo.name;

  // Subscribe to real-time price updates via WebSocket
  const subscription = websocket.subscribe(`candles:${tokenAddress}:${resolution}`, (candle) => {
    onTick({
      time: candle.timestamp * 1000,  // TradingView expects milliseconds
      open: candle.open,
      high: candle.high,
      low: candle.low,
      close: candle.close,
      volume: candle.volume
    });
  });

  // Store subscription for cleanup
  activeSubscriptions.set(listenerGuid, subscription);
}

unsubscribeBars: (listenerGuid) => {
  const subscription = activeSubscriptions.get(listenerGuid);
  if (subscription) {
    subscription.unsubscribe();
    activeSubscriptions.delete(listenerGuid);
  }
}
```

**Backend Candle Management:**

1. **Current Candle State (In-Memory):**
   - Maintain current candle in Redis for each (token, timeframe) pair
   - Update on every trade: recalculate open/high/low/close/volume
   - Emit WebSocket update to all subscribed clients

2. **Candle Finalization:**
   - When candle period closes (e.g., minute ends), persist to ClickHouse
   - Create new empty candle for next period
   - Continue updating in-memory

3. **Trade Processing Flow:**
```javascript
async function processTrade(trade) {
  // Update current candle for all timeframes
  for (const resolution of ['1m', '5m', '15m', '1h', '4h', '1d', '1w']) {
    const candle = await getCurrentCandle(trade.token_address, resolution);

    // Update candle with trade data
    candle.high = Math.max(candle.high, trade.price);
    candle.low = Math.min(candle.low, trade.price);
    candle.close = trade.price;
    candle.volume += trade.volume_usd;

    // Save updated candle to Redis
    await saveCurrentCandle(candle);

    // Emit WebSocket update
    websocket.publish(`candles:${trade.token_address}:${resolution}`, candle);

    // If candle period ended, finalize
    if (shouldFinalizeCandle(candle, resolution)) {
      await finalizeCandle(candle);
    }
  }
}
```

### Supported Timeframes

**Initial Support:**
- **1m** - 1-minute candles (intraday scalping)
- **5m** - 5-minute candles (short-term trading)
- **15m** - 15-minute candles (swing trading)
- **1h (60)** - 1-hour candles (medium-term analysis)
- **4h (240)** - 4-hour candles (daily trend analysis)
- **1d (D)** - Daily candles (long-term trends)
- **1w (W)** - Weekly candles (macro analysis)

**Coverage:** These 7 timeframes cover 95% of trader use cases.

**Data Retention Strategy:**
- **1m data:** 30 days (high frequency, limited retention)
- **5m/15m data:** 90 days
- **1h data:** 1 year
- **4h/1d/1w data:** Indefinite (permanent historical record)

### Chart Customization & Theming

**Dark Theme Integration:**
```javascript
const chartOptions = {
  theme: 'dark',
  custom_css_url: '/tradingview-custom-theme.css',
  overrides: {
    // Candles
    'mainSeriesProperties.candleStyle.upColor': '#26a69a',
    'mainSeriesProperties.candleStyle.downColor': '#ef5350',
    'mainSeriesProperties.candleStyle.borderUpColor': '#26a69a',
    'mainSeriesProperties.candleStyle.borderDownColor': '#ef5350',

    // Background and grid
    'paneProperties.background': '#131722',
    'paneProperties.gridColor': '#1e222d',

    // Volume
    'volumePaneSize': 'medium',
    'mainSeriesProperties.showCountdown': false
  },
  disabled_features: [
    'header_symbol_search',  // Use our custom token search
    'symbol_info'            // Use our custom token info panel
  ],
  enabled_features: [
    'study_templates',       // Save indicator layouts
    'use_localstorage_for_settings'  // Persist user preferences
  ]
};
```

**Branding:**
- Match Cooking.gg color scheme
- Hide TradingView logo (requires appropriate license tier)
- Custom toolbar colors
- Branded watermark (optional)

### Mobile Optimization Strategy

**Performance Challenges:**
- Full TradingView library ~500KB+ JavaScript
- 100+ indicators require significant processing
- Mobile devices have limited CPU/memory

**Solution: Conditional Library Loading**

```javascript
// Desktop: Full Charting Library
if (isDesktop) {
  import('tradingview-charting-library').then(TradingView => {
    initializeFullChart(TradingView);
  });
}

// Mobile: Lightweight Charts
if (isMobile) {
  import('lightweight-charts').then(LightweightCharts => {
    initializeLightweightChart(LightweightCharts);
  });
}
```

**Mobile Optimizations:**
- Limit visible candles to 500 (reduce rendering load)
- Disable complex indicators by default
- Lazy load drawing tools library
- Simplified touch interactions
- Use Lightweight Charts (free, smaller bundle ~50KB)

**Mobile Touch Interactions:**
- Pinch to zoom timeframe
- Swipe to pan historical data
- Long-press for crosshair and price tooltip
- Double-tap to reset zoom

### Trading from Chart Interface

**Order Placement Workflow:**

1. **Click Chart to Set Price:**
   - User clicks on chart at desired price level
   - Horizontal line appears at clicked price
   - Order entry modal pre-filled with chart price

2. **Visual Order Representation:**
   - **Active Buy Orders:** Green horizontal lines
   - **Active Sell Orders:** Red horizontal lines
   - **Take Profit Levels:** Green dashed lines
   - **Stop Loss Levels:** Red dashed lines

3. **Order Modification:**
   - Drag order line to modify price
   - Right-click order line for quick cancel
   - Hover shows order details (size, type, status)

4. **Execution Markers:**
   - Mark fill price on chart when order executes
   - Draw vertical line at execution time
   - Show profit/loss from entry to exit

**Implementation Example:**
```javascript
// Add order line to chart
function addOrderLine(order) {
  const line = chart.createPriceLine({
    price: order.price,
    color: order.side === 'buy' ? '#26a69a' : '#ef5350',
    lineWidth: 2,
    lineStyle: 0,  // Solid line
    axisLabelVisible: true,
    title: `${order.side.toUpperCase()} ${order.size} @ ${order.price}`
  });

  // Make line draggable for price modification
  line.applyOptions({
    draggable: true,
    onMove: (newPrice) => updateOrderPrice(order.id, newPrice)
  });

  orderLines.set(order.id, line);
}
```

### Caching Strategy

**Redis Cache for Popular Tokens:**

```javascript
// Cache OHLCV data for frequently accessed tokens/timeframes
async function getCachedOHLCV(tokenAddress, resolution, from, to) {
  const cacheKey = `ohlcv:${tokenAddress}:${resolution}:${from}:${to}`;

  // Try cache first
  const cached = await redis.get(cacheKey);
  if (cached) return JSON.parse(cached);

  // Fetch from ClickHouse
  const data = await clickhouse.query(`
    SELECT time, open, high, low, close, volume
    FROM ohlcv_${resolution}
    WHERE token_address = '${tokenAddress}'
      AND time >= ${from}
      AND time <= ${to}
    ORDER BY time ASC
  `);

  // Cache for 5 minutes (candles don't change after finalization)
  await redis.setex(cacheKey, 300, JSON.stringify(data));

  return data;
}
```

**Cache Benefits:**
- Reduce ClickHouse load for popular tokens
- Faster response for repeated queries
- Invalidation: 5-minute TTL (candles immutable after finalization)

**Cache Invalidation:**
- Current (unfinalized) candle: No cache (always fresh from Redis)
- Historical (finalized) candles: Cache safely (never change)

## Rationale

### TradingView Over Lightweight Charts

**User Expectations:**
- Industry standard: Binance, Coinbase, Kraken all use TradingView
- Traders familiar with TradingView interface and indicators
- Competitive pressure: alternatives lacking TradingView appear inferior

**Feature Gap:**
- **Lightweight Charts:** Limited to basic indicators, no drawing tools, simple customization
- **Charting Library:** 100+ indicators, full drawing tools, Pine Script support, study templates
- **Value Proposition:** Professional traders won't use platform without professional tools

**License Cost Justification:**
- TradingView commercial license: ~$3,000-$5,000/year
- User acquisition: Professional charts differentiate platform
- Retention: Advanced traders need advanced tools
- ROI: Even 5-10 retained traders justify cost

### Pre-Computed OHLCV Materialized Views

**Performance Necessity:**

Without materialized views:
```sql
-- On-demand aggregation (2-3 seconds, unacceptable)
SELECT
  toStartOfHour(timestamp) AS time,
  argMin(price, timestamp) AS open,
  max(price) AS high,
  min(price) AS low,
  argMax(price, timestamp) AS close,
  sum(volume_usd) AS volume
FROM trades
WHERE token_address = 'EPjF...'
  AND timestamp >= now() - INTERVAL 1 DAY
GROUP BY time
ORDER BY time;
-- Scans millions of trades, slow aggregation
```

With materialized views:
```sql
-- Pre-aggregated query (< 200ms, acceptable)
SELECT time, open, high, low, close, volume
FROM ohlcv_1h
WHERE token_address = 'EPjF...'
  AND time >= now() - INTERVAL 1 DAY
ORDER BY time;
-- Scans 24 pre-computed rows, instant
```

**Storage Trade-off:**
- Additional storage: ~10-15% of raw trade data
- Performance gain: 10x-15x faster queries
- User experience: Charts load instantly vs 2-3 second delays
- Aligns with ClickHouse strengths (materialized views primary feature)

**Aligns with ADR-001:** ClickHouse migration specifically chosen for materialized view capabilities.

### WebSocket for Real-Time Updates

**Why WebSocket Over Polling:**

Polling approach:
- Frontend polls /history endpoint every 3-5 seconds
- High server load (1000 users × 0.2 requests/sec = 200 req/sec)
- Latency: 3-5 seconds between updates (poor UX)
- Inefficient: most polls return no new data

WebSocket approach:
- Single persistent connection per user
- Server pushes updates only when candle changes
- Latency: < 500ms from trade to chart update
- Efficient: no unnecessary requests

**Scalability:**
- WebSocket connections: 1000 concurrent users = 1000 connections (manageable)
- Redis pub/sub: Distribute WebSocket messages across multiple servers
- Horizontal scaling: Add more WebSocket servers behind load balancer

**Aligns with ADR-003:** Platform already migrated to SSE for real-time updates. WebSocket follows similar pattern for candle subscriptions.

### Mobile: Lightweight Charts Trade-off

**Problem:**
- Full TradingView library: ~500KB JavaScript bundle
- Mobile data costs and slow networks
- Limited CPU for complex indicator calculations
- Smaller screens don't benefit from full feature set

**Solution:**
- Desktop: Full Charting Library (professional traders, full features)
- Mobile: Lightweight Charts (casual users, basic functionality)

**User Impact:**
- 95% of mobile users: casual browsing, don't use advanced indicators
- 5% of mobile users (serious traders): prefer desktop for trading anyway
- Acceptable compromise: mobile gets fast, responsive charts; desktop gets full power

**Bundle Size Comparison:**
- Charting Library: ~500KB gzipped
- Lightweight Charts: ~50KB gzipped
- Mobile savings: 90% reduction, faster load times

### Chart-Based Trading Integration

**User Workflow Optimization:**

Traditional workflow:
1. Analyze chart
2. Switch to order entry form
3. Manually enter price from chart
4. Submit order
5. Switch back to chart
6. Total: 5 steps, context switching, potential errors

Chart-based workflow:
1. Click chart at desired price
2. Confirm order in pre-filled modal
3. Total: 2 steps, no context switching, accurate pricing

**Industry Standard:**
- TradingView, Binance, Coinbase, Kraken all support chart-based trading
- User expectation for modern trading platforms
- Competitive necessity

## Consequences

### Positive

**User Experience:**
- Professional-grade charting matches industry standards
- Familiar interface for experienced traders (TradingView ubiquity)
- 100+ technical indicators enable sophisticated analysis
- Drawing tools support pattern recognition strategies
- Chart-based trading streamlines order placement workflow
- Real-time updates (< 500ms latency) provide smooth experience
- Save chart layouts and preferences for personalization

**Performance:**
- Materialized views deliver sub-200ms query times
- Pre-computation eliminates 2-3 second wait times
- Redis caching further accelerates popular tokens
- WebSocket updates minimize server load vs polling
- Support 1000+ concurrent chart viewers

**Competitive Advantage:**
- Professional charts differentiate from competitors
- Attract serious traders who require advanced tools
- Retention: traders won't leave platform lacking essential features
- Premium positioning: TradingView signals quality platform

**Development Efficiency:**
- TradingView handles complex chart rendering (don't build from scratch)
- Mature library reduces bugs and edge cases
- Extensive documentation and community support
- UDF protocol is well-established standard

**Platform Alignment:**
- Leverages ClickHouse materialized view capabilities (ADR-001)
- Uses WebSocket real-time infrastructure (ADR-003)
- Integrates with indexer OHLCV data (ADR-005)

### Negative

**License Cost:**
- TradingView commercial license: $3,000-$5,000/year recurring cost
- Potential usage-based fees if exceed limits
- Vendor dependency: price increases risk

**Implementation Complexity:**
- UDF protocol implementation requires careful adherence to specification
- Multiple API endpoints to build and maintain
- WebSocket candle management adds stateful complexity
- Materialized views for 7 timeframes increase database objects
- Real-time candle updates require precise timing logic

**Storage Overhead:**
- OHLCV materialized views consume 10-15% additional storage
- 7 timeframes × all tokens = significant data duplication
- Growing cost as token count and history expand

**Mobile Compromise:**
- Lightweight Charts on mobile lacks full feature set
- Desktop/mobile feature disparity may confuse users
- Maintaining two chart implementations (dual codebase)

**Vendor Lock-In:**
- Switching from TradingView costly (UI redesign, user retraining)
- Dependent on TradingView's roadmap and decisions
- License terms may change unfavorably

**Maintenance Burden:**
- Keep datafeed adapter compatible with TradingView updates
- Monitor and tune materialized view performance
- Manage WebSocket connection scaling
- Cache invalidation edge cases

**Data Retention Costs:**
- 1-minute data for 30 days across all tokens
- Storage costs grow linearly with token count
- Need retention policy enforcement

### Neutral

**Technical Debt:**
- Dual chart implementation (desktop/mobile) to maintain
- Future: potentially migrate mobile to Progressive Web App with full library

**Scalability:**
- Materialized views scale well with ClickHouse
- WebSocket connections require horizontal scaling
- Redis pub/sub distributes candle updates

## Alternatives Considered

### Option 1: Build Custom Chart from Scratch

**Description:** Implement custom charting solution using D3.js or Canvas API

**Pros:**
- No license fees
- Complete control over features and UI
- No vendor dependency
- Potentially lighter weight

**Cons:**
- Development time: 6-12 months for basic feature parity
- Indicator library: months to implement 100+ indicators
- Bug-prone: charting is complex domain, many edge cases
- User unfamiliarity: learning curve vs TradingView standard
- Ongoing maintenance burden

**Why Rejected:** Development cost far exceeds license cost. Users expect TradingView-level functionality, which takes years to build. Not core competency for Cooking.gg.

### Option 2: Lightweight Charts Only (All Devices)

**Description:** Use TradingView's free Lightweight Charts library for both desktop and mobile

**Pros:**
- Free, open-source
- Smaller bundle size (~50KB)
- Simpler implementation
- No license fees

**Cons:**
- Limited indicators (no RSI, MACD, Bollinger Bands, etc.)
- No drawing tools (no trendlines, Fibonacci, patterns)
- Basic customization compared to Charting Library
- Competitive disadvantage: serious traders won't use platform
- Missing features traders expect as standard

**Why Rejected:** Feature gap unacceptable for target audience (serious traders). Lightweight Charts suitable for casual users but insufficient for platform differentiation.

### Option 3: On-Demand OHLCV Aggregation (No Materialized Views)

**Description:** Calculate OHLCV candles on-demand from raw trade data when chart loads

**Pros:**
- No storage overhead for materialized views
- Simpler database schema
- No pre-computation pipeline to maintain

**Cons:**
- Unacceptable performance: 2-3 seconds per chart load
- High ClickHouse load: every chart request scans millions of trades
- Scalability issue: 1000 concurrent users = 1000 heavy queries
- Poor user experience: slow charts frustrate traders

**Why Rejected:** Performance unacceptable for real-time trading platform. Users expect instant chart loading. ClickHouse specifically chosen (ADR-001) for materialized view capabilities.

### Option 4: Third-Party Charting Service (e.g., Charting as a Service)

**Description:** Use external charting service that hosts TradingView and provides API

**Pros:**
- Outsource complexity to third party
- No direct TradingView license management
- Potentially faster implementation

**Cons:**
- Additional vendor dependency (double vendor lock-in)
- Data privacy concerns (trading data through third party)
- Limited customization compared to direct integration
- Potential latency: extra network hop for data
- Cost: service fees may exceed direct license cost

**Why Rejected:** Direct TradingView integration provides more control, better performance, and likely lower cost. Data privacy critical for trading platform.

### Option 5: Polling Instead of WebSocket for Real-Time Updates

**Description:** Frontend polls /history endpoint every 3-5 seconds for candle updates

**Pros:**
- Simpler implementation (no WebSocket infrastructure)
- Stateless (no connection management)
- HTTP caching possible

**Cons:**
- High server load: 1000 users × 0.2 req/sec = 200 req/sec
- Latency: 3-5 seconds between updates (poor UX)
- Inefficient: most polls return no new data (wasted requests)
- Scalability concern: load grows linearly with users

**Why Rejected:** WebSocket infrastructure already exists (ADR-003). Polling wastes resources and provides inferior user experience. Real-time trading requires low latency.

## Implementation Notes

### UDF Datafeed Adapter Implementation

**Full Datafeed Adapter Code:**

```javascript
import { getTokenMetadata, fetchOHLCV, subscribeToCandles } from './api';

const datafeed = {
  // Step 1: Provide chart configuration
  onReady: (callback) => {
    console.log('[Datafeed] onReady called');
    setTimeout(() => {
      callback({
        supported_resolutions: ['1', '5', '15', '60', '240', 'D', 'W'],
        supports_marks: true,
        supports_timescale_marks: true,
        supports_time: true,
        exchanges: [
          { value: 'Raydium', name: 'Raydium', desc: 'Raydium DEX' },
          { value: 'Orca', name: 'Orca', desc: 'Orca DEX' },
          { value: 'Jupiter', name: 'Jupiter', desc: 'Jupiter Aggregator' }
        ]
      });
    }, 0);
  },

  // Step 2: Search symbols by query
  searchSymbols: async (userInput, exchange, symbolType, onResult) => {
    console.log('[Datafeed] searchSymbols:', userInput);
    const results = await searchTokens(userInput, exchange);
    onResult(results.map(token => ({
      symbol: token.symbol,
      full_name: `${token.symbol}/SOL`,
      description: token.name,
      exchange: token.dex,
      type: 'crypto'
    })));
  },

  // Step 3: Resolve symbol metadata
  resolveSymbol: async (symbolName, onResolve, onError) => {
    console.log('[Datafeed] resolveSymbol:', symbolName);

    try {
      const tokenInfo = await getTokenMetadata(symbolName);

      const symbolInfo = {
        name: tokenInfo.symbol,
        ticker: tokenInfo.symbol,
        description: tokenInfo.name,
        type: 'crypto',
        session: '24x7',
        exchange: 'Solana',
        listed_exchange: tokenInfo.dex,
        timezone: 'Etc/UTC',
        minmov: 1,
        pricescale: 100000000,  // 8 decimal places
        has_intraday: true,
        has_weekly_and_monthly: true,
        has_daily: true,
        supported_resolutions: ['1', '5', '15', '60', '240', 'D', 'W'],
        volume_precision: 2,
        data_status: 'streaming',
        format: 'price'
      };

      setTimeout(() => onResolve(symbolInfo), 0);
    } catch (error) {
      console.error('[Datafeed] resolveSymbol error:', error);
      onError('Symbol not found');
    }
  },

  // Step 4: Fetch historical OHLCV bars
  getBars: async (symbolInfo, resolution, periodParams, onResult, onError) => {
    const { from, to, firstDataRequest } = periodParams;
    console.log('[Datafeed] getBars:', symbolInfo.name, resolution, from, to);

    try {
      const bars = await fetchOHLCV(symbolInfo.name, resolution, from, to);

      if (bars.length === 0) {
        onResult([], { noData: true });
      } else {
        onResult(bars, { noData: false });
      }
    } catch (error) {
      console.error('[Datafeed] getBars error:', error);
      onError(error.message);
    }
  },

  // Step 5: Subscribe to real-time candle updates
  subscribeBars: (symbolInfo, resolution, onTick, listenerGuid, onResetCacheNeededCallback) => {
    console.log('[Datafeed] subscribeBars:', symbolInfo.name, resolution, listenerGuid);

    const subscription = subscribeToCandles(
      symbolInfo.name,
      resolution,
      (candle) => {
        onTick({
          time: candle.timestamp * 1000,  // TradingView expects milliseconds
          open: candle.open,
          high: candle.high,
          low: candle.low,
          close: candle.close,
          volume: candle.volume
        });
      }
    );

    // Store subscription for cleanup
    subscriptions.set(listenerGuid, subscription);
  },

  // Step 6: Unsubscribe from real-time updates
  unsubscribeBars: (listenerGuid) => {
    console.log('[Datafeed] unsubscribeBars:', listenerGuid);

    const subscription = subscriptions.get(listenerGuid);
    if (subscription) {
      subscription.unsubscribe();
      subscriptions.delete(listenerGuid);
    }
  }
};

export default datafeed;
```

### ClickHouse Index Optimization

**Indexes for OHLCV Queries:**

```sql
-- Primary index already optimal: (token_address, time)
-- Queries always filter by token_address and time range

-- Projection for reverse time queries (latest candles first)
ALTER TABLE ohlcv_1m ADD PROJECTION latest_candles (
  SELECT * ORDER BY token_address, time DESC
);
```

### Redis Candle Management

**Current Candle State:**

```javascript
// Store current candle state in Redis
async function updateCurrentCandle(tokenAddress, resolution, trade) {
  const key = `current_candle:${tokenAddress}:${resolution}`;

  // Get current candle or create new
  let candle = await redis.get(key);
  if (!candle) {
    candle = {
      token_address: tokenAddress,
      time: getCandleStartTime(trade.timestamp, resolution),
      open: trade.price,
      high: trade.price,
      low: trade.price,
      close: trade.price,
      volume: 0
    };
  } else {
    candle = JSON.parse(candle);
  }

  // Update candle with trade
  candle.high = Math.max(candle.high, trade.price);
  candle.low = Math.min(candle.low, trade.price);
  candle.close = trade.price;
  candle.volume += trade.volume_usd;

  // Save back to Redis
  await redis.setex(key, 3600, JSON.stringify(candle));  // 1 hour TTL

  return candle;
}

// Check if candle should be finalized
function shouldFinalizeCandle(candle, resolution) {
  const now = Date.now() / 1000;
  const candleDuration = getResolutionSeconds(resolution);
  return now >= candle.time + candleDuration;
}

// Finalize candle to ClickHouse
async function finalizeCandle(candle, resolution) {
  await clickhouse.insert(`ohlcv_${resolution}`, [candle]);

  // Clear from Redis (new candle will be created on next trade)
  const key = `current_candle:${candle.token_address}:${resolution}`;
  await redis.del(key);
}
```

### Performance Monitoring

**Key Metrics:**

```javascript
// Track chart load performance
metrics.histogram('chart.load_time', loadTimeMs, {
  token: tokenAddress,
  resolution: resolution
});
// Target: < 2000ms

// Track real-time update latency
metrics.histogram('chart.update_latency', latencyMs, {
  token: tokenAddress,
  resolution: resolution
});
// Target: < 500ms

// Track concurrent chart viewers
metrics.gauge('chart.active_viewers', activeViewerCount);
// Target: Support 1000+

// Track OHLCV query performance
metrics.histogram('ohlcv.query_time', queryTimeMs, {
  resolution: resolution,
  bars_returned: barCount
});
// Target: < 200ms
```

## References

### Meeting Notes
- [TradingView Integration Technical Discussion 2025-09-02](../06-meetings/2025-09/2025-09-02-tradingview-integration.md) - Comprehensive TradingView integration planning

### Related Decisions
- ADR-001: ClickHouse Migration for Time-Series Data (materialized views foundation)
- ADR-003: WebSocket to SSE Migration (real-time updates infrastructure)
- ADR-005: Indexer Microservices by Protocol (trade data source)

### Technical References
- TradingView Charting Library Documentation: https://www.tradingview.com/charting-library-docs/
- UDF Protocol Specification: https://www.tradingview.com/charting-library-docs/latest/connecting_data/UDF
- Lightweight Charts Documentation: https://tradingview.github.io/lightweight-charts/
- ClickHouse Materialized Views Guide: https://clickhouse.com/docs/en/guides/developer/cascading-materialized-views
- Pine Script Reference: https://www.tradingview.com/pine-script-reference/v5/

### License Information
- TradingView Commercial License Terms
- Lightweight Charts Apache 2.0 License

## Revision History
- 2025-09-02: TradingView Charting Library integration decision made
- 2025-09-02: UDF protocol implementation designed
- 2025-09-02: OHLCV materialized views strategy defined
- 2025-09-02: Mobile optimization approach decided (Lightweight Charts)
- 2025-10-21: Formal ADR documented from meeting notes
