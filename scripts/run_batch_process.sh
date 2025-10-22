#!/bin/bash
#
# Batch Process Meeting Documents
#
# Usage:
#   ./run_batch_process.sh              # Process all files
#   ./run_batch_process.sh --dry-run    # Test run without changes
#   ./run_batch_process.sh --filter sync  # Process only files with 'sync' in name
#

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if ANTHROPIC_API_KEY is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Error: ANTHROPIC_API_KEY environment variable is not set"
    echo "Please set it with: export ANTHROPIC_API_KEY='your-key-here'"
    exit 1
fi

# Install requirements if needed
if ! python3 -c "import anthropic" 2>/dev/null; then
    echo "Installing Python dependencies..."
    pip3 install -r "$SCRIPT_DIR/requirements.txt"
fi

# Run the batch processor
echo "Starting batch document processor..."
python3 "$SCRIPT_DIR/batch_process_meetings.py" "$@"
