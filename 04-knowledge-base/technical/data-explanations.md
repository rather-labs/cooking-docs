---
title: Miscellaneous Data Explanations
type: technical-documentation
date: 2025-08-15
status: active
priority: high
created: 2025-08-15
updated: 2025-10-20
last-updated: 2025-10-20
tags: [documentation, data-definitions, metrics, calculations, user-education]
related:
  - "[[trading-methods]]"
  - "[[platform-user-documentation]]"
  - "[[settings-feature]]"
---

# Miscellaneous Data Explanations

## Market Details

### Market Cap

**What it is:** The total value of all tokens in circulation

**How it's calculated:** `Total number of tokens × current price per token`

### Liquidity

**What it is:** How much money is available for trading this token

**How it's calculated:** Add up all the money locked in trading pools for this token

### Volume

**What it is:** How much of the token has been traded over time

**How Cooking calculates it differently:**
- **Complete lifecycle tracking** - Cooking tracks volume from when a token is first created through its entire life
- **Cross-platform tracking** - Unlike other platforms that restart counting when tokens move between exchanges (like from Pump.fun to Raydium), Cooking keeps tracking continuously
- **Real-time updates** - Volume updates instantly as new trades happen
- **All platforms combined** - Adds up trading volume from every exchange where the token is listed

**How it's calculated:** `Token amount ÷ current token price in SOL`

### Total Holders

**What it is:** The total number of wallets that currently own any amount of the token

**Why it matters:**
- **Distribution indicator** - More holders usually means better token distribution across the community
- **Stability signal** - Tokens with more holders tend to be more stable (selling pressure is spread out)
- **Community interest** - Higher holder counts suggest broader adoption and engagement
- **Trading automation** - Can be used to trigger automated trades (e.g., "sell if holders drop below 100")

### Total Transactions

**What it is:** The total number of operations for a token. This value is also split by direction.

**Why it matters:**
- **Market emotion** - As this gauge modifies, the market feeling towards the token becomes more apparent.

### Makers

**What it is:** The total number of unique wallets that interacted with a token. This value is also split by direction.

**Why it matters:**
- **Community interest** - Higher counts suggest broader adoption and engagement

---

## Security Considerations

### Top 10 Holders

This metric represents the **percentage of the total token supply held by the 10 largest wallets**.

**Calculation:**
```
(Total token amount held by top 10 wallets / Total token supply) × 100
```

**Key insights:**
- Lower percentages are preferred as they suggest more distributed and decentralized token supply
- Reduces the risk of market manipulation by a few large holders
- ⚠️ **Important note:** Currently, bonding curves and other AMM pools can be included in this top 10 as holders

### Dev Hold (Dev Holdings)

This indicates the **percentage of tokens held by the developer's wallet** (the wallet responsible for creating the token).

**Key insights:**
- A higher percentage may indicate that the developer has a vested interest in the token's long-term success
- Related to "Dev Sold" - a Boolean indicator that flags whether the developer has sold their entire position

### Snipers

This represents the **number of wallets that bought tokens immediately after the launch** (specifically within the immediate 10 blocks after the mint creation).

**Key insights:**
- May include bot activity
- A lower count suggests less automated or manipulative activity
- Indicates more natural market behavior when numbers are lower

### Diamond Hands

These are **wallets that hold onto tokens for extended periods while maintaining profitability**.

**Requirements to qualify:**
- Hold tokens for more than 49 minutes on average
- Make more than 0.033 SOL profit (about $3-4)

**Behavioral characteristics:**
- Resist short-term selling even during market fluctuations
- Maintain positions through volatility while staying profitable
- Reflect confidence in the token's potential

### Insiders Count

**What it is:** How many people bought the token in the exact same block it was created

**How it's calculated:** Count unique wallets that bought tokens when the token was first minted

---

## Profit & Loss (PnL)

### Realized PnL

**What it is:** Actual profit/loss from tokens you've already sold

**How it's calculated:**
- Money received from selling tokens
- Minus the average cost of those tokens
- Uses your average buy price (total spent ÷ tokens bought)

**Formula:**
```
Realized PnL = Sale Proceeds - (Average Buy Price × Tokens Sold)
```

### Unrealized PnL

**What it is:** Potential profit/loss from tokens you still own

**How it's calculated:**
```
Unrealized PnL = Tokens you still have × (Current Price - Your Average Buy Price)
```

### Total PnL

**What it is:** Your complete profit/loss picture

**How it's calculated:**
```
Total PnL = Realized PnL + Unrealized PnL
```

### Take Profit (TP)

**What it does:** Automatically sells your tokens when you've made enough profit.

**How it works:**
- You set a profit target (like +20%)
- When your investment reaches that profit, the app sells automatically
- This locks in your gains so you don't lose them if prices drop

**Example:** You buy a token and set Take Profit at +30%. If the token goes up 30%, Cooking automatically sells and you keep your profit.

