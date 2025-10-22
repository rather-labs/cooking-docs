---
title: Type-Safe API Client Generation
type: decision-record
decision-id: ADR-103
date: 2025-10-10
status: accepted
owner: Martin Aranda
stakeholders: [Martin Aranda, Lucas Cufre, Frontend Team, Backend Team]
tags: [technical, typescript, api, code-generation, type-safety, developer-experience]
summary: |
  Decision to implement automated type-safe API client generation from backend API definitions to prevent runtime errors caused by frontend-backend type mismatches. The system auto-generates TypeScript clients for all services (main backend and microservices), providing compile-time type checking that catches breaking changes during development instead of production. Triggered by production bug where backend endpoint changes broke frontend transfers due to lack of type safety.
related-docs:
  - ../06-meetings/2025-10/2025-10-10-daily-standup.md
  - ADR-002: Microservices Architecture by Trading Algorithm
---

# Type-Safe API Client Generation

## Context and Problem Statement

Cooking.gg's architecture includes frontend applications (web React, mobile React Native) communicating with backend services (main backend + multiple microservices) via REST APIs. This distributed architecture creates type safety challenges:

**The Production Incident (October 2025):**

Esteban Restrepo migrated the "transfer funds" endpoint from the main backend to the new transaction microservice. The endpoint signature changed slightly:

```typescript
// Old endpoint (main backend)
POST /api/transfer
{
  "tokenAddress": "EPjF...",
  "amount": 1000000,
  "recipientAddress": "7xH..."
}

// New endpoint (transaction microservice)
POST /api/transactions/transfer
{
  "token_address": "EPjF...",  // Changed: camelCase → snake_case
  "amount": 1000000,
  "recipient_address": "7xH...", // Changed: camelCase → snake_case
  "user_id": "user-123"          // Added: required field
}
```

**What Happened:**

1. Backend deployed with new endpoint (breaking change)
2. Frontend still calling old endpoint signature
3. Transfers failed in production for all users
4. **Detection:** Users reported "transfer not working" (runtime failure)
5. **Root Cause:** No compile-time type checking between frontend and backend
6. **Time to Fix:** 2 hours (identify issue, update frontend, deploy)

**Why This Happened:**

- Frontend manually defines API client types (separate from backend)
- Backend changes don't automatically update frontend types
- TypeScript can't validate across service boundaries
- No automated contract validation in CI/CD pipeline

**Broader Problem: Microservices Amplify Type Safety Issues**

Cooking.gg's microservices architecture (ADR-002) exacerbates this problem:

- **Main Backend:** User management, authentication, wallet operations
- **Transaction Microservice:** Swap execution, transfers, order management
- **Indexer Service:** Token data, price feeds, historical trades
- **Future Microservices:** More services = more API boundaries

Each service has its own API contract. Frontend must integrate with all services. Without type safety, each service is a potential source of runtime failures.

**Current Manual Approach:**

```typescript
// Frontend: manually written API client (types can drift)
// src/api/transactions.ts
interface TransferRequest {
  tokenAddress: string;   // ❌ Doesn't match backend
  amount: number;
  recipientAddress: string;
}

async function transferFunds(request: TransferRequest) {
  return fetch('/api/transfer', {
    method: 'POST',
    body: JSON.stringify(request)
  });
}
```

```typescript
// Backend: actual endpoint definition (source of truth)
// transaction-service/src/controllers/transfer.ts
interface TransferRequestDto {
  token_address: string;   // ✅ Actual signature
  amount: number;
  recipient_address: string;
  user_id: string;
}

@Post('/transactions/transfer')
async transfer(@Body() request: TransferRequestDto) {
  // ...
}
```

**Types drift over time. No compile-time validation across services.**

**Additional Pain Points:**

1. **Onboarding New Developers:**
   - Must manually learn API contracts by reading backend code
   - No IDE autocomplete for API endpoints
   - High likelihood of errors (wrong field names, missing parameters)

2. **Refactoring Risk:**
   - Backend refactors (field renames, type changes) require manual frontend updates
   - Easy to miss dependent endpoints
   - Regression bugs slip through code review

3. **Documentation Drift:**
   - API documentation (if it exists) becomes outdated
   - Frontend developers rely on stale docs
   - Trial-and-error API integration

