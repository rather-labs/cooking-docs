#!/bin/bash

# Get the script directory and navigate to repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

mkdir -p logs

LOG_FILE="logs/weekly-validation-$(date +%Y-%m-%d-%H%M%S).log"
REPORT_FILE="logs/validation-report-$(date +%Y-%m-%d).md"

echo "╔════════════════════════════════════════════╗" | tee -a "$LOG_FILE"
echo "║      Weekly Validation - Started           ║" | tee -a "$LOG_FILE"
echo "║      $(date)                    ║" | tee -a "$LOG_FILE"
echo "╚════════════════════════════════════════════╝" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Initialize counters
ISSUES_FOUND=0
FILES_CHECKED=0

# Create report header
cat > "$REPORT_FILE" <<EOF
# Weekly Validation Report
**Date:** $(date +%Y-%m-%d)
**Generated:** $(date)

## Summary

EOF

echo "📋 Checking documents modified in last 7 days..." | tee -a "$LOG_FILE"

# Find recent files
RECENT_FILES=$(find . -name "*.md" -mtime -7 ! -path "./logs/*" ! -path "./07-archive/*" ! -path "./08-documents-to-parse/*" 2>/dev/null)

if [ -z "$RECENT_FILES" ]; then
    echo "✓ No recent documents to validate" | tee -a "$LOG_FILE"
    echo "No documents modified in the last 7 days." >> "$REPORT_FILE"
else
    FILE_COUNT=$(echo "$RECENT_FILES" | wc -l | tr -d ' ')
    echo "Found $FILE_COUNT file(s) to check" | tee -a "$LOG_FILE"
    echo "" | tee -a "$LOG_FILE"

    echo "### Recent Documents Checked: $FILE_COUNT" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"

    # Check each file
    while IFS= read -r file; do
        FILES_CHECKED=$((FILES_CHECKED + 1))
        echo "Checking: $file" >> "$LOG_FILE"

        # Check for YAML frontmatter
        if ! head -1 "$file" | grep -q "^---$"; then
            echo "⚠️  Missing frontmatter: $file" | tee -a "$LOG_FILE"
            echo "- ⚠️ **Missing frontmatter**: $file" >> "$REPORT_FILE"
            ISSUES_FOUND=$((ISSUES_FOUND + 1))
        fi

        # Check for required fields
        if grep -q "^---$" "$file"; then
            if ! grep -q "^title:" "$file"; then
                echo "⚠️  Missing title: $file" | tee -a "$LOG_FILE"
                echo "- ⚠️ **Missing title**: $file" >> "$REPORT_FILE"
                ISSUES_FOUND=$((ISSUES_FOUND + 1))
            fi

            if ! grep -q "^type:" "$file"; then
                echo "⚠️  Missing type: $file" | tee -a "$LOG_FILE"
                echo "- ⚠️ **Missing type**: $file" >> "$REPORT_FILE"
                ISSUES_FOUND=$((ISSUES_FOUND + 1))
            fi

            if ! grep -q "^date:" "$file"; then
                echo "⚠️  Missing date: $file" | tee -a "$LOG_FILE"
                echo "- ⚠️ **Missing date**: $file" >> "$REPORT_FILE"
                ISSUES_FOUND=$((ISSUES_FOUND + 1))
            fi
        fi

    done <<< "$RECENT_FILES"

    echo "" | tee -a "$LOG_FILE"
fi

# Add summary to report
cat >> "$REPORT_FILE" <<EOF

## Validation Results

- **Files Checked:** $FILES_CHECKED
- **Issues Found:** $ISSUES_FOUND

EOF

if [ $ISSUES_FOUND -eq 0 ]; then
    echo "✓ All documents passed validation!" | tee -a "$LOG_FILE"
    echo "✅ **All documents passed validation!**" >> "$REPORT_FILE"
else
    echo "⚠️  Found $ISSUES_FOUND issue(s) - see report for details" | tee -a "$LOG_FILE"
    echo "" >> "$REPORT_FILE"
    echo "## Recommendations" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "1. Review and fix documents with missing metadata" >> "$REPORT_FILE"
    echo "2. Ensure all documents have complete YAML frontmatter" >> "$REPORT_FILE"
    echo "3. Add missing fields (title, type, date, summary, tags)" >> "$REPORT_FILE"
fi

echo "" | tee -a "$LOG_FILE"
echo "════════════════════════════════════════════" | tee -a "$LOG_FILE"
echo "✓ Weekly Validation Completed: $(date)" | tee -a "$LOG_FILE"
echo "════════════════════════════════════════════" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

echo "📋 Validation Report: $REPORT_FILE" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "📄 Full log saved to: $LOG_FILE" | tee -a "$LOG_FILE"
