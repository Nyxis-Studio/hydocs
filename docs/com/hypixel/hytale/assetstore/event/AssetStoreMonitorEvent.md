**Source Hash:** `6d6a5266ad07bd1791a414e3bf8a99ce4dc41d8eb7727c3b5b8af9402726823a`
**Last Updated:** `2026-01-18T17:16:53-03:00`

# AssetStoreMonitorEvent

## Overview
Concrete monitor event that includes the `AssetStore` impacted by changes. Extends `AssetMonitorEvent` to add store context for reload/unload logic.

## Field Descriptions
- `assetStore`: Asset store affected by the filesystem changes.

## Constructor Descriptions
- `AssetStoreMonitorEvent(String assetPack, AssetStore<?, ?, ?> assetStore, List<Path> createdOrModified, List<Path> removed, List<Path> createdOrModifiedDirectories, List<Path> removedDirectories)`: Initializes the event with store and change lists.

## Method Descriptions
- `getAssetStore()`: Returns the affected asset store.
- `toString()`: Returns a textual representation including the store.

## Usage Notes
- Uses `Void` as the event type parameter.

## Examples
```java
AssetStore<?, ?, ?> store = event.getAssetStore();
```
