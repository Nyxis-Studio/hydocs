#!/usr/bin/env python3
"""
Custom Documentation Migration Script
Converts old format custom docs to the new format.
"""

import os
import sys
import re
from pathlib import Path
from typing import Optional

def migrate_file(file_path: str, dry_run: bool = False) -> tuple[bool, str]:
    """
    Migrates a single custom documentation file from old to new format.

    Returns:
        (success, message)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return (False, f"Failed to read file: {e}")

    lines = []

    # Extract overview
    overview_match = re.search(r'## Overview\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if overview_match:
        overview = overview_match.group(1).strip()
        # Convert bullet points to prose
        if overview.startswith('-'):
            overview_lines = [line.strip('- ').strip() for line in overview.split('\n') if line.strip().startswith('-')]
            # Remove generic lines
            overview_lines = [line for line in overview_lines if
                             not line.startswith('Documentation for') and
                             not line.startswith('Declared as')]
            if overview_lines:
                overview = ' '.join(overview_lines)
            else:
                overview = None

        if overview and len(overview) > 10:
            lines.append("## Overview")
            lines.append(overview)
            lines.append("")

    # Extract field descriptions (if exists)
    # Note: Old format might have fields in various formats

    # Extract constructor descriptions
    ctor_match = re.search(r'## Constructors\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if ctor_match:
        ctor_content = ctor_match.group(1).strip()
        if ctor_content and ctor_content != "- None." and ctor_content.lower() != "none.":
            # Parse old format constructors
            ctor_lines = []
            for line in ctor_content.split('\n'):
                line = line.strip()
                if line.startswith('-'):
                    # Extract constructor signature
                    match = re.match(r'-\s+`?([^`]+)`?', line)
                    if match:
                        sig = match.group(1).strip()
                        # Skip generic descriptions
                        if 'Executes' not in line and 'behavior' not in line:
                            ctor_lines.append(f"- `{sig}`: [Add description]")

            if ctor_lines:
                lines.append("## Constructor Descriptions")
                lines.extend(ctor_lines)
                lines.append("")

    # Extract method descriptions
    method_match = re.search(r'## Methods\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if method_match:
        method_content = method_match.group(1).strip()
        if method_content and method_content.lower() != "none.":
            # Parse old format methods
            method_lines = []
            current_method = None

            for line in method_content.split('\n'):
                line = line.strip()
                if line.startswith('-') and not line.startswith('  -'):
                    # Method signature
                    match = re.match(r'-\s+`?([^`]+)`?', line)
                    if match:
                        sig = match.group(1).strip()
                        # Check if there's a description on the same line
                        if ':' in line:
                            # Has inline description
                            parts = line.split(':', 1)
                            if len(parts) == 2:
                                desc = parts[1].strip()
                                # Skip generic descriptions
                                if 'Executes' not in desc and 'behavior' not in desc:
                                    method_lines.append(f"- `{sig}`: {desc}")
                                else:
                                    method_lines.append(f"- `{sig}`: [Add description]")
                        else:
                            current_method = sig
                elif line.startswith('  -') and current_method:
                    # Sub-description for current method
                    desc = line.strip('- ').strip()
                    if 'Executes' not in desc and 'behavior' not in desc:
                        method_lines.append(f"- `{current_method}`: {desc}")
                    else:
                        method_lines.append(f"- `{current_method}`: [Add description]")
                    current_method = None

            if method_lines:
                lines.append("## Method Descriptions")
                lines.extend(method_lines)
                lines.append("")

    # Extract notes
    notes_match = re.search(r'## Notes\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if notes_match:
        notes = notes_match.group(1).strip()
        if notes and notes.lower() != "no additional notes." and notes.lower() != "- no additional notes.":
            lines.append("## Usage Notes")
            lines.append(notes)
            lines.append("")

    # If no content was extracted, return failure
    if not lines:
        return (False, "No useful content to migrate")

    new_content = '\n'.join(lines)

    if dry_run:
        return (True, f"Would migrate to:\n{new_content}")

    # Write new content
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return (True, "Migrated successfully")
    except Exception as e:
        return (False, f"Failed to write file: {e}")

def migrate_directory(docs_dir: str, dry_run: bool = False, verbose: bool = False):
    """Migrates all custom documentation files in a directory."""
    total = 0
    success = 0
    failed = 0
    skipped = 0

    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                total += 1

                # Check if already in new format
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Skip if already migrated
                    if not content.strip().startswith('#') or re.search(r'^## Overview\s*\n[^-]', content, re.MULTILINE):
                        if verbose:
                            print(f"Skip (already migrated): {file_path}")
                        skipped += 1
                        continue
                except:
                    pass

                ok, msg = migrate_file(file_path, dry_run)

                if ok:
                    success += 1
                    if verbose:
                        print(f"✓ {file_path}")
                        if dry_run:
                            print(f"  {msg}")
                else:
                    failed += 1
                    if verbose:
                        print(f"✗ {file_path}: {msg}")

    print(f"\nMigration {'Preview' if dry_run else 'Complete'}:")
    print(f"  Total files: {total}")
    print(f"  Migrated: {success}")
    print(f"  Failed: {failed}")
    print(f"  Skipped: {skipped}")

    if dry_run:
        print(f"\nRun without --dry-run to apply changes")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Migrate custom docs to new format")
    parser.add_argument("--docs", "-d", default="docs", help="Custom docs directory (default: docs)")
    parser.add_argument("--file", "-f", help="Migrate a single file")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")

    args = parser.parse_args()

    if args.file:
        # Migrate single file
        if not os.path.exists(args.file):
            print(f"Error: File not found: {args.file}")
            sys.exit(1)

        ok, msg = migrate_file(args.file, args.dry_run)
        print(f"{'Preview' if args.dry_run else 'Result'}: {msg}")
        sys.exit(0 if ok else 1)

    # Migrate all files
    if not os.path.exists(args.docs):
        print(f"Error: Directory not found: {args.docs}")
        sys.exit(1)

    print(f"Migrating custom documentation in: {args.docs}")
    if args.dry_run:
        print("DRY RUN MODE - No files will be modified\n")

    migrate_directory(args.docs, args.dry_run, args.verbose)

if __name__ == "__main__":
    main()
