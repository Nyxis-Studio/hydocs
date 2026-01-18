# AssetRegistry

**Overview**
Central registry for `AssetStore` instances and global tag indices.
Provides APIs to register/unregister stores and create/query tag indices.

**Constructors**
- Not applicable. Static utility class.

**Methods**
- `getStoreMap()`: returns the immutable map of registered stores.
- `getAssetStore(Class<T> tClass)`: fetches the store for a class.
- `register(S assetStore)`: registers a store and dispatches a register event.
- `unregister(S assetStore)`: removes a store and dispatches a removal event.
- `getTagIndex(String tag)`: returns a tag index or `TAG_NOT_FOUND`.
- `getOrCreateTagIndex(String tag)`: creates or returns a tag index.
- `registerClientTag(String tag)`: registers a client tag entry.
- `getClientTags()`: returns a copy of the client tag map.

**Notes**
- Uses `ASSET_LOCK` to synchronize store registration.
- Uses `TAG_LOCK`/`NEXT_TAG_INDEX` for thread-safe tag indexing.
