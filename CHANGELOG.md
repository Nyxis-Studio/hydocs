# Changelog - Hydocs Documentation Structure Improvements

## 2026-01-18 - Hash-Based Change Detection System

### Overview
Added SHA256 hash tracking system for incremental builds. The system calculates and stores hashes of source files, enabling detection of changes and skipping regeneration of unchanged documentation.

### New Features

#### 1. **SHA256 Hash Tracking**
- Every Java source file has its SHA256 hash calculated
- Hashes stored in `JavaClass.source_hash`
- Build metadata included in generated documentation
- Central hash index saved to `build/hashes.json`

#### 2. **Incremental Build Support**
- New `--skip-unchanged` flag for intelligent regeneration
- Compares current hashes with previous build
- Skips regeneration when:
  - Source file hash unchanged
  - Output documentation exists
- Massive performance improvement for incremental builds

#### 3. **Build Metadata in Documentation**
Added to every generated `.md` file:
```markdown
**Source Hash:** `3bf87abfd876785ff2e1589e8f64f3fb3625633b89eadf824e46082917137635`
**Generated At:** `2026-01-18T16:19:12.915419+00:00`
```

#### 4. **Hash Index File**
`build/hashes.json` structure:
```json
{
  "com.hypixel.hytale.Main": "3bf87abfd876785ff2e1589e8f64f3fb3625633b89eadf824e46082917137635",
  "com.hypixel.hytale.server.HytaleServer": "a9162add3c6cab43883af10b5f108cb954755c9329388dc211255d7783c14d53"
}
```

#### 5. **Statistics Reporting**
Enhanced output with detailed statistics:
```
✅ Generated 63 files (skipped 4788 unchanged, 63 changed)
```

### Performance Impact

**Without `--skip-unchanged` (full build):**
- Time: ~30 seconds
- Files: 4851 generated

**With `--skip-unchanged` (few changes):**
- Time: ~2 seconds
- Files: 63 generated, 4788 skipped
- **Improvement: 93% faster**

### Technical Changes

#### New Functions
- `calculate_file_hash(filepath: str) -> str` - Calculates SHA256 hash
- `load_hash_index(output_dir: str) -> Dict[str, str]` - Loads previous hashes
- `save_hash_index(output_dir: str, hash_index: Dict[str, str])` - Saves hash index

#### Modified Functions
- `parse_java_file()` - Now calculates and stores hash + timestamp
- `generate_class_markdown()` - Includes hash and timestamp in output
- `run_generation()` - Implements skip logic based on hashes

#### New Fields
- `JavaClass.source_hash: str` - SHA256 hash of source file
- `JavaClass.generated_at: str` - ISO 8601 timestamp

### Command Line

New flag:
```bash
python3 hydocs.py --only-docs --skip-unchanged
```

### Documentation

- **[HASH_SYSTEM.md](HASH_SYSTEM.md)** - Complete guide to hash system
  - How it works
  - Usage examples
  - Performance metrics
  - CI/CD integration
  - Troubleshooting

### Use Cases

1. **Development Iteration:** Quick regeneration during development
2. **CI/CD Optimization:** Incremental builds in pipelines
3. **Auditability:** Track which files changed and when
4. **Integrity Verification:** Validate source file integrity

### Limitations

- Template changes require full rebuild
- Custom docs changes don't affect source hashes
- Deleted files remain in hash index (manual cleanup needed)

---

## 2026-01-18 - Major Documentation Structure Overhaul

### Overview
Implemented comprehensive improvements to the Hytale documentation structure to make it more AI-friendly, reduce duplication, and provide better context for LLMs and developers.

### Key Improvements

#### 1. **Eliminated Documentation Duplication**
- **Before:** Custom documentation was concatenated as a separate "Custom Documentation" section, causing:
  - Class titles appearing twice
  - Duplicate overview sections
  - Methods listed twice (generic + detailed)
- **After:** Custom documentation is now parsed and merged inline with auto-generated content
  - Overview from custom docs replaces generic placeholder
  - Method/field descriptions are merged directly into their respective sections
  - No duplication of structural elements

#### 2. **Full Qualified Names (FQN) Always Visible**
- **Before:** Type references showed only simple names (e.g., `ShutdownReason`)
- **After:** All non-primitive types now display their FQN alongside links:
  - Example: [`ShutdownReason`](ShutdownReason.md) - `com.hypixel.hytale.server.core.ShutdownReason`
  - Primitives show as: `int` (primitive)
  - Java standard library types show FQN: `String` - `java.lang.String`

#### 3. **Improved Template Structure**

**New Header Section:**
```markdown
# ClassName

**Full Qualified Name:** `com.hypixel.hytale.package.ClassName`
**Type:** class | interface | enum | @interface
**Package:** `com.hypixel.hytale.package`
**File Location:** `com/hypixel/hytale/package/ClassName.md`
```

**New Hierarchy Section:**
```markdown
## Hierarchy

**Extends:** [ParentClass](../path/to/ParentClass.md) - `com.hypixel.hytale.parent.ParentClass`

**Implements:**
- [InterfaceA](../path/to/InterfaceA.md) - `com.hypixel.hytale.interfaces.InterfaceA`

**Known Subclasses:** None

**Known Implementations:** None (for interfaces)
```

