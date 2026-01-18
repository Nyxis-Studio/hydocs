# PlayerWorldData

## Overview
- Documentation for `PlayerWorldData`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities.player.data`.

## Constructors
- `PlayerWorldData()`
  - Creates a `PlayerWorldData` instance.
- `PlayerWorldData(@Nonnull PlayerConfigData playerConfigData)`
  - Creates a `PlayerWorldData` instance.

## Methods
- `setPlayerConfigData(@Nonnull PlayerConfigData playerConfigData)`
  - Executes `setPlayerConfigData` behavior.
- `getLastPosition()`
  - Executes `getLastPosition` behavior.
- `setLastPosition(@Nonnull Transform lastPosition)`
  - Executes `setLastPosition` behavior.
- `getLastMovementStates()`
  - Executes `getLastMovementStates` behavior.
- `setLastMovementStates(@Nonnull MovementStates lastMovementStates, boolean save)`
  - Executes `setLastMovementStates` behavior.
- `setLastMovementStates_internal(@Nonnull MovementStates lastMovementStates)`
  - Executes `setLastMovementStates_internal` behavior.
- `getWorldMapMarkers()`
  - Executes `getWorldMapMarkers` behavior.
- `setWorldMapMarkers(MapMarker[] worldMapMarkers)`
  - Executes `setWorldMapMarkers` behavior.
- `isFirstSpawn()`
  - Executes `isFirstSpawn` behavior.
- `setFirstSpawn(boolean firstSpawn)`
  - Executes `setFirstSpawn` behavior.
- `getRespawnPoints()`
  - Executes `getRespawnPoints` behavior.
- `setRespawnPoints(@Nonnull PlayerRespawnPointData[] respawnPoints)`
  - Executes `setRespawnPoints` behavior.
- `getDeathPositions()`
  - Executes `getDeathPositions` behavior.
- `addLastDeath(@Nonnull String markerId, @Nonnull Transform transform, int deathDay)`
  - Executes `addLastDeath` behavior.
- `removeLastDeath(@Nonnull String markerId)`
  - Executes `removeLastDeath` behavior.

## Notes
- No additional notes.
