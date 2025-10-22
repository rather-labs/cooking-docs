#!/usr/bin/env python3
"""
Update meetings index based on processed meeting files.
"""

import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Use script location to find repo root
BASE_DIR = Path(__file__).parent.parent
MEETINGS_DIR = BASE_DIR / "06-meetings"
INDEX_FILE = MEETINGS_DIR / "_meetings-index.md"

# Meeting subdirectories
MEETING_TYPES = {
    'daily-standups': 'Daily Standups',
    'demos': 'Demo Meetings',
    'mobile': 'Mobile Planning',
    'sync-meetings': 'Z & Lucas Sync Meetings',
    'technical': 'Technical Discussions',
    'other': 'Other Meetings'
}

def collect_meeting_files():
    """Collect all meeting markdown files from month-based directories"""
    all_meetings = []

    # Find all YYYY-MM directories
    for month_dir in sorted(MEETINGS_DIR.glob("2025-*")):
        if month_dir.is_dir():
            files = sorted(month_dir.glob("*.md"))
            for file in files:
                if not file.name.startswith('_'):
                    all_meetings.append({
                        'path': file,
                        'name': file.stem,
                        'month': month_dir.name,
                        'relative_path': f"{month_dir.name}/{file.name}"
                    })

    # Categorize by type based on filename
    meetings_by_type = defaultdict(list)
    for meeting in all_meetings:
        name = meeting['name'].lower()
        if 'daily-standup' in name or 'daily-cookinggg' in name:
            meetings_by_type['daily-standups'].append(meeting)
        elif 'demo' in name:
            meetings_by_type['demos'].append(meeting)
        elif 'mobile' in name:
            meetings_by_type['mobile'].append(meeting)
        elif 'sync-z-lucas' in name or 'sync' in name:
            meetings_by_type['sync-meetings'].append(meeting)
        elif any(word in name for word in ['devops', 'echo', 'hl', 'indexer', 'tradingview', 'filters']):
            meetings_by_type['technical'].append(meeting)
        else:
            meetings_by_type['other'].append(meeting)

    return meetings_by_type

