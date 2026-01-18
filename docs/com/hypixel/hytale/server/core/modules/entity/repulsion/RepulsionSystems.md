# RepulsionSystems

## Overview
- Documentation for `RepulsionSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.repulsion`.

## Constructors
- None.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull Repulsion component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, Repulsion oldComponent, @Nonnull Repulsion newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull Repulsion component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `queueUpdatesFor(Ref<EntityStore> ref, @Nonnull Repulsion repulsion, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo)`
  - Executes `queueUpdatesFor` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
