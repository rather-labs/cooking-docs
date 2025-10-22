#!/usr/bin/env python3
"""
Process meeting notes from .docx files in 08-documents-to-parse folder.
Converts Gemini-generated meeting notes to structured markdown files.
"""

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
import json

# Paths - use script location to find repo root
BASE_DIR = Path(__file__).parent.parent
DOCS_TO_PARSE = BASE_DIR / "08-documents-to-parse"
MEETINGS_DIR = BASE_DIR / "06-meetings"
PROCESSED_DIR = BASE_DIR / "07-archive/processed-source-docs"

# Meeting type categorization
MEETING_TYPES = {
    'daily': ['Daily - Cooking.gg'],
    'demo': ['[Cooking] Demo'],
    'sync': ['Sync Z _ Lucas'],
    'mobile': ['Cooking Mobile'],
    'technical': [
        'Cooking _ DevOps',
        'Cooking _ Echo',
        'Cooking _ HL',
        'Cooking _ Indexer',
        'Cooking _ TradingView',
        'Liquidity Pools',
        'Limit Orders'
    ],
    'other': [
        'Alineación de Bugs',
        'Indexer + Features',
        'Referral Program',
        'Entrevista técnica',
        'Filters Mobile',
        'Kensei',
        'Miguel _ Cooking'
    ]
}

def extract_date_from_filename(filename):
    """Extract date from filename like 'Daily - Cooking.gg_ 2025_10_17 09_29 GMT-03_00'"""
    match = re.search(r'(\d{4})_(\d{2})_(\d{2})', filename)
    if match:
        year, month, day = match.groups()
        return f"{year}-{month}-{day}"
    return None

def categorize_meeting(filename):
    """Determine meeting type from filename"""
    for meeting_type, patterns in MEETING_TYPES.items():
        for pattern in patterns:
            if pattern in filename:
                return meeting_type
    return 'other'

