---
title: Settings Feature Specification
type: feature-specification
status: in-development
priority: high
created: 2025-08-20
date: 2025-10-20
updated: 2025-10-20
tags: [settings, account-management, security, user-experience]
related:
  - "[[security-password-wallet-manager]]"
  - "[[social-login-integration]]"
  - "[[platform-vision-requirements]]"
---

# Settings Feature Specification

## Overview

The intent of this feature is to centralize certain important settings in an easy to locate place for the user to access when needed. We understand most of these won't be required on a daily basis, but that is not an excuse for not having them accessible or scattered throughout the product.

## Access Point

In the navigation sidebar, the user will now find a **'Settings'** item. When clicking it, this will deploy a modal with 3 distinct sections:

1. **Account**: Manage Cooking Tag and Login Methods
2. **Shortcuts**: Consult navigation shortcuts
3. **Security**: Create or update Security Password

---

## Section 1: Account

### Cooking Tag

#### Overview

The Cooking Tag is a display name used to identify users within the Cooking ecosystem. This is especially important since Cooking doesn't require their users to perform any KYC before joining the product.

#### Initial Assignment

When first signing up, all traders will be assigned a tag **automatically generated**.

#### Update Rules

**User Permissions**:
- Tag can be updated **only once** by the user

**Admin Permissions**:
- Can be updated **many times** by an admin through the backoffice

#### Tag Requirements

**Uniqueness**: Each tag will be unique across the platform

**Format**:
- Length: **6 to 12 characters**
- Allowed characters:
  - Letters (a-z, A-Z)
  - Numbers (0-9)
  - Special characters: `. ! - / @ # $ €`
- **Spaces are not accepted**

#### Examples

Valid tags:
- `Trader#42`
- `Crypto.King`
- `Moon-Shot!`
- `User@2025`

Invalid tags:
- `Joe` (too short)
- `My Crypto Tag` (contains spaces)
- `VeryLongUsername123` (too long)

### Login Methodologies

#### Default Method

The method used to sign up is going to be the **default login method**.

#### Adding Fallback Methods

After signing up, users can include fallback methods to ensure access to their Cooking account.

#### Security Requirement

**Before accessing** the webview that allows for linking to another account, the user must **sign the transaction with their security password**. Otherwise the action should be truncated.

#### Supported Methods

- Google
- Apple ID
- Twitter
- Telegram
- Solana Wallet

#### User Flow

1. User navigates to Settings > Account > Login Methodologies
2. Views currently linked methods
3. Clicks "Add Login Method"
4. Prompted for Security Password
5. Enters password successfully
6. Redirected to provider authentication
7. Provider validates identity
8. New method linked to account
9. Confirmation notification displayed

---

## Section 2: Shortcuts

### Purpose

List with all the available keyboard shortcuts for navigation.

### Behavior

The user **cannot perform any action** here - this is a **read-only reference section**.

### Content Structure

Display format:
```
Action                Shortcut
--------------------------------
Open Token Search     CMD/CTRL + K
Create New Order      CMD/CTRL + N
Open Wallet Manager   CMD/CTRL + W
Toggle Portfolio      CMD/CTRL + P
View Trade History    CMD/CTRL + H
Open Settings         CMD/CTRL + ,
```

### Platform-Specific

- **macOS**: Display CMD
- **Windows/Linux**: Display CTRL

---

## Section 3: Security

### Create Security Password

#### Form Requirements

A form to create the Security Password with the following requirements:

**Password Rules**:
- At least **8 characters long**
- Include an **uppercase letter**
- Include a **number**
- Include a **symbol** (`@&$!#?`)

#### Security Implementation

- **Generated client-side**
- **Encrypted in the backend** after being submitted

#### Verification

- User must verify the password by **repeating it successfully**
- Must **acknowledge and accept full responsibility** for storing it in a private and safe location

#### Co-existence with Wallet Manager

This flow will co-exist with the current implementation in the Wallet Manager:

