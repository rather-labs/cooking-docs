---
title: AWS ECS over EKS for Container Orchestration
type: decision-record
decision-id: ADR-300
date: 2025-09-04
status: accepted
owner: Martin Aranda
stakeholders: [Eduardo Yuschuk, Lucas Cufré, Marcos Tacca, DevOps Team]
tags: [process, infrastructure, devops, container-orchestration, aws, deployment, scaling]
summary: |
  Decision to use AWS ECS (Elastic Container Service) over EKS (Elastic Kubernetes Service)
  for container orchestration in production, prioritizing simplicity, faster deployment,
  and lower operational overhead during beta launch phase.
related-docs:
  - ../06-meetings/2025-09/2025-09-04-devops-session-1.md
  - 2025-09-04-multi-az-deployment-high-availability.md
  - ADR-402-aws-waf-encryption-strategy.md
---

# ADR-300: AWS ECS over EKS for Container Orchestration

## Context

As the Cooking.gg platform approached its beta launch in late September/early October 2025, the team needed to finalize the production infrastructure architecture. All services had been containerized using Docker, and the team needed to select a container orchestration platform to manage deployment, scaling, service discovery, and health management across multiple microservices in production.

### Background

**Development Status (September 2025):**
- All services containerized with Docker
- Multiple microservices architecture established:
  - API Gateway
  - Trading Engine (multiple algorithms)
  - Indexer Service (by protocol: Solana, Hyperliquid)
  - WebSocket Server (real-time price feeds)
  - Background Workers (async tasks)
  - Transaction Service (isolated microservice)
- Beta launch approaching (5-6 weeks away)
- Team of 11+ members, but limited DevOps specialization
- Production infrastructure needed immediately for final testing and launch

**Service Architecture Requirements:**
- **Scalability**: Auto-scale based on load (expected 200-2,000 initial users, potential rapid growth)
- **High Availability**: Multi-AZ deployment for 99.9% uptime target
- **Zero-Downtime Deployments**: Blue-green or rolling updates
- **Service Discovery**: Automatic registration and discovery of services
- **Health Management**: Automated health checks and self-healing
- **Resource Efficiency**: Optimal resource utilization and cost management
- **Monitoring**: Integrated metrics, logging, and alerting

**Team Constraints:**
- Limited Kubernetes expertise on team
- Martin Aranda (Technical Lead) primary DevOps resource
- Eduardo Yuschuk (Indexer) assisting with infrastructure
- Timeline pressure: 5-6 weeks to production launch
- Need to focus on application development, not infrastructure learning curve

### Problem Statement

The team needed to choose between two primary container orchestration options:

**Option 1: Amazon ECS (Elastic Container Service)**
- AWS-managed container orchestration service
- Native AWS integration (ALB, CloudWatch, IAM, etc.)
- Simpler learning curve for teams familiar with AWS
- Task-based orchestration model

**Option 2: Amazon EKS (Elastic Kubernetes Service)**
- Managed Kubernetes service on AWS
- Industry-standard Kubernetes API
- More complex, more powerful
- Large ecosystem of tools and operators

**Key Considerations:**
1. **Time to Production**: How quickly can we deploy confidently?
2. **Operational Complexity**: Can our small team manage it?
3. **Learning Curve**: How much new knowledge required?
4. **Scalability**: Will it handle our growth trajectory?
5. **Cost**: Both infrastructure and operational costs
6. **Vendor Lock-in**: Future portability concerns
7. **Debugging and Troubleshooting**: Ease of issue resolution
8. **Integration**: How well does it integrate with our AWS stack?

---

## Decision

**Use Amazon ECS (Elastic Container Service) for container orchestration in production, with Fargate launch type for serverless container management.**

### Implementation Approach

**Container Orchestration:**
- **ECS Clusters**: Separate clusters for staging and production
- **Fargate Launch Type**: Serverless compute (no EC2 instance management)
- **Task Definitions**: Containerized service specifications with resource limits
- **Services**: Long-running tasks with auto-scaling and load balancing
- **Task Placement**: Spread across multiple availability zones