4. **Testing Gaps:**
   - Integration tests don't catch type mismatches (JSON serialization masks issues)
   - Type errors only surface at runtime with real user data

**User Impact:**

- Critical features fail in production (transfers, swaps, orders)
- Degraded user experience (error messages, failed transactions)
- Lost revenue (users can't trade)
- Support burden (debugging production issues)

**Requirements for Solution:**

1. **Compile-Time Type Safety:** Catch type mismatches before deployment
2. **Automatic Synchronization:** Backend changes instantly reflect in frontend types
3. **Microservices Coverage:** Support all services (current and future)
4. **Developer Experience:** IDE autocomplete, inline documentation
5. **Minimal Overhead:** Generation should be fast, not slow down builds
6. **Integration:** Fit into existing CI/CD pipeline

## Decision

**Implement automated type-safe API client generation using OpenAPI (Swagger) specifications and code generation tools (openapi-typescript-codegen or similar) to auto-generate TypeScript clients from backend API definitions.**

### Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                     Backend Services                              │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────┐ │
│  │  Main Backend   │  │  Transaction MS  │  │  Indexer MS     │ │
│  │  (NestJS)       │  │  (NestJS)        │  │  (NestJS)       │ │
│  └────────┬────────┘  └────────┬─────────┘  └────────┬────────┘ │
│           │                    │                      │          │
│           ▼                    ▼                      ▼          │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────┐ │
│  │ OpenAPI Spec    │  │ OpenAPI Spec     │  │ OpenAPI Spec    │ │
│  │ (swagger.json)  │  │ (swagger.json)   │  │ (swagger.json)  │ │
│  └────────┬────────┘  └────────┬─────────┘  └────────┬────────┘ │
└───────────┼────────────────────┼──────────────────────┼──────────┘
            │                    │                      │
            └────────────┬───────┴──────────────────────┘
                         │
                         ▼
            ┌─────────────────────────────────┐
            │   Code Generation Tool          │
            │  (openapi-typescript-codegen)   │
            │  - Reads OpenAPI specs          │
            │  - Generates TypeScript clients │
            │  - Creates type definitions     │
            └────────────┬────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│                  Generated API Clients                            │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────┐ │
│  │ mainApi.ts      │  │ transactionApi.ts│  │ indexerApi.ts   │ │
│  │ - TypeScript    │  │ - TypeScript     │  │ - TypeScript    │ │
│  │ - Type-safe     │  │ - Type-safe      │  │ - Type-safe     │ │
│  │ - Auto-complete │  │ - Auto-complete  │  │ - Auto-complete │ │
│  └────────┬────────┘  └────────┬─────────┘  └────────┬────────┘ │
└───────────┼────────────────────┼──────────────────────┼──────────┘
            │                    │                      │
            └────────────┬───────┴──────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│                    Frontend Application                           │
│  - Import generated clients                                       │
│  - Compile-time type checking                                     │
│  - IDE autocomplete and inline docs                               │
│  - Type errors caught before runtime                              │
└──────────────────────────────────────────────────────────────────┘
```

### Implementation Steps

**1. Backend: Generate OpenAPI Specifications**

NestJS (backend framework) has built-in OpenAPI support via `@nestjs/swagger`:

```typescript
// main.ts - Configure Swagger documentation
import { NestFactory } from '@nestjs/core';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Swagger configuration
  const config = new DocumentBuilder()
    .setTitle('Cooking.gg API')
    .setDescription('Trading platform REST API')
    .setVersion('1.0')
    .addBearerAuth()
    .build();

  const document = SwaggerModule.createDocument(app, config);

  // Expose OpenAPI spec at /api/docs
  SwaggerModule.setup('api/docs', app, document);

  // Export spec as JSON file for code generation
  const fs = require('fs');
  fs.writeFileSync('./openapi.json', JSON.stringify(document, null, 2));

  await app.listen(3000);
}
```

**2. Backend: Annotate DTOs and Endpoints**

Use Swagger decorators to document types:

```typescript
// transfer.dto.ts - Data Transfer Object
import { ApiProperty } from '@nestjs/swagger';
import { IsString, IsNumber, IsPositive } from 'class-validator';

export class TransferRequestDto {
  @ApiProperty({
    description: 'Solana token address to transfer',
    example: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
  })
  @IsString()
  token_address: string;

