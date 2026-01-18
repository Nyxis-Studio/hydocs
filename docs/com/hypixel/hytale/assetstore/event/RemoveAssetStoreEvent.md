**Source Hash:** `91abfd513e682a6516abc2162c08fbdbd063d4f723f3f77b01e1ef7eb6869330`
**Last Updated:** `2026-01-18T17:16:53-03:00`

## Overview
Event fired when an `AssetStore` is unregistered from `AssetRegistry`. Provides a typed hook for listeners to react to store removal.

## Field Descriptions
- `none`: Event carries only the asset store reference from the base class.

## Constructor Descriptions
- `RemoveAssetStoreEvent(AssetStore<?, ?, ?> assetStore)`: Wraps the removed store.

## Method Descriptions
- `getAssetStore()`: Inherited from `AssetStoreEvent` to access the store.

## Usage Notes
- Extends `AssetStoreEvent<Void>` with no additional fields.

## Examples
```java
@Subscribe
public void onRemove(RemoveAssetStoreEvent event) {
    AssetStore<?, ?, ?> store = event.getAssetStore();
}
```
