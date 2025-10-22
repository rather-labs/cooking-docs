---
title: Knowledge Base Maintenance Guide
type: operational-guide
date: 2025-10-17
last-updated: 2025-10-22
status: active
owner: Project Team
summary: |
  Comprehensive guide for maintaining the project knowledge database,
  including automated maintenance commands, regular tasks, best practices,
  troubleshooting, knowledge base management, and meeting transcript processing workflow.
---

# Knowledge Base Maintenance Guide

This guide explains how to keep the project knowledge database organized, up-to-date, and useful for both humans and LLMs.

## Automated Maintenance Commands

The knowledge base includes automated maintenance scripts that can be run via slash commands in Claude Code. These commands help you maintain quality, identify issues, and keep the documentation organized.

### Available Maintenance Commands

Run `/maintenance` to see all available commands:

- **`/maintenance-status`** - Quick Status: View recent logs
- **`/maintenance-daily`** - Daily Parse: Process new documents (~5 min)
- **`/maintenance-weekly`** - Weekly Validation: Check quality & duplicates (~15 min)
- **`/maintenance-monthly`** - Monthly Cleanup: Archive & consolidate (~30 min)
- **`/maintenance-full`** - Full Maintenance: Run all tasks (~50 min)

### Command Details

#### `/maintenance-daily` - Daily Parse

**Purpose:** Check for and report on files that need to be processed in the `08-documents-to-parse/` directory.

**What it does:**
- Scans `08-documents-to-parse/` for unprocessed files
- Reports the count of files found
- Lists files needing manual processing
- Checks the `review-needed/` subdirectory
- Creates a log file in `logs/`

**When to run:** Daily, or whenever you add new documents to parse

**Duration:** < 1 minute

**Output:** Log file at `logs/daily-parse-YYYY-MM-DD-HHMMSS.log`

#### `/maintenance-weekly` - Weekly Validation

**Purpose:** Comprehensive quality check of recent documents and overall structure.

**What it does:**
- Finds all markdown files modified in the last 7 days
- Checks for complete YAML frontmatter
- Validates required fields (title, type, date, summary, tags)
- Checks for ISO date format (YYYY-MM-DD)
- Generates a detailed validation report

**When to run:** Weekly (recommended: every Friday)

**Duration:** 2-5 minutes

**Output:**
- Validation report at `logs/validation-report-YYYY-MM-DD.md`
- Log file at `logs/weekly-validation-YYYY-MM-DD-HHMMSS.log`

**What to do after:** Review the validation report and fix any metadata issues identified

#### `/maintenance-monthly` - Monthly Cleanup

**Purpose:** Identify stale content, duplicates, and maintenance needs.

**What it does:**
- Finds meeting notes older than 6 months
- Identifies documents not updated in over a year
- Generates cleanup recommendations
- Provides action items for manual review

**When to run:** Monthly (recommended: first Monday of each month)

**Duration:** 1-3 minutes

**Output:**
- Cleanup report at `logs/cleanup-report-YYYY-MM-DD.md`
- Log file at `logs/monthly-cleanup-YYYY-MM-DD-HHMMSS.log`

**What to do after:** Review the report and manually execute recommended archival actions

**IMPORTANT:** This command only generates recommendations - it does NOT automatically delete or move any files.

#### `/maintenance-full` - Full Maintenance

**Purpose:** Run all maintenance tasks in sequence.

**What it does:**
- Runs daily parse
- Runs weekly validation
- Runs monthly cleanup
- Generates comprehensive reports

**When to run:** Monthly, or before major project milestones

**Duration:** 5-10 minutes

**Output:** Multiple log files and reports from each task

#### `/maintenance-status` - Quick Status

**Purpose:** View recent maintenance logs quickly.

**What it does:**
- Lists the 5 most recent log files
- Shows excerpt from latest daily parse log

**When to run:** Anytime you want to check recent maintenance activity

**Duration:** < 1 second

### How to Use Maintenance Commands

**In Claude Code:**
1. Type `/maintenance` to see all options
2. Type the specific command you want (e.g., `/maintenance-weekly`)
3. Claude Code will execute the script and show results
4. Review the output and any generated reports
5. Take action on issues identified

