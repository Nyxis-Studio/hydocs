# BlockModule

## Overview
- Documentation for `BlockModule`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.block`.

## Constructors
- `BlockModule(@Nonnull JavaPluginInit init)`
  - Creates a `BlockModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `ensureBlockEntity(WorldChunk chunk, int x, int y, int z)`
  - Executes `ensureBlockEntity` behavior.
- `onChunkPreLoadProcessEnsureBlockEntity(@Nonnull ChunkPreLoadProcessEvent event)`
  - Executes `onChunkPreLoadProcessEnsureBlockEntity` behavior.
- `getMigrationSystemType()`
  - Executes `getMigrationSystemType` behavior.
- `getBlockStateInfoComponentType()`
  - Executes `getBlockStateInfoComponentType` behavior.
- `getLaunchPadComponentType()`
  - Executes `getLaunchPadComponentType` behavior.
- `getRespawnBlockComponentType()`
  - Executes `getRespawnBlockComponentType` behavior.
- `getBlockMapMarkerComponentType()`
  - Executes `getBlockMapMarkerComponentType` behavior.
- `getBlockMapMarkersResourceType()`
  - Executes `getBlockMapMarkersResourceType` behavior.
- `getBlockStateInfoNeedRebuildResourceType()`
  - Executes `getBlockStateInfoNeedRebuildResourceType` behavior.
- `getBlockEntity(@Nonnull World world, int x, int y, int z)`
  - Executes `getBlockEntity` behavior.
- `getComponent(ComponentType<ChunkStore, T> componentType, World world, int x, int y, int z)`
  - Executes `getComponent` behavior.
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `getIndex()`
  - Executes `getIndex` behavior.
- `getChunkRef()`
  - Executes `getChunkRef` behavior.
- `markNeedsSaving()`
  - Executes `markNeedsSaving` behavior.
- `clone()`
  - Executes `clone` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `toString()`
  - Executes `toString` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityRemoved` behavior.
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `invalidateAndReturnIfNeedRebuild()`
  - Executes `invalidateAndReturnIfNeedRebuild` behavior.
- `markAsNeedRebuild()`
  - Executes `markAsNeedRebuild` behavior.

## Notes
- No additional notes.
