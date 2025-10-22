---
title: July 2025 - Meetings
type: index
date: 2025-10-21
summary: Index of Cooking.gg meeting notes from July 2025, covering Hyperliquid perpetuals integration and mobile filters implementation.
---

# July 2025 - Meetings

This directory contains structured meeting notes from Cooking.gg meetings during July 2025.

## Overview

**Period Covered:** July 2025
**Meeting Types:** Weekly Demos, Daily Standups, Technical Deep Dives, Weekly Syncs
**Team:** Cooking.gg Development Team
**Language:** English (translated from Spanish)

## Files

### Technical Deep Dive Meetings (Batch 10)
- `2025-07-24-hyperliquid-integration.md` - Perpetuals trading platform integration (Hyperliquid)
- `2025-07-24-mobile-filters.md` - Mobile app filtering and search implementation

### Weekly Demo Meetings
- `2025-07-04-cooking-demo.md` - Weekly product demonstration
- `2025-07-11-cooking-demo.md` - Weekly product demonstration
- `2025-07-18-cooking-demo.md` - Weekly product demonstration
- `2025-07-25-cooking-demo.md` - Weekly product demonstration

### Weekly Syncs
- `Cooking-Sync-2025-07-07.md` - Team synchronization meeting
- `Cooking-Sync-2025-07-14.md` - Team synchronization meeting

### Daily Standups
Located in `daily-standups/` subdirectory

## Major Themes

### Hyperliquid Perpetuals Integration (July 24)
Technical planning for integrating perpetuals trading via Hyperliquid:

- **Cross-Margin Trading**: Decided to implement cross-margin as default (simpler UX, better risk management)
- **Geoblocking Workaround**: Deploy backend in non-blocked regions (Argentina, Brazil, Mexico, Europe)
- **Order Types**: Market, Limit, Take Profit, Stop Loss
- **Permissions System**: Granular access control for perpetuals features
- **WebSocket Architecture**: Real-time price feeds and account state synchronization

### Mobile Filters & Discovery (July 24)
Advanced filtering and search for mobile application:

- **Hybrid Filtering**: Server-side initial fetch + client-side filtering for performance
- **Search Integration**: Elasticsearch for full-text search with fuzzy matching
- **Mobile UX Patterns**: Bottom sheet filters, swipe actions, pull-to-refresh
- **Performance Optimizations**: Virtualized lists, lazy loading, smart caching
- **Filter Categories**: Market stage, time-based metrics, risk indicators, social metrics

## Technical Highlights

### Infrastructure & Architecture
- **Perpetuals Service**: Separate microservice for perpetuals trading
- **WebSocket Resilience**: Automatic reconnection with state resynchronization
- **Multi-RPC Strategy**: Multiple Solana RPC providers for redundancy
- **Elasticsearch Integration**: Full-text search index for token discovery

### Mobile Development
- **React Native**: Continued mobile app development
- **State Management**: Redux for centralized state, AsyncStorage for persistence
- **Filter UI**: Bottom sheet pattern for mobile filtering
- **Performance**: Virtualized lists handling 10,000+ tokens

### Trading Features
- **Order Management**: Comprehensive order lifecycle management
- **TP/SL Support**: Take profit and stop loss order types
- **Real-Time Data**: WebSocket connections for price updates
- **Cross-Margin**: Simplified perpetuals trading with account-level collateral

## Key Decisions

### Technical Architecture
- **Decision**: ECS over EKS for container orchestration
- **Decision**: WebSocket-primary with REST fallback for real-time data
- **Decision**: Cross-margin only for perpetuals MVP
- **Decision**: Elasticsearch for mobile search functionality
- **Decision**: Hybrid filtering (server + client) for mobile performance

### Product Strategy
- **Decision**: Hyperliquid as perpetuals platform
- **Decision**: Deploy infrastructure in geographically compliant regions
- **Decision**: Mobile app to have feature parity with web for core trading

## Critical Issues & Solutions

### Hyperliquid Geoblocking
- **Issue**: API access blocked from US and sanctioned countries
- **Solution**: Deploy backend services in compliant regions, VPN routing

### Mobile Performance
- **Issue**: Large token lists causing performance issues on mobile
- **Solution**: Virtualized lists, client-side caching, lazy loading

## Action Items Carried Forward

### Hyperliquid Integration
- [ ] Obtain commercial licenses and API access
- [ ] Design database schema for perpetuals positions
- [ ] Implement WebSocket client for real-time data
- [ ] Build permissions system for access control

### Mobile Filters
- [ ] Set up Elasticsearch cluster for search
- [ ] Implement virtualized list components
- [ ] Design and build bottom sheet filter UI
- [ ] Create filter preset templates

## Meeting Attendance

**Technical Deep Dives:** Lucas Cufre, Martin Aranda, Eduardo Yuschuk, Gregory Chapman, Marcos Tacca

---

**Note:** These meetings were originally conducted in Spanish and have been translated to English while preserving technical terminology.
