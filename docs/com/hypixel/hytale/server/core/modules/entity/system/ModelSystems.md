# ModelSystems

## Overview
- Documentation for `ModelSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.system`.

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
- `queueUpdatesFor(@Nonnull Ref<EntityStore> ref, @Nonnull ActiveAnimationComponent animationComponent, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo)`
  - Executes `queueUpdatesFor` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull ModelComponent component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, ModelComponent oldComponent, @Nonnull ModelComponent newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull ModelComponent component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `updateMovementController(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `updateMovementController` behavior.
- `updateBoundingBox(@Nonnull Model model, @Nonnull BoundingBox boundingBox, @Nullable MovementStatesComponent movementStatesComponent)`
  - Executes `updateBoundingBox` behavior.
- `updateBoundingBox(@Nonnull Model model, @Nonnull BoundingBox boundingBox, @Nullable MovementStates movementStates)`
  - Executes `updateBoundingBox` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
