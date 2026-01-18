**Source Hash:** `a5b586db9104b6b808f96828dd4f9485524ade1c5c441eb55419e229b2b531b5`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetStoreEvent

## Overview
Base event class tied to an `AssetStore` instance. Used as a parent for asset store lifecycle events.

## Field Descriptions
- `assetStore`: Asset store associated with the event.

## Constructor Descriptions
- `AssetStoreEvent(AssetStore<?, ?, ?> assetStore)`: Stores the asset store reference.

## Method Descriptions
- `getAssetStore()`: Returns the associated asset store.
- `toString()`: Returns a string representation including the store.

## Usage Notes
- Implements `IEvent<KeyType>` for event system integration.

## Examples
```java
AssetStore<?, ?, ?> store = event.getAssetStore();
```
