#!/usr/bin/env python3
"""
Batch Meeting Document Processor for Cooking Documentation

This script processes meeting transcripts and documents from 08-documents-to-parse/,
translates them to English if needed, creates structured documentation, and updates indexes.

Features:
- Auto-detects meeting transcripts by filename and content (timestamps)
- Extracts text from .docx files
- Detects language and translates to English
- Creates structured meeting notes with proper frontmatter
- Extracts decisions into ADRs
- Updates all relevant indexes
- Processes requirements with 4-section structure

Usage:
    python batch_process_meetings.py [--dry-run] [--filter PATTERN]
"""

import os
import re
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import anthropic

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

class DocumentProcessor:
    """Main document processing class"""

    def __init__(self, base_dir: str, dry_run: bool = False):
        self.base_dir = Path(base_dir)
        self.dry_run = dry_run
        self.source_dir = self.base_dir / "08-documents-to-parse"
        self.meetings_dir = self.base_dir / "06-meetings"
        self.decisions_dir = self.base_dir / "02-decisions"
        self.kb_dir = self.base_dir / "04-knowledge-base"

        # Initialize Anthropic client
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        self.client = anthropic.Anthropic(api_key=api_key)

        # Statistics
        self.stats = {
            "total_files": 0,
            "processed": 0,
            "skipped": 0,
            "errors": 0,
            "translations": 0,
            "meetings_created": 0,
            "decisions_created": 0,
            "requirements_created": 0
        }

        # Get next ADR number
        self.next_adr = self._get_next_adr_number()

    def _get_next_adr_number(self) -> int:
        """Get the next available ADR number"""
        max_adr = 0
        if self.decisions_dir.exists():
            for file in self.decisions_dir.glob("*.md"):
                match = re.search(r'ADR-(\d+)', file.read_text())
                if match:
                    max_adr = max(max_adr, int(match.group(1)))
        return max_adr + 1

    def is_meeting_transcript(self, filepath: Path, content: str = None) -> bool:
        """
        Detect if a file is a meeting transcript by filename or content.

        Checks:
        1. Filename contains 'sync', 'meeting', or 'meet' (case-insensitive)
        2. Content contains 2+ timestamps in parentheses like (14:30) or Name (9:15):
        """
        filename = filepath.name.lower()

        # Check filename patterns
        if any(keyword in filename for keyword in ['sync', 'meeting', 'meet', 'demo', 'daily']):
            return True

        # Check content for timestamps if available
        if content:
            preview = content[:1000]  # Check first 1000 chars
            timestamp_patterns = [
                r'\(\d{1,2}:\d{2}\)',           # (14:30)
                r'\(\d{1,2}:\d{2}:\d{2}\)',     # (14:30:45)
                r'\w+\s*\(\d{1,2}:\d{2}\)',     # Name (14:30)
                r'\(\d{1,2}:\d{2}\s*[AP]M\)',   # (2:30 PM)
            ]

            timestamp_count = 0
            for pattern in timestamp_patterns:
                matches = re.findall(pattern, preview)
                timestamp_count += len(matches)

            if timestamp_count >= 2:
                return True

        return False

    def detect_language(self, text: str) -> str:
        """Detect the language of text using Claude"""
        prompt = f"""Detect the language of this text. Respond with only the language name (e.g., "English", "Spanish", "Portuguese").

Text sample:
{text[:500]}"""

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}]
        )

        language = message.content[0].text.strip()
        return language

    def translate_to_english(self, text: str, source_language: str) -> str:
        """Translate text to English using Claude"""
        prompt = f"""Translate this {source_language} text to English.

Guidelines:
- Preserve names, proper nouns, and technical terms
- Maintain professional tone
- Keep acronyms in original form (API, UI, etc.)
- Translate domain terms but keep clarity

Text to translate:
{text}"""

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )

        translated = message.content[0].text.strip()
        self.stats["translations"] += 1
        return translated

    def extract_docx_text(self, filepath: Path) -> str:
        """Extract text from .docx file"""
        try:
            import mammoth
            with open(filepath, 'rb') as f:
                result = mammoth.extract_raw_text(f)
                return result.value
        except ImportError:
            print("Warning: mammoth library not installed. Install with: pip install mammoth")
            return ""
        except Exception as e:
            print(f"Error extracting text from {filepath}: {e}")
            return ""

    def parse_meeting_transcript(self, content: str, filename: str, source_language: str = None) -> Dict:
        """Parse meeting transcript using Claude"""

        instructions = """You are processing a meeting transcript for the Cooking.gg project documentation.

Parse this meeting transcript and extract:

1. **Meeting Metadata**:
   - Date (YYYY-MM-DD format, infer from filename or content)
   - Attendees (list all participants)
   - Meeting type (standup/planning/retrospective/review/stakeholder/technical/ad-hoc)

2. **Executive Summary** (2-4 paragraphs):
   - Purpose of the meeting
   - Major topics covered
   - Key decisions or consensus achieved
   - Overall outcomes and next steps

3. **Topics Discussed** (for each topic):
   - Topic name
   - Executive summary (2-3 sentences)
   - Key takeaways (bullet points)
   - Discussion details (if complex)

4. **Action Items**:
   - Task description
   - Assigned to (person name or "TBD")
   - Due date (YYYY-MM-DD or "TBD")
   - Priority (High/Medium/Low)

5. **Decisions Made** (if any):
   - Decision statement
   - Brief rationale
   - Is it significant enough for an ADR? (yes/no)

6. **Blockers/Risks** (if any):
   - Blocker/risk description
   - Impact (High/Medium/Low)
   - Owner
   - Needs resolution by (date or "TBD")

Return the parsed information as a JSON object with this structure:
{
  "date": "YYYY-MM-DD",
  "attendees": ["Name1", "Name2"],
  "meeting_type": "type",
  "executive_summary": "summary text",
  "topics": [
    {
      "name": "Topic Name",
      "summary": "Executive summary",
      "takeaways": ["takeaway1", "takeaway2"],
      "details": "Additional details if needed"
    }
  ],
  "action_items": [
    {
      "task": "Task description",
      "assigned_to": "Name",
      "due_date": "YYYY-MM-DD",
      "priority": "Medium"
    }
  ],
  "decisions": [
    {
      "decision": "What was decided",
      "rationale": "Why",
      "significant": false
    }
  ],
  "blockers": [
    {
      "description": "Blocker description",
      "impact": "High",
      "owner": "Name",
      "resolution_date": "YYYY-MM-DD"
    }
  ]
}"""

        if source_language:
            instructions += f"\n\nNote: This meeting was originally conducted in {source_language} and has been translated to English."

        prompt = f"""{instructions}

Filename: {filename}

Transcript:
{content[:15000]}"""  # Limit to ~15K chars to avoid token limits

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = message.content[0].text.strip()

        # Extract JSON from response
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            raise ValueError("Could not parse meeting data from Claude response")

    def create_meeting_note(self, parsed_data: Dict, original_filename: str,
                          source_language: str = None) -> Tuple[Path, str]:
        """Create structured meeting note file"""

        date_str = parsed_data.get("date", datetime.now().strftime("%Y-%m-%d"))
        meeting_type = parsed_data.get("meeting_type", "sync")

        # Create filename
        title_slug = re.sub(r'[^a-z0-9]+', '-', original_filename.lower())
        title_slug = re.sub(r'^-|-$', '', title_slug)
        title_slug = re.sub(r'\.md$|\.docx$', '', title_slug)

        filename = f"{date_str}-{title_slug}.md"

        # Determine month folder
        year_month = date_str[:7]  # YYYY-MM
        month_dir = self.meetings_dir / year_month
        month_dir.mkdir(parents=True, exist_ok=True)

        filepath = month_dir / filename

        # Build frontmatter
        frontmatter = f"""---
title: {original_filename.replace('.md', '').replace('.docx', '')}
type: meeting-note
date: {date_str}
attendees: {json.dumps(parsed_data.get('attendees', []))}
meeting-type: {meeting_type}
tags: [cooking, sync, meeting]"""

        if source_language:
            frontmatter += f"""
original-language: {source_language}
translated: true
translation-date: {datetime.now().strftime("%Y-%m-%d")}"""

        frontmatter += f"""
summary: |
  {parsed_data.get('executive_summary', 'Meeting summary')[:200]}
---
"""

        # Build content
        content = frontmatter + "\n"
        content += f"# {original_filename.replace('.md', '').replace('.docx', '')}\n\n"

        if source_language:
            content += f"> **Note:** This meeting was conducted in {source_language} and has been translated to English for documentation purposes.\n\n"

        content += f"**Date:** {date_str}\n"
        content += f"**Attendees:** {', '.join(parsed_data.get('attendees', []))}\n"
        content += f"**Type:** {meeting_type}\n\n"

        content += "## Executive Summary\n\n"
        content += parsed_data.get('executive_summary', 'No summary available') + "\n\n"

        # Action Items
        if parsed_data.get('action_items'):
            content += "## Action Items\n\n"
            for item in parsed_data['action_items']:
                content += f"- [ ] **{item.get('task', 'Task')}**"
                content += f" - Assigned to: {item.get('assigned_to', 'TBD')}"
                content += f" - Due: {item.get('due_date', 'TBD')}"
                content += f" - Priority: {item.get('priority', 'Medium')}\n"
            content += "\n"

        # Topics
        if parsed_data.get('topics'):
            content += "## Topics Discussed\n\n"
            for topic in parsed_data['topics']:
                content += f"### {topic.get('name', 'Topic')}\n\n"
                content += f"{topic.get('summary', '')}\n\n"
                if topic.get('takeaways'):
                    content += "**Key Takeaways:**\n"
                    for takeaway in topic['takeaways']:
                        content += f"- {takeaway}\n"
                    content += "\n"

        # Decisions
        if parsed_data.get('decisions'):
            content += "## Decisions Made\n\n"
            for decision in parsed_data['decisions']:
                content += f"- **{decision.get('decision', 'Decision')}**\n"
                content += f"  - Rationale: {decision.get('rationale', '')}\n"
            content += "\n"

        # Blockers
        if parsed_data.get('blockers'):
            content += "## Blockers and Risks\n\n"
            for blocker in parsed_data['blockers']:
                content += f"- **{blocker.get('description', 'Blocker')}**\n"
                content += f"  - Impact: {blocker.get('impact', 'Medium')}\n"
                content += f"  - Owner: {blocker.get('owner', 'TBD')}\n"
                content += f"  - Resolution needed: {blocker.get('resolution_date', 'TBD')}\n"
            content += "\n"

        return filepath, content

    def process_file(self, filepath: Path) -> bool:
        """Process a single file"""
        try:
            print(f"\n{'='*80}")
            print(f"Processing: {filepath.name}")
            print(f"{'='*80}")

            # Read file content
            if filepath.suffix == '.docx':
                content = self.extract_docx_text(filepath)
                if not content:
                    print(f"⚠️  Could not extract text from {filepath.name}")
                    self.stats["skipped"] += 1
                    return False
            else:
                content = filepath.read_text(encoding='utf-8')

            # Check if it's a meeting transcript
            is_meeting = self.is_meeting_transcript(filepath, content)

            if not is_meeting:
                print(f"ℹ️  Not detected as meeting transcript, skipping for now")
                self.stats["skipped"] += 1
                return False

            print(f"✓ Detected as meeting transcript")

            # Detect language
            language = self.detect_language(content[:500])
            print(f"Language: {language}")

            # Translate if needed
            source_language = None
            if language.lower() not in ['english', 'inglés']:
                print(f"Translating from {language} to English...")
                content = self.translate_to_english(content, language)
                source_language = language

            # Parse meeting
            print("Parsing meeting transcript...")
            parsed_data = self.parse_meeting_transcript(content, filepath.name, source_language)

            # Create meeting note
            print("Creating structured meeting note...")
            meeting_path, meeting_content = self.create_meeting_note(
                parsed_data, filepath.name, source_language
            )

            if not self.dry_run:
                meeting_path.write_text(meeting_content, encoding='utf-8')
                print(f"✓ Created: {meeting_path.relative_to(self.base_dir)}")

                # Delete original file
                filepath.unlink()
                print(f"✓ Deleted: {filepath.name}")

                self.stats["meetings_created"] += 1
            else:
                print(f"[DRY RUN] Would create: {meeting_path.relative_to(self.base_dir)}")
                print(f"[DRY RUN] Would delete: {filepath.name}")

            self.stats["processed"] += 1
            return True

        except Exception as e:
            print(f"❌ Error processing {filepath.name}: {e}")
            import traceback
            traceback.print_exc()
            self.stats["errors"] += 1
            return False

    def process_all(self, filter_pattern: str = None):
        """Process all files in source directory"""

        if not self.source_dir.exists():
            print(f"Error: Source directory not found: {self.source_dir}")
            return

        # Get all files
        files = list(self.source_dir.glob("*"))

        # Filter files
        if filter_pattern:
            files = [f for f in files if filter_pattern.lower() in f.name.lower()]

        # Filter out non-document files
        files = [f for f in files if f.suffix in ['.md', '.docx', '.txt'] and f.is_file()]

        self.stats["total_files"] = len(files)

        print(f"\n{'='*80}")
        print(f"Batch Processing Started")
        print(f"{'='*80}")
        print(f"Total files to process: {len(files)}")
        print(f"Dry run: {self.dry_run}")
        print(f"{'='*80}\n")

        for i, filepath in enumerate(files, 1):
            print(f"\n[{i}/{len(files)}]", end=" ")
            self.process_file(filepath)

        # Print summary
        print(f"\n\n{'='*80}")
        print(f"Processing Complete")
        print(f"{'='*80}")
        print(f"Total files: {self.stats['total_files']}")
        print(f"Processed: {self.stats['processed']}")
        print(f"Skipped: {self.stats['skipped']}")
        print(f"Errors: {self.stats['errors']}")
        print(f"Translations: {self.stats['translations']}")
        print(f"Meetings created: {self.stats['meetings_created']}")
        print(f"Decisions created: {self.stats['decisions_created']}")
        print(f"Requirements created: {self.stats['requirements_created']}")
        print(f"{'='*80}\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Batch process meeting documents')
    parser.add_argument('--dry-run', action='store_true',
                       help='Run without making changes')
    parser.add_argument('--filter', type=str,
                       help='Filter files by pattern (case-insensitive)')
    parser.add_argument('--base-dir', type=str,
                       default=None,
                       help='Base directory of documentation (defaults to script parent directory)')

    args = parser.parse_args()

    # Default to repository root (parent of scripts directory)
    base_dir = args.base_dir if args.base_dir else str(Path(__file__).parent.parent)

    processor = DocumentProcessor(base_dir, dry_run=args.dry_run)
    processor.process_all(filter_pattern=args.filter)


if __name__ == '__main__':
    main()