def generate_index(meetings_by_type):
    """Generate updated meetings index"""

    total_meetings = sum(len(meetings) for meetings in meetings_by_type.values())

    # Get date range
    all_files = []
    for meetings in meetings_by_type.values():
        all_files.extend([m['name'] for m in meetings])

    dates = []
    for filename in all_files:
        parts = filename.split('-')
        if len(parts) >= 3 and parts[0].isdigit():
            dates.append(f"{parts[0]}-{parts[1]}-{parts[2]}")

    dates.sort()
    date_range = f"{dates[0] if dates else 'N/A'} to {dates[-1] if dates else 'N/A'}"

    markdown = f"""---
title: Meetings Index
type: index
date: {datetime.now().strftime('%Y-%m-%d')}
last-updated: {datetime.now().strftime('%Y-%m-%d')}
status: active
summary: |
  Index of all project meeting notes organized by type and date. Contains {total_meetings} meeting
  records auto-generated from Google Gemini meeting notes.
---

# Meetings Index

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

## Overview

This directory contains structured meeting notes processed from Google Gemini auto-generated meeting transcripts. All meetings have been categorized by type and organized for easy reference.

## Statistics

- **Total Meetings:** {total_meetings}
- **Date Range:** {date_range}
- **Meeting Types:**
"""

    # Add type counts
    for type_dir, type_name in MEETING_TYPES.items():
        count = len(meetings_by_type.get(type_dir, []))
        if count > 0:
            markdown += f"  - {type_name}: {count}\n"

    markdown += "\n## Recent Meetings (Last 10)\n\n"
    markdown += "| Date | Meeting | Type | Link |\n"
    markdown += "|------|---------|------|------|\n"

    # Get most recent 10 meetings across all types
    all_meetings = []
    for type_dir, meetings in meetings_by_type.items():
        for meeting in meetings:
            all_meetings.append({
                **meeting,
                'type': MEETING_TYPES[type_dir],
                'type_dir': type_dir
            })

    all_meetings.sort(key=lambda x: x['name'], reverse=True)

    for meeting in all_meetings[:10]:
        parts = meeting['name'].split('-', 3)
        date = f"{parts[0]}-{parts[1]}-{parts[2]}"
        title = parts[3].replace('-', ' ').title() if len(parts) > 3 else "Meeting"
        markdown += f"| {date} | {title} | {meeting['type']} | [{meeting['name'][:50]}...]({meeting['relative_path']}) |\n"

    markdown += "\n## Meetings by Type\n\n"

    # Daily Standups
    if 'daily-standups' in meetings_by_type:
        standups = meetings_by_type['daily-standups']
        markdown += f"### Daily Standups ({len(standups)} total)\n\n"
        markdown += "Regular team standups tracking daily progress and blockers.\n\n"

        # Group by month
        by_month = defaultdict(list)
        for meeting in standups:
            parts = meeting['name'].split('-')
            month_key = f"{parts[0]}-{parts[1]}"
            by_month[month_key].append(meeting)

        for month in sorted(by_month.keys(), reverse=True):
            month_meetings = by_month[month]
            month_name = datetime.strptime(month, '%Y-%m').strftime('%B %Y')
            markdown += f"\n**{month_name}** ({len(month_meetings)} meetings)\n"
            links = [f"[{m['name'][:10]}]({m['relative_path']})" for m in sorted(month_meetings, key=lambda x: x['name'], reverse=True)[:5]]
            markdown += "- " + " | ".join(links)
            if len(month_meetings) > 5:
                markdown += f" ... and {len(month_meetings) - 5} more"
            markdown += "\n"

    # Demo Meetings
    if 'demos' in meetings_by_type:
        demos = meetings_by_type['demos']
        markdown += f"\n### Demo Meetings ({len(demos)} total)\n\n"
        markdown += "Weekly demonstration and progress review meetings.\n\n"
        markdown += "| Date | Link |\n"
        markdown += "|------|------|\n"
        for meeting in sorted(demos, key=lambda x: x['name'], reverse=True)[:15]:
            date = '-'.join(meeting['name'].split('-')[:3])
            markdown += f"| {date} | [{meeting['name'][:40]}...]({meeting['relative_path']}) |\n"

    # Sync Meetings
    if 'sync-meetings' in meetings_by_type:
        syncs = meetings_by_type['sync-meetings']
        markdown += f"\n### Z & Lucas Sync Meetings ({len(syncs)} total)\n\n"
        markdown += "Regular sync meetings between Z and Lucas discussing project strategy and priorities.\n\n"
        markdown += "| Date | Link |\n"
        markdown += "|------|------|\n"
        for meeting in sorted(syncs, key=lambda x: x['name'], reverse=True):
            date = '-'.join(meeting['name'].split('-')[:3])
            markdown += f"| {date} | [{meeting['name'][:40]}...]({meeting['relative_path']}) |\n"

    # Mobile Meetings
    if 'mobile' in meetings_by_type:
        mobile = meetings_by_type['mobile']
        markdown += f"\n### Mobile Planning Meetings ({len(mobile)} total)\n\n"
        markdown += "Planning and discussion meetings for mobile app development.\n\n"
        markdown += "| Date | Link |\n"
        markdown += "|------|------|\n"
        for meeting in sorted(mobile, key=lambda x: x['name'], reverse=True):
            date = '-'.join(meeting['name'].split('-')[:3])
            markdown += f"| {date} | [{meeting['name'][:40]}...]({meeting['relative_path']}) |\n"

    # Technical Discussions
    if 'technical' in meetings_by_type:
        technical = meetings_by_type['technical']
        markdown += f"\n### Technical Discussions ({len(technical)} total)\n\n"
        markdown += "Technical planning, architecture, and integration discussions.\n\n"
        markdown += "| Date | Topic | Link |\n"
        markdown += "|------|-------|------|\n"
        for meeting in sorted(technical, key=lambda x: x['name'], reverse=True):
            date = '-'.join(meeting['name'].split('-')[:3])
            topic = '-'.join(meeting['name'].split('-')[3:]).replace('-', ' ').title()[:30]
            markdown += f"| {date} | {topic} | [{meeting['name'][:30]}...]({meeting['relative_path']}) |\n"

    # Other Meetings
    if 'other' in meetings_by_type:
        other = meetings_by_type['other']
        markdown += f"\n### Other Meetings ({len(other)} total)\n\n"
        markdown += "Miscellaneous meetings including planning sessions, interviews, and special topics.\n\n"
        markdown += "| Date | Topic | Link |\n"
        markdown += "|------|-------|------|\n"
        for meeting in sorted(other, key=lambda x: x['name'], reverse=True):
            date = '-'.join(meeting['name'].split('-')[:3])
            topic = '-'.join(meeting['name'].split('-')[3:]).replace('-', ' ').title()[:40]
            markdown += f"| {date} | {topic} | [{meeting['name'][:30]}...]({meeting['relative_path']}) |\n"

    markdown += """
## How to Use This Directory

### Meeting Organization

Meetings are organized chronologically in month-based subdirectories:
- `2025-05/` - May 2025 meetings
- `2025-06/` - June 2025 meetings
- `2025-07/` - July 2025 meetings
- `2025-08/` - August 2025 meetings
- `2025-09/` - September 2025 meetings
- `2025-10/` - October 2025 meetings

Meeting types are identified by filename patterns.

### File Naming Convention

Files follow the pattern: `YYYY-MM-DD-topic-description.md`

Examples:
- `2025-10-17-daily-standup.md` - Daily standup
- `2025-10-17-cooking-demo.md` - Demo meeting
- `2025-10-13-Sync-Z-Lucas.md` - Sync meeting

### Meeting Note Structure

Each meeting note includes:
- YAML frontmatter with metadata
- Meeting date and type
- List of attendees
- Executive summary
- Key discussion points
- Action items
- Links to related documents

## Template

Use [_template-meeting.md](_template-meeting.md) to create new meeting notes manually.

## Best Practices

- **Document within 24 hours** of meeting
- **Extract decisions** to [ADRs](../02-decisions/)
- **Track action items** in project management system
- **Link to relevant documents** in the knowledge base
- **Use consistent date format** (YYYY-MM-DD)
- **Tag appropriately** for discoverability

## Source Information

These meeting notes were auto-generated by Google Gemini during live meetings and then processed into structured markdown format. Original .docx files have been archived.

## Related Documents

- [Decisions](../02-decisions/) - Formal architectural and technical decision records
- [Current Status](../03-active-work/_current-status.md) - Current project status
- [Project Index](../00-PROJECT-INDEX.md) - Main project navigation
- [Glossary](../01-foundation/glossary.md) - Project terminology

---

**Maintenance Notes:**
- **Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
- **Next Review:** {(datetime.now().replace(day=1).month + 1) if datetime.now().month < 12 else 1}/{datetime.now().year if datetime.now().month < 12 else datetime.now().year + 1}
- **Maintainer:** Project Team
"""

    return markdown

def main():
    print("Generating meetings index...")
    meetings_by_type = collect_meeting_files()

    total = sum(len(m) for m in meetings_by_type.values())
    print(f"Found {total} meeting files:")
    for type_dir, meetings in meetings_by_type.items():
        print(f"  {MEETING_TYPES[type_dir]}: {len(meetings)}")

    markdown = generate_index(meetings_by_type)

    INDEX_FILE.write_text(markdown, encoding='utf-8')
    print(f"\n✅ Index updated: {INDEX_FILE}")

if __name__ == "__main__":
    main()
