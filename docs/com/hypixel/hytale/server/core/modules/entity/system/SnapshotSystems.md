# SnapshotSystems

## Overview
- Documentation for `SnapshotSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.system`.

## Constructors
- None.

## Methods
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `clone()`
  - Executes `clone` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
