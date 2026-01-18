# SpawningContext

## Overview
- Documentation for `SpawningContext`.
- Declared as a class in `com.hypixel.hytale.server.spawning`.

## Constructors
- `SpawningContext()`
  - Creates a `SpawningContext` instance.

## Methods
- `setSpawnable(@Nonnull ISpawnableWithModel spawnable)`
  - Executes `setSpawnable` behavior.
- `setSpawnable(@Nonnull ISpawnableWithModel spawnable, boolean maxScale)`
  - Executes `setSpawnable` behavior.
- `setModel(@Nullable String modelName, boolean maxScale)`
  - Executes `setModel` behavior.
- `clearModel()`
  - Executes `clearModel` behavior.
- `newModel()`
  - Executes `newModel` behavior.
- `getModel()`
  - Executes `getModel` behavior.
- `setChunk(@Nonnull WorldChunk worldChunk, int environmentIndex)`
  - Executes `setChunk` behavior.
- `setColumn(int x, int z, int yHint, @Nonnull int[] yRange)`
  - Executes `setColumn` behavior.
- `setColumn(int x, int z, int yHint, @Nonnull int[] yRange, @Nonnull SuppressionSpanHelper suppressionHelper)`
  - Executes `setColumn` behavior.
- `setColumn(int x, int z, @Nonnull SuppressionSpanHelper suppressionHelper)`
  - Executes `setColumn` behavior.
- `getModifierScope()`
  - Executes `getModifierScope` behavior.
- `set(@Nonnull World world, double x, double y, double z)`
  - Executes `set` behavior.
- `deleteCurrentSpawnSpan()`
  - Executes `deleteCurrentSpawnSpan` behavior.
- `selectRandomSpawnSpan()`
  - Executes `selectRandomSpawnSpan` behavior.
- `selectSpawnSpan(int index)`
  - Executes `selectSpawnSpan` behavior.
- `splitRangeToSpawnSpans(int min, int max)`
  - Executes `splitRangeToSpawnSpans` behavior.
- `addSpawnSpan(int top, int span, int groundLevel, int waterLevel)`
  - Executes `addSpawnSpan` behavior.
- `isSpawnSpanBlock(int x, int y, int z)`
  - Executes `isSpawnSpanBlock` behavior.
- `commonInit()`
  - Executes `commonInit` behavior.
- `canSpawn(boolean testOverlapBlocks, boolean testOverlapEntities)`
  - Executes `canSpawn` behavior.
- `canSpawn()`
  - Executes `canSpawn` behavior.
- `intersectsEntity()`
  - Executes `intersectsEntity` behavior.
- `intersectsBlock()`
  - Executes `intersectsBlock` behavior.
- `isWaterBlock(int fluidId)`
  - Executes `isWaterBlock` behavior.
- `getWaterLevel()`
  - Executes `getWaterLevel` behavior.
- `getAirHeight()`
  - Executes `getAirHeight` behavior.
- `isInsideSpan(double y)`
  - Executes `isInsideSpan` behavior.
- `isInWater(float minDepth)`
  - Executes `isInWater` behavior.
- `isOnSolidGround()`
  - Executes `isOnSolidGround` behavior.
- `isInAir(double height)`
  - Executes `isInAir` behavior.
- `validatePosition(int invalidMaterials)`
  - Executes `validatePosition` behavior.
- `canBreathe(boolean breathesInAir, boolean breathesInWater)`
  - Executes `canBreathe` behavior.
- `release()`
  - Executes `release` behavior.
- `releaseFull()`
  - Executes `releaseFull` behavior.
- `getExecutionContext()`
  - Executes `getExecutionContext` behavior.
- `newPosition()`
  - Executes `newPosition` behavior.
- `newRotation()`
  - Executes `newRotation` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
