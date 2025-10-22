---
title: WebSocket to SSE Migration for Real-Time Updates
type: decision-record
decision-id: ADR-003
date: 2025-08-27
status: accepted
owner: Martin Aranda, Esteban Restrepo
stakeholders: [Martin Aranda, Esteban Restrepo, Federico Caffaro, Luis Rivera, Eduardo Yuschuk, Backend Team, Frontend Team]
tags: [architecture, real-time, streaming, scalability, infrastructure, aws]
summary: |
  Decision to migrate from WebSocket to Server-Sent Events (SSE) with heartbeat mechanism for real-time data updates. WebSocket removal driven by AWS 60-second timeout limitations, scalability concerns, and infrastructure complexity. SSE with 25-second heartbeat intervals provides reliable, HTTP-based streaming while reducing resource overhead and improving horizontal scalability.
related-docs:
  - ../06-meetings/2025-08/2025-08-27-daily-standup.md
  - ../06-meetings/2025-08/2025-08-29-daily-standup.md
  - ../06-meetings/2025-08/2025-08-25-limit-orders.md
  - ../06-meetings/2025-08/2025-08-summary.md
---

# WebSocket to SSE Migration for Real-Time Updates

## Context and Problem Statement

Cooking.gg requires real-time data updates for critical features including:
- Live price feeds for trading pairs
- Order book updates
- Transaction status notifications
- Portfolio balance changes
- Limit order fill notifications
- Market data streaming (OHLCV charts)

Initially implemented with WebSocket connections, the team encountered significant production-readiness challenges as beta launch approached in September 2025.

**Problems with WebSocket Implementation:**

1. **AWS Infrastructure Timeout**: 60-second timeout limit on WebSocket connections
   - Connections would drop after 60 seconds of inactivity
   - Required complex reconnection logic
   - Unpredictable connection stability

2. **Resource Intensity**:
   - Persistent bidirectional connections consume more server resources
   - Each connection holds memory and file descriptors
   - Scaling horizontally difficult (sticky sessions required)
   - Higher infrastructure costs for maintaining connections

3. **Scaling Challenges**:
   - Horizontal scaling complicated by stateful connections
   - Load balancer complexity (connection affinity requirements)
   - Connection migration during deployments problematic
   - Difficult to predict resource needs under variable load

4. **Operational Complexity**:
   - Monitoring and debugging distributed WebSocket connections
   - Connection state management across microservices (see ADR-002)
   - Graceful shutdown challenges during deployments
   - Error recovery and retry logic complexity

**Requirements for Solution:**
- Reliable real-time data streaming
- Compatibility with AWS infrastructure constraints
- Horizontal scalability for production load (2,000-200,000 users)
- Simpler operational model
- Lower resource overhead
- Compatible with microservices architecture (ADR-002)
- Support for long-lived connections without timeout issues

## Decision

**Migrate from WebSocket to Server-Sent Events (SSE) with 25-second heartbeat intervals for all real-time data updates.**

### Implementation Strategy

**SSE with Heartbeat Protocol:**
- **Technology**: Server-Sent Events (SSE) via HTTP
- **Heartbeat Interval**: 25 seconds
- **Timeout Prevention**: Heartbeat keeps connection alive (AWS 60s limit)
- **Coverage**: Applied to all SSE controllers across backend
- **Fallback**: 10-second REST API polling for clients without SSE support

**SSE Characteristics:**
- Unidirectional data flow (server → client)
- HTTP-based protocol (simpler than WebSocket)
- Automatic reconnection built into EventSource API
- Standard HTTP infrastructure (load balancers, proxies, CDN-friendly)
- Text-based streaming (JSON payloads)

### Architecture Components

**Backend SSE Controllers:**
- Price feed controller (token prices, market data)
- Order status controller (limit orders, fills)
- Transaction controller (submission, confirmation status)
- Portfolio controller (balance updates)
- Each controller implements 25-second heartbeat

**Heartbeat Implementation:**
```javascript
// Pseudocode - SSE heartbeat pattern
setInterval(() => {
  // Send heartbeat every 25 seconds
  res.write('event: heartbeat\n');
  res.write('data: {"type":"heartbeat","timestamp":' + Date.now() + '}\n\n');
}, 25000); // 25-second intervals

// Client automatically receives heartbeat, preventing AWS timeout
```

**Frontend Integration:**
```javascript
// EventSource API provides automatic reconnection
const eventSource = new EventSource('/api/sse/prices');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'heartbeat') return; // Ignore heartbeats
  updateUI(data); // Process real data
};

eventSource.onerror = () => {
  // Browser automatically reconnects
  console.log('Connection lost, reconnecting...');
};
```

