**Source Hash:** `1622af46e47522886106afd2f87a8eb97b0f26bb632c75fce8194de557991411`
**Last Updated:** `2026-01-18T17:16:53-03:00`

## Overview
Provides expected-count constants used by asset validation and organization. Centralizes fixed values so asset loaders and validators stay consistent.

## Field Descriptions
- `EXPECTED_CHILDREN_PER_ASSET`: Expected number of child entries per asset when estimating container sizes.
- `EXPECTED_ASSETS_PER_PATH`: Expected number of assets per asset path.
- `EXPECTED_VALUES_PER_TAG`: Expected number of values stored per tag key.
- `EXPECTED_ASSETS_PER_TAG`: Expected number of assets associated with a tag.

## Constructor Descriptions
- None. Constants-only class.

## Method Descriptions
- `none()`: Constants-only class.

## Usage Notes
- These constants are sizing hints used by asset store collections to reduce resizing.

## Examples
```java
int expected = AssetConstants.EXPECTED_ASSETS_PER_PATH;
```
