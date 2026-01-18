# WorldSpawningSystem

## Overview
- Documentation for `WorldSpawningSystem`.
- Declared as a class in `com.hypixel.hytale.server.spawning.world.system`.

## Constructors
- `WorldSpawningSystem(@Nonnull ResourceType<EntityStore, WorldSpawnData> worldSpawnDataResourceType, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType, @Nonnull ComponentType<ChunkStore, SpawnJobData> spawnJobDataComponentType)`
  - Creates a `WorldSpawningSystem` instance.

## Methods
- `tick(float dt, int systemIndex, @Nonnull Store<ChunkStore> store)`
  - Executes `tick` behavior.
- `createRandomSpawnJob(@Nonnull WorldSpawnData worldData, @Nonnull Store<ChunkStore> chunkStore, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `createRandomSpawnJob` behavior.
- `getAndConsumeNextEnvironmentIndex(@Nonnull WorldSpawnData worldSpawnData, @Nonnull int[] environmentKeySet)`
  - Executes `getAndConsumeNextEnvironmentIndex` behavior.
- `pickRandomChunk(@Nonnull WorldEnvironmentSpawnData spawnData, @Nonnull WorldNPCSpawnStat stat, @Nonnull WorldSpawnData worldSpawnData, @Nonnull Store<ChunkStore> store)`
  - Executes `pickRandomChunk` behavior.
- `getAndUpdateSpawnCooldown(@Nonnull ChunkSpawnData chunkSpawnData)`
  - Executes `getAndUpdateSpawnCooldown` behavior.

## Notes
- No additional notes.
