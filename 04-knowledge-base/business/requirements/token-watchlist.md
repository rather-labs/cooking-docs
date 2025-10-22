---
title: Token Watchlist Feature
type: feature-specification
status: planned
priority: medium
created: 2025-09-22
date: 2025-10-20
updated: 2025-10-20
tags: [watchlist, token-tracking, portfolio, user-experience]
related:
  - "[[platform-vision-requirements]]"
  - "[[data-explanations]]"
---

# Token Watchlist Feature

## Overview

Allow users to easily follow tokens from a selected list. Track their market movements and other relevant metrics, allowing them to follow their narratives of interest.

## Access and Availability

### Platform Support
- **Desktop**: Primary implementation
- **Mobile**: Near future enhancement

### Accessibility
This feature should be accessible from **anywhere on the platform**:
- Global navigation menu
- Quick access button
- Keyboard shortcut support

---

## Core Functionality

### Adding and Removing Tokens

**Adding Tokens**:
- From token details page
- From search results
- From portfolio holdings
- Quick add button (+) on token cards

**Removing Tokens**:
- Remove button on watchlist items
- Swipe gesture (mobile, future)
- Bulk remove option

### Watchlist Management

**Organization**:
- Single "Watchlist" collection (initial version)
- Future: Multiple custom lists
- Search/filter within watchlist
- Sort by various metrics

---

## Token Display Parameters

Each token in the watchlist will show the following parameters:

### 1. Token Information
- **Symbol**: e.g., ROOSTER
- **Token Image**: Logo/icon
- **Token Name**: Full name
- **Provider**: Trading venue (Pump.fun, Raydium, etc.)
- **Social Links**: Quick access to Twitter, Telegram, website

### 2. Market Cap
- **Last Known Value**: Current market cap
- **1h PnL**: Percentage change in last hour
- **Display Currency**: USD by default, switchable to SOL
- **Visual Indicator**: Green for positive, red for negative

### 3. 1h Volume
- **Last Hour Trading Volume**: Trading activity in past hour
- **Display Currency**: USD by default, switchable to SOL
- **Trend Indicator**: Up/down arrow

### 4. Liquidity
- **Last Known Value**: Available trading liquidity
- **Display Currency**: USD by default, switchable to SOL
- **Health Indicator**: Color-coded based on liquidity levels

---

## User Actions

### Quick Actions

For each token in the watchlist, users should be able to:

1. **Copy Contract Address**
   - One-click copy to clipboard
   - Visual confirmation (checkmark)
   - Tooltip showing full address on hover

2. **Access Token Details Page**
   - Click token name/image
   - Opens full token details
   - Preserves watchlist state

3. **Remove from List**
   - Remove button (X icon)
   - Confirmation dialog (optional, preference-based)
   - Undo option (brief timeout)

---

## UI/UX Design

### List View

```
┌─────────────────────────────────────────────────────────────────┐
│ Watchlist (5)                            [⚙️ Settings] [+ Add] │
├─────────────────────────────────────────────────────────────────┤
│ Sort by: [Market Cap ▼]     Currency: ● USD  ○ SOL             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ ROOSTER │ 🐓                                                    │
│ Pump.fun  [🐦] [💬]                                            │
│ Market Cap: $3,670 (+2.5% 🔺)                                   │
│ 1h Volume: $142.5K   Liquidity: $8.5K                          │
│ [📋 Copy] [→ Details] [✕ Remove]                               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ SOL │ ◎                                                         │
│ Native  [🐦] [💬] [🌐]                                         │
│ Market Cap: $4.2B (-0.8% 🔻)                                    │
│ 1h Volume: $85.3M   Liquidity: $12.5M                          │
│ [📋 Copy] [→ Details] [✕ Remove]                               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ ... more tokens ...                                             │
└─────────────────────────────────────────────────────────────────┘
```

### Compact View (Optional)

```
┌─────────────────────────────────────────────────┐
│ Watchlist                         [⚙️] [+]     │
├─────────────────────────────────────────────────┤
│ 🐓 ROOSTER  $3.7K (+2.5%) Vol:$142K  [📋] [✕] │
│ ◎ SOL      $4.2B (-0.8%) Vol:$85M   [📋] [✕]  │
│ 🦊 DOGE    $8.5K (+12%)  Vol:$245K  [📋] [✕]  │
└─────────────────────────────────────────────────┘
```

---

## User Preferences

### Currency Toggle
- **Default**: USD
- **Option**: SOL
- **Persistence**: User preference saved
- **Global**: Applies to all watchlist views

### Sort Options
- Market Cap (high to low / low to high)
- 1h Volume (high to low / low to high)
- 1h PnL% (high to low / low to high)
- Liquidity (high to low / low to high)
- Alphabetical (A-Z / Z-A)
- Recently Added

### Refresh Rate
- **Auto-refresh**: Every 30 seconds (default)
- **Manual refresh**: Button available
- **User setting**: Adjust frequency (10s / 30s / 1m)

---

## Technical Considerations

### Data Updates
- Real-time data via WebSocket
- Fallback to polling if WebSocket unavailable
- Efficient data fetching (batch requests)

### Performance
- Lazy loading for large watchlists
- Virtual scrolling for 50+ tokens
- Optimized rendering

### Storage
- Watchlist saved to user profile
- Sync across devices
- Maximum 100 tokens per watchlist (configurable)

### API Endpoints

```
GET  /api/watchlist
POST /api/watchlist/add
DELETE /api/watchlist/remove/{tokenId}
PUT  /api/watchlist/reorder
```

---

## Future Enhancements

### Multiple Watchlists
- Create custom named lists
- "DeFi Tokens", "Memecoins", "Long-term Holds"
- Organize by strategy or category

### Advanced Features
- Price alerts for watchlist tokens
- Comparison view (side-by-side)
- Export watchlist (CSV, JSON)
- Share watchlist with others

### Analytics
- Watchlist performance tracking
- Historical data for watched tokens
- Correlation analysis

### Integration
- Quick trade from watchlist
- Add entire watchlist to custom order
- Portfolio comparison

---

## User Education

### Onboarding
- Tooltip on first visit: "Add tokens to track their performance"
- Suggested tokens based on portfolio
- Popular tokens to get started

### Help Documentation
- How to add/remove tokens
- Understanding metrics
- Best practices for watchlist management

---

## Analytics & Monitoring

### Track Metrics
- Watchlist adoption rate
- Average tokens per watchlist
- Most watched tokens
- Watchlist engagement (opens, interactions)
- Conversion: watchlist → trade

---

**Status**: Planned
**Priority**: Medium - Enhances user engagement and tracking
**Platform**: Desktop first, mobile later
**Next Steps**:
1. Design watchlist UI/UX
2. Implement data fetching and caching
3. Build watchlist management backend
4. Create user preference system
5. Implement real-time updates
6. Test performance with large lists
7. Deploy to desktop
8. Gather feedback
9. Plan mobile implementation