**Polling Fallback:**
- 10-second REST API polling for browsers without SSE support
- Legacy browser compatibility (IE, older mobile browsers)
- Degraded experience but functional
- Automatically detected and applied

### Migration Timeline

**Phase 1: SSE Implementation (July 23-28, 2025)**
- Initial SSE controller development
- Testing SSE streaming capabilities
- Frontend EventSource integration
- Mocking challenges addressed

**Phase 2: Heartbeat Decision (August 27, 2025)**
- AWS timeout issue identified
- 25-second heartbeat interval selected
- Application to all SSE controllers initiated
- Esteban Restrepo assigned implementation

**Phase 3: WebSocket Removal (August 29, 2025)**
- Decision made to remove WebSocket dependencies entirely
- Migration to REST endpoints where SSE not suitable
- Backend architectural simplification
- Production readiness focus

**Phase 4: Production Deployment (September 2025)**
- All SSE controllers with heartbeat deployed
- WebSocket dependencies removed
- Monitoring and stability validation
- Beta launch readiness achieved

## Rationale

### AWS Infrastructure Constraint (Primary Driver)

**60-Second Timeout Problem:**
- AWS load balancers and infrastructure enforce 60-second timeout on idle connections
- WebSocket connections would silently drop after 60 seconds without data
- Users experienced unexpected disconnections
- Reconnection logic created UX problems (loading states, missed updates)

**SSE + Heartbeat Solution:**
- 25-second heartbeat ensures connection never idle for >60 seconds
- Safe margin (25s * 2 = 50s, well under 60s limit)
- Automatic reconnection via EventSource API (browser handles it)
- No missed data during reconnection (SSE protocol supports Last-Event-ID)

**Why 25 Seconds:**
- Tested interval providing reliable operation
- Balances connection stability vs. network overhead
- 25s * 2 = 50s (10-second safety margin before 60s timeout)
- Matches industry patterns for SSE heartbeat intervals

### Scalability and Resource Efficiency

**WebSocket Resource Overhead:**
- Each WebSocket connection: persistent TCP connection + memory for buffers
- Bidirectional channels consume more resources (even when only server→client needed)
- Scaling requires sticky sessions (complicates load balancing)
- Connection migration during deployments causes disruptions

**SSE Advantages:**
- Unidirectional (server→client) - lower resource overhead
- Standard HTTP - no sticky sessions required (easier horizontal scaling)
- Stateless from server perspective (can migrate connections)
- Browser manages reconnection (reduces server complexity)

**Esteban Restrepo's Scaling Context (Aug 27):**
> "SSE improvements and scaling. Implementation: Heartbeat for connection stability (25s intervals). Current Work: Transaction service scaling proposal."

Team preparing for 100x user growth (2,000 → 200,000 users). SSE architecture scales more predictably.

### Operational Simplicity

**WebSocket Complexity:**
- Custom reconnection logic required
- Connection state management across distributed backend (microservices)
- Debugging distributed WebSocket connections difficult
- Graceful shutdown during deployments complex

**SSE Simplicity:**
- Standard HTTP (familiar debugging tools)
- Browser EventSource API handles reconnection automatically
- No connection state to manage (RESTful endpoints)
- Deployments: old connections drop, clients auto-reconnect to new instances

**Martin Aranda's Context (Aug 29):**
> "Planning WebSocket removal, preparing database migration. Decision to remove WebSocket dependencies to improve scalability."

Strategic decision aligned with production readiness and architectural simplification.

### Compatibility with Microservices Architecture

**Microservices Challenge (see ADR-002):**
- WebSocket connections tied to specific backend instances
- Microservices architecture: multiple services need to push updates
- Connection affinity creates scaling bottleneck
- Service discovery complexity for WebSocket routing

**SSE Solution:**
- HTTP-based: standard API gateway patterns work
- Each microservice can have SSE endpoints
- No connection affinity required (load balance freely)
- Aligns with RESTful microservices design

### Real-World Production Context

**August 2025: Final Weeks Before Beta**
- UI/UX polish prioritized over new features (Aug 27)
- Production stability critical for real-user beta
- Infrastructure simplification reduces risk
- Team capacity stretched - simpler solutions preferred

**Client Feedback (Aug 27 Demo):**
> "Functionality is there but needs polish. Loading states are confusing users."

WebSocket reconnection logic created loading state confusion. SSE automatic reconnection eliminated this UX problem.

