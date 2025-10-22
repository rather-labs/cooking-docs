#!/usr/bin/env python3
"""
Process project documentation from 08-documents-to-parse folder.
Organizes C-series documents and other project files into appropriate locations.
"""

import os
import re
from pathlib import Path
from datetime import datetime
import shutil

# Paths - use script location to find repo root
BASE_DIR = Path(__file__).parent.parent
DOCS_TO_PARSE = BASE_DIR / "08-documents-to-parse"

# Document categorization patterns
CATEGORIES = {
    'strategic': {
        'pattern': r'^C1\d{2}',
        'target': '03-active-work/strategy',
        'description': 'Strategic planning and vision documents'
    },
    'features': {
        'pattern': r'^C2\d{2}',
        'target': '04-knowledge-base/features',
        'description': 'Feature specifications and technical designs'
    },
    'referral': {
        'pattern': r'^C3\d{2}',
        'target': '04-knowledge-base/referral-program',
        'description': 'Referral program documentation'
    },
    'mobile': {
        'pattern': r'^C4\d{2}',
        'target': '04-knowledge-base/mobile',
        'description': 'Mobile app specifications and requirements'
    },
    'sync-meetings': {
        'pattern': r'Cooking.*Sync',
        'target': '06-meetings/sync-meetings',
        'description': 'Sync meeting notes'
    },
    'documentation': {
        'pattern': r'(Documentation|GitBook|PRD|Requirements)',
        'target': '04-knowledge-base/documentation',
        'description': 'User documentation and requirements'
    },
    'reference': {
        'pattern': r'(Reserved)',
        'target': '04-knowledge-base/reference',
        'description': 'Reference materials'
    }
}

def categorize_document(filename):
    """Determine category for a document based on filename"""
    for category, config in CATEGORIES.items():
        if re.search(config['pattern'], filename, re.IGNORECASE):
            return category, config['target']
    return None, None

def extract_metadata(content, filename):
    """Extract metadata from document frontmatter"""
    metadata = {
        'title': filename.replace('.md', ''),
        'creation_date': None,
        'tags': [],
        'related_notes': []
    }

    # Extract YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 2:
            frontmatter = parts[1]

            # Extract creation date
            date_match = re.search(r'Creation Date:\s*(.+)', frontmatter)
            if date_match:
                metadata['creation_date'] = date_match.group(1).strip()

            # Extract tags
            tags_match = re.search(r'tags:\s*\n((?:  - .+\n?)+)', frontmatter)
            if tags_match:
                tags_text = tags_match.group(1)
                metadata['tags'] = [t.strip('- ').strip() for t in tags_text.split('\n') if t.strip()]

    return metadata

def add_knowledge_base_links(content, filename):
    """Add navigation links at bottom of document"""

    links = """

---

**Related Documentation:**
- [Project Index](../../00-PROJECT-INDEX.md)
- [Knowledge Base](../_index.md)
- [Meetings](../../06-meetings/_meetings-index.md)

---

*Imported: {}*
*Source: 08-documents-to-parse/{}*
""".format(datetime.now().strftime('%Y-%m-%d'), filename)

    return content + links

def process_documents():
    """Main processing function"""
    print("Starting project documentation processing...")
    print(f"Scanning {DOCS_TO_PARSE}")

    # Get all .md files
    md_files = list(DOCS_TO_PARSE.glob("*.md"))
    print(f"Found {len(md_files)} markdown files to process\n")

    # Statistics
    stats = {
        'processed': 0,
        'skipped': 0,
        'by_category': {}
    }

    for md_file in md_files:
        try:
            print(f"Processing: {md_file.name}")

            # Skip hidden files
            if md_file.name.startswith('.'):
                stats['skipped'] += 1
                continue

            # Read content
            content = md_file.read_text(encoding='utf-8')

            # Categorize
            category, target_path = categorize_document(md_file.name)

            if not category:
                print(f"  ⚠️  No category match for {md_file.name}, skipping")
                stats['skipped'] += 1
                continue

            # Extract metadata
            metadata = extract_metadata(content, md_file.name)

            print(f"  Category: {category}")
            print(f"  Target: {target_path}")

            # Create target directory
            target_dir = BASE_DIR / target_path
            target_dir.mkdir(parents=True, exist_ok=True)

            # Add navigation links
            enhanced_content = add_knowledge_base_links(content, md_file.name)

            # Determine target filename (keep original name)
            target_file = target_dir / md_file.name

            # Write file
            target_file.write_text(enhanced_content, encoding='utf-8')
            print(f"  ✅ Created: {target_file}")

            # Update stats
            stats['processed'] += 1
            stats['by_category'][category] = stats['by_category'].get(category, 0) + 1

        except Exception as e:
            print(f"  ❌ Error processing {md_file.name}: {e}")
            stats['skipped'] += 1

    # Summary
    print(f"\n{'='*60}")
    print(f"Processing Complete!")
    print(f"{'='*60}")
    print(f"✅ Processed: {stats['processed']}")
    print(f"⚠️  Skipped: {stats['skipped']}")
    print(f"\nBy Category:")
    for category, count in sorted(stats['by_category'].items()):
        print(f"  {category}: {count}")
    print(f"{'='*60}\n")

    return stats

if __name__ == "__main__":
    process_documents()
