---
title: Referral Program - Custom Invite Code Generation
type: feature-specification
status: in-development
priority: high
created: 2025-07-09
date: 2025-10-20
updated: 2025-10-20
tags: [referral-program, invite-codes, acquisition, mobile-support]
related:
  - "[[referral-program-multilevel]]"
  - "[[mobile-app-prd]]"
  - "[[platform-vision-requirements]]"
---

# Referral Program - Custom Invite Code Generation

## Current State Analysis

### How It Currently Works

The current 'Referral Program' operates by creating a referral link with an **auto-generated code**. Said link is then shared through any channel the Cooking user chooses and if anybody decides to join, they'll become automatically their referrals when they first login.

This linking is **transparent** to both users as they have to do nothing to become associated on Cooking other than to use the correct Referral link.

### Current Method - Pros and Cons

#### PROs:
- The creation of the referral link is **immediate**
- The association when signing up is also **immediate** and presents the **lowest friction**

#### CONs:
- This method is **incompatible with multi-device products** such as Cooking intends to be since we cannot handle transparently the association of the referral to the referrer after downloading the app
- It **doesn't allow for existing users** to join as a referral of another user and leverage the commission discounts

---

## Proposed Solution

### Custom Invite Code System

The proposal is to modify slightly the code creation procedure, so now the would-be referrer would have the ability to **determine their invite code**.

### What Gets Created

As a result, we would create **both**:
1. **Referral Link**: Contains the invite code in URL
2. **Invite Code**: Standalone code for manual entry

### Purpose of Each

**Referral Link**:
- Serves the same purpose it has until now
- Automatic association on signup via link
- Works for web and deeplinks

**Invite Code**:
- Method to join through mobile or later down the line
- Can be manually entered at signup or after
- Device-agnostic solution

---

## Sharing Options

When ready to share, the user will be able to choose:

1. **Copy Referral Link**: Full URL with invite code embedded
   - Example: `https://cooking.gg/signup?ref=CRYPTO2025`

2. **Copy Invite Code**: Just the code itself
   - Example: `CRYPTO2025`

---

## Signup Scenarios

### Scenario 1: Signup Through Referral Link

**User Flow**:
1. User clicks referral link
2. Lands on signup page with invite code pre-filled (hidden)
3. Completes signup process
4. **Automatically linked** to referrer

**Works**: Exactly as it works right now - zero friction

### Scenario 2: Signup Without Referral Link

**Applies to**: Web app or mobile app direct download

**User Flow**:
1. User lands on signup page
2. Presented with choice:
   - "Do you have an invite code?"
   - ○ Yes  ○ No (or Skip)
3. If **Yes**: Required to enter invite code
   - Pasting the full referral link will also work (UI will not explicitly mention this)
4. If **No**: Proceeds without referral linkage

```
┌──────────────────────────────────────────┐
│ Sign Up for Cooking                     │
├──────────────────────────────────────────┤
│ [Email input]                            │
│ [Password input]                         │
│                                          │
│ Do you have an invite code?              │
│ ○ Yes, I have a code                    │
│ ● No, continue without                   │
│                                          │
│ [Invite Code field - only if Yes]       │
│                                          │
│ [Sign Up]                                │
└──────────────────────────────────────────┘
```

---

## Post-Signup Referral Linking

### For Existing Users or Users Who Skipped

We will still support the ability to join later on via a **new option in the referral program page**.

**User Flow**:
1. User navigates to Referral Program page
2. Sees option: "Join as someone's referral"
3. Clicks option
4. Asked to input the invite code
5. **Required to accept**, acknowledging that **joining as a referral is an irreversible choice**
6. Confirmation and linkage complete

```
┌──────────────────────────────────────────────────────────────┐
│ Join as a Referral                                           │
├──────────────────────────────────────────────────────────────┤
│ Enter your referrer's invite code to get 10% off all fees   │
│                                                              │
│ Invite Code: [_________________]                            │
│                                                              │
│ ⚠️ Important:                                               │
│ • Joining as a referral is permanent and cannot be undone   │
│ • You will receive a 10% discount on all trading fees       │
│ • Your trading volume will contribute to your referrer's    │
│   commission                                                 │
│                                                              │
│ ☑ I understand and accept these terms                       │
│                                                              │
│ [Join as Referral]  [Cancel]                                 │
└──────────────────────────────────────────────────────────────┘
```

---

## Future Capability

### Referrals Becoming Referrers

In a future update, **referrals will also be able to become referrers** via creation of their own invite codes.

**Architecture Consideration**: The system architecture should take this into account from the beginning to support this without major refactoring.

---

## New System - Pros and Cons

### PROs:
- **Device agnostic**: Can be used for webapp and mobile (iOS and Android)
- **Marketing potential**: User can customize code to their liking (e.g., their brand, username)
- **Flexible linking**: Allows for linking to a referrer at any point in time, not only when signing up
- **Mobile-friendly**: Works perfectly with app downloads from stores

### CONs:
- **Not as seamless**: Requires manual input for those not using referral link
- **User education needed**: Users need to understand they can enter code

---

## Invite Code Requirements

### Format Rules

**Length**: 6 to 12 characters

**Allowed Characters**:
- Letters (A-Z, a-z)
- Numbers (0-9)
- Special characters (limited): `-`, `_`

