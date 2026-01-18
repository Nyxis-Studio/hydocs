# RemoveAssetStoreEvent

**Overview**
Event fired when an `AssetStore` is unregistered from `AssetRegistry`.
Provides a typed hook for listeners to react to store removal.

**Constructors**
- `RemoveAssetStoreEvent(AssetStore<?, ?, ?> assetStore)`: wraps the removed store.

**Methods**
- Inherited from `AssetStoreEvent`.

**Notes**
- Extends `AssetStoreEvent<Void>` with no additional fields.
