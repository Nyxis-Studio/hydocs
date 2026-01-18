# ChunkSpawningSystems

## Overview
- Documentation for `ChunkSpawningSystems`.
- Declared as a class in `com.hypixel.hytale.server.spawning.world.system`.

## Constructors
- None.

## Methods
- `processStoppedChunk(@Nonnull Ref<ChunkStore> ref, @Nonnull Store<ChunkStore> store, @Nonnull WorldSpawnData worldSpawnData, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `processStoppedChunk` behavior.
- `processStartedChunk(@Nonnull Ref<ChunkStore> ref, @Nonnull Store<ChunkStore> store, @Nonnull WorldChunk worldChunk, @Nonnull WorldSpawnData worldSpawnData, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `processStartedChunk` behavior.
- `preprocessChunk(@Nonnull ChunkSpawnData chunkSpawnData, @Nonnull WorldChunk worldChunk)`
  - Executes `preprocessChunk` behavior.
- `preprocessColumn(@Nonnull ChunkSpawnData chunkSpawnData, @Nonnull WorldChunk worldChunk, int x, int z)`
  - Executes `preprocessColumn` behavior.
- `updateChunkCount(int newChunks, @Nonnull WorldSpawnData worldSpawnData)`
  - Executes `updateChunkCount` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<ChunkStore> ref, NonTicking<ChunkStore> oldComponent, @Nonnull NonTicking<ChunkStore> newComponent, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<ChunkStore> ref, @Nonnull NonTicking<ChunkStore> component, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
