---
title: Transaction Security Validation Pattern
type: decision-record
decision-id: ADR-105
date: 2025-10-10
status: accepted
owner: Martin Aranda
stakeholders: [Lucas Cufré, Zen (Client), Backend Team, Security Team]
tags: [technical, security, transaction-validation, backend, routing]
summary: |
  Decision to implement internal transaction breakdown and validation before execution,
  ensuring all transactions match expected patterns and mitigating risks from compromised
  external routing backends (Jupiter, Echo, etc.) without adding latency to user experience.
related-docs:
  - ../06-meetings/2025-10/2025-10-10-cooking-demo.md
  - ../06-meetings/2025-10/2025-10-16-mobile-app-final-sync.md
  - 2025-10-15-jupiter-primary-router.md
---

# ADR-105: Transaction Security Validation Pattern

## Context and Problem Statement

As Cooking.gg integrates with multiple external transaction routing providers (Jupiter, Echo, Hello Moon), the platform faces security risks if any of these external backends were to be compromised. A malicious or compromised routing service could potentially construct transactions that:

- Route funds to unexpected addresses
- Include hidden fees or drains
- Execute trades at unfavorable prices
- Manipulate transaction ordering or timing

**Key Security Concerns:**
- External routing services have control over transaction construction
- Users trust the platform to execute trades safely
- Blockchain transactions are irreversible once executed
- Multiple providers means multiple potential attack vectors
- No visibility into provider security practices

**Performance Requirements:**
- Validation must not add perceptible latency to user experience
- Current transaction times: 2-3 seconds (target to maintain)
- Real-time trading requires fast execution
- Cannot rely on external validation services (would add latency)

**Problem Statement:**
How can we ensure transaction security and integrity when relying on external routing providers, while maintaining the fast execution times required for competitive trading?

## Decision

**Implement internal transaction breakdown and validation system** that deconstructs every transaction before execution and verifies it against internally approved patterns.

### Implementation Details

**Transaction Validation Flow:**
1. **External Router Response:** Receive constructed transaction from provider (Jupiter, Echo, etc.)
2. **Internal Deconstruction:** Break down transaction into individual instructions and operations
3. **Pattern Matching:** Verify each component against approved transaction patterns
4. **Security Checks:**
   - Validate all destination addresses match expected patterns
   - Verify token amounts and types
   - Check for unexpected instructions or operations
   - Confirm fee structures match expected ranges
5. **Approval/Rejection:**
   - If validation passes: Sign and execute transaction
   - If validation fails: Reject and log security incident
6. **Backup Routing:** If primary provider transaction rejected, attempt with backup provider

**Validation Rules:**
- All swap destinations must be user-controlled wallets or approved protocols
- Fee instructions must match expected fee structure (platform fees, network fees)
- Token amounts must match user-specified trade parameters
- No unexpected account creations or modifications
- All programs/protocols must be on approved whitelist

**Performance Strategy:**
- Validation handled entirely internally (no external API calls)
- Pre-computed pattern matching (O(1) or O(log n) lookups)
- Parallel validation where possible
- Optimized for sub-100ms validation time
- Does not add perceptible latency to 2-3 second transaction flow

### Backup Routing System

**Multi-Provider Architecture:**
- Primary: Jupiter (most transactions)
- Secondary: Hello Moon (slower by ~500ms but reliable)
- Tertiary: Native system (fallback)
- Future: Echo (limited protocols - Pump.fun, LaunchLab)

**Failover Logic:**
- If transaction from Provider A fails validation → try Provider B
- If all providers fail → alert user and log incident
- Security failures logged separately from performance failures

## Rationale

### Security Benefits

1. **Defense in Depth:** Even if external provider compromised, malicious transactions blocked
2. **Provider Independence:** Not dependent on any single provider's security practices
3. **Audit Trail:** All validation decisions logged for security review
4. **User Protection:** Ensures trades execute as intended by user
5. **Rapid Incident Response:** Immediate detection of anomalous transaction patterns

### Technical Advantages

1. **Zero Latency Impact:** Internal validation faster than any external service
2. **Deterministic:** Clear rules for transaction approval/rejection
3. **Extensible:** Easy to add new validation rules as threats evolve
4. **Provider Agnostic:** Works with any routing provider
5. **Testable:** Validation logic can be comprehensively unit tested

### Business Value

1. **User Trust:** Demonstrates commitment to security
2. **Risk Mitigation:** Reduces legal/reputational exposure from compromised providers
3. **Competitive Advantage:** Higher security standard than competitors
4. **Regulatory Compliance:** Demonstrates transaction oversight and control

## Consequences

### Positive Consequences

- **Enhanced Security:** Multi-layered protection against compromised routing providers
- **No Performance Impact:** Validation adds <100ms, imperceptible in 2-3s transaction flow
- **Provider Flexibility:** Can confidently integrate new providers knowing validation layer protects users
- **Incident Detection:** Immediate alerting if provider begins serving malicious transactions
- **User Confidence:** Users can trade knowing transactions are validated before execution

