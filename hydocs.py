#!/usr/bin/env python3
"""
Hytale Docs Generator (hydocs)
A CLI tool to decompile the Hytale Server JAR and generate Markdown documentation for AI/LLM context.
"""

import os
import sys
import re
import json
import shutil
import argparse
import subprocess
import time
import threading
import hashlib
from datetime import datetime
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

# --- Configuration Constants ---
CFR_VERSION = "0.152"
CFR_JAR_NAME = f"cfr-{CFR_VERSION}.jar"
CFR_URL = f"https://www.benf.org/other/cfr/cfr-{CFR_VERSION}.jar"
BASE_PACKAGE = "com.hypixel.hytale"

# Detect CI environment (GitHub Actions, etc.)
IS_CI = os.environ.get('CI', '').lower() in ('true', '1', 'yes')

# --- Regex Patterns ---
PACKAGE_PATTERN = re.compile(r'package\s+([\w.]+)\s*;')
IMPORT_PATTERN = re.compile(r'import\s+(?:static\s+)?([\w.]+)(?:\.\*)?;')
CLASS_PATTERN = re.compile(
    r'(public\s+)?(abstract\s+)?(final\s+)?(static\s+)?'
    r'(class|interface|enum|@interface)\s+'
    r'(\w+)(?:<[^>]+>)?'
    r'(?:\s+extends\s+([\w.<>,\\s]+?))?'
    r'(?:\s+implements\s+([\w.<>,\\s]+?))?\s*\{'
)
METHOD_PATTERN = re.compile(
    r'^\s*(public|protected)?\s*'
    r'(static\s+)?(final\s+)?(abstract\s+)?(default\s+)?(synchronized\s+)?'
    r'(?:<([^>]+)>\s+)?'  # Generic type params
    r'([\w<>[\]\\,\s\?@]+?)\s+'
    r'(\w+)\s*'
    r'\(([^)]*)\)'
    r'(?:\s+throws\s+([\w,\s]+))?'
    r'\s*[{;]',
    re.MULTILINE
)
FIELD_PATTERN = re.compile(
    r'^\s*(public|protected)?\s*'
    r'(static\s+)?(final\s+)?(volatile\s+)?(transient\s+)?'
    r'([\w<>[\]\\,\s\?@]+?)\s+'
    r'(\w+)\s*'
    r'(?:=\s*[^;]+)?;',
    re.MULTILINE
)
ENUM_CONST_PATTERN = re.compile(r'^\s*([A-Z_][A-Z0-9_]*)\s*(?:\([^)]*\))?\s*[,;{]', re.MULTILINE)
TYPE_REFERENCE_PATTERN = re.compile(r'\b([A-Z][a-zA-Z0-9]*)\b')


# --- Data Structures ---
class JavaClass:
    def __init__(self):
        self.package = ""
        self.name = ""
        self.full_name = ""
        self.type = "class"
        self.modifiers = []
        self.extends = ""
        self.implements = []
        self.fields = []
        self.methods = []
        self.enum_constants = []
        self.imports = []
        self.source_file = ""
        self.output_file = ""
        self.source_hash = ""
        self.generated_at = ""

class JavaMethod:
    def __init__(self):
        self.name = ""
        self.return_type = ""
        self.parameters = []  # List of (type, name)
        self.modifiers = []
        self.throws = []
        self.generic_params = ""
        self.is_constructor = False

class JavaField:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.modifiers = []

class CustomDocs:
    """Parsed custom documentation content."""
    def __init__(self):
        self.overview = ""
        self.field_descriptions: Dict[str, str] = {}
        self.constructor_descriptions: Dict[str, str] = {}
        self.method_descriptions: Dict[str, str] = {}
        self.usage_notes = ""
        self.examples = ""

class ClassIndex:
    """Global index of all classes for link resolution."""
    def __init__(self):
        self.classes: Dict[str, str] = {}  # simple_name -> full_path
        self.full_names: Dict[str, str] = {}  # full_name -> file_path
        self.by_package: Dict[str, List[str]] = defaultdict(list)

    def add(self, simple_name: str, full_name: str, file_path: str):
        # Prioritize Hytale classes
        if simple_name not in self.classes or full_name.startswith(BASE_PACKAGE):
            self.classes[simple_name] = file_path
        self.full_names[full_name] = file_path
        pkg = '.'.join(full_name.split('.')[:-1])
        self.by_package[pkg].append(simple_name)

    def resolve(self, type_name: str, current_package: str, imports: List[str]) -> Optional[str]:
        """Resolves a type name to its file path."""
        # Remove generics/arrays
        base_type = re.sub(r'<.*>', '', type_name).strip()
        base_type = base_type.replace('[]', '').strip()

        # Skip primitives and standard Java types
        if base_type in ('void', 'int', 'long', 'short', 'byte', 'float', 'double',
                         'boolean', 'char', 'String', 'Object', 'Class', 'Void',
                         'Integer', 'Long', 'Short', 'Byte', 'Float', 'Double',
                         'Boolean', 'Character', 'List', 'Map', 'Set', 'Collection',
                         'Optional', 'Stream', 'Consumer', 'Supplier', 'Function',
                         'Predicate', 'BiFunction', 'BiConsumer', 'Runnable', 'Callable'):
            return None

        # Try full name
        if base_type in self.full_names:
            return self.full_names[base_type]

        # Try current package
        full_current = f"{current_package}.{base_type}"
        if full_current in self.full_names:
            return self.full_names[full_current]

        # Try imports
        for imp in imports:
            if imp.endswith(f".{base_type}"):
                if imp in self.full_names:
                    return self.full_names[imp]
            elif imp.endswith(".*"):
                pkg = imp[:-2]
                full_imp = f"{pkg}.{base_type}"
                if full_imp in self.full_names:
                    return self.full_names[full_imp]

        # Fallback: simple name
        if base_type in self.classes:
            return self.classes[base_type]

        return None


