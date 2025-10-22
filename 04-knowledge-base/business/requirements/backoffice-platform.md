---
title: Cooking Backoffice Platform
type: feature-specification
status: in-development
priority: high
created: 2025-04-17
date: 2025-10-20
updated: 2025-10-20
tags: [backoffice, admin-panel, analytics, support, user-management]
related:
  - "[[platform-vision-requirements]]"
  - "[[beta-release-q3-2025]]"
---

# Cooking Backoffice Platform

## Overview

Originally called an Admin Panel, the Backoffice should work as a hub where internal Cooking users can gather business and operational information as well as take action and provide support for end-users.

## Product Definition

> The platform's goal is to provide visibility into user/token/order activity, support fee configuration, and assist in resolving user-related issues.

## User Roles

We've identified two main user roles with access separation and strict security protocols as top priorities:

- **Business Role**: Analytics, reporting, fee management
- **Support Role**: User assistance, ticket management, issue resolution

## Product Scope

Features are listed in order of perceived importance:

### 1. Environment Development and Auth

- Development of a test and production environment
- Implementation of authentication methodology
- Research and implementation of either 2FA or Passkey security layer

### 2. Backoffice User Management

- **[BO] User Creation**: Create new backoffice users
- **[BO] User Deletion**: Remove backoffice users
- **[BO] User Edit**:
  - Change Role
  - Credential Reset
- **Role System**: Implement access separation by role

### 3. Fee Management - Basic

- Edit Fee at Platform Level
- Edit Fee at Order Level
- Edit Fee at Token Level

### 4. Platform Analytics

Implementation of [Amplitude](https://amplitude.com/) as Analytics tool ([Product Documentation](https://amplitude.com/docs?siteLocation=footer))

**Metrics to Track**:

- **User Metrics**:
  - DAU (Daily Active Users)
  - MAU (Monthly Active Users)
  - User growth variation

- **Transaction Metrics**:
  - Amount of Transactions per cycle
  - Filter per transaction type
  - Transaction volume

- **Revenue Metrics**:
  - Platform fees earned
  - Fees earned per user
  - Historical fee variation

- **Referral Program**:
  - Total amount of referrers
  - Total amount of referrals
  - Historical variation
  - Transaction volume of referral program

### 5. Support

- Integration of CRM for user generated tickets
- Event logs for platform activity (user and system triggered)

### 6. Platform User Management

- **Cohort Management**:
  - Create User cohort through 'Invite Code'

- **Fee Management - Advanced**:
  - Assign Custom Fee to individual user
  - Assign Custom Fee to cohort

- **Referral Program Management**:
  - Assign Custom Commission to individual user
  - Assign Custom Commission to cohort

## Feature Dependencies

- **Fee Management Advanced**: Depends on basic fee management
- **Referral Program Features**: Depends on referral program implementation
- **CRM Integration**: Requires third-party service selection

## Security Requirements

- Strict role-based access control (RBAC)
- 2FA or Passkey authentication
- Audit logging for all sensitive operations
- Encrypted credential storage
- Separate test and production environments

## Analytics Integration

**Primary Tool**: Amplitude

**Integration Requirements**:
- Real-time data sync
- Custom event tracking
- Dashboard customization
- Historical data retention
- Export capabilities

## Future Considerations

- Advanced reporting and data visualization
- Automated alert system for anomalies
- API access for external integrations
- Mobile app for backoffice access
- Machine learning for fraud detection

---

**Status**: In development
**Priority**: High - Core operational tool
**Next Steps**: Complete authentication layer, implement user management, integrate analytics platform