  @ApiProperty({
    description: 'Amount of tokens to transfer (in smallest unit)',
    example: 1000000
  })
  @IsNumber()
  @IsPositive()
  amount: number;

  @ApiProperty({
    description: 'Recipient wallet address',
    example: '7xH3FJzMcPpqVNqPCu7YSiPaBbsE3sZp9qJZX2jtHKcx'
  })
  @IsString()
  recipient_address: string;

  @ApiProperty({
    description: 'User ID initiating transfer',
    example: 'user-123'
  })
  @IsString()
  user_id: string;
}

export class TransferResponseDto {
  @ApiProperty({ description: 'Transaction signature' })
  signature: string;

  @ApiProperty({ description: 'Transaction status' })
  status: 'success' | 'pending' | 'failed';
}
```

```typescript
// transfer.controller.ts - Controller with Swagger annotations
import { Controller, Post, Body } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse } from '@nestjs/swagger';

@ApiTags('transactions')
@Controller('transactions')
export class TransferController {
  @Post('transfer')
  @ApiOperation({ summary: 'Transfer tokens between wallets' })
  @ApiResponse({
    status: 200,
    description: 'Transfer successful',
    type: TransferResponseDto
  })
  @ApiResponse({
    status: 400,
    description: 'Invalid request'
  })
  async transfer(
    @Body() request: TransferRequestDto
  ): Promise<TransferResponseDto> {
    // Implementation
  }
}
```

**3. Code Generation: Generate TypeScript Clients**

Install code generation tool:

```bash
npm install --save-dev openapi-typescript-codegen
```

Create generation script:

```json
// package.json
{
  "scripts": {
    "generate:api-clients": "node scripts/generate-api-clients.js"
  }
}
```

```javascript
// scripts/generate-api-clients.js
const { generate } = require('openapi-typescript-codegen');

async function generateClients() {
  // Generate client for main backend
  await generate({
    input: 'http://localhost:3000/api/docs-json',  // Or path to openapi.json
    output: './src/api/generated/main',
    httpClient: 'fetch',
    useOptions: true,
    useUnionTypes: true,
    exportCore: true,
    exportServices: true,
    exportModels: true
  });

  // Generate client for transaction microservice
  await generate({
    input: 'http://localhost:3001/api/docs-json',
    output: './src/api/generated/transactions',
    httpClient: 'fetch',
    useOptions: true,
    useUnionTypes: true
  });

  // Generate client for indexer microservice
  await generate({
    input: 'http://localhost:3002/api/docs-json',
    output: './src/api/generated/indexer',
    httpClient: 'fetch',
    useOptions: true,
    useUnionTypes: true
  });

  console.log('✅ API clients generated successfully');
}

generateClients().catch(console.error);
```

**4. Frontend: Use Generated Clients**

```typescript
// src/api/generated/transactions/services/TransactionService.ts (auto-generated)
export class TransactionService {
  /**
   * Transfer tokens between wallets
   * @param requestBody Transfer request
   * @returns TransferResponseDto Transfer successful
   * @throws ApiError
   */
  public static async transfer(
    requestBody: TransferRequestDto
  ): Promise<TransferResponseDto> {
    const result = await __request({
      method: 'POST',
      url: '/transactions/transfer',
      body: requestBody,
      errors: {
        400: 'Invalid request'
      }
    });
    return result.body;
  }
}

// src/api/generated/transactions/models/TransferRequestDto.ts (auto-generated)
export interface TransferRequestDto {
  /** Solana token address to transfer */
  token_address: string;
  /** Amount of tokens to transfer (in smallest unit) */
  amount: number;
  /** Recipient wallet address */
  recipient_address: string;
  /** User ID initiating transfer */
  user_id: string;
}
```

Frontend usage (type-safe):

```typescript
// src/features/wallet/TransferForm.tsx
import { TransactionService, TransferRequestDto } from '@/api/generated/transactions';

