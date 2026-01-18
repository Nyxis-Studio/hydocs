# EntityStatsSystems

## Overview
- Documentation for `EntityStatsSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entitystats`.

## Constructors
- None.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull EntityStatMap component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, EntityStatMap oldComponent, @Nonnull EntityStatMap newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull EntityStatMap component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `queueUpdatesForNewlyVisible(@Nonnull Ref<EntityStore> ref, @Nonnull EntityStatMap statMap, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> newlyVisibleTo)`
  - Executes `queueUpdatesForNewlyVisible` behavior.
- `queueUpdateForNewlyVisibleSelf(Ref<EntityStore> ref, @Nonnull EntityStatMap statMap, @Nonnull EntityTrackerSystems.EntityViewer viewer)`
  - Executes `queueUpdateForNewlyVisibleSelf` behavior.
- `testMaxValue(float value, float previousValue, @Nonnull EntityStatValue stat, @Nullable EntityStatType.EntityStatEffects valueEffects)`
  - Executes `testMaxValue` behavior.
- `testMinValue(float value, float previousValue, @Nonnull EntityStatValue stat, @Nullable EntityStatType.EntityStatEffects valueEffects)`
  - Executes `testMinValue` behavior.
- `runInteractions(@Nonnull Ref<EntityStore> ref, @Nonnull InteractionManager interactionManager, @Nullable EntityStatType.EntityStatEffects valueEffects, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `runInteractions` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
