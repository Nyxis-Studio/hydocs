# AssetStoreEvent

**Overview**
Base event class tied to an `AssetStore` instance.
Used as a parent for events such as register or remove store notifications.

**Constructors**
- `AssetStoreEvent(AssetStore<?, ?, ?> assetStore)`: stores the asset store reference.

**Methods**
- `getAssetStore()`: returns the associated asset store.
- `toString()`: returns a textual representation including the store.

**Notes**
- Implements `IEvent<KeyType>` for event system integration.
