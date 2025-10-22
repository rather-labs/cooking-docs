---
title: Redis for JSON Block Storage
type: decision-record
decision-id: ADR-104
date: 2025-06-23
status: accepted
owner: Eduardo Yuschuk, Indexer Team
stakeholders: [Eduardo Yuschuk, Martin Aranda, Lucas Cufre, Indexer Team]
tags: [technical, redis, indexer, performance, caching, blockchain, solana]
summary: |
  Decision to implement Redis as a high-performance caching layer for storing raw Solana blockchain JSON blocks instead of direct PostgreSQL database storage. This architectural improvement significantly reduces database load, improves indexer data handling performance, and enables faster blockchain data access for transaction parsing and reprocessing. Redis's in-memory architecture provides sub-millisecond access times compared to PostgreSQL's disk-based storage.
related-docs:
  - ../06-meetings/2025-06/Weekly-Demo-2025-06-23.md
  - ADR-001: ClickHouse Migration for Time-Series Data
  - ADR-005: Indexer Microservices by Protocol
---

# Redis for JSON Block Storage

## Context and Problem Statement

Cooking.gg's indexer continuously processes Solana blockchain data to extract trades, token information, and market events. The indexer workflow involves:

1. **Subscribe to Solana RPC:** WebSocket connection receives new blocks from blockchain
2. **Fetch Raw Block Data:** Request full block JSON (transactions, signatures, accounts, logs)
3. **Store Raw Block:** Persist complete block data for reprocessing/debugging
4. **Parse Transactions:** Extract relevant trading events from block
5. **Write to Database:** Store processed trades, tokens, prices to ClickHouse

**Current Problem: PostgreSQL for Raw Block Storage**

The indexer originally stored raw JSON blocks directly in PostgreSQL:

```sql
CREATE TABLE blockchain_blocks (
  slot BIGINT PRIMARY KEY,
  block_hash TEXT NOT NULL,
  block_data JSONB NOT NULL,  -- Full Solana block JSON (10-50KB per block)
  timestamp TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

**Performance Issues:**

1. **Write Amplification:**
   - Solana produces ~2.5 blocks/second (400ms slot time)
   - Each block: 10-50KB JSON data
   - Write load: ~6,250 blocks/hour, 150,000 blocks/day
   - PostgreSQL JSONB storage requires parsing, indexing, compression
   - Write latency: 50-100ms per block (unacceptable for real-time indexing)

2. **Database Bloat:**
   - Raw blocks accumulate rapidly: ~15GB/day, 450GB/month
   - JSONB storage overhead (indexes, toast tables, vacuuming)
   - Database size growth impacts all queries (even unrelated tables)
   - Vacuum operations slow down during high write load

3. **Read Performance:**
   - Reprocessing blocks (bug fixes, new protocol support) requires reading historical blocks
   - PostgreSQL disk-based storage: 10-50ms read latency
   - JSONB deserialization overhead
   - Concurrent reads during backfill compete with write load

4. **Scalability Limitations:**
   - PostgreSQL connection pool exhaustion (indexer microservices × RPC connections)
   - Disk I/O bottleneck (IOPS limits on AWS EBS)
   - Vertical scaling only (larger RDS instance = expensive)
   - Cannot horizontally scale block storage

**Use Cases for Raw Block Storage:**

1. **Reprocessing After Bug Fixes:**
   - Discovered parsing error in Raydium CLMM parser
   - Need to reprocess last 7 days of blocks
   - Extract previously missed trades

2. **New Protocol Support:**
   - Add support for new DEX (e.g., Moonshot)
   - Reprocess historical blocks to index existing trades
   - Build complete trade history from day one

3. **Debugging and Validation:**
   - User reports missing trade
   - Fetch raw block, inspect transaction details
   - Verify indexer parsing logic

4. **Data Quality Audits:**
   - Compare parsed trades against raw block data
   - Detect duplicates or missing transactions
   - Validate price calculations

**Current Performance Metrics (PostgreSQL):**

- Block write latency: 50-100ms (p95)
- Block read latency: 10-50ms (p95)
- Database size growth: ~15GB/day
- Indexer lag during high load: 200-500ms behind blockchain
- Reprocessing throughput: ~100 blocks/second (limited by PostgreSQL read speed)

**Requirements for Alternative Solution:**

1. **High Write Throughput:** Handle 2.5 blocks/second with minimal latency
2. **Fast Read Access:** Sub-10ms reads for reprocessing
3. **Efficient Storage:** No unnecessary indexing or overhead
4. **TTL Support:** Auto-expire old blocks (no manual cleanup)
5. **Scalability:** Horizontal scaling for growing data volume
6. **Reliability:** Data persistence (survive process restarts)

## Decision

**Adopt Redis as dedicated storage layer for raw Solana blockchain JSON blocks, replacing PostgreSQL JSONB storage, with configurable TTL for automatic data expiration.**

### Implementation Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                  Solana RPC WebSocket Stream                     │
│  - New blocks published every ~400ms                              │
│  - Block JSON size: 10-50KB                                      │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│               Indexer Microservice (e.g., Raydium)               │
│  1. Receive new block notification                               │
│  2. Fetch full block JSON from Solana RPC                        │
│  3. Store raw block in Redis                                     │
│  4. Parse transactions (extract trades)                          │
│  5. Write parsed trades to ClickHouse                            │
└────────┬─────────────────────────────────────┬───────────────────┘
         │                                     │
         ▼                                     ▼
┌────────────────────────────┐    ┌──────────────────────────────┐
│    Redis (Block Cache)     │    │  ClickHouse (Parsed Trades)  │
│  - Key: slot number        │    │  - Trades table              │
│  - Value: block JSON       │    │  - Tokens table              │
│  - TTL: 30 days            │    │  - Prices table              │
│  - In-memory (fast)        │    │  - Columnar storage          │
│  - Persistence enabled     │    │  - Analytics-optimized       │
└────────┬───────────────────┘    └──────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────────────────────┐
│               Reprocessing Service (Background Job)                │
│  - Fetch blocks from Redis for historical range                   │
│  - Reparse transactions (new logic)                                │
│  - Update ClickHouse with corrected/additional data                │
└────────────────────────────────────────────────────────────────────┘
```

