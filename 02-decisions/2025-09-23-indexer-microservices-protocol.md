---
title: Indexer Microservices by Protocol
type: decision-record
decision-id: ADR-005
date: 2025-09-23
status: accepted
owner: Eduardo Yuschuk, Martin Aranda
stakeholders: [Eduardo Yuschuk, Martin Aranda, Lucas Cufre, Backend Team]
tags: [architecture, indexer, microservices, scalability, blockchain, protocols]
summary: |
  Decision to organize indexer architecture as specialized microindexers per Solana DEX protocol (Raydium, Jupiter, Orca, Pump.fun, etc.) rather than monolithic unified indexer. Each protocol-specific indexer operates independently with standardized internal event format, enabling failure isolation, easier maintenance, and protocol-specific scaling. Kafka event queue buffers trades for reprocessing guarantees.
related-docs:
  - ../06-meetings/2025-09/2025-09-23-indexer-features.md
  - ADR-001: ClickHouse Migration for Time-Series Data
  - ADR-002: Microservices Architecture by Trading Algorithm
  - ADR-003: WebSocket to SSE Migration
---

# Indexer Microservices by Protocol

## Context and Problem Statement

Cooking.gg's indexer extracts real-time trading data from the Solana blockchain across multiple decentralized exchanges (DEXs). As the platform scales, the indexer faces increasing complexity and performance demands:

**Challenges with Current Unified Indexer:**

1. **Protocol Diversity**:
   - Each DEX protocol has unique contract interfaces and event structures
   - Raydium AMM vs CPMM vs CLMM: three different contract versions
   - Pump.fun vs Orca vs Jupiter: completely different architectures
   - Constant protocol upgrades requiring parser updates
   - New protocols launching frequently (Moonshot, Pump.swap)

2. **Scaling Demands**:
   - Higher query volumes as user base grows (2,000 → 200,000 users)
   - Real-time data requirements (<2 second end-to-end latency)
   - Complex historical analysis queries (24h volume, 7d trends, wallet analytics)
   - ClickHouse query performance bottlenecks (2-3 second token detail pages)

3. **Reliability Requirements**:
   - Single protocol failure shouldn't cascade to entire system
   - RPC provider outages must not cause complete data loss
   - Need to backfill historical data without impacting real-time indexing
   - Data quality issues (duplicates, missed trades, incorrect prices)

4. **Maintenance Burden**:
   - Single codebase handling all protocol parsing logic
   - Contract upgrades affect entire indexer (deployment risk)
   - Debugging protocol-specific issues difficult in unified system
   - Knowledge centralization (Eduardo as single indexer expert)

**Currently Indexed Protocols:**
- Raydium AMM (main contract)
- Pump.fun
- Launch Lab
- Orca
- Meteora (partial)

**Protocols Requiring Addition:**
- Raydium CPMM (Constant Product Market Maker)
- Raydium CLMM (Concentrated Liquidity Market Maker)
- Moonshot
- Pump.swap
- Jupiter Aggregator (full coverage)

**Key Requirements:**
- Failure isolation: protocol failures don't cascade
- Independent scaling per protocol based on volume
- Easier maintenance: update protocol parsers independently
- Data quality: no trade loss, no duplicates
- Historical backfill without impacting real-time processing
- Real-time latency: <2 seconds trade-to-UI

## Decision

**Implement specialized microindexer architecture: separate microservice per DEX protocol, with Kafka event buffering, unified internal event format, and independent backfill service.**

### Architecture Components

**Protocol-Specific Microindexers:**

Each protocol gets dedicated microservice:
- **Raydium AMM Indexer**: Original Raydium contracts
- **Raydium CPMM Indexer**: Constant Product Market Maker variant
- **Raydium CLMM Indexer**: Concentrated Liquidity Market Maker variant
- **Pump.fun Indexer**: Pump.fun bonding curve contracts
- **Jupiter Indexer**: Jupiter aggregator swap events
- **Orca Indexer**: Orca whirlpool contracts
- **Launch Lab Indexer**: Launch Lab specific events
- **Meteora Indexer**: Meteora dynamic pools

