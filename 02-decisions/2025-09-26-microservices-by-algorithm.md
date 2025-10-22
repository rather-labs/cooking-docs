---
title: Microservices Architecture by Trading Algorithm
type: decision-record
decision-id: ADR-002
date: 2025-09-26
status: accepted
owner: Lucas Cufré, Martin Aranda
stakeholders: [Lucas Cufré, Martin Aranda, Esteban Restrepo, Federico Caffaro, Eduardo Yuschuk, Cooking Team]
tags: [architecture, microservices, scalability, backend, trading-algorithms]
summary: |
  Decision to organize backend microservices by trading algorithm type (DCA, limit orders, perpetuals, etc.) while centralizing transaction execution logic. Frontend will communicate directly with microservices without an API gateway intermediary, choosing simplicity over complexity to accelerate delivery before beta launch.
related-docs:
  - ../06-meetings/2025-09/2025-09-26-daily-standup.md
  - ../06-meetings/2025-09/2025-09-15-bug-alignment.md
---

# Microservices Architecture by Trading Algorithm

## Context and Problem Statement

As Cooking.gg approached its October 2025 beta launch with real users requiring 24/7 operations, the team needed to establish a scalable, maintainable backend architecture that could:

1. **Handle Multiple Trading Algorithms**: Support diverse trading strategies (DCA, TWAP, VWAP, limit orders, perpetuals, market orders)
2. **Scale Horizontally**: Accommodate growth from 2,000 to potentially 200,000 users
3. **Maintain Code Quality**: Reduce code duplication while keeping services focused
4. **Enable Rapid Development**: Allow parallel development on different trading features
5. **Support High Transaction Volumes**: Process thousands of concurrent trades efficiently
6. **Simplify Frontend Integration**: Provide clear, reliable API contracts

**Key Challenges:**
- Complex transaction lifecycle management (signature generation, retry logic, confirmation polling)
- Need for horizontal scaling to handle variable user loads
- Event-driven architecture requirements for asynchronous transaction processing
- Balance between service isolation and code reuse
- Time pressure: decision made 3 weeks before beta launch

**Alternative Architectural Patterns Considered:**
- Monolithic backend with all trading logic centralized
- Single microservice with routing logic for different algorithms
- API Gateway pattern with service mesh
- Algorithm-specific microservices with direct frontend communication

## Decision

**Implement microservices architecture organized by trading algorithm type, with a unified transaction execution layer, and direct frontend-to-microservice communication without an API gateway.**

### Architecture Components

**Algorithm-Specific Microservices:**
- **DCA Service**: Dollar-cost averaging algorithm implementation
- **Limit Orders Service**: Take profit (TP) and stop loss (SL) order management
- **Perpetuals Service**: Hyper Liquid perpetuals trading integration
- **Market Orders Service**: Immediate execution spot trading
- **TWAP Service**: Time-weighted average price algorithm
- **VWAP Service**: Volume-weighted average price algorithm

Each service handles:
- Algorithm-specific business logic
- Order validation and scheduling
- Algorithm parameter management
- Status tracking for algorithm-specific operations

**Unified Transaction Execution Layer:**
- Centralized transaction microservice (6000+ lines of code)
- Event-driven architecture using RabbitMQ
- Handles transaction construction, signing, submission, and confirmation
- Automatic retry logic with signature regeneration on blockhash failures
- Confirmation worker polling RPC to verify finalized transactions
- Shared by all algorithm-specific services to eliminate code duplication

**Frontend Integration:**
- **No API Gateway**: Frontend has direct knowledge of all microservices
- Direct HTTP/REST communication with each service
- Polling-based transaction status updates using internal transaction IDs
- Simpler architecture chosen to accelerate delivery

### Scalability Design

**Horizontal Scaling:**
- Each microservice can scale independently based on load
- Transaction service designed for horizontal scaling (stateless processing)
- RabbitMQ message queue enables distributed transaction processing
- Connection pool optimization: 2 cores per replica dedicated to query processing

**Performance Optimizations:**
- Cron jobs decoupled from main backend queries
- Higher priority assigned to query connection pools
- Achieved loading time improvement from 30-60 seconds to near-instantaneous

## Rationale

### Scalability Argument (Esteban Restrepo)

**Core Insight:** "The current microservices architecture by trading algorithms is scalable."

