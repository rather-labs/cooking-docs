---
title: Indexer Features - 2025-09-23
type: meeting
meeting_type: technical_deep_dive
topic: Indexer
date: 2025-09-23
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# Indexer + Features Technical Discussion - Cooking.gg
**Date:** September 23, 2025, 09:30 GMT-03:00
**Duration:** ~1 hour 10 minutes
**Meeting Type:** Technical Deep Dive
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk

## Executive Summary
Comprehensive discussion on indexer architecture enhancements, new feature requirements, performance optimizations, and protocol coverage expansion. The team addressed ClickHouse query optimization, real-time data processing improvements, and strategies for indexing new Solana protocols.

## Meeting Context
As Cooking.gg scales, the indexer faces increasing demands: more protocols to support, higher query volumes, real-time data requirements, and feature requests requiring complex historical analysis. The team needed to plan architectural improvements and feature additions while maintaining system performance.

## Technical Discussion

### Indexer Architecture Evolution
**Current Architecture**:
- WebSocket connections to Solana RPC for real-time transaction monitoring
- Event-driven processing pipeline for trade extraction
- ClickHouse for time-series storage and analytics
- Redis for caching frequently accessed data

**Proposed Enhancements**:
1. **Multi-RPC Support**: Connect to multiple RPC providers for redundancy
2. **Event Queue**: Kafka or RabbitMQ for buffering and reprocessing
3. **Microindexers**: Specialized indexers per protocol (Radium, Pump.fun, etc.)
4. **Historical Backfill**: Separate service for indexing historical data

### Protocol Coverage Expansion
**Currently Indexed Protocols**:
- Radium AMM (main contract)
- Pump.fun
- Launch Lab
- Orca
- Meteora (partial)

**Protocols to Add**:
- Radium CPMM (Constant Product Market Maker)
- Radium CLMM (Concentrated Liquidity Market Maker)
- Moonshot
- Pump.swap
- Jupiter Aggregator (full coverage)

**Technical Challenge**: Each protocol has unique contract interfaces and event structures

**Solution Approach**:
- Create protocol-specific parsers
- Unified internal event format
- Abstraction layer for common operations
- Version control for contract upgrades

### ClickHouse Query Optimization
**Performance Bottlenecks Identified**:
- Token detail page queries taking 2-3 seconds
- Price history queries inefficient for large timeframes
- Trade history pagination slow for high-volume tokens

**Optimization Strategies**:
1. **Materialized Views**: Pre-aggregate common query patterns
2. **Partition Key Tuning**: Partition by (token_address, date) for faster queries
3. **Projection Optimization**: Create projections sorted by frequently filtered columns
4. **Query Rewriting**: Optimize WHERE clauses and JOIN operations
5. **Sampling**: Use SAMPLE clause for approximations when exact counts not needed

**Example Optimization**:
```sql
-- Before: Slow query for 24h volume
SELECT sum(volume_usd) as volume_24h
FROM trades
WHERE token_address = '...'
  AND timestamp >= now() - INTERVAL 24 HOUR;

-- After: Using materialized view
SELECT volume_24h
FROM token_metrics_hourly
WHERE token_address = '...'
  AND hour >= now() - INTERVAL 24 HOUR;
```

### Real-Time Data Processing
**Latency Goals**:
- Trade to database: < 1 second
- Database to UI update: < 500ms
- End-to-end (trade to user sees update): < 2 seconds

**Optimizations**:
- Batch inserts every 100ms instead of individual INSERTs
- Write to Redis cache simultaneously with ClickHouse write
- WebSocket pub/sub for instant UI updates
- Reduce ClickHouse write batch size for lower latency

### New Feature Requirements
**Top Trader Leaderboard**:
- Track P&L per wallet across all trades
- Time-windowed leaderboards (24h, 7d, 30d, all-time)
- Filter by token or protocol
- Anonymous by default, opt-in to show wallet

**Wallet Analytics**:
- Portfolio value over time
- Win rate percentage
- Average hold time
- Most profitable tokens
- Trading patterns (day/night, weekday/weekend)

**Token Social Metrics**:
- Twitter mentions and sentiment
- Telegram member count
- Website/social link validation
- Audit report integration

**Liquidity Pool Analytics**:
- LP token tracking
- Impermanent loss calculations
- Fee earnings projections
- Pool composition changes over time

### Data Quality & Validation
**Issues Identified**:
- Duplicate trades from multiple RPC providers
- Missed trades during RPC downtime
- Incorrect price calculations for low-liquidity pairs
- Spam tokens polluting dataset

**Solutions**:
- Transaction signature de-duplication
- Gaps detection and automatic backfill
- Price sanity checks (reject outliers >100x from recent average)
- Token quality scoring to filter spam

### Historical Data Backfill
**Requirement**: Index historical trades for tokens launched before Cooking's indexer

**Approach**:
- Use Solana archival nodes for historical transaction data
- Process transactions in batches (10k transactions per job)
- Priority queue: high-volume tokens first
- Rate limit to avoid RPC throttling
- Store backfill progress for resumability

**Technical Implementation**:
```javascript
async function backfillToken(tokenAddress, fromSlot, toSlot) {
  const chunkSize = 10000;
  const signatures = await getSignaturesForAddress(tokenAddress, fromSlot, toSlot);

  for (let i = 0; i < signatures.length; i += chunkSize) {
    const chunk = signatures.slice(i, i + chunkSize);
    const transactions = await getTransactions(chunk);
    const trades = parseTrades(transactions, tokenAddress);
    await insertTrades(trades);

    // Update progress
    await setBackfillProgress(tokenAddress, signatures[i + chunkSize - 1].slot);
  }
}
```

## Key Technical Decisions
- **Decision 1:** Implement microindexers per protocol - Isolates failures, easier to maintain
- **Decision 2:** Kafka for event buffering - Enables reprocessing and guarantees no data loss
- **Decision 3:** Materialized views for common aggregations - Dramatically improves query performance
- **Decision 4:** Multi-RPC provider support - Redundancy and failover capability
- **Decision 5:** Separate backfill service - Doesn't impact real-time indexing performance

## Action Items
- [ ] **Eduardo**: Design Kafka topic schema for trade events
- [ ] **Martin**: Implement Radium CPMM and CLMM parsers
- [ ] **Eduardo**: Create materialized views for token metrics
- [ ] **Martin**: Build backfill service for historical data
- [ ] **Team**: Define data quality metrics and monitoring

## Technical References
- ClickHouse Materialized Views: https://clickhouse.com/docs/en/guides/developer/cascading-materialized-views
- Solana RPC getSignaturesForAddress: https://docs.solana.com/api/http#getsignaturesforaddress

---
**Recording:** Transcription available
**Related Documents:**
- Indexer Architecture Diagram (04-knowledge-base/technical/)
