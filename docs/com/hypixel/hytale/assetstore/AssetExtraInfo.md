**Source Hash:** `6d823c9da8c7d5826af1a4cdd760a6e453f2ea08e9867e1e1e25978f492e461e`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetExtraInfo

## Overview
Carries extra asset metadata for validation and diagnostics during loading. Stores an optional asset path and a `Data` object that tracks the asset key, tags, and contained assets.

## Field Descriptions
- `assetPath`: Optional filesystem path associated with the asset being processed.
- `data`: Metadata container describing the asset, tags, and contained assets.

## Constructor Descriptions
- `AssetExtraInfo(Data data)`: Creates extra info without an asset path, using the provided metadata container.
- `AssetExtraInfo(Path assetPath, Data data)`: Creates extra info with the asset path and metadata container.

## Method Descriptions
- `generateKey()`: Builds a diagnostic key in `*<key>_<nextId>` format using the stored key and next identifier.
- `getKey()`: Returns the asset key from the metadata container.
- `getAssetPath()`: Returns the optional asset path.
- `getData()`: Returns the metadata container.
- `appendDetailsTo(StringBuilder sb)`: Appends the asset id and optional path to a diagnostics string.
- `getValidationResults()`: Returns validation results typed as `AssetValidationResults`.
- `toString()`: Returns a debug string including the asset path, data, and base `ExtraInfo` state.

## Usage Notes
- Extends `ExtraInfo` and always provisions `AssetValidationResults` for validation output.

## Examples
```java
AssetExtraInfo.Data data = new AssetExtraInfo.Data(MyAsset.class, key, parentKey);
AssetExtraInfo<?> info = new AssetExtraInfo<>(assetPath, data);
```

---

# AssetExtraInfo.Data

## Overview
Stores asset metadata during loading, including tags, parent/container links, and any contained assets. Builds tag indices for efficient queries and supports tag inheritance from container assets.

## Field Descriptions
- `TAG_VALUE_SEPARATOR`: Separator character used when composing `tag=value` entries.
- `containedAssets`: Map of loaded contained assets grouped by asset class.
- `containedRawAssets`: Map of raw contained assets grouped by asset class.
- `containerData`: Optional parent container metadata for inheritance.
- `assetClass`: The asset class associated with this metadata instance.
- `key`: Asset key for this metadata instance.
- `parentKey`: Parent asset key, if any.
- `rawTags`: Raw tag map keyed by tag name.
- `tagStorage`: Mutable tag-index storage keyed by tag index.
- `unmodifiableTagStorage`: Read-only view of tag index storage.
- `expandedTagStorage`: Expanded set of tag indices for tags and values.
- `unmodifiableExpandedTagStorage`: Read-only view of expanded tag indices.

## Constructor Descriptions
- `Data(Class<? extends JsonAsset<K>> assetClass, K key, K parentKey)`: Creates metadata for a single asset class, key, and parent key.
- `Data(Data containerData, Class<? extends JsonAsset<K>> aClass, K key, K parentKey, boolean inheritContainerTags)`: Creates metadata linked to a container and optionally inherits its tags.

## Method Descriptions
- `getAssetClass()`: Returns the asset class.
- `getKey()`: Returns the asset key.
- `getParentKey()`: Returns the parent key.
- `getRootContainerData()`: Walks up the container chain to return the root container metadata.
- `getContainerData()`: Returns the immediate container metadata, if any.
- `getContainerKey(Class<? extends JsonAsset<K>> aClass)`: Finds the container key for the specified class by walking up the container chain.
- `putTags(Map<String, String[]> tags)`: Registers raw tags, expands values into `tag=value` entries, and populates tag index sets.
- `getRawTags()`: Returns an unmodifiable view of the raw tag map.
- `getTags()`: Returns an unmodifiable view of tag index storage.
- `getExpandedTagIndexes()`: Returns an unmodifiable view of expanded tag indices.
- `getTag(int tagIndex)`: Returns the tag value index set for the given tag index, or empty if missing.
- `addContainedAsset(Class<T> assetClass, T asset)`: Adds a loaded asset instance to the contained-assets map.
- `addContainedAsset(Class<T> assetClass, RawAsset<K> rawAsset)`: Adds a raw asset instance to the contained-raw-assets map.
- `fetchContainedAssets(K key, Map<Class<? extends JsonAssetWithMap>, Map<K, List<Object>>> containedAssets)`: Adds contained assets for the provided key into the provided aggregation map.
- `fetchContainedRawAssets(K key, Map<Class<? extends JsonAssetWithMap>, Map<K, List<RawAsset<Object>>>> containedAssets)`: Adds contained raw assets for the provided key into the provided aggregation map.
- `containsAsset(Class<T> tClass, K key)`: Returns whether a contained asset or raw asset with the key exists for the given class.
- `loadContainedAssets(boolean reloading)`: Loads contained assets and raw buffers via their asset stores using the default update query.
- `toString()`: Returns a debug string with contained assets, tags, parent, class, and key.

## Usage Notes
- Uses `AssetRegistry` tag indices to accelerate queries and validation.
- Exposes unmodifiable tag views for safe external access.

## Examples
```java
AssetExtraInfo.Data data = new AssetExtraInfo.Data(MyAsset.class, key, parentKey);
data.putTags(tags);
```
