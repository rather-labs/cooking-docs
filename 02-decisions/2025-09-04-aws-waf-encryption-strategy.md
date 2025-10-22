---
title: AWS WAF and Encryption Strategy
type: decision-record
decision-id: ADR-402
date: 2025-09-04
status: accepted
owner: Marcos Tacca, Martin Aranda, Eduardo Yuschuk
stakeholders: [Marcos Tacca, Martin Aranda, Eduardo Yuschuk, Lucas Cufre, DevOps Team]
tags: [security, aws, waf, encryption, ddos, compliance, infrastructure]
summary: |
  Decision to implement AWS WAF (Web Application Firewall) with managed rule sets for DDoS protection and common attack prevention, combined with comprehensive encryption strategy covering data at rest (RDS, S3) and in transit (TLS 1.2+). Implementation includes rate limiting, geo-blocking capabilities, CloudFront Shield for DDoS protection, and AWS KMS for encryption key management. Cost-effective security hardening before production launch.
related-docs:
  - ../06-meetings/2025-09/2025-09-04-devops-session-2.md
  - ADR-500: Multi-AZ Deployment for High Availability
---

# AWS WAF and Encryption Strategy

## Context and Problem Statement

Cooking.gg is a financial trading platform handling sensitive user data and financial transactions on Solana blockchain. Before production launch, the platform must implement security hardening to protect against:

**Web Application Attacks:**

1. **DDoS (Distributed Denial of Service):**
   - Attacker floods platform with traffic
   - Legitimate users cannot access platform
   - Trading operations unavailable
   - **Impact:** Revenue loss, user frustration, reputation damage

2. **SQL Injection:**
   - Attacker injects malicious SQL into API parameters
   - Gains unauthorized database access
   - Steals user data, manipulates trades
   - **Impact:** Data breach, financial loss, regulatory fines

3. **XSS (Cross-Site Scripting):**
   - Attacker injects malicious JavaScript into user-facing pages
   - Steals session tokens, executes unauthorized actions
   - **Impact:** Account takeover, unauthorized trades

4. **Rate Abuse:**
   - Attacker hammers API endpoints
   - Exhausts server resources, increases costs
   - Legitimate requests denied
   - **Impact:** Degraded performance, increased AWS bills

5. **Bot Attacks:**
   - Automated bots scraping token data
   - Credential stuffing attacks (stolen passwords)
   - **Impact:** Data theft, account takeover, resource waste

**Data Security Requirements:**

1. **Data at Rest:**
   - User credentials (hashed passwords, security passwords)
   - Wallet private keys (encrypted)
   - Transaction history
   - Personal information (email, profile)
   - **Requirement:** Encryption to prevent data leaks from storage compromise

2. **Data in Transit:**
   - API requests/responses (user data, trades)
   - Database connections (application → RDS)
   - Internal service communication (microservices)
   - **Requirement:** TLS encryption to prevent man-in-the-middle attacks

3. **Sensitive Application Data:**
   - Turnkey wallet private keys
   - Third-party API keys (Jupiter, Auth0, etc.)
   - Database credentials
   - **Requirement:** Encrypted storage with strict access control

**Regulatory and Compliance:**

- **GDPR:** Data protection requirements (encryption, access control)
- **Financial Services:** Industry best practices for handling financial data
- **App Store Requirements:** Apple/Google security guidelines for financial apps

**Current State (Pre-Production):**

- **No WAF:** APIs publicly exposed, no attack protection
- **Encryption:** Partial (HTTPS for API, but not RDS/S3)
- **Rate Limiting:** Application-level only (can be bypassed)
- **DDoS Protection:** None (CloudFront without Shield)
- **Risk:** Vulnerable to common attacks, potential data breach

**Production Readiness Requirements:**

1. **Web Application Firewall:** Block common attacks (SQL injection, XSS)
2. **DDoS Protection:** Handle traffic spikes, prevent service disruption
3. **Encryption at Rest:** All data stores encrypted
4. **Encryption in Transit:** TLS 1.2+ for all connections
5. **Rate Limiting:** Multi-layer protection (WAF + application)
6. **Access Control:** Principle of least privilege (IAM roles)
7. **Key Management:** Secure encryption key storage (AWS KMS)

## Decision