**Rules**:
- Must be **unique** across platform
- **Case-insensitive** (CRYPTO2025 = crypto2025)
- No spaces allowed
- No offensive language (filtered against prohibited words list)

### Reserved Words

The platform reserves certain codes that cannot be used by users. See comprehensive list in original document (C302).

**Examples of Reserved Codes**:
- COOKGG, COOKING, COOKINGX
- COOKING1, COOKING99
- COOKINGAPP, COOKINGFUN
- And many more (see full list in specification)

**Recommended Platform Codes**:
- **8 chars**: COOKING1 or COOKINGX (clean, memorable)
- **9 chars**: COOKING99 (easy to remember, good length)
- **10 chars**: COOKINGAPP (professional, app-focused)

---

## User Experience

### Creating an Invite Code

```
┌──────────────────────────────────────────────────────────────┐
│ Create Your Invite Code                                      │
├──────────────────────────────────────────────────────────────┤
│ Choose a unique code to share with your friends (6-12 chars) │
│                                                              │
│ Your Code: [CRYPTO2025____________]                          │
│            ✓ Available                                       │
│                                                              │
│ Preview:                                                     │
│ • Referral Link: cooking.gg/signup?ref=CRYPTO2025          │
│ • Invite Code: CRYPTO2025                                    │
│                                                              │
│ [Create Code]                                                │
└──────────────────────────────────────────────────────────────┘
```

### Real-time Validation

As user types:
- Check availability
- Show format requirements if violated
- Suggest alternatives if taken

**Feedback Examples**:
- ✓ "CRYPTO2025 is available!"
- ✗ "CRYPTO is too short (minimum 6 characters)"
- ✗ "COOKING99 is reserved by Cooking"
- ✗ "TRADE2024 is already taken. Try: TRADE2025, TRADER24"

### Sharing Interface

```
┌──────────────────────────────────────────────────────────────┐
│ Share Your Referral                                          │
├──────────────────────────────────────────────────────────────┤
│ Your Invite Code: CRYPTO2025                                 │
│                                                              │
│ Share via:                                                   │
│ ┌────────────────────────────────────────────────────────┐  │
││ 🔗 Referral Link                         [📋 Copy]     ││  │
││ cooking.gg/signup?ref=CRYPTO2025                        ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐  │
││ #️⃣ Invite Code                           [📋 Copy]     ││  │
││ CRYPTO2025                                              ││  │
│└────────────────────────────────────────────────────────┘  │
│                                                              │
│ [Share on Twitter] [Share on Telegram] [More...]            │
└──────────────────────────────────────────────────────────────┘
```

---

## Technical Implementation

### Database Schema

```sql
CREATE TABLE invite_codes (
  id BIGINT PRIMARY KEY,
  user_id BIGINT,
  code VARCHAR(12) UNIQUE NOT NULL,
  created_at TIMESTAMP,
  is_active BOOLEAN DEFAULT TRUE,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE UNIQUE INDEX idx_invite_code_lowercase
  ON invite_codes(LOWER(code));

CREATE TABLE reserved_codes (
  code VARCHAR(12) PRIMARY KEY,
  reason VARCHAR(255)
);
```

### Code Validation Service

```pseudo
function validateInviteCode(code):
  # Format validation
  if length(code) < 6 or length(code) > 12:
    return error("Code must be 6-12 characters")

  if not matches_pattern(code, "^[A-Za-z0-9_-]+$"):
    return error("Only letters, numbers, - and _ allowed")

  # Uniqueness check
  if exists_in_reserved_codes(code):
    return error("This code is reserved by Cooking")

  if exists_in_invite_codes(code):
    return error("This code is already taken")

  # Profanity filter
  if contains_offensive_language(code):
    return error("This code is not allowed")

  return success("Code is available")
```

### Deeplink Handling (Mobile)

```
cooking://signup?ref=CRYPTO2025
```

When mobile app launches with this deeplink:
1. Extract invite code from URL
2. Pre-fill in signup flow
3. Associate on signup completion

---

## Migration Strategy

### For Existing Users with Auto-Generated Codes

**Option 1**: Keep existing auto-generated code
- Allow them to create a custom code as well (one active code at a time)

**Option 2**: Force migration to custom code
- Prompt existing referrers to claim a custom code
- Maintain referral relationships

**Recommended**: Option 1 for backward compatibility

---

## Analytics & Monitoring

### Track Metrics
- Custom code creation rate
- Signup via link vs. manual code entry
- Post-signup referral linking rate
- Code sharing methods (link vs. code)
- Most popular code patterns/lengths

---

## Future Enhancements

### Multiple Codes per User
- Different codes for different campaigns
- Track performance by code

### QR Code Generation
- Generate QR code containing referral link
- Easy sharing in-person or in content

### Vanity URLs
- cooking.gg/join/CRYPTO2025
- Shorter, cleaner URLs for marketing

---

**Status**: In development
**Priority**: High - Enables mobile support and flexible referral linking
**Dependencies**: Referral program v2, mobile app
**Next Steps**:
1. Implement invite code creation UI
2. Build code validation service
3. Populate reserved codes list
4. Add manual code entry to signup flow
5. Create post-signup referral linking option
6. Implement deeplink handling for mobile
7. Test across web and mobile
8. Migrate existing auto-generated codes (if needed)
9. Deploy with user education
