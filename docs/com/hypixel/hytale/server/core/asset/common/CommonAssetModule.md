**Source Hash:** `dc7177e16b6111ee573b009f4d092003a18fe1a3f337759831fb7b03a5c645f0`

# CommonAssetModule

## Overview

## Constructor Descriptions
- `CommonAssetModule(@Nonnull JavaPluginInit init)`
  - Creates a `CommonAssetModule` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `removeCommonAssets(@Nonnull AssetPack assetPack)`: Add description.
  - Executes `removeCommonAssets` behavior.
- `loadCommonAssets(@Nonnull AssetPack pack, long bootTime)`: Add description.
  - Executes `loadCommonAssets` behavior.
- `addCommonAsset(String pack, @Nonnull T asset)`: Add description.
  - Executes `addCommonAsset` behavior.
- `addCommonAsset(String pack, @Nonnull T asset, boolean log)`: Add description.
  - Executes `addCommonAsset` behavior.
- `getRequiredAssets()`: Add description.
  - Executes `getRequiredAssets` behavior.
- `readCommonAssetsIndexHashes(@Nonnull AssetPack pack)`: Add description.
  - Executes `readCommonAssetsIndexHashes` behavior.
- `readCommonAssetsIndexCache(@Nonnull AssetPack pack)`: Add description.
  - Executes `readCommonAssetsIndexCache` behavior.
- `walkFileTree(final @Nonnull AssetPack pack)`: Add description.
  - Executes `walkFileTree` behavior.
- `visitFile(@Nonnull Path path, @Nonnull BasicFileAttributes attrs)`: Add description.
  - Executes `visitFile` behavior.
- `unregisterAssetMonitor(@Nonnull AssetPack pack)`: Add description.
  - Executes `unregisterAssetMonitor` behavior.
- `reloadAsset(@Nonnull List<CompletableFuture<Void>> addedOrUpdatedAssets, String pack, @Nonnull Path file, @Nonnull String name)`: Add description.
  - Executes `reloadAsset` behavior.
- `onSendCommonAssets(@Nonnull SendCommonAssetsEvent event)`: Add description.
  - Executes `onSendCommonAssets` behavior.
- `sendAssetsToPlayer(@Nonnull PacketHandler packetHandler, @Nullable Asset[] requested, boolean forceRebuild)`: Add description.
  - Executes `sendAssetsToPlayer` behavior.
- `sendAssets(@Nonnull List<CommonAsset> toSend, boolean forceRebuild)`: Add description.
  - Executes `sendAssets` behavior.
- `sendAssetsToPlayer(@Nonnull PacketHandler packetHandler, @Nonnull List<CommonAsset> toSend, boolean forceRebuild)`: Add description.
  - Executes `sendAssetsToPlayer` behavior.
- `sendAsset(@Nonnull CommonAsset asset, boolean forceRebuild)`: Add description.
  - Executes `sendAsset` behavior.
- `sendRemoveAssets(@Nonnull List<CommonAssetRegistry.PackAsset> assets, boolean forceRebuild)`: Add description.
  - Executes `sendRemoveAssets` behavior.
- `getKey()`: Add description.
  - Executes `getKey` behavior.
- `test(Path path, EventKind eventKind)`: Add description.
  - Executes `test` behavior.
- `accept(Map<Path, EventKind> map)`: Add description.
  - Executes `accept` behavior.

## Notes
- No additional notes.
