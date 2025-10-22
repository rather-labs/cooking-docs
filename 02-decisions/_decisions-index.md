---
title: Decision Records Index
type: index
date: 2025-10-17
last-updated: 2025-10-21
status: active
summary: |
  Comprehensive index of all architectural and significant project decisions
  including their current status and relationships. Updated with all 30 ADRs
  (29 accepted + 1 proposed) from May-October 2025 covering the beta launch journey.
---

# Decision Records Index

This directory contains all significant project decisions documented using the Architecture Decision Record (ADR) format.

## Quick Links
- [Decision Template](_template-decision.md) - Use this to create new decisions
- [How to Create Decisions](README.md) - Guidelines for documenting decisions

## Decision Status Guide
- **Proposed:** Under consideration, not yet approved
- **Accepted:** Approved and should be implemented
- **Rejected:** Considered but not approved
- **Superseded:** Replaced by a newer decision
- **Deprecated:** No longer recommended but not fully replaced

---

## Active Decisions

### Architecture Decisions (001-099)

| ID | Title | Date | Status | Owner |
|----|-------|------|--------|-------|
| ADR-001 | [ClickHouse Migration for Time-Series Data](2025-06-27-clickhouse-time-series-data.md) | 2025-06-27 | Accepted | Eduardo Bellani |
| ADR-002 | [Microservices Architecture by Trading Algorithm](2025-09-26-microservices-by-algorithm.md) | 2025-09-26 | Accepted | Marcos Tacca, Martin Lecam |
| ADR-003 | [WebSocket to SSE Migration for Real-Time Updates](2025-08-27-websocket-to-sse-migration.md) | 2025-08-27 | Accepted | Eduardo Bellani, Byron Chavarria |
| ADR-004 | [Hybrid Filtering Architecture (Server + Client)](2025-07-24-hybrid-filtering-architecture.md) | 2025-07-24 | Accepted | Ali Jafarbeglou, Marko Jauregui |
| ADR-005 | [Indexer Microservices by Protocol](2025-09-23-indexer-microservices-protocol.md) | 2025-09-23 | Accepted | Eduardo Bellani |

### Technical Implementation Decisions (100-199)

| ID | Title | Date | Status | Owner |
|----|-------|------|--------|-------|
| ADR-100 | [Jupiter as Primary Router (Rejecting Echo)](2025-10-15-jupiter-primary-router.md) | 2025-10-15 | Accepted | Eduardo Bellani, Byron Chavarria |
| ADR-101 | [TradingView Charting Library Integration](2025-09-02-tradingview-charting-library.md) | 2025-09-02 | Accepted | Ali Jafarbeglou, Eduardo Bellani |
| ADR-102 | [Auth0 for Social Authentication](2025-08-auth0-social-authentication.md) | 2025-08-01 | Accepted | Martin Lecam, Byron Chavarria |
| ADR-103 | [Type-Safe API Client Generation](2025-10-10-type-safe-api-client-generation.md) | 2025-10-10 | Accepted | Marko Jauregui, Martin Lecam |
| ADR-104 | [Redis for JSON Block Storage](2025-06-23-redis-json-block-storage.md) | 2025-06-23 | Accepted | Eduardo Bellani |
| ADR-105 | [Transaction Security Validation Pattern](2025-10-10-transaction-security-validation.md) | 2025-10-10 | Accepted | Martin Aranda |
| ADR-106 | [Jupiter Transaction Optimization Strategy](2025-10-16-jupiter-transaction-optimization.md) | 2025-10-16 | Accepted | Martin Aranda |

### Business and Product Decisions (200-299)

| ID | Title | Date | Status | Owner |
|----|-------|------|--------|-------|
| ADR-200 | [Multilevel Referral Program Structure](2025-08-13-multilevel-referral-program.md) | 2025-08-13 | Accepted | Lucas Cufré, Martin Aranda |
| ADR-201 | [Closed Beta via Referral-Only Access](2025-08-11-closed-beta-referral-only-access.md) | 2025-08-11 | Accepted | Lucas Cufré |
| ADR-202 | [Zero Bridge Fees Strategic Decision](2025-08-20-zero-bridge-fees-strategic-decision.md) | 2025-08-20 | Accepted | Lucas Cufré |
| ADR-203 | [September Beta Launch Timeline](2025-08-11-september-beta-launch-timeline.md) | 2025-08-11 | Accepted | Lucas Cufré |

