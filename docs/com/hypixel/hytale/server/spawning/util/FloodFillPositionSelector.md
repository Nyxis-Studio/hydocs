**Source Hash:** `51f49526675715c95492f6a66ab318ba7cccb02b916269ff57334a44b5ee358b`

# FloodFillPositionSelector

## Overview

## Constructor Descriptions
- `FloodFillPositionSelector(World world, @Nonnull BeaconSpawnWrapper spawnWrapper)`
  - Creates a `FloodFillPositionSelector` instance.
- `FloodFillPositionSelector(this.world, this.spawnWrapper)`
  - Creates a `FloodFillPositionSelector` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `setCalculatePositionsAfter(double calculatePositionsAfter)`: Add description.
  - Executes `setCalculatePositionsAfter` behavior.
- `tickCalculatePositionsAfter(float dt)`: Add description.
  - Executes `tickCalculatePositionsAfter` behavior.
- `hasPositionsForRole(int roleIndex)`: Add description.
  - Executes `hasPositionsForRole` behavior.
- `prepareSpawnContext(@Nonnull Vector3d playerPosition, int spawnsThisRound, int roleIndex, @Nonnull SpawningContext spawningContext, @Nonnull BeaconSpawnWrapper spawnWrapper)`: Add description.
  - Executes `prepareSpawnContext` behavior.
- `shouldRebuildCache()`: Add description.
  - Executes `shouldRebuildCache` behavior.
- `forceRebuildCache()`: Add description.
  - Executes `forceRebuildCache` behavior.
- `init()`: Add description.
  - Executes `init` behavior.
- `buildPositionCache(@Nonnull Vector3d origin, @Nonnull FloodFillEntryPoolSimple pool)`: Add description.
  - Executes `buildPositionCache` behavior.
- `floodFill(int worldX, int worldY, int worldZ, int setX, int setZ, @Nonnull FloodFillEntryPoolSimple pool)`: Add description.
  - Executes `floodFill` behavior.
- `findPositions(int originX, int originZ)`: Add description.
  - Executes `findPositions` behavior.
- `buildLowerResolutionMap(@Nonnull BitSet targetMap, int mapSize, @Nonnull BitSet parentMap, int parentMapSize)`: Add description.
  - Executes `buildLowerResolutionMap` behavior.
- `pickOpenSegment(int lowResolutionIndex, int lowResolutionMapSize, @Nonnull BitSet higherResolutionMap, int highResolutionMapSize)`: Add description.
  - Executes `pickOpenSegment` behavior.
- `shiftIndexAwayFromWall(int index)`: Add description.
  - Executes `shiftIndexAwayFromWall` behavior.
- `canSpawn(int x, int y, int z, int roleIndex, @Nullable ChunkSuppressionEntry suppressionEntry)`: Add description.
  - Executes `canSpawn` behavior.
- `debugDumpBaseFloodFill()`: Add description.
  - Executes `debugDumpBaseFloodFill` behavior.
- `debugDumpLowResolutionMap(@Nonnull BitSet map, int size)`: Add description.
  - Executes `debugDumpLowResolutionMap` behavior.
- `getPositionIndex(int x, int z, int size)`: Add description.
  - Executes `getPositionIndex` behavior.
- `xFromIndex(int index, int size)`: Add description.
  - Executes `xFromIndex` behavior.
- `zFromIndex(int index, int size)`: Add description.
  - Executes `zFromIndex` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `getWeight()`: Add description.
  - Executes `getWeight` behavior.
- `getBuffer(int size)`: Add description.
  - Executes `getBuffer` behavior.

## Notes
- No additional notes.