**Reasoning:**
- Each trading algorithm has distinct business logic and lifecycle requirements
- Algorithm-specific services can scale independently based on usage patterns
- If DCA becomes popular, scale DCA service without affecting limit orders
- Isolation prevents cascading failures between different trading strategies
- Clear service boundaries enable parallel team development

### Code Reuse Through Centralization

**Transaction Layer Unification:**
- Eliminates duplicate transaction handling code across services
- Single source of truth for Solana transaction lifecycle
- Consistent retry and confirmation logic
- Reduces maintenance burden and bug surface area
- Enables transaction monitoring and analytics in one place

**Benefits:**
- 6000+ lines of transaction code maintained once, used by all algorithms
- Automatic signature regeneration on failures applied universally
- RabbitMQ event-driven architecture enables reliable async processing
- Confirmation polling centralized (previously duplicated across services)

### Delivery Acceleration (Martin Aranda)

**API Gateway Decision:**
- Initially considered implementing API gateway for service discovery and routing
- Decided against gateway to simplify architecture
- Frontend will have direct knowledge of microservices endpoints
- Reduces moving parts, fewer potential failure points
- Faster implementation: critical with 3 weeks until beta launch

**Pragmatic Tradeoffs:**
- Gateway can be added later if needed (not irreversible decision)
- Current scale (2,000-200,000 users) doesn't require gateway complexity
- Direct communication easier to debug and monitor
- Reduces latency (no additional network hop)

### Event-Driven Transaction Processing

**RabbitMQ Integration:**
- Asynchronous transaction submission enables responsive UI
- Horizontal scaling through message queue distribution
- Retry mechanism handles Solana's dynamic blockhash requirements
- Decouples transaction submission from confirmation polling

**Transaction Lifecycle:**
1. Algorithm service creates transaction request
2. Event published to RabbitMQ
3. Transaction service constructs and signs transaction
4. Submitted to Solana network
5. Confirmation worker polls RPC for finalization
6. Frontend polls internal transaction ID for status updates

### Knowledge from Production Experience

**ClickHouse Performance Crisis:**
- Team learned importance of service isolation and specialization
- Cron decoupling dramatically improved performance (30-60s → <2s)
- Validated microservices approach for separating concerns
- Eduardo Yuschuk: "Need to decentralize technical knowledge to avoid operational bottlenecks"

## Consequences

### Positive

**Scalability:**
- Independent scaling per trading algorithm based on actual usage patterns
- Horizontal scaling capability validated (prepared for 10x-100x user growth)
- Message queue architecture supports high transaction volumes
- Stateless transaction service enables unlimited replicas

**Development Velocity:**
- Parallel development on different trading algorithms without conflicts
- Clear service boundaries reduce coordination overhead
- Algorithm teams can deploy independently
- Centralized transaction logic reduces duplicate work

**Maintainability:**
- Isolated services limit blast radius of bugs
- Clear separation of concerns (algorithm logic vs. transaction execution)
- Single transaction codebase easier to optimize and debug
- Service-specific monitoring and logging

**Operational Benefits:**
- Independent deployment per service (reduce deployment risk)
- Service-specific rollback capabilities
- Failure isolation prevents cascade failures
- Can experiment with new algorithms without affecting production services

**Performance:**
- Achieved dramatic performance improvements (30-60s → <2s page loads)
- Connection pool optimization per service
- Cron decoupling validated architectural approach
- Transaction retry logic reduces user-facing errors

### Negative

**Complexity:**
- More services to deploy, monitor, and maintain (6+ microservices vs. 1 monolith)
- Distributed system debugging challenges
- Need for service health monitoring across multiple services
- Infrastructure costs: multiple containers vs. single monolithic deployment

**Frontend Burden:**
- Frontend must know about all microservices endpoints
- No service discovery abstraction (hardcoded endpoint configuration)
- Must handle partial failures across multiple services
- Polling-based transaction status adds client-side complexity

**Operational Overhead:**
- Each service needs deployment pipeline, monitoring, logging
- RabbitMQ adds dependency to manage and monitor
- Service-to-service communication failures must be handled
- Need distributed tracing to debug cross-service issues

**Knowledge Centralization Risk:**
- Eduardo Yuschuk raised concern: indexer knowledge concentrated in one person
- Same risk applies to transaction microservice architecture
- Need knowledge sharing and documentation to avoid bottlenecks
- On-call rotation system requires broader team understanding

