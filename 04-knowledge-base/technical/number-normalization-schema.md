---
title: Number Normalization Schema
type: technical-specification
date: 2025-10-23
status: active
summary: Number representation standards for Cooking.gg interface - defines formatting rules for currency, percentages, and token amounts with thousand separators, decimal precision, and abbreviation thresholds.
tags:
  - ui-ux
  - formatting
  - standards
  - numbers
  - display
related_documents:
  - error-messages-reference-guide.md
---

# Number Normalization Schema

Standard for all number representation in Cooking.gg except input fields.

## Core Rules

**Format Convention:**

- Thousands divider: `,` (comma)
- Decimal divider: `.` (point)
- Example: `999,999.99`

**Tooltip Behavior:**

- When hovering over a formatted value, display tooltip with complete unformatted value
- Exception: Only when strictly specified otherwise

---

## Formatting Rules by Magnitude

### Numbers > 999,999 (Millions)

**Format:** `n M` (no decimal places)

**Examples:**

| Displayed | Tooltip (Complete Value) | Type       |
| --------- | ------------------------ | ---------- |
| $10 M     | $10,000,000.12           | Currency   |
| 2 M %     | 2,123,456.012345 %       | Percentage |
| 234 M SOL | 234,003,193.001236 SOL   | Solana     |

**Rules:**

- Use M suffix
- No decimal places in display
- Round to nearest million
- Tooltip shows full precision

---

### Numbers > 99,999 (Thousands)

**Format:** `n.dd K` (up to 2 decimal places for the first hundred places)

**Examples:**

| Displayed   | Tooltip (Complete Value) | Type       | Note                |
| ----------- | ------------------------ | ---------- | ------------------- |
| $5.87 K     | $5,866.12                | Currency   | Values > 5 round up |
| 19.44 K %   | 19,442.023135 %          | Percentage |                     |
| 48.12 K SOL | 48,123.112345 SOL        | Solana     |                     |

**Rules:**

- Use K suffix
- Up to 2 decimal places
- Rounding: Values bigger than 5 round up
- Tooltip shows full precision

---

### Numbers < 999 (Standard)

**Format:** `n.dd` (2 decimal places)

**Examples:**

| Displayed | Tooltip (Complete Value) | Type       |
| --------- | ------------------------ | ---------- |
| $193.01   | $193.012345              | Currency   |
| 10.34 %   | 10.340145 %              | Percentage |

**Rules:**

- No suffix
- Show exactly 2 decimal places
- Rounding: Values bigger than 5 round up
- Tooltip shows full precision
- **Note:** This rule does NOT apply to Solana values (see special Solana rules below)

---

## Special Rules for Solana Values

### Solana Values < 10 (First 3 decimals ≠ 0)

**Format:** `n.dddddd` (up to 6 decimal places)

**Example:**

| Displayed | Note                          |
| --------- | ----------------------------- |
| 9.012345  | Values bigger than 5 round up |

**Rules:**

- Apply when value < 10
- Apply when first 3 decimal places are NOT all zeros
- Show up to 6 decimal places
- Rounding: Values bigger than 5 round up

---

### Solana Values < 10 (First 3 decimals = 0)

**Format:** `n.dₙddd` (subscript notation)

**Subscript value:** Represents the amount of zeros before the first three non-zero values

**Examples:**

| Displayed | Complete Value | Explanation        |
| --------- | -------------- | ------------------ |
| 0.0₃123   | 0.000123       | 3 zeros before 123 |
| 0.0₅456   | 0.00000456     | 5 zeros before 456 |
| 0.0₇891   | 0.0000000891   | 7 zeros before 891 |

**Rules:**

- Apply when value < 10
- Apply when first 3 decimal places ARE all zeros
- Use subscript (ₙ) to indicate number of leading zeros
- Show first 3 non-zero digits after the zeros
- Rounding: Values bigger than 5 round up

---

## Formatting Decision Tree

```
Is number > 999,999?
├─ YES → Format as "n M" (no decimals)
└─ NO
   │
   Is number > 99,999?
   ├─ YES → Format as "n.dd K" (2 decimals)
   └─ NO
      │
      Is number < 999?
      ├─ YES
      │  │
      │  Is value Solana AND < 10?
      │  ├─ YES
      │  │  │
      │  │  Are first 3 decimals = 0?
      │  │  ├─ YES → Format as "n.dₙddd" (subscript notation)
      │  │  └─ NO → Format as "n.dddddd" (6 decimals)
      │  │
      │  └─ NO → Format as "n.dd" (2 decimals)
      │
      └─ NO → Format as "n.dd" (2 decimals)
```

---

## Implementation Examples

### Currency (USD)

| Value         | Display | Tooltip        | Rule Applied       |
| ------------- | ------- | -------------- | ------------------ |
| 10,000,000.12 | $10 M   | $10,000,000.12 | > 999,999          |
| 5,866.12      | $5.87 K | $5,866.12      | > 99,999           |
| 193.012345    | $193.01 | $193.012345    | < 999 (2 decimals) |

### Percentage (%)

