---
title: ClickHouse Migration for Time-Series Data
type: decision-record
decision-id: ADR-001
date: 2025-06-27
status: accepted
owner: RatherLabs Development Team
stakeholders: [Eduardo Yuschuk, Darío Balmaceda, Lucas Cufré, Martin Aranda, Cooking Team]
tags: [architecture, database, performance, clickhouse, time-series, indexer]
summary: |
  Decision to migrate from traditional relational databases to ClickHouse, a columnar database optimized for analytical queries, to dramatically improve query performance for time-series trading data, token details, positions, and OHLCV data. This migration resolved critical performance bottlenecks and enabled real-time position updates at scale.
related-docs:
  - ../06-meetings/2025-06/Weekly-Demo-2025-06-27.md
  - ../06-meetings/2025-10/2025-10-06-daily-standup.md
  - ../06-meetings/2025-10/2025-10-17-cooking-demo.md
---

# ClickHouse Migration for Time-Series Data

## Context and Problem Statement

Cooking.gg is a high-frequency trading platform processing massive volumes of time-series data including token prices, trading positions, transaction history, and OHLCV (Open/High/Low/Close/Volume) data for charting. As the platform scaled, traditional relational databases became a critical bottleneck:

- Query times reaching 30-60 seconds for position updates
- Transaction history queries taking 12-14 seconds
- Database instances becoming saturated during high-load periods
- Up to 1,000+ pending queries accumulating, making the system unresponsive
- Poor performance for analytical queries on large datasets
- Position updates lagging behind actual transaction completion, degrading user experience

The platform requires sub-second query performance for:
- Real-time position updates after trades
- Historical transaction data retrieval
- Token price feeds and charts (Bars/OHLCV data)
- Token details and metadata
- User portfolio displays

## Decision

**Migrate to ClickHouse as the primary database for time-series and analytical data**, replacing traditional relational databases for the Indexer Provider. ClickHouse is a columnar database specifically optimized for analytical queries and time-series data.

**Scope of Migration:**
- **Bars** (OHLCV data for charts and last traded prices)
- **Token Details** (token metadata and information)
- **Positions** (user trading positions)
- **Transaction History**
- **Portfolio queries**

**Implementation approach:**
1. Deploy ClickHouse on RatherLabs internal account for testing (June 2025)
2. Enable ClickHouse on Cooking AWS environment
3. Migrate data tables to new Indexer Provider
4. Optimize with materialized views and projections
5. Deploy two-client architecture for different workload priorities

## Rationale

### Performance Requirements
- Trading platform users expect real-time updates (sub-second latency)
- Analytical queries on time-series data are read-heavy
- Data volume grows continuously with every trade on Solana blockchain
- Traditional row-based databases are optimized for transactional (write) workloads, not analytical (read) workloads

### ClickHouse Advantages for This Use Case
1. **Columnar storage**: Optimized for reading specific columns across large datasets
2. **Time-series optimization**: Built specifically for time-series data patterns
3. **Compression**: Reduces storage costs and improves query speed
4. **Analytical query performance**: Designed for aggregations, filtering, and analytics
5. **Horizontal scalability**: Can handle growing data volumes
6. **Real-time data ingestion**: Supports continuous data streaming from indexers

### Proven Results
- **15x query performance improvement** (30-60 seconds → 1-2 seconds)
- Position updates now real-time (matching user expectations)
- Transaction history queries matching active positions speed
- System stability dramatically improved
- Production performance matching development environment expectations

## Consequences

### Positive
- **Dramatic performance improvement**: Queries reduced from 12-14 seconds to sub-second
- **Real-time user experience**: Position updates now instantaneous after transaction confirmation
- **Scalability**: System can handle growing data volumes without degradation
- **Cost efficiency**: Better resource utilization, higher query throughput per instance
- **Data compression**: Reduced storage costs for massive time-series datasets
- **Stability**: Eliminated query queue saturation issues
- **99% cache hit rate**: Gigabytes of RAM efficiently utilized for hot data
- **Platform competitiveness**: Performance now matches user expectations for trading platform

### Negative
- **New technology adoption**: Team required learning ClickHouse-specific optimization techniques
- **Migration complexity**: Required careful planning and testing before production deployment
- **Specialized expertise**: Darío Balmaceda became critical knowledge holder (single point of dependency)
- **Query optimization learning curve**: Different patterns than relational databases (projections, materialized views)
- **Initial performance crisis**: Merge processes initially saturated instances before optimization
- **Data loss during recovery**: Backup recovery resulted in information gap during crisis resolution
- **Elevated resource usage**: CPU at 16-17 (vs. previous 8) though stable and manageable

