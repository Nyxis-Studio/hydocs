# Hydocs - Hytale Server Documentation Generator

Automated documentation generator for the Hytale Server. Decompiles the server JAR file and produces comprehensive Markdown documentation with MCP integration support.

## Features

- **Automatic Decompilation**: Uses CFR decompiler to convert Java bytecode to readable source
- **AI-Optimized Markdown**: Generates clean, navigable documentation optimized for LLMs
- **Full Qualified Names**: All types show FQN alongside links for precise resolution
- **Class Lookup Index**: Creates `class_lookup.json` for MCP server integration
- **Smart Custom Documentation**: Merges user-provided descriptions inline (no duplication)
- **Related Types Tracking**: Automatically discovers and links type dependencies
- **Hash-Based Change Detection**: Tracks file changes via SHA256 hashes for incremental builds
- **GitHub Actions Integration**: Automated builds and S3 publishing
- **Version Management**: Maintains versioned documentation with stable "latest" URLs

## Quick Start

### Local Usage

#### Prerequisites

- **Python 3.11+** (stdlib only, no external dependencies)
- **Java 17+** (for CFR decompiler)

#### Generate Documentation

```bash
# Download Hytale Server JAR
curl -L -o lib/HytaleServer.jar https://example.com/HytaleServer.jar

# Generate documentation
python3 hydocs.py --file lib/HytaleServer.jar --output build

# View output
ls build/
```

#### Output Structure

```
build/
├── INDEX.md                          # Main documentation index
├── class_lookup.json                 # Class lookup for MCP integration
├── com/hypixel/hytale/               # Generated class documentation
│   ├── Example.md
│   ├── util/
│   │   └── Helper.md
│   └── ...
└── custom/                           # Merged from docs/ directory
    └── guides.md
```

### Command Line Options

```bash
python3 hydocs.py --help

Usage: hydocs.py [OPTIONS]

Options:
  --file PATH            Path to the Hytale Server JAR file
  --output PATH          Output directory (default: build)
  --skip-unchanged       Skip files that haven't changed (incremental build)
  --only-docs            Skip decompilation, only generate docs
  --help                 Show this help message
```

### Incremental Builds (Hash System)

Hydocs tracks file changes using SHA256 hashes for faster regeneration:

```bash
# First build: Generates all files
python3 hydocs.py --only-docs
# ✅ Generated 4851 files (skipped 0 unchanged, 0 changed)

# Incremental build: Skips unchanged files
python3 hydocs.py --only-docs --skip-unchanged
# ✅ Generated 63 files (skipped 4788 unchanged, 63 changed)
```

**Performance:** Up to 99% faster when few files changed!

See **[HASH_SYSTEM.md](HASH_SYSTEM.md)** for complete documentation.

## Automated Workflow

### GitHub Actions Setup

This project includes a GitHub Actions workflow that automatically generates and publishes documentation to S3/MinIO.

#### 1. Configure Secrets

Go to **Settings** → **Secrets and variables** → **Actions** and add:

| Secret | Description | Example |
|--------|-------------|---------|
| `S3_ENDPOINT` | S3/MinIO endpoint URL | `https://minio.example.com` |
| `S3_ACCESS_KEY_ID` | S3 access key | `your-access-key` |
| `S3_SECRET_ACCESS_KEY` | S3 secret key | `your-secret-key` |
| `S3_BUCKET` | Target bucket name | `hytale-docs` |
| `S3_REGION` | S3 region | `us-east-1` or `auto` |
| `JAR_DOWNLOAD_URL` | Default JAR download URL | `https://cdn.example.com/server.jar` |

#### 2. Run the Workflow

**Via Web Interface:**
1. Go to the **Actions** tab
2. Select **"Generate Hytale Documentation"**
3. Click **"Run workflow"**
4. (Optional) Provide custom inputs
5. Click **"Run workflow"**

**Via GitHub CLI:**
```bash
# Run with defaults
gh workflow run generate-docs.yml

# Run with custom version tag
gh workflow run generate-docs.yml -f version_tag=v1.0.0

# Run with custom JAR URL
gh workflow run generate-docs.yml -f jar_url=https://example.com/custom.jar
```

#### 3. Access Published Documentation

After the workflow completes, documentation is available at:

