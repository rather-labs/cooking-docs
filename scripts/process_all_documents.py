#!/usr/bin/env python3
"""
Document Processing Script for Cooking.gg Documentation
Processes 128 documents from 08-documents-to-parse/ and converts them into structured documentation.
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Base paths - use script location to find repo root
BASE_DIR = Path(__file__).parent.parent
DOCS_TO_PARSE = BASE_DIR / "08-documents-to-parse"
CONVERTED_DIR = DOCS_TO_PARSE / "converted"

class DocumentProcessor:
    def __init__(self):
        self.docs_converted = []
        self.docs_root = []
        self.translation_count = {"Spanish": 0, "English": 0}
        self.meeting_count = 0
        self.technical_count = 0
        self.business_count = 0
        self.operational_count = 0
        self.next_adr = 2  # Start from ADR-002

    def scan_documents(self):
        """Scan and categorize all documents"""
        # Scan converted folder
        if CONVERTED_DIR.exists():
            for file in CONVERTED_DIR.glob("*.md"):
                self.docs_converted.append(file)

        # Scan root folder
        for file in DOCS_TO_PARSE.glob("*.md"):
            if file.name != "process_all_documents.py":
                self.docs_root.append(file)

        print(f"Found {len(self.docs_converted)} files in converted/")
        print(f"Found {len(self.docs_root)} files in root")
        print(f"Total: {len(self.docs_converted) + len(self.docs_root)} documents to process")

    def detect_language(self, content: str) -> str:
        """Detect if content is in Spanish or English"""
        spanish_indicators = [
            "Notas de Gemini", "Resumen", "Detalles", "Transcripción",
            "Invitados", "Archivos adjuntos", "la reunión", "el lunes"
        ]

        for indicator in spanish_indicators:
            if indicator in content[:1000]:
                return "Spanish"
        return "English"

    def detect_meeting_transcript(self, filename: str, content: str) -> bool:
        """
        Detect if document is a meeting transcript
        Check both filename and content for timestamp patterns
        """
        # Check filename patterns
        filename_lower = filename.lower()
        meeting_patterns = ["sync", "meeting", "meet", "demo", "daily"]

        for pattern in meeting_patterns:
            if pattern in filename_lower:
                return True

        # Check content for timestamps in parentheses
        # Look for patterns like (14:30), (9:15), Name (14:30):
        timestamp_patterns = [
            r'\(\d{1,2}:\d{2}\)',  # (14:30)
            r'\(\d{1,2}:\d{2}:\d{2}\)',  # (14:30:45)
            r'\w+\s*\(\d{1,2}:\d{2}\)',  # Name (14:30)
        ]

        # Check first 1000 characters
        preview = content[:1000]
        timestamp_count = 0

        for pattern in timestamp_patterns:
            matches = re.findall(pattern, preview)
            timestamp_count += len(matches)

        # If 2 or more timestamps found, it's a meeting transcript
        if timestamp_count >= 2:
            return True

        return False

    def extract_date_from_filename(self, filename: str) -> Optional[str]:
        """Extract date from various filename patterns"""
        # Pattern 1: 2025_07_09 format
        match = re.search(r'(\d{4})_(\d{2})_(\d{2})', filename)
        if match:
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

        # Pattern 2: 20250825 format
        match = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
        if match:
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

        # Pattern 3: Already in YYYY-MM-DD format
        match = re.search(r'(\d{4})-(\d{2})-(\d{2})', filename)
        if match:
            return match.group(0)

        return None

    def categorize_document(self, filename: str, content: str) -> str:
        """Determine document category"""
        filename_lower = filename.lower()
        content_lower = content.lower()[:2000]

        # Check for meeting transcript first
        if self.detect_meeting_transcript(filename, content):
            return "meeting"

        # Technical documentation indicators
        technical_patterns = [
            "api", "architecture", "technical", "integration", "backend",
            "frontend", "infrastructure", "deployment", "devops", "indexer"
        ]
        for pattern in technical_patterns:
            if pattern in filename_lower or pattern in content_lower:
                return "technical"

        # Business documentation indicators
        business_patterns = [
            "roadmap", "prd", "product", "requirements", "market", "user",
            "research", "competitive", "analysis"
        ]
        for pattern in business_patterns:
            if pattern in filename_lower or pattern in content_lower:
                return "business"

        # Operational documentation indicators
        operational_patterns = [
            "process", "runbook", "procedure", "workflow", "guide"
        ]
        for pattern in operational_patterns:
            if pattern in filename_lower or pattern in content_lower:
                return "operational"

        # Default to business if unclear
        return "business"

    def list_all_documents(self):
        """Create a manifest of all documents to process"""
        manifest = []

        for file in self.docs_converted + self.docs_root:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

            language = self.detect_language(content)
            category = self.categorize_document(file.name, content)
            date = self.extract_date_from_filename(file.name)

            manifest.append({
                "path": str(file),
                "filename": file.name,
                "category": category,
                "language": language,
                "date": date,
                "size": len(content)
            })

        return manifest

def main():
    processor = DocumentProcessor()
    processor.scan_documents()

    print("\n" + "="*80)
    print("DOCUMENT PROCESSING MANIFEST")
    print("="*80 + "\n")

    manifest = processor.list_all_documents()

    # Group by category
    by_category = {}
    for doc in manifest:
        cat = doc["category"]
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(doc)

    # Print summary
    print(f"Total Documents: {len(manifest)}\n")

    for category, docs in by_category.items():
        print(f"\n{category.upper()} ({len(docs)} documents):")
        print("-" * 80)

        spanish_count = len([d for d in docs if d["language"] == "Spanish"])
        english_count = len([d for d in docs if d["language"] == "English"])

        print(f"  Spanish: {spanish_count} | English: {english_count}")
        print(f"  Files:")
        for doc in docs[:5]:  # Show first 5 as examples
            print(f"    - {doc['filename'][:60]}... [{doc['language']}]")
        if len(docs) > 5:
            print(f"    ... and {len(docs) - 5} more")

    # Export to JSON for processing
    import json
    manifest_file = DOCS_TO_PARSE / "processing_manifest.json"
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n\nManifest saved to: {manifest_file}")
    print("\nThis manifest will be used to process all documents systematically.")

if __name__ == "__main__":
    main()
