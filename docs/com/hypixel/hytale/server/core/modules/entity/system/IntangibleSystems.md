# IntangibleSystems

## Overview
- Documentation for `IntangibleSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.system`.

## Constructors
- None.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull Intangible component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, Intangible oldComponent, @Nonnull Intangible newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull Intangible component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `queueUpdatesFor(Ref<EntityStore> ref, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo)`
  - Executes `queueUpdatesFor` behavior.
- `getResourceType()`
  - Executes `getResourceType` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