**Service Configuration:**
- API Gateway: 2-10 tasks (auto-scaled)
- Trading Engine: 2-8 tasks per algorithm
- Indexer Service: 2-6 tasks per protocol
- WebSocket Server: 2-10 tasks
- Background Workers: 2-6 tasks
- Transaction Service: 2-8 tasks

**Deployment Strategy:**
- **Rolling Updates**: Default deployment type
- **Health Checks**: Application-level health endpoints
- **Automatic Rollback**: Revert if health checks fail
- **Blue-Green Option**: Available for critical releases

---

## Rationale

### Primary Drivers

**1. Simpler Operational Overhead**

From DevOps Session 1:
> "Decision 1: ECS over EKS (Kubernetes) - Simpler operational overhead, faster to production, team familiarity"

**Operational Complexity Comparison:**
- **ECS**: Task definitions in JSON, AWS Console UI, familiar AWS concepts
- **EKS**: Kubernetes manifests, kubectl CLI, Helm charts, complex networking, RBAC

**Team Reality:**
- No dedicated DevOps engineer
- Martin Aranda wearing multiple hats (backend, technical lead, infrastructure)
- Limited Kubernetes experience across team
- Focus needed on application development, not infrastructure learning

**Operational Tasks - ECS:**
- Create task definition (JSON)
- Create service
- Configure auto-scaling rules
- Set up load balancer target groups
- Configure CloudWatch alarms

**Operational Tasks - EKS:**
- All of the above, plus:
- Kubernetes cluster management
- Node group configuration and upgrades
- Kubernetes API version management
- CNI plugin configuration
- RBAC policy management
- Helm chart maintenance
- Ingress controller setup and management

**Time Investment:**
- ECS: Days to proficiency
- EKS: Weeks to months to proficiency

**2. Faster to Production**

**Timeline Context:**
- September 4 DevOps session
- Beta launch target: End of September / Early October
- 5-6 weeks to production deployment
- Infrastructure needed ASAP for final testing

**ECS Time to Production:**
- Week 1: Set up ECS clusters, create task definitions
- Week 2: Configure services, set up CI/CD, test deployments
- Week 3: Implement monitoring, alerting, auto-scaling
- Week 4-5: Load testing, optimization, documentation
- Week 6: Production ready with confidence

**EKS Time to Production (Estimated):**
- Week 1: Learn Kubernetes concepts, set up EKS cluster
- Week 2: Configure Kubernetes networking, ingress
- Week 3: Create Kubernetes manifests, learn Helm
- Week 4: Debug Kubernetes-specific issues
- Week 5: Configure monitoring (Prometheus/Grafana or CloudWatch)
- Week 6: Still learning, not production-ready with confidence
- Week 7-8: Maybe ready, but less confidence

**Risk Assessment:**
- ECS: Low risk of timeline slip
- EKS: High risk of timeline slip, debugging delays, knowledge gaps

**3. Team Familiarity with AWS**

**Existing AWS Expertise:**
- Team already using AWS services: RDS, S3, CloudFront, Route 53, ElastiCache
- Familiar with AWS Console, CloudFormation, AWS CLI
- Understand AWS IAM, VPC, Security Groups concepts
- Experience with CloudWatch for monitoring and logging

**ECS Advantages:**
- Builds on existing AWS knowledge
- Native integration with services team already uses
- Same mental models (IAM roles, security groups, VPCs)
- Debugging in familiar CloudWatch interface

**EKS Disadvantages:**
- New paradigm: Kubernetes API and concepts
- Different mental models (pods, deployments, namespaces, etc.)
- Additional complexity layer on top of AWS
- Need to learn both Kubernetes AND how it maps to AWS

**4. Native AWS Integration**

**Seamless Integration with AWS Services:**

