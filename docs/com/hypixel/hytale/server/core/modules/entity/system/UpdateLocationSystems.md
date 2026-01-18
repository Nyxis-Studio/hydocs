# UpdateLocationSystems

## Overview
- Documentation for `UpdateLocationSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.system`.

## Constructors
- None.

## Methods
- `updateLocation(@Nonnull Ref<EntityStore> ref, @Nonnull TransformComponent transformComponent, @Nullable World world, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `updateLocation` behavior.
- `updateChunkAsync(@Nonnull Ref<EntityStore> ref, @Nullable Ref<ChunkStore> newChunkRef, @Nullable WorldChunk newWorldChunk, @Nonnull Store<ChunkStore> chunkComponentStore)`
  - Executes `updateChunkAsync` behavior.
- `updateChunk(@Nonnull Ref<EntityStore> ref, @Nonnull TransformComponent transformComponent, @Nullable Ref<ChunkStore> oldChunkRef, @Nullable Ref<ChunkStore> newChunkRef, @Nullable WorldChunk newWorldChunkComponent, @Nonnull ComponentAccessor<ChunkStore> chunkComponentStore, @Nonnull ComponentAccessor<EntityStore> entityComponentAccessor)`
  - Executes `updateChunk` behavior.
- `handleInvalidChunk(@Nonnull Ref<EntityStore> ref, @Nonnull TransformComponent transformComponent, boolean isPlayer, @Nonnull ComponentAccessor<EntityStore> entityComponentAccessor)`
  - Executes `handleInvalidChunk` behavior.
- `updateEntityInChunk(@Nonnull Ref<EntityStore> ref, @Nullable Ref<ChunkStore> oldChunkRef, @Nonnull Ref<ChunkStore> newChunkRef, @Nonnull WorldChunk newWorldChunk, @Nonnull ComponentAccessor<ChunkStore> chunkComponentStore, @Nonnull ComponentAccessor<EntityStore> entityComponentAccessor)`
  - Executes `updateEntityInChunk` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
