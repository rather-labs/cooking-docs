---
title: Table Improvements and Bubblemaps Integration
type: feature-specification
status: planned
priority: medium
created: 2025-08-21
date: 2025-10-20
updated: 2025-10-20
tags: [ui-ux, tables, bubblemaps, analytics, token-details]
related:
  - "[[data-explanations]]"
  - "[[platform-vision-requirements]]"
---

# Table Improvements and Bubblemaps Integration

## Problem Statement

The current experience of the tables for Token Details is lacking for experienced users. Key information for trading is difficult to understand and to map, which translates in missing profit opportunities.

## Solution Overview

In order to help solve these issues we will implement a series of improvements including Bubblemaps integration and enhanced table displays.

---

## Bubblemaps Integration

### Implementation

We will implement the **InsightX** or **Bubblemaps.io** tool for bubblemaps analytics.

**Technical Approach**:
- Deploy a modal window with an iframe
- Filter by contract address and blockchain
- Theme iframe to follow Cooking's design language

### What is a Bubblemap?

A bubblemap is a visual representation that helps illustrate transactions between addresses. Bubblemaps make it easier to trace the path of transactions, showing where funds originated and where they ended up, making it the most useful tool for:
- Tracking transactions
- Understanding the links between addresses
- Visualizing token distribution
- Identifying concentrated holdings

### User Experience

**Access**:
- Available from Token Details page
- Button/link to open Bubblemaps modal
- Modal overlay with themed iframe

**Features**:
- Automatic filtering by current token
- Themed to match Cooking design
- Full-screen or resizable modal
- Close button prominently displayed

---

## Token Details - Transactions Table

### Column Structure

Tables should be ordered as follows:

#### 1. Age
Indicator of time since the transaction was executed.

**Display Format**:
- "3s ago"
- "5m ago"
- "2h ago"
- "1d ago"

#### 2. Maker
Wallet address that executed the transaction.

**Address Display**:
- Truncated format (first 4 + last 4 characters)
- Copy to clipboard on click
- Link to explorer (optional)

**Wallet Indicators**:

These wallets will display indicators based on certain characteristics:

##### If the wallet belongs to the DEV:
- **Dev Bought**: if they purchased the token
- **Dev Sold**: if they sold the token
- **Diamond Hands**: if they met the currently defined criteria (Only applicable for SELL operations as these realize profits)
- **Top 10 Holders**: if this transaction got the wallet inside the threshold (Only applicable for BUY operations)

##### If the wallet is an Insider:
- **Insider**: if the token was purchased in the same block as the mint
- **Diamond Hands**: if they met the currently defined criteria (Only applicable for SELL operations as these realize profits)
- **Top 10 Holders**: if this transaction got the wallet inside the threshold (Only applicable for BUY operations)

##### If the wallet is a Sniper:
- **Sniper**: if the token was purchased in the 10 blocks following the mint
- **Diamond Hands**: if they met the currently defined criteria (Only applicable for SELL operations as these realize profits)
- **Top 10 Holders**: if this transaction got the wallet inside the threshold (Only applicable for BUY operations)

#### 3. Amount
Token quantity either bought or sold.

**Display Format**:
- Formatted with appropriate decimals
- Thousand separators for readability
- Token symbol suffix

#### 4. Total
Representation of the operation value.

**Display Options**:
- Can be expressed in **SOL** or **USD**
- User preference setting
- Clear indication of currency

---

## Holders and Top Traders Tables

### Additional Indicators

Only to add to the **Makers** column:

##### If the wallet belongs to the DEV:
- **Diamond Hands**: if they met the currently defined criteria (Only applicable for SELL operations as these realize profits)
- **Top 10 Holders**: if this transaction got the wallet inside the threshold (Only applicable for BUY operations)

##### If the wallet is an Insider:
- **Insider**: if the token was purchased in the same block as the mint
- **Diamond Hands**: if they met the currently defined criteria (Only applicable for SELL operations as these realize profits)
- **Top 10 Holders**: if this transaction got the wallet inside the threshold (Only applicable for BUY operations)

##### If the wallet is a Sniper:
- **Sniper**: if the token was purchased in the 10 blocks following the mint
- **Diamond Hands**: if they met the currently defined criteria (Only applicable for SELL operations as these realize profits)
- **Top 10 Holders**: if this transaction got the wallet inside the threshold (Only applicable for BUY operations)

---

## Badge/Indicator Design

### Visual Representation

**Badge Types**:
- **Dev**: Special color/icon indicating developer wallet
- **Dev Bought**: Green variant
- **Dev Sold**: Red variant
- **Insider**: Distinct color (e.g., purple)
- **Sniper**: Distinct color (e.g., orange)
- **Diamond Hands**: Diamond icon/badge
- **Top 10 Holders**: Crown or trophy icon

### Badge Stacking

**Multiple Indicators**:
- Wallets can have multiple badges
- Display in priority order
- Compact horizontal layout
- Tooltip for full details on hover

**Example**:
```
[Dev] [Diamond Hands] [Top 10]
```

---

## Implementation Details

### Performance Considerations

**Data Loading**:
- Lazy loading for large transaction lists
- Pagination or infinite scroll
- Caching of wallet classifications

**Real-time Updates**:
- WebSocket for live transaction feed
- Smooth animations for new entries
- Highlight new transactions briefly

### Responsive Design

**Desktop**:
- Full table with all columns
- Horizontal scroll if needed
- Sortable columns

**Mobile**:
- Condensed card view
- Swipe for additional details
- Most important info visible by default

---

## User Preferences

### Customization Options

**Currency Display**:
- SOL vs USD toggle
- Persistent user preference
- Apply across all tables

**Column Visibility**:
- Show/hide columns
- Reorder columns (future)
- Save preferences per user

---

## Analytics Integration

### Tracking

**User Behavior**:
- Bubblemaps modal open rate
- Time spent analyzing bubblemaps
- Table interaction patterns
- Currency preference distribution

**Performance Metrics**:
- Table load times
- Indicator rendering performance
- Modal open/close speed

---

## Future Enhancements

### Advanced Filtering
- Filter by wallet type (Dev, Insider, Sniper)
- Filter by transaction size
- Time range filtering

### Enhanced Visualizations
- Inline charts for price/volume
- Sparklines for trends
- Heat maps for transaction intensity

### Export Capabilities
- Export table data to CSV
- Export bubblemap snapshots
- Share analysis links

---

**Status**: Planned
**Priority**: Medium - Enhances user experience for power traders
**Dependencies**: InsightX/Bubblemaps.io API access, wallet classification system
**Next Steps**:
1. Select Bubblemaps provider (InsightX vs Bubblemaps.io)
2. Design badge/indicator system
3. Implement table column restructuring
4. Build modal for Bubblemaps iframe
5. Add user preference settings
6. Test performance with large datasets
7. Deploy to production
