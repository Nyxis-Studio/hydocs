# HitboxCollisionSystems

## Overview
- Documentation for `HitboxCollisionSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.hitboxcollision`.

## Constructors
- None.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull HitboxCollision component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, HitboxCollision oldComponent, @Nonnull HitboxCollision newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull HitboxCollision component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `queueUpdatesFor(Ref<EntityStore> ref, @Nonnull HitboxCollision hitboxCollision, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo)`
  - Executes `queueUpdatesFor` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
