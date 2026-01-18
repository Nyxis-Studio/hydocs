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
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

# --- Configuration Constants ---
CFR_VERSION = "0.152"
CFR_JAR_NAME = f"cfr-{CFR_VERSION}.jar"
CFR_URL = f"https://www.benf.org/other/cfr/cfr-{CFR_VERSION}.jar"
BASE_PACKAGE = "com.hypixel.hytale"

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

class JavaMethod:
    def __init__(self):
        self.name = ""
        self.return_type = ""
        self.parameters = []  # List of (type, name)
        self.modifiers = []
        self.throws = []
        self.generic_params = ""

class JavaField:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.modifiers = []

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
def make_type_link(type_str: str, index: ClassIndex, current_pkg: str, imports: List[str], current_file: str) -> str:
    """Converts a type name into a Markdown link if resolved."""
    if not type_str: return type_str

    result = type_str
    for match in TYPE_REFERENCE_PATTERN.finditer(type_str):
        type_name = match.group(1)
        resolved = index.resolve(type_name, current_pkg, imports)

        if resolved and resolved != current_file:
            current_dir = os.path.dirname(current_file)
            rel_path = os.path.relpath(resolved, current_dir)
            result = result.replace(type_name, f"[{type_name}]({rel_path})", 1)

    return result

def generate_class_markdown(java_class: JavaClass, index: ClassIndex, output_root: str, custom_root: str) -> str:
    """Generates the Markdown content for a single class."""
    lines = []

    # Header
    lines.append(f"# {java_class.name}")
    lines.append("")
    lines.append(f"**Path:** `{os.path.relpath(java_class.output_file, output_root)}`")
    lines.append("")
    lines.append(f"**Package:** `{java_class.package}`")
    lines.append("")
    lines.append(f"**Full Name:** `{java_class.full_name}`")
    lines.append("")
    lines.append(f"**Type:** {java_class.type}")
    lines.append("")

    # Source link (approximated)
    rel_src = os.path.relpath(java_class.source_file, output_root)
    lines.append(f"**Source:** [{java_class.name}.java]({rel_src})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Declaration
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
    
    # --- Custom Documentation Injection ---
    rel_path = os.path.relpath(java_class.output_file, output_root)
    custom_file = os.path.join(custom_root, rel_path)
    
    if os.path.exists(custom_file):
        try:
            with open(custom_file, 'r', encoding='utf-8') as f:
                custom_content = f.read()
            lines.append("## 📝 Custom Documentation")
            lines.append("")
            lines.append(custom_content)
            lines.append("")
            lines.append("---")
            lines.append("")
        except Exception as e:
            print(f"Warning: Failed to read custom docs for {java_class.name}: {e}")

    # Hierarchy
    if java_class.extends:
        ext_link = make_type_link(java_class.extends, index, java_class.package, java_class.imports, java_class.output_file)
        lines.append(f"**Extends:** `{ext_link}`")
        lines.append("")

    if java_class.implements:
        impl_links = []
        for impl in java_class.implements:
            impl_link = make_type_link(impl, index, java_class.package, java_class.imports, java_class.output_file)
            impl_links.append(f"`{impl_link}`")
        lines.append(f"**Implements:** {', '.join(impl_links)}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Enum Constants
    if java_class.enum_constants:
        lines.append("## Enum Constants")
        lines.append("")
        for const in java_class.enum_constants:
            lines.append(f"- `{const}`")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Fields
    public_fields = [f for f in java_class.fields
                     if "public" in f.modifiers or "protected" in f.modifiers or java_class.type == "interface"]
    if public_fields:
        lines.append("## Fields")
        lines.append("")
        for field in public_fields:
            mods = " ".join(field.modifiers) if field.modifiers else ""
            type_link = make_type_link(field.type, index, java_class.package, java_class.imports, java_class.output_file)
            lines.append(f"### `{field.name}`")
            lines.append("")
            lines.append(f"- **Type:** `{type_link}`")
            if mods:
                lines.append(f"- **Modifiers:** `{mods}`")
            lines.append("")
        lines.append("---")
        lines.append("")

    # Methods
    public_methods = [m for m in java_class.methods
                      if "public" in m.modifiers or "protected" in m.modifiers or java_class.type == "interface"]
    if public_methods:
        lines.append("## Methods")
        lines.append("")
        for method in public_methods:
            mods = " ".join(method.modifiers) if method.modifiers else ""
            return_link = make_type_link(method.return_type, index, java_class.package, java_class.imports, java_class.output_file)

            lines.append(f"### `{method.name}(...)`")
            lines.append("")
            lines.append("```java")
            sig = f"{mods} {method.return_type} {method.name}({', '.join(f'{p[0]} {p[1]}' for p in method.parameters)})"
            if method.throws:
                sig += f" throws {', '.join(method.throws)}"
            lines.append(sig.strip())
            lines.append("```")
            lines.append("")
            lines.append(f"- **Returns:** `{return_link}`")
            if method.parameters:
                lines.append("- **Parameters:**")
                for ptype, pname in method.parameters:
                    ptype_link = make_type_link(ptype, index, java_class.package, java_class.imports, java_class.output_file)
                    lines.append(f"  - `{pname}`: `{ptype_link}`")
            if method.throws:
                throw_links = [make_type_link(t, index, java_class.package, java_class.imports, java_class.output_file)
                               for t in method.throws]
                lines.append(f"- **Throws:** {', '.join(f'`{t}`' for t in throw_links)})")
            lines.append("")

    # Navigation
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
    print("   Please wait, this may take a few minutes depending on jar size...")
    
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

def run_generation(src_dir: str, output_dir: str, custom_docs_dir: str):
    """Orchestrates the documentation generation."""
    print(f"🔍 Scanning Java files in {src_dir}...")
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
        if i % 100 == 0: 
            sys.stdout.write(f"\r   Parsing {i}/{len(java_files)}")
            sys.stdout.flush()
        
        java_class = parse_java_file(filepath)
        if java_class and java_class.name:
            pkg_path = java_class.package.replace('.', '/')
            java_class.output_file = os.path.join(output_dir, pkg_path, f"{java_class.name}.md")
            
            index.add(java_class.name, java_class.full_name, java_class.output_file)
            classes_by_package[java_class.package].append(java_class)
            all_classes.append(java_class)
            
    print(f"\r✅ Indexed {len(all_classes)} classes.       ")

    print(f"📝 Generating Markdown in {output_dir} (custom docs from {custom_docs_dir})...")
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    for i, java_class in enumerate(all_classes):
        if i % 100 == 0:
            sys.stdout.write(f"\r   Writing {i}/{len(all_classes)}")
            sys.stdout.flush()
            
        os.makedirs(os.path.dirname(java_class.output_file), exist_ok=True)
        content = generate_class_markdown(java_class, index, output_dir, custom_docs_dir)
        with open(java_class.output_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"\r✅ Written {len(all_classes)} markdown files.      ")

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
        run_generation(src_full_path, out_full_path, custom_full_path)
    else:
        print("⏩ Skipping documentation generation...")
        
    print("\n✅ Done!")

if __name__ == "__main__":
    main()