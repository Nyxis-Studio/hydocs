**Source Hash:** `fed8d16c1bbd81beb1035d32eee24c3d6c7d8719794d9af7ea2597baf25b43d3`

# WorldMapTracker

## Overview

## Constructor Descriptions
- `WorldMapTracker(@Nonnull Player player)`
  - Creates a `WorldMapTracker` instance.

## Method Descriptions
- `tick(float dt)`: Add description.
  - Executes `tick` behavior.
- `updateCurrentZoneAndBiome(@Nonnull Ref<EntityStore> ref, @Nullable ZoneDiscoveryInfo zoneDiscoveryInfo, @Nullable String biomeName, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `updateCurrentZoneAndBiome` behavior.
- `onZoneDiscovered(@Nonnull Ref<EntityStore> ref, @Nonnull ZoneDiscoveryInfo zoneDiscoveryInfo, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onZoneDiscovered` behavior.
- `updateWorldMap(@Nonnull World world, float dt, @Nonnull WorldMapSettings worldMapSettings, int chunkViewRadius, int playerChunkX, int playerChunkZ)`: Add description.
  - Executes `updateWorldMap` behavior.
- `updatePointsOfInterest(@Nonnull World world, int chunkViewRadius, int playerChunkX, int playerChunkZ)`: Add description.
  - Executes `updatePointsOfInterest` behavior.
- `trySendMarker(int chunkViewRadius, int playerChunkX, int playerChunkZ, @Nonnull MapMarker marker)`: Add description.
  - Executes `trySendMarker` behavior.
- `trySendMarker(int chunkViewRadius, int playerChunkX, int playerChunkZ, @Nonnull Vector3d markerPos, float markerYaw, @Nonnull String markerId, @Nonnull String markerDisplayName, @Nonnull T param, @Nonnull TriFunction<String, String, T, MapMarker> markerSupplier)`: Add description.
  - Executes `trySendMarker` behavior.
- `trySendMarker(int chunkViewRadius, int playerChunkX, int playerChunkZ, double markerX, double markerZ, float markerYaw, @Nonnull String markerId, @Nonnull String markerName, @Nonnull T param, @Nonnull TriFunction<String, String, T, MapMarker> markerSupplier)`: Add description.
  - Executes `trySendMarker` behavior.
- `unloadImages(int chunkViewRadius, int playerChunkX, int playerChunkZ)`: Add description.
  - Executes `unloadImages` behavior.
- `processPendingReloadChunks(@Nonnull World world)`: Add description.
  - Executes `processPendingReloadChunks` behavior.
- `loadImages(@Nonnull World world, int chunkViewRadius, int playerChunkX, int playerChunkZ, int maxGeneration)`: Add description.
  - Executes `loadImages` behavior.
- `loadWorldMap(@Nonnull World world, @Nonnull Box2D worldMapArea, int maxGeneration)`: Add description.
  - Executes `loadWorldMap` behavior.
- `writeUpdatePacket(@Nullable List<MapChunk> list)`: Add description.
  - Executes `writeUpdatePacket` behavior.
- `getSentMarkers()`: Add description.
  - Executes `getSentMarkers` behavior.
- `getPlayer()`: Add description.
  - Executes `getPlayer` behavior.
- `clear()`: Add description.
  - Executes `clear` behavior.
- `clearChunks(@Nonnull LongSet chunkIndices)`: Add description.
  - Executes `clearChunks` behavior.
- `sendSettings(@Nonnull World world)`: Add description.
  - Executes `sendSettings` behavior.
- `hasDiscoveredZone(@Nonnull String zoneName)`: Add description.
  - Executes `hasDiscoveredZone` behavior.
- `discoverZone(@Nonnull World world, @Nonnull String zoneName)`: Add description.
  - Executes `discoverZone` behavior.
- `undiscoverZone(@Nonnull World world, @Nonnull String zoneName)`: Add description.
  - Executes `undiscoverZone` behavior.
- `discoverZones(@Nonnull World world, @Nonnull Set<String> zoneNames)`: Add description.
  - Executes `discoverZones` behavior.
- `undiscoverZones(@Nonnull World world, @Nonnull Set<String> zoneNames)`: Add description.
  - Executes `undiscoverZones` behavior.
- `isAllowTeleportToCoordinates()`: Add description.
  - Executes `isAllowTeleportToCoordinates` behavior.
- `setAllowTeleportToCoordinates(@Nonnull World world, boolean allowTeleportToCoordinates)`: Add description.
  - Executes `setAllowTeleportToCoordinates` behavior.
- `isAllowTeleportToMarkers()`: Add description.
  - Executes `isAllowTeleportToMarkers` behavior.
- `setAllowTeleportToMarkers(@Nonnull World world, boolean allowTeleportToMarkers)`: Add description.
  - Executes `setAllowTeleportToMarkers` behavior.
- `getPlayerMapFilter()`: Add description.
  - Executes `getPlayerMapFilter` behavior.
- `setPlayerMapFilter(Predicate<PlayerRef> playerMapFilter)`: Add description.
  - Executes `setPlayerMapFilter` behavior.
- `setClientHasWorldMapVisible(boolean visible)`: Add description.
  - Executes `setClientHasWorldMapVisible` behavior.
- `shouldUpdatePlayerMarkers()`: Add description.
  - Executes `shouldUpdatePlayerMarkers` behavior.
- `resetPlayerMarkersUpdateTimer()`: Add description.
  - Executes `resetPlayerMarkersUpdateTimer` behavior.
- `getViewRadiusOverride()`: Add description.
  - Executes `getViewRadiusOverride` behavior.
- `getCurrentBiomeName()`: Add description.
  - Executes `getCurrentBiomeName` behavior.
- `getCurrentZone()`: Add description.
  - Executes `getCurrentZone` behavior.
- `setViewRadiusOverride(@Nullable Integer viewRadiusOverride)`: Add description.
  - Executes `setViewRadiusOverride` behavior.
- `getEffectiveViewRadius(@Nonnull World world)`: Add description.
  - Executes `getEffectiveViewRadius` behavior.
- `shouldBeVisible(int chunkViewRadius, long chunkCoordinates)`: Add description.
  - Executes `shouldBeVisible` behavior.
- `copyFrom(@Nonnull WorldMapTracker worldMapTracker)`: Add description.
  - Executes `copyFrom` behavior.
- `shouldBeVisible(int chunkViewRadius, int chunkX, int chunkZ, int x, int z)`: Add description.
  - Executes `shouldBeVisible` behavior.
- `ZoneDiscoveryInfo(@Nonnull String zoneName, @Nonnull String regionName, boolean display, @Nullable String discoverySoundEventId, @Nullable String icon, boolean major, float duration, float fadeInDuration, float fadeOutDuration)`: Add description.
  - Executes `ZoneDiscoveryInfo` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.

## Notes
- No additional notes.
