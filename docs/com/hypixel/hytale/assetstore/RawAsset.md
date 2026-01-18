**Source Hash:** `16a2cc97037d096d658cefe7fcf13d247772190285c5d6197f9b97078d413b08`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# RawAsset

## Overview
Represents an asset in raw form, backed by a file path or an in-memory buffer. Stores key and parent information along with container data and contained-asset mode.

## Field Descriptions
- `parentPath`: Parent path for contained assets loaded from a larger file.
- `key`: Asset key when available.
- `lineOffset`: Line offset within the parent buffer.
- `parentKeyResolved`: Whether the parent key has been resolved.
- `parentKey`: Parent asset key when available.
- `path`: File path for standalone assets.
- `buffer`: Raw JSON buffer for contained assets.
- `containerData`: Metadata for the container asset, used for tag inheritance.
- `containedAssetMode`: Mode describing how contained assets inherit or generate identifiers.

## Constructor Descriptions
- `RawAsset(K key, Path path)`: Creates a raw asset from a file path without parent resolution.
- `RawAsset(Path parentPath, K key, K parentKey, int lineOffset, char[] buffer, AssetExtraInfo.Data containerData, ContainedAssetCodec.Mode containedAssetMode)`: Creates a raw asset from a buffer with resolved parent key and container metadata.

## Method Descriptions
- `getKey()`: Returns the asset key, if present.
- `isParentKeyResolved()`: Returns whether the parent key has been resolved.
- `getParentKey()`: Returns the parent key, if present.
- `getPath()`: Returns the asset path, if present.
- `getParentPath()`: Returns the parent asset path for contained assets.
- `getLineOffset()`: Returns the line offset for buffered assets.
- `getBuffer()`: Returns the raw buffer, if present.
- `getContainedAssetMode()`: Returns the contained-asset mode.
- `toRawJsonReader(Supplier<char[]> bufferSupplier)`: Creates a `RawJsonReader` from the file path or buffer.
- `makeData(Class<? extends JsonAssetWithMap<K, ?>> aClass, K key, K parentKey)`: Builds `AssetExtraInfo.Data`, inheriting tags based on the contained asset mode.
- `withResolveKeys(K key, K parentKey)`: Returns a copy with resolved keys and updated parent resolution state.
- `toString()`: Returns a diagnostic string including key, parent info, path, and buffer length.

## Usage Notes
- Tag inheritance is enabled for contained-asset modes that reuse or inject parent identifiers.

## Examples
```java
RawAsset<String> raw = new RawAsset<>(key, path);
RawJsonReader reader = raw.toRawJsonReader(bufferSupplier);
```
