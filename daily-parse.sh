#!/bin/bash

# Get the script directory and navigate to repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

# Create logs and review directories
mkdir -p logs
mkdir -p 08-documents-to-parse/review-needed

# Log file
LOG_FILE="logs/daily-parse-$(date +%Y-%m-%d-%H%M%S).log"

echo "╔════════════════════════════════════════════╗" | tee -a "$LOG_FILE"
echo "║        Daily Parse - Started               ║" | tee -a "$LOG_FILE"
echo "║        $(date)                    ║" | tee -a "$LOG_FILE"
echo "╚════════════════════════════════════════════╝" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Check if there are files to process
FILE_COUNT=$(find 08-documents-to-parse -maxdepth 1 -type f ! -name "README.md" 2>/dev/null | wc -l | tr -d ' ')

if [ "$FILE_COUNT" -eq 0 ]; then
    echo "✓ No files to process in 08-documents-to-parse/" | tee -a "$LOG_FILE"
    echo "" | tee -a "$LOG_FILE"
else
    echo "📁 Found $FILE_COUNT file(s) to process" | tee -a "$LOG_FILE"
    echo "" | tee -a "$LOG_FILE"
    echo "ℹ️  Files found - manual processing required:" | tee -a "$LOG_FILE"

    find 08-documents-to-parse -maxdepth 1 -type f ! -name "README.md" 2>/dev/null | while read -r file; do
        echo "   - $(basename "$file")" | tee -a "$LOG_FILE"
    done

    echo "" | tee -a "$LOG_FILE"
    echo "📝 To process these files, use Claude Code directly with the parsing workflow" | tee -a "$LOG_FILE"
    echo "   or move files to review-needed if they require manual review" | tee -a "$LOG_FILE"
fi

echo "" | tee -a "$LOG_FILE"
echo "════════════════════════════════════════════" | tee -a "$LOG_FILE"
echo "✓ Daily Parse Completed: $(date)" | tee -a "$LOG_FILE"
echo "════════════════════════════════════════════" | tee -a "$LOG_FILE"

# Check if there are files needing review
if [ -d "08-documents-to-parse/review-needed" ] && [ "$(ls -A 08-documents-to-parse/review-needed 2>/dev/null)" ]; then
    echo "" | tee -a "$LOG_FILE"
    echo "⚠️  ATTENTION: Files need manual review" | tee -a "$LOG_FILE"
    echo "    Location: 08-documents-to-parse/review-needed/" | tee -a "$LOG_FILE"
    ls -1 08-documents-to-parse/review-needed/ | sed 's/^/    - /' | tee -a "$LOG_FILE"
fi

echo "" | tee -a "$LOG_FILE"
echo "📄 Full log saved to: $LOG_FILE" | tee -a "$LOG_FILE"
