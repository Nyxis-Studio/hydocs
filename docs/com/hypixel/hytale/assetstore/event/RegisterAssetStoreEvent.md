# RegisterAssetStoreEvent

**Overview**
Event fired when an `AssetStore` is registered in `AssetRegistry`.
Provides a typed hook for listeners to react to store registration.

**Constructors**
- `RegisterAssetStoreEvent(AssetStore<?, ?, ?> assetStore)`: wraps the registered store.

**Methods**
- Inherited from `AssetStoreEvent`.

**Notes**
- Extends `AssetStoreEvent<Void>` with no additional fields.
