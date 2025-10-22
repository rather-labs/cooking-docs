#!/usr/bin/env python3
"""
Process Sync Z - Lucas Spanish meeting files and convert them to structured English meeting notes.
"""

import os
from docx import Document
from datetime import datetime
import re

def extract_docx_text(filepath):
    """Extract text from .docx file"""
    doc = Document(filepath)
    text = []
    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text)
    return '\n'.join(text)

def parse_meeting_date(filename):
    """Extract date from filename like 'Sync Z _ Lucas_ 2025_08_18...'"""
    match = re.search(r'(\d{4})_(\d{2})_(\d{2})', filename)
    if match:
        year, month, day = match.groups()
        return f"{year}-{month}-{day}"
    return None

def process_meeting(filepath):
    """Process a single meeting file"""
    filename = os.path.basename(filepath)
    meeting_date = parse_meeting_date(filename)

    # Extract Spanish text
    spanish_text = extract_docx_text(filepath)

    # Return data for processing
    return {
        'filename': filename,
        'filepath': filepath,
        'date': meeting_date,
        'spanish_text': spanish_text,
        'month_folder': meeting_date[:7] if meeting_date else None  # e.g., "2025-08"
    }

# List of meetings to process
meetings = [
    './07-archive/processed-source-docs/2025-10-19-gemini-meeting-notes/Sync Z _ Lucas_ 2025_08_18 10_15 GMT-03_00 - Notas de Gemini.docx',
    './07-archive/processed-source-docs/2025-10-19-gemini-meeting-notes/Sync Z _ Lucas_ 2025_08_25 10_14 GMT-03_00 - Notas de Gemini.docx',
    './07-archive/processed-source-docs/2025-10-19-gemini-meeting-notes/Sync Z _ Lucas_ 2025_09_08 10_14 GMT-03_00 - Notas de Gemini.docx',
    './07-archive/processed-source-docs/2025-10-19-gemini-meeting-notes/Sync Z _ Lucas_ 2025_09_15 10_15 GMT-03_00 - Notas de Gemini.docx',
    './07-archive/processed-source-docs/2025-10-19-gemini-meeting-notes/Sync Z _ Lucas_ 2025_09_22 10_15 GMT-03_00 - Notas de Gemini.docx',
    './07-archive/processed-source-docs/2025-10-19-gemini-meeting-notes/Sync Z _ Lucas_ 2025_09_29 10_14 GMT-03_00 - Notas de Gemini.docx',
    './07-archive/processed-source-docs/2025-10-19-gemini-meeting-notes/Sync Z _ Lucas_ 2025_10_13 10_15 GMT-03_00 - Notas de Gemini.docx',
]

# Process all meetings
print("Processing Sync Z - Lucas meetings...")
for meeting_path in meetings:
    data = process_meeting(meeting_path)
    print(f"\n{'='*80}")
    print(f"File: {data['filename']}")
    print(f"Date: {data['date']}")
    print(f"Month Folder: {data['month_folder']}")
    print(f"Text Length: {len(data['spanish_text'])} characters")
    print(f"Preview (first 500 chars):")
    print(data['spanish_text'][:500])
    print('='*80)

print("\nAll meetings extracted successfully!")
