---
title: Error Messages Reference Guide
type: technical-reference
date: 2025-10-23
status: active
summary: Single comprehensive spreadsheet of all error messages in the application, organized by endpoint, source (backend/frontend), domain, error reason, and examples for easy human readability and troubleshooting.
tags:
  - error-handling
  - reference
  - troubleshooting
  - user-experience
  - debugging
related_documents:
  - backend-error-messages-displayed-in-frontend.md
  - frontend-only-error-messages.md
---

# Error Messages Reference Guide

A single, comprehensive spreadsheet cataloging all 134+ error messages in the application.

## How to Use This Spreadsheet

- **Search**: Use Cmd/Ctrl+F to find specific errors
- **Filter by Domain**: Look for domain names (e.g., "Limit Orders", "Wallet Management")
- **Filter by Source**: Search "Backend" or "Frontend"
- **Find by Endpoint**: Search for API routes (e.g., "/limit-orders")
- **Locate Code**: Use "File Reference" column to find implementation

---

## Complete Error Messages Spreadsheet

| # | Endpoint | Source | Domain | Error Reason | Example Error Message | File Reference | Display Type |
|---|----------|--------|--------|--------------|----------------------|----------------|--------------|
| 1 | `POST /limit-orders` | Backend | Limit Orders | Order creation failed | "Limit order failed due to Insufficient balance" | `atomMutationLimitOrder.ts:79-80` | Toast |
| 2 | `POST /limit-orders` | Frontend | Limit Orders | No wallet selected | "No wallet selected" | `atomMutationLimitOrder.ts:48` | Error |
| 3 | `POST /limit-orders/cancel/:orderId` | Backend | Limit Orders | Order cancellation failed | "Limit order cancel for SOL failed" | `atomMutationCancelLimitOrder.ts:24-33` | Toast |
| 4 | `GET /limit-orders` | Backend | Limit Orders | Failed to fetch orders | "Failed to fetch user orders" | `atomQueryOrdersByWallet.ts:24-27` | Toast |
| 5 | `POST /twap` | Backend | TWAP Orders | Order creation failed | "TWAP order failed due to Invalid price range" | `atomMutationTwapOrder.ts:95-96` | Toast |
| 6 | `POST /twap` | Frontend | TWAP Orders | No wallet selected | "No wallet selected" | `atomMutationTwapOrder.ts:46` | Error |
| 7 | `POST /twap/:orderId/status/:status` | Backend | TWAP Orders | Status change failed | "TWAP status change failed" | `atomMutationTwapStatusChange.ts:32-38` | Toast |
| 8 | `GET /twap` | Backend | TWAP Orders | Failed to fetch orders | "Failed to fetch TWAP wallet orders" | `atomQueryTwapOrdersByWallet.ts:98-101` | Toast |
| 9 | `POST /dca` | Backend | DCA Orders | Order creation failed | "DCA order failed due to Amount below minimum" | `atomMutationDcaOrder.ts:82-83` | Toast |
| 10 | `POST /dca` | Frontend | DCA Orders | No wallet selected | "No wallet selected" | `atomMutationDcaOrder.ts:42` | Error |
| 11 | `POST /dca/:dcaId/status/:status` | Backend | DCA Orders | Status change failed | "DCA status change failed" | `useChangeDcaStatus.ts:49-57` | Toast |
| 12 | `GET /dca` | Backend | DCA Orders | Failed to fetch orders | "Failed to fetch DCA wallet orders" | `atomQueryDcaOrdersByWallet.ts:77-80` | Toast |
| 13 | `POST /vwap` | Backend | VWAP Orders | Order creation failed | "VWAP order failed due to Invalid time window" | `atomMutationVwapOrder.ts:103-104` | Toast |
| 14 | `POST /vwap` | Frontend | VWAP Orders | No wallet selected | "No wallet selected" | `atomMutationVwapOrder.ts:50` | Error |
| 15 | `POST /vwap/:orderId/status/:status` | Backend | VWAP Orders | Status change failed | "VWAP status change failed" | `useChangeVwapStatus.ts:52-59` | Toast |
| 16 | `POST /custom-orders` | Backend | Custom Orders | Order creation failed | "Custom order failed due to Invalid schedule configuration" | `atomMutationCustomOrder.ts:89-90` | Toast |
| 17 | `POST /custom-orders` | Frontend | Custom Orders | No wallet selected | "No wallet selected" | `atomMutationCustomOrder.ts:44` | Error |
| 18 | `POST /wallets/create` | Backend | Wallet Creation | Wallet creation failed | "Creating Wallet failed due to: Wallet name already exists" | `atomMutationCreateWallet.ts:52-57` | Toast |
| 19 | `DELETE /wallets/:walletId` | Backend | Wallet Deletion | Delete/archive failed | "There was a problem archiving your wallet due to: Wallet has active orders" | `atomMutationDeleteWallet.ts:39-46` | Toast |
| 20 | `PUT /wallets/:walletId` | Backend | Wallet Update | Name update failed | "There was a problem updating your wallet name due to: Name contains invalid characters" | `atomMutationUpdateWalletName.ts:35-40` | Toast |
| 21 | `PUT /wallets/:walletId/activate` | Backend | Wallet Reactivation | Reactivation failed | "Failed to reactivate wallet due to: Wallet not found" | `atomMutationReactivateWallet.ts:30-35` | Toast |
| 22 | `GET /wallets` | Backend | Wallet Fetch | Failed to fetch wallets | "Failed to fetch your wallets: Network error" | `atomQueryWallets.ts:21-23` | Toast |
| 23 | `POST /wallets/import/init-private-key` | Backend | Wallet Import | Rate limited | "Too many requests. Please wait 60 seconds before trying again." | `walletImportErrorHandling.ts:31-33` | Toast |
| 24 | `POST /wallets/import/init-private-key` | Backend | Wallet Import | Invalid credentials | "Invalid private key format. Please check and try again." | `walletImportErrorHandling.ts:31-33` | Toast |
| 25 | `POST /wallets/import/init-private-key` | Backend | Wallet Import | Server error | "Server error. Please try again later." | `walletImportErrorHandling.ts:31-33` | Toast |
| 26 | N/A | Frontend | Wallet Import | Private key validation | "Private key must be exactly 64 hexadecimal characters" | `walletImportValidation.ts:17` | Form Validation |
| 27 | N/A | Frontend | Wallet Import | Mnemonic validation | "Mnemonic phrase must contain exactly 12 or 24 words" | `walletImportValidation.ts:43` | Form Validation |
| 28 | N/A | Frontend | Wallet Import | Invalid format | "Invalid private key format" | `atomMutationPrivateKeyImport.ts:70` | Error |
| 29 | N/A | Frontend | Wallet Import | Address mismatch | "Private key does not match expected address" | `atomMutationPrivateKeyImport.ts:76` | Error |
| 30 | N/A | Frontend | Wallet Import | Wallet name required | "Wallet name is required" | `walletImportValidation.ts:93` | Form Validation |
| 31 | N/A | Frontend | Wallet Import | Wallet name too short | "Wallet name must be at least 3 characters" | `walletImportValidation.ts:94` | Form Validation |
| 32 | N/A | Frontend | Wallet Import | Wallet name too long | "Wallet name must be no more than 50 characters" | `walletImportValidation.ts:95` | Form Validation |
| 33 | N/A | Frontend | Wallet Import | Invalid name characters | "Wallet name can only contain letters, numbers, spaces, hyphens, and underscores" | `walletImportValidation.ts:104` | Form Validation |
| 34 | N/A | Frontend | Wallet Import | Security check | "Input contains potentially malicious content" | `walletImportValidation.ts:281` | Form Validation |
| 35 | N/A | Frontend | Wallet Import | Test data check | "Please use real wallet data, not test/placeholder values" | `walletImportValidation.ts:288` | Form Validation |
| 36 | N/A | Frontend | Wallet Import | Private key required | "Private key is required" | `walletImportValidation.ts:9` | Form Validation |
| 37 | N/A | Frontend | Wallet Import | Mnemonic required | "Mnemonic phrase is required" | `walletImportValidation.ts:35` | Form Validation |
| 38 | N/A | Frontend | Wallet Import | Invalid mnemonic words | "Invalid mnemonic phrase. Please check that all words are correct." | `walletImportValidation.ts:53` | Form Validation |
| 39 | N/A | Frontend | Wallet Import | Missing credentials | "Please enter a private key or mnemonic phrase" | `walletImportValidation.ts:62` | Form Validation |
| 40 | N/A | Frontend | Wallet Import | Invalid credentials format | "Please enter a valid private key (64 hex characters) or mnemonic phrase (12/24 words)" | `walletImportValidation.ts:84` | Form Validation |
| 41 | N/A | Frontend | Wallet Import | Password required | "Security password is required" | `walletImportValidation.ts:115` | Form Validation |
| 42 | N/A | Frontend | Wallet Import | Step incomplete | "All required fields must be completed for this step" | `walletImportValidation.ts:178` | Form Validation |
| 43 | `POST /wallets/transfer` | Backend | Wallet Transfer | Transfer failed | "Transfer failed due to: Insufficient balance" | `atomMutationTransfer.ts:44-47` | Toast |
| 44 | N/A | Frontend | Wallet Transfer | No sender selected | "You must select a sender wallet." | `TransferModal.tsx:49` | Form Validation |
| 45 | N/A | Frontend | Wallet Transfer | Zero amount | "Amount transferred cannot be 0." | `TransferModal.tsx:53` | Form Validation |
| 46 | `POST /wallets/export/:walletId` | Backend | Wallet Export | Export failed | "Exporting Wallet Seed Phrase failed due to: Invalid password" | `atomMutationExportSp.ts:37-44` | Toast |
| 47 | N/A | Frontend | Wallet Export | Wrong password | "Security Password is incorrect." | `handlePasswordError.ts:8-12` | Form Validation |
| 48 | `POST /hyperliquid/account/withdraw` | Backend | Wallet Withdrawal | Withdraw failed | "Withdraw failed due to: Minimum balance requirement not met" | `atomMutationWithdraw.ts:44-47` | Toast |
| 49 | N/A | Frontend | Wallet Withdrawal | No sender wallet | "You must select a sender wallet." | `WithdrawModal.tsx:54` | Form Validation |
| 50 | N/A | Frontend | Wallet Withdrawal | Zero amount | "Amount transferred cannot be 0." | `WithdrawModal.tsx:59` | Form Validation |
| 51 | N/A | Frontend | Wallet Withdrawal | No recipient | "Recipient must not be null" | `WithdrawModal.tsx:69` | Form Validation |
| 52 | N/A | Frontend | Wallet Withdrawal | Password required | "Password is required" | `WithdrawModal.tsx:76` | Form Validation |
| 53 | `POST /token/quick_operation_v2` | Backend | Quick Trade | Transaction failed | "Transaction failed for SOL: Slippage tolerance exceeded" | `atomMutationQuickOperation.ts:158-159` | Toast |
| 54 | N/A | Frontend | Quick Trade | No wallet selected | "No wallet selected" | `atomMutationQuickOperation.ts:84` | Error |
| 55 | N/A | Frontend | Quick Trade | Invalid amount | "Amount must be greater than 0" | `atomMutationQuickOperation.ts:88` | Error |
| 56 | N/A | Frontend | Quick Trade | Insufficient SOL | "Insufficient SOL balance" | `atomMutationQuickOperation.ts:96` | Error |
| 57 | N/A | Frontend | Quick Trade | Insufficient tokens | "Insufficient token balance" | `atomMutationQuickOperation.ts:103` | Error |
| 58 | N/A | Frontend | Quick Trade | Insufficient SOL with fee | "Insufficient SOL balance" | `atomMutationQuickOperation.ts:110` | Error |
| 59 | N/A | Frontend | Quick Trade | No wallet (toast) | "Please select a wallet" | `atomMutationQuickOperation.ts:135` | Toast |
| 60 | N/A | Frontend | Quick Trade | Insufficient SOL (toast) | "Insufficient SOL balance" | `atomMutationQuickOperation.ts:141` | Toast |
| 61 | N/A | Frontend | Quick Trade | Insufficient tokens (toast) | "Insufficient token balance" | `atomMutationQuickOperation.ts:147` | Toast |
| 62 | N/A | Frontend | Quick Trade | Invalid amount (toast) | "Amount must be greater than 0" | `atomMutationQuickOperation.ts:153` | Toast |
| 63 | N/A | Frontend | Transaction Status | Timeout | "Transaction timed out after 2 minutes" | `atomTransactionStatusQueue.ts:109` | Error |
| 64 | N/A | Frontend | Transaction Status | Verification failed | "Unable to check transaction status. Please verify in your wallet." | `atomTransactionStatusQueue.ts:189-192` | Error |
| 65 | N/A | Frontend | Transaction Status | Not found | "Transaction not found. Please verify in your wallet." | `atomTransactionStatusQueue.ts:191-192` | Error |
| 66 | N/A | Frontend | Transaction Status | Timeout (toast) | "Transaction timed out after 2 minutes." | `atomTransactionStatusQueue.ts:125` | Toast |
| 67 | N/A | Frontend | Transaction Status | Cannot verify | "Could not verify transaction status. Check your wallet." | `atomTransactionStatusQueue.ts:196` | Toast |
| 68 | N/A | Frontend | Transaction Status | Not found (toast) | "Transaction not found. Check your wallet." | `atomTransactionStatusQueue.ts:197` | Toast |
| 69 | `POST /token/recent-tokens` | Backend | Token Management | Add token failed | "Failed to add recent token: Token not found" | `atomMutationAddRecentToken.ts:27-28` | Toast |
| 70 | `GET /token/search` | Backend | Token Search | Search failed | "Failed token search" | `atomQuerySearchTokens.ts:34-37` | Toast |
| 71 | N/A | Frontend | Token Details | Missing address | "Token address is required" | `tokenDetails.ts:19` | Error |
| 72 | N/A | Frontend | Diamond Hands | Missing mint | "Mint address is required" | `diamondHandsEarlyTrades.ts:25` | Error |
| 73 | `POST /auth/providers/link` | Backend | Auth Provider | Link failed | "Email already linked to another account" | `atomMutationLinkProvider.ts:23-26` | Error |
| 74 | N/A | Frontend | Auth Provider | Not authenticated | "Authentication required for provider linking" | `atomMutationLinkProvider.ts:18` | Error |
| 75 | `DELETE /auth/providers/:providerType` | Backend | Auth Provider | Unlink failed | "Cannot unlink last authentication method" | `atomMutationUnlinkProvider.ts:30-33` | Error |
| 76 | N/A | Frontend | Auth Provider | Not authenticated | "Authentication required for provider unlinking" | `atomMutationUnlinkProvider.ts:23` | Error |
| 77 | `GET /auth/providers` | Backend | Auth Provider | Fetch failed | "Failed to fetch linked providers: Unauthorized" | `atomQueryLinkedProviders.ts:13-15` | Toast |
| 78 | N/A | Frontend | Auth Provider | Unsupported type | "Unsupported provider type: github" | `SecurityConfirmationModal.tsx:77` | Error |
| 79 | N/A | Frontend | Auth0 | Popup blocked | "Unable to open Auth0 login popup. Please disable your popup blocker and try again." | `auth0PopupLogin.ts:156-159` | Error |
| 80 | N/A | Frontend | Auth0 | Auth failed | "Auth0 authentication failed: Invalid credentials" | `auth0PopupLogin.ts:195-199` | Error |
| 81 | N/A | Frontend | Auth0 | Invalid response | "Invalid authentication response from Auth0." | `auth0PopupLogin.ts:206` | Error |
| 82 | N/A | Frontend | Auth0 | CSRF detected | "Invalid state parameter. Possible CSRF attack." | `auth0PopupLogin.ts:213` | Error |
| 83 | N/A | Frontend | Auth0 | User closed popup | "Authentication popup was closed by the user." | `auth0PopupLogin.ts:233` | Error |
| 84 | N/A | Frontend | Auth0 | Timeout | "Authentication timeout. Please try again." | `auth0PopupLogin.ts:251` | Error |
| 85 | N/A | Frontend | Auth0 | Timeout (COOP) | "Authentication timeout. Please try again." | `auth0PopupLogin.ts:258` | Error |
| 86 | N/A | Frontend | Solana Wallet | Not connected | "Please connect your Solana wallet first" | `useSolanaAuthentication.ts:27` | Toast |
| 87 | N/A | Frontend | Solana Wallet | Connection required | "Wallet connection required for linking" | `useProviderLinkingAuth.ts:343` | Toast |
| 88 | Telegram auth | Backend | Telegram Auth | Auth failed | "Telegram authentication failed: Invalid token" | `telegramAuthUtils.ts:82-86` | Toast |
| 89 | N/A | Frontend | Telegram Auth | Popup blocked | "Unable to open Telegram popup. Please disable popup blocker and try again." | `useProviderLinkingAuth.ts:254` | Error |
| 90 | N/A | Frontend | Telegram Auth | Login failed | "Unable to open Telegram login. Please disable your popup blocker and try again." | `useProviderLinkingAuth.ts:257` | Error |
| 91 | `PUT /user/info` | Backend | User Settings | Update failed | "Failed to update cooking tag. Please try again." | `useUserInfo.ts:52-55` | Toast |
| 92 | N/A | Frontend | Security | Password required | "This field is required." | `SecurityPasswordSection.tsx:23` | Form Validation |
| 93 | N/A | Frontend | Security | Password mismatch | "Passwords do not match." | `SecurityPasswordSection.tsx:32` | Form Validation |
| 94 | N/A | Frontend | Security | Same password | "New Password can't be the same as Current Password." | `SecurityPasswordSection.tsx:53` | Form Validation |
| 95 | N/A | Frontend | Security | Password required (new) | "This field is required." | `SecurityPasswordSection.tsx:45` | Form Validation |
| 96 | N/A | Frontend | Security | Password mismatch (new) | "Passwords do not match." | `SecurityPasswordSection.tsx:49` | Form Validation |
| 97 | N/A | Frontend | Transaction Fees | Invalid slippage | "Slippage must be at least 0" | `TxFeesPopoverContent.tsx:33` | Form Validation |
| 98 | N/A | Frontend | Transaction Fees | Invalid priority fee | "Priority Fee must be at least 0" | `TxFeesPopoverContent.tsx:40` | Form Validation |
| 99 | N/A | Frontend | Crypto Utilities | Invalid private key | "Invalid private key format" | `crypto.ts:78` | Error |
| 100 | N/A | Frontend | Crypto Utilities | Invalid private key (alt) | "Invalid private key format" | `crypto.ts:100` | Error |
| 101 | N/A | Frontend | Crypto Utilities | Invalid mnemonic | "Invalid mnemonic phrase" | `crypto.ts:115` | Error |
| 102 | N/A | Frontend | Crypto Utilities | Invalid key length | "Invalid private key length: 48. Expected 32 or 64 bytes." | `crypto.ts:160-161` | Error |
| 103 | N/A | Frontend | Crypto Utilities | Conversion failed | "Failed to convert private key: Invalid hex string" | `crypto.ts:165-166` | Error |
| 104 | N/A | Frontend | Mnemonic Utils | Invalid phrase | "Invalid mnemonic phrase" | `mnemonicUtils.ts:100` | Error |
| 105 | `POST /hyperliquid/trading/market-order` | Backend | Perpetuals Market | Order failed | "Error placing market order: Insufficient margin" | `atomMutationPlaceMarketOrder.ts:46-53` | Toast |
| 106 | `POST /hyperliquid/trading/limit-order` | Backend | Perpetuals Limit | Order failed | "Error placing limit order: Price outside acceptable range" | `atomMutationPlaceLimitOrder.ts:49-56` | Toast |
| 107 | `POST /hyperliquid/trading/update-leverage` | Backend | Perpetuals Leverage | Update failed | "Updating leverage failed due to: Maximum leverage exceeded" | `atomMutationUpdateLeverage.ts:21-25` | Toast |
| 108 | N/A | Frontend | Perpetuals Form | Missing limit price | "limitPrice is required when type is LIMIT" | `form.ts:23` | Form Validation |
| 109 | `POST /hyperliquid/account/deposit` | Backend | Perpetuals Deposit | Deposit failed | "Deposit amount below minimum" | `ConvertFundsForm.tsx:163-166` | Form Field Error |
| 110 | `POST /hyperliquid/account/deposit-slow` | Backend | Perpetuals Deposit | Deposit failed | "Deposit amount below minimum" | `ConvertFundsForm.tsx:163-166` | Form Field Error |
| 111 | `POST /hyperliquid/account/withdraw` | Backend | Perpetuals Withdraw | Withdraw failed | "There was a problem making a withdrawal in your Perpetuals Wallet due to: Insufficient funds" | `atomMutationHyperliquidAccountWithdraw.ts:37-45` | Toast |
| 112 | `POST /hyperliquid/account/withdraw-slow` | Backend | Perpetuals Withdraw | Withdraw failed | "There was a problem making a withdrawal in your Perpetuals Wallet due to: Insufficient funds" | `atomMutationHyperliquidAccountWithdraw.ts:37-45` | Toast |
| 113 | `GET /hyperliquid/account/validate-withdrawal/:amount` | Backend | Perpetuals Validation | Validation failed | "Minimum USDC needed: ~15 USDC" | `atomMutationHyperliquidAccountWithdraw.ts:37-45` | Error |
| 114 | N/A | Frontend | SSE Connection | Auth error | "Authentication error: 401" | `sse.ts:40` | Error |
| 115 | N/A | Frontend | SSE Connection | Client error | "Client error: 400" | `sse.ts:43` | Error |
| 116 | N/A | Frontend | SSE Connection | Server error | "Server error: 500" | `sse.ts:46` | Error |
| 117 | N/A | Frontend | SSE Connection | Not supported | "ReadableStream not supported by browser." | `sse.ts:50` | Error |
| 118 | N/A | Frontend | SSE Connection | Max retries | "SSE connection failed after 5 retries: Network timeout" | `sse.ts:100-102` | Error |
| 119 | N/A | Frontend | Path Service | Missing API URL | "PathService requires a valid API base URL. Please ensure NEXT_PUBLIC_API_URL environment variable is set." | `pathService.ts:54-56` | Error |
| 120 | N/A | Frontend | Path Service | Missing parameter | "Missing walletId parameter" | `pathService.ts:64` | Error |
| 121 | N/A | Frontend | Transaction Status | Missing ID | "External ID is required" | `useTransactionStatus.ts:25` | Error |
| 122 | N/A | Frontend | Clipboard | Copy success | "Link copied to clipboard https://..." | `copyLinkToClipboard.ts:6` | Toast (Success) |
| 123 | N/A | Frontend | Clipboard | Copy failed | "Failed to copy link to clipboard: Permission denied" | `copyLinkToClipboard.ts:8` | Toast |
| 124 | N/A | Frontend | Clipboard | Address copy success | "Address copied to clipboard 0x..." | `copyAddressToClipboard.ts:6` | Toast (Success) |
| 125 | N/A | Frontend | Clipboard | Address copy failed | "Failed to copy address to clipboard: Permission denied" | `copyAddressToClipboard.ts:8` | Toast |
| 126 | N/A | Frontend | React Context | Form context missing | "useFormField should be used within <FormField>" | `Form.tsx:62` | Error |
| 127 | N/A | Frontend | React Context | Tabs context missing | "useTabs must be used within a TabsProvider" | `Tabs.tsx:92` | Error |
| 128 | N/A | Frontend | React Context | Chart context missing | "useChart must be used within a <ChartContainer />" | `ChartContainer.tsx:24` | Error |
| 129 | N/A | Frontend | React Context | Contract context missing | "useSelectedContract must be used within SelectedContractProvider" | `useSelectedContract.tsx:7-8` | Error |
| 130 | N/A | Frontend | Solana Parser | Parent error | "Parent node set twice" | `solanaLogParser.ts:34` | Error |
| 131 | N/A | Frontend | Solana Parser | Node mismatch | "Closing a different node" | `solanaLogParser.ts:55` | Error |
| 132 | N/A | Frontend | Solana Parser | Duplicate close | "Closing node twice" | `solanaLogParser.ts:58` | Error |
| 133 | N/A | Frontend | Solana Parser | Duplicate close (alt) | "Closing node twice" | `solanaLogParser.ts:70` | Error |
| 134 | N/A | Frontend | Solana Parser | Missing node | "There is no current node" | `solanaLogParser.ts:125` | Error |
| 135 | N/A | Frontend | Solana Parser | Missing node (alt) | "There is no current node" | `solanaLogParser.ts:144` | Error |
| 136 | N/A | Frontend | Kitchen Filters | Unknown column | "Unknown column key: invalidColumn" | `filters/index.ts:105` | Error |
| 137 | `POST /referrals/rewards` | Backend | Referrals | No rewards available | "No rewards to claim" | `atomMutationReferralsClaimRewards.ts:18-22` | Toast |
| 138 | `POST /referrals/rewards` | Backend | Referrals | Claim success | "Rewards successfully claimed" | `atomMutationReferralsClaimRewards.ts:18-22` | Toast (Success) |
| 139 | `POST /referrals/rewards` | Backend | Referrals | Claim failed | "Rewards claim failed" | `atomMutationReferralsClaimRewards.ts:36-39` | Toast |
| 140 | N/A | Frontend | Generic | Unknown error | "Unknown error" | `createErrorHandler.ts:19` | Toast |
| 141 | N/A | Frontend | Generic | Unknown error (alt) | "an unknown error" | Various files | Toast |

