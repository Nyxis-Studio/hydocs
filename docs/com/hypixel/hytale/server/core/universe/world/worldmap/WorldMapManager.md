# WorldMapManager

## Overview
- Documentation for `WorldMapManager`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.worldmap`.

## Constructors
- `WorldMapManager(@Nonnull World world)`
  - Creates a `WorldMapManager` instance.

## Methods
- `getGenerator()`
  - Executes `getGenerator` behavior.
- `setGenerator(@Nullable IWorldMap generator)`
  - Executes `setGenerator` behavior.
- `isIdle()`
  - Executes `isIdle` behavior.
- `tick(float dt)`
  - Executes `tick` behavior.
- `onShutdown()`
  - Executes `onShutdown` behavior.
- `unloadImages()`
  - Executes `unloadImages` behavior.
- `isWorldMapEnabled()`
  - Executes `isWorldMapEnabled` behavior.
- `isWorldMapImageVisibleToAnyPlayer(@Nonnull List<Player> players, long imageIndex, @Nonnull WorldMapSettings settings)`
  - Executes `isWorldMapImageVisibleToAnyPlayer` behavior.
- `getWorld()`
  - Executes `getWorld` behavior.
- `getWorldMapSettings()`
  - Executes `getWorldMapSettings` behavior.
- `getMarkerProviders()`
  - Executes `getMarkerProviders` behavior.
- `addMarkerProvider(@Nonnull String key, @Nonnull MarkerProvider provider)`
  - Executes `addMarkerProvider` behavior.
- `getPointsOfInterest()`
  - Executes `getPointsOfInterest` behavior.
- `getImageIfInMemory(int x, int z)`
  - Executes `getImageIfInMemory` behavior.
- `getImageIfInMemory(long index)`
  - Executes `getImageIfInMemory` behavior.
- `getImageAsync(int x, int z)`
  - Executes `getImageAsync` behavior.
- `getImageAsync(long index)`
  - Executes `getImageAsync` behavior.
- `generate()`
  - Executes `generate` behavior.
- `sendSettings()`
  - Executes `sendSettings` behavior.
- `shouldTick()`
  - Executes `shouldTick` behavior.
- `updateTickingState(boolean before)`
  - Executes `updateTickingState` behavior.
- `clearImages()`
  - Executes `clearImages` behavior.
- `clearImagesInChunks(@Nonnull LongSet chunkIndices)`
  - Executes `clearImagesInChunks` behavior.
- `createPlayerMarker(@Nonnull Ref<EntityStore> playerRef, @Nonnull MapMarker marker, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `createPlayerMarker` behavior.
- `update(World var1, GameplayConfig var2, WorldMapTracker var3, int var4, int var5, int var6)`
  - Executes `update` behavior.
- `getPlayer()`
  - Executes `getPlayer` behavior.
- `getMarkerId()`
  - Executes `getMarkerId` behavior.
- `remove()`
  - Executes `remove` behavior.
- `removeMarkerFromOnlinePlayer(@Nonnull Player player)`
  - Executes `removeMarkerFromOnlinePlayer` behavior.
- `removeMarkerFromOfflinePlayer()`
  - Executes `removeMarkerFromOfflinePlayer` behavior.
- `removeMarkerFromData(@Nonnull PlayerConfigData data, @Nonnull String worldName, @Nonnull String markerId)`
  - Executes `removeMarkerFromData` behavior.

## Notes
- No additional notes.
