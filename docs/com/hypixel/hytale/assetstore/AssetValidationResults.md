**Source Hash:** `e5eb55e67f489731705b226a766f4332d3477da5f0f6d8f67371bd8574470c34`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetValidationResults

## Overview
`ValidationResults` specialization for assets with missing-asset handling. Adds optional suppression for missing asset types and GitHub-specific logging that includes file/line context.

## Field Descriptions
- `disabledMissingAssetClasses`: Optional set of asset classes that should not throw missing-asset exceptions.

## Constructor Descriptions
- `AssetValidationResults(ExtraInfo extraInfo)`: Initializes validation results with asset extra info.

## Method Descriptions
- `handleMissingAsset(String field, Class<? extends JsonAsset> assetType, Object assetId)`: Throws a `MissingAssetException` unless the asset type is suppressed.
- `handleMissingAsset(String field, Class<? extends JsonAsset> assetType, Object assetId, String extra)`: Throws a `MissingAssetException` with extra detail unless suppressed.
- `disableMissingAssetFor(Class<? extends JsonAsset> assetType)`: Adds an asset class to the suppression set.
- `logOrThrowValidatorExceptions(HytaleLogger logger, String msg)`: Logs or throws validation issues using default formatting.
- `logOrThrowValidatorExceptions(HytaleLogger logger, String msg, Path path, int lineOffset)`: In GitHub mode, emits runner-formatted messages for each validation issue, resolving the path from `AssetExtraInfo` when missing.

## Usage Notes
- When GitHub formatting is enabled, warnings/errors are emitted using `GithubMessageUtil` before delegating to the base logger.

## Examples
```java
AssetValidationResults results = new AssetValidationResults(extraInfo);
results.disableMissingAssetFor(MyAsset.class);
```