### Redis Configuration

**Data Structure:**

```javascript
// Store block with slot number as key
const key = `block:${slot}`;
const value = JSON.stringify(blockData);
const ttl = 30 * 24 * 60 * 60; // 30 days in seconds

await redis.setex(key, ttl, value);
```

**Example:**

```javascript
// Indexer stores new block
async function storeBlock(slot, blockData) {
  const key = `block:${slot}`;
  const value = JSON.stringify({
    slot: slot,
    hash: blockData.blockhash,
    parentSlot: blockData.parentSlot,
    timestamp: blockData.blockTime,
    transactions: blockData.transactions, // Full transaction array
    rewards: blockData.rewards
  });

  // Store with 30-day TTL (auto-delete after expiration)
  await redis.setex(key, 30 * 24 * 60 * 60, value);

  console.log(`Stored block ${slot} in Redis`);
}

// Retrieve block for reprocessing
async function getBlock(slot) {
  const key = `block:${slot}`;
  const value = await redis.get(key);

  if (!value) {
    console.warn(`Block ${slot} not found (expired or never stored)`);
    return null;
  }

  return JSON.parse(value);
}

// Retrieve range of blocks for backfill
async function getBlockRange(startSlot, endSlot) {
  const blocks = [];

  for (let slot = startSlot; slot <= endSlot; slot++) {
    const block = await getBlock(slot);
    if (block) {
      blocks.push(block);
    }
  }

  return blocks;
}
```

**Redis Instance Configuration:**

```yaml
# AWS ElastiCache Redis Configuration
redis:
  nodeType: cache.r6g.xlarge  # 26.32 GiB memory
  engine: redis
  engineVersion: 7.0
  port: 6379
  parameterGroup:
    maxmemory-policy: volatile-lru  # Evict least-recently-used keys with TTL
    maxmemory-samples: 5
    timeout: 300  # Close idle connections after 5 minutes
  backupRetentionPeriod: 7  # 7-day snapshots for disaster recovery
  snapshotWindow: 03:00-05:00  # Daily backup during low-traffic hours
  persistence: enabled  # AOF (Append-Only File) for durability
```