Each microindexer handles:
- WebSocket connection to Solana RPC (dedicated connection pool)
- Protocol-specific transaction parsing
- Event extraction and normalization
- Publishing to Kafka event queue
- Protocol-specific error handling and retries

**Kafka Event Queue (Central Hub):**
- Buffering layer between microindexers and database
- Enables reprocessing (replay trades if processing fails)
- Guarantees no data loss (persistent queue)
- Decouples producers (microindexers) from consumers (processors)
- Allows multiple consumers (real-time + analytics + backfill validation)

**Unified Trade Processing Service:**
- Consumes trades from Kafka topics
- Validates and de-duplicates trades (cross-protocol)
- Calculates derived metrics (USD volume, price, liquidity)
- Writes to ClickHouse in batches (100ms intervals)
- Simultaneous Redis cache write for instant queries
- WebSocket pub/sub for UI real-time updates

**Historical Backfill Service (Separate):**
- Independent service for historical data indexing
- Uses Solana archival nodes (not real-time RPC)
- Processes in batches (10k transactions per job)
- Priority queue: high-volume tokens first
- Rate-limited to avoid RPC throttling
- Stores progress for resumability
- Doesn't impact real-time indexing performance

**Multi-RPC Provider Support:**
- Each microindexer connects to multiple RPC providers
- Automatic failover on RPC downtime
- De-duplication handles same trade from multiple sources
- Redundancy ensures no missed trades

### Unified Internal Event Format

**Standardized Trade Event:**
```json
{
  "signature": "5xK3...",
  "slot": 123456789,
  "timestamp": 1695123456,
  "protocol": "raydium_amm",
  "protocol_version": "4",
  "token_address": "EPjF...",
  "quote_token": "So11...",
  "trader_wallet": "7xH...",
  "trade_type": "buy",
  "amount_tokens": 1000000,
  "amount_quote": 0.5,
  "price": 0.0000005,
  "fee": 0.0025,
  "liquidity_pool": "8Qp...",
  "metadata": {
    "protocol_specific": {}
  }
}
```

**Benefits:**
- Protocol-specific parsers output standardized format
- Downstream processing (database, analytics) protocol-agnostic
- Can add new protocols without changing consumers
- Versioning per protocol (track contract upgrades)

### ClickHouse Integration

**Materialized Views for Performance:**
```sql
-- Pre-aggregated token metrics (updated incrementally)
CREATE MATERIALIZED VIEW token_metrics_hourly
ENGINE = AggregatingMergeTree()
PARTITION BY toYYYYMMDD(hour)
ORDER BY (token_address, hour)
AS SELECT
  token_address,
  toStartOfHour(timestamp) as hour,
  sumState(volume_usd) as volume_24h,
  avgState(price) as avg_price,
  countState(*) as trade_count
FROM trades
GROUP BY token_address, hour;
```

**Partition Strategy:**
- Partition by (token_address, date)
- Faster queries for specific token time ranges
- Efficient data pruning for old data

**Projection Optimization:**
- Projections sorted by frequently filtered columns
- Pre-sorted data accelerates WHERE clauses
- Reduces query time from 2-3s to <500ms

### Data Quality & Validation

**De-duplication Strategy:**
- Transaction signature as unique key
- Multiple RPC providers may return same trade
- Kafka consumer de-duplicates before database write
- Prevents double-counting from redundant sources

**Gap Detection:**
- Monitor slot progression per microindexer
- Detect missed slots (RPC downtime, network issues)
- Automatic backfill triggers for detected gaps
- Alerts for gaps >100 slots

**Price Sanity Checks:**
- Reject prices >100x from recent average (likely spam/error)
- Cross-validate against multiple liquidity pools
- Flag low-liquidity trades for manual review

**Token Quality Scoring:**
- Filter spam tokens from UI
- Score based on: liquidity, holder count, social presence, audit status
- Quality threshold for inclusion in trending/discovery