**Load Balancing:**
- ECS: Native Application Load Balancer integration (target groups automatically managed)
- EKS: Requires AWS Load Balancer Controller, additional configuration

**Monitoring & Logging:**
- ECS: CloudWatch Logs automatic integration, metrics built-in
- EKS: Need to configure Fluent Bit/Fluentd for logs, metrics require Prometheus or CloudWatch Container Insights

**IAM Integration:**
- ECS: Task roles for fine-grained permissions per service
- EKS: IRSA (IAM Roles for Service Accounts) adds complexity layer

**Service Discovery:**
- ECS: AWS Cloud Map integration
- EKS: CoreDNS + External DNS setup required

**Secrets Management:**
- ECS: Direct integration with Secrets Manager and Parameter Store
- EKS: Requires Secrets Store CSI Driver or external secrets operator

**Cost Management:**
- ECS: Native AWS Cost Explorer, cost allocation tags
- EKS: More complex cost attribution across nodes and pods

**5. Cost Considerations**

**ECS with Fargate:**
- **Control Plane**: Free (AWS manages)
- **Compute**: Pay only for vCPU and memory resources used
- **No EC2 Management**: No idle capacity, no over-provisioning
- **Estimated Monthly Cost**: $800-1,500 for expected load

**EKS:**
- **Control Plane**: $0.10/hour ($73/month per cluster)
- **Worker Nodes**: EC2 instances (need to over-provision for pod scheduling)
- **Management Overhead**: More time spent managing = higher operational cost
- **Estimated Monthly Cost**: $1,200-2,000 for equivalent capacity

**Operational Cost (Staff Time):**
- ECS: 5-10 hours/month management
- EKS: 20-40 hours/month management (learning, troubleshooting, upgrades)

**At $100/hour engineering cost:**
- ECS operational cost: $500-1,000/month
- EKS operational cost: $2,000-4,000/month

**Total Cost of Ownership (Year 1):**
- ECS: ~$15,600-$30,000
- EKS: ~$38,760-$72,000

**6. Sufficient for Requirements**

**Scalability Assessment:**

**Current Needs:**
- 200-2,000 initial users
- ~10 microservices
- Auto-scaling based on CPU/memory
- Multi-AZ high availability

**ECS Capabilities:**
- ✅ Auto-scaling (up to thousands of tasks per service)
- ✅ Multi-AZ deployment
- ✅ Rolling updates and blue-green deployments
- ✅ Health checks and automatic replacement
- ✅ Load balancing across tasks
- ✅ Resource limits and reservation

**Future Growth:**
- 10,000 users: ECS handles easily
- 100,000 users: ECS still viable
- 1,000,000+ users: May need re-evaluation, but years away

**Conclusion:** ECS meets current needs and scales beyond foreseeable requirements. Kubernetes' additional power not needed for trading platform of this scale.

**7. Debugging and Troubleshooting**

**ECS Advantages:**
- CloudWatch Logs: All logs in one familiar interface
- ECS Events: Clear service event stream
- Task Definitions: Simple JSON inspection
- AWS Console: Visual task and service status
- Fewer abstraction layers to debug through

**EKS Challenges:**
- kubectl debugging required
- Multiple log aggregation points (node logs, pod logs, container logs)
- More abstraction layers (pod → deployment → replica set → node)
- Kubernetes-specific errors (ImagePullBackOff, CrashLoopBackOff, etc.)
- Need to understand both Kubernetes AND AWS layers

**3 AM Production Issue Scenario:**
- ECS: Check CloudWatch, view task events, inspect task definition, restart service
- EKS: SSH to node? kubectl describe pod? Check ingress controller? CNI issue? RBAC problem?

With limited Kubernetes expertise, ECS provides more confidence in ability to resolve production issues quickly.

---

## Alternatives Considered

### 1. Amazon EKS (Elastic Kubernetes Service) - REJECTED

**Description:** Managed Kubernetes service on AWS.