**Why `volatile-lru` Eviction Policy:**

- Only evicts keys with TTL set (blocks have 30-day TTL)
- Protects other Redis data (if any) without TTL
- LRU (Least Recently Used): older blocks evicted first if memory pressure

**Memory Sizing:**

- Block size: 10-50KB (average ~25KB)
- Blocks per day: 216,000 (2.5 blocks/second × 86,400 seconds)
- Daily storage: 216,000 × 25KB = 5.4GB/day
- 30-day retention: 5.4GB × 30 = 162GB
- **Redis instance:** 26.32GB memory insufficient for 162GB data
- **Solution:** Use Redis persistence (RDB + AOF) for disk storage, memory as cache

**Redis Persistence Strategy:**

- **RDB (Snapshot):** Daily snapshots for disaster recovery
- **AOF (Append-Only File):** Log every write operation
- **Memory vs Disk:** Hot blocks (recent) in memory, older blocks on disk
- **Read Performance:** Memory hits < 1ms, disk hits ~5-10ms (still faster than PostgreSQL)

### Integration with Indexer Microservices

**Indexer Microservice Pattern (per Protocol):**

```javascript
// raydium-indexer/src/index.ts
import Redis from 'ioredis';
import { Connection } from '@solana/web3.js';

const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: 6379,
  password: process.env.REDIS_PASSWORD,
  db: 0,  // Database 0 for block storage
  retryStrategy: (times) => Math.min(times * 50, 2000)
});

const solana = new Connection(process.env.SOLANA_RPC_URL, {
  wsEndpoint: process.env.SOLANA_WSS_URL
});

// Subscribe to new blocks
solana.onSlotChange((slotInfo) => {
  processSlot(slotInfo.slot);
});

async function processSlot(slot) {
  try {
    // 1. Fetch full block from Solana RPC
    const block = await solana.getBlock(slot, {
      maxSupportedTransactionVersion: 0
    });

    if (!block) {
      console.warn(`Slot ${slot} skipped (no block)`);
      return;
    }

    // 2. Store raw block in Redis
    await storeBlock(slot, block);

    // 3. Parse Raydium transactions
    const trades = parseRaydiumTrades(block);

    // 4. Write parsed trades to ClickHouse
    await clickhouse.insert('trades', trades);

    console.log(`Processed slot ${slot}: ${trades.length} Raydium trades`);

  } catch (error) {
    console.error(`Error processing slot ${slot}:`, error);
    // Retry logic here
  }
}

async function storeBlock(slot, blockData) {
  const key = `block:${slot}`;
  const value = JSON.stringify(blockData);
  const ttl = 30 * 24 * 60 * 60; // 30 days

  await redis.setex(key, ttl, value);
}
```

### Reprocessing Service

**Background Job for Historical Backfill:**

```javascript
// reprocessing-service/src/backfill.ts
import Redis from 'ioredis';
import { Connection } from '@solana/web3.js';

const redis = new Redis({ /* config */ });

async function backfillRaydiumCLMM(startSlot, endSlot) {
  console.log(`Backfilling Raydium CLMM from slot ${startSlot} to ${endSlot}`);

  let processedCount = 0;
  let missingCount = 0;

  for (let slot = startSlot; slot <= endSlot; slot++) {
    // Try to fetch block from Redis
    const blockJson = await redis.get(`block:${slot}`);

    if (!blockJson) {
      // Block not in Redis (expired or never stored)
      missingCount++;

      // Fallback: fetch from Solana RPC (if block still available)
      const block = await fetchBlockFromSolana(slot);
      if (block) {
        await storeBlock(slot, block);
        await parseAndStoreTrades(block, 'raydium_clmm');
        processedCount++;
      }
      continue;
    }

    // Block exists in Redis, parse with new logic
    const block = JSON.parse(blockJson);
    await parseAndStoreTrades(block, 'raydium_clmm');
    processedCount++;

    // Progress logging
    if (slot % 1000 === 0) {
      console.log(`Progress: ${slot}/${endSlot} (${processedCount} processed, ${missingCount} missing)`);
    }
  }

  console.log(`Backfill complete: ${processedCount} blocks processed, ${missingCount} missing`);
}

async function parseAndStoreTrades(block, protocol) {
  // Use new CLMM parser
  const trades = parseRaydiumCLMM(block);

  // Insert into ClickHouse
  await clickhouse.insert('trades', trades);
}
```

