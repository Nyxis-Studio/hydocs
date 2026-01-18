# FloodFillPositionSelector

## Overview
- Documentation for `FloodFillPositionSelector`.
- Declared as a class in `com.hypixel.hytale.server.spawning.util`.

## Constructors
- `FloodFillPositionSelector(World world, @Nonnull BeaconSpawnWrapper spawnWrapper)`
  - Creates a `FloodFillPositionSelector` instance.
- `FloodFillPositionSelector(this.world, this.spawnWrapper)`
  - Creates a `FloodFillPositionSelector` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `setCalculatePositionsAfter(double calculatePositionsAfter)`
  - Executes `setCalculatePositionsAfter` behavior.
- `tickCalculatePositionsAfter(float dt)`
  - Executes `tickCalculatePositionsAfter` behavior.
- `hasPositionsForRole(int roleIndex)`
  - Executes `hasPositionsForRole` behavior.
- `prepareSpawnContext(@Nonnull Vector3d playerPosition, int spawnsThisRound, int roleIndex, @Nonnull SpawningContext spawningContext, @Nonnull BeaconSpawnWrapper spawnWrapper)`
  - Executes `prepareSpawnContext` behavior.
- `shouldRebuildCache()`
  - Executes `shouldRebuildCache` behavior.
- `forceRebuildCache()`
  - Executes `forceRebuildCache` behavior.
- `init()`
  - Executes `init` behavior.
- `buildPositionCache(@Nonnull Vector3d origin, @Nonnull FloodFillEntryPoolSimple pool)`
  - Executes `buildPositionCache` behavior.
- `floodFill(int worldX, int worldY, int worldZ, int setX, int setZ, @Nonnull FloodFillEntryPoolSimple pool)`
  - Executes `floodFill` behavior.
- `findPositions(int originX, int originZ)`
  - Executes `findPositions` behavior.
- `buildLowerResolutionMap(@Nonnull BitSet targetMap, int mapSize, @Nonnull BitSet parentMap, int parentMapSize)`
  - Executes `buildLowerResolutionMap` behavior.
- `pickOpenSegment(int lowResolutionIndex, int lowResolutionMapSize, @Nonnull BitSet higherResolutionMap, int highResolutionMapSize)`
  - Executes `pickOpenSegment` behavior.
- `shiftIndexAwayFromWall(int index)`
  - Executes `shiftIndexAwayFromWall` behavior.
- `canSpawn(int x, int y, int z, int roleIndex, @Nullable ChunkSuppressionEntry suppressionEntry)`
  - Executes `canSpawn` behavior.
- `debugDumpBaseFloodFill()`
  - Executes `debugDumpBaseFloodFill` behavior.
- `debugDumpLowResolutionMap(@Nonnull BitSet map, int size)`
  - Executes `debugDumpLowResolutionMap` behavior.
- `getPositionIndex(int x, int z, int size)`
  - Executes `getPositionIndex` behavior.
- `xFromIndex(int index, int size)`
  - Executes `xFromIndex` behavior.
- `zFromIndex(int index, int size)`
  - Executes `zFromIndex` behavior.
- `clone()`
  - Executes `clone` behavior.
- `getWeight()`
  - Executes `getWeight` behavior.
- `getBuffer(int size)`
  - Executes `getBuffer` behavior.

## Notes
- No additional notes.