**Advantages:**
- Industry-standard Kubernetes API (portability)
- Massive ecosystem (Helm charts, operators, tools)
- Advanced features (custom resource definitions, operators)
- Resume benefit (Kubernetes experience valuable)
- Future-proof (Kubernetes likely dominant long-term)

**Disadvantages:**
- ❌ Steeper learning curve (weeks to months)
- ❌ Higher operational complexity
- ❌ Control plane cost ($73/month)
- ❌ Timeline risk (5-6 weeks to launch insufficient for learning)
- ❌ Team expertise gap
- ❌ More moving parts to debug
- ❌ Over-engineered for current scale

**Why Rejected:** Complexity and learning curve incompatible with 5-6 week timeline to production. Risk of timeline slip and operational issues outweighs future portability benefits.

### 2. ECS with EC2 Launch Type

**Description:** ECS with self-managed EC2 instances instead of Fargate.

**Advantages:**
- Lower per-task cost at scale
- More control over underlying infrastructure
- Can use Reserved Instances for cost savings
- Better performance for I/O-intensive workloads

**Disadvantages:**
- ❌ Need to manage EC2 instances (patching, scaling, availability)
- ❌ Over-provisioning required (always paying for capacity, not usage)
- ❌ Cluster management overhead
- ❌ More complex auto-scaling (both task-level and instance-level)

**Why Rejected:** Operational overhead outweighs cost benefits at current scale. Fargate's serverless model better for small team. Can migrate to EC2 launch type later if cost optimization needed.

### 3. Self-Managed Kubernetes on EC2

**Description:** Deploy Kubernetes ourselves using kubeadm or kops.

**Advantages:**
- No EKS control plane cost
- Maximum control and customization
- Can optimize for specific use cases

**Disadvantages:**
- ❌ All Kubernetes complexity PLUS cluster management
- ❌ Security patching and upgrades on team
- ❌ High availability setup complex
- ❌ No AWS support for control plane issues
- ❌ Massive operational burden

**Why Rejected:** Clearly inferior to both ECS and EKS for small team. Would require dedicated DevOps engineer.

### 4. Docker Swarm

**Description:** Docker's native orchestration solution.

**Advantages:**
- Simpler than Kubernetes
- Built into Docker
- Easier learning curve than Kubernetes

**Disadvantages:**
- ❌ Not well-supported on AWS (no managed service)
- ❌ Smaller ecosystem than Kubernetes or ECS
- ❌ Less mature than alternatives
- ❌ Declining industry adoption
- ❌ Uncertain long-term viability

**Why Rejected:** No AWS managed service, declining industry adoption, inferior to ECS for AWS deployments.

### 5. Nomad (HashiCorp)

**Description:** HashiCorp's orchestration solution.

**Advantages:**
- Simpler than Kubernetes
- Good for mixed workloads (containers, VMs, binaries)
- Integrates with HashiCorp ecosystem (Consul, Vault)

**Disadvantages:**
- ❌ No AWS managed service
- ❌ Smaller ecosystem
- ❌ Team has no HashiCorp expertise
- ❌ Additional vendor relationship
- ❌ Less common in industry (hiring/knowledge sharing)

**Why Rejected:** No managed AWS service, team expertise gap, smaller ecosystem.

### 6. Serverless (Lambda) for All Services

**Description:** Rewrite all services as AWS Lambda functions.

**Advantages:**
- True serverless (zero infrastructure management)
- Pay-per-invocation pricing
- Auto-scaling built-in

**Disadvantages:**
- ❌ Requires rewriting all existing containerized services
- ❌ Lambda limitations (15-minute timeout, cold starts)
- ❌ WebSocket and long-running task challenges
- ❌ Timeline: Months of rewrite work
- ❌ Vendor lock-in (very AWS-specific)

**Why Rejected:** Massive rewrite effort, timeline incompatible, not suitable for all service types (WebSocket server, long-running indexer).

---

## Consequences

### Positive Outcomes