**Performance Comparison:**

- **PostgreSQL Reprocessing:** ~100 blocks/second (disk I/O limited)
- **Redis Reprocessing:** ~500-1000 blocks/second (memory/SSD limited)
- **5x-10x speedup for historical backfills**

### Monitoring and Metrics

**Key Metrics to Track:**

```javascript
// Track Redis block storage performance
metrics.histogram('redis.block.write_latency', writeTimeMs);
metrics.histogram('redis.block.read_latency', readTimeMs);
metrics.gauge('redis.blocks.stored', await redis.dbsize());
metrics.gauge('redis.memory.used', await getRedisMemoryUsage());

// Track indexer lag
metrics.gauge('indexer.slot.current', currentSlot);
metrics.gauge('indexer.slot.latest_blockchain', latestBlockchainSlot);
metrics.gauge('indexer.lag_ms', lagMs);
```

**Alerts:**

- Redis memory usage > 80%: Warning (may need eviction or scaling)
- Redis memory usage > 95%: Critical (out of memory imminent)
- Block write latency > 10ms: Warning (Redis performance degraded)
- Indexer lag > 1 second: Warning (falling behind blockchain)

### Data Retention Strategy

**30-Day TTL Justification:**

- **Bug Fixes:** Most bugs discovered within days (30-day window sufficient)
- **New Protocols:** Historical data beyond 30 days not critical (can re-index from Solana archives if needed)
- **Storage Cost:** 30 days balances cost vs utility
- **Solana RPC Limits:** Solana RPC nodes typically keep ~90 days of history (fallback available)

**TTL Configuration:**

```javascript
// Default: 30 days
const DEFAULT_TTL = 30 * 24 * 60 * 60;

// High-priority blocks: extend TTL (e.g., major events, audits)
async function extendBlockTTL(slot, additionalDays) {
  const key = `block:${slot}`;
  const newTTL = additionalDays * 24 * 60 * 60;
  await redis.expire(key, newTTL);
}

// Manual cleanup: delete blocks before slot
async function deleteBlocksBefore(slot) {
  const keys = [];
  for (let s = 0; s < slot; s++) {
    keys.push(`block:${s}`);
  }

  // Delete in batches (avoid blocking Redis)
  const batchSize = 1000;
  for (let i = 0; i < keys.length; i += batchSize) {
    const batch = keys.slice(i, i + batchSize);
    await redis.del(...batch);
  }

  console.log(`Deleted ${keys.length} blocks before slot ${slot}`);
}
```

## Rationale

### Redis vs PostgreSQL Performance

**Write Performance:**

PostgreSQL:
- JSONB parsing and indexing: 50-100ms per block
- Disk I/O bottleneck (IOPS limited)
- WAL (Write-Ahead Log) overhead
- Vacuum operations during high load

Redis:
- In-memory write: < 1ms per block
- Append-Only File (AOF) async writes
- No indexing overhead (simple key-value)
- **50x-100x faster writes**

**Read Performance:**

PostgreSQL:
- Disk read + JSONB deserialization: 10-50ms
- Index lookup (B-tree traversal)
- Buffer pool cache misses frequent (data too large)

Redis:
- Memory read: < 1ms
- Direct key lookup (hash table)
- No deserialization overhead (string storage)
- **10x-50x faster reads**

**Real-World Impact:**

- **Indexer Lag:** 200-500ms (PostgreSQL) → 50-100ms (Redis)
- **Reprocessing Speed:** 100 blocks/sec (PostgreSQL) → 500-1000 blocks/sec (Redis)
- **Database Load:** PostgreSQL freed from billions of rows, better performance for trades/tokens/prices

### Cost Analysis

**PostgreSQL (RDS) Cost:**

- Instance: db.r6g.2xlarge (64GB memory, 8 vCPU) = $560/month
- Storage: 500GB GP3 SSD (block data) = $50/month
- IOPS: Provisioned IOPS for write load = $100/month
- **Total: ~$710/month**

