#!/bin/bash

# Process documents - convert .docx to .md
# This script converts all .docx files to markdown format

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/converted"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Counter
count=0

# Process each .docx file
for file in "$SCRIPT_DIR"/*.docx; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" .docx)
        output_file="$OUTPUT_DIR/${filename}.md"

        echo "Converting: $filename.docx"

        # Use textutil (macOS built-in) to convert to text, then save as .md
        textutil -convert txt -stdout "$file" > "$output_file"

        if [ $? -eq 0 ]; then
            count=$((count + 1))
            echo "  ✓ Converted to: ${filename}.md"
        else
            echo "  ✗ Failed to convert: $filename.docx"
        fi
    fi
done

echo ""
echo "========================================="
echo "Conversion complete!"
echo "Converted $count .docx files to markdown"
echo "Output directory: $OUTPUT_DIR"
echo "========================================="
