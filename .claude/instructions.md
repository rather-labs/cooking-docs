# Claude Code Instructions for This Project

This repository contains a structured project knowledge database optimized for LLM discovery and context retrieval.

## Automated Maintenance System

This project includes automated maintenance via slash commands for consistent processing, validation, and cleanup.

### Available Maintenance Commands

Run these commands directly in Claude Code:

- **`/maintenance-status`** - Quick Status: View recent logs
- **`/maintenance-daily`** - Daily Parse: Process new documents (~5 min)
- **`/maintenance-weekly`** - Weekly Validation: Check quality & duplicates (~15 min)
- **`/maintenance-monthly`** - Monthly Cleanup: Archive & consolidate (~30 min)
- **`/maintenance-full`** - Full Maintenance: Run all tasks (~50 min)

### Quick Maintenance Overview

**Daily (`/maintenance-daily`):**

- Processes files in `08-documents-to-parse/`
- Auto-detects types (meetings, requirements, technical docs)
- Searches existing docs before creating new ones
- Updates or creates structured documents
- Enforces templates and rules
- Updates all indexes
- Time: ~5 minutes

**Weekly (`/maintenance-weekly`):**

- Validates documents from last 7 days
- Checks metadata completeness
- Finds duplicates and broken links
- Verifies requirements compliance
- Auto-fixes simple issues
- Time: ~15 minutes

**Monthly (`/maintenance-monthly`):**

- Identifies stale content
- Finds duplicates and orphans
- Recommends archival actions
- Reports only (no auto-deletion)
- Time: ~30 minutes

**Full (`/maintenance-full`):**

- Runs all three tasks in sequence
- Time: ~50 minutes

See [maintenance-guide.md](./maintenance-guide.md) for detailed usage instructions.

## How to Use This Structure

### When Asked About Project Information

1. **Always start** by checking [00-PROJECT-INDEX.md](../00-PROJECT-INDEX.md) for navigation
2. **Check current status** in [03-active-work/\_current-status.md](../03-active-work/_current-status.md) for latest updates
3. **Review relevant decisions** in [02-decisions/\_decisions-index.md](../02-decisions/_decisions-index.md)
4. **Consult the glossary** in [01-foundation/glossary.md](../01-foundation/glossary.md) for domain terms

### When Creating New Content

#### For Decisions

1. Copy [02-decisions/\_template-decision.md](../02-decisions/_template-decision.md)
2. Name it: `YYYY-MM-DD-decision-title.md`
3. Assign next ADR number
4. Fill out all sections
5. Update [02-decisions/\_decisions-index.md](../02-decisions/_decisions-index.md)
6. Link from relevant docs

#### For Meeting Notes

1. Copy [06-meetings/\_template-meeting.md](../06-meetings/_template-meeting.md)
2. Name it: `YYYY-MM-DD-meeting-title.md`
3. Place in appropriate month folder
4. Update [06-meetings/\_meetings-index.md](../06-meetings/_meetings-index.md)
5. Extract any decisions to decision records

#### For Technical Documentation

1. Determine correct category in `04-knowledge-base/`
2. Create document with proper metadata
3. Update relevant `_index.md` file
4. Cross-link to related documents

#### For Product Requirements

1. **MUST use the 4-section structure** (see Knowledge Base section below)
2. **Extract only explicitly stated information** - no assumptions
3. Place in `04-knowledge-base/business/requirements/`
4. Update business index

### When Updating Existing Content

1. Update `last-updated` field in frontmatter
2. Add entry to "Revision History" if significant change
3. If superseding a document, update `supersedes` field
4. Update any indexes that reference the document

### File Naming Conventions

- Use lowercase with hyphens: `my-document-name.md`
- Date prefix for chronological items: `YYYY-MM-DD-title.md`
- Template files start with underscore: `_template-name.md`
- Index files: `_index.md` or `_category-index.md`

### Metadata Standards

Every document must have:

- `title`: Descriptive title
- `type`: Document type from standard list
- `date`: Creation date
- `summary`: 2-3 sentence description
- `tags`: Relevant keywords for discovery

### When Archiving Content

1. Move to `07-archive/YYYY-QQ/`
2. Update [07-archive/\_archive-log.md](../07-archive/_archive-log.md)
3. Update source document with `status: archived`
4. Update any linking documents
5. Remove from active indexes

### Cross-Referencing Rules

- Use relative paths: `../../folder/document.md`
- Always bi-directional: if A links to B, B should link to A
- Link to specific sections with anchors when relevant
- Keep "Related Documents" section updated

## Context Priority for LLMs

When answering questions, prioritize information in this order:

1. Current status and active work (`03-active-work/`)
2. Recent decisions (`02-decisions/`) - most recent first
3. Foundation documents (`01-foundation/`)
4. Knowledge base (`04-knowledge-base/`)
5. Research (`05-research/`)
6. Meeting notes (`06-meetings/`) - for specific details

## Red Flags to Watch For

- Documents without metadata
- Outdated status information (>1 week old)
- Broken internal links
- Decisions without ADR numbers
- Files in wrong locations
- Missing summaries in frontmatter
- Requirements without the 4-section structure
- Requirements with assumptions instead of stated facts

## Helpful Commands

- Find all documents of a type: `grep -r "type: decision-record" --include="*.md"`
- Find documents by tag: `grep -r "tags:.*architecture" --include="*.md"`
- Find recent updates: `find . -name "*.md" -mtime -7`
- Check for broken links: Use VS Code's markdown link checker or similar tools
- Process new documents: `/maintenance-daily`
- Validate quality: `/maintenance-weekly`
- Get cleanup recommendations: `/maintenance-monthly`