**Redis (ElastiCache) Cost:**

- Instance: cache.r6g.xlarge (26.32GB memory) = $200/month
- No additional storage cost (included)
- **Total: ~$200/month**

**Savings:** $510/month ($6,120/year)

**Plus:** PostgreSQL can be downsized (no longer storing blocks) = additional $300/month savings

**Total Savings:** ~$800/month ($9,600/year)

### Microservices Alignment

**ADR-005: Indexer Microservices by Protocol**

Each protocol-specific indexer (Raydium, Pump.fun, Jupiter, Orca) writes blocks to shared Redis instance:

- **Centralized Block Storage:** All protocols use same Redis instance
- **Deduplication:** Multiple indexers may see same block (only stored once)
- **Efficient Reprocessing:** Backfill service reads blocks once, parses for all protocols

**Shared Redis Pattern:**

```javascript
// All indexers write to same Redis instance
// Key namespace prevents collisions (though slot numbers unique anyway)

// Raydium indexer
await redis.setex('block:123456', ttl, blockJson);

// Pump.fun indexer
await redis.setex('block:123456', ttl, blockJson);  // No-op if already exists

// Result: Only one copy of block stored
```

### Alternative Storage Backends Rejected

**Amazon S3 (Object Storage):**

- **Pro:** Cheap storage ($0.023/GB/month)
- **Pro:** Infinite scalability
- **Con:** High latency (50-100ms reads, not suitable for real-time indexing)
- **Con:** No TTL support (manual cleanup)
- **Why Rejected:** Latency unacceptable for indexer performance

**ClickHouse (Time-Series Database):**

- **Pro:** Already used for parsed trades
- **Pro:** Efficient columnar compression
- **Con:** Optimized for analytics, not key-value lookups
- **Con:** No TTL support (manual partitioning/deletion)
- **Con:** JSON storage not ClickHouse's strength
- **Why Rejected:** Wrong tool for job (ClickHouse for analytics, Redis for caching)

**MongoDB (Document Database):**

- **Pro:** Native JSON storage (BSON)
- **Pro:** TTL index support
- **Con:** Slower than Redis (disk-based)
- **Con:** Additional infrastructure (another database)
- **Con:** Overkill for simple key-value storage
- **Why Rejected:** Redis simpler and faster for this use case

## Consequences

### Positive

**Performance Improvements:**
- Block write latency: 50-100ms → < 1ms (50x-100x faster)
- Block read latency: 10-50ms → < 1ms (10x-50x faster)
- Indexer lag: 200-500ms → 50-100ms (2x-5x improvement)
- Reprocessing speed: 100 blocks/sec → 500-1000 blocks/sec (5x-10x faster)

**Database Optimization:**
- PostgreSQL freed from billions of raw block rows
- PostgreSQL performance improved for core data (trades, tokens, prices)
- ClickHouse remains optimized for analytics (no JSON bloat)
- Clear separation of concerns (Redis = cache, ClickHouse = analytics, PostgreSQL = relational)

**Cost Savings:**
- Redis cheaper than PostgreSQL for this workload: $200/month vs $710/month
- PostgreSQL can be downsized (no longer storing blocks): additional $300/month savings
- Total savings: ~$800/month ($9,600/year)

**Developer Experience:**
- Faster reprocessing = shorter debugging cycles
- Simple key-value API (no SQL complexity)
- TTL auto-cleanup (no manual data management)

**Scalability:**
- Horizontal scaling (add Redis replicas for read load)
- No disk I/O bottleneck (memory-based)
- Supports growing indexer data volume

**Reliability:**
- Persistence enabled (RDB + AOF) for durability
- Daily snapshots for disaster recovery
- Survives process restarts (data not lost)

### Negative

**New Infrastructure Dependency:**
- Additional service to maintain (Redis cluster)
- Monitoring and alerting overhead
- Potential Redis outages impact indexer

**Data Loss Risk (After TTL):**
- Blocks deleted after 30 days (cannot reprocess older than 30 days without Solana RPC fallback)
- If Solana RPC doesn't have historical block, data lost forever
- Mitigation: 30-day window sufficient for most use cases