## Rationale

### Failure Isolation (Primary Driver)

**Monolithic Risk:**
- Single bug in Raydium parser crashes entire indexer
- All protocols stop indexing during deployment
- Debugging difficult (all protocol logic in one codebase)
- Contract upgrade forces full indexer redeploy

**Microindexer Benefits:**
- Raydium CLMM parser bug: only CLMM indexer affected
- Can deploy Pump.fun indexer update without touching Raydium
- Orca indexer crashes: Raydium, Jupiter, Pump.fun continue operating
- Each microindexer has isolated failure domain

**Real-World Context:**
Eduardo Yuschuk (indexer specialist) raised concerns about knowledge centralization (see ADR-002). Microindexers reduce blast radius of his absence - team members can work on individual protocol parsers independently.

### Protocol-Specific Complexity

**Each Protocol Requires Specialized Parsing:**

**Raydium AMM:**
```javascript
// Raydium AMM swap instruction layout
const SWAP_LAYOUT = struct([
  u64('amountIn'),
  u64('minimumAmountOut'),
]);
```

**Pump.fun:**
```javascript
// Pump.fun bonding curve buy instruction
const BUY_LAYOUT = struct([
  u64('tokenAmount'),
  u64('solAmount'),
  u64('maxSolCost'),
]);
```

**Jupiter Aggregator:**
```javascript
// Jupiter route-based swap (multi-hop)
const ROUTE_SWAP_LAYOUT = struct([
  publicKey('sourceMint'),
  publicKey('destinationMint'),
  array(publicKey(), 'route'),  // Multi-hop route
  u64('inAmount'),
  u64('outAmount'),
]);
```

**Protocol Differences:**
- Instruction layouts: Different binary structures
- Event logs: Different event types and formats
- Multi-hop swaps: Jupiter routes through multiple DEXs (complex parsing)
- Bonding curves: Pump.fun price calculation unique
- Liquidity math: Raydium CLMM (concentrated liquidity) vs AMM (xy=k)

