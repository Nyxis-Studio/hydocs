**Source Hash:** `fa09e7abf273dd5e5df1715bb7f8b88d1feba19e1a4ee5940859f9e2c5f2239e`

# EntityStatsSystems

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `getDependencies()`: Add description.
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`: Add description.
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `componentType()`: Add description.
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull EntityStatMap component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, EntityStatMap oldComponent, @Nonnull EntityStatMap newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull EntityStatMap component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onComponentRemoved` behavior.
- `getGroup()`: Add description.
  - Executes `getGroup` behavior.
- `queueUpdatesForNewlyVisible(@Nonnull Ref<EntityStore> ref, @Nonnull EntityStatMap statMap, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> newlyVisibleTo)`: Add description.
  - Executes `queueUpdatesForNewlyVisible` behavior.
- `queueUpdateForNewlyVisibleSelf(Ref<EntityStore> ref, @Nonnull EntityStatMap statMap, @Nonnull EntityTrackerSystems.EntityViewer viewer)`: Add description.
  - Executes `queueUpdateForNewlyVisibleSelf` behavior.
- `testMaxValue(float value, float previousValue, @Nonnull EntityStatValue stat, @Nullable EntityStatType.EntityStatEffects valueEffects)`: Add description.
  - Executes `testMaxValue` behavior.
- `testMinValue(float value, float previousValue, @Nonnull EntityStatValue stat, @Nullable EntityStatType.EntityStatEffects valueEffects)`: Add description.
  - Executes `testMinValue` behavior.
- `runInteractions(@Nonnull Ref<EntityStore> ref, @Nonnull InteractionManager interactionManager, @Nullable EntityStatType.EntityStatEffects valueEffects, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `runInteractions` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
