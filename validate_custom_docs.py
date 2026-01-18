#!/usr/bin/env python3
"""
Custom Documentation Validator
Checks if custom documentation files follow the new format.
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

class ValidationResult:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.suggestions: List[str] = []

def validate_custom_doc(file_path: str) -> ValidationResult:
    """Validates a single custom documentation file."""
    result = ValidationResult(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        result.errors.append(f"Failed to read file: {e}")
        return result

    # Check for old format indicators
    if content.strip().startswith('# '):
        result.errors.append("File starts with class title (# ClassName) - this is old format")
        result.suggestions.append("Remove the class title line - only include section headers (##)")

    if re.search(r'^## Declaration', content, re.MULTILINE):
        result.errors.append("Contains ## Declaration section - this is structural duplication")
        result.suggestions.append("Remove declaration section - it's auto-generated")

    if re.search(r'^## Methods\s*$', content, re.MULTILINE):
        result.warnings.append("Has generic ## Methods section - should be ## Method Descriptions")
        result.suggestions.append("Rename to ## Method Descriptions")

    if re.search(r'^## Constructors\s*$', content, re.MULTILINE):
        result.warnings.append("Has generic ## Constructors section - should be ## Constructor Descriptions")
        result.suggestions.append("Rename to ## Constructor Descriptions")

    if re.search(r'^## Fields\s*$', content, re.MULTILINE):
        result.warnings.append("Has generic ## Fields section - should be ## Field Descriptions")
        result.suggestions.append("Rename to ## Field Descriptions")

    # Check for valid sections
    has_overview = bool(re.search(r'^## Overview', content, re.MULTILINE))
    has_any_content = bool(re.search(r'^## (Overview|Field Descriptions|Constructor Descriptions|Method Descriptions|Usage Notes|Examples)', content, re.MULTILINE))

    if not has_any_content:
        result.errors.append("No valid sections found - file appears to be in old format or empty")
        result.suggestions.append("Use new format with ## Overview, ## Method Descriptions, etc.")

    # Check for generic descriptions
    generic_patterns = [
        (r'Executes \w+ behavior', 'Generic "Executes X behavior" found'),
        (r'Documentation for `\w+`', 'Generic "Documentation for X" found'),
        (r'Declared as a \w+ in', 'Generic "Declared as" found'),
    ]

    for pattern, msg in generic_patterns:
        if re.search(pattern, content):
            result.warnings.append(msg)
            result.suggestions.append("Replace generic descriptions with specific, useful information")

    # Check method description format
    method_section = re.search(r'## Method Descriptions\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if method_section:
        method_content = method_section.group(1)
        # Check if using correct format: - `methodName(...)`: description
        if not re.search(r'-\s+`\w+\([^)]*\)`:', method_content):
            result.warnings.append("Method descriptions don't follow format: - `methodName()`: description")

    # Check field description format
    field_section = re.search(r'## Field Descriptions\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if field_section:
        field_content = field_section.group(1)
        if not re.search(r'-\s+`[A-Z_][A-Z0-9_]*`:', field_content):
            result.warnings.append("Field descriptions don't follow format: - `FIELD_NAME`: description")

    # Positive checks
    if has_overview:
        overview_match = re.search(r'## Overview\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if overview_match:
            overview_text = overview_match.group(1).strip()
            if len(overview_text) < 20:
                result.warnings.append("Overview is very short - consider adding more context")
            elif overview_text.startswith('-'):
                result.warnings.append("Overview uses bullet points - prefer prose description")

    return result

def validate_all_custom_docs(docs_dir: str) -> List[ValidationResult]:
    """Validates all custom documentation files in a directory."""
    results = []

    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                result = validate_custom_doc(file_path)
                results.append(result)

    return results

def print_results(results: List[ValidationResult]):
    """Prints validation results in a nice format."""
    total_files = len(results)
    files_with_errors = sum(1 for r in results if r.errors)
    files_with_warnings = sum(1 for r in results if r.warnings and not r.errors)
    files_clean = sum(1 for r in results if not r.errors and not r.warnings)

    print(f"\n{BLUE}{'='*80}{RESET}")
    print(f"{BLUE}Custom Documentation Validation Report{RESET}")
    print(f"{BLUE}{'='*80}{RESET}\n")

    print(f"Total files checked: {total_files}")
    print(f"{GREEN}✓ Clean: {files_clean}{RESET}")
    print(f"{YELLOW}⚠ Warnings: {files_with_warnings}{RESET}")
    print(f"{RED}✗ Errors: {files_with_errors}{RESET}\n")

    # Print detailed results
    for result in results:
        if not result.errors and not result.warnings:
            continue

        rel_path = os.path.relpath(result.file_path)

        if result.errors:
            print(f"{RED}✗ {rel_path}{RESET}")
        elif result.warnings:
            print(f"{YELLOW}⚠ {rel_path}{RESET}")

        for error in result.errors:
            print(f"  {RED}ERROR:{RESET} {error}")

        for warning in result.warnings:
            print(f"  {YELLOW}WARNING:{RESET} {warning}")

        if result.suggestions:
            print(f"  {BLUE}Suggestions:{RESET}")
            for suggestion in result.suggestions:
                print(f"    → {suggestion}")

        print()

    # Summary
    print(f"{BLUE}{'='*80}{RESET}")
    if files_with_errors == 0:
        print(f"{GREEN}✓ All files are valid!{RESET}")
    else:
        print(f"{RED}✗ {files_with_errors} file(s) need attention{RESET}")
    print(f"{BLUE}{'='*80}{RESET}\n")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate custom documentation format")
    parser.add_argument("--docs", "-d", default="docs", help="Custom docs directory (default: docs)")
    parser.add_argument("--file", "-f", help="Validate a single file")
    parser.add_argument("--quiet", "-q", action="store_true", help="Only show files with issues")

    args = parser.parse_args()

    if args.file:
        # Validate single file
        if not os.path.exists(args.file):
            print(f"{RED}Error: File not found: {args.file}{RESET}")
            sys.exit(1)

        result = validate_custom_doc(args.file)
        print_results([result])
        sys.exit(1 if result.errors else 0)

    # Validate all files
    if not os.path.exists(args.docs):
        print(f"{RED}Error: Directory not found: {args.docs}{RESET}")
        sys.exit(1)

    print(f"Validating custom documentation in: {args.docs}")
    results = validate_all_custom_docs(args.docs)

    if args.quiet:
        results = [r for r in results if r.errors or r.warnings]

    print_results(results)

    # Exit with error if any files have errors
    sys.exit(1 if any(r.errors for r in results) else 0)

if __name__ == "__main__":
    main()