# --- Hash Functions ---
def calculate_file_hash(filepath: str) -> str:
    """Calculates SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            # Read file in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception:
        return ""

def load_hash_index(output_dir: str) -> Dict[str, str]:
    """Loads the hash index from previous build."""
    hash_file = os.path.join(output_dir, "hashes.json")
    if not os.path.exists(hash_file):
        return {}

    try:
        with open(hash_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def save_hash_index(output_dir: str, hash_index: Dict[str, str]):
    """Saves the hash index for future builds."""
    hash_file = os.path.join(output_dir, "hashes.json")
    try:
        with open(hash_file, 'w', encoding='utf-8') as f:
            json.dump(hash_index, f, indent=2, sort_keys=True)
    except Exception as e:
        print(f"Warning: Failed to save hash index: {e}")

# --- Parsing Functions ---
def parse_java_file(filepath: str) -> Optional[JavaClass]:
    """Parse a Java file and extract class information."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception:
        return None

    java_class = JavaClass()
    java_class.source_file = filepath
    java_class.source_hash = calculate_file_hash(filepath)
    java_class.generated_at = datetime.now().astimezone().isoformat()

    # Extract package
    pkg_match = PACKAGE_PATTERN.search(content)
    if pkg_match:
        java_class.package = pkg_match.group(1)
        
    # Filter: Only process com.hypixel.hytale packages
    if not java_class.package.startswith(BASE_PACKAGE):
        return None

    # Extract imports
    for match in IMPORT_PATTERN.finditer(content):
        java_class.imports.append(match.group(1))

    # Extract class declaration
    class_match = CLASS_PATTERN.search(content)
    if not class_match:
        return None

    if class_match.group(1): java_class.modifiers.append("public")
    if class_match.group(2): java_class.modifiers.append("abstract")
    if class_match.group(3): java_class.modifiers.append("final")
    if class_match.group(4): java_class.modifiers.append("static")

    java_class.type = class_match.group(5)
    java_class.name = class_match.group(6)
    java_class.full_name = f"{java_class.package}.{java_class.name}" if java_class.package else java_class.name

    if class_match.group(7):
        java_class.extends = class_match.group(7).strip()
    if class_match.group(8):
        java_class.implements = [i.strip() for i in class_match.group(8).split(',')]

    # Get class body
    brace_count = 0
    class_body_start = content.find('{', class_match.start())
    class_body = ""
    if class_body_start != -1:
        for i, char in enumerate(content[class_body_start:]):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    class_body = content[class_body_start+1:class_body_start+i]
                    break

    # Extract enum constants
    if java_class.type == "enum":
        enum_section = class_body.split(';')[0] if ';' in class_body else class_body
        for match in ENUM_CONST_PATTERN.finditer(enum_section):
            java_class.enum_constants.append(match.group(1))

    # Extract fields
    for match in FIELD_PATTERN.finditer(class_body):
        visibility = match.group(1) or ""
        if visibility not in ("public", "protected", ""):
            continue
        if java_class.type == "interface" or visibility in ("public", "protected"):
            field = JavaField()
            field.name = match.group(7)
            field.type = match.group(6).strip()
            if visibility: field.modifiers.append(visibility)
            if match.group(2): field.modifiers.append("static")
            if match.group(3): field.modifiers.append("final")

            if field.name in ('class', 'interface', 'enum', 'void', 'return', 'if', 'for', 'while', 'new', 'try'):
                continue
            if '(' in field.type or ')' in field.type:
                continue

            java_class.fields.append(field)

    # Extract methods
    for match in METHOD_PATTERN.finditer(class_body):
        visibility = match.group(1) or ""
        if visibility == "private":
            continue

        method = JavaMethod()
        method.name = match.group(9)
        method.return_type = match.group(8).strip()

        if method.return_type in ('if', 'for', 'while', 'switch', 'try', 'catch', 'synchronized', 'new'):
            continue

        # Detect constructors (same name as class, no return type keywords)
        if method.name == java_class.name:
            method.is_constructor = True

        if visibility: method.modifiers.append(visibility)
        if match.group(2): method.modifiers.append("static")
        if match.group(3): method.modifiers.append("final")
        if match.group(4): method.modifiers.append("abstract")
        if match.group(5): method.modifiers.append("default")
        if match.group(7): method.generic_params = match.group(7)

        # Parse parameters
        params_str = match.group(10).strip()
        if params_str:
            params = []
            depth = 0
            current = ""
            for char in params_str:
                if char in '<[(': depth += 1
                elif char in '>])': depth -= 1
                elif char == ',' and depth == 0:
                    if current.strip(): params.append(current.strip())
                    current = ""
                    continue
                current += char
            if current.strip(): params.append(current.strip())

            for p in params:
                p = re.sub(r'@\w+\s*', '', p).strip()
                parts = p.rsplit(' ', 1)
                if len(parts) == 2:
                    method.parameters.append((parts[0].strip(), parts[1].strip()))
                elif len(parts) == 1 and parts[0]:
                    method.parameters.append((parts[0], ""))

        if match.group(11):
            method.throws = [t.strip() for t in match.group(11).split(',')]

        java_class.methods.append(method)

    return java_class


