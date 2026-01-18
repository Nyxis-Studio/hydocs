**Source Hash:** `80e097253d8ec556022f04b23c7ca904d6a2827cf43955345badc16dda1d9754`
**Last Updated:** `2026-01-18T17:16:53-03:00`

## Overview
Enumerates strategies for assigning IDs and parent relationships to contained assets during decoding. These modes are used by `ContainedAssetCodec` and `RawAsset` to control tag inheritance and key generation.

## Field Descriptions
- `NONE`: Indicates no contained-asset behavior; unsupported by `ContainedAssetCodec`.
- `GENERATE_ID`: Generates a new key for the contained asset and does not inherit container tags.
- `INHERIT_ID`: Reuses the container's key and inherits container tags.
- `INHERIT_ID_AND_PARENT`: Reuses the container's key and fills in missing parent ids from the container metadata.
- `INJECT_PARENT`: Generates a new key and injects the container key as the parent when absent.

## Usage Notes
- `ContainedAssetCodec` throws if constructed with `NONE`.
- Tag inheritance is enabled for all modes except `GENERATE_ID`.

## Examples
```java
ContainedAssetCodec.Mode mode = ContainedAssetCodec.Mode.INJECT_PARENT;
```
