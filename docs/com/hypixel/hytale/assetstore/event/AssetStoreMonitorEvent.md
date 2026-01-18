# AssetStoreMonitorEvent

**Overview**
Concrete monitor event that includes the `AssetStore` impacted by changes.
Extends `AssetMonitorEvent` to add store context for reload/unload logic.

**Constructors**
- `AssetStoreMonitorEvent(String assetPack, AssetStore<?, ?, ?> assetStore, List<Path> createdOrModified, List<Path> removed, List<Path> createdOrModifiedDirectories, List<Path> removedDirectories)`: initializes the event with store and change lists.

**Methods**
- `getAssetStore()`: returns the affected asset store.
- `toString()`: returns a textual representation including the store.

**Notes**
- Uses `Void` as the event type parameter.
