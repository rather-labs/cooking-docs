---
title: Batch Document Processing Scripts
type: documentation
date: 2025-10-20
summary: Automated scripts for processing meeting transcripts and documents with multi-language support and intelligent structured output generation.
---

# Batch Document Processing Scripts

Automated scripts to process meeting transcripts and documents from `08-documents-to-parse/` into structured documentation.

## Features

✅ **Auto-detection of meeting transcripts**
- By filename patterns (sync, meeting, meet, demo, daily)
- By content analysis (detects timestamps in parentheses)

✅ **Multi-language support**
- Automatic language detection
- Translation to English using Claude
- Preserves original language metadata

✅ **Structured output**
- Creates properly formatted meeting notes in `06-meetings/`
- Extracts executive summaries, topics, action items, decisions
- Generates frontmatter with complete metadata
- Organizes by year-month folders

✅ **Intelligent processing**
- Processes .docx and .md files
- Extracts text from Word documents
- Handles large files efficiently
- Error recovery and detailed logging

## Prerequisites

1. **Python 3.8+** installed
2. **Anthropic API key** set as environment variable
3. **Python dependencies** (auto-installed on first run)

## Setup

### 1. Set your Anthropic API key

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Add to your `~/.bashrc` or `~/.zshrc` to make it permanent:

```bash
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 2. Install dependencies (automatic on first run)

```bash
pip3 install -r scripts/requirements.txt
```

## Usage

### Process all documents

From the repository root directory:

```bash
./scripts/run_batch_process.sh
```

### Dry run (test without making changes)

```bash
./scripts/run_batch_process.sh --dry-run
```

### Process specific files only

```bash
# Process only files with 'sync' in the name
./scripts/run_batch_process.sh --filter sync

# Process only files with 'weekly' in the name
./scripts/run_batch_process.sh --filter weekly

# Process only files from August 2025
./scripts/run_batch_process.sh --filter 2025_08
```

### Combine options

```bash
# Dry run on sync files only
./scripts/run_batch_process.sh --dry-run --filter sync
```

## What the Script Does

### 1. **File Detection**

For each file in `08-documents-to-parse/`:
- Checks if it's a meeting transcript (by filename or timestamps in content)
- Skips non-meeting files (will be handled in future versions)

### 2. **Language Processing**

- Detects the language of the content
- If not English, translates the entire document
- Adds translation metadata to frontmatter

### 3. **Meeting Parsing**

Uses Claude AI to extract:
- Meeting metadata (date, attendees, type)
- Executive summary
- Topics discussed with key takeaways
- Action items with owners and due dates
- Decisions made
- Blockers and risks

### 4. **File Creation**

- Creates structured meeting note in `06-meetings/YYYY-MM/`
- Follows the meeting note template format
- Adds proper frontmatter with all metadata
- Deletes original file from `08-documents-to-parse/`

### 5. **Output**

Example output structure:

```
06-meetings/
├── 2025-07/
│   ├── 2025-07-07-cooking-sync-july-07.md
│   └── 2025-07-14-cooking-sync-14072025.md
├── 2025-08/
│   ├── 2025-08-18-cooking-weekly-sync-20250818.md
│   └── 2025-08-25-sync-z-lucas-2025-08-25.md
└── 2025-09/
    └── 2025-09-01-cooking-weekly-sync-20250901.md
```

## Output Example

The script creates meeting notes like this:

```markdown
---
title: Cooking Sync July 07
type: meeting-note
date: 2025-07-07
attendees: ["Lucas Cufré", "Naji Osmat", "Gregory Chapman", "Vadim Pleshkov"]
meeting-type: sync
tags: [cooking, sync, meeting]
summary: |
  Discussion about mobile app development, Apple account setup,
  and design approach with Evil Martians team.
---

# Cooking Sync July 07

**Date:** 2025-07-07
**Attendees:** Lucas Cufré, Naji Osmat, Gregory Chapman, Vadim Pleshkov
**Type:** sync

## Executive Summary

The team discussed mobile app development priorities...

## Action Items

- [ ] **Send Apple account documentation** - Assigned to: Lucas - Due: 2025-07-08 - Priority: High
- [ ] **Review mobile designs with Leo** - Assigned to: Naji - Due: 2025-07-14 - Priority: Medium