# --- Generation Functions ---
def parse_custom_docs(custom_file: str) -> Optional[CustomDocs]:
    """Parses custom documentation file and extracts descriptions."""
    if not os.path.exists(custom_file):
        return None

    try:
        with open(custom_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    docs = CustomDocs()

    # Extract Overview
    overview_match = re.search(r'##\s+Overview\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if overview_match:
        docs.overview = overview_match.group(1).strip()

    # Extract Field Descriptions
    field_section = re.search(r'##\s+Field Descriptions\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if field_section:
        for line in field_section.group(1).split('\n'):
            match = re.match(r'-\s+`([^`]+)`:\s*(.+)', line.strip())
            if match:
                docs.field_descriptions[match.group(1)] = match.group(2).strip()

    # Extract Constructor Descriptions
    ctor_section = re.search(r'##\s+Constructor Descriptions\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if ctor_section:
        for line in ctor_section.group(1).split('\n'):
            match = re.match(r'-\s+`([^`]+)`:\s*(.+)', line.strip())
            if match:
                docs.constructor_descriptions[match.group(1)] = match.group(2).strip()

    # Extract Method Descriptions
    method_section = re.search(r'##\s+Method Descriptions\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if method_section:
        for line in method_section.group(1).split('\n'):
            match = re.match(r'-\s+`([^`]+)`:\s*(.+)', line.strip())
            if match:
                docs.method_descriptions[match.group(1)] = match.group(2).strip()

    # Extract Usage Notes
    usage_match = re.search(r'##\s+Usage Notes\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if usage_match:
        docs.usage_notes = usage_match.group(1).strip()

    # Extract Examples
    examples_match = re.search(r'##\s+Examples\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if examples_match:
        docs.examples = examples_match.group(1).strip()

    return docs

def get_full_qualified_name(type_name: str, current_pkg: str, imports: List[str], index: ClassIndex) -> str:
    """Gets the full qualified name for a type."""
    # Remove generics/arrays
    base_type = re.sub(r'<.*>', '', type_name).strip()
    base_type = base_type.replace('[]', '').strip()

    # Skip primitives
    if base_type in ('void', 'int', 'long', 'short', 'byte', 'float', 'double', 'boolean', 'char'):
        return ""

    # Check if it's already a full name
    if '.' in base_type:
        return base_type

    # Try to resolve from index
    if base_type in index.full_names:
        return base_type

    # Try current package
    full_current = f"{current_pkg}.{base_type}"
    if full_current in index.full_names:
        return full_current

    # Try imports
    for imp in imports:
        if imp.endswith(f".{base_type}"):
            return imp
        elif imp.endswith(".*"):
            pkg = imp[:-2]
            full_imp = f"{pkg}.{base_type}"
            if full_imp in index.full_names:
                return full_imp

    # Java standard library types
    if base_type in ('String', 'Object', 'Class', 'Void', 'Integer', 'Long', 'Short',
                     'Byte', 'Float', 'Double', 'Boolean', 'Character'):
        return f"java.lang.{base_type}"
    if base_type in ('List', 'Map', 'Set', 'Collection', 'ArrayList', 'HashMap', 'HashSet'):
        return f"java.util.{base_type}"
    if base_type in ('Optional', 'Stream'):
        return f"java.util.{base_type}"
    if base_type in ('Consumer', 'Supplier', 'Function', 'Predicate', 'BiFunction',
                     'BiConsumer', 'Runnable', 'Callable'):
        return f"java.util.function.{base_type}" if base_type not in ('Runnable', 'Callable') else f"java.lang.{base_type}"

    return ""

def make_type_link(type_str: str, index: ClassIndex, current_pkg: str, imports: List[str], current_file: str) -> Tuple[str, str]:
    """Converts a type name into a Markdown link and returns (link, fqn).

    Returns:
        Tuple of (markdown_link, full_qualified_name)
    """
    if not type_str:
        return ("", "")

    # Get FQN
    fqn = get_full_qualified_name(type_str, current_pkg, imports, index)

    # Build link
    result = type_str
    for match in TYPE_REFERENCE_PATTERN.finditer(type_str):
        type_name = match.group(1)
        resolved = index.resolve(type_name, current_pkg, imports)

        if resolved and resolved != current_file:
            current_dir = os.path.dirname(current_file)
            rel_path = os.path.relpath(resolved, current_dir)
            result = result.replace(type_name, f"[`{type_name}`]({rel_path})", 1)
        elif type_name not in ('void', 'int', 'long', 'short', 'byte', 'float', 'double', 'boolean', 'char'):
            # Non-linked type, still wrap in backticks
            result = result.replace(type_name, f"`{type_name}`", 1)

    return (result, fqn)

def generate_class_markdown(java_class: JavaClass, index: ClassIndex, output_root: str, custom_root: str) -> str:
    """Generates the Markdown content for a single class following the new improved template."""
    lines = []

    # Parse custom documentation
    rel_path = os.path.relpath(java_class.output_file, output_root)
    custom_file = os.path.join(custom_root, rel_path)
    custom_docs = parse_custom_docs(custom_file)

    # Track related types for "Related Types" section
    related_types = set()

    # ========== HEADER ==========
    lines.append(f"# {java_class.name}")
    lines.append("")
    lines.append(f"**Full Qualified Name:** `{java_class.full_name}`")
    lines.append("")
    lines.append(f"**Type:** {java_class.type}")
    lines.append("")
    lines.append(f"**Package:** `{java_class.package}`")
    lines.append("")
    lines.append(f"**File Location:** `{rel_path}`")
    lines.append("")

    # Build metadata
    if java_class.source_hash:
        lines.append(f"**Source Hash:** `{java_class.source_hash}`")
        lines.append("")
    if java_class.generated_at:
        lines.append(f"**Generated At:** `{java_class.generated_at}`")
        lines.append("")

    lines.append("---")
    lines.append("")

    # ========== OVERVIEW ==========
    lines.append("## Overview")
    lines.append("")
    if custom_docs and custom_docs.overview:
        lines.append(custom_docs.overview)
    else:
        lines.append(f"Documentation for {java_class.type} `{java_class.name}`.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ========== DECLARATION ==========
    lines.append("## Declaration")
    lines.append("")
    lines.append("```java")
    decl_parts = java_class.modifiers + [java_class.type, java_class.name]
    decl = " ".join(decl_parts)
    if java_class.extends:
        decl += f" extends {java_class.extends}"
    if java_class.implements:
        decl += f" implements {', '.join(java_class.implements)}"
    lines.append(decl)
    lines.append("```")
    lines.append("")

    # ========== HIERARCHY ==========
    lines.append("## Hierarchy")
    lines.append("")

    if java_class.extends:
        ext_link, ext_fqn = make_type_link(java_class.extends, index, java_class.package, java_class.imports, java_class.output_file)
        if ext_fqn:
            lines.append(f"**Extends:** {ext_link} - `{ext_fqn}`")
            related_types.add(ext_fqn)
        else:
            lines.append(f"**Extends:** `{java_class.extends}`")
    else:
        lines.append("**Extends:** `java.lang.Object`")
    lines.append("")

    if java_class.implements:
        lines.append("**Implements:**")
        for impl in java_class.implements:
            impl_link, impl_fqn = make_type_link(impl, index, java_class.package, java_class.imports, java_class.output_file)
            if impl_fqn:
                lines.append(f"- {impl_link} - `{impl_fqn}`")
                related_types.add(impl_fqn)
            else:
                lines.append(f"- `{impl}`")
        lines.append("")
    else:
        lines.append("**Implements:** None")
        lines.append("")

    lines.append("**Known Subclasses:** None")
    lines.append("")

    if java_class.type == "interface":
        lines.append("**Known Implementations:** None")
        lines.append("")

    lines.append("---")
    lines.append("")

    # ========== ENUM CONSTANTS ==========
    if java_class.enum_constants:
        lines.append("## Enum Constants")
        lines.append("")
        lines.append("| Constant | Description |")
        lines.append("|----------|-------------|")
        for const in java_class.enum_constants:
            # Check for custom description
            desc = ""
            if custom_docs and const in custom_docs.field_descriptions:
                desc = custom_docs.field_descriptions[const]
            lines.append(f"| `{const}` | {desc} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    # ========== FIELDS ==========
    public_fields = [f for f in java_class.fields
                     if "public" in f.modifiers or "protected" in f.modifiers or java_class.type == "interface"]
    if public_fields:
        lines.append("## Fields")
        lines.append("")
        for field in public_fields:
            mods = " ".join(field.modifiers) if field.modifiers else ""
            type_link, type_fqn = make_type_link(field.type, index, java_class.package, java_class.imports, java_class.output_file)

            if type_fqn and type_fqn.startswith(BASE_PACKAGE):
                related_types.add(type_fqn)

            lines.append(f"### `{field.name}`")
            lines.append("")
            lines.append("```java")
            lines.append(f"{mods} {field.type} {field.name}".strip())
            lines.append("```")
            lines.append("")

            if type_fqn:
                lines.append(f"- **Type:** {type_link} - `{type_fqn}`")
            else:
                lines.append(f"- **Type:** `{field.type}` (primitive)")

            if mods:
                lines.append(f"- **Modifiers:** `{mods}`")

            # Add custom description if available
            if custom_docs and field.name in custom_docs.field_descriptions:
                lines.append(f"- **Description:** {custom_docs.field_descriptions[field.name]}")

            lines.append("")

        lines.append("---")
        lines.append("")

    # ========== CONSTRUCTORS ==========
    constructors = [m for m in java_class.methods
                    if m.is_constructor and ("public" in m.modifiers or "protected" in m.modifiers)]
    if constructors:
        lines.append("## Constructors")
        lines.append("")
        for ctor in constructors:
            mods = " ".join(ctor.modifiers) if ctor.modifiers else ""

            # Build parameter signature
            param_sig = ", ".join(f"{p[0]} {p[1]}" for p in ctor.parameters)
            sig_key = f"{ctor.name}({param_sig})"

            lines.append(f"### `{ctor.name}(...)`")
            lines.append("")
            lines.append("```java")
            sig = f"{mods} {ctor.name}({param_sig})"
            if ctor.throws:
                sig += f" throws {', '.join(ctor.throws)}"
            lines.append(sig.strip())
            lines.append("```")
            lines.append("")

            if ctor.parameters:
                lines.append("**Parameters:**")
                for ptype, pname in ctor.parameters:
                    ptype_link, ptype_fqn = make_type_link(ptype, index, java_class.package, java_class.imports, java_class.output_file)
                    if ptype_fqn and ptype_fqn.startswith(BASE_PACKAGE):
                        related_types.add(ptype_fqn)

                    if ptype_fqn:
                        lines.append(f"- `{pname}`: {ptype_link} - `{ptype_fqn}`")
                    else:
                        lines.append(f"- `{pname}`: `{ptype}`")
                lines.append("")

            if ctor.throws:
                lines.append("**Throws:**")
                for throw in ctor.throws:
                    throw_link, throw_fqn = make_type_link(throw, index, java_class.package, java_class.imports, java_class.output_file)
                    if throw_fqn and throw_fqn.startswith(BASE_PACKAGE):
                        related_types.add(throw_fqn)

                    if throw_fqn:
                        lines.append(f"- {throw_link} - `{throw_fqn}`")
                    else:
                        lines.append(f"- `{throw}`")
                lines.append("")

            # Add custom description if available
            if custom_docs and sig_key in custom_docs.constructor_descriptions:
                lines.append(f"**Description:** {custom_docs.constructor_descriptions[sig_key]}")
                lines.append("")

        lines.append("---")
        lines.append("")

    # ========== METHODS ==========
    public_methods = [m for m in java_class.methods
                      if not m.is_constructor and ("public" in m.modifiers or "protected" in m.modifiers or java_class.type == "interface")]
    if public_methods:
        lines.append("## Methods")
        lines.append("")
        for method in public_methods:
            mods = " ".join(method.modifiers) if method.modifiers else ""
            return_link, return_fqn = make_type_link(method.return_type, index, java_class.package, java_class.imports, java_class.output_file)

            if return_fqn and return_fqn.startswith(BASE_PACKAGE):
                related_types.add(return_fqn)

            # Build parameter signature for lookup
            param_sig = ", ".join(f"{p[0]} {p[1]}" for p in method.parameters)
            sig_key = f"{method.name}({param_sig})"

            lines.append(f"### `{method.name}(...)`")
            lines.append("")
            lines.append("```java")
            sig = f"{mods} {method.return_type} {method.name}({param_sig})"
            if method.throws:
                sig += f" throws {', '.join(method.throws)}"
            lines.append(sig.strip())
            lines.append("```")
            lines.append("")

            # Returns
            if return_fqn:
                lines.append(f"**Returns:** {return_link} - `{return_fqn}`")
            else:
                lines.append(f"**Returns:** `{method.return_type}`")
            lines.append("")

            # Parameters
            if method.parameters:
                lines.append("**Parameters:**")
                for ptype, pname in method.parameters:
                    ptype_link, ptype_fqn = make_type_link(ptype, index, java_class.package, java_class.imports, java_class.output_file)
                    if ptype_fqn and ptype_fqn.startswith(BASE_PACKAGE):
                        related_types.add(ptype_fqn)

                    if ptype_fqn:
                        lines.append(f"- `{pname}`: {ptype_link} - `{ptype_fqn}`")
                    else:
                        lines.append(f"- `{pname}`: `{ptype}`")
                lines.append("")

            # Throws
            if method.throws:
                lines.append("**Throws:**")
                for throw in method.throws:
                    throw_link, throw_fqn = make_type_link(throw, index, java_class.package, java_class.imports, java_class.output_file)
                    if throw_fqn and throw_fqn.startswith(BASE_PACKAGE):
                        related_types.add(throw_fqn)

                    if throw_fqn:
                        lines.append(f"- {throw_link} - `{throw_fqn}`")
                    else:
                        lines.append(f"- `{throw}`")
                lines.append("")

            # Modifiers
            if mods:
                lines.append(f"**Modifiers:** `{mods}`")
                lines.append("")

            # Add custom description if available
            if custom_docs and sig_key in custom_docs.method_descriptions:
                lines.append(f"**Description:** {custom_docs.method_descriptions[sig_key]}")
                lines.append("")

    # ========== RELATED TYPES ==========
    if related_types:
        lines.append("---")
        lines.append("")
        lines.append("## Related Types")
        lines.append("")
        lines.append("**Uses:**")
        for related in sorted(related_types):
            simple_name = related.split('.')[-1]
            resolved = index.resolve(simple_name, java_class.package, java_class.imports)
            if resolved:
                current_dir = os.path.dirname(java_class.output_file)
                rel_path_link = os.path.relpath(resolved, current_dir)
                lines.append(f"- [`{simple_name}`]({rel_path_link}) - `{related}`")
            else:
                lines.append(f"- `{related}`")
        lines.append("")

    # ========== USAGE NOTES & EXAMPLES ==========
    if custom_docs:
        if custom_docs.usage_notes:
            lines.append("---")
            lines.append("")
            lines.append("## Usage Notes")
            lines.append("")
            lines.append(custom_docs.usage_notes)
            lines.append("")

        if custom_docs.examples:
            lines.append("---")
            lines.append("")
            lines.append("## Examples")
            lines.append("")
            lines.append(custom_docs.examples)
            lines.append("")

    # ========== NAVIGATION ==========
    lines.append("---")
    lines.append("")
    lines.append("## Navigation")
    lines.append("")

    pkg_index = os.path.join(output_root, java_class.package.replace('.', '/'), "_index.md")
    rel_pkg_index = os.path.relpath(pkg_index, os.path.dirname(java_class.output_file))
    lines.append(f"- [📦 Package Index (`{java_class.package}`)]({rel_pkg_index})")

    main_index = os.path.join(output_root, "INDEX.md")
    rel_main_index = os.path.relpath(main_index, os.path.dirname(java_class.output_file))
    lines.append(f"- [📚 Main Index]({rel_main_index})")

    class_lookup = os.path.join(output_root, "class_lookup.json")
    rel_class_lookup = os.path.relpath(class_lookup, os.path.dirname(java_class.output_file))
    lines.append(f"- [🔍 Class Lookup JSON]({rel_class_lookup})")
    lines.append("")

    return "\n".join(lines)

def generate_package_index(package: str, classes: List[JavaClass], output_dir: str) -> str:
    """Generates the index file for a package."""
    lines = []
    pkg_dir = os.path.join(output_dir, package.replace('.', '/'))
    index_file = os.path.join(pkg_dir, "_index.md")

    lines.append(f"# 📦 {package}")
    lines.append("")
    lines.append(f"**Path:** `{os.path.relpath(index_file, output_dir)}`")
    lines.append("")
    lines.append(f"**Type Count:** {len(classes)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    by_type = defaultdict(list)
    for cls in classes:
        by_type[cls.type].append(cls)

    type_order = [("interface", "🔌 Interfaces"), ("class", "📦 Classes"),
                  ("enum", "📋 Enums"), ("@interface", "🏷️ Annotations")]

    for t, label in type_order:
        if t in by_type:
            lines.append(f"## {label}")
            lines.append("")
            for cls in sorted(by_type[t], key=lambda x: x.name):
                rel_path = f"{cls.name}.md"
                lines.append(f"- [{cls.name}]({rel_path}) - `{cls.full_name}`")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Navigation")
    lines.append("")
    main_index = os.path.join(output_dir, "INDEX.md")
    rel_main = os.path.relpath(main_index, pkg_dir)
    lines.append(f"- [📚 Main Index]({rel_main})")
    lines.append("")

    return "\n".join(lines)

# --- CLI Actions ---
def download_cfr(lib_dir: str):
    """Downloads the CFR decompiler to the lib directory if missing."""
    if not os.path.exists(lib_dir):
        os.makedirs(lib_dir)
        
    cfr_path = os.path.join(lib_dir, CFR_JAR_NAME)
    if os.path.exists(cfr_path):
        return

    print(f"⬇️  Downloading Decompiler ({CFR_JAR_NAME}) to {lib_dir}...")
    try:
        subprocess.run(["curl", "-L", "-o", cfr_path, CFR_URL], check=True)
    except Exception:
        subprocess.run(["wget", "-O", cfr_path, CFR_URL], check=True)
    print("✅ Download complete.")

def decompile_jar(jar_path: str, src_dir: str, lib_dir: str):
    """Runs CFR to decompile the jar with visual feedback."""
    cfr_path = os.path.join(lib_dir, CFR_JAR_NAME)
    print(f"🔨 Decompiling {os.path.basename(jar_path)}...")

    if not os.path.exists(src_dir):
        os.makedirs(src_dir)

    cmd = [
        "java", "-jar",cfr_path,
        jar_path,
        "--outputdir", src_dir,
        "--caseinsensitivefs", "true",
        "--silent", "true",
        "--clobber", "true"
    ]

    if IS_CI:
        # In CI: simple message, no spinner
        print("   Decompiling... (this may take a few minutes)")
        start_time = time.time()
        try:
            subprocess.run(cmd, check=True)
            elapsed = int(time.time() - start_time)
            print(f"✅ Decompilation complete ({elapsed}s)")
        except subprocess.CalledProcessError as e:
            print(f"❌ Decompilation failed: {e}")
            sys.exit(1)
    else:
        # Interactive terminal: show spinner
        print("   Please wait, this may take a few minutes depending on jar size...")
        done = False
        def spin():
            spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
            i = 0
            start_time = time.time()
            while not done:
                elapsed = int(time.time() - start_time)
                sys.stdout.write(f"\r   {spinner[i]} Processing... ({elapsed}s)")
                sys.stdout.flush()
                time.sleep(0.1)
                i = (i + 1) % len(spinner)

        t = threading.Thread(target=spin)
        t.start()

        try:
            subprocess.run(cmd, check=True)
            done = True
            t.join()
            print(f"\r✅ Decompilation complete.        ")
        except subprocess.CalledProcessError as e:
            done = True
            t.join()
            print(f"\r❌ Decompilation failed: {e}")
            sys.exit(1)

def run_generation(src_dir: str, output_dir: str, custom_docs_dir: str, skip_unchanged: bool = False):
    """Orchestrates the documentation generation."""
    print(f"🔍 Scanning Java files in {src_dir}...")

    # Load previous hash index
    previous_hashes = {}
    if skip_unchanged:
        previous_hashes = load_hash_index(output_dir)
        if previous_hashes:
            print(f"📋 Loaded {len(previous_hashes)} previous file hashes...")
    java_files = []
    base_pkg_path = BASE_PACKAGE.replace('.', os.sep)
    
    for root, _, files in os.walk(src_dir):
        for f in files:
            if f.endswith('.java') and '$' not in f:
                full_path = os.path.join(root, f)
                if base_pkg_path in full_path:
                    java_files.append(full_path)
    
    print(f"📁 Found {len(java_files)} potential files in {BASE_PACKAGE}...")

    print("📖 Building class index...")
    index = ClassIndex()
    classes_by_package = defaultdict(list)
    all_classes = []

    for i, filepath in enumerate(java_files):
        if not IS_CI and i % 100 == 0:
            sys.stdout.write(f"\r   Parsing {i}/{len(java_files)}")
            sys.stdout.flush()

        java_class = parse_java_file(filepath)
        if java_class and java_class.name:
            pkg_path = java_class.package.replace('.', '/')
            java_class.output_file = os.path.join(output_dir, pkg_path, f"{java_class.name}.md")

            index.add(java_class.name, java_class.full_name, java_class.output_file)
            classes_by_package[java_class.package].append(java_class)
            all_classes.append(java_class)

    if IS_CI:
        print(f"✅ Indexed {len(all_classes)} classes")
    else:
        print(f"\r✅ Indexed {len(all_classes)} classes.       ")

    print(f"📝 Generating Markdown in {output_dir} (custom docs from {custom_docs_dir})...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Track statistics
    new_hash_index = {}
    stats = {
        'total': len(all_classes),
        'generated': 0,
        'skipped': 0,
        'changed': 0
    }

    for i, java_class in enumerate(all_classes):
        if not IS_CI and i % 100 == 0:
            sys.stdout.write(f"\r   Writing {i}/{len(all_classes)} (skipped: {stats['skipped']})")
            sys.stdout.flush()

        # Check if file changed
        current_hash = java_class.source_hash
        new_hash_index[java_class.full_name] = current_hash

        if skip_unchanged and java_class.full_name in previous_hashes:
            if previous_hashes[java_class.full_name] == current_hash:
                # File unchanged, skip regeneration if output exists
                if os.path.exists(java_class.output_file):
                    stats['skipped'] += 1
                    continue
                # Output missing, regenerate even though source unchanged
            else:
                stats['changed'] += 1

        os.makedirs(os.path.dirname(java_class.output_file), exist_ok=True)
        content = generate_class_markdown(java_class, index, output_dir, custom_docs_dir)
        with open(java_class.output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        stats['generated'] += 1

    if IS_CI:
        print(f"✅ Generated {stats['generated']} files (skipped {stats['skipped']} unchanged, {stats['changed']} changed)")
    else:
        print(f"\r✅ Generated {stats['generated']} files (skipped {stats['skipped']} unchanged, {stats['changed']} changed).      ")

    # Save hash index
    save_hash_index(output_dir, new_hash_index)

    print("📚 Generating Package Indexes...")
    for pkg, classes in classes_by_package.items():
        pkg_dir = os.path.join(output_dir, pkg.replace('.', '/'))
        os.makedirs(pkg_dir, exist_ok=True)
        content = generate_package_index(pkg, classes, output_dir)
        with open(os.path.join(pkg_dir, "_index.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    print("🤖 Generating AI Lookup JSON...")
    lookup = {}
    for cls in all_classes:
        rel_path = os.path.relpath(cls.output_file, output_dir)
        info = {
            "full_name": cls.full_name,
            "path": rel_path,
            "type": cls.type,
            "package": cls.package
        }
        lookup[cls.name] = info
        lookup[cls.full_name] = info

    with open(os.path.join(output_dir, "class_lookup.json"), 'w', encoding='utf-8') as f:
        json.dump(lookup, f, indent=2)

    # Main Index
    print("📚 Generating Main Index...")
    main_lines = [
        "# 📚 Hytale Server API",
        "",
        "Reference documentation generated for AI navigation.",
        "",
        f"**Total Types:** {len(all_classes)}",
        "",
        "---",
        "",
        "## Packages",
        ""
    ]
    
    top_level = defaultdict(list)
    for pkg in sorted(classes_by_package.keys()):
        parts = pkg.split('.')
        top = '.'.join(parts[:4]) if len(parts) >= 4 else pkg
        top_level[top].append(pkg)

    for top in sorted(top_level.keys()):
        sub_packages = top_level[top]
        total = sum(len(classes_by_package[p]) for p in sub_packages)
        main_lines.append(f"### `{top}` ({total} types)")
        main_lines.append("")
        for pkg in sorted(sub_packages):
            count = len(classes_by_package[pkg])
            pkg_path = pkg.replace('.', '/')
            display = pkg.replace(top + '.', '') if pkg != top else pkg.split('.')[-1]
            main_lines.append(f"- [{display}]({pkg_path}/_index.md) ({count})")
        main_lines.append("")

    with open(os.path.join(output_dir, "INDEX.md"), 'w', encoding='utf-8') as f:
        f.write("\n".join(main_lines))

    print(f"✨ Documentation generated in: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Hytale Documentation Generator")
    parser.add_argument("--file", "-f", default=os.path.join("lib", "HytaleServer.jar"), help="Path to HytaleServer.jar")
    parser.add_argument("--src", "-s", default=os.path.join("lib", "src"), help="Directory for decompiled source code")
    parser.add_argument("--output", "-o", default="build", help="Directory for generated documentation (default: build)")
    parser.add_argument("--custom", "-c", default="docs", help="Directory for custom documentation overrides (default: docs)")
    parser.add_argument("--lib", "-l", default="lib", help="Directory for libraries/tools (default: lib)")
    parser.add_argument("--skip-decomp", action="store_true", help="Skip decompilation step")
    parser.add_argument("--only-decomp", action="store_true", help="Only perform decompilation")
    parser.add_argument("--only-docs", action="store_true", help="Only generate docs")
    parser.add_argument("--skip-unchanged", action="store_true", help="Skip regenerating files that haven't changed (based on source hash)")

    args = parser.parse_args()
    
    cwd = os.getcwd()
    jar_full_path = os.path.abspath(args.file)
    src_full_path = os.path.abspath(args.src)
    out_full_path = os.path.abspath(args.output)
    custom_full_path = os.path.abspath(args.custom)
    lib_full_path = os.path.abspath(args.lib)
    
    # Resolve flags
    skip_decomp = args.skip_decomp or args.only_docs
    skip_docs = args.only_decomp

    print(f"🚀 Hydocs - Hytale Documentation Tool")
    print(f"   Target: {jar_full_path}")
    print(f"   Source: {src_full_path}")
    print(f"   Custom Docs: {custom_full_path}")
    print(f"   Lib Folder: {lib_full_path}")
    print("")

    if not skip_decomp:
        download_cfr(lib_full_path)
        if not os.path.exists(jar_full_path):
            print(f"❌ Error: Jar file not found at {jar_full_path}")
            sys.exit(1)
        decompile_jar(jar_full_path, src_full_path, lib_full_path)
    else:
        print("⏩ Skipping decompilation step...")

    if not skip_docs:
        run_generation(src_full_path, out_full_path, custom_full_path, args.skip_unchanged)
    else:
        print("⏩ Skipping documentation generation...")
        
    print("\n✅ Done!")

if __name__ == "__main__":
    main()