### Process and Operational Decisions (300-399)

| ID | Title | Date | Status | Owner |
|----|-------|------|--------|-------|
| ADR-300 | [AWS ECS over EKS for Container Orchestration](2025-09-04-aws-ecs-over-eks-container-orchestration.md) | 2025-09-04 | Accepted | Martin Aranda |
| ADR-301 | [Weekly Sprint Calls with Client](2025-08-11-weekly-sprint-calls-with-client.md) | 2025-08-11 | Accepted | Lucas Cufré |
| ADR-302 | [Feature Freeze for Stability](2025-08-11-feature-freeze-for-stability.md) | 2025-08-11 | Accepted | Lucas Cufré |
| ADR-303 | [Working Guards On-Call Rotation for Beta Support](2025-10-20-working-guards-on-call-rotation.md) | 2025-10-20 | Proposed | Lucas Cufré |

### Security and Compliance Decisions (400-499)

| ID | Title | Date | Status | Owner |
|----|-------|------|--------|-------|
| ADR-400 | [Security Password for Wallet Operations](2025-06-06-security-password-wallet.md) | 2025-06-06 | Accepted | Martin Lecam, Marko Jauregui |
| ADR-401 | [Biometric Authentication Required for Mobile Trading](2025-10-01-biometric-authentication-mobile.md) | 2025-10-01 | Accepted | Martin Aranda, Mobile Team |
| ADR-402 | [AWS WAF and Encryption Strategy](2025-09-04-aws-waf-encryption-strategy.md) | 2025-09-04 | Accepted | Martin Lecam, Marcos Tacca |

### Infrastructure and DevOps Decisions (500-599)

| ID | Title | Date | Status | Owner |
|----|-------|------|--------|-------|
| ADR-500 | [Multi-AZ Deployment for High Availability](2025-09-04-multi-az-deployment-high-availability.md) | 2025-09-04 | Accepted | Lucas Cufré |
| ADR-501 | [Turnkey for Wallet Management](2025-07-04-turnkey-wallet-management.md) | 2025-07-04 | Accepted | Byron Chavarria |
| ADR-502 | [ClickHouse Two-Client Architecture](2025-10-06-clickhouse-two-client-architecture.md) | 2025-10-06 | Accepted | Darío Balmaceda |

---

## Legacy Decisions (Pre-Categorization System)

**Note:** This decision predates the current categorization system (001-599) and uses the original ADR-001 identifier.

| ID | Title | Date | Status | Owner | Notes |
|----|-------|------|--------|-------|-------|
| ADR-001 (Legacy) | [Use Telegram for User Authentication](2024-10-03-telegram-authentication.md) | 2024-10-03 | Superseded | Project Lead | Replaced by ADR-102 (Auth0 Social Authentication) |

**Current ADR-001:** [ClickHouse Migration for Time-Series Data](2025-06-27-clickhouse-time-series-data.md) (2025-06-27)

---

## Recent Decisions (October 2025)

| ID | Title | Date | Impact |
|----|-------|------|--------|
| ADR-303 | Working Guards On-Call Rotation (Proposed) | 2025-10-20 | High - 24/7 beta support coverage |
| ADR-106 | Jupiter Transaction Optimization Strategy | 2025-10-16 | High - 50% faster transactions (5-6s → 2-3s) |
| ADR-100 | Jupiter as Primary Router (Rejecting Echo) | 2025-10-15 | High - Rejected client request |
| ADR-105 | Transaction Security Validation Pattern | 2025-10-10 | Critical - Security layer for external routers |
| ADR-103 | Type-Safe API Client Generation | 2025-10-10 | Medium - Code quality improvement |
| ADR-502 | ClickHouse Two-Client Architecture | 2025-10-06 | Critical - Performance crisis resolution |
| ADR-401 | Biometric Authentication for Mobile | 2025-10-01 | High - Mobile security enhancement |

---

## Rejected Decisions

| ID | Title | Date Rejected | Reason |
|----|-------|--------------|--------|
| Echo Router | Alternative to Jupiter for Solana swaps | 2025-10-15 | Technical incompatibility, performance issues (See ADR-100) |

---

## Decision Relationships