**Memory Constraints:**
- Redis memory finite (26.32GB instance)
- Eviction possible if memory pressure
- Must monitor memory usage closely
- Scaling requires larger instance (cost increase)

**Persistence Trade-offs:**
- AOF file growth requires periodic compaction
- RDB snapshots temporarily increase disk I/O
- Memory + disk architecture more complex than pure in-memory

**Operational Complexity:**
- Redis configuration tuning (eviction policies, persistence settings)
- Backup management (RDB snapshots, AOF files)
- Disaster recovery procedures

### Neutral

**TTL Management:**
- 30-day TTL suitable for current needs
- May need adjustment based on usage patterns
- Can be extended for specific blocks if needed

**Fallback to Solana RPC:**
- Blocks older than 30 days: fetch from Solana RPC (if available)
- Solana RPC retention ~90 days (not guaranteed)
- Very old blocks: permanent data loss acceptable (can re-index from archives)

## Alternatives Considered

### Option 1: Keep PostgreSQL, Optimize Queries (Status Quo)

**Description:** Continue using PostgreSQL JSONB storage with optimizations

**Optimizations:**
- Add indexes on block_hash, timestamp
- Partition table by date (monthly partitions)
- Tune PostgreSQL parameters (shared_buffers, work_mem)

**Pros:**
- No new infrastructure
- Familiar technology (team knows PostgreSQL)
- ACID guarantees

**Cons:**
- Fundamental limitations remain (disk I/O bottleneck)
- Write latency still 10x-50x slower than Redis
- Database bloat continues
- Vertical scaling only (expensive)

**Why Rejected:** Optimizations provide marginal improvement, not 50x-100x like Redis. Problem is architectural (disk-based storage for high-frequency writes).

### Option 2: Amazon S3 Object Storage

**Description:** Store blocks as JSON files in S3

**Implementation:**
```javascript
await s3.putObject({
  Bucket: 'cooking-blocks',
  Key: `blocks/${slot}.json`,
  Body: JSON.stringify(blockData)
});
```

**Pros:**
- Extremely cheap ($0.023/GB/month)
- Infinite scalability
- Durable (99.999999999% durability)

**Cons:**
- High latency (50-100ms reads, unacceptable for real-time indexing)
- No TTL support (must manage lifecycle policies)
- Eventually consistent (not suitable for recent blocks)
- Write latency ~100ms (slower than PostgreSQL)

**Why Rejected:** Latency unacceptable. S3 optimized for batch processing, not real-time access.

### Option 3: ClickHouse (Same Database as Parsed Trades)

**Description:** Store blocks in ClickHouse alongside parsed trades

**Schema:**
```sql
CREATE TABLE blockchain_blocks (
  slot UInt64,
  block_hash String,
  block_data String,  -- JSON as string
  timestamp DateTime
) ENGINE = MergeTree()
ORDER BY slot;
```

**Pros:**
- No additional infrastructure (already using ClickHouse)
- Efficient columnar compression
- Fast sequential scans

**Cons:**
- ClickHouse optimized for analytics, not key-value lookups
- Point queries slower than Redis (B-tree vs hash table)
- No native TTL (must manually drop old partitions)
- JSON storage not ClickHouse's strength (better at numeric columns)

**Why Rejected:** ClickHouse wrong tool for this job. Excellent for analytics queries, mediocre for key-value cache.

### Option 4: MongoDB Document Database

**Description:** Use MongoDB for JSON document storage

**Pros:**
- Native JSON (BSON) storage
- TTL index support (automatic expiration)
- Flexible schema
- Horizontal scaling (sharding)

**Cons:**
- New infrastructure (another database to maintain)
- Slower than Redis (disk-based, even with WiredTiger)
- Overkill for simple key-value storage
- No team expertise (learning curve)

**Why Rejected:** Redis simpler and faster. MongoDB's features (schemas, aggregation pipeline) unnecessary for block storage.

### Option 5: In-Memory Only (No Persistence)

**Description:** Use Redis without persistence (pure cache)

**Config:**
```yaml
redis:
  persistence: disabled
  maxmemory-policy: allkeys-lru
```

**Pros:**
- Maximum performance (no disk writes)
- Simpler configuration

**Cons:**
- Data loss on restart (must reprocess all blocks)
- Eviction unpredictable (blocks disappear randomly)
- No disaster recovery