**Implement AWS WAF with managed rule sets for web application protection, CloudFront Shield for DDoS mitigation, comprehensive encryption at rest (RDS, S3) and in transit (TLS 1.2+), and AWS KMS for centralized encryption key management.**

### Implementation Architecture

```
                                    Internet
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│                      AWS CloudFront (CDN)                    │
│  - SSL/TLS Termination (ACM Certificate)                     │
│  - HSTS Headers (Force HTTPS)                                │
│  - DDoS Protection (CloudFront Shield - Basic)               │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                       AWS WAF                                │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Managed Rule Sets:                                     │ │
│  │ - AWS Core Rule Set (OWASP Top 10)                    │ │
│  │ - Known Bad Inputs (SQL injection, XSS)               │ │
│  │ - Rate-Based Rule (100 req/5min per IP)               │ │
│  │ - Geo-Blocking (optional - sanctioned countries)      │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  Custom Rules:                                               │
│  - Block suspicious user agents                             │
│  - Rate limit API endpoints                                 │
│  - Whitelist legitimate IPs (office, monitoring)            │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                  Application Load Balancer (ALB)             │
│  - HTTPS Listener (Port 443)                                 │
│  - HTTP → HTTPS Redirect (Port 80)                           │
│  - Health Checks                                             │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│                    ECS Services (Containers)                 │
│  - Backend API (NestJS)                                      │
│  - Transaction Microservice                                  │
│  - Indexer Services                                          │
│                                                              │
│  Encryption in Transit:                                      │
│  - TLS 1.2+ for all external connections                    │
│  - Encrypted DB connections (RDS SSL)                        │
│  - HTTPS for third-party APIs                               │
└────────────┬──────────────────────────┬──────────────────────┘
             │                          │
             ▼                          ▼
┌─────────────────────────┐   ┌─────────────────────────────┐
│   Amazon RDS            │   │    Amazon S3                │
│   (PostgreSQL)          │   │    (Static Assets)          │
│                         │   │                             │
│ Encryption at Rest:     │   │ Encryption at Rest:         │
│ - AES-256 encryption    │   │ - SSE-S3 (AES-256)          │
│ - AWS KMS managed keys  │   │ - Bucket encryption default │
│ - Automated backups     │   │ - Versioning enabled        │
│   encrypted             │   │                             │
└─────────────────────────┘   └─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────────────────────┐
│                    AWS KMS (Key Management)                  │
│  - Master encryption keys                                    │
│  - Automatic key rotation                                    │
│  - Access logging and auditing                               │
│  - IAM policy enforcement                                    │
└──────────────────────────────────────────────────────────────┘
```

### AWS WAF Configuration

**Managed Rule Sets:**

AWS WAF provides pre-configured rule sets maintained by AWS security team:

```terraform
# Terraform configuration for AWS WAF
resource "aws_wafv2_web_acl" "cooking_waf" {
  name  = "cooking-production-waf"
  scope = "CLOUDFRONT"

  default_action {
    allow {}
  }

  # AWS Managed Rule: Core Rule Set (CRS)
  rule {
    name     = "AWSManagedRulesCommonRuleSet"
    priority = 1

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesCommonRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "AWSManagedRulesCommonRuleSetMetric"
      sampled_requests_enabled   = true
    }
  }

  # AWS Managed Rule: Known Bad Inputs
  rule {
    name     = "AWSManagedRulesKnownBadInputsRuleSet"
    priority = 2

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesKnownBadInputsRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "AWSManagedRulesKnownBadInputsMetric"
      sampled_requests_enabled   = true
    }
  }

  # Rate-Based Rule: Block IPs exceeding 100 requests per 5 minutes
  rule {
    name     = "RateLimitRule"
    priority = 3

    action {
      block {}
    }

    statement {
      rate_based_statement {
        limit              = 100
        aggregate_key_type = "IP"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "RateLimitRuleMetric"
      sampled_requests_enabled   = true
    }
  }

  # Geo-Blocking (Optional): Block sanctioned countries
  rule {
    name     = "GeoBlockingRule"
    priority = 4

    action {
      block {}
    }

    statement {
      geo_match_statement {
        country_codes = ["KP", "IR", "SY"]  # North Korea, Iran, Syria
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "GeoBlockingRuleMetric"
      sampled_requests_enabled   = true
    }
  }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "CookingWAFMetric"
    sampled_requests_enabled   = true
  }
}
```

