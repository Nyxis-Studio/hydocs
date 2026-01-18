#!/usr/bin/env python3
"""
Creates checklist markdown files with chunks of 10 files each
"""
import os
from pathlib import Path

# Read all files
with open('/tmp/all_files.txt', 'r') as f:
    all_files = [line.strip() for line in f.readlines()]

build_dir = Path('/home/goustkor/Documents/nyxis/hytale/hydocs/build')
checklist_dir = build_dir / 'checklists'
checklist_dir.mkdir(exist_ok=True)

# Create chunks of 10
chunk_size = 10
total_files = len(all_files)
num_chunks = (total_files + chunk_size - 1) // chunk_size

print(f"📋 Creating {num_chunks} checklist files...")
print(f"   Total files: {total_files}")
print(f"   Chunk size: {chunk_size}")
print()

for chunk_idx in range(num_chunks):
    start_idx = chunk_idx * chunk_size
    end_idx = min(start_idx + chunk_size, total_files)
    chunk_files = all_files[start_idx:end_idx]

    # Create checklist content
    lines = []
    lines.append(f"# Checklist - Chunk {chunk_idx + 1}/{num_chunks}")
    lines.append("")
    lines.append(f"**Files {start_idx + 1} - {end_idx} of {total_files}**")
    lines.append("")
    lines.append("---")
    lines.append("")

    for file_path in chunk_files:
        # Get relative path from build dir
        rel_path = os.path.relpath(file_path, build_dir)

        # Extract class name from path
        class_name = os.path.basename(file_path).replace('.md', '')

        # Get package from path
        pkg_path = os.path.dirname(rel_path).replace('/', '.')

        lines.append(f"## [ ] {class_name}")
        lines.append("")
        lines.append(f"- **Package:** `{pkg_path}`")
        lines.append(f"- **File:** `{rel_path}`")
        lines.append(f"- **Full Path:** `{file_path}`")
        lines.append("")
        lines.append("**Notes:**")
        lines.append("")
        lines.append("```")
        lines.append("")
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Navigation
    lines.append("## Navigation")
    lines.append("")
    if chunk_idx > 0:
        lines.append(f"- [⬅️ Previous Chunk (Chunk {chunk_idx})](checklist_{chunk_idx:04d}.md)")
    if chunk_idx < num_chunks - 1:
        lines.append(f"- [➡️ Next Chunk (Chunk {chunk_idx + 2})](checklist_{chunk_idx + 2:04d}.md)")
    lines.append(f"- [📚 Checklist Index](checklist_index.md)")
    lines.append("")

    # Write file
    checklist_file = checklist_dir / f"checklist_{chunk_idx + 1:04d}.md"
    with open(checklist_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    if (chunk_idx + 1) % 100 == 0:
        print(f"   Created {chunk_idx + 1}/{num_chunks} checklists...")

# Create index file
print("\n📚 Creating checklist index...")
index_lines = []
index_lines.append("# Hytale Server Checklist Index")
index_lines.append("")
index_lines.append(f"**Total Files:** {total_files}")
index_lines.append(f"**Total Chunks:** {num_chunks}")
index_lines.append(f"**Files per Chunk:** {chunk_size}")
index_lines.append("")
index_lines.append("---")
index_lines.append("")
index_lines.append("## Checklist Files")
index_lines.append("")

for chunk_idx in range(num_chunks):
    start_idx = chunk_idx * chunk_size
    end_idx = min(start_idx + chunk_size, total_files)
    index_lines.append(f"{chunk_idx + 1}. [Chunk {chunk_idx + 1} (Files {start_idx + 1}-{end_idx})](checklist_{chunk_idx + 1:04d}.md)")

index_lines.append("")
index_lines.append("---")
index_lines.append("")
index_lines.append("## Quick Navigation")
index_lines.append("")
index_lines.append(f"- [First Chunk](checklist_0001.md)")
index_lines.append(f"- [Last Chunk](checklist_{num_chunks:04d}.md)")
index_lines.append(f"- [Main Documentation Index](../INDEX.md)")
index_lines.append("")

index_file = checklist_dir / "checklist_index.md"
with open(index_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(index_lines))

print(f"\n✅ Created {num_chunks} checklist files in: {checklist_dir}")
print(f"   Index file: {index_file}")
print("\n✨ Done!")