---

## Summary Statistics

| Category | Count | Percentage |
|----------|-------|------------|
| **Total Errors** | 141 | 100% |
| Backend Errors | 41 | 29% |
| Frontend Errors | 100 | 71% |
| Toast Messages | 72 | 51% |
| Form Validations | 42 | 30% |
| Direct Errors | 27 | 19% |

### By Domain

| Domain | Count |
|--------|-------|
| Wallet Management | 35 |
| Orders (All Types) | 17 |
| Authentication | 16 |
| Quick Trade | 10 |
| Transaction Status | 6 |
| Perpetuals | 9 |
| Token Management | 4 |
| System/Network | 18 |
| Validation | 10 |
| Referrals | 3 |
| Generic | 2 |
| Other | 11 |

### By Source

| Source | Error Count | Display Types |
|--------|-------------|---------------|
| **Backend** | 41 | Toast (38), Form Field (2), Error (1) |
| **Frontend** | 100 | Form Validation (42), Toast (34), Error (24) |

---

## Common Error Patterns

### Pattern 1: "No wallet selected"
**Occurrences:** 6
**Domains:** Limit Orders, TWAP, DCA, VWAP, Custom Orders, Quick Trade
**Solution:** Select a wallet from the wallet dropdown

### Pattern 2: "Insufficient balance"
**Occurrences:** 5
**Domains:** Quick Trade, Wallet Transfer, Order Creation
**Solution:** Ensure wallet has sufficient SOL or token balance

