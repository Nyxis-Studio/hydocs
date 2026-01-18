**Source Hash:** `4b29ad8884a8f4de60c251843120a5d25d3d0a500ac5bc6fac7943c53c75ab2e`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# MissingAssetException

## Overview
Runtime exception thrown when a referenced asset cannot be resolved. Provides static helpers that delegate to `AssetValidationResults` when available.

## Field Descriptions
- `field`: Field name that referenced the missing asset.
- `assetType`: Asset class that was expected.
- `assetId`: Identifier of the missing asset.

## Constructor Descriptions
- `MissingAssetException(String field, Class<? extends JsonAsset> assetType, Object assetId)`: Builds a standard missing-asset message.
- `MissingAssetException(String field, Class<? extends JsonAsset> assetType, Object assetId, String extra)`: Builds the message with extra context appended.

## Method Descriptions
- `getField()`: Returns the field name that referenced the asset.
- `getAssetType()`: Returns the expected asset type.
- `getAssetId()`: Returns the missing asset id.
- `handle(ExtraInfo extraInfo, String field, Class<? extends JsonAsset> assetType, Object assetId)`: Delegates missing-asset handling to `AssetValidationResults` when available, otherwise throws immediately.
- `handle(ExtraInfo extraInfo, String field, Class<? extends JsonAsset> assetType, Object assetId, String extra)`: Delegates missing-asset handling with extra context when available, otherwise throws immediately.

## Usage Notes
- Use the static `handle` helpers when you want missing-asset behavior to respect validation result configuration.

## Examples
```java
MissingAssetException.handle(extraInfo, "weapon", WeaponAsset.class, "sword_01");
```
