---
title: Backend Error Handling Guide
type: technical-reference
date: 2025-10-24
status: active
summary: Complete guide to backend error handling covering all API endpoints, error messages, frontend display patterns, code implementation details, and recommendations. Combines endpoint-by-endpoint error catalog with technical implementation patterns.
tags:
  - error-handling
  - backend
  - frontend
  - api
  - user-experience
  - error-messages
  - endpoints
  - implementation
related_documents:
  - frontend-only-error-messages.md
  - error-messages-reference-guide.md
---

# Backend Error Handling Guide

**Version:** 2.0 (Merged from comprehensive report and implementation guide)
**Last Updated:** October 24, 2025
**Maintainer:** Backend Team

This document provides both a business/product view of all backend error messages and a technical implementation view of how errors are handled in the frontend code.

## Quick Navigation

- [Overview](#overview)
- [Error Display Patterns](#error-display-patterns)
- [Frontend Implementation Patterns](#frontend-implementation-patterns)
- [Order Management Endpoints](#1-order-management-endpoints)
- [Wallet Management Endpoints](#2-wallet-management-endpoints)
- [Token & Trading Endpoints](#3-token--trading-endpoints)
- [Perpetuals (Hyperliquid) Endpoints](#4-perpetuals-hyperliquid-endpoints)
- [User & Authentication Endpoints](#5-user--authentication-endpoints)
- [Referrals Endpoints](#6-referrals-endpoints)
- [System-Wide Errors](#7-system-wide-errors)
- [Summary & Statistics](#8-summary--statistics)
- [Recommendations](#9-recommendations)

---

## Overview

This guide documents all error messages from backend API endpoints and how they are displayed to users in the frontend. It serves multiple audiences:

- **Product/UX Teams**: Understand what error messages users see
- **Backend Developers**: Know what errors to throw and their display impact
- **Frontend Developers**: Understand error extraction and display patterns
- **QA/Support**: Reference for testing and troubleshooting

**Legend:**
- ✅ **Backend message displayed**: The exact error message from the backend is shown to the user in a toast/notification
- ⚠️ **Generic message only**: A generic error message is shown, backend message is not displayed
- 🔍 **Categorized handling**: Frontend applies custom logic based on error type/code
- 📝 **Form field error**: Error is displayed inline in a form field

---

## Error Display Patterns

### Display Methods

1. **Toast Notification** (51% of errors)
   - Most common display method
   - Temporary notification at top/bottom of screen
   - Can show success, failure, or info states

2. **Form Field Validation** (30% of errors)
   - Inline error below form field
   - Prevents form submission until resolved
   - Real-time validation feedback

3. **Thrown Errors** (19% of errors)
   - Re-thrown for parent component to handle
   - Often logged to Sentry
   - May or may not display to user

### Common Extraction Pattern

```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message ?? fallback;
}
```

**Standard locations for backend messages:**
- `error.response.data.message` (primary)
- `error.response.data` (some endpoints)
- `error.message` (fallback for network errors)

---

## Frontend Implementation Patterns

### Pattern 1: Centralized Error Handler (`createErrorHandler`)

**File:** `/src/lib/utils/createErrorHandler.ts`

**Implementation:**
```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message ?? reason;
}
```

**Display:** Toast notification (failure type)
**Fallback:** "Unknown error"
**Features:** Re-throws after displaying, logs to Sentry

**Used by 8+ mutations:**
- Transfer operations (`atomMutationTransfer.ts`)
- Create wallet (`atomMutationCreateWallet.ts`)
- Delete/archive wallet (`atomMutationDeleteWallet.ts`)
- Export seed phrase (`atomMutationExportSp.ts`)
- Withdraw funds (`atomMutationWithdraw.ts`)
- Change wallet name (`atomMutationChangeWalletName.ts`)
- Reactivate wallet (`atomMutationReactivateWallet.ts`)
- Update leverage (`atomMutationUpdateLeverage.ts`)

---

### Pattern 2: Wallet Import Error Handler

**File:** `/src/utils/walletImportErrorHandling.ts`

**Implementation:**
```typescript
if (error instanceof AxiosError) {
  const status = error.response?.status;
  const message = error.response?.data?.message || error.message;
}
```

**Features:**
- Categorizes errors by type (rate limit, validation, network, API, encryption)
- Converts technical backend messages to user-friendly text
- Provides retry logic with exponential backoff
- Extracts `retry-after` header for rate limiting

**Status code handling:**
- `429` → Rate limit message with wait time
- `400` → Validation error with backend message
- `500-504` → Generic server error message

**Used by:** Private key import mutation (`atomMutationPrivateKeyImport.ts`)

---

### Pattern 3: Password Error Handler

**File:** `/src/app/(cook)/wallet-manager/utils/handlePasswordError.ts`

**Implementation:**
```typescript
if (error instanceof AxiosError && error.response?.status === 403) {
  form.setError("password", {
    type: "manual",
    message: "Security Password is incorrect.",
  });
}
```

**Display:** Form validation error (inline)
**Note:** Uses custom frontend message, not backend message

**Used by:**
- Withdraw modal
- Transfer modal
- Wallet name change
- Export seed phrase

---

### Pattern 4: Order Creation Mutations

**Files:**
- `atomMutationLimitOrder.ts`
- `atomMutationTwapOrder.ts`
- `atomMutationDcaOrder.ts`
- `atomMutationCustomOrder.ts`
- `atomMutationVwapOrder.ts`

**Implementation:**
```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message;
}
```

**Display Pattern:**
- Toast: `{OrderType} order failed due to ${reason}`
- Fallback: "Unknown error"
- Also logs to Sentry

---

### Pattern 5: Order Status Changes

**Files:**
- `atomMutationTwapStatusChange.ts`
- `useChangeDcaStatus.ts`
- `useChangeVwapStatus.ts`

**Implementation:**
```typescript
onError: (error, { orderId }) => {
  if (!(error instanceof AxiosError)) {
    captureException(new Error("{ORDER_TYPE}_ERROR"), {
      extra: { error, orderId },
    });
  }
  rollbackStatus(orderId);
  toast(`{OrderType} status change failed`, "failure");
}
```

**Display Pattern:**
- Toast: Generic message only
- **Does NOT show backend error message**
- Logs non-Axios errors to Sentry

---

## 1. Order Management Endpoints

### 1.1 POST `/limit-orders` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationLimitOrder.ts:79-80`

**Frontend Validation (lines 48-110):**
```typescript
if (!wallet) throw new Error("No wallet selected");
if (amount <= 0) throw new Error("Amount must be greater than 0");
// Balance checks for SOL and tokens
```

**Backend Error Messages:**

1. `"takeProfit and stopLoss must be accompanied by at least one trigger condition (e.g., targetPrice, marketCapTarget, holdersCount)."`
   - **When:** User tries to create a limit order with only takeProfit/stopLoss conditions without a valid trigger
   - **Type:** `BadRequestException` (400)

2. `"Invalid Wallet Address"`
   - **When:** Wallet doesn't exist for the user
   - **Type:** `BadRequestException` (400)

3. `"Invalid Solana address format"`
   - **When:** Provided wallet address is not a valid Solana address
   - **Type:** `BadRequestException` (400)

4. `"Insufficient SOL balance considering locked orders."`
   - **When:** User doesn't have enough SOL balance for a buy order, considering amounts locked in other pending orders
   - **Type:** `BadRequestException` (400)

5. `"Insufficient token balance considering locked orders."`
   - **When:** User doesn't have enough token balance for a sell order, considering amounts locked in other pending orders
   - **Type:** `BadRequestException` (400)

6. `"Price not found for Mint {mintAddress}"`
   - **When:** Unable to fetch price data for the specified token
   - **Type:** `BadRequestException` (400)

---

### 1.2 POST `/limit-orders/cancel/:orderId` ⚠️

**Frontend Display:** Generic message only
**Implementation:** `atomMutationCancelLimitOrder.ts:24-33`

**Display Pattern:**
```typescript
catch (error) {
  if (!(error instanceof AxiosError)) {
    Sentry.captureException(new Error("LIMIT_ORDER_ERROR"), {
      extra: { error, orderId },
    });
  }
  toast(`Limit order cancel for ${ticker} failed`, "failure");
}
```

**Backend Error Messages:**

1. `"Order with ID {id} not found."`
   - **When:** Order doesn't exist or doesn't belong to the user
   - **Type:** `NotFoundException` (404)

2. `"Only pending orders can be canceled."`
   - **When:** User tries to cancel an order that's not in PENDING status
   - **Type:** `BadRequestException` (400)

---

### 1.3 GET `/limit-orders?walletAddress={address}&limit={limit}` ⚠️

**Frontend Display:** Generic message only
**Implementation:** `atomQueryOrdersByWallet.ts:24-27`

**Display Pattern:**
```typescript
onError: () => {
  toast("Failed to fetch user orders", "failure");
}
```

**Backend Error Messages:**
- No explicit error messages thrown in controller
- Errors would be generic database/validation errors

---

### 1.4 POST `/twap` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationTwapOrder.ts:95-96`

**Frontend Validation (lines 46-102):**
```typescript
if (!wallet) throw new Error("No wallet selected");
// Similar validation to limit orders
```

**Backend Error Messages:**

1. `"Wallet not found"`
   - **When:** Specified wallet doesn't belong to the user
   - **Type:** `BadRequestException` (400)

---

### 1.5 POST `/twap/:orderId/status/:status` ⚠️

**Frontend Display:** Generic message only
**Implementation:** `atomMutationTwapStatusChange.ts:32-38`

**Backend Error Messages:**

1. `"Status not allowed!"`
   - **When:** Provided status is not in the TWAP_STATUS_MAP
   - **Type:** `BadRequestException` (400)

---

### 1.6 GET `/twap` ⚠️

**Frontend Display:** Generic message only
**Implementation:** `atomQueryTwapOrdersByWallet.ts:98-101`

**Backend Error Messages:**
- No explicit error messages thrown in controller

---

### 1.7 POST `/dca` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationDcaOrder.ts:82-83`

**Frontend Validation (lines 42-78):**
```typescript
if (!wallet) throw new Error("No wallet selected");
// Similar validation to other order types
```

**Backend Error Messages:**

1. `"Wallet not found"`
   - **When:** Specified wallet doesn't belong to the user
   - **Type:** `BadRequestException` (400)

---

### 1.8 POST `/dca/:dcaId/status/:status` ⚠️

**Frontend Display:** Generic message only
**Implementation:** `useChangeDcaStatus.ts:49-57`

**Backend Error Messages:**

1. `"Status not allowed!"`
   - **When:** Provided status is not in the DCA_STATUS_MAP
   - **Type:** `BadRequestException` (400)

---

### 1.9 GET `/dca` ⚠️

**Frontend Display:** Generic message only
**Implementation:** `atomQueryDcaOrdersByWallet.ts:77-80`

**Backend Error Messages:**
- No explicit error messages thrown in controller

---

### 1.10 POST `/vwap` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationVwapOrder.ts:103-104`

**Frontend Validation (lines 50-98):**
```typescript
if (!wallet) throw new Error("No wallet selected");
// Similar validation to other order types
```

**Backend Error Messages:**

1. `"Wallet not found"`
   - **When:** Specified wallet doesn't belong to the user
   - **Type:** `BadRequestException` (400)

---

### 1.11 POST `/vwap/:orderId/status/:status` ⚠️

**Frontend Display:** Generic message only
**Implementation:** `useChangeVwapStatus.ts:52-59`

**Backend Error Messages:**

1. `"Status not allowed!"`
   - **When:** Provided status is not in the VWAP_STATUS_MAP
   - **Type:** `BadRequestException` (400)

---

### 1.12 POST `/custom-orders` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationCustomOrder.ts:89-90`

**Frontend Validation (lines 44-84):**
```typescript
if (!wallet) throw new Error("No wallet selected");
// Similar validation to other order types
```

**Backend Error Messages:**
- **Note:** No `/custom-orders` endpoint found in the codebase. This may be a legacy endpoint or handled differently.

---

## 2. Wallet Management Endpoints

### 2.1 GET `/wallets` ⚠️

**Frontend Display:** Error.message in toast
**Implementation:** `atomQueryWallets.ts:21-23`

**Display Pattern:**
```typescript
onError: (error: Error) => {
  if (error instanceof Error) {
    toast(`Failed to fetch your wallets: ${error.message}`, "failure");
  }
}
```

**Backend Error Messages:**

1. `"Security is not enabled"`
   - **When:** User tries to access wallets without enabling security
   - **Type:** `BadRequestException` (400)

---

### 2.2 POST `/wallets/create` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationCreateWallet.ts:52-57` (uses createErrorHandler)

**Display Pattern:**
```typescript
onError: get(
  createErrorHandlerAtom<CreateWalletProps>({
    toastMessage: (reason) => `Creating Wallet failed due to: ${reason}`,
    sentryTag: "WALLET_CREATION_ERROR",
    omitFields: ["password"],
  }),
)
```

**Backend Error Messages:**

1. `"Security data is required"`
   - **When:** Creating an external wallet without security data
   - **Type:** `BadRequestException` (400)

2. `"Wallet name is required."`
   - **When:** No wallet name provided
   - **Type:** `BadRequestException` (400)

3. `"Address is required for external wallets"`
   - **When:** Creating external wallet without address
   - **Type:** `BadRequestException` (400)

4. `"This address is already registered"`
   - **When:** External wallet address already exists
   - **Type:** `BadRequestException` (400)

5. `"Invalid Solana address format"`
   - **When:** Provided address is not a valid Solana address
   - **Type:** `BadRequestException` (400)

6. `"A wallet with this name already exists."`
   - **When:** User already has a wallet with the same name
   - **Type:** `BadRequestException` (400)

7. `"User has reached the maximum number of wallets allowed: {MAX_WALLETS_PER_USER}"`
   - **When:** User tries to create more wallets than allowed
   - **Type:** `BadRequestException` (400)

8. `"Wallet address is required"`
   - **When:** Address is missing for external wallet
   - **Type:** `BadRequestException` (400)

9. `"User not found"`
   - **When:** User doesn't exist in the system
   - **Type:** `BadRequestException` (400)

10. `"Invalid Solana address format"` (from Turnkey service)
    - **When:** Turnkey validates the address and finds it invalid
    - **Type:** `BadRequestException` (400)

11. `"Failed to create wallet after {MAX_RETRIES} attempts"`
    - **When:** Turnkey wallet creation fails after retries
    - **Type:** `BadRequestException` (400)

---

### 2.3 DELETE `/wallets/:walletId` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationDeleteWallet.ts:39-46` (uses createErrorHandler)

**Display Pattern:**
```typescript
onError: get(
  createErrorHandlerAtom<ArchiveWalletProps>({
    toastMessage: (reason, { isExternal }) =>
      `There was a problem ${isExternal ? "deleting" : "archiving"} your wallet due to: ${reason}.`,
    sentryTag: "WALLET_DELETE_ERROR",
    omitFields: ["password"],
  }),
)
```

**Backend Error Messages:**

1. `"Wallet {walletId} not found"`
   - **When:** Wallet doesn't exist for the user
   - **Type:** `BadRequestException` (400)

2. `"Not supported operation"`
   - **When:** Trying to delete a wallet of unsupported type
   - **Type:** `BadRequestException` (400)

3. `"Security data is required"`
   - **When:** Deleting external wallet without security verification
   - **Type:** `BadRequestException` (400)

4. `"Wallet not found"` (from service)
   - **When:** Wallet doesn't exist
   - **Type:** `NotFoundException` (404)

5. `"Cannot delete wallet with active balance. Please withdraw all funds first."`
   - **When:** Wallet has SOL or token balance
   - **Type:** `BadRequestException` (400)

---

### 2.4 PUT `/wallets/:walletId` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationUpdateWalletName.ts:35-40` (uses createErrorHandler)

**Display Pattern:**
```typescript
onError: get(
  createErrorHandlerAtom<UpdateWalletNameProps>({
    toastMessage: (reason) =>
      `There was a problem updating your wallet name due to: ${reason}.`,
    sentryTag: "WALLET_UPDATE_NAME_ERROR",
    omitFields: ["password"],
  }),
)
```

**Backend Error Messages:**

1. `"Wallet {walletId} not found"`
   - **When:** Wallet doesn't exist for the user
   - **Type:** `BadRequestException` (400)

2. `"Not supported operation"`
   - **When:** Trying to update a wallet of unsupported type
   - **Type:** `BadRequestException` (400)

3. `"Security data is required"`
   - **When:** Updating external wallet without security verification
   - **Type:** `BadRequestException` (400)

4. `"Wallet not found"` (from service)
   - **When:** Wallet doesn't exist
   - **Type:** `BadRequestException` (400)

---

### 2.5 PUT `/wallets/:walletId/activate` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationReactivateWallet.ts:30-35` (uses createErrorHandler)

**Display Pattern:**
```typescript
onError: get(
  createErrorHandlerAtom<ReactivateWalletProps>({
    toastMessage: (reason) => `Failed to reactivate wallet due to: ${reason}`,
    sentryTag: "WALLET_REACTIVATION_ERROR",
  }),
)
```

**Backend Error Messages:**

1. `"Wallet not found"`
   - **When:** Wallet doesn't exist
   - **Type:** `NotFoundException` (404)

2. `"Not supported operation"`
   - **When:** Trying to activate a wallet of unsupported type
   - **Type:** `BadRequestException` (400)

3. `"Wallet is already active"`
   - **When:** Wallet is already in active state
   - **Type:** `BadRequestException` (400)

---

### 2.6 POST `/wallets/transfer` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationTransfer.ts:44-47` (uses createErrorHandler)

**Display Pattern:**
```typescript
const errorHandlerAtom = createErrorHandlerAtom<Partial<TransferProps>>({
  toastMessage: (reason) => `Transfer failed due to: ${reason}`,
  sentryTag: "TRANSFER_ERROR",
  omitFields: ["password"],
});
```

**Frontend Validation:** `TransferModal.tsx:49-77`
```typescript
if (!senderWallet) {
  toast("You must select a sender wallet.", "failure");
  return;
}
if (amount === 0) {
  toast("Amount transferred cannot be 0.", "failure");
  return;
}
```

**Backend Error Messages:**

1. `"Not supported operation"` (recipient wallet)
   - **When:** Trying to transfer to unsupported wallet type
   - **Type:** `BadRequestException` (400)

2. `"Security data is required"`
   - **When:** External transfer without security verification
   - **Type:** `BadRequestException` (400)

3. `"Amount must be greater than zero"`
   - **When:** Transfer amount is zero or negative
   - **Type:** `BadRequestException` (400)

4. `"Sender wallet not found"`
   - **When:** Source wallet doesn't exist
   - **Type:** `NotFoundException` (404)

5. `"Sender wallet does not belong to the authenticated user"`
   - **When:** User tries to transfer from another user's wallet
   - **Type:** `BadRequestException` (400)

6. `"Not supported operation"` (sender wallet)
   - **When:** Sender wallet type is not supported
   - **Type:** `BadRequestException` (400)

---

### 2.7 POST `/wallets/export/:walletId` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationExportSp.ts:37-44` (uses createErrorHandler)

**Display Pattern:**
```typescript
onError: get(
  createErrorHandlerAtom<ExportSeedPhraseProps>({
    toastMessage: (reason) =>
      `Exporting Wallet Seed Phrase failed due to: ${reason}`,
    sentryTag: "EXPORT_WALLET_ERROR",
    omitFields: ["password"],
  }),
)
```

**Password Validation:** `handlePasswordError.ts:8-12`
```typescript
if (error instanceof AxiosError && error.response?.status === 403) {
  form.setError("password", {
    type: "manual",
    message: "Security Password is incorrect.",
  });
}
```

**Backend Error Messages:**

1. `"Wallet not found"`
   - **When:** Wallet doesn't exist
   - **Type:** `NotFoundException` (404)

2. `"Not supported operation"`
   - **When:** Trying to export unsupported wallet type
   - **Type:** `BadRequestException` (400)

3. `"Invalid Wallet Address"`
   - **When:** Wallet address is invalid
   - **Type:** `BadRequestException` (400)

---

### 2.8 POST `/wallets/import/init-private-key` 🔍

**Frontend Display:** Categorized error handling
**Implementation:** `atomMutationPrivateKeyImport.ts:133-135` (uses walletImportErrorHandling)

**Error Handler:** `walletImportErrorHandling.ts:31-33`
```typescript
if (error instanceof AxiosError) {
  const status = error.response?.status;
  const message = error.response?.data?.message || error.message;

  // Categorizes as: rate limit, validation, network, API, or encryption errors
  // Converts to user-friendly messages
}
```

**Frontend Validation:** `walletImportValidation.ts`
- Private key format validation (64 hex chars)
- Mnemonic validation (12/24 words)
- Wallet name validation (3-50 chars)
- Security checks for malicious content

**Backend Error Messages:**

1. `"User not found"`
   - **When:** User doesn't exist
   - **Type:** `BadRequestException` (400)

2. `"User ID mismatch"`
   - **When:** Session user ID doesn't match authenticated user
   - **Type:** `BadRequestException` (400)

3. `"A wallet with name '{name}' already exists for this user"`
   - **When:** Wallet name already exists
   - **Type:** `BadRequestException` (400)

4. `"This private key is already imported for user {userId}"`
   - **When:** Private key was already imported
   - **Type:** `BadRequestException` (400)

---

### 2.9 POST `/wallets/import/complete-private-key` 🔍

**Frontend Display:** Categorized error handling
**Implementation:** Same as init-private-key

**Backend Error Messages:**

1. `"User not found"`
   - **When:** User doesn't exist
   - **Type:** `BadRequestException` (400)

2. `"Import session data mismatch"`
   - **When:** Session data doesn't match
   - **Type:** `BadRequestException` (400)

3. `"This private key has already been imported by user {userId}"`
   - **When:** Private key already imported
   - **Type:** `BadRequestException` (400)

---

### 2.10 GET `/wallets/balances?addresses={addresses}` ⚠️

**Frontend Display:** Not mentioned in report, but errors are thrown

**Backend Error Messages:**

1. `"addresses query parameter is required"`
   - **When:** No addresses provided
   - **Type:** `BadRequestException` (400)

2. `"At least one address is required"`
   - **When:** Empty addresses list
   - **Type:** `BadRequestException` (400)

3. `"Maximum 100 addresses allowed per request"`
   - **When:** More than 100 addresses requested
   - **Type:** `BadRequestException` (400)

4. `"Invalid Solana address: {address}"`
   - **When:** Invalid address in the list
   - **Type:** `BadRequestException` (400)

---

## 3. Token & Trading Endpoints

### 3.1 POST `/token/quick_operation_v2` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationQuickOperation.ts:158-159`

**Display Pattern:**
```typescript
if (error instanceof AxiosError) {
  message = `Transaction failed for ${ticker}: ${error?.response?.data?.message}`;
}
```

**Frontend Validation (lines 84-153):**
```typescript
if (!wallet) throw new Error("No wallet selected");
if (amount <= 0) throw new Error("Amount must be greater than 0");
if (side === "buy" && solBalance < amount) {
  throw new Error("Insufficient SOL balance");
}
if (side === "sell" && tokenBalance < amount) {
  throw new Error("Insufficient token balance");
}
// Additional checks for priority fees
```

**Backend Error Messages:**

1. `"Wallet not found"`
   - **When:** Wallet doesn't exist for user
   - **Type:** `BadRequestException` (400)

2. `"User doesn't match with wallet address."`
   - **When:** Wallet doesn't belong to the user
   - **Type:** `BadRequestException` (400)

---

### 3.2 GET `/token/search?query={query}` ⚠️

**Frontend Display:** Generic message only
**Implementation:** `atomQuerySearchTokens.ts:34-37`

**Display Pattern:**
```typescript
onError: () => {
  toast("Failed token search", "failure");
}
```

**Backend Error Messages:**
- No explicit error messages thrown in controller

---

### 3.3 POST `/token/recent-token` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationAddRecentToken.ts:27-28`

**Display Pattern:**
```typescript
if (error instanceof AxiosError && error?.response?.data?.message) {
  reason = error.response.data.message;
}
```

**Backend Error Messages:**
- No explicit error messages thrown in controller
- Returns success message: `"Token successfully added to recent tokens list."`

---

### 3.4 GET `/token/:mint/info` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"Missing mint address"`
   - **When:** Mint address parameter is missing
   - **Type:** `BadRequestException` (400)

2. `"Token not found"`
   - **When:** Token data doesn't exist for the mint
   - **Type:** `NotFoundException` (404)

---

### 3.5 GET `/token/:mint/diamond-hands-early-trades` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"Missing mint address"`
   - **When:** Mint address parameter is missing
   - **Type:** `BadRequestException` (400)

2. `"Token Data not found"`
   - **When:** Token data doesn't exist
   - **Type:** `NotFoundException` (404)

---

### 3.6 GET `/token/:mint/bars` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"Missing timeframe"`
   - **When:** Timeframe parameter is missing
   - **Type:** `BadRequestException` (400)

2. `"Invalid timeframe (allowed: 1, 300)"`
   - **When:** Timeframe is not 1 or 300 seconds
   - **Type:** `BadRequestException` (400)

3. `"Limit must be a positive integer"`
   - **When:** Limit is not a valid positive integer
   - **Type:** `BadRequestException` (400)

4. `"Limit cannot be greater than 1000"`
   - **When:** Limit exceeds maximum
   - **Type:** `BadRequestException` (400)

5. `"Missing mint address"`
   - **When:** Mint address is missing (from service)
   - **Type:** `BadRequestException` (400)

---

### 3.7 GET `/token/v2/:mint/bars` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"Missing mint address"`
   - **When:** Mint address parameter is missing
   - **Type:** `BadRequestException` (400)

2. `"Missing or invalid secondsQty"`
   - **When:** secondsQty parameter is missing or not a number
   - **Type:** `BadRequestException` (400)

3. `"Time range is required"`
   - **When:** from or to timestamp is missing
   - **Type:** `BadRequestException` (400)

4. `"Invalid time range. From timestamp must be less than to timestamp."`
   - **When:** from timestamp is greater than to timestamp
   - **Type:** `BadRequestException` (400)

5. `"countback must be a positive integer"`
   - **When:** countback is not a positive integer
   - **Type:** `BadRequestException` (400)

---

## 4. Perpetuals (Hyperliquid) Endpoints

### 4.1 POST `/hyperliquid/trading/market-order` ✅

**Frontend Display:** Extracted from order statuses
**Implementation:** `atomMutationPlaceMarketOrder.ts:46-53`

**Display Pattern:**
```typescript
const errorMessages = response.data.response.data.statuses
  .filter((status) => status.error)
  .map((status) => status.error)
  .join(", ");

if (errorMessages) {
  throw new Error(errorMessages);
}
// Caught by error handler: `Error placing market order: ${reason}`
```

**Backend Error Messages:**

1. `"No HyperLiquid wallet found for user"`
   - **When:** User doesn't have a HyperLiquid wallet configured
   - **Type:** `BadRequestException` (400)

2. `"Wallet does not have an associated sub-organization"`
   - **When:** Wallet lacks required subOrganizationId
   - **Type:** `BadRequestException` (400)

3. `"Insufficient margin for market order"`
   - **When:** Not enough margin to execute the order
   - **Type:** `BadRequestException` (400)

4. `"Failed to place market order for {coin}: {error.message}"`
   - **When:** Order placement fails
   - **Type:** `InternalServerErrorException` (500)

---

### 4.2 POST `/hyperliquid/trading/limit-order` ✅

**Frontend Display:** Extracted from order statuses
**Implementation:** `atomMutationPlaceLimitOrder.ts:49-56`

**Display Pattern:** Same as market order (extracts from status array)

**Backend Error Messages:**

1. `"No HyperLiquid wallet found for user"`
   - **When:** User doesn't have a HyperLiquid wallet
   - **Type:** `BadRequestException` (400)

2. `"Wallet does not have an associated sub-organization"`
   - **When:** Wallet lacks required subOrganizationId
   - **Type:** `BadRequestException` (400)

3. `"Insufficient margin for limit order"`
   - **When:** Not enough margin to execute the order
   - **Type:** `BadRequestException` (400)

4. `"Failed to place limit order for {coin}: {error.message}"`
   - **When:** Order placement fails
   - **Type:** `InternalServerErrorException` (500)

---

### 4.3 POST `/hyperliquid/trading/update-leverage` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationUpdateLeverage.ts:21-25` (uses createErrorHandler)

**Display Pattern:**
```typescript
onError: createErrorHandler({
  toastMessage: (reason) => `Updating leverage failed due to: ${reason}`,
  sentryTag: "PERPETUALS_UPDATE_LEVERAGE_ERROR",
});
```

**Backend Error Messages:**

1. `"No HyperLiquid wallet found for user"`
   - **When:** User doesn't have a HyperLiquid wallet
   - **Type:** `BadRequestException` (400)

2. `"Failed to update leverage for {coin}"`
   - **When:** Leverage update fails
   - **Type:** `InternalServerErrorException` (500)

---

### 4.4 POST `/hyperliquid/trading/close-position` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"No position found for {coin}"`
   - **When:** User doesn't have any position for the coin
   - **Type:** `BadRequestException` (400)

2. `"No open position for {coin}"`
   - **When:** Position exists but size is 0
   - **Type:** `BadRequestException` (400)

3. `"Wallet does not have an associated sub-organization"`
   - **When:** Wallet lacks required subOrganizationId
   - **Type:** `BadRequestException` (400)

4. `"No HyperLiquid wallet found for user"`
   - **When:** User doesn't have a HyperLiquid wallet
   - **Type:** `BadRequestException` (400)

5. `"Failed to close position for {coin}: {error.message}"`
   - **When:** Position closing fails
   - **Type:** `InternalServerErrorException` (500)

---

### 4.5 POST `/hyperliquid/trading/cancel-order` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"No HyperLiquid wallet found for user"`
   - **When:** User doesn't have a HyperLiquid wallet
   - **Type:** `BadRequestException` (400)

2. `"Failed to cancel order: {error.message}"`
   - **When:** Order cancellation fails
   - **Type:** `InternalServerErrorException` (500)

---

### 4.6 POST `/hyperliquid/trading/cancel-all-orders` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"No HyperLiquid wallet found for user"`
   - **When:** User doesn't have a HyperLiquid wallet
   - **Type:** `BadRequestException` (400)

2. `"Failed to cancel all orders: {error.message}"`
   - **When:** Bulk cancellation fails
   - **Type:** `InternalServerErrorException` (500)

---

### 4.7 GET `/hyperliquid/trading/open-orders` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"Unable to get user positions"`
   - **When:** Failed to fetch user positions
   - **Type:** `BadRequestException` (400)

2. `"Failed to retrieve open orders: {error.message}"`
   - **When:** Order retrieval fails
   - **Type:** `InternalServerErrorException` (500)

---

### 4.8 POST `/hyperliquid/account/deposit` 📝

**Frontend Display:** Form field error (inline)
**Implementation:** `ConvertFundsForm.tsx:163-166`

**Display Pattern:**
```typescript
onError: (error) => {
  if (error instanceof AxiosError) {
    form.setError("amount", {
      message: error.response?.data?.message,
    });
  }
}
```

**Backend Error Messages:**

1. `"Source wallet subOrganizationId is required for deposit"`
   - **When:** Source wallet doesn't have subOrganizationId
   - **Type:** `BadRequestException` (400)

2. `"Source wallet not found"`
   - **When:** Wallet doesn't exist
   - **Type:** `BadRequestException` (400)

3. `"Not supported operation"`
   - **When:** Wallet type is not supported
   - **Type:** `BadRequestException` (400)

4. `"Source wallet does not belong to the authenticated user"`
   - **When:** Wallet doesn't belong to user
   - **Type:** `BadRequestException` (400)

5. `"Insufficient SOL balance for deposit and transaction fees"`
   - **When:** Not enough SOL in wallet
   - **Type:** `BadRequestException` (400)

---

### 4.9 POST `/hyperliquid/account/deposit-slow` 📝

**Frontend Display:** Form field error (inline)
**Implementation:** Same as deposit endpoint

**Backend Error Messages:**

1. `"Source wallet subOrganizationId is required for batch deposit"`
   - **When:** Source wallet doesn't have subOrganizationId
   - **Type:** `BadRequestException` (400)

2. `"User wallet subOrganizationId not found"`
   - **When:** Wallet lacks subOrganizationId
   - **Type:** `BadRequestException` (400)

3. `"Source wallet not found"`
   - **When:** Wallet doesn't exist
   - **Type:** `BadRequestException` (400)

4. `"Not supported operation"`
   - **When:** Wallet type is not supported
   - **Type:** `BadRequestException` (400)

5. `"Source wallet does not belong to the authenticated user"`
   - **When:** Wallet doesn't belong to user
   - **Type:** `BadRequestException` (400)

6. `"Invalid operation type"`
   - **When:** Operation type is not 'deposit' or 'withdraw'
   - **Type:** `BadRequestException` (400)

---

### 4.10 POST `/hyperliquid/account/withdraw` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `atomMutationHyperliquidAccountWithdraw.ts:37-45` (uses createErrorHandler)

**Display Pattern:**
```typescript
// Validation first
if (result.status !== "ok") {
  if (result.response.type === "err") {
    throw new Error(result.response.data);
  }
  throw new Error("Minimum USDC needed: ~15 USDC");
}
// Error handler: `There was a problem making a withdrawal in your Perpetuals Wallet due to: ${reason}.`
```

**Frontend Validation:** `WithdrawModal.tsx:54-76`
```typescript
if (!senderWallet) {
  toast("You must select a sender wallet.", "failure");
  return;
}
if (amount === 0) {
  toast("Amount transferred cannot be 0.", "failure");
  return;
}
```

**Backend Error Messages:**

1. `"Destination wallet subOrganizationId is required for withdrawal"`
   - **When:** Destination wallet doesn't have subOrganizationId
   - **Type:** `BadRequestException` (400)

2. `"Destination wallet not found"`
   - **When:** Wallet doesn't exist
   - **Type:** `BadRequestException` (400)

3. `"Destination wallet does not belong to the authenticated user"`
   - **When:** Wallet doesn't belong to user
   - **Type:** `BadRequestException` (400)

4. `"Cannot withdraw: Insufficient USDC balance on HyperLiquid"`
   - **When:** Not enough USDC in HyperLiquid account
   - **Type:** `BadRequestException` (400)

5. `"Cannot withdraw: Withdrawal would leave account below minimum balance requirement"`
   - **When:** Withdrawal would violate minimum balance
   - **Type:** `BadRequestException` (400)

6. `"Cannot withdraw: Insufficient account value (including unrealized PnL)"`
   - **When:** Account value too low
   - **Type:** `BadRequestException` (400)

---

### 4.11 POST `/hyperliquid/account/withdraw-slow` ✅

**Frontend Display:** Backend message in toast
**Implementation:** Same as withdraw endpoint

**Backend Error Messages:**

1. `"User wallet subOrganizationId not found"`
   - **When:** Wallet lacks subOrganizationId
   - **Type:** `BadRequestException` (400)

2. `"Invalid operation type"`
   - **When:** Operation type is not 'deposit' or 'withdraw'
   - **Type:** `BadRequestException` (400)

3. Similar validation errors as withdraw endpoint

---

### 4.12 GET `/hyperliquid/account/validate-withdrawal/:amount` ✅

**Frontend Display:** Backend validation message
**Implementation:** `atomMutationHyperliquidAccountWithdraw.ts:37-45`

**Backend Response:**
- Returns validation object with `isValid`, `estimatedSolAmount`, `solPrice`, and optional `reason`
- Possible reasons:
  - `"Insufficient USDC balance"`
  - `"Withdrawal would leave account below minimum"`
  - `"Insufficient account value including unrealized PnL"`

---

## 5. User & Authentication Endpoints

### 5.1 PUT `/user/info` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `useUserInfo.ts:52-55`

**Display Pattern:**
```typescript
const errorMessage =
  error instanceof AxiosError && error?.response?.data?.message
    ? error.response.data.message
    : "Failed to update cooking tag. Please try again.";
toast(errorMessage, "failure");
```

**Backend Error Messages:**

1. `"User info not found"`
   - **When:** User info doesn't exist
   - **Type:** `NotFoundException` (404)

2. `"Cooking tag can only be updated once"`
   - **When:** User tries to update cooking tag more than once
   - **Type:** `BadRequestException` (400)

3. `"Cooking tag must be between 3 and 15 characters"`
   - **When:** Cooking tag length is invalid
   - **Type:** `BadRequestException` (400)

4. `"Cooking tag must contain only alphanumeric characters, underscores, hyphens, and periods"`
   - **When:** Cooking tag contains invalid characters
   - **Type:** `BadRequestException` (400)

5. `"Cooking tag contains reserved words"`
   - **When:** Cooking tag uses reserved words
   - **Type:** `BadRequestException` (400)

6. `"Cooking tag is already taken"`
   - **When:** Another user already uses this cooking tag
   - **Type:** `BadRequestException` (400)

7. `"User not found"`
   - **When:** User doesn't exist
   - **Type:** `BadRequestException` (400)

---

### 5.2 POST `/auth/providers/link` ✅

**Frontend Display:** Backend message (re-thrown)
**Implementation:** `atomMutationLinkProvider.ts:23-26`

**Display Pattern:**
```typescript
if (error instanceof AxiosError && error.response?.data?.message) {
  throw new Error(error.response.data.message);
} else {
  throw new Error("Provider linking failed");
}
```

**Backend Error Messages:**

1. `"Provider type already linked to account"`
   - **When:** User already has this provider type linked
   - **Type:** `BadRequestException` (400)

2. `"Provider already linked to another account"`
   - **When:** This provider is already linked to a different account
   - **Type:** `ConflictException` (409)

3. `"Invalid Telegram Login data"`
   - **When:** Telegram authentication data is invalid
   - **Type:** `BadRequestException` (400)

4. `"Unauthorized! The data has expired."`
   - **When:** Telegram login data has expired (older than 1 day)
   - **Type:** `BadRequestException` (400)

5. `"Invalid provider ID"`
   - **When:** Telegram provider ID is invalid
   - **Type:** `BadRequestException` (400)

6. `"Access token is required for email or auth0 provider"`
   - **When:** No access token provided for email/auth0
   - **Type:** `BadRequestException` (400)

7. Auth0-specific errors:
   - `"Invalid token format"`
   - `"Token missing key ID (kid)"`
   - `"Token has expired"`
   - `"Invalid token signature or format"`
   - `"Token is not active yet"`
   - `"Token validation failed"`
   - All type: `UnauthorizedException` (401)

---

### 5.3 DELETE `/auth/providers/:providerType` ✅

**Frontend Display:** Backend message (re-thrown)
**Implementation:** `atomMutationUnlinkProvider.ts:30-33`

**Display Pattern:**
```typescript
if (error instanceof AxiosError && error.response?.data?.message) {
  throw new Error(error.response.data.message);
} else {
  throw new Error("Provider unlinking failed");
}
```

**Backend Error Messages:**

1. `"Cannot unlink the only remaining authentication method"`
   - **When:** User tries to remove their last provider
   - **Type:** `BadRequestException` (400)

2. `"Provider not found for this user"`
   - **When:** User doesn't have this provider linked
   - **Type:** `NotFoundException` (404)

---

### 5.4 GET `/auth/providers` ⚠️

**Frontend Display:** Error.message in toast
**Implementation:** `atomQueryLinkedProviders.ts:13-15`

**Display Pattern:**
```typescript
onError: (error: Error) => {
  if (error instanceof Error) {
    toast(`Failed to fetch linked providers: ${error.message}`, "failure");
  }
}
```

**Backend Error Messages:**

1. `"Unable to fetch user providers or metadata"`
   - **When:** Failed to retrieve providers or metadata
   - **Type:** `BadRequestException` (400)

---

### 5.5 POST `/auth/telegram` ✅

**Frontend Display:** Backend message in toast
**Implementation:** `telegramAuthUtils.ts:82-86` (uses createErrorHandler)

**Display Pattern:**
```typescript
onError: createErrorHandler({
  toastMessage: (reason) => `Telegram authentication failed: ${reason}`,
  sentryTag: "TELEGRAM_AUTH_ERROR",
});
```

**Backend Error Messages:**
- Same as Telegram provider errors in link endpoint:
  - `"Invalid Telegram Login data"`
  - `"Unauthorized! The data has expired."`
  - `"Invalid provider ID"`

---

### 5.6 POST `/user/security` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"Current security data is required"`
   - **When:** Updating security without providing current credentials
   - **Type:** `BadRequestException` (400)

2. `"User security data not found"`
   - **When:** User doesn't have security data set
   - **Type:** `BadRequestException` (400)

3. `"Invalid security data"`
   - **When:** Provided security credentials are incorrect
   - **Type:** `ForbiddenException` (403)

---

### 5.7 DELETE `/user/account` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"User security data not found"`
   - **When:** User doesn't have security data
   - **Type:** `BadRequestException` (400)

2. `"Invalid security data"`
   - **When:** Security verification fails
   - **Type:** `ForbiddenException` (403)

---

### 5.8 GET `/user/referrer-username?referralCode={code}` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"Referral code is required"`
   - **When:** No referral code provided
   - **Type:** `BadRequestException` (400)

2. `"Referral code not found"`
   - **When:** Referral code doesn't exist
   - **Type:** `BadRequestException` (400)

3. `"User not found for referral code"`
   - **When:** User associated with code doesn't exist
   - **Type:** `BadRequestException` (400)

---

### 5.9 PUT `/user/priority-fee` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"User not found"`
   - **When:** User doesn't exist
   - **Type:** `BadRequestException` (400)

2. `"If auto priority fee is disabled, custom priority fee must be provided and must be a positive number"`
   - **When:** Auto priority disabled but no valid custom fee provided
   - **Type:** `BadRequestException` (400)

---

## 6. Referrals Endpoints

### 6.1 POST `/referrals/rewards` ✅

**Frontend Display:** Custom frontend message
**Implementation:** `atomMutationReferralsClaimRewards.ts:18-22`

**Display Pattern:**
```typescript
if (transferResult.message === "No pending rewards to claim.") {
  toast("No rewards to claim", "failure");
} else {
  toast("Rewards successfully claimed", "success");
}
// Error handler (lines 36-39): Shows generic "Rewards claim failed"
```

**Backend Error Messages:**

1. `"User not found"`
   - **When:** User doesn't exist
   - **Type:** `BadRequestException` (400)

2. `"No active wallet found for user {userId}"`
   - **When:** User has no active wallet to receive rewards
   - **Type:** `BadRequestException` (400)

3. `"Invalid reward amount: {rewardAmount}."`
   - **When:** Reward amount is invalid or zero
   - **Type:** `BadRequestException` (400)

4. `"Insufficient balance in rewards wallet"`
   - **When:** Rewards wallet doesn't have enough SOL
   - **Type:** `BadRequestException` (400)

5. `"Insufficient balance after accounting for transaction fees"`
   - **When:** Not enough balance to cover transfer + fees
   - **Type:** `BadRequestException` (400)

---

### 6.2 PUT `/referrals/codes` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"User already has a custom referral code"`
   - **When:** User tries to update code more than once
   - **Type:** `BadRequestException` (400)

2. `"Referral code cannot be empty"`
   - **When:** New referral code is empty
   - **Type:** `BadRequestException` (400)

3. `"Referral code must be between 3 and 20 characters"`
   - **When:** Code length is invalid
   - **Type:** `BadRequestException` (400)

4. `"Invalid code. Please review and correct."`
   - **When:** Code contains invalid characters (must be alphanumeric, underscores, hyphens only)
   - **Type:** `BadRequestException` (400)

5. `"Referral code is already taken. Please choose another one."`
   - **When:** Another user already uses this code
   - **Type:** `BadRequestException` (400)

6. `"User not found"`
   - **When:** User doesn't exist
   - **Type:** `BadRequestException` (400)

7. `"Old referral code does not match"`
   - **When:** Provided old code doesn't match current code
   - **Type:** `BadRequestException` (400)

8. `"Failed to update referral code"`
   - **When:** Update operation fails
   - **Type:** `BadRequestException` (400)

---

### 6.3 POST `/referrals/link-referral-code` ✅

**Frontend Display:** Backend message in toast

**Backend Error Messages:**

1. `"User not found"`
   - **When:** User doesn't exist
   - **Type:** `BadRequestException` (400)

2. `"User already has a referrer"`
   - **When:** User is already linked to a referrer
   - **Type:** `BadRequestException` (400)

3. `"Referral code cannot be empty"`
   - **When:** Empty referral code provided
   - **Type:** `BadRequestException` (400)

4. `"Referrer user not found"`
   - **When:** Referrer doesn't exist
   - **Type:** `BadRequestException` (400)

5. `"Users cannot refer themselves"`
   - **When:** User tries to use their own referral code
   - **Type:** `BadRequestException` (400)

6. `"Referral code not found"`
   - **When:** Provided code doesn't exist
   - **Type:** `BadRequestException` (400)

7. `"User not found for referral code"`
   - **When:** User for the code doesn't exist
   - **Type:** `BadRequestException` (400)

8. `"Cannot link referral code to user of different referrer"`
   - **When:** Code belongs to different referrer than expected
   - **Type:** `BadRequestException` (400)

---

## 7. System-Wide Errors

### 7.1 Authentication & Authorization

**Error Messages:**

1. `"Unauthorized"` (401)
   - **When:** No valid JWT token provided or token is invalid/expired
   - **Type:** `UnauthorizedException`
   - **Frontend Handling:** `api.ts:37-39` - Silently clears auth token

2. `"User role not found"` (403)
   - **When:** User doesn't have a role assigned
   - **Type:** `ForbiddenException`

3. `"Insufficient permissions"` (403)
   - **When:** User doesn't have required role for the endpoint
   - **Type:** `ForbiddenException`

4. `"Invalid refresh token"` (401)
   - **When:** Refresh token is invalid, expired, or payload is incorrect
   - **Type:** `UnauthorizedException`

5. `"User not found"` (400)
   - **When:** User ID from token doesn't exist in database
   - **Type:** `BadRequestException`

---

### 7.2 Solana Wallet Authentication

**Error Messages:**

1. `"Authentication failed"` (400)
   - **When:** Signature verification fails or message format is invalid
   - **Type:** `BadRequestException`

2. `"Invalid public key format"` (400)
   - **When:** Public key is not a valid Solana address
   - **Type:** `BadRequestException`

3. `"Message signature has expired (valid for 5 minutes)"` (400)
   - **When:** Signed message is older than 5 minutes
   - **Type:** `BadRequestException`

4. `"Invalid domain in message"` (400)
   - **When:** Message domain doesn't match configured domain
   - **Type:** `BadRequestException`

5. `"Invalid message format"` (400)
   - **When:** Message doesn't follow expected SIWS format
   - **Type:** `BadRequestException`

---

### 7.3 Whitelist (if enabled)

**Error Messages:**

1. `"Whitelist validation failed: wallet is required"`
   - **When:** No wallet address provided
   - **Type:** `BadRequestException` (400)

2. `"Wallet address must be a string"`
   - **When:** Wallet address is not a string
   - **Type:** `BadRequestException` (400)

3. `"Access denied. User not in whitelist."`
   - **When:** Wallet is not in the whitelist
   - **Type:** `BadRequestException` (400)

---

### 7.4 Global Axios Interceptor

**Implementation:** `/src/lib/api/api.ts:37-39`

```typescript
if (axios.isAxiosError(error) && error.response?.status === 401) {
  store.set(atomStorageAccessToken, () => "");
}
```

**Behavior:**
- No user-facing message
- Silently clears auth token on 401
- Forces re-authentication

---

## 8. Summary & Statistics

### Error Display Methods

| Method | Count | Percentage | Description |
|--------|-------|------------|-------------|
| **Toast Notification** | 38+ | ~65% | Temporary notification with backend message |
| **Generic Toast** | 10+ | ~17% | Generic message, backend error not shown |
| **Form Field Error** | 2 | ~3% | Inline validation with backend message |
| **Specialized Handling** | 2 | ~3% | Custom error categorization |
| **Re-throw** | 3 | ~5% | Backend message re-thrown for caller |
| **Silent** | 1 | ~2% | No user message (auth token clear) |
| **Total** | **56+** | **100%** | Total error handling locations |

---

### Error Types Distribution

| HTTP Status | Exception Type | Count | Percentage |
|-------------|---------------|-------|------------|
| 400 | `BadRequestException` | ~120 | ~90% |
| 404 | `NotFoundException` | ~8 | ~6% |
| 401 | `UnauthorizedException` | ~4 | ~3% |
| 403 | `ForbiddenException` | ~2 | ~1% |
| 409 | `ConflictException` | ~1 | <1% |
| 500 | `InternalServerErrorException` | ~3 | <1% |

---

### Frontend Implementation Patterns

| Pattern | Usage Count | Files |
|---------|-------------|-------|
| `error?.response?.data?.message` → Toast | 25+ | Order mutations, quick operation, user info |
| `createErrorHandler` utility | 8+ | Wallet operations, perpetuals |
| Generic message (ignores backend) | 6+ | Order status changes, queries |
| Form field error | 2 | ConvertFundsForm, password validation |
| Specialized processing | 2 | Wallet import, perpetuals orders |
| Re-throw for caller | 3 | Provider link/unlink |

---

### Endpoints by Display Pattern

#### Backend Message Displayed (25+ endpoints)

**Order Creation:**
- POST `/limit-orders`
- POST `/twap`
- POST `/dca`
- POST `/vwap`
- POST `/custom-orders`

**Wallet Management:**
- POST `/wallets/create`
- DELETE `/wallets/:walletId`
- PUT `/wallets/:walletId`
- PUT `/wallets/:walletId/activate`
- POST `/wallets/transfer`
- POST `/wallets/export/:walletId`

**Trading:**
- POST `/token/quick_operation_v2`
- POST `/token/recent-token`

**Perpetuals:**
- POST `/hyperliquid/trading/market-order`
- POST `/hyperliquid/trading/limit-order`
- POST `/hyperliquid/trading/update-leverage`
- POST `/hyperliquid/account/withdraw`

**User/Auth:**
- PUT `/user/info`
- POST `/auth/providers/link`
- DELETE `/auth/providers/:providerType`
- POST `/auth/telegram`

---

#### Generic Message Only (10+ endpoints)

**Order Operations:**
- POST `/limit-orders/cancel/:orderId`
- GET `/limit-orders`
- POST `/twap/:orderId/status/:status`
- GET `/twap`
- POST `/dca/:dcaId/status/:status`
- GET `/dca`
- POST `/vwap/:orderId/status/:status`

**Queries:**
- GET `/token/search`
- GET `/auth/providers`

---

#### Form Field Error (2 endpoints)

**Perpetuals:**
- POST `/hyperliquid/account/deposit`
- POST `/hyperliquid/account/deposit-slow`

---

#### Specialized Handling (2 endpoints)

**Wallet Import:**
- POST `/wallets/import/init-private-key`
- POST `/wallets/import/complete-private-key`

---

### Top Error Scenarios

| Scenario | Frequency | Examples |
|----------|-----------|----------|
| **Wallet validation** | High | Invalid addresses, insufficient balance, wallet not found |
| **User validation** | High | User not found, invalid credentials, permission denied |
| **Security verification** | Medium | Missing security data, invalid PIN/password |
| **Resource validation** | Medium | Token not found, order not found, invalid parameters |
| **Business logic** | Medium | Already exists, status conflicts, limit exceeded |
| **Network/Server** | Low | Connection timeouts, 500 errors, service unavailable |

---

### Common Fallback Messages

When backend doesn't provide a message:

- `"Unknown error"` (most common)
- `"an unknown error"` (lowercase variant)
- `"[Operation] failed"` (generic)
- Custom frontend message for specific operations

---

## 9. Recommendations

### For Frontend Team

1. **Consistent Error Handling**
   - Standardize all endpoints to display backend messages instead of generic errors
   - Use `createErrorHandler` pattern for all mutations
   - Avoid mixing generic and specific error messages

2. **Error Code Classification**
   - Implement error code mapping for better UX messaging
   - Create user-friendly translations for technical errors
   - Maintain consistency in error tone and voice

3. **Validation Feedback**
   - Add inline validation for common errors before submission
   - Validate wallet addresses, amounts, and formats client-side
   - Provide real-time feedback as user types

4. **Retry Logic**
   - Implement retry mechanisms for `InternalServerErrorException` (500) errors
   - Add exponential backoff for rate-limited operations
   - Show retry progress to users

5. **Error Tracking**
   - Add analytics for error frequency to identify pain points
   - Track which errors users encounter most often
   - Monitor error resolution rates

6. **User Experience**
   - Provide actionable error messages (what went wrong + how to fix)
   - Include links to help documentation when relevant
   - Test error messages with actual users

---

### For Backend Team

1. **Error Message Consistency**
   - Standardize error message formats across all services
   - Use consistent capitalization and punctuation
   - Follow a template: "Action failed: reason" or "Cannot action: reason"

2. **Error Codes**
   - Consider adding custom error codes to help frontend categorize errors
   - Use error code prefixes by domain (e.g., WAL001, ORD001)
   - Document error codes in API specification

3. **Detailed Context**
   - Include more context in error messages
   - Show expected vs actual values when validation fails
   - Provide hints for resolution when possible

4. **Input Validation**
   - Move more validation to DTOs with class-validator
   - Return consistent validation error structures
   - Group related validation errors together

5. **Error Documentation**
   - Keep this document updated as new endpoints are added
   - Document error conditions in OpenAPI/Swagger specs
   - Maintain error message catalog for QA testing

6. **HTTP Status Codes**
   - Use appropriate status codes consistently
   - 400 for client errors (validation, business logic)
   - 404 for not found resources
   - 403 for authorization failures
   - 500 only for unexpected server errors

---

### For Product/UX Team

1. **Error Message Review**
   - Review all error messages for clarity and tone
   - Ensure messages are user-friendly, not technical
   - Test messages with non-technical users

2. **Error Prevention**
   - Design UI to prevent common errors
   - Use input masks, dropdowns, and validation
   - Show balance checks before submission

3. **Error Recovery**
   - Provide clear next steps in error messages
   - Design recovery flows for common errors
   - Make it easy to retry or correct mistakes

4. **User Testing**
   - Test error scenarios in user research
   - Observe how users react to different error messages
   - Iterate based on feedback

---

### For QA/Testing Team

1. **Error Testing Matrix**
   - Test all error scenarios documented here
   - Verify error messages match specifications
   - Test both frontend validation and backend errors

2. **Error Consistency**
   - Check that similar errors show similar messages
   - Verify display method matches specification
   - Test error logging and Sentry integration

3. **Edge Cases**
   - Test network timeouts and disconnections
   - Test concurrent operations and race conditions
   - Test rate limiting and throttling

4. **Cross-Browser Testing**
   - Verify error displays work across browsers
   - Test toast notifications and form validations
   - Check error styling and accessibility

---

## Observations & Insights

1. **Most common extraction:** `error?.response?.data?.message` (used in 25+ locations)

2. **Centralized handling:** `createErrorHandler` utility provides consistency across 8+ mutations

3. **Inconsistency exists:** Some operations show backend messages, others use generic text

4. **Toast is primary:** Toast notifications are the dominant display method (65%)

5. **Form errors rare:** Only 2 locations show backend errors inline in forms

6. **No global handler:** Each operation handles its own error display

7. **Sentry integration:** Most error handlers log to Sentry with context

8. **Order operations:** Order creation shows backend errors, status changes show generic errors

9. **Wallet operations:** All use `createErrorHandler` for consistency

10. **Authentication:** Mix of approaches - some show backend messages, some use custom text

---

## Change Log

### Version 2.0 (2025-10-24)
- Merged comprehensive report with implementation guide
- Added frontend code implementation patterns
- Added code snippets for error extraction
- Enhanced with validation patterns
- Consolidated duplicate information
- Improved navigation and structure

### Version 1.0 (2025-10-23)
- Initial comprehensive report
- Endpoint-by-endpoint error catalog
- Basic statistics and recommendations

---

**Document Version:** 2.0
**Last Updated:** October 24, 2025
**Maintainer:** Backend Team
**Contributors:** Frontend Team, Product Team
