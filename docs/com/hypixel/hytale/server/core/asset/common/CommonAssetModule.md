# CommonAssetModule

## Overview
- Documentation for `CommonAssetModule`.
- Declared as a class in `com.hypixel.hytale.server.core.asset.common`.

## Constructors
- `CommonAssetModule(@Nonnull JavaPluginInit init)`
  - Creates a `CommonAssetModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `removeCommonAssets(@Nonnull AssetPack assetPack)`
  - Executes `removeCommonAssets` behavior.
- `loadCommonAssets(@Nonnull AssetPack pack, long bootTime)`
  - Executes `loadCommonAssets` behavior.
- `addCommonAsset(String pack, @Nonnull T asset)`
  - Executes `addCommonAsset` behavior.
- `addCommonAsset(String pack, @Nonnull T asset, boolean log)`
  - Executes `addCommonAsset` behavior.
- `getRequiredAssets()`
  - Executes `getRequiredAssets` behavior.
- `readCommonAssetsIndexHashes(@Nonnull AssetPack pack)`
  - Executes `readCommonAssetsIndexHashes` behavior.
- `readCommonAssetsIndexCache(@Nonnull AssetPack pack)`
  - Executes `readCommonAssetsIndexCache` behavior.
- `walkFileTree(final @Nonnull AssetPack pack)`
  - Executes `walkFileTree` behavior.
- `visitFile(@Nonnull Path path, @Nonnull BasicFileAttributes attrs)`
  - Executes `visitFile` behavior.
- `unregisterAssetMonitor(@Nonnull AssetPack pack)`
  - Executes `unregisterAssetMonitor` behavior.
- `reloadAsset(@Nonnull List<CompletableFuture<Void>> addedOrUpdatedAssets, String pack, @Nonnull Path file, @Nonnull String name)`
  - Executes `reloadAsset` behavior.
- `onSendCommonAssets(@Nonnull SendCommonAssetsEvent event)`
  - Executes `onSendCommonAssets` behavior.
- `sendAssetsToPlayer(@Nonnull PacketHandler packetHandler, @Nullable Asset[] requested, boolean forceRebuild)`
  - Executes `sendAssetsToPlayer` behavior.
- `sendAssets(@Nonnull List<CommonAsset> toSend, boolean forceRebuild)`
  - Executes `sendAssets` behavior.
- `sendAssetsToPlayer(@Nonnull PacketHandler packetHandler, @Nonnull List<CommonAsset> toSend, boolean forceRebuild)`
  - Executes `sendAssetsToPlayer` behavior.
- `sendAsset(@Nonnull CommonAsset asset, boolean forceRebuild)`
  - Executes `sendAsset` behavior.
- `sendRemoveAssets(@Nonnull List<CommonAssetRegistry.PackAsset> assets, boolean forceRebuild)`
  - Executes `sendRemoveAssets` behavior.
- `getKey()`
  - Executes `getKey` behavior.
- `test(Path path, EventKind eventKind)`
  - Executes `test` behavior.
- `accept(Map<Path, EventKind> map)`
  - Executes `accept` behavior.

## Notes
- No additional notes.