### Stop Loss (SL)

**What it does:** Automatically sells your tokens if you're losing too much money.

**How it works:**
- You set a loss limit (like -10%)
- If your investment drops to that loss, the app sells automatically
- This prevents you from losing even more money

**Example:** You buy a token and set Stop Loss at -15%. If the token drops 15%, Cooking automatically sells to prevent bigger losses.

### Important Rules

**When you can use them:**
- Right now, you can only set Take Profit and Stop Loss when creating **Buy Limit Orders**

**What this means:**
- **Buy Limit Orders:** You can set both Take Profit **AND** Stop Loss

**Remember:** These safety orders only work if your main order goes through first.

---

_Think of Take Profit and Stop Loss like automatic safety switches that protect your money while you sleep._

---

## Trading Settings

### Slippage

**What it does:** Protects you from bad price changes when your trade happens.

**How it works:**
- You set a maximum price change you're willing to accept (like 30%)
- If the price moves too much while your trade is processing, the trade stops
- **For buying**: Price can't go higher than your limit
- **For selling**: Price can't go lower than your limit

**Example:** You want to buy a token at $1, with 30% slippage. If the price jumps to $1.40 while your trade processes, it will cancel instead of overpaying.

### Priority Fee

**What it does:** Pays extra to get your trade processed faster.

**How it works:**
- You pay a small extra fee (default: 0.008 SOL) to blockchain validators
- Higher fees = faster trade processing
- Like paying extra for express shipping

**Example:** During busy trading times, paying a higher priority fee helps your trade go through quickly instead of waiting in line.

### Gas Fee

**What it does:** The basic cost to put your trade on the blockchain.

**How it works:**
- Every blockchain transaction costs gas to process
- The fee varies based on how busy the network is
- This fee is automatically calculated and shown before you trade

**Example:** Think of it like a postage stamp - you need to pay this fee for your trade to be delivered to the blockchain.

### Time To Live (TTL)

**What it does:** Sets an expiration date for your order.

**How it works:**
- You choose how long your order stays active (minutes, hours, or days)
- If your order doesn't execute by that time, it automatically cancels
- Prevents old orders from accidentally executing later

**Example:** You set a limit order to buy a token at a specific price with 24-hour TTL. If the price doesn't hit your target in 24 hours, the order cancels automatically.

---

_These settings help you control costs, speed, and timing for your trades while protecting you from unwanted surprises._

---

## Miscellaneous

### Security Password

**What it does:** An extra password that protects your most important wallet actions.

**How it works:**
- You must create this password before you can use wallet features
- You'll need to enter it for sensitive actions like:
  - Sending money to new wallets
  - Viewing your seed phrase
  - Adding withdrawal addresses
- It's stored securely and encrypted
- Once you create it on web or mobile, it works on both

**Why it's important:** Adds an extra layer of protection so even if someone gets into your account, they can't steal your money without this password.

**Requirements:**
- Must be strong (long and complex)
- Cannot be skipped or bypassed
- You must acknowledge security warnings before creating it

---

### Seed Phrase

**What it does:** A secret backup key that can recover your entire wallet.

**How it works:**
- It's a list of 12-24 words that represents your wallet
- Think of it as the "master key" to your wallet
- If you lose access to the app, you can use these words to recover everything
- **ONE-TIME ONLY:** You can only view it once for security reasons

**Critical warnings:**
- ⚠️ Anyone with your seed phrase can steal all your money
- Write it down on paper and store it safely
- Never share it with anyone
- Never store it digitally (photos, emails, cloud storage)
- If you lose it, you could lose access to your wallet forever

**How to access:**
- Requires your Security Password
- Only available once per wallet
- After viewing it once, the option disappears permanently

---

**Security Summary:**
- **Security Password** = Daily protection for sensitive actions
- **Seed Phrase** = Ultimate backup for wallet recovery (handle with extreme care)

_Both are essential for keeping your crypto safe - the Security Password protects daily use, while the seed phrase is your emergency recovery option._

---

## Quick Reference Tables

### Security Metrics

| Metric | Good Range | Warning Signs |
|--------|-----------|---------------|
| Top 10 Holders | < 40% | > 60% (concentration risk) |
| Dev Hold | 5-15% | 0% (abandoned) or > 30% (control risk) |
| Snipers | < 10 | > 50 (bot activity) |
| Diamond Hands | > 20% | < 5% (speculative) |
| Insiders | < 5 | > 20 (pre-launch distribution) |

### Trading Settings Defaults

| Setting | Default Value | Range |
|---------|--------------|-------|
| Slippage | 30% | 0.1% - 50% |
| Priority Fee | 0.008 SOL | 0.001 - 0.1 SOL |
| Gas Fee | Variable | Network-dependent |
| TTL | 24 hours | 1 min - 30 days |

---

**Status**: Active documentation
**Audience**: End users, support team
**Maintenance**: Update when new metrics or features added
