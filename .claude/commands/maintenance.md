---
description: Show maintenance options
---

# Knowledge Base Maintenance Commands

The following automated maintenance commands help keep your documentation organized, validated, and up-to-date:

## Available Commands

### `/maintenance-status` - Quick Status
**Duration:** < 1 second
**Purpose:** View recent maintenance logs quickly

### `/maintenance-daily` - Daily Parse
**Duration:** ~1 minute
**Purpose:** Check for files in `08-documents-to-parse/` that need processing
**Outputs:** Log file in `logs/`

### `/maintenance-weekly` - Weekly Validation
**Duration:** ~2-5 minutes
**Purpose:** Validate document quality and metadata completeness
**Outputs:** Validation report + log file in `logs/`
**Action Required:** Review and fix issues in the validation report

### `/maintenance-monthly` - Monthly Cleanup
**Duration:** ~1-3 minutes
**Purpose:** Identify stale content and archival candidates
**Outputs:** Cleanup report + log file in `logs/`
**Action Required:** Review report and manually execute recommended actions

### `/maintenance-full` - Full Maintenance
**Duration:** ~5-10 minutes
**Purpose:** Run all maintenance tasks (daily, weekly, monthly)
**Outputs:** Multiple reports and log files

## How to Use

1. Choose the appropriate command from the list above
2. Type the command (e.g., `/maintenance-weekly`)
3. Review the output and any generated reports in `logs/`
4. Take action on identified issues

## When to Run

- **Daily:** `/maintenance-daily` when adding new documents
- **Weekly:** `/maintenance-weekly` every Friday
- **Monthly:** `/maintenance-monthly` first Monday of month
- **Quarterly:** `/maintenance-full` for comprehensive check

For more details, see the [Maintenance Guide](../.claude/maintenance-guide.md)