**Operational Simplicity:**
- ✅ Team productive with ECS within days
- ✅ Familiar AWS mental models and tools
- ✅ Fewer abstraction layers to debug
- ✅ Clear documentation and AWS support

**Timeline Success:**
- ✅ Production-ready infrastructure in 4 weeks
- ✅ Beta launched on time (October 17, 2025)
- ✅ No infrastructure-related delays
- ✅ Team focused on application development

**Cost Efficiency:**
- ✅ Lower infrastructure costs ($800-1,500/month vs. $1,200-2,000)
- ✅ Lower operational costs (5-10 hrs/month vs. 20-40 hrs/month)
- ✅ No over-provisioning (Fargate pay-per-use)
- ✅ Total cost of ownership 40-50% lower than EKS

**Integration Benefits:**
- ✅ Seamless ALB, CloudWatch, IAM, Secrets Manager integration
- ✅ Single-vendor simplicity (all AWS)
- ✅ Consistent monitoring and logging
- ✅ Native cost allocation and tracking

**Team Confidence:**
- ✅ High confidence in ability to troubleshoot production issues
- ✅ Can hand off infrastructure to new team members easily
- ✅ Clear operational runbooks
- ✅ Fewer "unknown unknowns"

**Production Stability:**
- ✅ 99.9% uptime achieved at beta launch
- ✅ Auto-scaling working reliably
- ✅ Zero-downtime deployments successful
- ✅ Fast incident response times

### Negative Consequences

**Vendor Lock-in:**
- ⚠️ ECS is AWS-specific (no multi-cloud portability)
- ⚠️ Migrating to Kubernetes later requires work
- ⚠️ Task definitions not compatible with Kubernetes manifests

**Mitigation:**
- Docker containers remain portable
- Can migrate to EKS later if business requires (conversion tools exist)
- For this project, AWS commitment already made (RDS, S3, etc.)
- Multi-cloud not a current or near-future requirement

**Limited Advanced Features:**
- ⚠️ No Kubernetes operators or custom resource definitions
- ⚠️ Smaller ecosystem than Kubernetes
- ⚠️ Some advanced networking features unavailable

**Mitigation:**
- Current requirements fully met by ECS features
- Can extend with custom tooling if needed
- AWS regularly adds ECS features based on customer needs
- If truly need Kubernetes features, migration path exists

**Resume/Hiring Impact:**
- ⚠️ Kubernetes more common on resumes than ECS
- ⚠️ May be harder to hire "Kubernetes engineers"
- ⚠️ Some candidates prefer Kubernetes experience

**Mitigation:**
- Many engineers familiar with both or willing to learn ECS
- ECS simpler = easier to onboard new team members
- AWS experience valuable and in-demand
- Team can learn Kubernetes in parallel if desired

**Ecosystem Size:**
- ⚠️ Fewer third-party tools than Kubernetes
- ⚠️ Smaller community for troubleshooting
- ⚠️ Less Stack Overflow content

**Mitigation:**
- AWS documentation excellent
- AWS support available
- ECS simpler = less need for third-party tools
- Community still active and growing

### Trade-offs Accepted

**Portability vs. Simplicity:**
- Chose simplicity and speed over multi-cloud portability
- Rationale: AWS commitment already deep, multi-cloud not foreseeable requirement

**Ecosystem vs. Time-to-Production:**
- Chose faster production deployment over larger ecosystem
- Rationale: 5-6 week timeline critical, ecosystem size sufficient for current needs

**Industry Standard vs. Operational Efficiency:**
- Chose operational efficiency over Kubernetes resume benefit
- Rationale: Small team, limited DevOps expertise, timeline pressure

**Future Flexibility vs. Current Execution:**
- Chose current execution (beta launch) over future flexibility
- Rationale: Can migrate to EKS later if needed, but must launch beta now

---

## Implementation

### ECS Cluster Setup

