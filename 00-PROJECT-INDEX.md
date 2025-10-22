---
title: Project Master Index
type: project-index
date: 2025-10-17
last-updated: 2025-10-22
status: active
summary: |
  Central navigation hub for all project knowledge and documentation.
  Start here to find any information about the project.
---

# Project Master Knowledge Index

**Last Updated:** 2025-10-22
**Project Status:** ✅ Beta Launched | October 17, 2025 - Internal Testing Ongoing (Oct 21-27)

**Documentation Statistics:**
- 📄 **Total Documents:** 170+
- ✅ **Architecture Decision Records (ADRs):** 27 decisions (May-October 2025)
- 📝 **Requirements:** 36 specifications
- 🔬 **Research Documents:** 5
- 📊 **Meeting Notes:** 105 (including 4 from Oct 17-22: daily standups, QA session, weekly sync)
- ✅ **Processing Status:** Knowledge base fully updated through October 22

**Recent Updates (October 22, 2025):**
- ✅ **Documentation Updated from Last 4 Meetings** - Oct 17, 20, 21, 22 meetings processed
- ✅ **Current Status Updated** - Cookie auth migration, knowledge base centralization, production bugs documented
- ✅ **Priorities Updated** - P0 production bug fixes added (CORS, custom order validation)
- ✅ **Blockers Updated** - Minor production issues documented with mitigation plans
- ✅ **Glossary Enhanced** - Added 5 new terms: Axios, Fetch API, Borsh, Next.js Proxy, Pam Fun/Pam Swap
- ✅ **Knowledge Base Centralization Complete** - Claude AI indexing operational for instant knowledge queries

**Recent Updates (Session 10 - 2025-10-21):**
- ✅ **Phase 5: Index Updates COMPLETE** - All indexes updated with final knowledge base enhancement
- ✅ **Knowledge Base Enhancement Project COMPLETE** - All 5 phases successfully finished
  - Phase 1: 27 ADRs created (100% complete)
  - Phase 2: Current status updates (100% complete)
  - Phase 3: Glossary enhancement with 90+ terms (100% complete)
  - Phase 4: 7 requirements updated (100% complete)
  - Phase 5: All 3 indexes updated (100% complete)
- ✅ **27 ADRs Documented** - Complete decision history from May-October 2025 covering beta launch journey
  - Architecture (5): ClickHouse, Microservices, SSE, Hybrid Filtering, Indexer
  - Technical (5): Jupiter, TradingView, Auth0, Type-Safe API, Redis
  - Business (4): Multilevel Referral, Closed Beta, Zero Fees, Beta Timeline
  - Process (3): AWS ECS, Sprint Calls, Feature Freeze
  - Security (3): Security Password, Biometric Auth, WAF/Encryption
  - Infrastructure (3): Multi-AZ, Turnkey, Two-Client ClickHouse
- ✅ **Requirements Enhanced** - Added biometric authentication, Auth0 details, US geolocation workaround, launch metrics
- ✅ **October 17 Beta Launch** - Successfully deployed with 99.9% uptime, 3s transactions, referral-only access
- ✅ **Total Time Investment** - ~13 hours across 10 sessions to extract and integrate 101 meeting notes into knowledge base

## Quick Navigation
- 📊 [Current Status](03-active-work/_current-status.md) - Updated weekly
- 🎯 [Current Priorities](03-active-work/priorities.md)
- 🚧 [Active Blockers](03-active-work/blockers-and-risks.md)
- 📋 [Recent Decisions](02-decisions/_decisions-index.md)
- 🏗️ [Project Charter](01-foundation/project-charter.md)
- 📥 [Documents to Parse](08-documents-to-parse/) - Drop unstructured content here

## Project Overview
This is a new project using a structured knowledge base system designed to make all project information easily discoverable by both team members and AI assistants. The knowledge base follows best practices for documentation, decision tracking, and knowledge management.

Start by reviewing the [Project Charter](01-foundation/project-charter.md) to understand the project's purpose, and check the [Current Status](03-active-work/_current-status.md) for the latest updates.

## Project Health Dashboard
| Dimension | Status | Last Updated |
|-----------|--------|--------------|
| Schedule | ✅ Delivered | 2025-10-21 (Beta launched Oct 17) |
| Quality | ✅ Excellent | 2025-10-21 (99.9% uptime, 3s txns) |
| Scope | ✅ Complete | 2025-10-21 (All beta features deployed) |
| Performance | ✅ Optimized | 2025-10-21 (15x query improvement) |
| Team | 🟢 Healthy | 2025-10-21 |
| Documentation | 🟢 Comprehensive | 2025-10-21 (27 ADRs, 36 requirements) |

