---
title: Tradingview Integration - 2025-09-02
type: meeting
meeting_type: technical_deep_dive
topic: TradingView
date: 2025-09-02
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# TradingView Integration Technical Discussion - Cooking.gg
**Date:** September 2, 2025, 08:59 GMT-03:00
**Duration:** ~1 hour
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk

## Executive Summary
The team discussed integrating TradingView charts into Cooking.gg to provide professional-grade technical analysis tools. Key decisions included using TradingView's Charting Library, implementing custom data feeds, supporting technical indicators, and designing chart interaction patterns for both desktop and mobile.

## Meeting Context
Users requested advanced charting capabilities beyond basic price charts. TradingView is the industry standard for trading charts, offering hundreds of technical indicators, drawing tools, and customizable interfaces. Integration requires implementing TradingView's data feed protocol and embedding their Charting Library.

## Technical Discussion

### TradingView Charting Library Integration
**Library Options**:
1. **TradingView Charting Library**: Full-featured, requires commercial license
2. **Lightweight Charts**: Free, open-source, limited features
3. **Advanced Charts**: TradingView's premium tier with real-time data and social features

**Decision**: Start with Charting Library (commercial license required)

**Technical Implementation**:
- Embed TradingView widget via iframe or direct JavaScript integration
- Custom datafeed adapter to provide OHLCV data from Cooking's indexer
- Support multiple timeframes: 1m, 5m, 15m, 1h, 4h, 1d, 1w
- Enable indicator library and drawing tools
- Responsive layout for mobile and desktop

### Data Feed Protocol Implementation
**UDF (Universal Data Feed) Requirements**:
TradingView expects specific API endpoints:

1. **/config**: Chart configuration and supported features
2. **/symbols**: Search symbols by query
3. **/symbol_info**: Get symbol metadata
4. **/history**: Fetch historical OHLCV data
5. **/marks**: Custom markers on chart (optional)
6. **/timescale_marks**: Time-based markers (optional)

**Implementation Example**:
```javascript
// Datafeed adapter
const datafeed = {
  onReady: (callback) => {
    // Provide chart configuration
    callback({
      supported_resolutions: ['1', '5', '15', '60', '240', 'D', 'W'],
      supports_marks: true,
      supports_timescale_marks: true
    });
  },

  resolveSymbol: (symbolName, onResolve, onError) => {
    // Fetch symbol metadata from Cooking API
    getTokenInfo(symbolName).then(info => {
      onResolve({
        name: info.symbol,
        ticker: info.symbol,
        description: info.name,
        type: 'crypto',
        session: '24x7',
        exchange: 'Solana',
        listed_exchange: info.dex,
        timezone: 'Etc/UTC',
        minmov: 1,
        pricescale: 100000000,
        has_intraday: true,
        has_weekly_and_monthly: true,
        supported_resolutions: ['1', '5', '15', '60', '240', 'D', 'W'],
        volume_precision: 2,
        data_status: 'streaming'
      });
    });
  },

  getBars: (symbolInfo, resolution, periodParams, onResult, onError) => {
    // Fetch historical OHLCV data from ClickHouse
    fetchOHLCV(symbolInfo.name, resolution, periodParams.from, periodParams.to)
      .then(bars => onResult(bars, { noData: bars.length === 0 }))
      .catch(onError);
  },

  subscribeBars: (symbolInfo, resolution, onTick, listenerGuid) => {
    // Subscribe to real-time price updates via WebSocket
    subscribeToPrice(symbolInfo.name, (tick) => {
      onTick({
        time: tick.timestamp,
        open: tick.open,
        high: tick.high,
        low: tick.low,
        close: tick.close,
        volume: tick.volume
      });
    });
  },

  unsubscribeBars: (listenerGuid) => {
    // Unsubscribe from price updates
    unsubscribeFromPrice(listenerGuid);
  }
};
```

### OHLCV Data Generation
**Challenge**: Raw trade data needs aggregation into OHLCV candles

**Solution**: Pre-compute OHLCV data in ClickHouse
```sql
-- Materialize OHLCV views for each timeframe
CREATE MATERIALIZED VIEW ohlcv_1m AS
SELECT
  token_address,
  toStartOfMinute(timestamp) AS time,
  argMin(price, timestamp) AS open,
  max(price) AS high,
  min(price) AS low,
  argMax(price, timestamp) AS close,
  sum(volume) AS volume
FROM trades
GROUP BY token_address, time
ORDER BY token_address, time;

-- Similar views for 5m, 15m, 1h, 4h, 1d, 1w
```