### Hybrid Approach for Edge Cases

**Some Features Retained Polling:**
- Limit order fill notifications: WebSocket primary, 10-second polling fallback (Aug 25)
- Later migrated to SSE as well (Aug 27-29)
- Demonstrates pragmatic, phased migration approach

**Why Fallback Matters:**
- Legacy browser support (corporate networks, old devices)
- Network environments blocking SSE (rare but exists)
- Graceful degradation ensures functionality for all users

## Consequences

### Positive

**Infrastructure Reliability:**
- No more 60-second timeout disconnections
- Heartbeat mechanism ensures connection stability
- Automatic browser reconnection reduces error scenarios
- Predictable connection behavior in production

**Scalability:**
- Horizontal scaling simplified (no sticky sessions)
- Lower resource overhead per connection
- Can handle 100x user growth more efficiently
- Microservices can scale independently (see ADR-002)

**Operational Benefits:**
- Standard HTTP debugging tools work (curl, Postman, browser DevTools)
- Simpler deployment process (no connection migration complexity)
- Monitoring easier (HTTP metrics, no WebSocket-specific tooling)
- Reduced operational complexity for on-call team

**Development Velocity:**
- Browser EventSource API reduces client-side code
- No custom reconnection logic needed
- Faster feature development (simpler data streaming)
- Less testing complexity (standard HTTP patterns)