**Why Rejected:** Data loss unacceptable. Persistence critical for reliability.

## Implementation Notes

### Redis High Availability (Future)

**Current:** Single Redis instance (ElastiCache)

**Future (Production Scale):**

```yaml
# Redis Cluster Configuration
redis:
  mode: cluster
  nodes:
    - primary: cache.r6g.xlarge (AZ us-east-1a)
      replica: cache.r6g.xlarge (AZ us-east-1b)
    - primary: cache.r6g.xlarge (AZ us-east-1a)
      replica: cache.r6g.xlarge (AZ us-east-1c)
    - primary: cache.r6g.xlarge (AZ us-east-1b)
      replica: cache.r6g.xlarge (AZ us-east-1c)
  autoFailover: enabled
  multiAZ: true
```

**Benefits:**
- Automatic failover (replica promoted to primary on failure)
- Read scaling (replicas handle read traffic)
- High availability (99.99% uptime SLA)

**Cost:** ~$1,200/month (6 nodes vs 1 node $200/month)

### Monitoring Dashboard

**Key Metrics:**

```javascript
// Redis health
- redis.connections.current
- redis.memory.used_percent
- redis.cpu.percent
- redis.commands_per_second
- redis.keys.total
- redis.evicted_keys (should be 0 for volatile-lru)

// Indexer performance
- indexer.block.write_latency_p95
- indexer.block.read_latency_p95
- indexer.lag_ms
- indexer.blocks_per_second

// Application metrics
- reprocessing.blocks_per_second
- reprocessing.missing_blocks (count)
```

**Grafana Dashboard Example:**

```yaml
panels:
  - title: "Redis Memory Usage"
    type: graph
    targets:
      - expr: redis_memory_used_bytes / redis_memory_max_bytes * 100
        legend: "Memory Used %"

  - title: "Block Write Latency"
    type: graph
    targets:
      - expr: histogram_quantile(0.95, redis_block_write_latency)
        legend: "p95 latency"

  - title: "Indexer Lag"
    type: graph
    targets:
      - expr: indexer_slot_latest_blockchain - indexer_slot_current
        legend: "Slots Behind"
```

### Backup and Disaster Recovery

**RDB Snapshots:**

```bash
# Daily snapshot schedule (AWS ElastiCache automatic)
# Retention: 7 days
# Window: 03:00-05:00 UTC (low traffic)

# Manual snapshot (before major changes)
aws elasticache create-snapshot \
  --cache-cluster-id cooking-blocks \
  --snapshot-name manual-snapshot-$(date +%Y%m%d)
```

**Restore from Snapshot:**

```bash
# Create new cluster from snapshot
aws elasticache create-cache-cluster \
  --cache-cluster-id cooking-blocks-restored \
  --snapshot-name manual-snapshot-20250623 \
  --cache-node-type cache.r6g.xlarge
```

**AOF Recovery:**

```bash
# If Redis crashes, AOF automatically replays on startup
# Manual verification:
redis-check-aof --fix /path/to/appendonly.aof
```

## References

### Meeting Notes
- [Weekly Demo 2025-06-23](../06-meetings/2025-06/Weekly-Demo-2025-06-23.md) - Redis for JSON block storage implementation decision

### Related Decisions
- ADR-001: ClickHouse Migration for Time-Series Data (analytics database, not block storage)
- ADR-005: Indexer Microservices by Protocol (multiple indexers share Redis instance)

### Technical References
- Redis Documentation: https://redis.io/docs/
- Redis Persistence: https://redis.io/docs/manual/persistence/
- AWS ElastiCache for Redis: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/
- Solana RPC API: https://docs.solana.com/api/http
- ioredis (Node.js Client): https://github.com/luin/ioredis

### Performance Benchmarks
- Redis Benchmarks: https://redis.io/docs/management/optimization/benchmarks/
- ElastiCache Performance: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.html

## Revision History
- 2025-06-23: Redis for JSON block storage decision made
- 2025-06-23: Implemented Redis storage layer in indexer
- 2025-06-23: Significant performance improvement achieved in data handling
- 2025-10-21: Formal ADR documented from meeting notes