- **Latest (Stable URL)**: `https://your-endpoint/your-bucket/latest/INDEX.md`
- **Class Lookup**: `https://your-endpoint/your-bucket/latest/class_lookup.json`
- **Specific Version**: `https://your-endpoint/your-bucket/versions/v1.0.0/INDEX.md`
- **All Versions**: `https://your-endpoint/your-bucket/versions.json`

See [.github/workflows/README.md](.github/workflows/README.md) for detailed workflow documentation.

## S3 Storage Structure

```
s3://your-bucket/
├── latest/                    # Always points to most recent build
│   ├── INDEX.md
│   ├── class_lookup.json
│   ├── VERSION.json
│   └── com/hypixel/hytale/...
│
├── versions/                  # Historical builds
│   ├── commit-abc123/
│   ├── commit-def456/
│   └── v1.0.0/
│
└── versions.json              # List of all versions
```

## MCP Integration

The generated `class_lookup.json` enables integration with Model Context Protocol (MCP) servers.

### Configuration Example

```json
{
  "mcpServers": {
    "hytale-docs": {
      "command": "mcp-server",
      "args": ["--class-lookup", "https://your-endpoint/your-bucket/latest/class_lookup.json"]
    }
  }
}
```

### Class Lookup Format

```json
{
  "com.hypixel.hytale.Example": "com/hypixel/hytale/Example.md",
  "com.hypixel.hytale.util.Helper": "com/hypixel/hytale/util/Helper.md"
}
```

To retrieve documentation for a class:
```
https://your-endpoint/your-bucket/latest/{path_from_lookup}
```

## Custom Documentation

Enhance auto-generated documentation with meaningful descriptions using the new custom docs format.

### Quick Start

1. **Create custom docs** in `/docs/` following the package structure:
   ```
   docs/com/hypixel/hytale/Main.md
   ```

2. **Use the new format** (descriptions only, no structure):
   ```markdown
   ## Overview
   Entry point class for the Hytale server. Handles JVM initialization.

   ## Method Descriptions
   - `main(String[] args)`: Main entry point. Initializes transforming class loader.

   ## Usage Notes
   - Always launch through this main class for proper initialization
   ```

3. **Generate documentation**:
   ```bash
   python3 hydocs.py --only-docs
   ```

### Documentation Resources

- **[📘 AI Reference Guide](AI_REFERENCE_GUIDE.md)** - Quick reference for LLMs (Portuguese)
- **[📗 Custom Docs Guide](CUSTOM_DOCS_GUIDE.md)** - Complete guide for writing custom docs
- **[📕 Example Template](EXAMPLE_CUSTOM_DOCS.md)** - Full example with all fields
- **[📙 Changelog](CHANGELOG.md)** - Recent improvements and changes

### Validation & Migration Tools

**Validate custom docs format:**
```bash
python3 validate_custom_docs.py --docs docs
```

**Migrate old format to new:**
```bash
# Preview changes
python3 migrate_custom_docs.py --docs docs --dry-run

# Apply migration
python3 migrate_custom_docs.py --docs docs
```

### New Documentation Template

Custom docs are now merged **inline** with auto-generated content:

**Before (Old Format - Duplicated):**
- Class title appeared twice
- Overview duplicated
- Methods listed twice

**After (New Format - Merged):**
- Overview from custom docs replaces generic placeholder
- Method descriptions merged into auto-generated sections
- Zero duplication, cleaner output

**Example Output Structure:**
```markdown
# ClassName

**Full Qualified Name:** `com.hypixel.hytale.package.ClassName`
**Type:** class

## Overview
[Your custom description here]

## Declaration
```java
public class ClassName extends Parent
```

## Methods

### `methodName(...)`
```java
public ReturnType methodName(ParamType param)
```

**Returns:** [`ReturnType`](link.md) - `com.hypixel.hytale.types.ReturnType`
**Parameters:**
- `param`: [`ParamType`](link.md) - `com.hypixel.hytale.types.ParamType`

**Description:** [Your custom description merged here]
```

See **[EXAMPLE_CUSTOM_DOCS.md](EXAMPLE_CUSTOM_DOCS.md)** for a complete reference.

## How It Works

1. **JAR Download**: Downloads Hytale Server JAR from configured URL
2. **Decompilation**: Uses CFR decompiler (bundled) to convert bytecode to Java source
3. **Markdown Generation**: Converts decompiled source to formatted Markdown
4. **Index Creation**: Generates `INDEX.md` with navigation and `class_lookup.json` for programmatic access
5. **Custom Docs Merge**: Copies files from `docs/` directory
6. **S3 Upload**: (Workflow only) Publishes to S3 with versioning and public access

