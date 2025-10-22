#!/bin/bash

# Get the script directory and navigate to repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

mkdir -p logs

LOG_FILE="logs/monthly-cleanup-$(date +%Y-%m-%d-%H%M%S).log"
REPORT_FILE="logs/cleanup-report-$(date +%Y-%m-%d).md"

echo "╔════════════════════════════════════════════╗" | tee -a "$LOG_FILE"
echo "║      Monthly Cleanup - Started             ║" | tee -a "$LOG_FILE"
echo "║      $(date)                    ║" | tee -a "$LOG_FILE"
echo "╚════════════════════════════════════════════╝" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Create report header
cat > "$REPORT_FILE" <<EOF
# Monthly Cleanup Report
**Date:** $(date +%Y-%m-%d)
**Generated:** $(date)

## Summary

This report identifies content that may need attention. **No files have been modified or deleted.**

## Recommendations

EOF

echo "📋 Analyzing knowledge base for cleanup opportunities..." | tee -a "$LOG_FILE"

# Find old meeting notes (>6 months)
echo "" | tee -a "$LOG_FILE"
echo "Checking for old meeting notes..." | tee -a "$LOG_FILE"
OLD_MEETINGS=$(find 06-meetings -name "*.md" -mtime +180 2>/dev/null)

if [ -n "$OLD_MEETINGS" ]; then
    MEETING_COUNT=$(echo "$OLD_MEETINGS" | wc -l | tr -d ' ')
    echo "Found $MEETING_COUNT meeting note(s) older than 6 months" | tee -a "$LOG_FILE"
    echo "" >> "$REPORT_FILE"
    echo "### Old Meeting Notes ($MEETING_COUNT files)" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Consider archiving these meeting notes:" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "$OLD_MEETINGS" | while read -r file; do
        echo "- \`$file\`" >> "$REPORT_FILE"
    done
else
    echo "No old meeting notes found" | tee -a "$LOG_FILE"
    echo "### Old Meeting Notes" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "No meeting notes older than 6 months found." >> "$REPORT_FILE"
fi

# Find documents not updated in over a year
echo "" | tee -a "$LOG_FILE"
echo "Checking for stale documents..." | tee -a "$LOG_FILE"
STALE_DOCS=$(find . -name "*.md" -mtime +365 ! -path "./logs/*" ! -path "./07-archive/*" ! -path "./08-documents-to-parse/*" 2>/dev/null)

if [ -n "$STALE_DOCS" ]; then
    STALE_COUNT=$(echo "$STALE_DOCS" | wc -l | tr -d ' ')
    echo "Found $STALE_COUNT document(s) not updated in over a year" | tee -a "$LOG_FILE"
    echo "" >> "$REPORT_FILE"
    echo "### Stale Documents ($STALE_COUNT files)" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "These documents haven't been updated in over a year:" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "$STALE_DOCS" | while read -r file; do
        echo "- \`$file\`" >> "$REPORT_FILE"
    done
else
    echo "No stale documents found" | tee -a "$LOG_FILE"
fi

# Add action items to report
cat >> "$REPORT_FILE" <<EOF

## Suggested Actions

1. **Review old meeting notes** - Archive meetings older than 6 months to \`07-archive/\`
2. **Update or archive stale documents** - Review documents not updated in over a year
3. **Check for duplicates** - Manually review similar document titles
4. **Validate cross-references** - Run link checker to find broken links

## Next Steps

- Review this report carefully before taking any action
- Move outdated content to \`07-archive/YYYY-QQ/\`
- Update \`07-archive/_archive-log.md\` for any archived content
- Run \`/maintenance-weekly\` to validate remaining documents

**Remember:** This is a recommendation report only. Always review before archiving.
EOF

echo "" | tee -a "$LOG_FILE"
echo "════════════════════════════════════════════" | tee -a "$LOG_FILE"
echo "✓ Monthly Cleanup Completed: $(date)" | tee -a "$LOG_FILE"
echo "════════════════════════════════════════════" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

echo "📋 Cleanup Report: $REPORT_FILE" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "⚠️  IMPORTANT: Review report and manually execute recommended actions" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "📄 Full log saved to: $LOG_FILE" | tee -a "$LOG_FILE"