### Critical Decision Chain for October 17 Beta Launch

```
ADR-203 (Beta Launch Timeline)
    ├── ADR-201 (Closed Beta Referral-Only)
    │       └── ADR-200 (Multilevel Referral Program)
    ├── ADR-001 (ClickHouse Migration)
    │       └── ADR-502 (Two-Client Architecture)
    ├── ADR-102 (Auth0 Social Login)
    │       ├── ADR-501 (Turnkey Wallet)
    │       └── ADR-400 (Security Password)
    │               └── ADR-401 (Biometric Auth Mobile)
    ├── ADR-302 (Feature Freeze)
    └── ADR-300 (AWS ECS Deployment)
            └── ADR-500 (Multi-AZ Deployment)
                    └── ADR-402 (WAF & Encryption)
```

### Architecture Evolution Chain

```
ADR-001 (ClickHouse) → Performance Foundation
    ├── ADR-502 (Two-Client) → Query Prioritization
    └── ADR-101 (TradingView) → Real-time Charts

ADR-003 (SSE Migration) → Real-time Updates
    └── ADR-002 (Microservices by Algorithm) → Scalable Architecture
            └── ADR-005 (Indexer by Protocol) → Data Processing
```

### User Experience Chain

```
ADR-102 (Auth0) → Social Login
    └── ADR-501 (Turnkey) → Wallet Creation
            ├── ADR-400 (Security Password) → Wallet Protection
            └── ADR-401 (Biometric Auth) → Mobile Security

ADR-200 (Multilevel Referral) → Growth Mechanism
    └── ADR-201 (Closed Beta) → Controlled Launch
```

---

## Decisions by Theme

### Performance & Scalability
- [ADR-001: ClickHouse Migration](2025-06-27-clickhouse-time-series-data.md) - 15x query improvement
- [ADR-502: Two-Client Architecture](2025-10-06-clickhouse-two-client-architecture.md) - Performance crisis resolution
- [ADR-104: Redis for JSON Block Storage](2025-06-23-redis-json-block-storage.md) - 50x-100x write improvement
- [ADR-003: SSE Migration](2025-08-27-websocket-to-sse-migration.md) - Real-time scalability

### Security
- [ADR-400: Security Password](2025-06-06-security-password-wallet.md) - Wallet operations protection
- [ADR-401: Biometric Authentication](2025-10-01-biometric-authentication-mobile.md) - Mobile trading security
- [ADR-402: AWS WAF and Encryption](2025-09-04-aws-waf-encryption-strategy.md) - Infrastructure security
- [ADR-102: Auth0](2025-08-auth0-social-authentication.md) - Social login security

### User Experience
- [ADR-102: Auth0](2025-08-auth0-social-authentication.md) - Seamless social login (95% completion)
- [ADR-501: Turnkey](2025-07-04-turnkey-wallet-management.md) - No seed phrase onboarding
- [ADR-101: TradingView](2025-09-02-tradingview-charting-library.md) - Professional charting
- [ADR-004: Hybrid Filtering](2025-07-24-hybrid-filtering-architecture.md) - Fast token filtering

### Business Strategy
- [ADR-200: Multilevel Referral](2025-08-13-multilevel-referral-program.md) - Viral growth mechanism
- [ADR-201: Closed Beta](2025-08-11-closed-beta-referral-only-access.md) - Controlled launch strategy
- [ADR-202: Zero Bridge Fees](2025-08-20-zero-bridge-fees-strategic-decision.md) - Competitive positioning
- [ADR-203: Beta Timeline](2025-08-11-september-beta-launch-timeline.md) - Commitment to delivery

### Infrastructure
- [ADR-300: AWS ECS](2025-09-04-aws-ecs-over-eks-container-orchestration.md) - Simplified orchestration
- [ADR-500: Multi-AZ](2025-09-04-multi-az-deployment-high-availability.md) - 99.9% uptime
- [ADR-005: Indexer Microservices](2025-09-23-indexer-microservices-protocol.md) - Protocol-specific processing

### Technical Implementation
- [ADR-100: Jupiter Router](2025-10-15-jupiter-primary-router.md) - Swap aggregation
- [ADR-103: Type-Safe API](2025-10-10-type-safe-api-client-generation.md) - Code quality
- [ADR-002: Microservices](2025-09-26-microservices-by-algorithm.md) - Trading algorithm separation

