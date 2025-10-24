---
title: Backend Error Messages Displayed in Frontend
type: technical-reference
date: 2025-10-23
status: active
summary: Comprehensive catalog of all locations where backend API error messages are extracted and displayed to users in the frontend, including centralized error handlers, order operations, wallet management, and authentication flows.
tags:
  - error-handling
  - frontend
  - backend
  - api
  - user-experience
  - toast-notifications
related_documents:
  - frontend-only-error-messages.md
---

# Backend Error Messages Displayed in Frontend

This document catalogs all locations where backend API error messages are extracted and displayed to users in the frontend.

## Table of Contents

- [Centralized Error Handlers](#centralized-error-handlers)
- [Order Creation Mutations](#order-creation-mutations)
- [Order Status Changes](#order-status-changes)
- [Wallet Operations](#wallet-operations)
- [User Management](#user-management)
- [Perpetuals (Hyperliquid)](#perpetuals-hyperliquid)
- [Referrals](#referrals)
- [Authentication](#authentication)
- [Other Operations](#other-operations)
- [Summary](#summary)

---

## Centralized Error Handlers

### createErrorHandler Utility

**File:** `/src/lib/utils/createErrorHandler.ts`

**Lines 21-22:**

```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message ?? reason;
}
```

**Display Method:** Toast notification (failure type)
**Fallback:** "Unknown error"
**Also:** Re-throws error after displaying, logs to Sentry

**Used by the following mutations:**

- Transfer operations (`atomMutationTransfer.ts`)
- Create wallet (`atomMutationCreateWallet.ts`)
- Delete/archive wallet (`atomMutationDeleteWallet.ts`)
- Export seed phrase (`atomMutationExportSp.ts`)
- Withdraw funds (`atomMutationWithdraw.ts`)
- Change wallet name (`atomMutationChangeWalletName.ts`)
- Reactivate wallet (`atomMutationReactivateWallet.ts`)

---

### Wallet Import Error Handler

**File:** `/src/utils/walletImportErrorHandling.ts`

**Lines 31-33:**

```typescript
if (error instanceof AxiosError) {
  const status = error.response?.status;
  const message = error.response?.data?.message || error.message;
}
```

**Display Method:** Toast notification with user-friendly conversion
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

### Password Error Handler

**File:** `/src/app/(cook)/wallet-manager/utils/handlePasswordError.ts`

**Lines 8-12:**

```typescript
if (error instanceof AxiosError && error.response?.status === 403) {
  form.setError("password", {
    type: "manual",
    message: "Security Password is incorrect.",
  });
}
```

**Display Method:** Form validation error (inline)
**Note:** Uses custom frontend message, not backend message
**Used by:** Withdraw modal, transfer modal, wallet name change, export seed phrase

---

## Order Creation Mutations

### Limit Order

**File:** `/src/atoms/atomMutationLimitOrder.ts`

**Endpoint:** `POST /limit-orders`

**Lines 79-80:**

```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message;
}
```

**Display Pattern:**

- Toast: `Limit order failed due ${reason}`
- Fallback: "Unknown error"
- Also logs to Sentry

---

### TWAP Order

**File:** `/src/atoms/atomMutationTwapOrder.ts`

**Endpoint:** `POST /twap`

**Lines 95-96:**

```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message;
}
```

**Display Pattern:**

- Toast: `TWAP order failed due ${reason}`
- Fallback: "Unknown error"

---

### DCA Order

**File:** `/src/atoms/atomMutationDcaOrder.ts`

**Endpoint:** `POST /dca`

**Lines 82-83:**

```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message;
}
```

**Display Pattern:**

- Toast: `DCA order failed due ${reason}`
- Fallback: "Unknown error"

---

### Custom Order

**File:** `/src/atoms/atomMutationCustomOrder.ts`

**Endpoint:** `POST /custom-orders`

**Lines 89-90:**

```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message;
}
```

**Display Pattern:**

- Toast: `Custom order failed due ${reason}`
- Fallback: "Unknown error"

---

### VWAP Order

**File:** `/src/atoms/atomMutationVwapOrder.ts`

**Endpoint:** `POST /vwap`

**Lines 103-104:**

```typescript
if (error instanceof AxiosError) {
  reason = error?.response?.data?.message;
}
```

**Display Pattern:**

- Toast: `VWAP order failed due to ${reason}`
- Fallback: "Unknown error"

---

## Order Status Changes

### TWAP Status Change

**File:** `/src/atoms/atomMutationTwapStatusChange.ts`

**Endpoint:** `POST /twap/:orderId/status/:status`

**Lines 32-38:**

```typescript
if (!(error instanceof AxiosError)) {
  Sentry.captureException(new Error("TWAP_ORDER_ERROR"), {
    extra: { error, orderId },
  });
}
toast(`TWAP status change failed`, "failure");
```

**Display Pattern:**

- Toast: Generic message only
- **Does NOT show backend error message**
- Logs non-Axios errors to Sentry

**Alternative location:** `/src/app/(cook)/orders/hooks/useChangeTwapStatus.ts` (same pattern)

---

### DCA Status Change

**File:** `/src/app/(cook)/orders/hooks/useChangeDcaStatus.ts`

**Endpoint:** `POST /dca/:dcaId/status/:status`

**Lines 49-57:**

```typescript
onError: (error, { orderId }) => {
  if (!(error instanceof AxiosError)) {
    captureException(new Error("DCA_ORDER_ERROR"), {
      extra: { error, orderId },
    });
  }
  rollbackStatus(orderId);
  toast(`DCA status change failed`, "failure");
};
```

**Display Pattern:**

- Toast: Generic message only
- **Does NOT show backend error message**

---

### VWAP Status Change

**File:** `/src/app/(cook)/orders/hooks/useChangeVwapStatus.ts`

**Endpoint:** `POST /vwap/:orderId/status/:status`

**Lines 52-59:**

```typescript
onError: (error, { orderId }) => {
  if (!(error instanceof AxiosError)) {
    captureException(new Error("VWAP_ORDER_ERROR"), {
      extra: { error, orderId },
    });
  }
  rollbackStatus(orderId);
  toast(`VWAP status change failed`, "failure");
};
```

**Display Pattern:**

- Toast: Generic message only
- **Does NOT show backend error message**

---

### Limit Order Cancel

**File:** `/src/atoms/atomMutationCancelLimitOrder.ts`

**Endpoint:** `POST /limit-orders/cancel/:orderId`

**Lines 24-33:**

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

**Display Pattern:**

- Toast: Generic message only
- **Does NOT show backend error message**

---

## Wallet Operations

### Transfer Funds

**File:** `/src/atoms/atomMutationTransfer.ts`

**Endpoint:** `POST /wallets/transfer`

**Lines 44-47:**

```typescript
const errorHandlerAtom = createErrorHandlerAtom<Partial<TransferProps>>({
  toastMessage: (reason) => `Transfer failed due to: ${reason}`,
  sentryTag: "TRANSFER_ERROR",
  omitFields: ["password"],
});
```

**Display Pattern:**

- Uses `createErrorHandler`
- Extracts: `error?.response?.data?.message`
- Toast: `Transfer failed due to: ${backend_message}`
- Fallback: "Unknown error"

---

### Create Wallet

**File:** `/src/atoms/atomMutationCreateWallet.ts`

**Endpoint:** `POST /wallets/create`

**Lines 52-57:**

```typescript
onError: get(
  createErrorHandlerAtom<CreateWalletProps>({
    toastMessage: (reason) => `Creating Wallet failed due to: ${reason}`,
    sentryTag: "WALLET_CREATION_ERROR",
    omitFields: ["password"],
  }),
);
```

**Display Pattern:**

- Uses `createErrorHandler`
- Toast: `Creating Wallet failed due to: ${backend_message}`

---

### Delete/Archive Wallet

**File:** `/src/atoms/atomMutationDeleteWallet.ts`

**Endpoint:** `DELETE /wallets/:walletId`

**Lines 39-46:**

```typescript
onError: get(
  createErrorHandlerAtom<ArchiveWalletProps>({
    toastMessage: (reason, { isExternal }) =>
      `There was a problem ${isExternal ? "deleting" : "archiving"} your wallet due to: ${reason}.`,
    sentryTag: "WALLET_DELETE_ERROR",
    omitFields: ["password"],
  }),
);
```

**Display Pattern:**

- Uses `createErrorHandler`
- Toast: `There was a problem deleting/archiving your wallet due to: ${backend_message}.`

---

### Export Seed Phrase

**File:** `/src/atoms/atomMutationExportSp.ts`

**Endpoint:** `POST /wallets/export/:walletId`

**Lines 37-44:**

```typescript
onError: get(
  createErrorHandlerAtom<ExportSeedPhraseProps>({
    toastMessage: (reason) =>
      `Exporting Wallet Seed Phrase failed due to: ${reason}`,
    sentryTag: "EXPORT_WALLET_ERROR",
    omitFields: ["password"],
  }),
);
```

**Display Pattern:**

- Uses `createErrorHandler`
- Toast: `Exporting Wallet Seed Phrase failed due to: ${backend_message}`

---

### Withdraw Funds

**File:** `/src/atoms/atomMutationWithdraw.ts`

**Endpoint:** `POST /hyperliquid/account/withdraw` or `POST /hyperliquid/account/withdraw-slow`

**Lines 44-47:**

```typescript
const errorHandlerAtom = createErrorHandlerAtom<Partial<WithdrawProps>>({
  toastMessage: (reason) => `Withdraw failed due to: ${reason}`,
  sentryTag: "WITHDRAW_ERROR",
  omitFields: ["password"],
});
```

**Display Pattern:**

- Uses `createErrorHandler`
- Toast: `Withdraw failed due to: ${backend_message}`

---

### Change Wallet Name

**File:** `/src/atoms/atomMutationUpdateWalletName.ts`

**Endpoint:** `PUT /wallets/:walletId`

**Lines 35-40:**

```typescript
onError: get(
  createErrorHandlerAtom<UpdateWalletNameProps>({
    toastMessage: (reason) =>
      `There was a problem updating your wallet name due to: ${reason}.`,
    sentryTag: "WALLET_UPDATE_NAME_ERROR",
    omitFields: ["password"],
  }),
);
```

**Display Pattern:**

- Uses `createErrorHandler`
- Toast: `There was a problem updating your wallet name due to: ${backend_message}.`

---

### Reactivate Wallet

**File:** `/src/atoms/atomMutationReactivateWallet.ts`

**Endpoint:** `PUT /wallets/:walletId/activate`

**Lines 30-35:**

```typescript
onError: get(
  createErrorHandlerAtom<ReactivateWalletProps>({
    toastMessage: (reason) => `Failed to reactivate wallet due to: ${reason}`,
    sentryTag: "WALLET_REACTIVATION_ERROR",
  }),
);
```

**Display Pattern:**

- Uses `createErrorHandler`
- Toast: `Failed to reactivate wallet due to: ${backend_message}`

---

### Import Private Key

**File:** `/src/atoms/atomMutationPrivateKeyImport.ts`

**Endpoint:**

- `POST /wallets/import/init-private-key`
- `POST /wallets/import/complete-private-key`

**Lines 133-135:**

```typescript
onError: (error) => {
  handleWalletImportError(error);
};
```

**Display Pattern:**

- Uses specialized `handleWalletImportError`
- Extracts: `error.response?.data?.message || error.message`
- Categorizes errors and provides user-friendly messages
- Toast with converted message

---

## User Management

### Quick Operation (Buy/Sell)

**File:** `/src/atoms/atomMutationQuickOperation.ts`

**Endpoint:** `POST /token/quick_operation_v2`

**Lines 158-159:**

```typescript
if (error instanceof AxiosError) {
  message = `Transaction failed for ${ticker}: ${error?.response?.data?.message}`;
}
```

**Display Pattern:**

- Toast: `Transaction failed for ${ticker}: ${backend_message}`
- Fallback: Uses `error.message` for non-Axios errors
- **Note:** Frontend validation errors take precedence

---

### Update Cooking Tag

**File:** `/src/lib/hooks/useUserInfo.ts`

**Endpoint:** `PUT /user/info`

**Lines 52-55:**

```typescript
const errorMessage =
  error instanceof AxiosError && error?.response?.data?.message
    ? error.response.data.message
    : "Failed to update cooking tag. Please try again.";
toast(errorMessage, "failure");
```

**Display Pattern:**

- Toast: Direct backend message if available
- Fallback: "Failed to update cooking tag. Please try again."

---

### Add Recent Token

**File:** `/src/atoms/atomMutationAddRecentToken.ts`

**Endpoint:** `POST /token/recent-tokens` (via apiClient.tokenControllerAddRecentToken)

**Lines 27-28:**

```typescript
if (error instanceof AxiosError && error?.response?.data?.message) {
  reason = error.response.data.message;
}
```

**Display Pattern:**

- Toast: Backend message
- Fallback: "an unknown error"

---

### Fetch Wallets

**File:** `/src/atoms/atomQueryWallets.ts`

**Endpoint:** `GET /wallets`

**Lines 21-23:**

```typescript
onError: (error: Error) => {
  if (error instanceof Error) {
    toast(`Failed to fetch your wallets: ${error.message}`, "failure");
  }
};
```

**Display Pattern:**

- Toast: `Failed to fetch your wallets: ${error.message}`
- **Note:** Uses `Error.message`, which may or may not be from backend

---

### Fetch Linked Providers

**File:** `/src/atoms/atomQueryLinkedProviders.ts`

**Endpoint:** `GET /auth/providers` (via apiClient.authProvidersControllerGetUserProviders)

**Lines 13-15:**

```typescript
onError: (error: Error) => {
  if (error instanceof Error) {
    toast(`Failed to fetch linked providers: ${error.message}`, "failure");
  }
};
```

**Display Pattern:**

- Toast: `Failed to fetch linked providers: ${error.message}`

---

## Perpetuals (Hyperliquid)

### Place Market Order

**File:** `/src/app/(cook)/perpetuals/PerpetualsForm/atoms/atomMutationPlaceMarketOrder.ts`

**Endpoint:** `POST /hyperliquid/trading/market-order`

**Lines 46-53:**

```typescript
const errorMessages = response.data.response.data.statuses
  .filter((status) => status.error)
  .map((status) => status.error)
  .join(", ");

if (errorMessages) {
  throw new Error(errorMessages);
}
```

**Display Pattern:**

- Extracts error messages from order statuses in response
- Concatenates multiple errors with ", "
- Toast: `Error placing market order: ${reason}` (via error handler)

---

### Place Limit Order

**File:** `/src/app/(cook)/perpetuals/PerpetualsForm/atoms/atomMutationPlaceLimitOrder.ts`

**Endpoint:** `POST /hyperliquid/trading/limit-order`

**Lines 49-56:**

```typescript
const errorMessages = response.data.response.data.statuses
  .filter((status) => status.error)
  .map((status) => status.error)
  .join(", ");

if (errorMessages) {
  throw new Error(errorMessages);
}
```

**Display Pattern:**

- Extracts error messages from order statuses
- Toast: `Error placing limit order: ${reason}` (via error handler)

---

### Update Leverage

**File:** `/src/app/(cook)/perpetuals/PerpetualsForm/atoms/atomMutationUpdateLeverage.ts`

**Endpoint:** `POST /hyperliquid/trading/update-leverage`

**Lines 21-25:**

```typescript
onError: createErrorHandler({
  toastMessage: (reason) => `Updating leverage failed due to: ${reason}`,
  sentryTag: "PERPETUALS_UPDATE_LEVERAGE_ERROR",
});
```

**Display Pattern:**

- Uses `createErrorHandler`
- Toast: `Updating leverage failed due to: ${backend_message}`

---

### Hyperliquid Account Withdraw

**File:** `/src/components/ConvertFundsDialog/atoms/atomMutationHyperliquidAccountWithdraw.ts`

**Endpoint:**

- `GET /hyperliquid/account/validate-withdrawal/:amount` (validation)
- `POST /hyperliquid/account/withdraw` (quick convert)
- `POST /hyperliquid/account/withdraw-slow` (standard)

**Lines 37-45:**

```typescript
if (result.status !== "ok") {
  if (result.response.type === "err") {
    throw new Error(result.response.data);
  }
  throw new Error("Minimum USDC needed: ~15 USDC");
}
```

**Display Pattern:**

- Toast: `There was a problem making a withdrawal in your Perpetuals Wallet due to: ${reason}.` (via error handler)
- Throws backend validation reason directly

---

### Convert Funds Form

**File:** `/src/components/ConvertFundsDialog/ConvertFundsForm/ConvertFundsForm.tsx`

**Endpoint:**

- `POST /hyperliquid/account/deposit` or `POST /hyperliquid/account/deposit-slow` (deposit)
- `POST /hyperliquid/account/withdraw` or `POST /hyperliquid/account/withdraw-slow` (withdraw)

**Lines 163-166:**

```typescript
onError: (error) => {
  if (error instanceof AxiosError) {
    form.setError("amount", {
      message: error.response?.data?.message,
    });
  }
};
```

**Display Pattern:**

- Form field error (inline on amount field)
- Direct backend message, no fallback in this path

---

## Referrals

### Claim Rewards

**File:** `/src/atoms/atomMutationReferralsClaimRewards.ts`

**Endpoint:** `POST /referrals/rewards`

**Lines 18-22:**

```typescript
if (transferResult.message === "No pending rewards to claim.") {
  toast("No rewards to claim", "failure");
} else {
  toast("Rewards successfully claimed", "success");
}
```

**Display Pattern:**

- Checks backend message but displays custom frontend text
- In error handler (lines 36-39): Shows generic "Rewards claim failed"

---

## Authentication

### Link Provider

**File:** `/src/atoms/atomMutationLinkProvider.ts`

**Endpoint:** `POST /auth/providers/link`

**Lines 23-26:**

```typescript
if (error instanceof AxiosError && error.response?.data?.message) {
  throw new Error(error.response.data.message);
} else {
  throw new Error("Provider linking failed");
}
```

**Display Pattern:**

- Re-throws backend message
- Fallback: "Provider linking failed"
- **Note:** No toast here, handled by caller

---

### Unlink Provider

**File:** `/src/atoms/atomMutationUnlinkProvider.ts`

**Endpoint:** `DELETE /auth/providers/:providerType`

**Lines 30-33:**

```typescript
if (error instanceof AxiosError && error.response?.data?.message) {
  throw new Error(error.response.data.message);
} else {
  throw new Error("Provider unlinking failed");
}
```

**Display Pattern:**

- Re-throws backend message
- Fallback: "Provider unlinking failed"

---

### Telegram Authentication

**File:** `/src/lib/services/auth/telegramAuthUtils.ts`

**Endpoint:** (uses atomMutationTelegramLogin which calls backend Telegram auth endpoint)

**Lines 82-86:**

```typescript
onError: createErrorHandler({
  toastMessage: (reason) => `Telegram authentication failed: ${reason}`,
  sentryTag: "TELEGRAM_AUTH_ERROR",
});
```

**Display Pattern:**

- Uses `createErrorHandler`
- Toast: `Telegram authentication failed: ${backend_message}`

---

## Other Operations

### Search Tokens

**File:** `/src/atoms/atomQuerySearchTokens.ts`

**Endpoint:** `GET /token/search?query={query}`

**Lines 34-37:**

```typescript
onError: () => {
  toast("Failed token search", "failure");
};
```

**Display Pattern:**

- Toast: Generic message only
- **Does NOT show backend error message**

---

### Fetch Orders by Wallet

**File:** `/src/atoms/atomQueryOrdersByWallet.ts`

**Endpoint:** `GET /limit-orders?walletAddress={walletAddress}&limit={limit}`

**Lines 24-27:**

```typescript
onError: () => {
  toast("Failed to fetch user orders", "failure");
};
```

**Display Pattern:**

- Toast: Generic message only
- **Does NOT show backend error message**

---

### Fetch DCA Orders

**File:** `/src/atoms/atomQueryDcaOrdersByWallet.ts`

**Endpoint:** `GET /dca` (via apiClient.dcaControllerGetDcaByUserId)

**Lines 77-80:**

```typescript
onError: () => {
  toast("Failed to fetch DCA wallet orders", "failure");
};
```

**Display Pattern:**

- Toast: Generic message only
- **Does NOT show backend error message**

---

### Fetch TWAP Orders

**File:** `/src/atoms/atomQueryTwapOrdersByWallet.ts`

**Endpoint:** `GET /twap`

**Lines 98-101:**

```typescript
onError: () => {
  toast("Failed to fetch TWAP wallet orders", "failure");
};
```

**Display Pattern:**

- Toast: Generic message only
- **Does NOT show backend error message**

---

### Global Axios Interceptor

**File:** `/src/lib/api/api.ts`

**Lines 37-39:**

```typescript
if (axios.isAxiosError(error) && error.response?.status === 401) {
  store.set(atomStorageAccessToken, () => "");
}
```

**Display Pattern:**

- No user-facing message
- Silently clears auth token on 401

---

## Summary

### Patterns for Displaying Backend Errors

#### Pattern 1: `error?.response?.data?.message` → Toast

**Count:** 25+ locations

**Files:**

- All order creation mutations (Limit, TWAP, DCA, Custom, VWAP)
- Quick operation (buy/sell)
- createErrorHandler utility (used by 8+ mutations)
- User info updates
- Add recent token
- Perpetuals operations

**Format:** `"[Operation] failed due to: ${backend_message}"`

---

#### Pattern 2: Backend Message → Form Field Error

**Count:** 2 locations

**Files:**

- ConvertFundsForm (amount field)
- handlePasswordError (password field - uses custom message, not backend)

---

#### Pattern 3: Backend Message Checked, Custom Message Shown

**Count:** 6+ locations

**Files:**

- Order status changes (TWAP, DCA, VWAP)
- Limit order cancel
- Referrals claim
- Token/order queries

**Behavior:** Generic error message shown, backend message not displayed to user

---

#### Pattern 4: Specialized Error Processing

**Count:** 2 locations

**Files:**

- walletImportErrorHandling.ts (categorizes and translates errors)
- Perpetuals order placement (extracts from status array)

---

#### Pattern 5: Re-throw Backend Message

**Count:** 3 locations

**Files:**

- Link/unlink provider mutations
- Various query utilities

**Behavior:** Re-throws error with backend message for caller to handle

---

### Key Statistics

| Category                              | Count   |
| ------------------------------------- | ------- |
| Direct backend message in toast       | 25+     |
| Generic message (ignores backend)     | 6+      |
| Backend message in form field         | 2       |
| Specialized error processing          | 2       |
| Re-throws for caller                  | 3       |
| **Total backend error display sites** | **38+** |

---

### Common Fallback Messages

When backend doesn't provide a message:

- "Unknown error" (most common)
- "an unknown error" (lowercase variant)
- "[Operation] failed" (generic)

---

### Observations

1. **Most common extraction:** `error?.response?.data?.message`
2. **Centralized handling:** `createErrorHandler` used by 8+ mutations
3. **Inconsistency:** Some show backend messages, others don't
4. **Toast is primary:** Toast notifications are the main display method
5. **Form errors rare:** Only 2 places show backend errors inline in forms
6. **No global handler:** Each operation handles its own error display
7. **Sentry integration:** Most error handlers log to Sentry with context

---

## Complete Endpoint List

This section lists all backend API endpoints where error messages are extracted and displayed to users.

### Order Management Endpoints

| Endpoint                                              | Method | Error Display            | File                              |
| ----------------------------------------------------- | ------ | ------------------------ | --------------------------------- |
| `/limit-orders`                                       | POST   | Backend message in toast | `atomMutationLimitOrder.ts`       |
| `/twap`                                               | POST   | Backend message in toast | `atomMutationTwapOrder.ts`        |
| `/dca`                                                | POST   | Backend message in toast | `atomMutationDcaOrder.ts`         |
| `/custom-orders`                                      | POST   | Backend message in toast | `atomMutationCustomOrder.ts`      |
| `/vwap`                                               | POST   | Backend message in toast | `atomMutationVwapOrder.ts`        |
| `/twap/:orderId/status/:status`                       | POST   | Generic message only     | `atomMutationTwapStatusChange.ts` |
| `/dca/:dcaId/status/:status`                          | POST   | Generic message only     | `useChangeDcaStatus.ts`           |
| `/vwap/:orderId/status/:status`                       | POST   | Generic message only     | `useChangeVwapStatus.ts`          |
| `/limit-orders/cancel/:orderId`                       | POST   | Generic message only     | `atomMutationCancelLimitOrder.ts` |
| `/limit-orders?walletAddress={address}&limit={limit}` | GET    | Generic message only     | `atomQueryOrdersByWallet.ts`      |
| `/dca`                                                | GET    | Generic message only     | `atomQueryDcaOrdersByWallet.ts`   |
| `/twap`                                               | GET    | Generic message only     | `atomQueryTwapOrdersByWallet.ts`  |

### Wallet Management Endpoints

| Endpoint                               | Method | Error Display              | File                              |
| -------------------------------------- | ------ | -------------------------- | --------------------------------- |
| `/wallets`                             | GET    | Error.message in toast     | `atomQueryWallets.ts`             |
| `/wallets/create`                      | POST   | Backend message in toast   | `atomMutationCreateWallet.ts`     |
| `/wallets/:walletId`                   | DELETE | Backend message in toast   | `atomMutationDeleteWallet.ts`     |
| `/wallets/:walletId`                   | PUT    | Backend message in toast   | `atomMutationUpdateWalletName.ts` |
| `/wallets/:walletId/activate`          | PUT    | Backend message in toast   | `atomMutationReactivateWallet.ts` |
| `/wallets/transfer`                    | POST   | Backend message in toast   | `atomMutationTransfer.ts`         |
| `/wallets/export/:walletId`            | POST   | Backend message in toast   | `atomMutationExportSp.ts`         |
| `/wallets/import/init-private-key`     | POST   | Categorized error handling | `atomMutationPrivateKeyImport.ts` |
| `/wallets/import/complete-private-key` | POST   | Categorized error handling | `atomMutationPrivateKeyImport.ts` |

### Token & Trading Endpoints

| Endpoint                      | Method | Error Display            | File                            |
| ----------------------------- | ------ | ------------------------ | ------------------------------- |
| `/token/quick_operation_v2`   | POST   | Backend message in toast | `atomMutationQuickOperation.ts` |
| `/token/search?query={query}` | GET    | Generic message only     | `atomQuerySearchTokens.ts`      |
| `/token/recent-tokens`        | POST   | Backend message in toast | `atomMutationAddRecentToken.ts` |

### Perpetuals (Hyperliquid) Endpoints

| Endpoint                                           | Method | Error Display                 | File                                        |
| -------------------------------------------------- | ------ | ----------------------------- | ------------------------------------------- |
| `/hyperliquid/trading/market-order`                | POST   | Extracted from order statuses | `atomMutationPlaceMarketOrder.ts`           |
| `/hyperliquid/trading/limit-order`                 | POST   | Extracted from order statuses | `atomMutationPlaceLimitOrder.ts`            |
| `/hyperliquid/trading/update-leverage`             | POST   | Backend message in toast      | `atomMutationUpdateLeverage.ts`             |
| `/hyperliquid/account/deposit`                     | POST   | Form field error (inline)     | `ConvertFundsForm.tsx`                      |
| `/hyperliquid/account/deposit-slow`                | POST   | Form field error (inline)     | `ConvertFundsForm.tsx`                      |
| `/hyperliquid/account/withdraw`                    | POST   | Backend message in toast      | `atomMutationHyperliquidAccountWithdraw.ts` |
| `/hyperliquid/account/withdraw-slow`               | POST   | Backend message in toast      | `atomMutationHyperliquidAccountWithdraw.ts` |
| `/hyperliquid/account/validate-withdrawal/:amount` | GET    | Backend validation message    | `atomMutationHyperliquidAccountWithdraw.ts` |

### User & Authentication Endpoints

| Endpoint                        | Method | Error Display               | File                            |
| ------------------------------- | ------ | --------------------------- | ------------------------------- |
| `/user/info`                    | PUT    | Backend message in toast    | `useUserInfo.ts`                |
| `/auth/providers/link`          | POST   | Backend message (re-thrown) | `atomMutationLinkProvider.ts`   |
| `/auth/providers/:providerType` | DELETE | Backend message (re-thrown) | `atomMutationUnlinkProvider.ts` |
| `/auth/providers`               | GET    | Error.message in toast      | `atomQueryLinkedProviders.ts`   |
| Telegram auth endpoint          | POST   | Backend message in toast    | `telegramAuthUtils.ts`          |

### Referrals Endpoints

| Endpoint             | Method | Error Display           | File                                   |
| -------------------- | ------ | ----------------------- | -------------------------------------- |
| `/referrals/rewards` | POST   | Custom frontend message | `atomMutationReferralsClaimRewards.ts` |

### Summary by Error Display Pattern

**Backend message displayed (25+ endpoints):**

- All order creation endpoints (limit, TWAP, DCA, custom, VWAP)
- Most wallet management endpoints
- Quick operation endpoint
- User info update
- Recent token addition
- Perpetuals trading operations
- Link/unlink provider endpoints

**Generic message only (10+ endpoints):**

- Order status changes (TWAP, DCA, VWAP)
- Limit order cancellation
- Token/order query endpoints

**Form field error (2 endpoints):**

- Hyperliquid deposit/withdraw (ConvertFundsForm)

**Specialized handling (2 endpoints):**

- Wallet import (categorized error handling)
- Perpetuals orders (status array extraction)