### Pattern 3: "Transaction timed out"
**Occurrences:** 2
**Domain:** Transaction Status
**Solution:** Check wallet for transaction status (may have succeeded)

### Pattern 4: "Authentication required"
**Occurrences:** 2
**Domains:** Provider linking/unlinking
**Solution:** Log in or refresh authentication session

### Pattern 5: "Invalid format"
**Occurrences:** 8
**Domains:** Wallet Import, Crypto Operations
**Solution:** Verify input follows correct format

---

## Quick Reference: Error by User Action

### Creating Orders
- Check wallet is selected (#2, #6, #10, #14, #17)
- Verify sufficient balance (#1, #5, #9, #13, #16)
- Check order parameters are valid (#5, #9, #13, #16)

### Managing Wallets
- Use correct password (#47)
- Verify wallet name is valid (#30-33)
- Check for active orders before deletion (#19)
- Ensure sufficient balance for transfers (#43)

### Importing Wallets
- Private key must be 64 hex characters (#26)
- Mnemonic must be 12 or 24 words (#27)
- Check for address match (#29)
- Provide valid wallet name (#30-33)

### Trading
- Select a wallet first (#54, #59)
- Ensure sufficient SOL for gas (#56, #60)
- Check token balance (#57, #61)
- Enter amount greater than 0 (#55, #62)

### Authentication
- Allow popups for login (#79, #89, #90)
- Check authentication status (#74, #76)
- Verify provider is supported (#78)

### Perpetuals
- Check margin requirements (#105)
- Verify leverage limits (#107)
- Ensure minimum balance (#111, #113)
- Provide limit price for limit orders (#108)

---

## Using This Reference

### For Developers
1. Search by **File Reference** to find code location
2. Use **#** column for quick reference in discussions
3. Check **Display Type** to know how error appears to users

### For QA/Testing
1. Filter by **Domain** to organize test cases
2. Verify **Example Error Message** appears as specified
3. Test both **Backend** and **Frontend** error sources

### For Support
1. Search user's error message in **Example Error Message** column
2. Check **Error Reason** for context
3. Reference common patterns section for solutions

### For Product/UX
1. Review **Display Type** for consistency
2. Check error message clarity and helpfulness
2. Identify areas needing better error messages

---

## Export Options

This spreadsheet can be exported to:
- **CSV**: For Excel/Google Sheets analysis
- **JSON**: For programmatic access
- **SQL**: For database import

Example CSV export:
```csv
Number,Endpoint,Source,Domain,ErrorReason,ExampleErrorMessage,FileReference,DisplayType
1,POST /limit-orders,Backend,Limit Orders,Order creation failed,"Limit order failed due to Insufficient balance",atomMutationLimitOrder.ts:79-80,Toast
...
```

---

## Related Documentation

- [Backend Error Messages Displayed in Frontend](backend-error-messages-displayed-in-frontend.md) - Detailed backend error handling
- [Frontend-Only Error Messages](frontend-only-error-messages.md) - Detailed frontend validation

---

**Last Updated:** 2025-10-23
**Total Errors Cataloged:** 141
**Coverage:** Complete (Backend + Frontend)