**From Command Line:**
```bash
# Run the maintenance menu (interactive)
./run-maintenance.sh

# Or run specific task directly (non-interactive)
./run-maintenance.sh 1  # Daily parse
./run-maintenance.sh 2  # Weekly validation
./run-maintenance.sh 3  # Monthly cleanup
./run-maintenance.sh 4  # Full maintenance
./run-maintenance.sh 5  # Quick status
```

### Maintenance Script Locations

All maintenance scripts are in the `scripts/` directory:
- `scripts/daily-parse.sh` - Daily document parsing check
- `scripts/weekly-validation.sh` - Weekly quality validation
- `scripts/monthly-cleanup.sh` - Monthly cleanup recommendations
- `run-maintenance.sh` - Main menu script that calls the others

### Log Files

All maintenance commands create log files in the `logs/` directory:
- `logs/daily-parse-*.log` - Daily parse execution logs
- `logs/weekly-validation-*.log` - Weekly validation execution logs
- `logs/validation-report-*.md` - Detailed validation reports
- `logs/monthly-cleanup-*.log` - Monthly cleanup execution logs
- `logs/cleanup-report-*.md` - Detailed cleanup recommendation reports

**Tip:** Check the `logs/` directory regularly to track maintenance history and identify recurring issues.

## Daily Maintenance

### As Work Happens

- **Document decisions immediately** - Don't wait; context is fresh now
- **Update blockers** - Add new blockers to [03-active-work/blockers-and-risks.md](../03-active-work/blockers-and-risks.md) as they arise
- **File meeting notes** - Create note from template within 24 hours of meeting
- **Process meeting transcripts** - Use the meeting transcript parser workflow (see below)
- **Update knowledge base** - Add technical docs, requirements, or runbooks as work is completed
- **Cross-reference** - When creating new docs, link to related existing docs

### Check for Documents to Parse

**IMPORTANT:** Check [08-documents-to-parse/](../08-documents-to-parse/) folder daily for new unstructured content.

**Process:**

1. Review any files in the folder
2. Parse and structure content using templates
3. Create appropriate documents in correct locations
4. Update all relevant indexes
5. **Delete** the original file after successful processing

**What goes in this folder:**

- Meeting transcripts (.docx, .md, .txt files)
- Email threads about project topics
- Slack conversation exports
- Raw research findings
- Requirements documents
- Technical documentation drafts
- Any unstructured project content

**Auto-detection for meeting transcripts:**
Files containing "sync", "meeting", or "meet" in the filename are automatically identified as meeting transcripts.

