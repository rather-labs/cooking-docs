# Documents to Parse - Intake Folder

This folder is the **intake point** for unstructured content that needs to be processed and structured into the knowledge base.

## Purpose

Drop any unstructured documents here and Claude Code will automatically:
1. Analyze the content
2. Extract key information
3. Create properly structured documents in appropriate locations
4. Update all relevant indexes
5. Delete the original file from this folder after successful processing

## What to Put Here

### Meeting Notes
- Raw meeting transcripts
- Unstructured meeting notes
- Email threads discussing meetings
- Slack conversations from meetings

### Technical Documentation
- Architecture diagrams with notes
- API documentation drafts
- Technical specs in raw form
- Code comments or design documents

### Research & Findings
- Research notes
- Competitive analysis data
- User study results
- Investigation findings

### Requirements
- Product requirement documents
- User stories (unstructured)
- Feature requests
- Specifications

### Status Reports
- Project updates
- Progress reports
- Team updates
- Sprint summaries

### Email & Chat Logs
- Important email threads
- Slack/Teams conversations
- Discussion threads with decisions

### Any Other Project Content
If you have project-related content that needs proper structure, drop it here!

## How It Works

### 1. You Add Content
Simply copy/paste or save files to this directory:
- Text files (.txt)
- Markdown files (.md)
- Word docs (.docx) - paste as text
- Email exports
- Any text-based content

### 2. Claude Code Processes It
When Claude Code checks this folder (daily or on demand), it will:

**Analyze:**
- Determine document type(s)
- Identify key information (dates, people, decisions)
- Extract structured data

**Create:**
- Meeting notes in [06-meetings/](../06-meetings/)
- Decision records in [02-decisions/](../02-decisions/)
- Research documents in [05-research/](../05-research/)
- Technical docs in [04-knowledge-base/](../04-knowledge-base/)
- Status updates in [03-active-work/](../03-active-work/)

**Update:**
- All relevant indexes
- Glossary with new terms
- Cross-references between documents

**Clean Up:**
- Delete the original file from this folder
- Confirm all content was properly structured

### 3. You Find Structured Content
Your unstructured content is now:
- Properly formatted with metadata
- Organized in the correct location
- Indexed and discoverable
- Cross-referenced with related documents

## File Naming (for this folder)

No strict rules here - use whatever names make sense to you:
- `meeting-notes-oct-15.txt`
- `architecture-discussion.md`
- `user-research-findings.md`
- `requirements-draft.txt`

The structured documents will follow proper naming conventions after parsing.


## What Happens to Files

### ✅ After Successful Processing (Standard Workflow)

**IMPORTANT: Original files are ALWAYS deleted after successful processing!**

-  ✅ Original file is **DELETED** from this folder (mandatory)
-  ✅ Content is preserved in properly structured documents
-  ✅ All relevant indexes are updated
-  ✅ You receive a summary of what was created and deleted
-  📁 Optional: Backup created in `processed/YYYY-MM/` before deletion

**Why delete?**
- Keeps this folder clean and ready for new content
- Prevents duplicate processing
- Ensures you work with structured content, not raw files
- All information is preserved in proper documentation

### ⚠️ If Processing Cannot Complete

**Files are moved to `review-needed/` subfolder (NOT deleted):**
- ⚠️ Content was unclear or ambiguous
- ⚠️ Critical information missing (dates, context)
- ⚠️ Processing encountered an error
- ⚠️ File format not supported
- ⚠️ Unclear if should update existing or create new document

You'll receive notification explaining why the file needs manual review.
## Best Practices

### Provide Context When Possible
Add a header to your document with context:
```
Source: Sprint Planning Meeting
Date: October 15, 2025
Attendees: Alice, Bob, Carol
---
[rest of content]
```

### One Topic Per File (Preferred)
While Claude Code can handle multi-topic documents, it's easier to process:
- One meeting per file
- One decision per file
- One research topic per file

### Include Dates
Mention dates in the content or filename:
- "Meeting on 2025-10-15"
- "Decided on October 15"
- File: `2025-10-15-meeting-notes.txt`

### Name Participants
Mention who was involved:
- "Alice proposed..."
- "Bob agreed..."
- "Team decided..."