### Neutral
- Additional database technology in stack (increased operational complexity)
- Two-client architecture required for workload separation (API vs. cron jobs)
- Requires monitoring different metrics than traditional databases
- ClickHouse-specific SQL dialect differences from PostgreSQL/MySQL

## Alternatives Considered

### Option 1: Optimize Existing Relational Database
**Description:** Tune PostgreSQL/MySQL with better indexes, partitioning, and caching

**Pros:**
- No technology change required
- Team already familiar with relational databases
- No migration effort needed
- Standard operational procedures

**Cons:**
- Relational databases fundamentally optimized for different workload (OLTP not OLAP)
- Indexing overhead increases write latency
- Partitioning helps but doesn't solve columnar query inefficiency
- Would only delay the problem as data grows
- Cache warming strategies complex for time-series data

**Why Rejected:** Fundamental architecture mismatch. Row-based storage is inefficient for analytical queries on time-series data. Would not achieve required performance levels.

### Option 2: TimescaleDB (PostgreSQL Extension)
**Description:** Use TimescaleDB, a time-series extension for PostgreSQL

**Pros:**
- PostgreSQL compatibility (familiar SQL)
- Time-series optimizations built-in
- Easier learning curve than ClickHouse
- Hybrid OLTP/OLAP capabilities

**Cons:**
- Performance not as optimized as pure columnar databases
- Still row-based storage underneath
- Scaling limitations compared to ClickHouse
- Not as mature for high-throughput analytical workloads

**Why Rejected:** While better than standard PostgreSQL, ClickHouse offers superior performance for pure analytical workloads. The platform doesn't need strong OLTP capabilities in the analytical layer.

### Option 3: Amazon Timestream
**Description:** AWS managed time-series database service

**Pros:**
- Fully managed (reduced operational burden)
- Built for time-series data
- Automatic scaling
- AWS integration

**Cons:**
- Vendor lock-in to AWS
- Higher cost than self-managed ClickHouse
- Less control over optimization
- Query performance not as strong as ClickHouse for this use case
- Limited customization for specific workload patterns

**Why Rejected:** Higher cost, vendor lock-in, and less performance control. Team capable of managing ClickHouse with appropriate expertise.

## Implementation Notes

### Deployment Architecture
1. **Two-Client Configuration** (ADR-502):
   - **API Client**: Higher priority, more CPU allocation for user-facing queries
   - **Cron Jobs Client**: Lower priority, less CPU for background analytics
   - Prevents background jobs from saturating resources needed for user queries

### Performance Optimization Techniques
1. **Projections**: Created optimized data projections with correct ordering
   - Reduced rows read by factor of 10
   - Dramatic improvement in portfolio and holder queries
2. **Materialized Views**: Pre-computed aggregations for common queries
3. **Merge Process Management**: Configured to prevent resource saturation
   - Initial crisis: three instances simultaneously merging, saturating resources
   - Solution: Optimized merge scheduling and resource allocation
4. **Concurrency Control**: Requires careful CPU cycle allocation for query scheduling
   - Queries can get stuck when merges saturate system without proper configuration

### Critical Success Factors
- **Darío Balmaceda's expertise**: Critical for resolving performance crisis and optimization
- **Thorough testing**: RatherLabs internal environment before production deployment
- **Phased migration**: Migrated tables incrementally (Bars → Token Details → Positions)
- **Monitoring**: CPU and query performance metrics essential for optimization
- **Documentation**: Persisting ClickHouse configuration changes to repository

### Migration Timeline
- **June 27, 2025**: Decision made, integration completed on RatherLabs internal account
- **June-September 2025**: Incremental table migration and optimization
- **October 6, 2025**: Performance crisis resolved with projection optimization
- **October 17, 2025**: Production deployment successful, position lag eliminated

## References

### Meeting Notes
- [Weekly Demo 2025-06-27](../06-meetings/2025-06/Weekly-Demo-2025-06-27.md) - Initial migration decision and testing
- [Daily Standup 2025-10-06](../06-meetings/2025-10/2025-10-06-daily-standup.md) - Performance crisis resolution
- [Cooking Demo 2025-10-17](../06-meetings/2025-10/2025-10-17-cooking-demo.md) - Production deployment success

### Related Decisions
- ADR-502: ClickHouse Two-Client Architecture

### External Resources
- ClickHouse Documentation: https://clickhouse.com/docs
- ClickHouse for Time-Series Data: https://clickhouse.com/docs/en/guides/developer/time-series
- Materialized Views: https://clickhouse.com/docs/en/guides/developer/cascading-materialized-views
- Projections: https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree#projections

## Revision History
- 2025-06-27: Initial decision to migrate to ClickHouse
- 2025-10-06: Performance optimization with projections
- 2025-10-17: Production deployment completed
- 2025-10-21: Formal ADR documented from meeting notes
