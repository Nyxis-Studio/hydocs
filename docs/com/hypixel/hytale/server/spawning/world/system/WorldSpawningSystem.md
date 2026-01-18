**Source Hash:** `61dacbc1245e9235699078b45beb0ffc4d58af1857965cd26fe32c9ded2ea9de`

# WorldSpawningSystem

## Overview

## Constructor Descriptions
- `WorldSpawningSystem(@Nonnull ResourceType<EntityStore, WorldSpawnData> worldSpawnDataResourceType, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType, @Nonnull ComponentType<ChunkStore, SpawnJobData> spawnJobDataComponentType)`
  - Creates a `WorldSpawningSystem` instance.

## Method Descriptions
- `tick(float dt, int systemIndex, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `tick` behavior.
- `createRandomSpawnJob(@Nonnull WorldSpawnData worldData, @Nonnull Store<ChunkStore> chunkStore, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `createRandomSpawnJob` behavior.
- `getAndConsumeNextEnvironmentIndex(@Nonnull WorldSpawnData worldSpawnData, @Nonnull int[] environmentKeySet)`: Add description.
  - Executes `getAndConsumeNextEnvironmentIndex` behavior.
- `pickRandomChunk(@Nonnull WorldEnvironmentSpawnData spawnData, @Nonnull WorldNPCSpawnStat stat, @Nonnull WorldSpawnData worldSpawnData, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `pickRandomChunk` behavior.
- `getAndUpdateSpawnCooldown(@Nonnull ChunkSpawnData chunkSpawnData)`: Add description.
  - Executes `getAndUpdateSpawnCooldown` behavior.

## Notes
- No additional notes.
