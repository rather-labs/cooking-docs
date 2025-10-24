---
title: Frontend-Only Error Messages
type: technical-reference
date: 2025-10-23
status: active
summary: Comprehensive catalog of all error messages generated and defined in the frontend codebase, including client-side validation, authentication flows, cryptographic operations, and transaction handling.
tags:
  - error-handling
  - frontend
  - validation
  - user-experience
  - client-side
related_documents:
  - backend-error-messages-displayed-in-frontend.md
---

# Frontend-Only Error Messages

This document catalogs all error messages that are generated and defined in the frontend codebase.

## Table of Contents

- [Client-Side Validation (Zod Schemas)](#client-side-validation-zod-schemas)
- [Frontend Logic Validation](#frontend-logic-validation)
- [Transaction Timeout & Status](#transaction-timeout--status)
- [Authentication](#authentication)
- [Cryptographic Validation](#cryptographic-validation)
- [React Context Validation](#react-context-validation)
- [Clipboard Operations](#clipboard-operations)
- [SSE & Network](#sse--network)
- [Configuration & Utilities](#configuration--utilities)
- [Solana Log Parser](#solana-log-parser)
- [Generic Fallback](#generic-fallback)

---

## Client-Side Validation (Zod Schemas)

### Wallet Import Validation

**File:** `/src/validation/walletImportValidation.ts`

| Line | Error Message                                                                           |
| ---- | --------------------------------------------------------------------------------------- |
| 9    | "Private key is required"                                                               |
| 17   | "Private key must be exactly 64 hexadecimal characters"                                 |
| 26   | "Invalid private key format"                                                            |
| 35   | "Mnemonic phrase is required"                                                           |
| 43   | "Mnemonic phrase must contain exactly 12 or 24 words"                                   |
| 53   | "Invalid mnemonic phrase. Please check that all words are correct."                     |
| 62   | "Please enter a private key or mnemonic phrase"                                         |
| 84   | "Please enter a valid private key (64 hex characters) or mnemonic phrase (12/24 words)" |
| 93   | "Wallet name is required"                                                               |
| 94   | "Wallet name must be at least 3 characters"                                             |
| 95   | "Wallet name must be no more than 50 characters"                                        |
| 104  | "Wallet name can only contain letters, numbers, spaces, hyphens, and underscores"       |
| 115  | "Security password is required"                                                         |
| 178  | "All required fields must be completed for this step"                                   |
| 281  | "Input contains potentially malicious content"                                          |
| 288  | "Please use real wallet data, not test/placeholder values"                              |

### Withdrawal Modal Validation

**File:** `/src/app/(cook)/wallet-manager/components/TotalBalance/components/WithdrawModal.tsx`

| Line | Error Message                      |
| ---- | ---------------------------------- |
| 54   | "You must select a sender wallet." |
| 59   | "Amount transferred cannot be 0."  |
| 69   | "Recipient must not be null"       |
| 76   | "Password is required"             |

### Transfer Modal Validation

**File:** `/src/app/(cook)/wallet-manager/components/TotalBalance/components/TransferModal.tsx`

| Line | Error Message                      |
| ---- | ---------------------------------- |
| 49   | "You must select a sender wallet." |
| 53   | "Amount transferred cannot be 0."  |

### Security Password Validation

**File:** `/src/components/auth/SecurityPasswordSection.tsx`

| Line | Error Message                                         |
| ---- | ----------------------------------------------------- |
| 23   | "This field is required." (password)                  |
| 32   | "Passwords do not match." (confirm password)          |
| 45   | "This field is required." (new password form)         |
| 49   | "Passwords do not match." (new password form)         |
| 53   | "New Password can't be the same as Current Password." |

### Transaction Fees Validation

**File:** `/src/components/v2/widgets/TxFeesPopover/TxFeesPopoverContent/TxFeesPopoverContent.tsx`

| Line | Error Message                     |
| ---- | --------------------------------- |
| 33   | "Slippage must be at least 0"     |
| 40   | "Priority Fee must be at least 0" |

### Perpetuals Form Validation

**File:** `/src/app/(cook)/perpetuals/types/form.ts`

| Line | Error Message                               |
| ---- | ------------------------------------------- |
| 23   | "limitPrice is required when type is LIMIT" |

---

## Frontend Logic Validation

### Quick Operations

**File:** `/src/atoms/atomMutationQuickOperation.ts`

| Line | Type            | Error Message                                           |
| ---- | --------------- | ------------------------------------------------------- |
| 84   | Thrown Error    | "No wallet selected"                                    |
| 88   | Thrown Error    | "Amount must be greater than 0"                         |
| 96   | Thrown Error    | "Insufficient SOL balance"                              |
| 103  | Thrown Error    | "Insufficient token balance"                            |
| 110  | Thrown Error    | "Insufficient SOL balance" (for sell with priority fee) |
| 135  | Toast (failure) | "Please select a wallet"                                |
| 141  | Toast (failure) | "Insufficient SOL balance"                              |
| 147  | Toast (failure) | "Insufficient token balance"                            |
| 153  | Toast (failure) | "Amount must be greater than 0"                         |

### Order Mutations (No Wallet Selected)

**Files and Lines:**

| File                                    | Line | Error Message        |
| --------------------------------------- | ---- | -------------------- |
| `/src/atoms/atomMutationLimitOrder.ts`  | 48   | "No wallet selected" |
| `/src/atoms/atomMutationDcaOrder.ts`    | 42   | "No wallet selected" |
| `/src/atoms/atomMutationTwapOrder.ts`   | 46   | "No wallet selected" |
| `/src/atoms/atomMutationVwapOrder.ts`   | 50   | "No wallet selected" |
| `/src/atoms/atomMutationCustomOrder.ts` | 44   | "No wallet selected" |

---

## Transaction Timeout & Status

**File:** `/src/atoms/atomTransactionStatusQueue.ts`

| Line    | Type            | Error Message                                                       |
| ------- | --------------- | ------------------------------------------------------------------- |
| 109     | Error           | "Transaction timed out after 2 minutes"                             |
| 125     | Toast (failure) | "Transaction timed out after 2 minutes."                            |
| 189-192 | Error           | "Unable to check transaction status. Please verify in your wallet." |
| 191-192 | Error           | "Transaction not found. Please verify in your wallet."              |
| 196     | Toast (failure) | "Could not verify transaction status. Check your wallet."           |
| 197     | Toast (failure) | "Transaction not found. Check your wallet."                         |

---

## Authentication

### Auth0 Popup Authentication

**File:** `/src/lib/auth/auth0PopupLogin.ts`

| Line    | Error Message                                                                        |
| ------- | ------------------------------------------------------------------------------------ |
| 156-159 | "Unable to open Auth0 login popup. Please disable your popup blocker and try again." |
| 195-199 | "Auth0 authentication failed: {error_description or error}"                          |
| 206     | "Invalid authentication response from Auth0."                                        |
| 213     | "Invalid state parameter. Possible CSRF attack."                                     |
| 233     | "Authentication popup was closed by the user."                                       |
| 251     | "Authentication timeout. Please try again."                                          |
| 258     | "Authentication timeout. Please try again." (COOP policy fallback)                   |

### Solana Wallet Authentication

**File:** `/src/lib/hooks/useSolanaAuthentication.ts`

| Line | Type            | Error Message                             |
| ---- | --------------- | ----------------------------------------- |
| 27   | Toast (failure) | "Please connect your Solana wallet first" |

### Provider Linking

**File:** `/src/lib/hooks/useProviderLinkingAuth.ts`

| Line | Type            | Error Message                                                                     |
| ---- | --------------- | --------------------------------------------------------------------------------- |
| 254  | Error           | "Unable to open Telegram popup. Please disable popup blocker and try again."      |
| 257  | Error           | "Unable to open Telegram login. Please disable your popup blocker and try again." |
| 343  | Toast (failure) | "Wallet connection required for linking"                                          |

### Provider Mutations

**Files and Lines:**

| File                                       | Line | Error Message                                    |
| ------------------------------------------ | ---- | ------------------------------------------------ |
| `/src/atoms/atomMutationLinkProvider.ts`   | 18   | "Authentication required for provider linking"   |
| `/src/atoms/atomMutationUnlinkProvider.ts` | 23   | "Authentication required for provider unlinking" |

### Security Confirmation

**File:** `/src/components/auth/SecurityConfirmationModal.tsx`

| Line | Error Message                               |
| ---- | ------------------------------------------- |
| 77   | "Unsupported provider type: {providerType}" |

---

## Cryptographic Validation

### Crypto Utilities

**File:** `/src/utils/crypto.ts`

| Line    | Error Message                                               |
| ------- | ----------------------------------------------------------- |
| 78      | "Invalid private key format"                                |
| 100     | "Invalid private key format"                                |
| 115     | "Invalid mnemonic phrase"                                   |
| 160-161 | "Invalid private key length: {X}. Expected 32 or 64 bytes." |
| 165-166 | "Failed to convert private key: {error message}"            |

### Mnemonic Utilities

**File:** `/src/utils/mnemonicUtils.ts`

| Line | Error Message             |
| ---- | ------------------------- |
| 100  | "Invalid mnemonic phrase" |

### Private Key Import

**File:** `/src/atoms/atomMutationPrivateKeyImport.ts`

| Line | Error Message                                 |
| ---- | --------------------------------------------- |
| 70   | "Invalid private key format"                  |
| 76   | "Private key does not match expected address" |

---

## React Context Validation

| File                                                                  | Line | Error Message                                                      |
| --------------------------------------------------------------------- | ---- | ------------------------------------------------------------------ |
| `/src/components/ui/Form.tsx`                                         | 62   | "useFormField should be used within <FormField>"                   |
| `/src/components/v2/ui/molecules/Tabs/Tabs.tsx`                       | 92   | "useTabs must be used within a TabsProvider"                       |
| `/src/components/v2/ui/organisms/Chart/components/ChartContainer.tsx` | 24   | "useChart must be used within a <ChartContainer />"                |
| `/src/app/(cook)/perpetuals/hooks/useSelectedContract.tsx`            | 7-8  | "useSelectedContract must be used within SelectedContractProvider" |

---

## Clipboard Operations

### Copy Link to Clipboard

**File:** `/src/lib/utils/copyLinkToClipboard.ts`

| Line | Type            | Error Message                             |
| ---- | --------------- | ----------------------------------------- |
| 6    | Toast (success) | "Link copied to clipboard {address}"      |
| 8    | Toast (failure) | "Failed to copy link to clipboard: {err}" |

### Copy Address to Clipboard

**File:** `/src/lib/utils/copyAddressToClipboard.ts`

| Line | Type            | Error Message                                |
| ---- | --------------- | -------------------------------------------- |
| 6    | Toast (success) | "Address copied to clipboard {address}"      |
| 8    | Toast (failure) | "Failed to copy address to clipboard: {err}" |

---

## SSE & Network

**File:** `/src/lib/api/sse.ts`

| Line    | Error Message                                               |
| ------- | ----------------------------------------------------------- |
| 40      | "Authentication error: {status}"                            |
| 43      | "Client error: {status}"                                    |
| 46      | "Server error: {status}"                                    |
| 50      | "ReadableStream not supported by browser."                  |
| 100-102 | "SSE connection failed after {maxRetries} retries: {error}" |

---

## Configuration & Utilities

### Path Service

**File:** `/src/lib/services/pathService.ts`

| Line  | Error Message                                                                                               |
| ----- | ----------------------------------------------------------------------------------------------------------- |
| 54-56 | "PathService requires a valid API base URL. Please ensure NEXT_PUBLIC_API_URL environment variable is set." |
| 64    | "Missing {key} parameter"                                                                                   |

### Query Utilities

**Files and Lines:**

| File                                          | Line | Error Message               |
| --------------------------------------------- | ---- | --------------------------- |
| `/src/lib/queries/tokenDetails.ts`            | 19   | "Token address is required" |
| `/src/lib/queries/diamondHandsEarlyTrades.ts` | 25   | "Mint address is required"  |
| `/src/lib/queries/useTransactionStatus.ts`    | 25   | "External ID is required"   |

### Kitchen Filters

**File:** `/src/app/(cook)/kitchen/filters/index.ts`

| Line | Error Message               |
| ---- | --------------------------- |
| 105  | "Unknown column key: {key}" |

---

## Solana Log Parser

**File:** `/src/lib/utils/solanaLogParser.ts`

| Line | Error Message              |
| ---- | -------------------------- |
| 34   | "Parent node set twice"    |
| 55   | "Closing a different node" |
| 58   | "Closing node twice"       |
| 70   | "Closing node twice"       |
| 125  | "There is no current node" |
| 144  | "There is no current node" |

---

## Generic Fallback

**File:** `/src/lib/utils/createErrorHandler.ts`

| Line | Error Message   |
| ---- | --------------- |
| 19   | "Unknown error" |

**Context:** This is the default error message used when no specific error message is available from any error handling scenario.

---

## Summary Statistics

| Category                               | Count  |
| -------------------------------------- | ------ |
| Zod Validation                         | 32     |
| Frontend Logic (wallet/balance checks) | 13     |
| Transaction Status                     | 6      |
| Auth0 & Wallet Auth                    | 13     |
| Cryptographic Validation               | 7      |
| React Context                          | 4      |
| Clipboard                              | 4      |
| SSE/Network                            | 5      |
| Configuration                          | 5      |
| Solana Parser                          | 6      |
| Generic Fallback                       | 1      |
| **Total**                              | **96** |

---