**Cluster Configuration:**
```
Production Cluster:
  - Region: us-east-1
  - Launch Type: Fargate
  - Networking: VPC with 3 AZs
  - Container Insights: Enabled
  - Capacity Providers: FARGATE and FARGATE_SPOT
```

**Task Definitions:**
- JSON-based service specifications
- Resource limits: CPU (256-2048 vCPU), Memory (512MB-8GB)
- Health check endpoints: `/health` for each service
- Environment variables from Parameter Store/Secrets Manager
- Logging to CloudWatch Logs with structured JSON format

### Service Configuration

**API Gateway Service:**
```
Desired Count: 2
Min Capacity: 2
Max Capacity: 10
Auto-scaling: Target CPU 70%
Load Balancer: ALB with health checks
Deployment: Rolling update, minimum healthy 100%
```

*Similar configuration for other services with service-specific resource allocations*

### CI/CD Pipeline

**GitHub Actions Workflow:**
1. Run tests on pull request
2. Build Docker image on merge to main
3. Push to Amazon ECR
4. Update ECS task definition
5. Deploy new service revision
6. Monitor health checks
7. Rollback on failure

**Deployment Strategy:**
- Staging: Auto-deploy on merge to develop
- Production: Manual approval after staging validation

### Monitoring & Alerting

**CloudWatch Alarms:**
- CPU utilization > 80% for 5 minutes
- Memory utilization > 85% for 5 minutes
- Error rate > 5% for 2 minutes
- Response time > 2 seconds (p95) for 3 minutes
- Task count < minimum for 1 minute (service down)

**SNS Notifications:**
- Slack integration for alerts
- Email for critical alarms
- PagerDuty escalation for production

**Custom Metrics:**
- Trading volume
- Active users
- Order fill rate
- Indexer lag
- WebSocket connection count

### Auto-Scaling Configuration

**Target Tracking Scaling Policy:**
```
Metric: ECS Service CPU Utilization
Target Value: 70%
Scale-out Cooldown: 120 seconds
Scale-in Cooldown: 300 seconds
```

**Step Scaling (Additional):**
```
CPU > 90%: Add 2 tasks immediately
CPU < 30% for 5 min: Remove 1 task
```

### Disaster Recovery

**Backup Strategy:**
- Task definitions versioned in Git
- ECR images retained (30 days)
- Configuration in Parameter Store backed up to S3
- Multi-AZ deployment for high availability

**Rollback Procedures:**
1. Identify failing task definition version
2. Update service to previous task definition
3. Force new deployment
4. Monitor health checks
5. Document incident for post-mortem

---

## Related Decisions

- **[ADR-500: Multi-AZ Deployment for High Availability](2025-09-04-multi-az-deployment-high-availability.md)** - Complements ECS with multi-AZ strategy
- **[ADR-402: AWS WAF and Encryption Strategy](ADR-402-aws-waf-encryption-strategy.md)** - Security infrastructure integrated with ECS deployment

---

## References

### Source Meetings

**[DevOps Session 1 (2025-09-04)](../06-meetings/2025-09/2025-09-04-devops-session-1.md)**
- Lines 125-130: Key Technical Decisions
  > "Decision 1: ECS over EKS (Kubernetes) - Simpler operational overhead, faster to production, team familiarity"
  > "Decision 2: Multi-AZ deployment for production - High availability at reasonable cost increase"
  > "Decision 3: Blue-green deployment strategy - Zero-downtime deployments with easy rollback"

- Lines 25-38: AWS Infrastructure Architecture
  - ECS selected as container orchestration platform
  - VPC configuration across 3 availability zones
  - Integration with ALB, CloudWatch, Route 53

- Lines 40-67: Deployment Pipeline and Service Orchestration
  - CI/CD workflow using GitHub Actions
  - Docker containerization strategy
  - Service architecture details

- Lines 99-109: Scaling & Performance
  - Auto-scaling configuration targeting 70% CPU
  - Min 2 tasks, max 10 tasks per service
  - Read replicas and connection pooling