| Value            | Display   | Tooltip            | Rule Applied       |
| ---------------- | --------- | ------------------ | ------------------ |
| 2,123,456.012345 | 2 M %     | 2,123,456.012345 % | > 999,999          |
| 19,442.023135    | 19.44 K % | 19,442.023135 %    | > 99,999           |
| 10.340145        | 10.34 %   | 10.340145 %        | < 999 (2 decimals) |

### Solana (SOL)

| Value              | Display      | Tooltip                | Rule Applied                            |
| ------------------ | ------------ | ---------------------- | --------------------------------------- |
| 234,003,193.001236 | 234 M SOL    | 234,003,193.001236 SOL | > 999,999                               |
| 48,123.112345      | 48.12 K SOL  | 48,123.112345 SOL      | > 99,999                                |
| 9.012345           | 9.012345 SOL | 9.012345 SOL           | < 10, first 3 decimals ≠ 0 (6 decimals) |
| 0.000123           | 0.0₃123 SOL  | 0.000123 SOL           | < 10, first 3 decimals = 0 (subscript)  |

---

## Rounding Rules

**General Principle:** Values bigger than 5 round up

**Applied across all formatting:**

- When showing 2 decimal places: round 3rd decimal if > 5
- When showing 6 decimal places: round 7th decimal if > 5
- When abbreviating to K/M: round accordingly

**Examples:**

- `5.866` → `5.87` (6 > 5, rounds up)
- `5.864` → `5.86` (4 ≤ 5, rounds down)
- `193.012345` → `193.01` (2 ≤ 5, rounds down)

---

## Exclusions

**Input Fields:** These rules do NOT apply to input fields where users enter numbers

**During Input:**

- Users can type any format
- No automatic formatting while typing
- Apply formatting only on blur/submit

---

## Technical Implementation

### TypeScript Type Definitions

```typescript
enum NumberFormat {
  MILLIONS = "millions", // > 999,999
  THOUSANDS = "thousands", // > 99,999
  STANDARD = "standard", // < 999
  SOLANA_EXTENDED = "solana_extended", // < 10, first 3 decimals ≠ 0
  SOLANA_SUBSCRIPT = "solana_subscript", // < 10, first 3 decimals = 0
}

interface FormatConfig {
  value: number;
  type: "currency" | "percentage" | "solana";
  showTooltip: boolean;
}

interface FormattedNumber {
  display: string;
  tooltip: string;
  format: NumberFormat;
}
```

### Format Function Signature

```typescript
function formatNumber(config: FormatConfig): FormattedNumber {
  // Implementation based on rules above
}
```

---

## Display Specifications

### Font & Styling

**Subscript Numbers:**

- Use subscript Unicode characters: ₀₁₂₃₄₅₆₇₈₉
- Or CSS: `vertical-align: sub; font-size: smaller;`
- Ensure consistent baseline alignment

### Tooltip Implementation

**Default Behavior:**

```tsx
<span title={completeValue}>{displayValue}</span>
```

**Requirements:**

- Instant show on hover
- Display complete unformatted value
- Use system tooltip or custom styled tooltip
- Should not obstruct number being viewed

---

## Testing Matrix

### Test Cases for Each Rule

| Input          | Expected Display | Expected Tooltip | Format Type      |
| -------------- | ---------------- | ---------------- | ---------------- |
| 10,000,000.12  | 10 M             | 10,000,000.12    | MILLIONS         |
| 5,866.12       | 5.87 K           | 5,866.12         | THOUSANDS        |
| 193.012345     | 193.01           | 193.012345       | STANDARD         |
| 9.012345 (SOL) | 9.012345         | 9.012345         | SOLANA_EXTENDED  |
| 0.000123 (SOL) | 0.0₃123          | 0.000123         | SOLANA_SUBSCRIPT |

### Edge Cases

| Scenario             | Input     | Expected Display |
| -------------------- | --------- | ---------------- |
| Exactly 999,999      | 999,999   | 999,999.00       |
| Exactly 1,000,000    | 1,000,000 | 1 M              |
| Exactly 99,999       | 99,999    | 99,999.00        |
| Exactly 100,000      | 100,000   | 100.00 K         |
| SOL exactly 10       | 10.0      | 10.00            |
| SOL exactly 9.999999 | 9.999999  | 10.000000        |

---

## Summary

**Abbreviation Thresholds:**

- Millions (M): > 999,999 → 0 decimals
- Thousands (K): > 99,999 → 2 decimals
- Standard (non-Solana): < 999 → exactly 2 decimals

**Solana Special Cases:**

- Values ≥ 100,000: Follow standard K/M abbreviation rules
- Values < 10 with non-zero first 3 decimals → 6 decimals
- Values < 10 with zero first 3 decimals → subscript notation

**Universal Rules:**

- Thousands separator: comma (,)
- Decimal separator: point (.)
- Rounding: values > 5 round up
- Tooltips: always show complete value (unless specified otherwise)
- Input fields: excluded from these rules

---

**Last Updated:** 2025-10-23
**Source Document:** Number representation.md
**Applies To:** All number displays except input fields