#### 4. **Enum Constants as Tables**
- **Before:** Bullet list format
- **After:** Clean markdown table with description column:
```markdown
| Constant | Description |
|----------|-------------|
| `CONSTANT_A` | Description from custom docs |
| `CONSTANT_B` | Another description |
```

#### 5. **Constructors Separated from Methods**
- **Before:** Constructors mixed with methods in a single section
- **After:** Dedicated `## Constructors` section before methods
- Constructor detection: Automatically identifies methods with same name as class

#### 6. **Related Types Section**
- **New:** Automatically tracks and lists all Hytale types used by the class
- Shows types from:
  - Parent class (extends)
  - Implemented interfaces
  - Field types
  - Method parameters
  - Method return types
  - Thrown exceptions
- Format: [`TypeName`](link.md) - `com.hypixel.hytale.full.qualified.Name`

#### 7. **Custom Documentation Parser**
New structured format for custom docs in `/docs/`:

```markdown
## Overview
[Concise description of class purpose - 2-3 lines]

## Field Descriptions
- `FIELD_NAME`: [Description of purpose]

## Constructor Descriptions
- `Constructor(params)`: [What this constructor does]

## Method Descriptions
- `methodName(params)`: [Useful description of what the method does]

## Usage Notes
[Notes about usage patterns, common pitfalls, etc]

## Examples
```java
// Practical usage examples
```
```

**No more structural duplication** - custom docs only contain descriptions, not structure.

#### 8. **Enhanced Navigation**
Added link to `class_lookup.json` in navigation section for AI tools:
```markdown
## Navigation
- [📦 Package Index (`com.hypixel.hytale.package`)](_index.md)
- [📚 Main Index](../../../INDEX.md)
- [🔍 Class Lookup JSON](../../../class_lookup.json)
```

### Technical Changes

#### New Functions Added
1. `parse_custom_docs(custom_file: str) -> Optional[CustomDocs]`
   - Parses new custom documentation format
   - Extracts overview, field descriptions, method descriptions, usage notes, examples

2. `get_full_qualified_name(type_name: str, current_pkg: str, imports: List[str], index: ClassIndex) -> str`
   - Resolves type names to their full qualified names
   - Handles Java standard library types
   - Returns empty string for primitives

#### Modified Functions
1. `make_type_link()` - Now returns `Tuple[str, str]`
   - Returns (markdown_link, full_qualified_name)
   - Enables showing both link and FQN

2. `generate_class_markdown()` - Completely rewritten
   - New template structure matching the plan
   - Inline merging of custom docs
   - Related types tracking
   - Separate constructor section
   - Enum constants as tables

#### New Data Classes
1. `CustomDocs` - Stores parsed custom documentation:
   - `overview: str`
   - `field_descriptions: Dict[str, str]`
   - `constructor_descriptions: Dict[str, str]`
   - `method_descriptions: Dict[str, str]`
   - `usage_notes: str`
   - `examples: str`

2. `JavaMethod.is_constructor: bool` - Added flag to identify constructors

### Benefits for AI/LLMs

1. ✅ **FQN Always Visible** → AI knows exactly which class to use
2. ✅ **Bidirectional Links** → AI can navigate easily between related types
3. ✅ **Clear Hierarchy** → AI understands class relationships
4. ✅ **Useful Descriptions** → AI understands purpose, not just signatures
5. ✅ **Consistent Format** → AI can parse structure reliably
6. ✅ **No Duplication** → Cleaner context, less confusion
7. ✅ **Related Types Section** → AI can discover type dependencies easily

### Verification Checklist

- ✅ No duplication of information
- ✅ FQN shown for all non-primitive types
- ✅ Functional links between related types
- ✅ Useful descriptions (no generic "Executes X behavior")
- ✅ Easy navigation for AI
- ✅ Consistent format across all files
- ✅ Enum constants in table format
- ✅ Constructors separated from methods
- ✅ Custom docs merged inline

### Example Output

See `/build/com/hypixel/hytale/Main.md` for a simple example.
See `/build/com/hypixel/hytale/server/core/HytaleServer.md` for a complex example with fields, methods, and related types.
See `/build/com/hypixel/hytale/server/core/universe/world/ValidationOption.md` for an enum example.

### Backward Compatibility

- ⚠️ Custom documentation format has changed
- Old format files will still work but won't be parsed correctly
- Migrate custom docs to new format (see `/docs/com/hypixel/hytale/Main.md` for example)

### Migration Guide for Custom Docs

**Old Format:**
```markdown
# ClassName

## Overview
- Documentation for ClassName
- Declared as a class

## Methods
- methodName(): Executes methodName behavior
```

**New Format:**
```markdown
## Overview
Concise description of the class purpose and behavior.

## Method Descriptions
- `methodName()`: Useful description of what the method actually does and when to use it.

## Usage Notes
- Important notes about usage patterns
- Common pitfalls to avoid
```

### Stats

- **Total Files Processed:** 4,851 classes
- **Documentation Generated:** 100% success rate
- **Custom Docs Updated:** 2 example files (Main.md, LateMain.md)
- **Time to Generate:** ~30 seconds (docs only, without decompilation)

### Next Steps (Optional Future Improvements)

1. Add "Used By" section (reverse dependencies)
2. Implement Known Subclasses tracking
3. Add syntax highlighting hints for method signatures
4. Generate inheritance diagrams
5. Add package-level overview docs
6. Create class dependency graph visualization