**Microindexers Enable:**
- Each parser optimized for specific protocol
- Version control per protocol (Raydium v4 vs v5)
- Can update Raydium parser without risking Pump.fun
- Team members can specialize (reduce Eduardo's bus factor)

### Scalability: Independent Scaling Per Protocol

**Volume Distribution (Not Uniform):**
- Raydium: 10,000 trades/hour (highest volume)
- Pump.fun: 5,000 trades/hour (high volume)
- Jupiter: 8,000 trades/hour (aggregator, multi-protocol)
- Orca: 1,000 trades/hour (lower volume)
- Launch Lab: 100 trades/hour (niche)

**Monolithic Scaling Problem:**
- Must scale entire indexer for Raydium's volume
- Wastes resources on low-volume protocol parsers
- Cannot optimize for protocol-specific characteristics

**Microindexer Scaling Solution:**
- Raydium indexer: 5 instances (high volume)
- Pump.fun indexer: 3 instances (medium volume)
- Orca indexer: 1 instance (low volume sufficient)
- Each scales horizontally based on actual load
- Kafka partitioning distributes work across instances

**Resource Optimization:**
- Raydium indexer: more RPC connections, higher batch size
- Launch Lab indexer: minimal resources, lower priority
- Cost-efficient: pay for what you need per protocol

### Kafka for Reliability & Reprocessing

**Why Kafka Over Direct Database Writes:**

**Problem with Direct Writes:**
- Trade parsed → Write to ClickHouse fails → Trade lost forever
- ClickHouse temporary downtime = data loss
- Cannot replay trades if processing logic changes
- No buffering for database write bursts

**Kafka Advantages:**
- **Persistent Queue**: Trades buffered on disk, survive microindexer restarts
- **Reprocessing**: Can replay trades from Kafka if database corrupted
- **Decoupling**: Microindexers publish, processor consumes independently
- **Guaranteed Delivery**: At-least-once semantics (de-duplicate downstream)
- **Multiple Consumers**: Real-time processor + analytics + validation

**Example Scenario:**
1. ClickHouse crashes (hardware failure)
2. Trades continue buffering in Kafka (no data loss)
3. ClickHouse restored
4. Processor resumes consuming from Kafka offset
5. All buffered trades processed (no gap)

**Alternative (RabbitMQ):**
Team considered RabbitMQ but chose Kafka for:
- Better persistence guarantees
- Higher throughput (blockchain data volume)
- Stronger ordering guarantees
- Better tooling for monitoring/replay

### Materialized Views for Query Performance

**Problem:**
Token detail page query taking 2-3 seconds:
```sql
SELECT sum(volume_usd) as volume_24h
FROM trades
WHERE token_address = 'EPjF...'
  AND timestamp >= now() - INTERVAL 24 HOUR;
-- Scans millions of rows, slow
```

**Solution:**
Materialized view pre-aggregates:
```sql
SELECT volume_24h FROM token_metrics_hourly
WHERE token_address = 'EPjF...'
  AND hour >= now() - INTERVAL 24 HOUR;
-- Scans 24 pre-aggregated rows, fast (<500ms)
```

**Performance Impact:**
- Before: 2-3 seconds (scanning raw trades)
- After: <500ms (querying hourly aggregates)
- Enables real-time dashboard performance

**Aligns with ClickHouse Migration (ADR-001):**
Materialized views leverage ClickHouse strengths (incremental aggregation)

### Separate Backfill Service

**Why Separate from Real-Time Indexing:**

**Problems with Unified Backfill:**
- Historical data processing competes with real-time
- Backfill RPC calls slow real-time transaction processing
- Database write bursts from backfill impact query performance
- Cannot prioritize real-time over historical

**Separate Service Benefits:**
- **Isolated Resources**: Backfill doesn't steal RPC connections from real-time
- **Different RPC Endpoints**: Backfill uses archival nodes (slower but complete history)
- **Batch Scheduling**: Process during off-peak hours
- **Resumability**: Store progress, restart from last checkpoint
- **Priority Control**: High-volume tokens backfilled first

**Implementation:**
- Separate Kubernetes deployment
- Lower resource priority (CPU/memory)
- Rate-limited RPC calls (avoid throttling)
- Batched database writes (10k trades per transaction)

## Consequences

### Positive

**Reliability & Resilience:**
- Protocol failure isolation (Orca crash doesn't affect Raydium)
- Multi-RPC provider redundancy (no single point of failure)
- Kafka persistence guarantees no trade loss
- Gap detection and automatic backfill
- Can deploy protocol updates independently (lower risk)

**Scalability:**
- Independent scaling per protocol based on volume
- Kafka partitioning distributes load
- Horizontal scaling per microindexer
- Resource optimization (pay for what you need)
- Materialized views reduce query load 5x-10x

**Maintainability:**
- Clear ownership per protocol (reduce bus factor)
- Isolated codebases easier to understand
- Update one protocol parser without risking others
- Debugging scoped to specific protocol
- Version control per protocol (track contract upgrades)

**Performance:**
- Materialized views: 2-3s → <500ms queries
- Real-time latency: <2 seconds trade-to-UI
- Kafka buffering handles write bursts
- Backfill service doesn't impact real-time
- Redis cache + ClickHouse writes simultaneous

**Development Velocity:**
- Parallel development on different protocol parsers
- Can add new protocol without touching existing
- Testing isolated per protocol
- Faster deployment cycles (smaller blast radius)

**Data Quality:**
- De-duplication across multiple RPC providers
- Price sanity checks filter spam
- Gap detection prevents missed trades
- Token quality scoring for UI filtering

### Negative

**Operational Complexity:**
- More services to deploy, monitor, manage (8+ microindexers vs 1)
- Kafka adds infrastructure dependency (must maintain)
- Multiple RPC provider subscriptions (cost)
- Distributed debugging challenges (trade through Kafka)
- Need monitoring per microindexer

**Infrastructure Costs:**
- Each microindexer requires compute resources
- Kafka cluster infrastructure (3+ brokers for HA)
- Multiple RPC provider subscriptions
- Redis caching layer
- Separate backfill service resources

**Initial Migration Effort:**
- Refactor existing unified indexer to microindexers
- Set up Kafka infrastructure
- Implement standardized event format
- Migrate existing trade data
- Build backfill service from scratch

**Kafka Learning Curve:**
- Team needs Kafka expertise (Eduardo familiar, but others?)
- Monitoring Kafka topics, consumer lag, offsets
- Debugging Kafka issues (serialization, partitioning)
- Operational overhead (Kafka upgrades, tuning)

**Data Duplication Risk:**
- Multiple RPC providers may return same trade
- Must de-duplicate before database write
- Incorrect de-duplication = missing trades or duplicates
- Testing edge cases complex

**Protocol Version Management:**
- Must track contract upgrades per protocol
- Version schema in event format
- Backward compatibility for old events
- Migration path when protocols upgrade

### Neutral

- Standardized event format (helpful but adds abstraction layer)
- Multi-RPC providers (reliability vs cost tradeoff)
- Materialized views (performance vs storage tradeoff)
- Separate backfill service (complexity vs isolation benefit)

## Alternatives Considered

### Option 1: Monolithic Unified Indexer (Status Quo)
**Description:** Single indexer service handling all protocol parsing

**Pros:**
- Simplest deployment (one service)
- Shared resources (single RPC connection pool)
- Centralized monitoring and logging
- No Kafka dependency
- Easier to debug (single codebase)

**Cons:**
- Protocol failure cascades to entire indexer
- Cannot scale protocols independently
- Deployment risk (update one protocol, risk all)
- Protocol-specific complexity mixed together
- Single RPC provider = single point of failure
- Knowledge centralized in Eduardo (bus factor)

**Why Rejected:** Failure isolation critical as scale increases. Single Raydium parsing bug shouldn't stop Pump.fun indexing. Eduardo's concern about knowledge centralization (mentioned in ADR-002 meeting) highlights bus factor risk.

### Option 2: Microindexers Without Kafka (Direct Database Writes)
**Description:** Protocol-specific microindexers, but write directly to ClickHouse

**Pros:**
- Failure isolation achieved
- Independent scaling per protocol
- No Kafka infrastructure dependency
- Simpler architecture (fewer moving parts)
- Lower latency (no Kafka hop)

**Cons:**
- No buffering: database downtime = data loss
- Cannot reprocess trades (no replay capability)
- Write bursts overwhelm database
- No at-least-once delivery guarantees
- Difficult to add analytics consumers

**Why Rejected:** Kafka's reliability guarantees critical for financial data. Cannot risk losing trades during ClickHouse outages. Reprocessing capability valuable for fixing bugs in processing logic.

### Option 3: Single Indexer + Kafka (No Microindexers)
**Description:** Keep unified indexer, add Kafka for buffering

**Pros:**
- Kafka reliability benefits
- Simpler than microindexers (single codebase)
- Buffering and reprocessing capability
- Easier to deploy (one service)

**Cons:**
- No failure isolation between protocols
- Cannot scale protocols independently
- Deployment still risky (all protocols together)
- Protocol complexity still mixed
- Doesn't address maintenance burden

**Why Rejected:** Doesn't solve failure isolation problem. Kafka adds reliability but not scalability or maintainability. Microindexers + Kafka achieves both.

### Option 4: Serverless Functions Per Protocol (AWS Lambda)
**Description:** Lambda function per protocol triggered by blockchain events

**Pros:**
- Auto-scaling built-in
- Pay-per-invocation pricing
- No server management
- Isolation by design

**Cons:**
- Cold start latency unacceptable for real-time (<2s requirement)
- Difficult to maintain WebSocket connections (Solana RPC)
- Lambda execution time limits (15 minutes)
- Vendor lock-in to AWS
- Team unfamiliar with serverless patterns

**Why Rejected:** Real-time blockchain indexing requires persistent WebSocket connections. Lambda cold starts incompatible with <2 second latency requirement.

### Option 5: Third-Party Indexing Service (e.g., Helius, SimpleHash)
**Description:** Use third-party Solana indexing API instead of building own

**Pros:**
- No indexer infrastructure to maintain
- Instant access to all protocols
- Experts handle protocol upgrades
- Lower initial development cost

**Cons:**
- Vendor lock-in (pricing changes, API limits)
- Cannot customize for Cooking-specific features
- May not support all protocols needed (Pump.fun edge cases)
- Data latency (depends on vendor)
- Cost at scale (per-API-call pricing expensive)
- Privacy concerns (trading data through third party)

**Why Rejected:** Control over indexer critical for platform differentiation. Custom features (top trader leaderboard, wallet analytics) require custom indexing logic. Cost at scale (200,000 users) prohibitive with per-API-call pricing.

## Implementation Notes

### Microindexer Deployment Architecture

**Kubernetes Configuration:**
```yaml
# Raydium AMM Indexer (high volume)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: raydium-amm-indexer
spec:
  replicas: 5  # Scale for volume
  template:
    spec:
      containers:
      - name: indexer
        env:
        - name: PROTOCOL: raydium_amm
        - name: KAFKA_TOPIC: trades-raydium-amm
        - name: RPC_PROVIDERS: ["helius", "quicknode", "triton"]
        resources:
          requests:
            cpu: 500m
            memory: 1Gi

# Launch Lab Indexer (low volume)
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: launchlab-indexer
spec:
  replicas: 1  # Low volume, single instance sufficient
  template:
    spec:
      containers:
      - name: indexer
        env:
        - name: PROTOCOL: launchlab
        - name: KAFKA_TOPIC: trades-launchlab
        resources:
          requests:
            cpu: 100m  # Lower resource allocation
            memory: 256Mi
```

### Kafka Topic Structure

**Trade Topics by Protocol:**
```
trades-raydium-amm        (10 partitions, high volume)
trades-raydium-cpmm       (5 partitions)
trades-raydium-clmm       (5 partitions)
trades-pumpfun            (8 partitions, high volume)
trades-jupiter            (10 partitions, aggregator)
trades-orca               (3 partitions)
trades-launchlab          (1 partition, low volume)
trades-meteora            (2 partitions)
```

**Partition Strategy:**
- Partition key: `token_address`
- Ensures all trades for same token go to same partition
- Enables ordered processing per token
- Partitions = parallelism for consumers

**Retention Policy:**
- 7 days retention (reprocessing window)
- Compression: lz4 (balance speed/size)
- Replication factor: 3 (high availability)

### Unified Trade Processing Consumer

**Consumer Group Pattern:**
```javascript
const consumer = kafka.consumer({ groupId: 'trade-processor' });

await consumer.subscribe({
  topics: [
    'trades-raydium-amm',
    'trades-pumpfun',
    'trades-jupiter',
    // ... all protocol topics
  ]
});

await consumer.run({
  eachBatch: async ({ batch, resolveOffset }) => {
    const trades = batch.messages.map(msg => JSON.parse(msg.value));

    // De-duplicate across protocols
    const dedupedTrades = deduplicateBySignature(trades);

    // Calculate derived metrics
    const enrichedTrades = enrichTrades(dedupedTrades);

    // Batch write to ClickHouse
    await clickhouse.insert('trades', enrichedTrades);

    // Simultaneous Redis cache update
    await redis.pipeline(enrichedTrades.map(t =>
      ['set', `trade:${t.signature}`, JSON.stringify(t), 'EX', 3600]
    )).exec();

    // WebSocket pub/sub for UI
    enrichedTrades.forEach(trade => {
      pubsub.publish(`token:${trade.token_address}`, trade);
    });

    await resolveOffset(batch.lastOffset());
  }
});
```

### Protocol Parser Interface

**Standardized Parser Contract:**
```typescript
interface ProtocolParser {
  protocolName: string;
  protocolVersion: string;

  // Parse transaction to extract trades
  parseTrades(transaction: Transaction): Trade[];

  // Validate trade data integrity
  validateTrade(trade: Trade): boolean;

  // Calculate protocol-specific metrics
  calculateMetrics(trade: Trade): TradeMetrics;
}

// Example: Raydium AMM Parser
class RaydiumAMMParser implements ProtocolParser {
  protocolName = 'raydium_amm';
  protocolVersion = '4';

  parseTrades(tx: Transaction): Trade[] {
    const swapInstructions = tx.message.instructions.filter(
      instr => this.isSwapInstruction(instr)
    );

    return swapInstructions.map(instr => {
      const data = this.decodeSwapInstruction(instr);

      return {
        signature: tx.signature,
        protocol: this.protocolName,
        protocol_version: this.protocolVersion,
        // ... extract trade details
      };
    });
  }
}
```

### Historical Backfill Service

**Priority Queue Implementation:**
```javascript
// Priority queue: high-volume tokens first
const backfillQueue = [
  { tokenAddress: 'EPjF...', priority: 1, volume24h: 10000000 },
  { tokenAddress: '7xH...', priority: 1, volume24h: 5000000 },
  { tokenAddress: '8Qp...', priority: 2, volume24h: 1000000 },
  // ... sorted by volume descending
];

async function processBackfillQueue() {
  for (const token of backfillQueue) {
    const progress = await getBackfillProgress(token.tokenAddress);

    if (progress.completed) continue;

    await backfillToken(
      token.tokenAddress,
      progress.lastSlot || 0,  // Resume from last checkpoint
      getCurrentSlot()
    );

    await markBackfillComplete(token.tokenAddress);

    // Rate limit: 1 second between tokens (avoid RPC throttle)
    await sleep(1000);
  }
}
```

### Monitoring & Alerting

**Key Metrics Per Microindexer:**
- Trades processed per minute
- RPC connection health (WebSocket uptime)
- Kafka publish latency
- Parse errors per protocol
- RPC failover events

**ClickHouse Query Performance:**
- Query latency (p50, p95, p99)
- Materialized view lag (how far behind real-time)
- Write throughput (inserts per second)
- Partition size and growth rate

**Kafka Health:**
- Consumer lag per topic (how far behind)
- Partition rebalancing events
- Message throughput per topic
- Disk usage and retention

**Alerts:**
- Microindexer offline >1 minute (critical)
- Consumer lag >10,000 messages (warning)
- Parse error rate >1% (warning)
- All RPC providers down (critical)
- Materialized view lag >5 minutes (warning)

## References

### Meeting Notes
- [Indexer Features Technical Deep Dive 2025-09-23](../06-meetings/2025-09/2025-09-23-indexer-features.md) - Comprehensive indexer architecture discussion

### Related Decisions
- ADR-001: ClickHouse Migration for Time-Series Data (storage layer)
- ADR-002: Microservices Architecture by Trading Algorithm (microservices pattern)
- ADR-003: WebSocket to SSE Migration (real-time updates to UI)

### Technical References
- ClickHouse Materialized Views: https://clickhouse.com/docs/en/guides/developer/cascading-materialized-views
- Solana RPC Documentation: https://docs.solana.com/api/http
- Apache Kafka Documentation: https://kafka.apache.org/documentation/
- Raydium Program Documentation
- Jupiter Aggregator Documentation

### Protocol Specifications
- Raydium AMM Program ID: 675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8
- Pump.fun Program ID: 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P
- Jupiter Aggregator: JUP4Fb2cqiRUcaTHdrPC8h2gNsA2ETXiPDD33WcGuJB

### Data Quality
- Transaction de-duplication strategy
- Price sanity check thresholds
- Token quality scoring algorithm

## Revision History
- 2025-09-23: Microindexer architecture decision made
- 2025-09-23: Kafka chosen for event buffering
- 2025-09-23: Materialized views strategy defined
- 2025-10-21: Formal ADR documented from meeting notes