**Testing Complexity:**
- Integration testing requires multiple services running
- End-to-end testing spans algorithm service → transaction service → RabbitMQ → Solana
- Mock/stub complexity for local development
- Deployment testing requires full environment

### Neutral

- Direct frontend-to-microservice communication (simpler now, may need gateway later)
- Transaction polling pattern (acceptable for beta, may need WebSocket/SSE later)
- RabbitMQ choice (locks into message queue pattern but proven technology)
- Service boundaries by algorithm (could have chosen other decomposition strategies)

## Alternatives Considered

### Option 1: Monolithic Backend
**Description:** Single backend service handling all trading algorithms

**Pros:**
- Simplest deployment (one container)
- Easier debugging (single codebase, single log stream)
- No service-to-service communication overhead
- Shared code reuse trivial (just function calls)
- Lower infrastructure costs

**Cons:**
- Cannot scale algorithms independently
- Single point of failure for all trading functionality
- Tight coupling between trading strategies
- Difficult parallel development (merge conflicts, coordination overhead)
- Entire backend must redeploy for any algorithm change
- Resource allocation challenging (DCA and perpetuals share same resources)

**Why Rejected:** Does not support independent scaling per algorithm. As team validated, DCA might have 10x usage of perpetuals - monolith forces same resource allocation. Esteban's scalability argument validated microservices approach.

### Option 2: API Gateway with Service Mesh
**Description:** Microservices behind API gateway for routing and service discovery

**Pros:**
- Frontend only knows gateway endpoint (abstraction layer)
- Service discovery and routing centralized
- Can add cross-cutting concerns (rate limiting, auth) at gateway
- Service endpoints can change without frontend changes
- Load balancing and failover at gateway layer

**Cons:**
- Additional complexity and deployment
- Gateway becomes single point of failure
- Added network hop increases latency
- More moving parts to debug and monitor
- Overkill for current scale (2,000-200,000 users)
- Would delay delivery (decision made 3 weeks before beta)

**Why Rejected:** Martin Aranda's acceleration argument won. Gateway adds complexity without sufficient benefit at current scale. Can be added later if needed. Team prioritized delivery over architectural "perfection."

### Option 3: Microservices by Technical Layer
**Description:** Split by frontend/backend/database instead of by algorithm

**Pros:**
- Clear technical boundaries
- Standard layered architecture pattern
- Easier to understand for new developers
- Follows typical enterprise architecture

**Cons:**
- Algorithm changes span multiple services (coordination overhead)
- Cannot scale by business feature (can only scale technical layers)
- Tight coupling between layers for algorithm logic
- Doesn't align with business domain (trading algorithms)
- Less clear ownership (who owns "the backend"?)

**Why Rejected:** Doesn't align with business domain. Trading algorithms are the natural service boundaries - each has distinct logic, lifecycle, and scaling needs. Domain-driven design principles favor algorithm-based decomposition.

### Option 4: Function-as-a-Service (Serverless)
**Description:** AWS Lambda functions for each trading algorithm

**Pros:**
- Auto-scaling built-in (no manual horizontal scaling)
- Pay-per-use pricing model
- No server management
- Isolation by design (each function independent)

**Cons:**
- Cold start latency unacceptable for trading (milliseconds matter)
- Vendor lock-in to AWS Lambda
- Harder to debug and test locally
- RabbitMQ integration complexity in serverless environment
- Transaction confirmation polling doesn't fit Lambda model (long-running)
- Team unfamiliar with serverless patterns

**Why Rejected:** Trading requires low latency and long-running transaction confirmation polling. Serverless cold starts and execution time limits incompatible with requirements. Team expertise in containerized microservices, not serverless.

### Option 5: Single Microservice with Internal Routing
**Description:** One microservice with routing logic for different algorithms

**Pros:**
- Single deployment
- Simpler than multiple microservices
- Shared code easy to reuse
- Still separates from other system components

**Cons:**
- Cannot scale algorithms independently (back to monolith problem)
- Routing logic complexity grows with algorithms
- Single point of failure for all trading
- Algorithm changes require full service redeploy
- Tight coupling between algorithms

**Why Rejected:** Combines worst of both approaches - still a monolith (cannot scale independently) but with added routing complexity. Esteban's scalability argument showed independent algorithm scaling is critical.

## Implementation Notes

### Service Decomposition

**Algorithm Microservices (Current):**
- DCA (Dollar-Cost Averaging)
- Limit Orders (TP/SL)
- Perpetuals (Hyper Liquid)
- Market Orders