**Legend:** ✅ Delivered/Excellent | 🟢 Green (Healthy) | 🟡 Yellow (At Risk) | 🔴 Red (Critical)

## Key Documents by Category

### Foundation & Strategy
- [Project Charter](01-foundation/project-charter.md) - Why this project exists and what we aim to achieve
- [Objectives & Scope](01-foundation/objectives-and-scope.md) - What we're building and what's out of scope
- [Stakeholders](01-foundation/stakeholders.md) - Who's involved and their roles
- [Glossary](01-foundation/glossary.md) - Domain terminology and definitions
- [Constraints & Assumptions](01-foundation/constraints-and-assumptions.md) - Project boundaries and assumptions

### Architecture & Technical
- [Technical Index](04-knowledge-base/technical/_index.md) - Overview of technical documentation
- [User Documentation](04-knowledge-base/technical/)
  - [Platform User Documentation](04-knowledge-base/technical/platform-user-documentation.md) - Complete user guide for all features
  - [Data Explanations](04-knowledge-base/technical/data-explanations.md) - Detailed explanations of all platform metrics and calculations
  - [GitBook Index](04-knowledge-base/technical/gitbook-index.md) - Public documentation structure
- [Architecture](04-knowledge-base/technical/architecture/) - System design and architecture decisions
- [APIs & Integrations](04-knowledge-base/technical/apis-and-integrations/) - API documentation and integration points
- [Infrastructure](04-knowledge-base/technical/infrastructure/) - Infrastructure and deployment documentation

### Business & Requirements
- [Business Index](04-knowledge-base/business/_index.md) - Overview of business documentation
- [Requirements](04-knowledge-base/business/requirements/) - Product requirements and specifications (36 documents)
  - **Platform & Vision**
    - [Platform Vision & Requirements](04-knowledge-base/business/requirements/platform-vision-requirements.md) - Strategic direction and market positioning
    - [Q2 & Q3 2025 Roadmap](04-knowledge-base/business/requirements/roadmap-q2-q3-2025.md) - Development roadmap with 14 prioritized features
    - [Q3 2025 Beta Release](04-knowledge-base/business/requirements/beta-release-q3-2025.md) - Beta launch specifications
    - [Stakeholder Requirements](04-knowledge-base/business/requirements/stakeholder-requirements.md) - Feature prioritization from stakeholder discussions
  - **Core Trading Features**
    - [Trading Methods Specification](04-knowledge-base/business/requirements/trading-methods.md) - All order types (Market, DCA, Limit, TWAP, VWAP, Custom)
    - [Trading Methods UX Design](04-knowledge-base/business/requirements/trading-methods-ux-design.md) - Detailed UX specifications
    - [Limit Orders with TP/SL](04-knowledge-base/business/requirements/limit-orders-methodology.md) - Implementation methodology
    - [Portfolio-Wide TP/SL](04-knowledge-base/business/requirements/portfolio-wide-tpsl.md) - Risk management at portfolio level
    - [Market Cap Variation Algorithm](04-knowledge-base/business/requirements/market-cap-variation-algorithm.md) - Automated trading based on MC changes
    - [Auto-Adjusting Priority Fee](04-knowledge-base/business/requirements/auto-adjusting-priority-fee.md) - Network-optimized fees
  - **Authentication & Security**
    - [Social Login Integration](04-knowledge-base/business/requirements/social-login-integration.md) - Multi-method authentication via Turnkey
    - [Security Password in Wallet Manager](04-knowledge-base/business/requirements/security-password-wallet-manager.md) - Critical operations protection
    - [External Wallet Support](04-knowledge-base/business/requirements/external-wallet-support.md) - Import existing Solana wallets
  - **Mobile App** (8 documents)
    - [Mobile App PRD](04-knowledge-base/business/requirements/mobile-app-prd.md) - iOS mobile app product requirements
    - [Mobile Signup, Login & Home](04-knowledge-base/business/requirements/mobile-signup-login-home.md) - Authentication and discovery
    - [Mobile Token Details](04-knowledge-base/business/requirements/mobile-token-details.md) - Token info and trading
    - [Mobile Wallet](04-knowledge-base/business/requirements/mobile-wallet.md) - Portfolio and wallet management
  - **Referral Program**
    - [Referral Program v2 - Multilevel](04-knowledge-base/business/requirements/referral-program-multilevel.md) - 3-level commission structure
    - [Referral Program - Invite Codes](04-knowledge-base/business/requirements/referral-program-invite-codes.md) - Custom code generation
  - **Platform Features**
    - [Settings Feature](04-knowledge-base/business/requirements/settings-feature.md) - Account, shortcuts, and security settings
    - [Token Watchlist](04-knowledge-base/business/requirements/token-watchlist.md) - Track favorite tokens
    - [Table Improvements & Bubblemaps](04-knowledge-base/business/requirements/table-improvements-bubblemaps.md) - Enhanced data visualization
    - [Spot Fee Customization](04-knowledge-base/business/requirements/spot-fee-customization.md) - Dynamic fee rules
  - **Integrations**
    - [HyperLiquid Perpetuals](04-knowledge-base/business/requirements/hyperliquid-perpetuals-integration.md) - Derivatives trading integration
    - [Backoffice Platform](04-knowledge-base/business/requirements/backoffice-platform.md) - Admin and analytics tools