**Real-Time Updates**:
- Maintain current candle in memory
- Update on each new trade
- Emit update to all subscribed chart clients via WebSocket
- Finalize candle and persist to database at candle close

### Technical Indicators Support
**TradingView Built-In Indicators**:
- Moving Averages (SMA, EMA, WMA)
- RSI, MACD, Bollinger Bands
- Volume indicators
- Fibonacci retracements
- 100+ indicators available

**Custom Indicators** (if needed):
- Can define custom Pine Script indicators
- Integrate Cooking-specific metrics (e.g., bonding curve progress)
- Require TradingView Advanced Charts license

### Chart Customization & Theming
**Theme Integration**:
- Match Cooking.gg's dark theme
- Custom color scheme for candles, background, grid
- Branded toolbar colors
- Hide TradingView branding (requires license tier support)

**Layout Configuration**:
- Default to candlestick chart type
- Volume overlay enabled by default
- Adjustable chart height for mobile/desktop
- Save user preferences (indicators, layouts) to database

### Mobile Chart Optimization
**Touch Interactions**:
- Pinch to zoom timeframe
- Swipe to pan historical data
- Long-press for crosshair and price info
- Double-tap to reset zoom

**Performance Considerations**:
- Limit visible candles to 500 for mobile
- Reduce indicator calculations on lower-end devices
- Lazy load drawing tools library
- Use Lightweight Charts library for mobile to reduce bundle size

### Trading from Chart
**Integration with Order Entry**:
- Click on chart to set limit order price
- Draw horizontal line to visualize order price
- Drag line to modify order price
- Right-click order line for quick cancel
- Visual representation of TP/SL levels

**Order Visualization**:
- Active orders displayed as horizontal lines
- Color-coded: green for buy, red for sell
- TP/SL shown with dashed lines
- Fill price marked on chart when order executes

## Key Technical Decisions
- **Decision 1:** TradingView Charting Library over Lightweight Charts - Professional features justify license cost
- **Decision 2:** Pre-compute OHLCV in ClickHouse - Much faster than on-demand aggregation
- **Decision 3:** WebSocket for real-time candle updates - Low latency, efficient for multiple subscribers
- **Decision 4:** Support 1m to 1w timeframes initially - Covers 95% of user needs
- **Decision 5:** Enable trading directly from chart - Significantly improves UX for technical traders

## Architecture & Design Considerations
- **Caching**: Cache OHLCV data in Redis for frequently accessed timeframes
- **Data Retention**: Store 1m data for 30 days, 1h data for 1 year, 1d data indefinitely
- **API Performance**: Optimize queries with proper indexes on (token_address, timestamp)
- **License Management**: Track API usage to stay within TradingView license limits

## Performance & Scalability Notes
- **Load Time**: Target < 2 seconds for chart initialization
- **Real-Time Latency**: < 500ms from trade to chart update
- **Concurrent Users**: Support 1000+ simultaneous chart viewers
- **Data Volume**: Expect ~10GB OHLCV data growth per month

## Action Items
- [ ] **Lucas**: Obtain TradingView Charting Library commercial license
- [ ] **Eduardo**: Implement OHLCV materialized views in ClickHouse
- [ ] **Martin**: Build UDF API endpoints for TradingView integration
- [ ] **Martin**: Implement real-time candle updates via WebSocket
- [ ] **Eduardo**: Optimize database queries with appropriate indexes
- [ ] **Team**: Design chart layout for desktop and mobile views

## Follow-up Items
- Evaluate TradingView Advanced Charts for social trading features
- Plan custom indicators for Cooking-specific metrics
- Determine if drawing tools require separate license tier
- Test chart performance with high-frequency data updates

## Technical References
- TradingView Charting Library Docs: https://www.tradingview.com/charting-library-docs/
- UDF Protocol Specification: https://www.tradingview.com/charting-library-docs/latest/connecting_data/UDF
- Pine Script Reference: https://www.tradingview.com/pine-script-reference/v5/

---
**Recording:** Transcription available
**Related Documents:**
- TradingView Integration Requirements (04-knowledge-base/business/requirements/)
- OHLCV Data Schema (04-knowledge-base/technical/)
