# GitHub Actions Workflow Documentation

This directory contains the automated workflow for generating and publishing Hytale Server documentation to S3/MinIO.

## Workflow: `generate-docs.yml`

Automatically decompiles the Hytale Server JAR, generates Markdown documentation, and publishes it to S3 with versioning.

### Features

- **Automated Documentation Generation**: Uses `hydocs.py` to decompile and document Hytale Server classes
- **S3/MinIO Publishing**: Deploys documentation to any S3-compatible storage
- **Version Management**: Maintains versioned builds and a stable "latest" URL
- **Public Access**: Configures public URLs for easy sharing
- **MCP Integration Ready**: Generates `class_lookup.json` for MCP server integration

## Setup Instructions

### 1. Configure GitHub Secrets

Navigate to your repository: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add the following secrets:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `S3_ENDPOINT` | S3 or MinIO endpoint URL | `https://minio.example.com` |
| `S3_ACCESS_KEY_ID` | Access key for S3 authentication | `minio-access-key` |
| `S3_SECRET_ACCESS_KEY` | Secret key for S3 authentication | `minio-secret-key` |
| `S3_BUCKET` | Target bucket name | `hytale-docs` |
| `S3_REGION` | S3 region (use `auto` for MinIO) | `us-east-1` or `auto` |
| `JAR_DOWNLOAD_URL` | Default URL to download Hytale Server JAR | `https://example.com/HytaleServer.jar` |

### 2. Verify S3 Bucket Exists

Ensure your S3 bucket is created before running the workflow. The workflow will attempt to create it if it doesn't exist, but this requires appropriate permissions.

```bash
# Using MinIO Client (mc)
mc alias set myminio https://minio.example.com ACCESS_KEY SECRET_KEY
mc mb myminio/hytale-docs
```

### 3. Run the Workflow

#### Via GitHub Web Interface

1. Go to **Actions** tab
2. Select **"Generate Hytale Documentation"** workflow
3. Click **"Run workflow"** button
4. (Optional) Provide custom inputs:
   - **jar_url**: Override the JAR download URL
   - **version_tag**: Set a custom version tag (e.g., `v1.0.0`)
5. Click **"Run workflow"**

#### Via GitHub CLI

```bash
# Run with defaults (uses secrets)
gh workflow run generate-docs.yml

# Run with custom JAR URL
gh workflow run generate-docs.yml -f jar_url=https://example.com/custom.jar

# Run with custom version tag
gh workflow run generate-docs.yml -f version_tag=v1.0.0

# Run with both custom inputs
gh workflow run generate-docs.yml \
  -f jar_url=https://example.com/custom.jar \
  -f version_tag=v1.0.0
```

## S3 Storage Structure

The workflow creates the following directory structure in S3:

```
s3://hytale-docs/
├── latest/                          # Always points to most recent build
│   ├── INDEX.md                     # Main documentation index
│   ├── class_lookup.json            # Class lookup index for MCP
│   ├── VERSION.json                 # Build metadata
│   └── com/hypixel/hytale/...       # Documentation files
│
├── versions/                        # Versioned builds archive
│   ├── commit-abc123/               # Build from commit abc123
│   │   ├── INDEX.md
│   │   ├── class_lookup.json
│   │   └── ...
│   ├── commit-def456/               # Build from commit def456
│   └── v1.0.0/                      # Build from tag v1.0.0
│
└── versions.json                    # List of all available versions
```

### Version Determination Logic

The workflow determines the version in this priority order:

1. **Manual Input**: `version_tag` workflow input
2. **Git Tag**: If current commit has a git tag
3. **Commit SHA**: Format `commit-<7-char-sha>` as fallback

### Public URLs

After deployment, documentation is accessible via public URLs:

- **Latest Index**: `https://minio.example.com/hytale-docs/latest/INDEX.md`
- **Latest Class Lookup**: `https://minio.example.com/hytale-docs/latest/class_lookup.json`
- **Specific Version**: `https://minio.example.com/hytale-docs/versions/v1.0.0/INDEX.md`
- **Versions List**: `https://minio.example.com/hytale-docs/versions.json`

## Workflow Jobs

### Job 1: Build Documentation

