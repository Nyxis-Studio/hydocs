# AssetValidationResults

**Overview**
`ValidationResults` specialization for assets with missing-asset handling.
Includes logging tailored for CI/GitHub with file and line context.

**Constructors**
- `AssetValidationResults(ExtraInfo extraInfo)`: initializes results with asset extra info.

**Methods**
- `handleMissingAsset(String field, Class<? extends JsonAsset> assetType, Object assetId)`: throws a missing asset exception.
- `handleMissingAsset(String field, Class<? extends JsonAsset> assetType, Object assetId, String extra)`: throws a missing asset exception with extra details.
- `disableMissingAssetFor(Class<? extends JsonAsset> assetType)`: disables missing-asset errors for a type.
- `logOrThrowValidatorExceptions(HytaleLogger logger, String msg)`: logs or throws validator issues with default formatting.
- `logOrThrowValidatorExceptions(HytaleLogger logger, String msg, Path path, int lineOffset)`: logs with optional path and line offset.

**Notes**
- Uses `AssetExtraInfo` to resolve asset paths when not provided.
- In GitHub mode, converts warnings/errors into runner-formatted messages.