**What These Rules Protect Against:**

1. **Core Rule Set (CRS):**
   - SQL injection attacks
   - Cross-site scripting (XSS)
   - Local file inclusion (LFI)
   - Remote file inclusion (RFI)
   - Remote code execution (RCE)
   - HTTP protocol violations

2. **Known Bad Inputs:**
   - Log4j vulnerability (CVE-2021-44228)
   - Common attack patterns
   - Malformed requests

3. **Rate Limiting:**
   - DDoS mitigation (per-IP limit)
   - Credential stuffing prevention
   - API abuse prevention

4. **Geo-Blocking:**
   - Compliance with sanctions
   - Reduce attack surface (block high-risk regions)

### CloudFront Shield (DDoS Protection)

**Basic Shield (Included with CloudFront):**

Free DDoS protection automatically enabled:

- **Layer 3/4 Protection:** SYN floods, UDP floods, reflection attacks
- **Automatic Mitigation:** AWS detects and mitigates attacks automatically
- **No Configuration Required:** Always-on protection

**Shield Advanced (Optional):**

For higher-value targets, Shield Advanced provides:

- **Cost Protection:** Refunds for scaling costs during DDoS attacks
- **24/7 DDoS Response Team:** Expert support during attacks
- **Advanced Attack Analytics:** Real-time visibility into attacks
- **Cost:** $3,000/month

**Decision:** Start with Basic Shield, evaluate Advanced if attacked.

### Encryption at Rest

**Amazon RDS (PostgreSQL):**

```terraform
resource "aws_db_instance" "cooking_db" {
  identifier           = "cooking-production"
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.r6g.xlarge"
  allocated_storage    = 500

  # Encryption at rest
  storage_encrypted = true
  kms_key_id        = aws_kms_key.rds_key.arn

  # Automated backups (also encrypted)
  backup_retention_period = 7
  backup_window           = "03:00-04:00"

  # Enable encryption in transit
  enabled_cloudwatch_logs_exports = ["postgresql"]
}

# KMS key for RDS encryption
resource "aws_kms_key" "rds_key" {
  description             = "KMS key for RDS encryption"
  deletion_window_in_days = 30
  enable_key_rotation     = true
}
```

**Amazon S3 (Static Assets, Backups):**