async function handleTransfer(tokenAddress: string, amount: number, recipient: string) {
  try {
    // ✅ TypeScript validates this at compile-time
    const response = await TransactionService.transfer({
      token_address: tokenAddress,   // Correct field name (type-safe)
      amount: amount,
      recipient_address: recipient,
      user_id: currentUser.id
    });

    // ❌ This would be caught at compile-time:
    // await TransactionService.transfer({
    //   tokenAddress: tokenAddress,  // ERROR: Property 'tokenAddress' does not exist
    //   amount: amount
    // });

    console.log('Transfer successful:', response.signature);
  } catch (error) {
    console.error('Transfer failed:', error);
  }
}
```

**IDE Benefits:**

- **Autocomplete:** IDE suggests `token_address`, `amount`, `recipient_address`, `user_id`
- **Inline Documentation:** Hover shows field descriptions from `@ApiProperty`
- **Type Checking:** Missing fields or wrong types caught immediately
- **Refactoring:** Rename backend field → TypeScript errors guide frontend updates

### CI/CD Integration

**Option 1: Pre-commit Hook (Generate on Developer Machine)**

```json
// .husky/pre-commit
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

npm run generate:api-clients
git add src/api/generated
```

**Pros:**
- Immediate feedback (developers see type errors before pushing)
- No CI/CD pipeline dependency

**Cons:**
- Requires backend services running locally
- Slows down commits

**Option 2: GitHub Actions (Generate on Push)**

```yaml
# .github/workflows/generate-api-clients.yml
name: Generate API Clients

on:
  push:
    branches: [main, develop]
    paths:
      - 'backend/**/*.dto.ts'
      - 'backend/**/*.controller.ts'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Start backend services
        run: |
          docker-compose up -d backend transaction-service indexer-service
          sleep 10  # Wait for services to be ready

      - name: Generate API clients
        run: npm run generate:api-clients

      - name: Commit generated files
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add src/api/generated
          git commit -m "chore: regenerate API clients" || echo "No changes"
          git push

      - name: Shutdown services
        run: docker-compose down
```

**Pros:**
- No developer machine dependency
- Automated, consistent generation

**Cons:**
- Slight delay (developers must pull after backend changes)
- Requires CI/CD infrastructure

**Decision (Pending):** Martin noted "needs decision on when to run generation (GitHub actions timing)". Team will evaluate trade-offs and decide on generation trigger.

### Handling Multiple Microservices

As microservices architecture grows (ADR-002), each service gets its own generated client:

```typescript
// src/api/index.ts - Central API export
export * from './generated/main';
export * from './generated/transactions';
export * from './generated/indexer';

