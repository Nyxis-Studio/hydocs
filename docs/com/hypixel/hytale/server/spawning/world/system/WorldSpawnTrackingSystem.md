**Source Hash:** `8a156fdd926cacb06dff396bee64af3632000c07e2807da32faca15597ef7190`

# WorldSpawnTrackingSystem

## Overview

## Constructor Descriptions
- `WorldSpawnTrackingSystem(@Nonnull ResourceType<EntityStore, WorldSpawnData> worldSpawnDataResourceType, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType)`
  - Creates a `WorldSpawnTrackingSystem` instance.

## Method Descriptions
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.
- `trackNPC(int environmentIndex, int roleIndex, @Nonnull WorldSpawnData worldSpawnData, @Nonnull World world, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `trackNPC` behavior.
- `untrackNPC(int environmentIndex, int roleIndex, @Nonnull WorldSpawnData worldSpawnData)`: Add description.
  - Executes `untrackNPC` behavior.
- `trackNewNPC(@Nonnull Ref<ChunkStore> ref, int environmentIndex, double count, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `trackNewNPC` behavior.
- `untrackRemovedNPC(@Nonnull Ref<ChunkStore> ref, int environmentIndex, double count, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `untrackRemovedNPC` behavior.
- `getEnvironmentName(int id)`: Add description.
  - Executes `getEnvironmentName` behavior.

## Notes
- No additional notes.