## Topics Discussed

### Mobile App Account Setup

Decision to use business account instead of personal account...

**Key Takeaways:**
- Business account provides better credibility
- Requires more documentation but same cost
- Better for financial applications

...
```

## Progress Tracking

The script shows real-time progress:

```
================================================================================
Batch Processing Started
================================================================================
Total files to process: 134
Dry run: False
================================================================================

[1/134] Processing: C107 - Weekly Demo.md
================================================================================
✓ Detected as meeting transcript
Language: English
Parsing meeting transcript...
Creating structured meeting note...
✓ Created: 06-meetings/2025-05/2025-05-16-weekly-demo.md
✓ Deleted: C107 - Weekly Demo.md

[2/134] Processing: Sync Z _ Lucas_ 2025_08_18 10_15 GMT-03_00 - Notas de Gemini.docx
================================================================================
✓ Detected as meeting transcript
Language: Spanish
Translating from Spanish to English...
Parsing meeting transcript...
Creating structured meeting note...
✓ Created: 06-meetings/2025-08/2025-08-18-sync-z-lucas.md
✓ Deleted: Sync Z _ Lucas_ 2025_08_18 10_15 GMT-03_00 - Notas de Gemini.docx

...

================================================================================
Processing Complete
================================================================================
Total files: 134
Processed: 98
Skipped: 34
Errors: 2
Translations: 73
Meetings created: 98
Decisions created: 0
Requirements created: 0
================================================================================
```

## Processing Time Estimates

Based on file analysis:

| File Type | Count | Time per File | Total Time |
|-----------|-------|---------------|------------|
| English .md meetings | 9 | 2-3 min | 20-30 min |
| Spanish .docx meetings | 73+ | 3-5 min | 4-6 hours |
| Requirements docs | 42 | 2-3 min | 1.5-2 hours |
| **TOTAL** | **124+** | | **~6-8.5 hours** |

The script can run unattended, so you can start it and let it process overnight.

## Dry Run Mode

Always test with `--dry-run` first:

```bash
./scripts/run_batch_process.sh --dry-run --filter "weekly sync"
```

This will:
- Show what files would be processed
- Display the structured output
- NOT create any files
- NOT delete any source files

## Troubleshooting

### Error: ANTHROPIC_API_KEY not set

```bash
export ANTHROPIC_API_KEY='your-key-here'
```

### Error: mammoth module not found

```bash
pip3 install mammoth
```

### Error: Permission denied

```bash
chmod +x scripts/run_batch_process.sh
```

### Files not being detected as meetings

The script checks for:
1. Filename contains: sync, meeting, meet, demo, daily
2. Content has 2+ timestamps like `(14:30)` or `Name (9:15):`

If a file should be processed but isn't, check these criteria.

## Advanced Usage

### Python API directly

```python
from batch_process_meetings import DocumentProcessor

processor = DocumentProcessor(
    base_dir="/path/to/CookingDocumentation",
    dry_run=False
)

# Process all files
processor.process_all()

# Process with filter
processor.process_all(filter_pattern="sync")

# Process single file
from pathlib import Path
processor.process_file(Path("08-documents-to-parse/meeting.md"))

# Get statistics
print(processor.stats)
```

### Customize processing

Edit `batch_process_meetings.py` to:
- Adjust Claude model (`claude-3-5-sonnet-20241022`)
- Modify meeting note format
- Add custom document type handlers
- Change detection patterns

## Next Steps

After processing completes:

1. **Review created files** in `06-meetings/`
2. **Update meeting index** manually or run index update script
3. **Extract significant decisions** into separate ADRs if needed
4. **Verify translations** for accuracy
5. **Process remaining non-meeting files** (requirements, technical docs)

## Future Enhancements

- [ ] Process requirement documents (C-series)
- [ ] Extract decisions into ADRs automatically
- [ ] Update indexes automatically
- [ ] Handle technical documentation
- [ ] Process research documents
- [ ] Batch update all indexes
- [ ] Resume from interruption
- [ ] Parallel processing for speed

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the dry-run output
3. Check error messages in terminal
4. Verify API key is set correctly
