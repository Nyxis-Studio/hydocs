**Source Hash:** `53981661bedd1ec68d1437d7fe13c939c3dc28c94edaa232eac819b46945bbe0`

# UpdateLocationSystems

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `updateLocation(@Nonnull Ref<EntityStore> ref, @Nonnull TransformComponent transformComponent, @Nullable World world, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `updateLocation` behavior.
- `updateChunkAsync(@Nonnull Ref<EntityStore> ref, @Nullable Ref<ChunkStore> newChunkRef, @Nullable WorldChunk newWorldChunk, @Nonnull Store<ChunkStore> chunkComponentStore)`: Add description.
  - Executes `updateChunkAsync` behavior.
- `updateChunk(@Nonnull Ref<EntityStore> ref, @Nonnull TransformComponent transformComponent, @Nullable Ref<ChunkStore> oldChunkRef, @Nullable Ref<ChunkStore> newChunkRef, @Nullable WorldChunk newWorldChunkComponent, @Nonnull ComponentAccessor<ChunkStore> chunkComponentStore, @Nonnull ComponentAccessor<EntityStore> entityComponentAccessor)`: Add description.
  - Executes `updateChunk` behavior.
- `handleInvalidChunk(@Nonnull Ref<EntityStore> ref, @Nonnull TransformComponent transformComponent, boolean isPlayer, @Nonnull ComponentAccessor<EntityStore> entityComponentAccessor)`: Add description.
  - Executes `handleInvalidChunk` behavior.
- `updateEntityInChunk(@Nonnull Ref<EntityStore> ref, @Nullable Ref<ChunkStore> oldChunkRef, @Nonnull Ref<ChunkStore> newChunkRef, @Nonnull WorldChunk newWorldChunk, @Nonnull ComponentAccessor<ChunkStore> chunkComponentStore, @Nonnull ComponentAccessor<EntityStore> entityComponentAccessor)`: Add description.
  - Executes `updateEntityInChunk` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