### Negative Consequences

- **Development Complexity:** Requires building and maintaining validation rule engine
- **False Positives Risk:** Overly strict validation could reject legitimate transactions
- **Maintenance Burden:** Validation rules must be updated as protocols/patterns evolve
- **Testing Requirements:** Comprehensive test coverage needed for all validation paths

### Neutral Consequences

- **Backup Provider Cost:** May use more expensive backup providers if primary fails validation
- **Logging Overhead:** Validation failures generate significant logs requiring storage/analysis
- **Monitoring Required:** Need dashboards and alerts for validation failure patterns

## Alternatives Considered

### Option 1: Trust External Providers (No Validation)

**Description:** Rely entirely on external routing providers' security practices.

**Pros:**
- Simplest implementation
- Zero development cost
- No performance overhead
- No maintenance burden

**Cons:**
- Complete exposure to provider compromise
- No defense layer
- Irreversible user fund loss if provider compromised
- Reputational damage
- Potential legal liability

**Rejected:** Unacceptable security risk for trading platform handling user funds.

### Option 2: External Validation Service

**Description:** Use third-party transaction validation API before execution.

**Pros:**
- Offloads validation complexity
- Professional security expertise
- Regular updates from external team

**Cons:**
- **Adds 200-500ms latency** (makes 2-3s transactions become 2.5-3.5s)
- Additional cost per transaction
- New dependency and potential failure point
- Still requires internal fallback for service outages
- Limited customization for platform-specific needs

**Rejected:** Latency impact unacceptable for competitive trading experience.

### Option 3: Blockchain-Level Validation

**Description:** Use Solana program verification or on-chain guards.

**Pros:**
- Maximum security (enforced by blockchain)
- No backend trust required
- Immutable security guarantees

**Cons:**
- Extremely high development cost
- Requires custom Solana programs
- Significant blockchain expertise needed
- Would increase transaction costs (compute units)
- Inflexible (hard to update validation rules)
- Still need backend validation for pre-submission checks

**Rejected:** Over-engineered for current needs; internal validation sufficient.

### Option 4: Manual Review for High-Value Transactions

**Description:** Flag high-value transactions for human review before execution.

**Pros:**
- Human judgment for edge cases
- Lower development cost than automated system

**Cons:**
- Terrible user experience (delays)
- Doesn't scale
- Still need automated validation for normal transactions
- Creates bottleneck and support burden
- Not viable for real-time trading

**Rejected:** Incompatible with real-time trading requirements.

## Implementation Notes

### Phase 1: Core Validation (Completed)

- ✅ Transaction deconstruction engine
- ✅ Basic pattern matching for swaps
- ✅ Destination address validation
- ✅ Fee structure validation
- ✅ Logging and monitoring

### Phase 2: Enhanced Validation (In Progress)

- ⏳ Whitelist management for approved protocols
- ⏳ Advanced pattern matching for complex trades
- ⏳ Rate limiting and anomaly detection
- ⏳ Automated security alerts

### Phase 3: Future Enhancements

- Planned: Machine learning for anomaly detection
- Planned: Historical pattern analysis
- Planned: Integration with blockchain security feeds
- Planned: Automated response to security incidents

### Validation Rule Examples

**Approved Swap Pattern:**
```
1. Transfer SOL/USDC from user wallet → Jupiter program
2. Execute swap through approved DEX (Raydium, Orca, etc.)
3. Transfer output token → user wallet
4. Platform fee instruction (if applicable)
```

**Rejected Pattern (Security Risk):**
```
1. Transfer tokens from user wallet → unknown address
2. ❌ VALIDATION FAILURE: Unknown destination
```

### Monitoring and Alerting

**Metrics to Track:**
- Validation pass rate per provider
- Average validation time
- Types of validation failures
- Provider-specific failure patterns
- False positive rate

**Alerts:**
- Critical: >5% validation failure rate from any provider
- Critical: Unknown instruction type detected
- Warning: New destination address pattern
- Warning: Unusual fee structure
- Info: Backup provider used due to validation failure

## References

### Related Meetings
- [2025-10-10 Cooking Demo](../06-meetings/2025-10/2025-10-10-cooking-demo.md) - Initial security discussion with Zen
- [2025-10-16 Mobile App Final Sync](../06-meetings/2025-10/2025-10-16-mobile-app-final-sync.md) - Validation implementation confirmation

### Related ADRs
- [ADR-100: Jupiter as Primary Router](2025-10-15-jupiter-primary-router.md) - Primary routing provider
- [ADR-002: Microservices Architecture by Trading Algorithm](2025-09-26-microservices-by-algorithm.md) - Transaction processing architecture

### Technical References
- Solana transaction structure documentation
- Jupiter API transaction format
- Internal transaction processing architecture

---

**Status:** Accepted and Implemented
**Implementation Date:** October 2025
**Owner:** Martin Aranda (Backend Team)
**Review Date:** Post-beta launch (monitor validation metrics)