def convert_docx_to_text(docx_path):
    """Convert .docx file to plain text using textutil"""
    try:
        result = subprocess.run(
            ['textutil', '-convert', 'txt', '-stdout', str(docx_path)],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error converting {docx_path}: {e}")
        return None

def parse_meeting_content(text):
    """Parse Gemini meeting notes structure"""
    data = {
        'title': '',
        'date': '',
        'attendees': [],
        'summary': '',
        'details': '',
        'action_items': [],
        'transcript': ''
    }

    # Extract title and date
    lines = text.split('\n')
    for i, line in enumerate(lines[:10]):
        if re.match(r'\d{1,2}\s+\w+\s+\d{4}', line):
            data['date'] = line.strip()
        elif line.strip() and not line.startswith('📝') and not line.startswith('Invitados'):
            if not data['title'] and len(line.strip()) > 3:
                data['title'] = line.strip()

    # Extract attendees
    attendees_match = re.search(r'Invitados\s+(.+?)(?:\n|Archivos)', text, re.DOTALL)
    if attendees_match:
        attendees_text = attendees_match.group(1)
        data['attendees'] = [a.strip() for a in re.split(r'\s+', attendees_text) if a.strip()]

    # Extract summary
    summary_match = re.search(r'Resumen\s*\n(.+?)(?:\nDetalles|\n\n)', text, re.DOTALL)
    if summary_match:
        data['summary'] = summary_match.group(1).strip()

    # Extract details
    details_match = re.search(r'Detalles\s*\n(.+?)(?:\nPasos siguientes|Revisa las notas)', text, re.DOTALL)
    if details_match:
        data['details'] = details_match.group(1).strip()

    # Extract action items
    actions_match = re.search(r'Pasos siguientes recomendados\s*\n(.+?)(?:\nRevisa las notas|📖 Transcripción)', text, re.DOTALL)
    if actions_match:
        actions_text = actions_match.group(1).strip()
        # Split by bullet points
        action_items = re.findall(r'•\s*(.+?)(?=\n\s*•|\Z)', actions_text, re.DOTALL)
        data['action_items'] = [item.strip() for item in action_items if item.strip()]

    return data

def create_markdown_file(meeting_data, date_str, meeting_type, original_filename):
    """Create structured markdown meeting file"""

    # Determine file path based on meeting type
    if meeting_type == 'daily':
        subdir = 'daily-standups'
    elif meeting_type == 'demo':
        subdir = 'demos'
    elif meeting_type == 'sync':
        subdir = 'sync-meetings'
    elif meeting_type == 'mobile':
        subdir = 'mobile'
    elif meeting_type == 'technical':
        subdir = 'technical'
    else:
        subdir = 'other'

    meeting_subdir = MEETINGS_DIR / subdir
    meeting_subdir.mkdir(parents=True, exist_ok=True)

    # Create filename
    title_slug = re.sub(r'[^\w\s-]', '', meeting_data['title'].lower())
    title_slug = re.sub(r'[-\s]+', '-', title_slug)[:50]
    filename = f"{date_str}-{title_slug}.md"
    filepath = meeting_subdir / filename

    # Create markdown content
    markdown = f"""---
title: {meeting_data['title']}
type: meeting-notes
date: {date_str}
meeting-type: {meeting_type}
source: gemini-auto-notes
attendees: {json.dumps(meeting_data['attendees'][:10])}
summary: |
  {meeting_data['summary'][:200]}...
---

# {meeting_data['title']}

**Date:** {date_str}
**Meeting Type:** {meeting_type.title()}
**Source:** Auto-generated by Google Gemini

## Attendees
{chr(10).join([f'- {attendee}' for attendee in meeting_data['attendees'][:20]])}

## Summary

{meeting_data['summary']}

## Key Discussion Points

{meeting_data['details']}

## Action Items

{chr(10).join([f'- {item}' for item in meeting_data['action_items']])}

## Notes

- Original file: `{original_filename}`
- These notes were auto-generated by Google Gemini during the meeting
- Full transcript available in source document

---

**Related Documents:**
- [Meetings Index](../_meetings-index.md)
- [Project Status](../../03-active-work/_current-status.md)
"""

    return filepath, markdown

def main():
    """Main processing function"""
    print("Starting meeting notes processing...")
    print(f"Scanning {DOCS_TO_PARSE}")

    # Get all .docx files
    docx_files = list(DOCS_TO_PARSE.glob("*.docx"))
    print(f"Found {len(docx_files)} .docx files to process")

    # Create processed directory
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    skipped_count = 0
    error_count = 0

    for docx_file in docx_files:
        try:
            print(f"\nProcessing: {docx_file.name}")

            # Skip .DS_Store and other non-meeting files
            if docx_file.name.startswith('.'):
                skipped_count += 1
                continue

            # Extract date
            date_str = extract_date_from_filename(docx_file.name)
            if not date_str:
                print(f"  ⚠️  Could not extract date from {docx_file.name}")
                skipped_count += 1
                continue

            # Categorize meeting
            meeting_type = categorize_meeting(docx_file.name)
            print(f"  Type: {meeting_type}, Date: {date_str}")

            # Convert to text
            text = convert_docx_to_text(docx_file)
            if not text:
                print(f"  ❌ Failed to convert {docx_file.name}")
                error_count += 1
                continue

            # Parse content
            meeting_data = parse_meeting_content(text)
            if not meeting_data['title']:
                meeting_data['title'] = docx_file.stem

            # Create markdown file
            filepath, markdown = create_markdown_file(
                meeting_data,
                date_str,
                meeting_type,
                docx_file.name
            )

            # Write file
            filepath.write_text(markdown, encoding='utf-8')
            print(f"  ✅ Created: {filepath}")

            processed_count += 1

        except Exception as e:
            print(f"  ❌ Error processing {docx_file.name}: {e}")
            error_count += 1

    # Summary
    print(f"\n{'='*60}")
    print(f"Processing Complete!")
    print(f"{'='*60}")
    print(f"✅ Processed: {processed_count}")
    print(f"⚠️  Skipped: {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