- [User Research](04-knowledge-base/business/user-research/) - User studies and research findings
- [Market Analysis](04-knowledge-base/business/market-analysis/) - Market research and competitive analysis

### Operational Knowledge
- [Operational Index](04-knowledge-base/operational/_index.md) - Overview of operational documentation
- [Processes](04-knowledge-base/operational/processes/) - Team processes and workflows
- [Runbooks](04-knowledge-base/operational/runbooks/) - Operational procedures and guides

### Decisions (Most Recent)
1. [ADR-001: Use Telegram for User Authentication](02-decisions/2024-10-03-telegram-authentication.md) - 2024-10-03

*Note: Additional architectural decisions documented in meeting notes and requirements documents*

See [all decisions](02-decisions/_decisions-index.md).

### Research
- [Research Index](05-research/_research-index.md) - All research activities (5 documents)
- [Coin Trading Research](05-research/coin-trading-research.md) - Market analysis on trading patterns and memecoin behavior
- [Jupiter vs HelloMoon Analysis](05-research/jupiter-vs-hellomoon-analysis.md) - Routing solution comparison (Decision: Jupiter)
- [On-Ramp Solution Research](05-research/onramp-solution-research.md) - Crossmint vs Onramper comparison (Decision: Onramper)
- [Apple App Store Requirements](05-research/apple-app-store-business-requirements.md) - Multi-jurisdiction business account setup

See [all research](05-research/_research-index.md).

## Recent Activity
### This Week (Week of 2025-10-20)
- **📝 144 Documents Processed** - Successfully converted and organized all English documentation + July daily standups
  - **116 Meeting Notes** (May-October 2025) - 19 Weekly Demos, 9 Weekly Syncs, 50 Daily Standups, 17 Demo meetings
  - **36 Feature Specifications** - Core trading features, mobile app, referral program
  - **5 Research Documents** - Technical comparisons and market analysis
- **✅ Batch 6 Complete** - July Daily Standups (10 meetings):
  - Hyperliquid Integration Crisis - US regulatory restrictions created major legal concerns
  - ClickHouse Migration Success - Constant query complexity achieved
  - UI Component Refactoring - Major B2 components system reorganization
  - Team Changes - Ramiro departure, Evil Martians onboarding
- **✅ Batch 3 Complete** - All English requirements and feature specs processed:
  - 18 Core Trading Features (Market cap algorithm, limit orders, TWAP/VWAP, custom orders)
  - 8 Mobile App Specifications (Signup, wallet, settings, token details)
  - 2 Referral Program Specs (Multilevel system, invite codes)
  - 5 Research Documents (Jupiter vs HelloMoon, onramp comparison, Apple requirements)
- **🗂️ Knowledge Base Expanded** - All specs now in structured format with cross-references
- **📊 Processing Tracker** - 53 Spanish documents remaining (11 August + 10 September + 9 October + 13 specialized + 3 other)

### Last Week (Week of 2025-10-17)
- **Cooking.gg inception document processed** - Comprehensive project documentation extracted
- **Project Charter created** - Foundation document establishing project purpose, scope, and timeline
- **Glossary updated** - Added 15+ key terms (Bonding Curve, Diamond Hands, Pump.fun, Raydium, etc.)
- **ADR-001 created** - Decision to use Telegram for user authentication
- Project knowledge base structure created
- Templates and indexes established

### Last 30 Days
- **2024-10-03:** Cooking.gg project inception document created
- **2025-10-17:** Project knowledge base initialization and inception document processing
- **2025-10-19:** Meeting notes processing - 84 documents converted and organized (daily standups, demos, technical discussions)
- **2025-10-20:** Batch 1 processing complete - 28 additional meeting documents added (weekly demos and sync meetings from May-Sep)

