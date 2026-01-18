# BlockEntitySystems

## Overview
- Documentation for `BlockEntitySystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity`.

## Constructors
- None.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `queueUpdatesFor(Ref<EntityStore> ref, @Nonnull BlockEntity entity, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo, float entityScale)`
  - Executes `queueUpdatesFor` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