```terraform
resource "aws_s3_bucket" "cooking_assets" {
  bucket = "cooking-production-assets"
}

# Enable default encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "cooking_assets" {
  bucket = aws_s3_bucket.cooking_assets.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"  # SSE-S3 (AWS-managed keys)
    }
  }
}

# Enable versioning (protect against accidental deletion)
resource "aws_s3_bucket_versioning" "cooking_assets" {
  bucket = aws_s3_bucket.cooking_assets.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Block public access
resource "aws_s3_bucket_public_access_block" "cooking_assets" {
  bucket = aws_s3_bucket.cooking_assets.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

**ElastiCache Redis:**

```terraform
resource "aws_elasticache_replication_group" "cooking_redis" {
  replication_group_id       = "cooking-redis"
  replication_group_description = "Redis for block storage"

  engine         = "redis"
  engine_version = "7.0"
  node_type      = "cache.r6g.xlarge"

  # Encryption at rest
  at_rest_encryption_enabled = true
  kms_key_id                 = aws_kms_key.redis_key.arn

  # Encryption in transit
  transit_encryption_enabled = true
  auth_token                 = var.redis_auth_token

  # Snapshots (also encrypted)
  snapshot_retention_limit = 7
  snapshot_window          = "03:00-05:00"
}
```

**ClickHouse:**

ClickHouse encryption handled at disk level (AWS EBS volume encryption):

```terraform
resource "aws_instance" "clickhouse" {
  ami           = var.clickhouse_ami
  instance_type = "r6g.4xlarge"

  # Encrypted EBS volumes
  root_block_device {
    encrypted   = true
    kms_key_id  = aws_kms_key.clickhouse_key.arn
    volume_size = 500
    volume_type = "gp3"
  }
}
```

### Encryption in Transit

**TLS Configuration:**

```nginx
# NGINX configuration (within ECS containers)
server {
    listen 443 ssl http2;
    server_name api.cooking.gg;

    # SSL Certificate (from ACM)
    ssl_certificate     /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    # TLS Protocol (TLS 1.2+, disable older versions)
    ssl_protocols TLSv1.2 TLSv1.3;

    # Strong Cipher Suites
    ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers on;

    # HSTS (Force HTTPS for 1 year)
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    # Additional security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    location / {
        proxy_pass http://backend:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

# HTTP → HTTPS Redirect
server {
    listen 80;
    server_name api.cooking.gg;

    return 301 https://$server_name$request_uri;
}
```

**Database Connections (TLS Enforced):**

```javascript
// PostgreSQL connection with SSL
import { Client } from 'pg';

const client = new Client({
  host: process.env.DB_HOST,
  port: 5432,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  ssl: {
    rejectUnauthorized: true,  // Verify server certificate
    ca: fs.readFileSync('/path/to/rds-ca-bundle.pem')
  }
});
```

**Third-Party API Calls (HTTPS):**

```javascript
// All third-party API calls use HTTPS
import axios from 'axios';

const jupiterApi = axios.create({
  baseURL: 'https://quote-api.jup.ag',  // HTTPS only
  timeout: 5000,
  headers: { 'Accept': 'application/json' }
});

const auth0Api = axios.create({
  baseURL: 'https://cooking.auth0.com',  // HTTPS only
  timeout: 10000
});
```

### AWS KMS (Key Management Service)

**Centralized Key Management:**

```terraform
# Master encryption key for application
resource "aws_kms_key" "app_master_key" {
  description             = "Master encryption key for Cooking.gg application"
  deletion_window_in_days = 30
  enable_key_rotation     = true  # Automatic annual rotation

  tags = {
    Name        = "cooking-app-master-key"
    Environment = "production"
  }
}

# Alias for easier reference
resource "aws_kms_alias" "app_master_key" {
  name          = "alias/cooking-app-master"
  target_key_id = aws_kms_key.app_master_key.key_id
}

# IAM policy: Allow ECS tasks to use key
resource "aws_kms_key_policy" "app_master_key" {
  key_id = aws_kms_key.app_master_key.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root"
        }
        Action   = "kms:*"
        Resource = "*"
      },
      {
        Sid    = "Allow ECS tasks to decrypt"
        Effect = "Allow"
        Principal = {
          AWS = aws_iam_role.ecs_task_execution.arn
        }
        Action = [
          "kms:Decrypt",
          "kms:DescribeKey"
        ]
        Resource = "*"
      }
    ]
  })
}
```

**Encrypt Sensitive Application Secrets:**

```javascript
// Encrypt Turnkey private key before storing
import { KMSClient, EncryptCommand, DecryptCommand } from "@aws-sdk/client-kms";

const kms = new KMSClient({ region: "us-east-1" });

async function encryptPrivateKey(privateKey) {
  const command = new EncryptCommand({
    KeyId: "alias/cooking-app-master",
    Plaintext: Buffer.from(privateKey)
  });

  const response = await kms.send(command);
  return response.CiphertextBlob.toString('base64');
}

async function decryptPrivateKey(encryptedKey) {
  const command = new DecryptCommand({
    CiphertextBlob: Buffer.from(encryptedKey, 'base64')
  });

  const response = await kms.send(command);
  return response.Plaintext.toString('utf-8');
}
```

### Rate Limiting (Multi-Layer)

**Layer 1: WAF Rate Limiting (Perimeter)**

```terraform
# Already configured in WAF (100 requests per 5 minutes per IP)
```

**Layer 2: API Gateway Rate Limiting**

```terraform
resource "aws_api_gateway_usage_plan" "cooking_api" {
  name = "cooking-api-usage-plan"

  throttle_settings {
    burst_limit = 200   # Max concurrent requests
    rate_limit  = 100   # Requests per second
  }

  quota_settings {
    limit  = 10000  # Requests per day
    period = "DAY"
  }
}
```

**Layer 3: Application-Level Rate Limiting**

```javascript
// Express.js rate limiting per endpoint
import rateLimit from 'express-rate-limit';

// General API rate limit
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  message: 'Too many requests from this IP, please try again later.'
});