// Future microservices
// export * from './generated/perpetuals';
// export * from './generated/referrals';
```

Frontend imports specific service:

```typescript
import { TransactionService } from '@/api';
import { IndexerService } from '@/api';
import { UserService } from '@/api';
```

**No naming conflicts:** Each service namespaced by service name.

### Versioning and Backward Compatibility

**Breaking Changes Detection:**

If backend introduces breaking change, frontend build fails:

```typescript
// Backend changes field name: token_address → tokenAddress
// Frontend code using old generated client:
await TransactionService.transfer({
  token_address: tokenAddress,  // ❌ TypeScript error after regeneration
  // Property 'token_address' does not exist on type 'TransferRequestDto'
  // Did you mean 'tokenAddress'?
});
```

**Migration Path:**

1. Backend introduces breaking change with new version (`/v2/transfer`)
2. Generate new client (includes v1 and v2 endpoints)
3. Frontend migrates incrementally (v1 → v2)
4. Deprecate v1 once migration complete

**Semantic Versioning:**

```typescript
// OpenAPI spec version
{
  "openapi": "3.0.0",
  "info": {
    "version": "1.2.0"  // Increment on breaking changes
  }
}
```

## Rationale

### Type Safety Prevents Entire Class of Bugs

**Production Incident Impact:**

- **Transfer Bug:** 2 hours downtime, users unable to transfer funds
- **Root Cause:** Type mismatch between frontend and backend
- **Detection:** Runtime (production), not compile-time
- **Fix Effort:** 2 hours (identify + update + deploy)

**With Type-Safe Client Generation:**

- **Detection:** Compile-time (developer machine or CI)
- **Fix Effort:** Immediate (IDE highlights error, developer fixes before commit)
- **Production Impact:** Zero (bug never reaches production)

**Prevented Bug Categories:**

1. **Field Name Mismatches:** `tokenAddress` vs `token_address`
2. **Missing Required Fields:** Forgot `user_id` parameter
3. **Type Mismatches:** Passed string instead of number
4. **Endpoint URL Errors:** Wrong path `/transfer` vs `/transactions/transfer`
5. **Response Handling:** Wrong response structure assumptions

**Cost of Runtime Bugs:**

- User frustration (features don't work)
- Support tickets (debugging user issues)
- Developer time (emergency fixes)
- Revenue loss (users can't trade)
- Reputation damage (platform unreliability)

**Type safety eliminates this entire category of bugs.**

### Developer Experience Improvement

**Before (Manual API Clients):**

Developer workflow:
1. Read backend code to understand endpoint signature
2. Manually write frontend API call
3. Hope types match (no verification)
4. Test in development (trial and error)
5. Fix runtime errors as they occur

**After (Generated API Clients):**

Developer workflow:
1. Import generated service
2. IDE autocomplete shows available methods and parameters
3. TypeScript validates types at compile-time
4. Code works first try (assuming business logic correct)

**Onboarding Time:**

- New developers don't need to read backend code to integrate APIs
- IDE autocomplete teaches API contracts
- Inline documentation explains parameters

**Refactoring Confidence:**

Backend developer renames field:
- **Before:** Hope frontend developers notice and update (likely missed)
- **After:** TypeScript errors guide all necessary frontend updates

### Microservices Architecture Amplification

**Problem Scale:**

Without type generation:
- 1 backend service = 1 API boundary to manually maintain
- 5 microservices = 5 API boundaries to manually maintain
- 10 microservices = 10 API boundaries to manually maintain

**With type generation:**
- N microservices = N automated clients (no additional manual work)

**Cooking.gg Microservices (ADR-002):**

Current:
- Main backend
- Transaction microservice
- Indexer microservice

Future (planned):
- Perpetuals microservice
- Referral microservice
- Analytics microservice

**Each new microservice:** Automatic type-safe client. No additional developer burden.

### Industry Best Practice

**Companies Using Generated Clients:**

- **Stripe:** Auto-generated clients for 8+ languages
- **Twilio:** OpenAPI-based client libraries
- **GitHub:** Octokit generated from OpenAPI specs
- **AWS:** SDK generation from service definitions

**Why They Use It:**

- Scale: hundreds of API endpoints, impossible to manually maintain
- Consistency: same patterns across all endpoints
- Accuracy: source of truth is API definition, not documentation

### Alternative Approaches Rejected

**GraphQL Instead of REST:**

- **Pro:** Built-in type safety (GraphQL schema enforced)
- **Con:** Requires complete backend rewrite (too costly)
- **Con:** Team unfamiliar with GraphQL (learning curve)
- **Decision:** REST + code generation achieves type safety without rewrite

**Manual TypeScript Definitions:**

- **Pro:** Full control over types
- **Con:** Manual synchronization (types drift)
- **Con:** Exactly the problem we're trying to solve

**tRPC (TypeScript RPC):**

- **Pro:** End-to-end type safety for TypeScript monorepos
- **Con:** Requires shared TypeScript codebase (backend + frontend)
- **Con:** Doesn't support microservices in different repos
- **Decision:** OpenAPI generation more flexible for distributed architecture

## Consequences

### Positive

**Bug Prevention:**
- Entire class of type mismatch bugs eliminated
- Frontend-backend contract violations caught at compile-time
- Production stability improved (fewer runtime errors)

**Developer Experience:**
- IDE autocomplete for all API endpoints
- Inline documentation from `@ApiProperty` decorators
- Faster development (no trial-and-error API integration)
- Easier onboarding (API contracts self-documenting)

**Refactoring Safety:**
- Backend changes instantly surface required frontend updates
- TypeScript errors guide developers to all affected code
- Confident refactoring (compiler verifies correctness)

**Microservices Scalability:**
- N microservices = N automated clients (no additional manual effort)
- Consistent patterns across all services
- No inter-service type drift

**Documentation Accuracy:**
- OpenAPI spec is source of truth (can't drift from implementation)
- Interactive API docs (Swagger UI) always up-to-date
- Frontend types guaranteed to match backend

**Testing Efficiency:**
- Integration tests focus on business logic, not type correctness
- Type errors caught before tests run (faster feedback loop)

### Negative

**Build Complexity:**
- New build step (API client generation)
- Requires backend services running during generation (or access to OpenAPI specs)
- CI/CD pipeline more complex (start services, generate, commit)

**Generated Code Volume:**
- Generated TypeScript files can be large (hundreds of KB)
- Repository size increases (mitigated by `.gitignore` if desired)
- Build artifacts may be noisy in PRs

**Backend Annotation Burden:**
- Developers must annotate DTOs with `@ApiProperty` decorators
- Adds boilerplate to backend code
- Incomplete annotations = incomplete type safety

**Regeneration Timing Uncertainty:**
- Team hasn't decided when to trigger generation (pre-commit, GitHub actions, manually)
- Wrong timing = developers working with stale types
- Requires team process/workflow decision

**Learning Curve:**
- Team must learn OpenAPI specification format
- Understand code generation tool configuration
- Debugging generated code more difficult (abstraction layer)

**Version Synchronization:**
- Frontend must regenerate after backend changes
- Asynchronous updates (backend deployed, frontend not yet updated) create temporary mismatch
- Requires deployment coordination

**Breaking Changes:**
- Backend breaking changes fail frontend build (good for safety, bad for velocity)
- May require coordination between frontend and backend teams
- Migration effort for large breaking changes

### Neutral

**OpenAPI Specification Dependency:**
- Platform tied to OpenAPI standard (widely adopted, but dependency nonetheless)
- Alternative: tRPC, GraphQL, Protocol Buffers

**Tooling Choice:**
- Selected `openapi-typescript-codegen` (could use alternatives: `openapi-generator`, `swagger-codegen`)
- Tool migration possible but requires effort

## Alternatives Considered

### Option 1: Manual TypeScript Type Definitions (Status Quo)

**Description:** Frontend developers manually write TypeScript interfaces matching backend DTOs

**Pros:**
- Simple (no tooling required)
- Full control over types
- No build step

**Cons:**
- Types drift from backend (no synchronization)
- Manual updates required for every backend change
- Exactly the problem causing production bugs

**Why Rejected:** This is the current approach that caused the transfer bug. Manual synchronization is error-prone and unscalable.

### Option 2: GraphQL

**Description:** Replace REST APIs with GraphQL, leverage built-in schema and type safety

**Pros:**
- Built-in type safety (GraphQL schema enforced at runtime)
- Client-specified queries (no over-fetching)
- Single endpoint (simplifies architecture)

**Cons:**
- Complete backend rewrite required (REST → GraphQL)
- Team unfamiliar with GraphQL (steep learning curve)
- Complexity: resolvers, schemas, caching strategies
- Overkill for simple CRUD operations

**Why Rejected:** Cost of migration too high. REST + code generation achieves type safety without rewrite.

### Option 3: tRPC (TypeScript RPC)

**Description:** End-to-end type safety for TypeScript applications using RPC pattern

**Pros:**
- Perfect type safety (backend types exported to frontend directly)
- No code generation (types shared via TypeScript compiler)
- Excellent developer experience

**Cons:**
- Requires shared TypeScript codebase (monorepo)
- Doesn't support microservices in separate repos
- Backend must be TypeScript (NestJS compatible, but adds constraints)
- Coupling between frontend and backend codebases

**Why Rejected:** Cooking.gg has separate repos for services. tRPC requires monorepo or complex setup. OpenAPI generation more flexible for distributed microservices.

### Option 4: Protocol Buffers (Protobuf)

**Description:** Define service contracts in `.proto` files, generate code for frontend and backend

**Pros:**
- Strong type safety (contract-first design)
- Language-agnostic (supports multiple languages)
- Efficient binary serialization (performance benefit)

**Cons:**
- Requires learning Protobuf syntax
- Additional build step (proto compilation)
- REST APIs would need translation layer (gRPC-Web)
- Team unfamiliar with Protobuf ecosystem

**Why Rejected:** Learning curve and ecosystem change too significant. OpenAPI aligns with existing REST architecture.

### Option 5: JSON Schema Validation

**Description:** Define JSON schemas for API contracts, validate requests/responses at runtime

**Pros:**
- Runtime validation (catches errors in production)
- Schema-driven (single source of truth)
- Language-agnostic

**Cons:**
- Runtime validation (errors caught late, not compile-time)
- Performance overhead (validation on every request)
- Doesn't provide TypeScript types (still manual type definitions)

**Why Rejected:** Runtime validation doesn't solve compile-time type safety problem. OpenAPI can generate both validators and types.

## Implementation Notes

### OpenAPI Decorator Best Practices

**Comprehensive Annotations:**

```typescript
import { ApiProperty } from '@nestjs/swagger';

