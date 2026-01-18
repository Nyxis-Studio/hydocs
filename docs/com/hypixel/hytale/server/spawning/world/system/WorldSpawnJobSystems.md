# WorldSpawnJobSystems

## Overview
- Documentation for `WorldSpawnJobSystems`.
- Declared as a class in `com.hypixel.hytale.server.spawning.world.system`.

## Constructors
- None.

## Methods
- `run(@Nonnull SpawnJobData spawnJobData, @Nonnull WorldChunk chunk, @Nonnull ChunkEnvironmentSpawnData chunkEnvironmentSpawnData, @Nonnull WorldSpawnData worldSpawnData, @Nonnull SpawnSuppressionController spawnSuppressionController)`
  - Executes `run` behavior.
- `getSpawnable(int roleIndex)`
  - Executes `getSpawnable` behavior.
- `trySpawn(@Nonnull ISpawnableWithModel spawnable, IntSet spawnBlockSet, int spawnFluidTag, @Nonnull SpawnJobData spawnJobData, @Nonnull WorldChunk worldChunk, @Nonnull ChunkEnvironmentSpawnData environmentSpawnData, @Nonnull WorldSpawnData worldSpawnData)`
  - Executes `trySpawn` behavior.
- `spawn(@Nonnull SpawnJobData spawnJobData, @Nonnull WorldChunk worldChunk, @Nonnull WorldSpawnData worldSpawnData)`
  - Executes `spawn` behavior.
- `preAddToWorld(@Nonnull NPCEntity npc, @Nonnull Holder<EntityStore> holder, int roleIndex, @Nonnull SpawnJobData spawnJobData)`
  - Executes `preAddToWorld` behavior.
- `canSpawnOnBlock(@Nullable IntSet spawnBlockSet, int spawnFluidTag, @Nonnull SpawningContext spawningContext)`
  - Executes `canSpawnOnBlock` behavior.
- `rejectSpan(@Nonnull Object2IntMap<SpawnRejection> rejectionMap, SpawnRejection rejection)`
  - Executes `rejectSpan` behavior.
- `endProbing(Result result, @Nonnull SpawnJobData spawnJobData, @Nonnull WorldChunk worldChunk, @Nonnull WorldSpawnData worldSpawnData)`
  - Executes `endProbing` behavior.
- `updateSpawnStats(@Nonnull WorldSpawnData worldSpawnData, @Nonnull SpawnJobData spawnJobData, Result result)`
  - Executes `updateSpawnStats` behavior.
- `getSpawnableName(int roleIndex)`
  - Executes `getSpawnableName` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `tick` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<ChunkStore> ref, NonTicking<ChunkStore> oldComponent, @Nonnull NonTicking<ChunkStore> newComponent, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> entityHolder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