1. **Checkout Repository**: Clones the hydocs repository
2. **Setup Java 17**: Installs Temurin JDK 17 (required for CFR decompiler)
3. **Setup Python 3.11+**: Installs Python (hydocs.py uses stdlib only)
4. **Determine Version**: Resolves version from input/tag/commit
5. **Determine JAR URL**: Uses input or secret
6. **Download JAR**: Downloads Hytale Server JAR file
7. **Generate Docs**: Runs `hydocs.py --file lib/HytaleServer.jar --output build`
8. **Create Metadata**: Generates `VERSION.json` with build info
9. **Upload Artifacts**: Saves build output for debugging (30-day retention)

### Job 2: Deploy to S3

1. **Download Artifacts**: Retrieves build output from Job 1
2. **Install MinIO Client**: Downloads `mc` CLI tool
3. **Configure S3 Alias**: Authenticates with S3/MinIO
4. **Upload Versioned Docs**: Copies to `versions/<VERSION>/`
5. **Update Latest**: Overwrites `latest/` with new build
6. **Set Public Access**: Enables public download permissions
7. **Generate Versions List**: Creates/updates `versions.json`
8. **Job Summary**: Outputs public URLs and instructions

## Troubleshooting

### JAR Download Fails

**Error**: `Error: Failed to download JAR file`

**Solutions**:
- Verify `JAR_DOWNLOAD_URL` secret is set correctly
- Test URL manually: `curl -I <JAR_URL>`
- Check if URL requires authentication
- Ensure URL is publicly accessible or use a different source

### S3 Upload Fails

**Error**: `mc: <ERROR> Unable to make bucket`

**Solutions**:
- Verify all S3 secrets are configured correctly
- Check S3_ENDPOINT format: must include `https://` or `http://`
- Test credentials manually:
  ```bash
  mc alias set test $S3_ENDPOINT $ACCESS_KEY $SECRET_KEY
  mc ls test/
  ```
- Ensure bucket exists or service account has `s3:CreateBucket` permission

### Documentation Generation Fails

**Error**: `Error: Documentation generation failed - INDEX.md not found`

**Solutions**:
- Check if JAR file is valid (not HTML error page)
- Verify Java 17 is working: check workflow logs
- Review `hydocs.py` output for decompilation errors
- Test locally: `python3 hydocs.py --file <jar> --output build`

### Public Access Not Working

**Error**: 403 Forbidden when accessing public URLs

**Solutions**:
- Check bucket policy allows public reads
- Verify MinIO has `mc anonymous set download` support
- For AWS S3, may need to set bucket policy manually:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::hytale-docs/*"
    }]
  }
  ```

## MCP Server Integration

To integrate with an MCP server:

1. Use the stable URL for `class_lookup.json`:
   ```
   https://minio.example.com/hytale-docs/latest/class_lookup.json
   ```

2. Configure your MCP server to fetch this file periodically

3. The `class_lookup.json` format:
   ```json
   {
     "com.hypixel.hytale.Example": "com/hypixel/hytale/Example.md",
     "com.hypixel.hytale.util.Helper": "com/hypixel/hytale/util/Helper.md"
   }
   ```

4. Construct full documentation URLs:
   ```
   https://minio.example.com/hytale-docs/latest/com/hypixel/hytale/Example.md
   ```

## Advanced Usage

### Trigger on Git Tag Push

To automatically run the workflow when you push a version tag:

```yaml
# Add to .github/workflows/generate-docs.yml under 'on:'
on:
  push:
    tags:
      - 'v*.*.*'  # Triggers on v1.0.0, v2.1.3, etc.
  workflow_dispatch:
    # ... existing inputs
```

### Schedule Regular Builds

To generate documentation daily (e.g., to catch upstream JAR updates):

```yaml
# Add to .github/workflows/generate-docs.yml under 'on:'
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC
  workflow_dispatch:
    # ... existing inputs
```

### Custom Storage Regions

For AWS S3 with specific regions:

```yaml
# Update the "Configure S3 alias" step
mc alias set s3storage \
  "https://s3.${{ secrets.S3_REGION }}.amazonaws.com" \
  "$S3_ACCESS_KEY_ID" \
  "$S3_SECRET_ACCESS_KEY"
```

## Security Considerations

- **Secrets**: Never commit S3 credentials to git. Always use GitHub Secrets.
- **Public Access**: Documentation is publicly readable. Don't include sensitive information.
- **JAR Source**: Only use trusted JAR sources to prevent malicious code execution during decompilation.
- **S3 Costs**: Public downloads may incur egress costs. Monitor usage.

## Contributing

If you improve this workflow:

1. Test changes thoroughly in a fork
2. Document new secrets/requirements
3. Update this README
4. Submit a pull request

## License

This workflow is part of the Hydocs project and follows the same license (MIT).