### AWS Documentation References

- **ECS Best Practices**: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html
- **Fargate Documentation**: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
- **ECS vs EKS Comparison**: https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/

---

## Notes

### Strategic Context

This decision was made during the critical final stretch before beta launch. The team had 5-6 weeks to finalize production infrastructure, complete final testing, and launch to real users. The decision prioritized **execution over perfection** and **simplicity over sophistication**.

### Team Reality Drove Decision

Key factors that made ECS the right choice:
1. **Small Team**: 11 total members, only Martin as primary DevOps resource
2. **Timeline Pressure**: 5-6 weeks to production, no time for Kubernetes learning curve
3. **Existing AWS Knowledge**: Team already proficient with AWS services
4. **Scale Appropriate**: ECS sufficient for foreseeable growth (years away from outgrowing it)

This is a textbook example of choosing "boring technology" - proven, well-understood, good enough. Kubernetes would have been resume-driven development, not business-driven development.

### Migration Path Exists

If business requirements change (e.g., multi-cloud mandate, need Kubernetes-specific features), migration path exists:
- Containers already portable
- AWS provides tools to convert ECS task definitions to Kubernetes manifests
- Can run hybrid (some services ECS, some EKS) during migration
- Data layer (RDS, S3) unchanged

### Cost-Benefit Was Clear

**Year 1 Savings Estimate:**
- Infrastructure: ~$6,000 saved (ECS cheaper)
- Operational: ~$18,000-36,000 saved (less management time)
- **Total: $24,000-42,000 saved**

**Opportunity Cost:**
- Engineering time saved = features shipped
- Features shipped = faster product-market fit validation
- Faster validation = competitive advantage

The team chose to invest time in product development rather than infrastructure complexity.

### Post-Launch Validation

The October 17, 2025 beta launch successfully validated this decision:
- ✅ Infrastructure ready on time (no delays)
- ✅ 99.9% uptime achieved
- ✅ Auto-scaling working reliably
- ✅ Zero-downtime deployments successful
- ✅ Team confident troubleshooting production issues
- ✅ Costs within budget

No production incidents related to ECS choice. Several deployments executed smoothly. Team able to focus on application bugs, not infrastructure issues.

### Future Considerations

**When to Reconsider EKS:**
1. Multi-cloud requirement emerges (very unlikely for trading platform)
2. Scale exceeds ECS capabilities (100,000+ concurrent users, years away)
3. Need Kubernetes-specific features (custom operators, advanced networking)
4. Team grows dedicated DevOps engineers with Kubernetes expertise
5. Hiring difficulties due to lack of Kubernetes on tech stack

**None of these are foreseeable in next 2-3 years.**

### Lessons Learned

**Key Takeaways:**
1. Choose technology appropriate for team size and expertise
2. Timeline pressure is a real constraint, not to be ignored
3. "Industry standard" doesn't mean "right for us"
4. Operational simplicity has real business value
5. Can always migrate later if needs change (containers are portable)

**Application to Future Decisions:**
- Default to simpler, proven solutions
- Evaluate team expertise honestly
- Consider operational burden, not just feature lists
- Timeline constraints are legitimate decision factors
- Boring technology often the right technology

---

**Decision Status:** ✅ Accepted and Successfully Implemented
**Implementation Date:** September 2025
**Production Launch:** October 17, 2025
**Validation:** 99.9% uptime, zero infrastructure-related incidents
**Review Date:** Annually, or if scale/requirements change significantly

**Success Criteria Met:**
- ✅ Production infrastructure ready by beta launch
- ✅ Team confident operating infrastructure
- ✅ Auto-scaling working reliably
- ✅ Costs within budget
- ✅ Zero-downtime deployments
- ✅ Fast incident response

---

*This ADR documents a pragmatic infrastructure decision prioritizing team capability, timeline constraints, and operational simplicity over industry trends and future-proofing.*