**Logic**:
- Whichever one the user completes first will invalidate the other one
- If user creates password from **Settings**, then **Wallet Manager** won't enforce creation
- If user creates password from **Wallet Manager**, then **Settings** won't enforce creation

#### Acknowledgment Text

```
⚠️ Security Password Responsibility

I understand that:
• This password protects sensitive wallet operations
• I am solely responsible for storing it securely
• Cooking cannot recover or reset this password
• Loss of this password may result in loss of access to critical features

☑️ I accept full responsibility for securing my password
```

### Update Security Password

#### Requirements

After the security Password has been created, users can always update it:

**Process**:
1. Must fulfill the same password requirements
2. Must **sign the action with the current password**
3. Must verify new password by repeating it
4. Must acknowledge responsibility

#### Acknowledgment

This action also requires an acknowledgment on importance and responsibility on storing it privately.

#### Deprecation

With this flow we will **deprecate** the existing 'Update Security Password' flow in the Wallet Manager.

---

## User Experience Considerations

### Modal Design

**Modal Behavior**:
- Overlay on current screen
- Dismissible by clicking outside or ESC key
- Responsive design for mobile and desktop
- Smooth animations

**Navigation**:
- Tab-based interface between sections
- Active section highlighted
- Breadcrumb trail if needed

### Accessibility

- Keyboard navigation support
- Screen reader compatible
- High contrast mode support
- Focus management

### Error Handling

**Password Creation Errors**:
- Real-time validation feedback
- Clear error messages
- Suggestions for fixing issues

**Login Method Linking Errors**:
- Provider-specific error messages
- Retry option
- Fallback contact support

### Confirmation Feedback

**Success Messages**:
- "Cooking Tag updated successfully"
- "Login method linked successfully"
- "Security password created successfully"
- "Security password updated successfully"

**Visual Feedback**:
- Green checkmark for success
- Toast notifications
- Updated display of changes

---

## Technical Implementation

### State Management

- Current user settings loaded on modal open
- Local state for form inputs
- Optimistic updates for better UX

### API Endpoints

```
GET  /api/user/settings
PUT  /api/user/cooking-tag
POST /api/user/login-methods
POST /api/user/security-password
PUT  /api/user/security-password
```

### Security

- All sensitive operations require security password
- HTTPS required
- CSRF protection
- Rate limiting on password attempts

### Validation

**Client-side**:
- Immediate feedback on input
- Password strength meter
- Format validation

**Server-side**:
- Double-check all validation rules
- Uniqueness checks (Cooking Tag)
- Security password verification

---

## Future Enhancements

### Account Section
- Two-factor authentication (2FA) setup
- Email notifications preferences
- Language preferences
- Time zone settings

### Shortcuts Section
- Customizable shortcuts
- Search/filter shortcuts
- Print/export shortcut list

### Security Section
- Biometric authentication
- Session management
- Login history
- Trusted devices management

---

## Mobile Considerations

### Responsive Design

- Full-screen modal on mobile
- Touch-friendly buttons and inputs
- Virtual keyboard optimization

### Mobile-Specific Features

- Biometric unlock for security password
- Copy to clipboard for Cooking Tag
- Deep links for social login

---

## Analytics & Monitoring

### Track Metrics

- Settings modal open rate
- Section usage distribution
- Cooking Tag update frequency
- Login methods added per user
- Security password creation/update rate
- Error rates by action

### User Behavior

- Time spent in each section
- Abandonment rates
- Common error patterns
- Support ticket correlation

---

**Status**: In development
**Priority**: High - Improves user experience and security management
**Next Steps**:
1. Design modal UI/UX
2. Implement Settings modal structure
3. Build Account section (Cooking Tag, Login Methods)
4. Build Shortcuts section (read-only list)
5. Build Security section (password creation/update)
6. Integrate with existing Wallet Manager flows
7. Test cross-platform (web + mobile)
8. Deploy and monitor adoption