**User Experience:**
- Seamless reconnection (users don't notice)
- No loading states during reconnection
- Missed updates handled by SSE protocol (Last-Event-ID)
- Consistent experience across all network conditions

**Cost Efficiency:**
- Lower infrastructure costs (less resource per connection)
- Predictable AWS billing (no WebSocket-specific charges)
- Can serve more users with same infrastructure

### Negative

**Unidirectional Only:**
- SSE is server→client only (no client→server streaming)
- For client→server: must use separate POST requests
- Slightly less efficient for bidirectional scenarios (trading doesn't need this)

**Browser Compatibility:**
- EventSource not supported in IE11 (falling back to polling)
- Some corporate proxies block SSE (rare, but polling fallback needed)
- Requires polyfill for very old browsers

**Heartbeat Overhead:**
- 25-second heartbeat adds network traffic (minimal: ~10 bytes every 25s)
- All clients receive heartbeats (wasteful for inactive tabs)
- Trade-off: small overhead vs. connection reliability

**Less Sophisticated Than WebSocket:**
- No built-in binary data support (JSON text only - acceptable for our use case)
- No multiplexing within single connection (not needed)
- Less suitable for gaming/ultra-low-latency (trading is not this)

**Migration Effort:**
- Refactor all WebSocket controllers to SSE
- Update frontend code from WebSocket to EventSource
- Test all real-time features with new implementation
- August 2025 timeline pressure (weeks before beta)

**Monitoring Gaps (Initially):**
- Existing WebSocket monitoring tools don't apply to SSE
- Need to establish new SSE connection metrics
- Heartbeat success rate monitoring needed
- Learning curve for team

### Neutral

- Polling fallback (necessary for compatibility, but adds code complexity)
- HTTP-based (familiar, but no special WebSocket features)
- Heartbeat interval tuning (25s chosen empirically, could be optimized)
- Text-based protocol (JSON overhead acceptable for our data volumes)

## Alternatives Considered

### Option 1: Keep WebSocket with Custom Heartbeat
**Description:** Retain WebSocket but implement custom heartbeat to prevent AWS timeout

**Pros:**
- Bidirectional communication (client→server, server→client)
- No migration effort required
- Team already familiar with WebSocket code
- True real-time with lower latency

**Cons:**
- Still complex to scale horizontally (sticky sessions)
- Custom heartbeat logic on both client and server
- Higher resource overhead per connection
- WebSocket debugging still difficult
- Doesn't address operational complexity

**Why Rejected:** Heartbeat solves timeout but doesn't address scalability, resource efficiency, or operational complexity. SSE provides heartbeat + additional benefits. Team decision (Aug 29) to remove WebSocket entirely indicates confidence in SSE approach.

### Option 2: Pure REST Polling (No Streaming)
**Description:** Eliminate streaming entirely, use 10-second REST API polling for all updates

**Pros:**
- Simplest implementation (no long-lived connections)
- Easiest to scale (stateless HTTP requests)
- No timeout issues
- Minimal server resources
- Familiar HTTP patterns

**Cons:**
- 10-second polling too slow for trading platform (price updates feel laggy)
- High server load (constant polling from all clients)
- Wasted requests when no data changed
- Poor user experience (delayed updates)
- Not competitive with WebSocket-based platforms

**Why Rejected:** User experience unacceptable for real-time trading platform. Competitors use WebSocket/SSE - polling creates competitive disadvantage. Team already invested in streaming architecture.

### Option 3: GraphQL Subscriptions
**Description:** Use GraphQL subscriptions for real-time data (typically over WebSocket)

**Pros:**
- Modern approach (GraphQL ecosystem growing)
- Type-safe subscriptions
- Client can specify exactly what data to receive
- Good developer experience

**Cons:**
- Still uses WebSocket under the hood (same AWS timeout problem)
- Adds GraphQL dependency (team using REST APIs)
- Learning curve for team
- Overkill for simple streaming use case
- Migration effort larger than SSE switch

**Why Rejected:** Doesn't solve underlying WebSocket problems (still WebSocket transport). Introduces new technology stack. SSE simpler and addresses actual constraints.

### Option 4: WebRTC Data Channels
**Description:** Use WebRTC for peer-to-peer or server-client real-time communication

**Pros:**
- Very low latency (designed for real-time)
- Supports binary data efficiently
- P2P possible (reduce server load)

**Cons:**
- Massive overkill for server→client data streaming
- Complex setup (STUN/TURN servers, ICE negotiation)
- Browser compatibility issues
- Not designed for server-to-many-clients pattern
- Debugging extremely difficult

**Why Rejected:** WebRTC designed for video/audio calling, not server data streaming. Complexity far exceeds SSE. No peer-to-peer benefit in our use case (centralized data from indexer).

### Option 5: WebSocket with AWS ALB Timeout Configuration
**Description:** Configure AWS Application Load Balancer for longer WebSocket timeout

**Pros:**
- Solves AWS timeout issue directly
- Retain WebSocket benefits
- No code changes required

**Cons:**
- AWS ALB WebSocket timeout maximum is 1 hour (not guaranteed)
- Doesn't address scalability or resource concerns
- Still complex to operate and debug
- Configuration-based solution (risky, not in code)
- Future AWS changes could break it

**Why Rejected:** Treats symptom, not root cause. Team wants architectural simplification, not AWS config hacks. SSE provides better long-term solution.

### Option 6: Long Polling
**Description:** HTTP long polling (client requests, server holds until data available)

**Pros:**
- Works everywhere (no special browser support needed)
- No persistent connection (lower server resources)
- Familiar HTTP pattern

**Cons:**
- Higher latency than SSE (request/response overhead)
- More complex server code (track pending requests)
- Poor scalability (many hanging requests)
- Outdated pattern (SSE supersedes long polling)

**Why Rejected:** Long polling is older technology superseded by SSE. SSE provides same benefits with better browser integration and cleaner code.

## Implementation Notes

### SSE Controller Pattern

**Standard SSE Response Structure:**
```javascript
// Backend SSE controller pattern
app.get('/api/sse/prices', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  // Heartbeat interval
  const heartbeat = setInterval(() => {
    res.write('event: heartbeat\n');
    res.write('data: {"type":"heartbeat"}\n\n');
  }, 25000); // 25 seconds

  // Data streaming
  const dataStream = subscribeToPriceUpdates((priceUpdate) => {
    res.write('event: price\n');
    res.write('data: ' + JSON.stringify(priceUpdate) + '\n\n');
  });

  // Cleanup on disconnect
  req.on('close', () => {
    clearInterval(heartbeat);
    dataStream.unsubscribe();
  });
});
```

### Frontend EventSource Pattern

**Standard Client Implementation:**
```javascript
// Frontend SSE client pattern
class SSEConnection {
  constructor(url) {
    this.eventSource = new EventSource(url);

    // Handle price updates
    this.eventSource.addEventListener('price', (event) => {
      const data = JSON.parse(event.data);
      this.handlePriceUpdate(data);
    });

    // Ignore heartbeats (browser handles them automatically)
    this.eventSource.addEventListener('heartbeat', () => {
      // Heartbeat received, connection alive
    });

    // Handle errors (browser auto-reconnects)
    this.eventSource.onerror = (error) => {
      console.log('SSE connection error, browser will reconnect');
    };
  }

  close() {
    this.eventSource.close();
  }
}
```

### Polling Fallback Implementation

**Legacy Browser Support:**
```javascript
// Feature detection
const useSSE = typeof EventSource !== 'undefined';

if (useSSE) {
  // Use SSE for modern browsers
  const conn = new SSEConnection('/api/sse/prices');
} else {
  // Fall back to polling for IE11
  setInterval(async () => {
    const data = await fetch('/api/prices');
    handlePriceUpdate(await data.json());
  }, 10000); // 10-second polling
}
```

### Controllers Requiring SSE Migration

**Priority 1 (Critical for Trading):**
- Price feed controller (token prices from indexer)
- Order status controller (limit order fills)
- Transaction status controller (confirmation updates)

**Priority 2 (Important for UX):**
- Portfolio balance controller (real-time balance)
- Market data controller (OHLCV chart updates)
- Notification controller (system alerts)

**Implementation Checklist:**
- [ ] Apply 25-second heartbeat to all SSE controllers
- [ ] Add EventSource integration to frontend
- [ ] Implement polling fallback for legacy browsers
- [ ] Remove WebSocket dependencies
- [ ] Update monitoring for SSE connection metrics
- [ ] Test reconnection behavior under various network conditions
- [ ] Validate heartbeat prevents AWS timeout
- [ ] Load test SSE endpoint scalability

### Monitoring and Metrics

**SSE-Specific Metrics:**
- Active SSE connections count
- Heartbeat success rate
- Reconnection frequency
- Average connection duration
- Data throughput per connection
- Client distribution (SSE vs. polling fallback)

**Alerting Thresholds:**
- Heartbeat failure rate >1% (investigate AWS issues)
- Reconnection rate >10% (network instability)
- Active connections spike (potential DoS)
- Connection duration <25s (heartbeat not working)

### Migration Rollout Strategy

**Week 1: SSE Implementation (July 23-28)**
- Implement SSE controllers
- Add frontend EventSource integration
- Test in development environment

**Week 2: Heartbeat Addition (August 27)**
- Add 25-second heartbeat to all controllers
- Validate AWS timeout prevention
- Deploy to staging environment

**Week 3: WebSocket Removal (August 29)**
- Remove WebSocket dependencies
- Migrate all remaining features to SSE or REST
- Production deployment

**Week 4: Monitoring & Optimization (September)**
- Monitor SSE connection stability
- Optimize heartbeat interval if needed
- Address any production issues

### Testing Strategy

**Unit Tests:**
- SSE controller heartbeat interval
- EventSource reconnection logic
- Polling fallback activation

**Integration Tests:**
- End-to-end SSE streaming
- Heartbeat prevents timeout
- Reconnection after disconnection
- Data consistency during reconnection

**Load Tests:**
- 10,000 concurrent SSE connections
- Heartbeat overhead measurement
- Server resource usage
- Horizontal scaling validation

**Network Simulation:**
- Intermittent connectivity
- High latency networks
- Corporate proxy environments
- Mobile network conditions

## References

### Meeting Notes
- [Daily Standup 2025-08-27](../06-meetings/2025-08/2025-08-27-daily-standup.md) - SSE heartbeat decision and implementation
- [Daily Standup 2025-08-29](../06-meetings/2025-08/2025-08-29-daily-standup.md) - WebSocket removal decision
- [Limit Orders Meeting 2025-08-25](../06-meetings/2025-08/2025-08-25-limit-orders.md) - WebSocket with polling fallback discussion
- [August 2025 Summary](../06-meetings/2025-08/2025-08-summary.md) - Monthly technical decisions

### Related Decisions
- ADR-002: Microservices Architecture by Trading Algorithm (SSE per microservice)
- ADR-005: Indexer Microservices by Protocol (data source for SSE streams)
- ADR-300: AWS ECS Container Orchestration (infrastructure context)

### Technical References
- MDN EventSource API: https://developer.mozilla.org/en-US/docs/Web/API/EventSource
- SSE Specification: https://html.spec.whatwg.org/multipage/server-sent-events.html
- AWS ALB Timeout Documentation
- Server-Sent Events vs WebSocket comparison articles

### AWS Infrastructure Constraints
- AWS Application Load Balancer 60-second idle timeout
- AWS ECS task resource allocation
- Connection pooling for distributed backend

### Performance Benchmarks
- WebSocket resource overhead measurements
- SSE heartbeat network traffic analysis
- Concurrent connection load testing results

## Revision History
- 2025-07-23: Initial SSE implementation started
- 2025-08-27: 25-second heartbeat decision made and implementation assigned to Esteban Restrepo
- 2025-08-29: WebSocket removal decision finalized by Martin Aranda
- 2025-09-XX: Production deployment for beta launch
- 2025-10-21: Formal ADR documented from meeting notes
