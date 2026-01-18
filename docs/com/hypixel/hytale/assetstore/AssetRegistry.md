**Source Hash:** `c4104e7c542d27ddbf4a049a58c0153d842094a74fc2db9f3b767ddf62c83a75`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetRegistry

## Overview
Central registry for `AssetStore` instances and global tag indices. Manages registration events, tag indexing, and client tag tracking with thread-safe locks.

## Field Descriptions
- `ASSET_LOCK`: Read/write lock guarding asset store registration.
- `HAS_INIT`: Flag used by callers to track registry initialization state.
- `TAG_NOT_FOUND`: Sentinel value returned when a tag is missing.
- `storeMap`: Mutable map of asset stores keyed by asset class.
- `storeMapUnmodifiable`: Read-only view of registered stores.
- `NEXT_TAG_INDEX`: Atomic counter for allocating new tag indices.
- `TAG_LOCK`: Stamped lock used to guard tag maps.
- `TAG_MAP`: Tag name to index map with default return value of `TAG_NOT_FOUND`.
- `CLIENT_TAG_MAP`: Client tag map with default return value of `TAG_NOT_FOUND`.

## Constructor Descriptions
- None. Static utility class.

## Method Descriptions
- `getStoreMap()`: Returns the unmodifiable map of registered asset stores.
- `getAssetStore(Class<T> tClass)`: Returns the asset store for the given asset class.
- `register(AssetStore assetStore)`: Registers the asset store, throws if already registered, and dispatches `RegisterAssetStoreEvent` if listeners are present.
- `unregister(AssetStore assetStore)`: Unregisters the asset store and dispatches `RemoveAssetStoreEvent` if listeners are present.
- `getTagIndex(String tag)`: Returns the tag index or `TAG_NOT_FOUND`; throws if tag is null.
- `getOrCreateTagIndex(String tag)`: Returns the tag index, creating one if missing; throws if tag is null.
- `registerClientTag(String tag)`: Registers a tag in the client map and returns true if it was newly added.
- `getClientTags()`: Returns a copy of the client tag map.

## Usage Notes
- Registration uses `ASSET_LOCK` for thread safety; tag access uses `TAG_LOCK`.
- Tag maps intern keys and default to `TAG_NOT_FOUND` when absent.

## Examples
```java
AssetRegistry.register(store);
int tagIndex = AssetRegistry.getOrCreateTagIndex("biome");
```
