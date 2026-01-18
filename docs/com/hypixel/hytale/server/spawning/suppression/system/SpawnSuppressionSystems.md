# SpawnSuppressionSystems

## Overview
- Documentation for `SpawnSuppressionSystems`.
- Declared as a class in `com.hypixel.hytale.server.spawning.suppression.system`.

## Constructors
- None.

## Methods
- `suppressSpawns(@Nonnull ResourceType<ChunkStore, ChunkSuppressionQueue> chunkSuppressionQueueResourceType, @Nonnull ComponentType<EntityStore, SpawnMarkerEntity> spawnMarkerEntityComponentType, UUID uuid, @Nonnull SpawnSuppressorEntry entry, @Nonnull SpawnSuppressionController suppressionController, @Nonnull Store<EntityStore> store, @Nonnull ChunkStore chunkComponentStore)`
  - Executes `suppressSpawns` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> reference, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> reference, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `onSystemAddedToStore(@Nonnull Store<EntityStore> store)`
  - Executes `onSystemAddedToStore` behavior.
- `onSystemRemovedFromStore(@Nonnull Store<EntityStore> store)`
  - Executes `onSystemRemovedFromStore` behavior.
- `onSystemUnregistered()`
  - Executes `onSystemUnregistered` behavior.
- `onSpawnSuppressionsLoaded(@Nonnull LoadedAssetsEvent<String, SpawnSuppression, IndexedAssetMap<String, SpawnSuppression>> event)`
  - Executes `onSpawnSuppressionsLoaded` behavior.
- `onSpawnSuppressionsRemoved(@Nonnull RemovedAssetsEvent<String, SpawnSuppression, IndexedAssetMap<String, SpawnSuppression>> event)`
  - Executes `onSpawnSuppressionsRemoved` behavior.
- `rebuildSuppressionMap(@Nonnull World world, @Nonnull Store<EntityStore> store, @Nonnull SpawnSuppressionController suppressionController)`
  - Executes `rebuildSuppressionMap` behavior.

## Notes
- No additional notes.