---

## Decision Statistics

**Total Decisions:** 28 (27 active + 1 superseded legacy)
**Active (Accepted):** 27
**Proposed:** 0
**Superseded:** 1 (Legacy ADR-001 Telegram Auth)
**Rejected:** 1 (Echo Router - documented in ADR-100)

**By Category:**
- Architecture (001-099): 5 decisions
- Technical (100-199): 5 decisions
- Business (200-299): 4 decisions
- Process (300-399): 3 decisions
- Security (400-499): 3 decisions
- Infrastructure (500-599): 3 decisions
- Legacy (pre-categorization): 1 decision (superseded)

**Decision Timeline:**
- May 2025: 0 decisions
- June 2025: 3 decisions (ADR-001, ADR-400, ADR-104)
- July 2025: 2 decisions (ADR-004, ADR-501)
- August 2025: 6 decisions (ADR-003, ADR-102, ADR-200, ADR-201, ADR-202, ADR-203)
- September 2025: 5 decisions (ADR-002, ADR-005, ADR-101, ADR-300, ADR-402, ADR-500)
- October 2025: 5 decisions (ADR-401, ADR-502, ADR-100, ADR-103, ADR-301, ADR-302)

**Last Updated:** 2025-10-21

---

## Decision ID Allocation

### ID Ranges by Category
- **001-099:** Architecture decisions (Next: ADR-006)
- **100-199:** Technical implementation decisions (Next: ADR-105)
- **200-299:** Business and product decisions (Next: ADR-204)
- **300-399:** Process and operational decisions (Next: ADR-303)
- **400-499:** Security and compliance decisions (Next: ADR-403)
- **500-599:** Infrastructure and DevOps decisions (Next: ADR-503)

### Category Usage
- Architecture: 5/99 (5% utilized)
- Technical: 5/100 (5% utilized)
- Business: 4/100 (4% utilized)
- Process: 3/100 (3% utilized)
- Security: 3/100 (3% utilized)
- Infrastructure: 3/100 (3% utilized)

---

## Key Milestones

### June 2025 - Performance Foundation
- ClickHouse migration initiated (ADR-001)
- Security password implementation (ADR-400)
- Redis block storage optimization (ADR-104)

### July-August 2025 - Growth & Authentication
- Auth0 social login (ADR-102)
- Turnkey wallet integration (ADR-501)
- Multilevel referral program design (ADR-200)
- Closed beta strategy (ADR-201)
- Feature freeze commitment (ADR-302)

### September 2025 - Production Readiness
- Microservices architecture (ADR-002)
- AWS ECS deployment (ADR-300)
- Multi-AZ high availability (ADR-500)
- TradingView integration (ADR-101)
- AWS WAF security (ADR-402)

### October 2025 - Launch & Optimization
- Biometric authentication (ADR-401)
- ClickHouse two-client fix (ADR-502)
- Jupiter router finalized (ADR-100)
- Type-safe API implementation (ADR-103)
- **October 17: Successful Beta Launch** 🚀

---

## Maintenance

**Review Frequency:** Monthly
**Owner:** Lucas Cufré, Technical Leads
**Last Review:** 2025-10-21
**Next Review:** 2025-11-21

### Monthly Maintenance Checklist
- [x] Review decision statuses
- [x] Update statistics
- [x] Check for decisions that should be superseded
- [x] Verify all links work
- [x] Update recent decisions list
- [ ] Archive old superseded/rejected decisions (none yet)

---

## References

**Related Documents:**
- [Project Charter](../01-foundation/project-charter.md)
- [Current Status](../03-active-work/_current-status.md)
- [Meeting Notes](../06-meetings/)
- [Requirements](../04-knowledge-base/business/requirements/)
- [Knowledge Base Update Tracker](../Knowledge_base_update_tracker.md)

**Key Outcomes:**
- **Performance:** 15x query improvement, 3-second transactions
- **Security:** Multi-layered authentication (Auth0, Security Password, Biometrics)
- **Growth:** Multilevel referral program with 30-55% commissions
- **Stability:** 99.9% uptime, Multi-AZ deployment
- **Launch:** October 17, 2025 - Successful closed beta deployment

---

*This index reflects the complete decision history from May-October 2025 covering the journey to successful beta launch.*
