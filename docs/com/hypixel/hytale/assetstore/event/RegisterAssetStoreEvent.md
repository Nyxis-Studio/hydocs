**Source Hash:** `7b0a3977cef0573376a590321d627e0c0d648acd65b2554a3eafb67cae58bc6d`
**Last Updated:** `2026-01-18T17:16:53-03:00`

## Overview
Event fired when an `AssetStore` is registered in `AssetRegistry`. Provides a typed hook for listeners to react to store registration.

## Field Descriptions
- `none`: Event carries only the asset store reference from the base class.

## Constructor Descriptions
- `RegisterAssetStoreEvent(AssetStore<?, ?, ?> assetStore)`: Wraps the registered store.

## Method Descriptions
- `getAssetStore()`: Inherited from `AssetStoreEvent` to access the store.

## Usage Notes
- Extends `AssetStoreEvent<Void>` with no additional fields.

## Examples
```java
@Subscribe
public void onRegister(RegisterAssetStoreEvent event) {
    AssetStore<?, ?, ?> store = event.getAssetStore();
}
```
