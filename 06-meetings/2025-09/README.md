---
title: September 2025 - Meetings
type: index
date: 2025-10-21
summary: Index of Cooking.gg meeting notes from September 2025, covering TradingView integration, DevOps infrastructure, and indexer enhancements.
---

# September 2025 - Meetings

This directory contains structured meeting notes from Cooking.gg meetings during September 2025.

## Overview

**Period Covered:** September 2025
**Meeting Types:** Daily Standups, Technical Deep Dives
**Team:** Cooking.gg Development Team
**Language:** English (translated from Spanish)

## Files

### Technical Deep Dive Meetings (Batch 10)
- `2025-09-02-tradingview-integration.md` - TradingView charts integration technical planning
- `2025-09-04-devops-session-1.md` - Infrastructure & deployment setup
- `2025-09-04-devops-session-2.md` - Security & production readiness
- `2025-09-23-indexer-features.md` - Indexer enhancements and protocol expansion

### Daily Standups
- `2025-09-26-daily-standup.md` - Critical performance breakthrough, backend query optimization

## Major Themes

### TradingView Integration (Sept 2)
Professional-grade charting implementation:

- **Charting Library**: TradingView commercial license for full features
- **Data Feed Protocol**: UDF (Universal Data Feed) implementation
- **OHLCV Generation**: Pre-computed candles in ClickHouse materialized views
- **Real-Time Updates**: WebSocket for live candle updates
- **Trading from Chart**: Click to set orders, visual TP/SL levels
- **Timeframes**: 1m, 5m, 15m, 1h, 4h, 1d, 1w support

### DevOps Infrastructure (Sept 4)
Production environment preparation in two sessions:

**Session 1 - Infrastructure**:
- **AWS Architecture**: ECS, RDS PostgreSQL, ElastiCache Redis, S3, CloudFront
- **Deployment Pipeline**: GitHub Actions CI/CD with automated testing
- **Environment Strategy**: Dev (local), Staging (AWS), Production (multi-AZ)
- **Monitoring**: CloudWatch logs, metrics, alarms, SNS notifications
- **Auto-Scaling**: Target tracking on CPU, 2-10 tasks per service
- **Backup Strategy**: Daily database snapshots, 7-day retention

**Session 2 - Security**:
- **SSL/TLS**: ACM certificates with auto-renewal, TLS 1.2+ only
- **WAF & DDoS**: AWS WAF with managed rule sets, CloudFront Shield
- **Access Control**: IAM roles, MFA enforcement, least privilege principle
- **Encryption**: At rest (RDS, S3) and in transit (TLS), KMS for key management
- **Production Checklist**: Security audit, load testing, incident response plan

### Indexer Evolution (Sept 23)
Architecture enhancements and protocol expansion:

- **Microindexers**: Protocol-specific indexers (Radium, Pump.fun, etc.)
- **Event Queue**: Kafka/RabbitMQ for buffering and reprocessing
- **Multi-RPC Support**: Multiple providers for redundancy
- **Protocol Coverage**: Add Radium CPMM, CLMM, Moonshot, Pump.swap
- **ClickHouse Optimization**: Materialized views, partition tuning, projections
- **Historical Backfill**: Separate service for indexing past data

### Performance Breakthrough (Sept 26)
Dramatic performance improvement resolving critical bottleneck:

- **Loading Time**: 30-60 seconds → 1-2 seconds (near-instantaneous)
- **Root Cause**: Crons coupled with backend queries causing contention
- **Solution**: Decoupled crons, increased priority (2 cores per replica)
- **Impact**: Kitchen could stream overnight without crashing

## Technical Highlights

### TradingView Integration
**Data Feed Architecture**:
- `/config` - Chart configuration
- `/symbols` - Symbol search
- `/history` - Historical OHLCV data
- `/subscribeBars` - Real-time updates via WebSocket

**OHLCV Pre-Computation**:
```sql
CREATE MATERIALIZED VIEW ohlcv_1m AS
SELECT token_address, toStartOfMinute(timestamp) AS time,
       argMin(price, timestamp) AS open, max(price) AS high,
       min(price) AS low, argMax(price, timestamp) AS close,
       sum(volume) AS volume
FROM trades GROUP BY token_address, time;
```

### DevOps Architecture
**AWS Services Stack**:
- ECS for container orchestration
- Multi-AZ RDS PostgreSQL with read replicas
- ElastiCache Redis for caching
- S3 + CloudFront for CDN
- Route 53 for DNS

**Security Layers**:
- WAF for web application firewall
- AWS Secrets Manager for credential management
- CloudWatch for monitoring and alerting
- IAM roles for service accounts

### Indexer Enhancements
**Proposed Architecture**:
- Protocol-specific microindexers
- Kafka event queue for reliability
- Multi-RPC connections for redundancy
- Historical backfill service

**ClickHouse Optimizations**:
- Materialized views for aggregations
- Partition by (token_address, date)
- Projections for common query patterns
- SAMPLE clause for approximations

## Key Decisions

### Technical Architecture
- **Decision**: TradingView Charting Library over Lightweight Charts - Professional features justify cost
- **Decision**: ECS over EKS - Simpler ops, faster to production
- **Decision**: Multi-AZ deployment - High availability at reasonable cost
- **Decision**: CloudWatch over third-party monitoring - Cost-effective, native integration
- **Decision**: Microindexers per protocol - Isolation of failures, easier maintenance

### Data & Performance
- **Decision**: Pre-compute OHLCV in ClickHouse - Much faster than on-demand
- **Decision**: WebSocket for real-time candles - Low latency, efficient
- **Decision**: Materialized views for aggregations - Dramatic query performance improvement
- **Decision**: Kafka for event buffering - No data loss, reprocessing capability

## Critical Issues & Solutions

### Performance Crisis (Sept 26)
- **Issue**: 30-60 second page load times, crashes
- **Solution**: Decouple crons from backend queries
- **Result**: 1-2 second loads, stable overnight operation

### TradingView Data Feed
- **Challenge**: Real-time OHLCV updates
- **Solution**: Materialized views + WebSocket pub/sub
- **Result**: < 500ms latency from trade to chart

### Security Hardening
- **Challenge**: Production security requirements
- **Solution**: Multi-layer security (WAF, encryption, IAM, Secrets Manager)
- **Result**: Production-ready secure infrastructure

### Protocol Coverage Gaps
- **Challenge**: Missing trades from new Radium routing
- **Solution**: Plan microindexers for CPMM, CLMM contracts
- **Future**: Gradual protocol expansion based on volume

## Action Items Carried Forward

### TradingView
- [ ] Obtain commercial license
- [ ] Implement UDF API endpoints
- [ ] Build OHLCV materialized views
- [ ] Implement WebSocket real-time updates

### DevOps
- [ ] Complete load testing
- [ ] Finalize security audit
- [ ] Document runbooks and DR procedures
- [ ] Set up on-call rotation

### Indexer
- [ ] Design Kafka topic schema
- [ ] Implement Radium CPMM/CLMM parsers
- [ ] Build historical backfill service
- [ ] Create data quality monitoring

## Meeting Attendance

**Technical Deep Dives:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Marcos Tacca

**Daily Standups:** Full Cooking.gg development team

---

**Note:** These meetings were originally conducted in Spanish and have been translated to English while preserving technical terminology.
