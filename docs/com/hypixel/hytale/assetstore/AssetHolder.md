**Source Hash:** `86b5ad95130c32e41704d60eb101d0840c3a7d1d1ea5daac1774a6ae27facf4f`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetHolder

## Overview
Marker interface for types that represent or hold assets. Acts as a generic constraint within the asset store ecosystem.

## Field Descriptions
- `none`: Interface-only contract; no fields.

## Constructor Descriptions
- `none()`: Interface type.

## Method Descriptions
- `none()`: Marker interface with no methods.

## Usage Notes
- Use the `K` type parameter to specify the asset key type.

## Examples
```java
public final class MyAsset implements AssetHolder<String> {
}
```
