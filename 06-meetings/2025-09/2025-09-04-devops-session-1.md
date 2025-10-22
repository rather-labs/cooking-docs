---
title: Devops Session 1 - 2025-09-04
type: meeting
meeting_type: technical_deep_dive
topic: DevOps
date: 2025-09-04
attendees: [Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Marcos Tacca]
language: English (translated from Spanish)
translation_note: Spanish content translated to English, technical terms preserved
---

# DevOps Session 1 - Infrastructure & Deployment - Cooking.gg
**Date:** September 4, 2025, 13:59 GMT-03:00
**Duration:** ~30 minutes
**Meeting Type:** Technical Deep Dive - DevOps Infrastructure
**Attendees:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Marcos Tacca

## Executive Summary
First DevOps session focusing on infrastructure setup, AWS architecture, deployment pipelines, and production environment preparation. The team addressed critical deployment concerns including environment configuration, service orchestration, monitoring setup, and rollback strategies.

## Meeting Context
With the beta launch approaching, the team needed to finalize production infrastructure, establish reliable deployment processes, configure monitoring and alerting systems, and ensure all services are properly containerized and scalable for the expected user load.

## Technical Discussion

### AWS Infrastructure Architecture
**Core Services Setup**:
- **ECS (Elastic Container Service)**: Container orchestration for all microservices
- **RDS PostgreSQL**: Primary database for user data, orders, transactions
- **ElastiCache Redis**: Caching layer for session data and frequently accessed queries
- **S3**: Static asset storage (token logos, user uploads)
- **CloudFront**: CDN for global content delivery
- **Route 53**: DNS management and traffic routing

**Network Architecture**:
- **VPC Configuration**: Isolated VPC with public and private subnets across 3 availability zones
- **Security Groups**: Restrictive inbound rules, only necessary ports exposed
- **Load Balancer**: Application Load Balancer for distributing traffic across ECS tasks
- **NAT Gateway**: Outbound internet access for private subnet resources

### Deployment Pipeline
**CI/CD Workflow**:
1. **Code Commit**: Push to GitHub triggers CI/CD pipeline
2. **Build Stage**: GitHub Actions builds Docker images
3. **Test Stage**: Run unit tests, integration tests, linting
4. **Image Push**: Push Docker images to Amazon ECR (Elastic Container Registry)
5. **Deploy Stage**: Update ECS service with new task definition
6. **Health Check**: Verify new tasks healthy before terminating old tasks
7. **Rollback**: Automatic rollback if health checks fail

**Environment Strategy**:
- **Development**: Local Docker Compose for individual developer environments
- **Staging**: AWS staging environment mirroring production architecture
- **Production**: Full production setup with autoscaling and high availability

### Containerization & Service Configuration
**Docker Setup**:
- All services containerized with optimized multi-stage builds
- Base images pinned to specific versions for reproducibility
- Health check endpoints implemented in each service
- Resource limits defined (CPU, memory) for each container

**Service Orchestration**:
- **API Gateway**: Entry point for all client requests
- **Trading Engine**: Handles order execution and routing
- **Indexer Service**: Processes blockchain data and updates database
- **WebSocket Server**: Maintains real-time connections for price feeds
- **Background Workers**: Process async tasks (email, notifications, data aggregation)

### Environment Variables & Secrets Management
**Configuration Management**:
- **AWS Systems Manager Parameter Store**: Secure storage for configuration values
- **AWS Secrets Manager**: Encrypted storage for sensitive data (API keys, DB passwords)
- **Environment-Specific Configs**: Separate parameter namespaces per environment
- **Automatic Rotation**: Database credentials rotated monthly

**Critical Environment Variables**:
- Database connection strings
- RPC endpoints (Solana, Hyperliquid)
- API keys (Jupiter, Echo, TradingView)
- JWT signing keys
- CORS allowed origins
- Rate limiting thresholds

### Monitoring & Logging
**Logging Strategy**:
- **CloudWatch Logs**: Centralized log aggregation from all ECS tasks
- **Structured Logging**: JSON format for easy parsing and searching
- **Log Retention**: 30 days for application logs, 90 days for audit logs
- **Log Levels**: DEBUG in staging, INFO in production, ERROR alerts

**Monitoring & Alerting**:
- **CloudWatch Metrics**: Track CPU, memory, request count, error rate, latency
- **Custom Metrics**: Trading volume, active users, order fill rate, indexer lag
- **Alarms**: Set up alerts for critical thresholds (error rate > 5%, latency > 2s)
- **SNS Notifications**: Send alerts to Slack and email
- **Dashboard**: Real-time dashboard showing key system metrics

### Scaling & Performance
**Auto-Scaling Configuration**:
- **Target Tracking**: Scale based on CPU utilization (target: 70%)
- **Min/Max Tasks**: Minimum 2 tasks per service, maximum 10
- **Scale-Out**: Add tasks when CPU > 70% for 2 minutes
- **Scale-In**: Remove tasks when CPU < 30% for 5 minutes

**Database Scaling**:
- **Read Replicas**: 2 read replicas for query load distribution
- **Connection Pooling**: PgBouncer for efficient connection management
- **Query Optimization**: Indexes on all frequently queried columns
- **Caching**: Redis caching for expensive queries

### Backup & Disaster Recovery
**Backup Strategy**:
- **Database**: Automated daily snapshots, retained for 7 days
- **S3**: Versioning enabled, cross-region replication
- **Configuration**: Parameter Store values backed up to S3 weekly
- **Recovery Time Objective (RTO)**: < 4 hours
- **Recovery Point Objective (RPO)**: < 15 minutes

**Disaster Recovery Plan**:
- Regular DR drills quarterly
- Documented runbooks for common failure scenarios
- Automated failover for database using Multi-AZ deployment
- Cross-region backup for catastrophic regional failure

## Key Technical Decisions
- **Decision 1:** ECS over EKS (Kubernetes) - Simpler operational overhead, faster to production, team familiarity
- **Decision 2:** Multi-AZ deployment for production - High availability at reasonable cost increase
- **Decision 3:** Blue-green deployment strategy - Zero-downtime deployments with easy rollback
- **Decision 4:** CloudWatch over third-party monitoring - Cost-effective, native AWS integration
- **Decision 5:** Secrets Manager for all sensitive data - Enhanced security with automatic rotation

## Action Items
- [ ] **Eduardo**: Finalize ECS task definitions with resource limits and health checks
- [ ] **Martin**: Set up GitHub Actions workflows for CI/CD pipeline
- [ ] **Marcos**: Configure CloudWatch alarms and SNS notifications to Slack
- [ ] **Team**: Document deployment runbook and rollback procedures
- [ ] **Eduardo**: Set up database backup verification and restoration testing
- [ ] **Martin**: Implement structured logging across all services

## Follow-up Items
- Schedule disaster recovery drill for next month
- Evaluate cost optimization opportunities (Reserved Instances, Savings Plans)
- Plan for implementing blue-green deployment
- Set up performance testing environment for load testing

## Technical References
- AWS ECS Best Practices: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html
- Docker Multi-Stage Builds: https://docs.docker.com/build/building/multi-stage/
- CloudWatch Logs Insights: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html

---
**Recording:** Transcription available
**Related Documents:**
- AWS Infrastructure Diagram (to be created)
- Deployment Runbook (to be created)