## Version Management

### Version Determination

The workflow determines version in this order:

1. **Workflow Input**: Manual `version_tag` parameter
2. **Git Tag**: If current commit has a tag (e.g., `v1.0.0`)
3. **Commit SHA**: Fallback to `commit-<7-char-sha>`

### Versioned URLs

Each build creates a unique versioned path:
- `versions/commit-abc123/`
- `versions/v1.0.0/`

The `latest/` directory always points to the most recent build.

## Troubleshooting

### Local Execution Issues

**"Java not found"**
```bash
# Install Java 17
sudo apt-get install openjdk-17-jdk  # Ubuntu/Debian
brew install openjdk@17               # macOS
```

**"Permission denied"**
```bash
chmod +x hydocs.py
```

**"JAR file not found"**
- Ensure the JAR path is correct
- Check that the file exists: `ls -lh lib/HytaleServer.jar`

### GitHub Actions Issues

**JAR Download Fails**
- Verify `JAR_DOWNLOAD_URL` secret is set
- Test URL manually: `curl -I <url>`
- Check if URL requires authentication

**S3 Upload Fails**
- Verify all S3 secrets are correct
- Test credentials: `mc alias set test $ENDPOINT $KEY $SECRET`
- Ensure bucket exists

**Documentation Generation Fails**
- Check JAR file is valid (not an error page)
- Review workflow logs for decompilation errors
- Test locally first

See [.github/workflows/README.md](.github/workflows/README.md) for detailed troubleshooting.

## Project Structure

```
hydocs/
├── .github/
│   └── workflows/
│       ├── generate-docs.yml           # Main workflow
│       └── README.md                   # Workflow documentation
├── docs/                               # Custom documentation (optional)
│   └── com/hypixel/hytale/
│       ├── Main.md                     # Example custom docs
│       └── ...
├── lib/                                # Downloaded JARs
│   ├── HytaleServer.jar
│   └── src/                            # Decompiled source
├── build/                              # Generated output
│   ├── INDEX.md
│   ├── class_lookup.json
│   ├── hashes.json                     # SHA256 hash index
│   └── com/hypixel/hytale/...
├── hydocs.py                           # Main documentation generator
├── validate_custom_docs.py             # Custom docs validator
├── migrate_custom_docs.py              # Format migration tool
├── AI_REFERENCE_GUIDE.md               # Quick reference for LLMs (PT)
├── CUSTOM_DOCS_GUIDE.md                # Complete custom docs guide (EN)
├── EXAMPLE_CUSTOM_DOCS.md              # Full example template
├── HASH_SYSTEM.md                      # Hash-based change detection guide
├── CHANGELOG.md                        # Recent improvements
├── IMPLEMENTATION_SUMMARY.md           # Implementation details
├── LICENSE                             # MIT License
└── README.md                           # This file
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly (local generation + workflow)
5. Submit a pull request

### Development

```bash
# Clone repository
git clone https://github.com/your-org/hydocs.git
cd hydocs

# Test local generation
python3 hydocs.py --file path/to/server.jar --output test-output

# Verify output
ls test-output/INDEX.md
cat test-output/class_lookup.json | jq .
```

## Security

- **JAR Sources**: Only process JARs from trusted sources
- **Secrets Management**: Never commit S3 credentials to git
- **Public Access**: Generated documentation is publicly readable
- **Decompilation**: CFR runs in isolated process, but still validate JAR integrity

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **CFR Decompiler**: By Lee Benfield ([benf.org/other/cfr](https://www.benf.org/other/cfr/))
- **Hytale**: By Hypixel Studios
- **MinIO Client**: By MinIO ([min.io](https://min.io))

## Support

For issues and questions:

- **GitHub Issues**: [github.com/your-org/hydocs/issues](https://github.com/your-org/hydocs/issues)
- **Workflow Documentation**: [.github/workflows/README.md](.github/workflows/README.md)
- **Discussions**: [github.com/your-org/hydocs/discussions](https://github.com/your-org/hydocs/discussions)

---

**Note**: This project is not affiliated with or endorsed by Hypixel Studios or Hytale. It is a community tool for documentation purposes.
