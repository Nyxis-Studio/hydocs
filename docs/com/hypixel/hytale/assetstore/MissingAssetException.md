# MissingAssetException

**Overview**
Runtime exception thrown when a referenced asset cannot be resolved.
Supports optional extra context and integration with validation results.

**Constructors**
- `MissingAssetException(String field, Class<? extends JsonAsset> assetType, Object assetId)`: builds a standard missing-asset message.
- `MissingAssetException(String field, Class<? extends JsonAsset> assetType, Object assetId, String extra)`: adds extra context to the message.

**Methods**
- `getField()`: returns the field name that referenced the asset.
- `getAssetType()`: returns the expected asset type.
- `getAssetId()`: returns the missing asset id.
- `handle(ExtraInfo extraInfo, String field, Class<? extends JsonAsset> assetType, Object assetId)`: delegates to `AssetValidationResults` when available.
- `handle(ExtraInfo extraInfo, String field, Class<? extends JsonAsset> assetType, Object assetId, String extra)`: delegates with extra context.

**Notes**
- Falls back to throwing directly when the validation results are not asset-aware.
