**Source Hash:** `367e083db3c919c2ca9546ea258abbf70a3cd861ae9e2dd800fa847f7ee8917f`

# WorldSpawnJobSystems

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `run(@Nonnull SpawnJobData spawnJobData, @Nonnull WorldChunk chunk, @Nonnull ChunkEnvironmentSpawnData chunkEnvironmentSpawnData, @Nonnull WorldSpawnData worldSpawnData, @Nonnull SpawnSuppressionController spawnSuppressionController)`: Add description.
  - Executes `run` behavior.
- `getSpawnable(int roleIndex)`: Add description.
  - Executes `getSpawnable` behavior.
- `trySpawn(@Nonnull ISpawnableWithModel spawnable, IntSet spawnBlockSet, int spawnFluidTag, @Nonnull SpawnJobData spawnJobData, @Nonnull WorldChunk worldChunk, @Nonnull ChunkEnvironmentSpawnData environmentSpawnData, @Nonnull WorldSpawnData worldSpawnData)`: Add description.
  - Executes `trySpawn` behavior.
- `spawn(@Nonnull SpawnJobData spawnJobData, @Nonnull WorldChunk worldChunk, @Nonnull WorldSpawnData worldSpawnData)`: Add description.
  - Executes `spawn` behavior.
- `preAddToWorld(@Nonnull NPCEntity npc, @Nonnull Holder<EntityStore> holder, int roleIndex, @Nonnull SpawnJobData spawnJobData)`: Add description.
  - Executes `preAddToWorld` behavior.
- `canSpawnOnBlock(@Nullable IntSet spawnBlockSet, int spawnFluidTag, @Nonnull SpawningContext spawningContext)`: Add description.
  - Executes `canSpawnOnBlock` behavior.
- `rejectSpan(@Nonnull Object2IntMap<SpawnRejection> rejectionMap, SpawnRejection rejection)`: Add description.
  - Executes `rejectSpan` behavior.
- `endProbing(Result result, @Nonnull SpawnJobData spawnJobData, @Nonnull WorldChunk worldChunk, @Nonnull WorldSpawnData worldSpawnData)`: Add description.
  - Executes `endProbing` behavior.
- `updateSpawnStats(@Nonnull WorldSpawnData worldSpawnData, @Nonnull SpawnJobData spawnJobData, Result result)`: Add description.
  - Executes `updateSpawnStats` behavior.
- `getSpawnableName(int roleIndex)`: Add description.
  - Executes `getSpawnableName` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`: Add description.
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `componentType()`: Add description.
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<ChunkStore> ref, NonTicking<ChunkStore> oldComponent, @Nonnull NonTicking<ChunkStore> newComponent, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onComponentRemoved` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> entityHolder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
