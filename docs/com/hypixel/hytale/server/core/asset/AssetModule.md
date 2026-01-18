# AssetModule

## Overview
- Documentation for `AssetModule`.
- Declared as a class in `com.hypixel.hytale.server.core.asset`.

## Constructors
- `AssetModule(@Nonnull JavaPluginInit init)`
  - Creates a `AssetModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `getBaseAssetPack()`
  - Executes `getBaseAssetPack` behavior.
- `getAssetPacks()`
  - Executes `getAssetPacks` behavior.
- `getAssetMonitor()`
  - Executes `getAssetMonitor` behavior.
- `findAssetPackForPath(Path path)`
  - Executes `findAssetPackForPath` behavior.
- `isAssetPathImmutable(@Nonnull Path path)`
  - Executes `isAssetPathImmutable` behavior.
- `loadPackManifest(Path packPath)`
  - Executes `loadPackManifest` behavior.
- `loadPacksFromDirectory(Path modsPath)`
  - Executes `loadPacksFromDirectory` behavior.
- `loadAndRegisterPack(Path packPath)`
  - Executes `loadAndRegisterPack` behavior.
- `registerPack(@Nonnull String name, @Nonnull Path path, @Nonnull PluginManifest manifest)`
  - Executes `registerPack` behavior.
- `unregisterPack(@Nonnull String name)`
  - Executes `unregisterPack` behavior.
- `getAssetPack(@Nonnull String name)`
  - Executes `getAssetPack` behavior.
- `onRemoveStore(@Nonnull RemoveAssetStoreEvent event)`
  - Executes `onRemoveStore` behavior.
- `onNewStore(@Nonnull RegisterAssetStoreEvent event)`
  - Executes `onNewStore` behavior.
- `initPendingStores()`
  - Executes `initPendingStores` behavior.
- `initStore(@Nonnull AssetStore<?, ?, ?> assetStore)`
  - Executes `initStore` behavior.
- `validateWorldGen(@Nonnull LoadAssetEvent event)`
  - Executes `validateWorldGen` behavior.

## Notes
- No additional notes.
