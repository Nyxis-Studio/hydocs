# RawAsset

**Overview**
Represents an asset in raw form, backed by a file path or an in-memory buffer.
Stores key and parent information along with container data and contained-asset mode.

**Constructors**
- `RawAsset(K key, Path path)`: creates a raw asset from a file path without parent resolution.
- `RawAsset(Path parentPath, K key, K parentKey, int lineOffset, char[] buffer, AssetExtraInfo.Data containerData, ContainedAssetCodec.Mode containedAssetMode)`: creates a raw asset from a buffer and parent context.
- `RawAsset(K key, boolean parentKeyResolved, K parentKey, Path path, char[] buffer, AssetExtraInfo.Data containerData, ContainedAssetCodec.Mode containedAssetMode)`: internal constructor used by key resolution.

**Methods**
- `getKey()`: returns the asset key, if present.
- `isParentKeyResolved()`: indicates whether the parent key is resolved.
- `getParentKey()`: returns the parent key, if present.
- `getPath()`: returns the asset path if backed by a file.
- `getParentPath()`: returns the parent path for contained assets.
- `getLineOffset()`: returns the line offset for buffered assets.
- `getBuffer()`: returns the raw buffer, if present.
- `getContainedAssetMode()`: returns the contained-asset mode.
- `toRawJsonReader(Supplier<char[]> bufferSupplier)`: opens a `RawJsonReader` from path or buffer.
- `makeData(Class<? extends JsonAssetWithMap<K, ?>> aClass, K key, K parentKey)`: creates `AssetExtraInfo.Data` with tag inheritance based on mode.
- `withResolveKeys(K key, K parentKey)`: returns a new `RawAsset` with resolved keys.
- `toString()`: returns a diagnostic string.

**Notes**
- Uses `ContainedAssetCodec.Mode` to decide whether tags are inherited.