See [Claude Code Instructions](./instructions.md#parsing-unstructured-content) for detailed parsing workflow.

### Processing Meeting Transcripts

Meeting transcripts can be in multiple formats: .docx (Word), .md (Markdown), or .txt (plain text).

#### Quick Workflow

1. **Drop file** in `08-documents-to-parse/` (files with "sync", "meeting", or "meet" in name are auto-detected)
2. **Language translation** - If not in English, automatically translate to English
3. **Analyze** - Extract metadata, topics, decisions, action items, blockers, new terms
4. **Create Meeting Note** - Use structure from [06-meetings/\_template-meeting.md](../06-meetings/_template-meeting.md)
5. **Extract ADRs** - Create decision records for significant decisions
6. **Update Active Work** - Refresh current status, priorities, and blockers as needed
7. **Update Glossary** - Add new terminology to [01-foundation/glossary.md](../01-foundation/glossary.md)
8. **Update Indexes** - Meetings index, decisions index, master index
9. **Cross-Reference** - Link all related documents bidirectionally
10. **Delete original** - Remove processed file from `08-documents-to-parse/`

#### Meeting Note Structure

Every meeting note should include:

- **Frontmatter** - Complete metadata including original language if translated
- **Translation Note** - If meeting was not in English, note at top of document
- **Executive Summary** - 2-4 paragraph overview of the entire meeting
- **Action Items** - Checkboxes with owner, due date, priority
- **Index** - Table of contents for topics discussed
- **Topics: Breakdown** - Each topic with executive summary and key takeaways
- **Decisions Made** - List with links to ADRs for significant ones
- **Blockers and Risks** - Any impediments identified
- **Parking Lot** - Deferred topics
- **Next Steps** - What happens next
- **References** - Links to related materials

#### When to Create ADRs from Meetings

Create an ADR if the decision:

- Has long-term architectural or strategic implications
- Affects multiple systems or teams
- Involves choosing between meaningful alternatives
- Has notable tradeoffs or consequences
- Sets a precedent for future decisions
- Commits significant resources or changes direction

**Minor decisions stay in meeting notes only.**

#### Parsing Tips

**Recognizing action items:**

- "I'll/I will [do something]"
- "[Person] can you [do something]"
- "We need to [do something]"
- "Action item:", "TODO:", "Follow up on"

**Recognizing decisions:**

- "We've decided to..."
- "Let's go with [option]"
- "We're choosing X over Y"
- "Agreed upon approach..."
- Consensus reached after discussion

**Recognizing blockers:**

- "We're blocked by..."
- "Waiting on..."
- "Can't proceed until..."
- "Risk that..."
- "Potential issue..."

#### Quality Checklist for Meeting Notes

Before finalizing:

- [ ] Executive summary is clear and comprehensive
- [ ] All action items have owners (or marked TBD)
- [ ] Topics are professionally titled and structured
- [ ] Dates in ISO format (YYYY-MM-DD)
- [ ] All attendees listed
- [ ] Significant decisions extracted to ADRs
- [ ] New terms added to glossary
- [ ] All indexes updated
- [ ] Cross-references are bidirectional
- [ ] Translation noted if applicable

#### Missing Information Handling

- **No date:** Estimate from context, note as "estimated"
- **No attendees:** List names from transcript or mark "Not recorded"
- **No owner for action:** Use "Team/TBD"
- **No due date:** Use "TBD" or estimate from context
- **Unclear decision:** Note in meeting but don't create ADR

#### Language Translation

**All transcripts must be in English:**

- Auto-detect language of transcript
- Translate to English if needed
- Note original language in metadata
- Add translation note at top of document
- Preserve names, proper nouns, technical terms

See [Claude Code Instructions - Meeting Transcript Parser](./instructions.md#meeting-transcript-parser) for comprehensive parsing guidelines.

## Knowledge Base Maintenance

### Understanding Knowledge Base Structure

The knowledge base (`04-knowledge-base/`) is organized into three domains:

**Technical Domain** (`04-knowledge-base/technical/`)

- **architecture/** - System design, components, patterns, data models
- **apis-and-integrations/** - API specs, integration points, third-party services
- **infrastructure/** - Deployment, environments, monitoring, security

**Business Domain** (`04-knowledge-base/business/`)

- **requirements/** - User stories, acceptance criteria, specifications
- **user-research/** - Personas, journey maps, interviews, usability studies
- **market-analysis/** - Competitive analysis, market sizing, trends

**Operational Domain** (`04-knowledge-base/operational/`)

- **processes/** - Workflows, procedures, best practices, standards
- **runbooks/** - Operational procedures, troubleshooting, incident response

### Daily Knowledge Base Tasks

**As you work:**

- Document technical implementations in `technical/`
- Create/update requirements in `business/requirements/`
- Add troubleshooting steps to `operational/runbooks/`
- Update process documentation when workflows change

**What to document immediately:**

- New API endpoints or integrations
- Architecture changes or new components
- User research findings
- Process improvements
- Incident resolutions

### Weekly Knowledge Base Review

**Every Friday:**

1. **Review new technical work**

   - Did we build new features? Document in `technical/architecture/`
   - Did we integrate new services? Document in `technical/apis-and-integrations/`
   - Did we change infrastructure? Document in `technical/infrastructure/`

2. **Review new requirements**

   - New user stories? Add to `business/requirements/`
   - User research completed? Add to `business/user-research/`
   - Market insights? Add to `business/market-analysis/`

3. **Review operational changes**

   - New workflows? Update `operational/processes/`
   - New procedures? Add to `operational/runbooks/`

4. **Update knowledge base indexes**
   - Update `04-knowledge-base/technical/_index.md`
   - Update `04-knowledge-base/business/_index.md`
   - Update `04-knowledge-base/operational/_index.md`

**Time required:** 20-30 minutes

### Monthly Knowledge Base Audit

**First Monday of each month:**

1. **Check for outdated content**

   - Review technical docs for deprecated features
   - Update requirements that have changed
   - Verify runbooks still work as documented

2. **Validate cross-references**

   - Technical docs link to related decisions
   - Requirements link to implementation docs
   - Runbooks reference current architecture

3. **Check for gaps**

   - Undocumented features or systems
   - Missing API documentation
   - Incomplete runbooks

4. **Update domain indexes**
   - Ensure all documents are listed
   - Add descriptions for new entries
   - Remove archived items

**Time required:** 30-45 minutes

### Quarterly Knowledge Base Deep Dive

**First week of each quarter:**

1. **Architecture documentation review**

   - Are diagrams current?
   - Do they reflect actual implementation?
   - Are data models up to date?

2. **Requirements sync**

   - Do documented requirements match what was built?
   - Archive completed user stories
   - Update specifications that evolved

3. **Runbook validation**

   - Test operational procedures
   - Update based on recent incidents
   - Add missing troubleshooting steps

4. **Process optimization**
   - Review workflow documentation
   - Identify process improvements
   - Update based on team feedback

**Time required:** 2-3 hours

### Best Practices for Knowledge Base Content

**For Technical Documentation:**

1. Include code examples and diagrams
2. Document the "why" not just the "what"
3. Update when implementations change
4. Link to related decisions and requirements
5. Add technical terms to glossary

**For Business Documentation:**

1. Write user stories in standard format
2. Include clear acceptance criteria
3. Link requirements to user research
4. Keep market data fresh
5. Document assumptions and constraints

**For Operational Documentation:**

1. Write step-by-step procedures
2. Include expected outcomes
3. Add troubleshooting sections
4. Include rollback procedures
5. Test runbooks regularly
6. Update after incidents

## Weekly Maintenance (Every Friday)

### 1. Update Project Status

**File:** [03-active-work/\_current-status.md](../03-active-work/_current-status.md)

- Update report date and period
- Refresh "What Changed This Period" section
- Update metrics and KPIs
- Review and update active blockers
- Update upcoming milestones
- Add links to new decisions made this week

**Time required:** 15-20 minutes

### 2. Review and Process New Content

- **Check [08-documents-to-parse/](../08-documents-to-parse/)** for any unprocessed documents
- Parse and structure any remaining content
- Check for any loose markdown files in root directory
- Move them to appropriate category folders
- Ensure all new files have proper metadata
- Update relevant index files

**Time required:** 15-20 minutes (depending on volume)

### 3. Meeting Notes Cleanup

- Ensure all meetings from the week are documented
- Extract any decisions into proper decision records
- File action items into appropriate tracking system
- Update [06-meetings/\_meetings-index.md](../06-meetings/_meetings-index.md)
- Verify all meeting transcripts were processed and structured

**Time required:** 10 minutes

### 4. Knowledge Base Updates

- Review technical work completed this week
- Document new features, APIs, or infrastructure changes
- Update requirements based on recent discussions
- Add any new operational procedures or runbooks
- Update knowledge base indexes

**Time required:** 20-30 minutes

## Monthly Maintenance (First Monday of Month)

### 1. Update Master Index

**File:** [00-PROJECT-INDEX.md](../00-PROJECT-INDEX.md)

- Refresh "Recent Decisions" list with last 5 decisions
- Update "Recent Activity" section
- Update Project Health Dashboard
- Review and update "Key Documents" links
- Verify all navigation links work
- Update knowledge base highlights

**Time required:** 20-30 minutes

### 2. Decision Records Audit

**File:** [02-decisions/\_decisions-index.md](../02-decisions/_decisions-index.md)

- Review decision statuses - are any now superseded?
- Update index with new decisions
- Check for decisions that should be archived
- Verify ADR numbering sequence is correct
- Link decisions to implementation docs in knowledge base

**Time required:** 15 minutes

### 3. Priorities Review

**File:** [03-active-work/priorities.md](../03-active-work/priorities.md)

- Update current priorities based on recent decisions
- Remove completed priorities
- Add new priorities from planning sessions
- Ensure alignment with project objectives

**Time required:** 15-20 minutes

### 4. Glossary Update

**File:** [01-foundation/glossary.md](../01-foundation/glossary.md)

- Add new terms that have emerged
- Update definitions that have evolved
- Remove deprecated terms
- Alphabetize entries
- Link terms to documents where they're defined

**Time required:** 10-15 minutes

### 5. Knowledge Base Audit

- Check for outdated technical documentation
- Update requirements that have changed
- Verify runbooks reflect current procedures
- Update all knowledge base indexes
- Check cross-references between domains

**Time required:** 30-45 minutes

## Quarterly Maintenance (First Week of Quarter)

### 1. Archive Old Content

**Directory:** [07-archive/](../07-archive/)

Content to archive:

- Meeting notes older than 6 months
- Superseded decision records
- Completed research that's no longer active
- Outdated technical documentation
- Deprecated features or systems
- Old requirements that have been fulfilled

**Process:**

1. Create new quarter folder: `07-archive/YYYY-QQ/`
2. Move old content to appropriate subfolder (decisions/, meetings/, knowledge-base/)
3. Update [07-archive/\_archive-log.md](../07-archive/_archive-log.md)
4. Update source documents with `status: archived`
5. Remove from active indexes

**Time required:** 1-2 hours

### 2. Link Health Check

- Run link checker on all markdown files
- Fix broken internal links
- Update external links that have changed
- Remove links to archived content (or update to archive location)
- Verify cross-references between knowledge base domains

**Tools:** VS Code Markdown Link Checker or similar

**Time required:** 30-45 minutes

### 3. Metadata Audit

Check random sample of documents (20-30) for:

- Complete YAML frontmatter
- Accurate `last-updated` dates
- Proper `status` values
- Meaningful summaries
- Appropriate tags
- Correct document types

**Time required:** 30 minutes

### 4. Structure Review

- Are documents in the right categories?
- Do we need new categories in knowledge base?
- Are templates still appropriate?
- Is the folder structure still serving us well?
- Should we split or merge any knowledge base subcategories?

**Time required:** 30 minutes

### 5. Knowledge Base Deep Dive

- Review architecture documentation accuracy
- Validate API documentation against actual APIs
- Test runbooks and update as needed
- Review requirements vs. implementation
- Update market analysis data
- Consolidate fragmented documentation

**Time required:** 2-3 hours

### 6. User Feedback Integration

- Review feedback from team about knowledge base
- Identify pain points or missing content
- Plan improvements
- Update templates if needed
- Address documentation gaps

**Time required:** 30-60 minutes

## Best Practices

### Writing Document Summaries

Good summaries for LLM discovery:

- **Be specific:** "Decision to use PostgreSQL for primary database instead of MongoDB"
- **Not vague:** "Database decision"

- **Include impact:** "Architecture decision affecting all backend services and data models"
- **Not generic:** "Technical decision"

- **Use keywords:** Include searchable terms like "authentication", "API", "infrastructure"

### Tagging Strategy

- Use 3-7 tags per document
- Use consistent tag names across documents
- Common useful tags:
  - **Technical:** `architecture`, `infrastructure`, `security`, `api`, `database`, `frontend`, `backend`
  - **Business:** `requirements`, `user-research`, `market-analysis`, `user-experience`
  - **Operational:** `process`, `runbook`, `deployment`, `monitoring`, `incident-response`
  - **Priority:** `high-priority`, `blocked`, `technical-debt`
  - **Type:** `decision`, `planning`, `retrospective`, `troubleshooting`

### Cross-Referencing

Always link bidirectionally:

```markdown
<!-- In ADR document -->

Related:

- See [Database Architecture](../knowledge-base/technical/architecture/database-architecture.md)
- Implements [Requirement: Data Storage](../knowledge-base/business/requirements/data-storage-requirements.md)

<!-- In technical architecture document -->

Related:

- Based on [ADR-015: Database Selection](../../02-decisions/2025-10-17-database-selection.md)
- Fulfills [Data Storage Requirements](../../business/requirements/data-storage-requirements.md)

<!-- In requirement document -->

Related:

- Decided in [ADR-015](../../../02-decisions/2025-10-17-database-selection.md)
- Implemented in [Database Architecture](../../technical/architecture/database-architecture.md)
```

### Status Indicators

Use consistent status values:

- **active** - Current, in use
- **draft** - Work in progress, not yet finalized
- **proposed** - Awaiting approval/decision
- **accepted** - Approved (for decisions)
- **rejected** - Not approved (for decisions)
- **superseded** - Replaced by newer version
- **deprecated** - No longer recommended but not fully replaced
- **archived** - Historical, not current

### Knowledge Base Organization Tips

**Keep related content together:**

- Group API documentation by service
- Keep architecture docs for related components together
- Organize requirements by feature area

**Use clear naming:**

- `user-authentication-api.md` not `auth.md`
- `deployment-production-runbook.md` not `deploy.md`
- `user-persona-enterprise-admin.md` not `persona1.md`

**Document relationships:**

- Link requirements to their implementations
- Connect architecture docs to the decisions that drove them
- Link runbooks to the systems they operate

## Troubleshooting

### "I can't find information I know we documented"

**Solutions:**

1. Check [00-PROJECT-INDEX.md](../00-PROJECT-INDEX.md) navigation
2. Search by tag: `grep -r "tags:.*keyword" --include="*.md"`
3. Search by title: `grep -r "title:.*keyword" --include="*.md"`
4. Check appropriate knowledge base domain (_technical, business, operational_)
5. Check archive: Content may have been moved to `07-archive/`
6. Use VS Code search (Cmd+Shift+F / Ctrl+Shift+F)

### "I don't know where to put a document"

**Solutions:**

1. Review [Claude Code Instructions - Knowledge Base Structure](./instructions.md#knowledge-base-structure-and-workflows)
2. Determine primary purpose:
   - System/tech details? → `technical/`
   - User needs/market? → `business/`
   - How we work/operate? → `operational/`
3. Check similar existing documents
4. When in doubt, use tags to capture secondary topics

### "The knowledge base feels disorganized"

**Solutions:**

1. Run monthly maintenance tasks if overdue
2. Review and move misplaced files to correct domains
3. Update indexes in all knowledge base domains
4. Consider whether subcategories need adjustment
5. Schedule time for quarterly structure review

### "People aren't updating documents"

**Solutions:**

1. Make it part of definition of done
2. Add reminders to team rituals
3. Demonstrate value by using it in meetings
4. Simplify templates if they're too complex
5. Recognize and appreciate good documentation
6. Show how knowledge base helps with onboarding

### "Documents are getting stale"

**Solutions:**

1. Set calendar reminders for regular reviews
2. Assign owners to key documents
3. Add "last reviewed" dates to high-value docs
4. Include doc review in sprint planning
5. Archive truly outdated content rather than letting it rot

### "Technical docs don't match implementation"

**Solutions:**

1. Update docs when implementation changes
2. Review architecture docs during tech reviews
3. Test runbooks regularly and update
4. Link code changes to doc updates in PRs
5. Schedule quarterly validation of technical docs

## Automation Opportunities

Consider automating these tasks:

- **Link checking:** CI/CD pipeline can check for broken links
- **Metadata validation:** Script to verify all docs have required fields
- **Index generation:** Auto-generate parts of index files from metadata
- **Stale content alerts:** Notify owners when docs haven't been updated in X days
- **Template enforcement:** Pre-commit hooks to ensure templates are used
- **Meeting transcript processing:** Auto-detect and prompt for processing new transcripts

## Questions or Suggestions?

If this maintenance guide doesn't cover something you need:

1. Document your question/need
2. Propose an update to this guide
3. Share with the team for feedback
4. Update the guide with the improvement

## Maintenance Checklist

### Daily (As Needed)

- [ ] **Run `/maintenance-daily`** - Check for files to process
- [ ] Process meeting transcripts using parser workflow
- [ ] Document decisions immediately
- [ ] Update blockers as they arise
- [ ] Add technical docs as work is completed
- [ ] Update runbooks after incidents

### Weekly (Every Friday)

- [ ] **Run `/maintenance-weekly`** - Validate recent document quality
- [ ] **Review validation report** in `logs/validation-report-*.md`
- [ ] **Fix metadata issues** identified in the report
- [ ] Update [\_current-status.md](../03-active-work/_current-status.md)
- [ ] Clean up meeting notes and extract ADRs
- [ ] Update meeting index
- [ ] Ensure all meeting transcripts are processed
- [ ] Review and update knowledge base domains
- [ ] Update knowledge base indexes

### Monthly (First Monday)

- [ ] **Run `/maintenance-monthly`** - Get cleanup recommendations
- [ ] **Review cleanup report** in `logs/cleanup-report-*.md`
- [ ] **Execute recommended archival actions** manually
- [ ] Update [00-PROJECT-INDEX.md](../00-PROJECT-INDEX.md)
- [ ] Audit decision records
- [ ] Review and update priorities
- [ ] Update glossary
- [ ] Audit knowledge base for outdated content
- [ ] Validate cross-references across domains

### Quarterly (First Week)

- [ ] **Run `/maintenance-full`** - Comprehensive maintenance check
- [ ] Archive old content (based on monthly reports)
- [ ] Check all links
- [ ] Audit metadata sample
- [ ] Review structure
- [ ] Deep dive on knowledge base domains
- [ ] Validate technical documentation accuracy
- [ ] Test all runbooks
- [ ] Integrate user feedback

### Quick Check Anytime

- [ ] **Run `/maintenance-status`** - View recent maintenance activity

---

## Quick Reference: Meeting Transcript Parser

### Input: Meeting Transcript

**Supported formats:**

- Word documents (.docx)
- Markdown files (.md)
- Plain text files (.txt)

**What to provide:**

- Drop file in `08-documents-to-parse/`
- Files with "sync", "meeting", or "meet" in name are auto-detected
- Can be in any language (will be translated to English)

### Output: Structured Documentation

**What you'll get:**

1. **Meeting Note** in `06-meetings/YYYY-MM/`

   - Professional executive summary
   - Structured topics with key takeaways
   - Action items with owners and dates
   - Blockers and risks identified
   - Translation note if applicable

2. **Decision Records** (if applicable) in `02-decisions/`

   - ADRs for significant decisions
   - Context, rationale, alternatives, consequences

3. **Updated Documents**

   - Current status (if status discussed)
   - Priorities (if changed)
   - Blockers document
   - Glossary (new terms)

4. **Updated Indexes**

   - Meetings index
   - Decisions index
   - Master index (if significant)

5. **Cleanup**
   - Original transcript file deleted from `08-documents-to-parse/`

### Processing Time

- Simple standup: 10-15 minutes
- Regular meeting: 20-30 minutes
- Complex technical discussion: 30-45 minutes
- Multi-topic planning session: 45-60 minutes

### Voice and Tone

All output uses:

- Professional and clear language
- Objective, factual presentation
- Concise but comprehensive coverage
- Action-oriented emphasis

---

## Quick Reference: Knowledge Base Domains

### Technical Domain (`04-knowledge-base/technical/`)

**When to use:**

- Documenting system architecture and design
- Creating API documentation
- Documenting infrastructure and deployment
- Recording technical specifications
- Writing security documentation

**Common documents:**

- Architecture diagrams and designs
- API specifications
- Database schemas
- Deployment guides
- Security protocols

### Business Domain (`04-knowledge-base/business/`)

**When to use:**

- Writing user stories and requirements
- Documenting user research
- Recording market analysis
- Creating user personas
- Defining acceptance criteria

**Common documents:**

- User stories
- Product requirements
- User personas and journey maps
- Competitive analysis
- Market research reports

### Operational Domain (`04-knowledge-base/operational/`)

**When to use:**

- Documenting team processes
- Creating operational runbooks
- Writing troubleshooting guides
- Recording incident response procedures
- Defining workflows and standards

**Common documents:**

- Development workflows
- Deployment procedures
- Troubleshooting guides
- Incident response playbooks
- On-call procedures

---

**Remember:** A well-maintained knowledge base is a force multiplier for the entire team. The time invested in maintenance pays dividends in faster onboarding, better decisions, and reduced context-switching costs. The meeting transcript parser ensures every conversation becomes searchable, structured knowledge. The three-domain knowledge base structure keeps all project information organized and discoverable.