**Future Algorithm Services:**
- TWAP (Time-Weighted Average Price)
- VWAP (Volume-Weighted Average Price)
- Trailing Stop Loss
- Market Cap Variation Trading

**Shared Transaction Service:**
- Transaction construction and signing
- Solana network submission
- Retry logic with signature regeneration
- Confirmation polling and status tracking
- RabbitMQ event consumption

### Technology Stack

**Microservices Framework:**
- Backend language: Node.js/TypeScript (inferred from team context)
- REST APIs for frontend communication
- RabbitMQ for event-driven transaction processing
- Connection pooling for database queries

**Infrastructure:**
- AWS ECS for container orchestration (see ADR-300)
- Multi-AZ deployment for high availability (see ADR-500)
- Connection pool optimization: 2 cores per replica

**Transaction Processing:**
- RabbitMQ message queue
- Event-driven architecture
- Automatic retry with blockhash regeneration
- RPC polling for transaction confirmation

### Frontend Integration Pattern

**Direct Service Communication:**
```
Frontend → DCA Microservice → Transaction Service → RabbitMQ → Solana
                ↓
         Internal Transaction ID
                ↓
         Frontend Polling for Status
```

**Endpoint Configuration:**
- Frontend maintains service endpoint configuration
- Example: `DCA_SERVICE_URL`, `LIMIT_ORDERS_URL`, `PERPETUALS_URL`
- Direct HTTP requests to each service
- No service discovery or gateway routing

**Transaction Status Updates:**
- Frontend receives internal transaction ID on submission
- Polls transaction service for status updates
- Transaction states: pending → submitted → confirmed → finalized
- Error handling for failed or rejected transactions

### Deployment Strategy

**Independent Deployment:**
- Each algorithm service deploys independently
- Transaction service upgrades don't require algorithm service redeployment
- Gradual rollout possible (deploy to subset of users)
- Rollback per service if issues detected

**Scaling Configuration:**
- Auto-scaling based on service-specific metrics
- DCA service: scale on active DCA order count
- Limit orders: scale on open order monitoring load
- Transaction service: scale on RabbitMQ queue depth
- Perpetuals: scale on Hyper Liquid API call volume

### Testing Approach

**Unit Testing:**
- Algorithm logic tested in isolation
- Transaction construction tested independently
- Mock RabbitMQ for event publishing tests

**Integration Testing:**
- Algorithm service + Transaction service + RabbitMQ
- Use Solana devnet for end-to-end testing
- Verify transaction retry and confirmation logic

**Load Testing:**
- Simulate 2,000 → 200,000 user growth
- Validate horizontal scaling assumptions
- Test RabbitMQ throughput limits
- Verify connection pool optimization

### Migration from Monolith (If Applicable)

**Incremental Extraction:**
1. Start with new algorithm (lowest risk)
2. Extract transaction logic to shared service
3. Migrate existing algorithms one at a time
4. Dual-run during migration for validation
5. Sunset monolith when all algorithms migrated

### Knowledge Sharing Requirements

**Addressing Centralization Risk:**
- Document transaction service architecture (prevent Eduardo situation)
- On-call rotation includes all services (spreads knowledge)
- Pair programming on transaction service changes
- Architecture decision records for service boundaries
- Regular architecture review sessions

## References

### Meeting Notes
- [Daily Standup 2025-09-26](../06-meetings/2025-09/2025-09-26-daily-standup.md) - Microservices decision and transaction service presentation
- [Bug Alignment 2025-09-15](../06-meetings/2025-09/2025-09-15-bug-alignment.md) - Scalability discussion and architectural context

### Related Decisions
- ADR-300: AWS ECS over EKS for Container Orchestration
- ADR-500: Multi-AZ Deployment for High Availability
- ADR-104: Redis for JSON Block Storage
- ADR-003: WebSocket to SSE Migration (real-time updates architecture)

### Technical References
- Esteban Restrepo's transaction microservice presentation (6000+ lines)
- RabbitMQ event-driven architecture documentation
- Solana transaction lifecycle and blockhash requirements

### Performance Context
- Performance breakthrough: 30-60s → <2s page load times
- Cron decoupling validated service isolation approach
- Connection pool optimization: 2 cores per replica

## Revision History
- 2025-09-26: Initial decision - algorithm-based microservices without API gateway
- 2025-10-21: Formal ADR documented from meeting notes