app.use('/api/', apiLimiter);

// Stricter limit for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5, // 5 login attempts per 15 minutes
  message: 'Too many login attempts, please try again later.'
});

app.use('/api/auth/login', authLimiter);

// Strict limit for trading
const tradeLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 10, // 10 trades per minute
  message: 'Trading rate limit exceeded, please slow down.'
});

app.use('/api/trades', tradeLimiter);
```

### Access Control (IAM Principle of Least Privilege)

**ECS Task IAM Role (Minimal Permissions):**

```terraform
resource "aws_iam_role" "ecs_task_execution" {
  name = "cooking-ecs-task-execution"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
        Effect = "Allow"
      }
    ]
  })
}

# Policy: Only permissions needed for task operation
resource "aws_iam_role_policy" "ecs_task_policy" {
  role = aws_iam_role.ecs_task_execution.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "kms:Decrypt",
          "kms:DescribeKey"
        ]
        Resource = aws_kms_key.app_master_key.arn
      },
      {
        Effect = "Allow"
        Action = [
          "secretsmanager:GetSecretValue"
        ]
        Resource = "arn:aws:secretsmanager:us-east-1:*:secret:cooking/*"
      },
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject"
        ]
        Resource = "arn:aws:s3:::cooking-production-assets/*"
      }
    ]
  })
}
```

**Database User Permissions (Least Privilege):**

```sql
-- Application database user (read/write to application tables only)
CREATE USER app_user WITH PASSWORD 'strong_password';
GRANT CONNECT ON DATABASE cooking_db TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- Read-only analytics user
CREATE USER analytics_user WITH PASSWORD 'strong_password';
GRANT CONNECT ON DATABASE cooking_db TO analytics_user;
GRANT USAGE ON SCHEMA public TO analytics_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analytics_user;

-- Admin user (schema changes, backups)
CREATE USER admin_user WITH PASSWORD 'strong_password';
GRANT ALL PRIVILEGES ON DATABASE cooking_db TO admin_user;
```

### Monitoring and Alerts

**CloudWatch Alarms:**

```terraform
# WAF blocked requests (potential attack)
resource "aws_cloudwatch_metric_alarm" "waf_blocked_requests" {
  alarm_name          = "cooking-waf-blocked-requests-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "BlockedRequests"
  namespace           = "AWS/WAFV2"
  period              = "300"  # 5 minutes
  statistic           = "Sum"
  threshold           = "100"  # > 100 blocked requests in 5 min

  alarm_description = "High number of WAF blocked requests (potential attack)"
  alarm_actions     = [aws_sns_topic.alerts.arn]
}

