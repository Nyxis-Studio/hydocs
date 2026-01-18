# WorldSpawnTrackingSystem

## Overview
- Documentation for `WorldSpawnTrackingSystem`.
- Declared as a class in `com.hypixel.hytale.server.spawning.world.system`.

## Constructors
- `WorldSpawnTrackingSystem(@Nonnull ResourceType<EntityStore, WorldSpawnData> worldSpawnDataResourceType, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType)`
  - Creates a `WorldSpawnTrackingSystem` instance.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `trackNPC(int environmentIndex, int roleIndex, @Nonnull WorldSpawnData worldSpawnData, @Nonnull World world, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `trackNPC` behavior.
- `untrackNPC(int environmentIndex, int roleIndex, @Nonnull WorldSpawnData worldSpawnData)`
  - Executes `untrackNPC` behavior.
- `trackNewNPC(@Nonnull Ref<ChunkStore> ref, int environmentIndex, double count, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType, @Nonnull Store<ChunkStore> store)`
  - Executes `trackNewNPC` behavior.
- `untrackRemovedNPC(@Nonnull Ref<ChunkStore> ref, int environmentIndex, double count, @Nonnull ComponentType<ChunkStore, ChunkSpawnData> chunkSpawnDataComponentType, @Nonnull ComponentType<ChunkStore, ChunkSpawnedNPCData> chunkSpawnedNPCDataComponentType, @Nonnull Store<ChunkStore> store)`
  - Executes `untrackRemovedNPC` behavior.
- `getEnvironmentName(int id)`
  - Executes `getEnvironmentName` behavior.

## Notes
- No additional notes.
