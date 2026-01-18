# PositionCacheSystems

## Overview
- Documentation for `PositionCacheSystems`.
- Declared as a class in `com.hypixel.hytale.server.npc.systems`.

## Constructors
- None.

## Methods
- `initialisePositionCache(@Nonnull Role role, @Nullable StateEvaluator stateEvaluator, double flockInfluenceRange)`
  - Executes `initialisePositionCache` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `steppedTick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `steppedTick` behavior.
- `addEntities(@Nonnull Ref<EntityStore> self, @Nonnull Vector3d position, @Nonnull EntityList entityList, @Nonnull SpatialResource<Ref<EntityStore>, EntityStore> spatialResource, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `addEntities` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, FlockMembership oldComponent, @Nonnull FlockMembership newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull FlockMembership component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.

## Notes
- No additional notes.