# DDoS detected
resource "aws_cloudwatch_metric_alarm" "ddos_attack" {
  alarm_name          = "cooking-ddos-detected"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "DDoSDetected"
  namespace           = "AWS/DDoSProtection"
  period              = "60"
  statistic           = "Sum"
  threshold           = "1"

  alarm_description = "DDoS attack detected by Shield"
  alarm_actions     = [aws_sns_topic.alerts.arn]
}
```

## Rationale

### WAF Cost-Benefit Analysis

**AWS WAF Pricing:**

- **Web ACL:** $5/month
- **Rule:** $1/month per rule (4 rules = $4/month)
- **Requests:** $0.60 per million requests

**Monthly Cost Estimate:**

- Web ACL: $5
- Rules (4): $4
- Requests (100M/month): $60
- **Total: ~$69/month**

**Alternative: No WAF**

- **Cost:** $0
- **Risk:** SQL injection, XSS, DDoS → data breach, service outage
- **Potential Loss:**
  - Data breach fine: $50,000-$500,000 (GDPR, regulatory)
  - Revenue loss during outage: $10,000/day
  - Reputation damage: immeasurable
  - Customer churn: 20-30% after breach

**ROI:** $69/month insurance against $50k+ potential loss = obvious choice.

### Encryption Cost-Benefit

**Encryption Overhead:**

- **RDS:** Minimal performance impact (~3-5%)
- **S3:** No performance impact (transparent encryption)
- **KMS:** $1/month per key + $0.03 per 10,000 requests
- **Cost:** ~$10/month total

**Benefits:**

- **Compliance:** GDPR, financial regulations require encryption
- **Data Breach Protection:** Even if attacker gains disk access, data encrypted
- **Customer Trust:** Industry standard for financial platforms

**No-Brainer:** $10/month for regulatory compliance and data protection.

### CloudFront Shield (Basic vs Advanced)

**Basic Shield:**

- **Cost:** Free (included with CloudFront)
- **Protection:** Layer 3/4 DDoS (SYN floods, UDP floods)
- **Sufficient For:** Small-to-medium sites (<10Gbps attacks)

**Shield Advanced:**

- **Cost:** $3,000/month
- **Protection:** Layer 3/4 + Layer 7 (application-layer) DDoS
- **Benefits:** Cost protection, DDoS Response Team, advanced analytics
- **Justification:** High-value targets (large financial platforms)

**Decision:** Start with Basic Shield. Evaluate Advanced if:
- Revenue > $100k/month (justify cost)
- Experiencing frequent DDoS attacks
- Downtime cost > $3k/month

## Consequences

### Positive

**Security Hardening:**
- WAF blocks common attacks (SQL injection, XSS, DDoS)
- Encryption protects data at rest and in transit
- Rate limiting prevents API abuse
- KMS provides centralized key management

**Compliance & Trust:**
- Meets GDPR encryption requirements
- Industry best practices for financial platforms
- App Store approval (security guidelines met)
- Customer confidence (professional security posture)

**Cost-Effective:**
- WAF: ~$69/month (minimal cost for protection)
- Encryption: ~$10/month (compliance requirement)
- Shield Basic: Free (DDoS protection included)
- **Total: ~$79/month for enterprise-grade security**

**Operational Benefits:**
- Automatic attack mitigation (no manual intervention)
- CloudWatch alerts for security events
- Centralized logging (WAF, CloudTrail)
- Easy compliance audits (encryption enabled by default)

### Negative

**Implementation Complexity:**
- Terraform configuration for WAF, KMS, encryption
- Testing WAF rules (false positives possible)
- Rotation of encryption keys (automated but requires monitoring)
- IAM policy management (least privilege requires careful design)

**Performance Overhead:**
- WAF adds ~5-10ms latency per request (negligible)
- Encryption adds ~3-5% CPU overhead (minimal)
- TLS handshake adds ~50-100ms (first request only)
- **Overall impact: <50ms, acceptable for API**

**Potential False Positives:**
- WAF may block legitimate requests (overly aggressive rules)
- Requires tuning and monitoring
- Whitelist legitimate traffic patterns

**Cost at Scale:**
- WAF costs grow with request volume ($0.60 per million requests)
- At 1 billion requests/month: $600/month (still reasonable)
- Shield Advanced ($3k/month) may be needed for large scale

**Maintenance Burden:**
- Monitor WAF metrics (blocked requests, false positives)
- Rotate KMS keys (automated but requires validation)
- Update TLS certificates (ACM handles automatically, but verify)
- Regular security audits

### Neutral

**Trade-offs:**
- Security vs performance (encryption overhead acceptable)
- Cost vs protection (WAF cost justified by risk reduction)
- Flexibility vs security (strict IAM policies require more configuration)

## Alternatives Considered

### Option 1: No WAF (Rely on Application-Level Security Only)

**Description:** Implement security at application level (input validation, rate limiting)

**Pros:**
- No WAF cost ($0/month)
- Simpler infrastructure (no WAF configuration)

**Cons:**
- Vulnerable to DDoS (application overwhelmed before processing)
- No Layer 7 attack protection (SQL injection can bypass app validation)
- Single point of failure (if app compromised, no perimeter defense)

**Why Rejected:** Unacceptable risk for financial platform. WAF provides defense-in-depth.

### Option 2: Third-Party WAF (Cloudflare, Imperva)

**Description:** Use Cloudflare or Imperva instead of AWS WAF

**Pros:**
- More advanced features (bot detection, image optimization)
- Global CDN (faster than CloudFront in some regions)

**Cons:**
- Additional vendor dependency (platform lock-in)
- Higher cost (Cloudflare Pro: $20/month + usage, Imperva: $$$)
- Data flows through third party (privacy concerns)
- Integration complexity (route traffic through Cloudflare)

**Why Rejected:** AWS WAF integrates natively with CloudFront, simpler architecture. Sufficient for current needs.

### Option 3: No Encryption at Rest

**Description:** Only encrypt data in transit (HTTPS), skip RDS/S3 encryption

**Pros:**
- Slightly lower cost (~$10/month saved)
- No encryption overhead (~3-5% CPU)

**Cons:**
- **Regulatory Non-Compliance:** GDPR requires encryption at rest
- **Data Breach Risk:** If attacker gains disk access, data exposed
- **Reputational Damage:** Financial platform without encryption = red flag

**Why Rejected:** Encryption at rest is industry standard for financial apps. Non-compliance unacceptable.

### Option 4: Shield Advanced from Day One

**Description:** Subscribe to Shield Advanced ($3k/month) immediately

**Pros:**
- Maximum DDoS protection
- Cost protection (AWS refunds scaling costs during attacks)
- 24/7 DDoS Response Team

**Cons:**
- Expensive ($36k/year)
- Overkill for launch (low traffic initially)
- Can upgrade later if needed

**Why Rejected:** Start with Shield Basic (free). Upgrade to Advanced if experiencing attacks or revenue justifies cost.

## Implementation Notes

### Production Readiness Checklist

- [x] WAF configured with managed rule sets
- [x] RDS encryption enabled
- [x] S3 bucket encryption enabled
- [x] ElastiCache Redis encryption enabled
- [x] TLS 1.2+ enforced for all connections
- [x] KMS keys created for encryption
- [x] IAM roles follow least privilege
- [x] Rate limiting configured (WAF + application)
- [x] CloudWatch alarms set up
- [x] HTTP → HTTPS redirect configured

### Testing Strategy

**WAF Testing:**

```bash
# Test SQL injection blocked
curl -X POST https://api.cooking.gg/api/users \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "name": "Robert'); DROP TABLE users;--"}'