## Examples

### Example 1: Meeting Notes
**You drop:** `team-meeting-oct-15.txt`
```
Met today to discuss Q4 priorities. Alice, Bob, and Carol attended.

Discussed:
- Need to improve API performance
- User research shows confusion with onboarding

Decided:
- Will implement caching for API (Alice to own)
- Will redesign onboarding flow (Bob to research)

Action items:
- Alice: Implement Redis caching by Oct 30
- Bob: User research on onboarding by Oct 22
```

**Claude Code creates:**
1. `06-meetings/2025-10/2025-10-15-team-meeting.md` - Structured meeting note
2. `02-decisions/2025-10-15-implement-api-caching.md` - ADR for caching decision
3. `02-decisions/2025-10-15-redesign-onboarding.md` - ADR for onboarding decision
4. Updates `06-meetings/_meetings-index.md`
5. Updates `02-decisions/_decisions-index.md`
6. Deletes `team-meeting-oct-15.txt`

### Example 2: Technical Documentation
**You drop:** `api-architecture.md`
```
Our API uses a three-tier architecture:

1. API Gateway (handles auth, rate limiting)
2. Service Layer (business logic)
3. Data Layer (PostgreSQL database)

Key decisions:
- Using JWT for authentication
- Rate limit: 1000 requests/hour per user
- Database uses connection pooling (max 50 connections)
```

**Claude Code creates:**
1. `04-knowledge-base/technical/architecture/api-architecture.md` - Structured technical doc
2. `02-decisions/2025-10-17-jwt-authentication.md` - ADR for JWT decision
3. Updates `04-knowledge-base/technical/_index.md`
4. Updates `01-foundation/glossary.md` with new terms (JWT, rate limiting, etc.)
5. Deletes `api-architecture.md`

### Example 3: Research Findings
**You drop:** `user-research-findings.txt`
```
Conducted user interviews with 10 customers (Oct 10-15, 2025)

Question: Why do users abandon onboarding?

Findings:
- 8/10 said too many steps
- 7/10 confused by technical terms
- 5/10 wanted to skip and explore first

Recommendation: Reduce onboarding to 3 essential steps, add "skip for now" option
```

**Claude Code creates:**
1. `05-research/2025-10-15-onboarding-abandonment/findings.md` - Structured research doc
2. Updates `05-research/_research-index.md`
3. Updates `01-foundation/glossary.md` if new terms found
4. Deletes `user-research-findings.txt`

## Troubleshooting

### File Still Here After Processing?
Reasons a file might remain:
- Content was unclear or ambiguous
- Critical information missing (dates, context)
- Processing encountered an error
- File format not supported

Check for a note from Claude Code explaining why.

### Content Seems Lost?
It's not lost! Check:
- Relevant directories ([02-decisions/](../02-decisions/), [06-meetings/](../06-meetings/), etc.)
- Index files for new entries
- [00-PROJECT-INDEX.md](../00-PROJECT-INDEX.md) recent activity

### Wrong Categorization?
You can always:
- Move the document to the correct location
- Update the metadata
- Update the relevant indexes
- Provide feedback to improve future parsing

## Tips for Better Results

### 1. Be Explicit About Dates
Good: "Meeting on October 15, 2025"
Less good: "Meeting yesterday"

### 2. Name People and Roles
Good: "Alice (Tech Lead) proposed using Redis"
Less good: "Someone suggested caching"

### 3. Mark Decisions Clearly
Good: "We decided to use PostgreSQL because..."
Less good: "Maybe we should use PostgreSQL"

### 4. Include Context
Good: "Background: Users are complaining about slow load times..."
Less good: "Need to speed things up"

### 5. Separate Action Items
Good:
```
Action items:
- Alice: Implement caching - Due: Oct 30
- Bob: Write tests - Due: Nov 5
```

Less good: "Alice and Bob will do stuff soon"

## Need Help?

- See [Claude Code Instructions](../.claude/instructions.md#parsing-unstructured-content) for detailed parsing workflow
- Check [Maintenance Guide](../.claude/maintenance-guide.md) for processing schedule
- Review template files in other directories for structure examples

---

**Ready to get started?** Drop your first unstructured document here and let Claude Code structure it for you!