export class CreateOrderDto {
  @ApiProperty({
    description: 'Token to trade',
    example: 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v',
    required: true
  })
  token_address: string;

  @ApiProperty({
    description: 'Order type',
    enum: ['market', 'limit', 'twap', 'dca'],
    example: 'limit'
  })
  order_type: 'market' | 'limit' | 'twap' | 'dca';

  @ApiProperty({
    description: 'Order amount in tokens',
    type: Number,
    minimum: 1,
    example: 1000000
  })
  amount: number;

  @ApiProperty({
    description: 'Limit price (required for limit orders)',
    type: Number,
    required: false,
    nullable: true
  })
  limit_price?: number;
}
```

**Enum Documentation:**

```typescript
export enum OrderStatus {
  PENDING = 'pending',
  OPEN = 'open',
  FILLED = 'filled',
  CANCELLED = 'cancelled',
  FAILED = 'failed'
}

@ApiProperty({
  enum: OrderStatus,
  description: 'Current order status',
  example: OrderStatus.PENDING
})
status: OrderStatus;
```

### Code Generation Configuration

**Recommended Settings:**

```javascript
{
  httpClient: 'fetch',      // Use native fetch API
  useOptions: true,         // Generate options parameter for flexibility
  useUnionTypes: true,      // Use union types instead of enums
  exportCore: true,         // Export core utilities (ApiError, etc.)
  exportServices: true,     // Export service classes
  exportModels: true,       // Export model interfaces
  indent: '  ',             // 2-space indentation
  postfixModels: 'Dto',     // Suffix model names with Dto
  postfixServices: 'Service' // Suffix service names with Service
}
```

### Version Control Strategy

**Option A: Commit Generated Files**

```
src/
  api/
    generated/       # ✅ Committed to git
      main/
      transactions/
      indexer/