## Key Contacts
| Role | Name | Responsibility |
|------|------|----------------|
| Project Lead | Lucas Cufré | Overall delivery, coordination, and client relations |
| Tech Lead | Martin Aranda | Architecture, technical decisions, and infrastructure |
| Backend/Indexer Lead | Eduardo Yuschuk | Solana indexer, database optimization, and backend systems |
| Mobile Lead | Byron Chavarria | iOS development and mobile app |
| Frontend Team | Luis Rivera, Germán Derbes Catoni, Marko Jauregui | UI/UX implementation and frontend features |
| Product Stakeholders | Z (Zane), Greg, Naji, Shakib | Product vision, requirements, and priorities |

*Based on meeting attendance from June-October 2025*

## Getting Started
New to this project? Read these documents in order:

1. **[Project Charter](01-foundation/project-charter.md)** - Understand the why and what
2. **[Current Status](03-active-work/_current-status.md)** - Get up to speed on current state
3. **[Glossary](01-foundation/glossary.md)** - Learn the domain language
4. **[Objectives & Scope](01-foundation/objectives-and-scope.md)** - Understand what we're building

For developers, also review:
- [Technical Architecture Overview](04-knowledge-base/technical/architecture/)
- [Recent Technical Decisions](02-decisions/_decisions-index.md)

## Documentation Standards
All documents in this knowledge base follow these conventions:
- **YAML frontmatter** with metadata for easy discovery
- **Date format:** YYYY-MM-DD
- **File naming:** lowercase-with-hyphens.md
- **Decisions:** Use ADR format with sequential IDs (ADR-001, ADR-002, etc.)
- **Summaries:** All documents include a summary for LLM context
- **Cross-linking:** Bidirectional links between related documents

## How to Use This Knowledge Base

### For Team Members
- **Finding information:** Start here at the index, or use VS Code search
- **Adding structured content:** Use templates in each category folder
- **Adding unstructured content:** Drop files in [08-documents-to-parse/](08-documents-to-parse/) and let Claude Code structure them
- **Making decisions:** Use the [decision template](02-decisions/_template-decision.md)
- **Meeting notes:** Use the [meeting template](06-meetings/_template-meeting.md) or drop raw notes in [08-documents-to-parse/](08-documents-to-parse/)

### Unstructured Content Workflow
Have meeting notes, email threads, or research findings that need structure?

1. **Drop files** in [08-documents-to-parse/](08-documents-to-parse/)
2. **Claude Code parses** the content automatically
3. **Structured documents** are created in appropriate locations
4. **Indexes updated** for discoverability
5. **Original file deleted** after successful processing

See [Documents to Parse README](08-documents-to-parse/README.md) for details and examples.

### For AI Assistants (Claude Code, etc.)
- See [.claude/instructions.md](.claude/instructions.md) for detailed guidance
- Always check this index first for navigation
- Prioritize recent status and decisions
- Use metadata and summaries for context

## Maintenance Schedule
- **Weekly:** Update current status, file new content
- **Monthly:** Update this index, review decisions, update glossary
- **Quarterly:** Archive old content, audit structure

See [Maintenance Guide](.claude/maintenance-guide.md) for detailed procedures.

## Quick Links

### Templates
- [Decision Template](02-decisions/_template-decision.md)
- [Meeting Template](06-meetings/_template-meeting.md)
- [Research Template](05-research/_template-research.md)

### Indexes
- [Decisions Index](02-decisions/_decisions-index.md)
- [Meetings Index](06-meetings/_meetings-index.md)
- [Research Index](05-research/_research-index.md)
- [Archive Log](07-archive/_archive-log.md)

### Guides
- [Claude Code Instructions](.claude/instructions.md)
- [Maintenance Guide](.claude/maintenance-guide.md)
- [How to Add Decisions](02-decisions/README.md)
- [How to File Meetings](06-meetings/README.md)

## Need Help?

### Documentation Questions
- Check the README files in each section
- Review the templates for examples
- Consult the [Maintenance Guide](.claude/maintenance-guide.md)

### Project Questions
- Review [Current Status](03-active-work/_current-status.md)
- Check [Active Blockers](03-active-work/blockers-and-risks.md)
- Review recent [Decisions](02-decisions/_decisions-index.md)
- Contact the project lead or relevant stakeholder

---

**Welcome to the project!** This knowledge base is designed to grow with the project and make information easily accessible to everyone. Start by exploring the foundation documents, and don't hesitate to add new content using the provided templates.