## Regular Maintenance Tasks

### Automated via Slash Commands

- **Daily**: Run `/maintenance-daily` to process new documents
- **Weekly**: Run `/maintenance-weekly` to validate quality
- **Monthly**: Run `/maintenance-monthly` for cleanup recommendations

### Manual Updates (Still Required)

- Weekly: Update [03-active-work/\_current-status.md](../03-active-work/_current-status.md)
- Monthly: Review decision statuses
- Quarterly: Execute archival actions from cleanup reports

See [maintenance-guide.md](./maintenance-guide.md) for complete maintenance workflow.

## Knowledge Base Structure and Workflows

### Knowledge Base Organization

The knowledge base (`04-knowledge-base/`) is organized into three domains:

```
04-knowledge-base/
├── technical/              # System architecture, APIs, infrastructure
├── business/              # Requirements, user research, market analysis
└── operational/           # Processes and runbooks
```

### When to Use Each Domain

**Technical** (`04-knowledge-base/technical/`)

- Architecture documents, API specs, infrastructure guides
- Subcategories: `architecture/`, `apis-and-integrations/`, `infrastructure/`

**Business** (`04-knowledge-base/business/`)

- **requirements/** - Product requirements (follow mandatory structure below)
- **user-research/** - User feedback and research
- **market-analysis/** - Competitive and market data

**Operational** (`04-knowledge-base/operational/`)

- **processes/** - Development workflows
- **runbooks/** - Troubleshooting and deployment guides

### Product Requirements Structure

**CRITICAL:** All requirements in `04-knowledge-base/business/requirements/` MUST follow this exact structure.

**IMPORTANT:** Only include information explicitly stated in the source document or existing in the project repository. Do NOT add assumptions, inferences, or placeholder content.

```markdown
---
title: [Feature Name]
type: requirement
date: YYYY-MM-DD
last-updated: YYYY-MM-DD
status: [draft | active | in-development | completed]
owner: [Product Owner if stated]
stakeholders: [Only list if explicitly mentioned]
tags: [relevant, keywords, from, document]
summary: |
  Brief overview based only on what's stated in the document.
related-docs:
  - [Only link if document explicitly references other docs]
---

# [Feature Name]

## Executive Summary

**Why:** [Why this feature exists - only if stated in document]

**How:** [How it works - only what's explicitly described]

**Expected Results:** [Expected outcomes - only if stated in document]

[If any of these sections are not in the source document, write "Not specified in source document"]

## Technical Considerations

[List ONLY technical details explicitly stated in the document:]

- [Item 1 from document]
- [Item 2 from document]

[If none stated, write: "No technical considerations specified in source document"]

## Acceptance Criteria

[List ONLY criteria explicitly stated in the document:]

- [ ] [Criterion 1 as stated]
- [ ] [Criterion 2 as stated]
- [ ] [Criterion 3 as stated]

[If none stated, write: "No acceptance criteria specified in source document"]

## Permissions

[List ONLY permissions explicitly mentioned in the document:]

- **[Role]**: [Permission as stated]

[If none stated, write: "No permissions specified in source document"]

## Related Information

[Only include links explicitly mentioned in source document]
```

### Rules for Requirements Processing

**DO:**

- Extract exactly what's written in the source document
- Use the exact wording when possible
- Mark sections as "Not specified" if information is missing
- Link only to documents explicitly referenced

**DO NOT:**

- Add assumptions or inferences
- Fill in blanks with "typical" information
- Add placeholder text like "To be determined"
- Infer technical requirements not stated
- Assume permissions based on similar features
- Add acceptance criteria not in the document

## Parsing Unstructured Content

### Automated Processing with /maintenance-daily

The `/maintenance-daily` command automatically processes all files in `08-documents-to-parse/` folder.

**What it does:**

1. Detects document type (meetings, requirements, technical docs)
2. Searches for existing related documents before creating new ones
3. Creates or updates documents using proper templates
4. Validates quality and enforces structure rules
5. Updates all indexes
6. Deletes processed files or flags for review

**To use:**
Simply place files in `08-documents-to-parse/` and run `/maintenance-daily`

### Check for Documents to Parse

**IMPORTANT:** Always check the [08-documents-to-parse/](../08-documents-to-parse/) folder for new content that needs to be processed and structured.

When you find documents in this folder:

1. Run `/maintenance-daily` to process them automatically
2. Review the processing log in `logs/` directory
3. Check `08-documents-to-parse/review-needed/` for flagged files
4. Address any files that need manual review

### Document Analysis Decision Tree

For each unstructured document, the system determines its type(s):

**Meeting Record** → Create in `06-meetings/YYYY-MM/`

- **Auto-detected by filename:** Contains "sync", "meeting", or "meet"
- **Auto-detected by content:** Contains 2+ timestamps in parentheses like `(14:30)` or `Name (9:15):`
- Look for: Date, attendees, discussion topics, action items
- Extract decisions to separate ADRs
- Update meeting index
- **CRITICAL:** If document contains timestamps in parentheses, it is a meeting transcript regardless of filename

**Decision** → Create in `02-decisions/`

- Look for: "We decided", "we chose", "we agreed"
- Assign next ADR number
- Document context, alternatives, rationale
- Update decisions index

**Research/Investigation** → Create in `05-research/`

- Look for: Research question, methodology, findings
- Include raw data references
- Update research index

**Requirements** → Create in `04-knowledge-base/business/requirements/`

- Look for: Feature descriptions, user stories, specifications
- **MUST use the 4-section structure:** Executive Summary, Technical Considerations, Acceptance Criteria, Permissions
- **Extract only what's explicitly stated** - no assumptions
- Update business index

**Technical Documentation** → Create in `04-knowledge-base/technical/`

- Look for: Architecture, APIs, infrastructure details
- **Subcategory signals:**
  - "system design", "components", "patterns", "data model" → `architecture/`
  - "endpoint", "integration", "webhook", "API" → `apis-and-integrations/`
  - "deployment", "environment", "monitoring", "security" → `infrastructure/`
- Add new terms to glossary
- Update technical index

**Process Documentation** → Create in `04-knowledge-base/operational/processes/`

- Look for: Workflows, procedures, standards, best practices
- Signals: "workflow", "procedure", "standard", "how we"
- Update operational index

**Runbooks** → Create in `04-knowledge-base/operational/runbooks/`

- Look for: Troubleshooting guides, deployment procedures
- Signals: "troubleshooting", "incident response", "if X then Y"
- Update operational index

**Status Update** → Update `03-active-work/_current-status.md`

- Look for: Progress reports, metrics, blockers
- Update priorities and risks as needed
- Note significant changes in project index

### Automated Parsing Workflow

When `/maintenance-daily` runs, it follows this workflow for each document:

#### Step 1: Extract Key Information

- **Dates:** Convert all dates to YYYY-MM-DD format
- **People:** Identify participants, owners, stakeholders
- **Decisions:** Any conclusions or choices made
- **Action Items:** Tasks with owners and due dates
- **Technical Terms:** New terminology to add to glossary
- **Blockers:** Impediments or risks identified

#### Step 2: Check for Existing Related Documents

**CRITICAL: The system ALWAYS searches for existing documents before creating new ones.**

**Search Process:**

1. Extract key topics/features from the content
2. Search existing documents in relevant category by:
   - Similar titles
   - Matching tags
   - Content similarity
3. Make decision based on findings

**Decision Logic:**

- **If similar document exists (high confidence):**
  - UPDATE existing document
  - Preserve original metadata (date, owner)
  - Update `last-updated` field to today
  - Add entry to "Revision History" section
  - Merge new information coherently
  - Note source of new information
- **If similar document might exist (moderate confidence):**

  - FLAG for human review
  - Move to `08-documents-to-parse/review-needed/`
  - Create comparison report
  - Wait for human decision

- **If no similar document found:**
  - CREATE new document
  - Use appropriate template
  - Generate complete metadata
  - Follow all structure rules

**For Requirements Updates:**

- Maintain 4-section structure
- Only add information if explicitly stated in new source
- Mark any new sections as "Not specified" if appropriate
- Preserve existing "Not specified" markers unless new info available

#### Step 3: Create or Update Structured Documents

For each piece of content identified:

1. **Use appropriate template** from the relevant directory
2. **Generate complete metadata:**

   ```yaml
   ---
   title: [Specific, descriptive title]
   type: [Standard type from our list]
   date: [Content creation date - preserve if updating]
   last-updated: [Today's date if creating or updating]
   status: active
   owner: [Primary responsible person - preserve if updating]
   stakeholders: [All involved parties]
   tags: [relevant, keywords, for, search]
   summary: |
     Clear 2-3 sentence summary explaining what this document
     contains and why it matters for context and discovery.
   related-docs:
     - [../path/to/related.md]
   ---
   ```

3. **Structure the content** with clear headings and sections
4. **Follow naming conventions:** `YYYY-MM-DD-descriptive-title.md`
5. **Assign ADR numbers** for decisions (check index for next number)
6. **For requirements: Use 4-section structure with only stated information**

#### Step 4: Handle Multi-Type Documents

If a document contains multiple types of information (common with meetings):

1. Create primary document (e.g., meeting note)
2. Extract significant decisions into separate ADRs
3. Extract action items and update relevant docs
4. Add new terms to glossary
5. Cross-link all created documents

#### Step 5: Update All Indexes

**Always update relevant indexes:**

- `02-decisions/_decisions-index.md` - Add new decisions
- `06-meetings/_meetings-index.md` - Add new meetings
- `05-research/_research-index.md` - Add new research
- `04-knowledge-base/technical/_index.md` - Add new technical docs
- `04-knowledge-base/business/_index.md` - Add new business docs
- `04-knowledge-base/operational/_index.md` - Add new operational docs
- `01-foundation/glossary.md` - Add new terms
- `00-PROJECT-INDEX.md` - Update if significant

#### Step 6: Quality Validation

Before finishing, verify:

- [ ] All dates in ISO format (YYYY-MM-DD)
- [ ] Complete metadata with summary
- [ ] Related documents cross-linked
- [ ] Indexes updated
- [ ] File naming follows conventions
- [ ] ADR numbers assigned and unique
- [ ] Action items have owners and dates
- [ ] New terms added to glossary
- [ ] No broken internal links
- [ ] **For requirements: 4-section structure used with only explicitly stated information**
- [ ] **For requirements: No assumptions or inferences added**
- [ ] **If updated: Original date preserved, last-updated field current**
- [ ] **If updated: Revision history entry added**

#### Step 7: Clean Up

**After successful processing:**

- Delete the original file from `08-documents-to-parse/`
- Confirm all content has been properly structured
- Verify no information was lost
- Files problematic documents in `08-documents-to-parse/review-needed/` with explanation

### Content Extraction Patterns

**Meetings:**

- Opening usually has: date, time, attendees, agenda
- Look for: "discussed", "reviewed", "decided"
- Action items often marked: "TODO", "action item", "follow up"
- Blockers indicated by: "blocked by", "waiting on", "can't proceed"

**Decisions:**

- Indicated by: "we decided to...", "after discussion we agreed...", "going forward we will..."
- Should have context explaining why
- May mention alternatives considered
- Often includes implications or next steps

**Technical Content:**

- Contains: system names, technical terms, code examples
- Describes: architecture, APIs, configurations
- May include: diagrams, specifications, procedures
- Often has: dependencies, constraints, requirements
- **Architecture signals**: "system design", "components", "patterns", "data model"
- **API signals**: "endpoint", "integration", "webhook", "third-party service"
- **Infrastructure signals**: "deployment", "environment", "monitoring", "security"

**Business Content:**

- **Requirements signals**: "feature", "user story", "acceptance criteria", "product spec"
  - **MUST follow 4-section structure** when creating requirement docs
  - **Only extract explicitly stated information** - no assumptions or inferences
- **Research signals**: "user interview", "persona", "usability test", "user feedback"
- **Market signals**: "competitive analysis", "market size", "industry trends"

**Operational Content:**

- **Process signals**: "workflow", "procedure", "standard", "best practice", "how we"
- **Runbook signals**: "troubleshooting", "incident response", "deployment steps", "if X then Y"

**Research:**

- States: research question or hypothesis
- Describes: methodology and data sources
- Presents: findings with evidence
- Concludes: recommendations or next steps

### Handling Ambiguity

**If date is unclear:**

- Use best estimate based on context
- Add note: "Date estimated based on context"
- Check surrounding documents for clues

**If owner is unclear:**

- Use participants mentioned in content
- Mark as "TBD" if truly unknown
- Check previous related documents

**If document type is unclear:**

- Choose primary purpose
- Create multiple documents if needed
- Use tags to capture secondary topics
- If still unclear, flag for review

**If knowledge base subcategory is unclear:**

- Default to best fit based on primary content
- Use cross-references to link to other relevant areas
- Check similar existing documents for guidance

**If categorization is unclear:**

- Default to best fit based on content
- Use cross-references liberally
- When in doubt, flag for human review

**If similar document might exist:**

- Don't guess - flag for review
- Provide comparison information
- Let human decide update vs. create

### Reporting After Parsing

After processing documents, `/maintenance-daily` provides:

1. **Summary of created documents:**

   ```
   Created:
   - [path/to/doc1.md] - Brief description
   - [path/to/doc2.md] - Brief description

   Updated:
   - [path/to/existing-doc.md] - Added information from [source]

   Updated Indexes:
   - [path/to/index.md]
   ```

2. **Any questions or ambiguities:**

   ```
   Questions:
   - [Specific question needing clarification]
   ```

3. **Deleted files:**

   ```
   Processed and removed:
   - 08-documents-to-parse/original-file.md
   ```

4. **Flagged for review:**
   ```
   Moved to review-needed/:
   - unclear-document.md - Reason: [explanation]
   ```

## Meeting Transcript Parser

### Meeting Transcript File Identification

Meeting transcripts can be provided in multiple formats:

#### Supported File Formats

- **Word Documents**: `.docx` files
- **Markdown Files**: `.md` files
- **Plain Text**: `.txt` files

#### File Naming Patterns

Automatically identified by these naming patterns (case-insensitive):

- Contains the word **"sync"**: `weekly-sync.docx`, `team-sync-notes.md`, `sync-2024-10-20.docx`
- Contains the word **"meeting"**: `project-meeting.docx`, `meeting-notes.md`, `stakeholder-meeting.md`
- Contains the word **"meet"**: `meet-notes.docx`, `team-meet.md`, `client-meet-summary.md`

**Examples of auto-detected filenames:**

- ✅ `2024-10-15-sprint-sync.docx`
- ✅ `weekly-team-meeting.md`
- ✅ `client-meet-notes-oct.docx`
- ✅ `standup-sync.md`
- ✅ `architecture-meeting-transcript.docx`

#### Content-Based Detection

**CRITICAL: Even if filename doesn't match patterns above, the system checks document content for meeting transcript indicators.**

Automatically identifies documents as meeting transcripts if content contains **timestamps in parentheses**:

**Timestamp patterns detected:**

- `(HH:MM)` - e.g., `(14:30)`, `(9:15)`
- `(HH:MM:SS)` - e.g., `(14:30:45)`, `(9:15:03)`
- `(MM:SS)` - e.g., `(05:30)`, `(0:45)`
- Timestamps with names/speakers: `John Doe (14:30):`, `Sarah (9:15 AM):`

**Examples of content that triggers transcript detection:**

```
John (14:30): Let's start with the project update.
Sarah (14:31): The backend is ready for testing.

Speaker 1 (00:00): Welcome everyone to today's sync.
Speaker 2 (00:45): Thanks for having me.

(14:25) Discussion about database migration
(14:30) Decision to proceed with PostgreSQL

Alice (2:15 PM): I think we should consider the API approach.
Bob (2:17 PM): I agree, let me outline the benefits.
```

**Detection workflow:**

1. Reads first 500-1000 characters of document content
2. Searches for timestamp patterns in parentheses
3. If 2+ timestamps found → Identifies as meeting transcript
4. Executes full meeting transcript processing workflow
5. Works even if filename doesn't contain "sync", "meeting", or "meet"

**Why this matters:**

- Recording software often auto-generates transcripts with timestamps
- Exported chat logs contain timestamps
- Many transcript formats use timestamps regardless of filename
- Catches transcripts that would otherwise be missed

### Automated Meeting Processing

When `/maintenance-daily` processes meeting transcripts:

#### Step 1: File Reading

```javascript
// For .docx files, use mammoth to extract text
import * as mammoth from "mammoth";
const arrayBuffer = await window.fs.readFile("filename.docx");
const result = await mammoth.extractRawText({ arrayBuffer });
const transcriptText = result.value;

// For .md files, read directly
const transcriptText = await window.fs.readFile("filename.md", {
  encoding: "utf8",
});
```

#### Step 2: Language Detection and Translation

**CRITICAL: All transcripts must be translated to English before processing.**

Before parsing any transcript:

1. **Detect the language** of the transcript content
2. **If not in English**, translate the entire transcript to English first
3. **Only after translation**, proceed with parsing and structuring

**Translation Note in Document:**

If a transcript was translated, note this in the meeting note frontmatter:

```yaml
original-language: [Spanish/Portuguese/French/etc.]
translated: true
translation-date: YYYY-MM-DD
```

And add a note at the top of the document:

```markdown
> **Note:** This meeting was conducted in [Original Language] and has been translated to English for documentation purposes.
```

**Language Translation Guidelines:**

When translating:

- Preserve names, proper nouns, and technical terms
- Maintain professional tone in English
- Keep acronyms in original form if they're standard (API, UI, etc.)
- Translate domain-specific terms but add original in parentheses if needed for clarity
- Example: "We discussed the 'planejamento' (planning) phase" → "We discussed the planning phase"

**Common languages to watch for:**

- Spanish
- Portuguese
- French
- German
- Italian
- Chinese
- Japanese
- And any others

**If language detection is uncertain:**

- Process as English by default
- Note in output that language was ambiguous
- Ask user for confirmation if critical

#### Step 3: Parse and Process

After translation (if needed), follow the standard parsing workflow.

### Primary Task: Transform Meeting Transcripts into Structured Documentation

When processing a meeting transcript, the system creates professionally structured documentation that makes the information easily discoverable and actionable.

### Voice and Tone

- **Professional and clear** throughout all documentation
- Objective and factual - avoid editorial commentary
- Concise but comprehensive - capture all important information
- Action-oriented - emphasize decisions and next steps

### Core Processing Workflow for Meetings

#### Step 1: Initial Analysis

When receiving a meeting transcript, first extract:

- **Meeting metadata**: Date, time, attendees, meeting type
- **Main topics discussed**: What were the primary subjects?
- **Decisions made**: Any conclusive choices or agreements?
- **Action items**: Tasks assigned with owners
- **Blockers or risks**: Issues raised that need resolution
- **New terminology**: Domain-specific terms that should be in glossary

#### Step 2: Create Primary Meeting Note

Create the meeting note in: `06-meetings/YYYY-MM/YYYY-MM-DD-meeting-name.md`

Use this structure:

```markdown
---
title: [Meeting Name]
type: meeting-note
date: YYYY-MM-DD
attendees: [Person 1, Person 2, Person 3]
meeting-type:
  [
    standup | planning | retrospective | review | stakeholder | technical | ad-hoc,
  ]
tags: [relevant, keywords]
original-language: [Language if translated, omit if English]
translated: [true/false, omit if not translated]
translation-date: [YYYY-MM-DD, omit if not translated]
summary: |
  Professional, clear summary of meeting outcomes and key decisions made.
related-docs:
  - [Links to created decision records]
  - [Links to related documentation]
---

# [Meeting Name]

> **Note:** [Only include if translated] This meeting was conducted in [Original Language] and has been translated to English for documentation purposes.

**Date:** YYYY-MM-DD  
**Time:** HH:MM - HH:MM (or duration if known)  
**Attendees:** [List all participants]  
**Facilitator:** [Name if identifiable]

## Executive Summary

[2-4 paragraph overview of everything discussed throughout the meeting. This should be a professional, clear narrative that captures:

- The purpose of the meeting
- Major topics covered
- Key decisions or consensus achieved
- Overall outcomes and next steps]

## Action Items

[Actionable items to be pursued after the meeting and agreed upon]

- [ ] **[Specific task description]** - Assigned to: [Name] - Due: YYYY-MM-DD - Priority: [High/Medium/Low]
- [ ] **[Specific task description]** - Assigned to: [Name] - Due: YYYY-MM-DD - Priority: [High/Medium/Low]
- [ ] **[Specific task description]** - Assigned to: [Name] - Due: YYYY-MM-DD - Priority: [High/Medium/Low]

## Index

[List of topics covered in the meeting - serves as a table of contents]

1. [Topic 1]
2. [Topic 2]
3. [Topic 3]
4. [Topic 4]

---

## Topics: Breakdown

### Topic 1: [Topic Name]

#### Executive Summary

[Professional, clear overview of this specific topic. 2-3 sentences capturing what was discussed and what was concluded.]

#### Key Takeaways

- [Important point or insight from this discussion]
- [Important point or insight from this discussion]
- [Important point or insight from this discussion]
- [Decisions made related to this topic]
- [Action items specific to this topic]

#### Discussion Details

[Optional: More detailed notes if the topic was complex. Include:

- Questions raised
- Alternatives considered
- Concerns voiced
- Context that led to the discussion]

---

### Topic 2: [Topic Name]

#### Executive Summary

[Professional, clear overview of this specific topic.]

#### Key Takeaways

- [Important point or insight]
- [Important point or insight]
- [Important point or insight]

#### Discussion Details

[Optional: Additional context if needed]

---

[Continue for all topics discussed]

---

## Decisions Made

[If any formal decisions were reached, list them here. Each decision should link to a separate ADR if it's significant.]

1. **[Decision]** - [Brief rationale] - [Link to ADR-XXX if created]
2. **[Decision]** - [Brief rationale] - [Link to ADR-XXX if created]

## Blockers and Risks Identified

[Any issues that were raised that could impede progress]

- **[Blocker/Risk]** - Impact: [High/Medium/Low] - Owner: [Name] - Needs resolution by: [Date]

## Parking Lot

[Topics that were raised but deferred for later discussion]

- [Topic to revisit]
- [Topic to revisit]

## Next Steps

[High-level summary of what happens next]

- Next meeting scheduled for: YYYY-MM-DD
- Follow-up actions required before next meeting
- Decisions pending for next session

## References

- [Links to relevant documents discussed]
- [Links to shared materials]
- [Recording link if available]
```

#### Step 3: Extract Significant Decisions into ADRs

**Decision Identification Criteria:**

A decision is significant enough for an ADR if it:

- Has long-term architectural or strategic implications
- Affects multiple systems or teams
- Involves choosing between meaningful alternatives
- Has notable tradeoffs or consequences
- Sets a precedent for future decisions
- Commits significant resources or changes direction

**For each significant decision, create:** `02-decisions/YYYY-MM-DD-decision-title.md`

Use the template in [02-decisions/\_template-decision.md](../02-decisions/_template-decision.md)

**Significant decisions get ADRs. Minor decisions stay in meeting notes.**

#### Step 4: Update Active Work Documents

**Update Current Status:** `03-active-work/_current-status.md`

If the meeting included status updates, refresh the current status document:

- Update "What Changed This Period" section
- Refresh current focus areas
- Update metrics if discussed
- Add new blockers
- Update decisions needed

**Update Priorities:** `03-active-work/priorities.md`

If priorities were discussed or changed:

- Reorder priority list
- Add context for why priorities shifted
- Link to meeting where priority change was discussed

**Update Blockers:** `03-active-work/blockers-and-risks.md`

If new blockers or risks were identified:

```markdown
### [Blocker/Risk Name]

- **Identified:** YYYY-MM-DD in [Meeting Name](../meetings/YYYY-MM/YYYY-MM-DD-meeting-name.md)
- **Impact:** [High/Medium/Low]
- **Affects:** [What's blocked]
- **Owner:** [Person responsible for resolution]
- **Target Resolution:** YYYY-MM-DD
- **Status:** [Active/Mitigating/Resolved]
- **Mitigation Plan:** [Steps being taken]
```

#### Step 5: Update Glossary (If Needed)

If new terminology was introduced or defined in the meeting:

Update: `01-foundation/glossary.md`

```markdown
**[Term]**: [Clear, professional definition based on how it was used in context. Include which meeting/document first introduced it.]
_Source: [Meeting Name](../meetings/YYYY-MM/YYYY-MM-DD-meeting-name.md)_
```

#### Step 6: Update All Indexes

**Update Meetings Index:** `06-meetings/_meetings-index.md`

Add entry in reverse chronological order:

```markdown
| YYYY-MM-DD | [Meeting Name](./YYYY-MM/YYYY-MM-DD-meeting-name.md) | [Key topics: Topic 1, Topic 2, Topic 3] | [Attendees] | [# decisions] | [# action items] |
```

**Update Decisions Index:** `02-decisions/_decisions-index.md`

For each ADR created:

```markdown
| ADR-XXX | YYYY-MM-DD | [Decision Title](./YYYY-MM-DD-decision-title.md) | accepted | [Brief description] | [Meeting source](../meetings/YYYY-MM/YYYY-MM-DD-meeting-name.md) |
```

**Update Master Index:** `00-PROJECT-INDEX.md`

If significant, add to "Recent Activity" section:

```markdown
### This Week

- [YYYY-MM-DD: Meeting Name](06-meetings/YYYY-MM/YYYY-MM-DD-meeting-name.md) - Key decisions on [topic]
```

#### Step 7: Create Cross-References

Ensure bidirectional linking:

- Meeting note links to all ADRs created from it
- Each ADR links back to source meeting
- Related documents are cross-referenced in frontmatter
- Action items reference relevant knowledge base docs if applicable

### Parsing Guidelines for Meeting Transcripts

#### Recognizing Meeting Metadata

**Date/Time:**

- Look for timestamps, date mentions, "today is", scheduling context
- If not explicit, use filename or context clues
- Format as YYYY-MM-DD HH:MM

**Attendees:**

- Names mentioned in introductions
- People who spoke during the meeting
- Sign-offs or attendance lists
- Format as: First Last, First Last, First Last

**Meeting Type:**

- Sprint planning, retrospective, standup = clear identifiers
- Technical deep-dive = technical meeting
- Stakeholder update = stakeholder meeting
- Unstructured discussion = ad-hoc meeting

#### Identifying Topics

Topics are typically indicated by:

- Clear topic transitions: "Next topic", "Moving on to", "Let's discuss"
- New subject matter being introduced
- Questions that start new discussions
- Agenda items being checked off

**How to name topics:**

- Use clear, descriptive titles (not just "Discussion")
- Professional language: "Database Selection Strategy" not "DB stuff"
- Be specific: "Q4 Revenue Projections" not "Revenue"

#### Extracting Action Items

**Action item indicators:**

- "I'll/I will [do something]"
- "[Person] can you [do something]"
- "Let's make sure to [do something]"
- "We need to [do something]"
- "Action item:", "TODO:", "Next step:"
- "Follow up on [something]"

**Action item format:**

```markdown
- [ ] **[Clear, specific task]** - Assigned to: [Name] - Due: [Date] - Priority: [High/Medium/Low]
```

**If information is missing:**

- No owner mentioned? → "Assigned to: Team/TBD"
- No due date? → "Due: TBD" or estimate based on context
- No priority? → Default to "Medium" or infer from urgency in discussion

#### Identifying Decisions

**Decision indicators:**

- "We've decided to..."
- "Let's go with [option]"
- "We're choosing X over Y"
- "Agreed upon approach..."
- "The decision is..."
- Consensus reached after discussion
- Vote taken and outcome

**For each decision:**

1. What was decided? (The outcome)
2. Why? (The rationale)
3. What else was considered? (Alternatives)
4. Who decided? (Decision makers)
5. Is this significant? (Create ADR if yes)

#### Recognizing Blockers and Risks

**Blocker/risk indicators:**

- "We're blocked by..."
- "We can't proceed until..."
- "Waiting on..."
- "Risk that..."
- "Potential issue..."
- "Concern about..."
- "Dependency on..."

**Capture:**

- What's blocked or at risk
- Impact level (infer from urgency and scope)
- Who's responsible for resolution
- When it needs to be resolved

#### Extracting Key Takeaways

Key takeaways are:

- Important insights or learnings
- Consensus points
- Critical information shared
- "Aha moments"
- Conclusions reached
- Important facts or data mentioned
- Commitments made

**Format as bullet points:**

- Start with the core insight
- Include context if needed for clarity
- Link to decisions or action items when relevant

### Quality Assurance

#### Automated Validation with /maintenance-weekly

Run `/maintenance-weekly` to check:

- Documents created in last 7 days
- Metadata completeness
- Requirements structure compliance
- Duplicate content
- Broken links
- Orphaned documents

**Auto-fixes simple issues:**

- Date format corrections
- Missing tags
- Trailing whitespace

**Reports for human review:**

- Content issues
- Structural problems
- Complex duplicates
- Missing metadata fields
- Requirements violations

#### Manual Quality Checks

**Before finalizing any document, verify:**

**Meeting Note Quality:**

- [ ] Executive summary clearly captures meeting purpose and outcomes
- [ ] All action items have owners (or marked TBD)
- [ ] Action items are specific and actionable
- [ ] Topics are clearly titled and cover all discussions
- [ ] Each topic has executive summary and key takeaways
- [ ] Professional, clear tone throughout
- [ ] Dates are in ISO format (YYYY-MM-DD)
- [ ] All attendees are listed
- [ ] Cross-references to related docs are included
- [ ] Translation noted in metadata if applicable

**Decision Records Quality:**

- [ ] ADR only created for significant decisions
- [ ] Decision statement is clear and definitive
- [ ] Context explains why decision was needed
- [ ] Rationale includes key factors
- [ ] Alternatives are documented with pros/cons
- [ ] Consequences (positive/negative) are identified
- [ ] Implementation guidance is included
- [ ] Links back to source meeting
- [ ] Assigned unique ADR number

**Requirements Quality:**

- [ ] Uses 4-section structure
- [ ] Contains ONLY explicitly stated information
- [ ] No assumptions or inferences added
- [ ] "Not specified" used appropriately for missing sections
- [ ] Executive Summary has Why, How, Expected Results

**Index Updates:**

- [ ] Meeting added to meetings index
- [ ] All ADRs added to decisions index
- [ ] Significant content noted in master index
- [ ] Cross-references are bidirectional

**Active Work Updates:**

- [ ] Current status updated if status discussed
- [ ] New blockers added to blockers document
- [ ] Priorities updated if they changed
- [ ] Action items flow to appropriate tracking

**Metadata Quality:**

- [ ] All frontmatter fields complete
- [ ] Tags are relevant and consistent
- [ ] Summary is clear and informative
- [ ] Related docs are cross-linked
- [ ] File naming follows conventions

### Handling Edge Cases

#### Informal or Unstructured Transcripts

- Extract structure even if the conversation was informal
- Group related discussions into coherent topics
- Use context clues to identify decisions and actions
- Professional summary even if the conversation was casual

#### Missing Information

- **No date:** Use "Date: Unknown (estimated YYYY-MM-DD based on context)"
- **No attendees:** Use "Attendees: [Names from transcript]" or "Attendees: Not recorded"
- **No clear agenda:** Create topics based on what was discussed
- **Unclear decisions:** Note in meeting notes but don't create ADR

#### Very Short Meetings

- Still use full structure
- Sections may be brief but should all be present
- Even short meetings can have significant decisions
- Don't skip quality just because content is limited

#### Very Long Meetings

- Break into clear topic sections
- Use sub-topics if needed
- Extract multiple ADRs if multiple decisions
- Executive summary becomes more critical for scannability

#### Technical Jargon

- Add terms to glossary
- Provide context in meeting notes
- Don't assume reader knows acronyms
- Link to technical documentation when relevant

#### Conflicting Information

- Note disagreements in meeting notes
- If decision was contested, capture dissenting views
- Professional, neutral tone when documenting conflict
- If no consensus, note that decision is pending

### Manual Review Points

**After /maintenance-daily:**

- Check `logs/daily-parse-*.log` for processing report
- Review `08-documents-to-parse/review-needed/` for flagged files
- Verify created/updated documents are accurate
- Confirm indexes were updated correctly

**After /maintenance-weekly:**

- Review `logs/validation-report-*.md`
- Address critical issues immediately
- Plan fixes for important issues
- Track minor issues for later

**After /maintenance-monthly:**

- Review `logs/cleanup-report-*.md`
- Execute recommended archival actions
- Consolidate identified duplicates
- Fix broken links
- Update document categorization

## Automatic File Processing Mode

When files are uploaded or placed in `08-documents-to-parse/`:

**Automatic workflow when `/maintenance-daily` runs:**

1. **Detect if meeting transcript:**

   - Check filename for "sync", "meeting", or "meet"
   - **Read file content and search for timestamps in parentheses**
   - If 2+ timestamps found like `(14:30)` or `Name (9:15):` → It's a transcript

2. **If meeting transcript identified:**

   - Detect file type (.docx, .md, or .txt)
   - Read content appropriately
   - Detect language
   - Translate to English if needed
   - Parse using meeting transcript structure
   - Create all structured documents
   - Update indexes

3. **If not a meeting transcript:**

   - Analyze content type (technical doc, requirement, research, etc.)
   - Search for existing related documents
   - Update existing or create new based on findings
   - Process according to document type
   - Create structured documents
   - Update indexes

4. **Report results:**
   - Files processed count
   - Created vs updated
   - Decisions extracted
   - Action items identified
   - Files flagged for review

**CRITICAL: Always check content for timestamps, not just filename!**

### Batch Processing Output

Example output when processing multiple files:

```
📁 Processing Documents...

File: project-notes.docx
├── Detection: Timestamps found → Identified as meeting transcript
├── Language: English (no translation needed)
├── Action: Updated existing document (06-meetings/2024-10/2024-10-15-project-notes.md)
├── Reason: Similar meeting note from same date already existed
├── Added: 2 new action items, 1 decision
├── Extracted: 1 decision (ADR-045)
└── Status: ✅ Complete

File: 2024-10-15-sprint-sync.docx
├── Detection: Filename contains "sync" → Meeting transcript
├── Language: Spanish → Translated to English
├── Action: Created new document
├── Created: 06-meetings/2024-10/2024-10-15-sprint-sync.md
├── Extracted: 2 decisions (ADR-046, ADR-047)
├── Action Items: 5
└── Status: ✅ Complete

File: feature-request.md
├── Detection: Contains requirements → Product requirement
├── Action: Created new document
├── Created: 04-knowledge-base/business/requirements/user-notifications.md
├── Structure: 4-section format (Executive Summary, Technical Considerations, Acceptance Criteria, Permissions)
├── Extracted: Only explicitly stated information
└── Status: ✅ Complete

File: technical-spec.md
├── Detection: No timestamps, no meeting keywords → Technical document
├── Action: Created new document
├── Created: 04-knowledge-base/technical/architecture/api-design.md
├── Updated: technical index, glossary
└── Status: ✅ Complete

File: unclear-notes.txt
├── Detection: Ambiguous content type
├── Action: Flagged for review
├── Moved to: 08-documents-to-parse/review-needed/unclear-notes.txt
├── Reason: Could not determine if meeting or general notes
└── Status: ⚠️ Needs Review

Summary:
✅ Processed 5 documents
✅ Updated 1 existing document
✅ Created 4 new documents
✅ Extracted 3 decision records
✅ Total action items: 7
📝 1 translation performed (Spanish)
🎯 Timestamp detection found 1 transcript that would have been missed by filename alone
✅ Requirement doc used mandatory 4-section structure with only stated information
⚠️ 1 file needs manual review
```

### Output After Processing

After processing documents, `/maintenance-daily` provides:

#### 1. Summary of Created/Updated Documents

```
✅ Created Documents:

Meeting Note:
- 06-meetings/YYYY-MM/YYYY-MM-DD-meeting-name.md
  Topics: [list], Action Items: [count], Decisions: [count]
  [Language: Translated from [Original Language] if applicable]

Decision Records:
- 02-decisions/YYYY-MM-DD-decision-title.md (ADR-XXX)
- 02-decisions/YYYY-MM-DD-another-decision.md (ADR-XXX)

Updated Documents:
- 06-meetings/YYYY-MM/YYYY-MM-DD-existing-meeting.md
  Added: 3 action items, 1 decision
  Reason: New information from follow-up transcript

- 03-active-work/_current-status.md
- 03-active-work/blockers-and-risks.md
- 01-foundation/glossary.md (added X terms)

Updated Indexes:
- 06-meetings/_meetings-index.md
- 02-decisions/_decisions-index.md
- 00-PROJECT-INDEX.md
```

#### 2. Action Items Summary

```
📋 Action Items Extracted: [count]

High Priority:
- [Task] - Owner: [Name] - Due: [Date]

Medium Priority:
- [Task] - Owner: [Name] - Due: [Date]

Missing Information:
- [Any action items missing owner or due date]
```

#### 3. Questions or Clarifications Needed

```
❓ Questions:

- [Any ambiguities in the transcript]
- [Information that seems incomplete]
- [Dates or names that couldn't be determined]
- [Language detection uncertainties]
- [Unclear if should update existing or create new]
```

#### 4. Files Flagged for Review

```
⚠️ Files Moved to review-needed/:

- unclear-document.md
  Reason: Could not determine document type with confidence
  Next steps: Review content and clarify type

- potential-duplicate.md
  Reason: Similar to existing document but unclear if update or separate
  Next steps: Compare with [existing-doc.md] and decide
```

#### 5. Recommendations

```
💡 Recommendations:

- [Suggested follow-ups based on content]
- [Documents that should be created or updated]
- [Related knowledge base areas that might need updating]
- [Suggested consolidation opportunities]
```

## Need Help?

- Template examples in each category's `_template-*.md`
- Category-specific guides in `README.md` files
- Maintenance procedures in [maintenance-guide.md](./maintenance-guide.md)
- Processing logs in `logs/` directory
- Run `/maintenance-status` to view recent activity
- Check `08-documents-to-parse/review-needed/` for flagged files
