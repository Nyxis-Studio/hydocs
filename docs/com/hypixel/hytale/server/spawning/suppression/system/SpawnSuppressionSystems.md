**Source Hash:** `141a01b913822a3d57e1c89c327ef777b95acd10802b636b3e21b05bccb980aa`

# SpawnSuppressionSystems

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `suppressSpawns(@Nonnull ResourceType<ChunkStore, ChunkSuppressionQueue> chunkSuppressionQueueResourceType, @Nonnull ComponentType<EntityStore, SpawnMarkerEntity> spawnMarkerEntityComponentType, UUID uuid, @Nonnull SpawnSuppressorEntry entry, @Nonnull SpawnSuppressionController suppressionController, @Nonnull Store<EntityStore> store, @Nonnull ChunkStore chunkComponentStore)`: Add description.
  - Executes `suppressSpawns` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onEntityRemoved` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `getGroup()`: Add description.
  - Executes `getGroup` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> reference, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> reference, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.
- `onSystemAddedToStore(@Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onSystemAddedToStore` behavior.
- `onSystemRemovedFromStore(@Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onSystemRemovedFromStore` behavior.
- `onSystemUnregistered()`: Add description.
  - Executes `onSystemUnregistered` behavior.
- `onSpawnSuppressionsLoaded(@Nonnull LoadedAssetsEvent<String, SpawnSuppression, IndexedAssetMap<String, SpawnSuppression>> event)`: Add description.
  - Executes `onSpawnSuppressionsLoaded` behavior.
- `onSpawnSuppressionsRemoved(@Nonnull RemovedAssetsEvent<String, SpawnSuppression, IndexedAssetMap<String, SpawnSuppression>> event)`: Add description.
  - Executes `onSpawnSuppressionsRemoved` behavior.
- `rebuildSuppressionMap(@Nonnull World world, @Nonnull Store<EntityStore> store, @Nonnull SpawnSuppressionController suppressionController)`: Add description.
  - Executes `rebuildSuppressionMap` behavior.

## Notes
- No additional notes.