```

**Pros:**
- Frontend builds work immediately (no generation step)
- Developers see exactly what changed in PRs

**Cons:**
- Larger diffs (generated code changes)
- Potential merge conflicts

**Option B: Ignore Generated Files**

```
# .gitignore
src/api/generated/
```

**Pros:**
- Cleaner commits (no generated code)
- No merge conflicts in generated files

**Cons:**
- Requires generation step on every checkout/pull
- CI/CD must generate before build

**Recommendation:** Commit generated files for easier developer experience.

### Monitoring and Validation

**Pre-Deployment Validation:**

```bash
# scripts/validate-api-clients.sh
#!/bin/bash

# Generate fresh API clients
npm run generate:api-clients

# Check for git changes (indicates backend changed without regeneration)
if ! git diff --quiet src/api/generated; then
  echo "❌ API clients out of date. Run 'npm run generate:api-clients'"
  exit 1
fi

echo "✅ API clients up to date"
```

**Add to CI:**

```yaml
# .github/workflows/ci.yml
- name: Validate API clients
  run: npm run validate:api-clients
```

## References

### Meeting Notes
- [Daily Standup 2025-10-10](../06-meetings/2025-10/2025-10-10-daily-standup.md) - Type-safe API client generation implementation, production bug trigger

### Related Decisions
- ADR-002: Microservices Architecture by Trading Algorithm (multiple services amplify type safety need)

### Technical References
- OpenAPI Specification: https://swagger.io/specification/
- NestJS OpenAPI (Swagger): https://docs.nestjs.com/openapi/introduction
- openapi-typescript-codegen: https://github.com/ferdikoomen/openapi-typescript-codegen
- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html

### Industry Examples
- Stripe API Client Generation: https://github.com/stripe/stripe-node
- Octokit (GitHub API): https://github.com/octokit/rest.js
- AWS SDK Generation: https://github.com/aws/aws-sdk-js-v3

## Revision History
- 2025-10-10: Type-safe API client generation implemented (triggered by production transfer bug)
- 2025-10-10: Pending decision on generation timing (GitHub actions vs pre-commit)
- 2025-10-21: Formal ADR documented from meeting notes
