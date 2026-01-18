# MovementStatesSystems

## Overview
- Documentation for `MovementStatesSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.movement`.

## Constructors
- None.

## Methods
- `getGroup()`
  - Executes `getGroup` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `queueUpdatesFor(@Nonnull Ref<EntityStore> ref, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo, @Nonnull MovementStatesComponent movementStatesComponent)`
  - Executes `queueUpdatesFor` behavior.
- `copyMovementStatesFrom(@Nonnull MovementStates from, @Nonnull MovementStates to)`
  - Executes `copyMovementStatesFrom` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