# Expected: 403 Forbidden (WAF blocked)

# Test XSS blocked
curl https://api.cooking.gg/api/search?q=<script>alert('XSS')</script>

# Expected: 403 Forbidden (WAF blocked)

# Test rate limiting
for i in {1..150}; do
  curl https://api.cooking.gg/api/health
done

# Expected: First 100 succeed, remaining 50 blocked
```

**Encryption Validation:**

```sql
-- Verify RDS encryption enabled
SELECT encrypted FROM aws_describe_db_instances WHERE db_instance_identifier = 'cooking-production';

-- Expected: encrypted = true
```

```bash
# Verify S3 encryption
aws s3api get-bucket-encryption --bucket cooking-production-assets

# Expected: SSE-S3 enabled
```

### Rollback Plan

If WAF causes issues (false positives blocking legitimate traffic):

1. **Temporary:** Set WAF to count mode (log violations, don't block)
2. **Investigate:** Review CloudWatch Logs for false positives
3. **Tune Rules:** Add exceptions for legitimate traffic patterns
4. **Re-enable:** Switch back to block mode after tuning

```terraform
# WAF in count mode (logging only)
rule {
  name     = "AWSManagedRulesCommonRuleSet"
  priority = 1

  override_action {
    count {}  # Count violations instead of blocking
  }

  # ... rest of configuration
}
```

## References

### Meeting Notes
- [DevOps Session 2 - Security & Production Readiness 2025-09-04](../06-meetings/2025-09/2025-09-04-devops-session-2.md) - WAF and encryption strategy decisions

### Related Decisions
- ADR-500: Multi-AZ Deployment for High Availability (infrastructure resilience)

### Technical References
- AWS WAF Documentation: https://docs.aws.amazon.com/waf/
- AWS Shield: https://aws.amazon.com/shield/
- AWS KMS: https://docs.aws.amazon.com/kms/
- RDS Encryption: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html
- S3 Encryption: https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html
- TLS Best Practices: https://wiki.mozilla.org/Security/Server_Side_TLS

### Security Standards
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- AWS Security Best Practices: https://docs.aws.amazon.com/security/
- NIST Encryption Standards: https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines

## Revision History
- 2025-09-04: WAF and encryption strategy decision made
- 2025-09-04: AWS WAF with managed rule sets selected
- 2025-09-04: Encryption at rest enabled for all data stores
- 2025-10-21: Formal ADR documented from meeting notes
