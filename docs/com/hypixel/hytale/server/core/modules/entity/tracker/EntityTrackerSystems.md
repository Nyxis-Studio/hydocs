# EntityTrackerSystems

## Overview
- Documentation for `EntityTrackerSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.tracker`.

## Constructors
- None.

## Methods
- `despawnAll(@Nonnull Ref<EntityStore> viewerRef, @Nonnull Store<EntityStore> store)`
  - Executes `despawnAll` behavior.
- `clear(@Nonnull Ref<EntityStore> viewerRef, @Nonnull Store<EntityStore> store)`
  - Executes `clear` behavior.
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `clone()`
  - Executes `clone` behavior.
- `queueRemove(Ref<EntityStore> ref, ComponentUpdateType type)`
  - Executes `queueRemove` behavior.
- `queueUpdate(Ref<EntityStore> ref, ComponentUpdate update)`
  - Executes `queueUpdate` behavior.
- `addViewerParallel(Ref<EntityStore> ref, EntityViewer entityViewer)`
  - Executes `addViewerParallel` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `queueFullUpdate(@Nonnull Ref<EntityStore> ref, @Nonnull EffectControllerComponent effectControllerComponent, @Nonnull Map<Ref<EntityStore>, EntityViewer> visibleTo)`
  - Executes `queueFullUpdate` behavior.
- `queueUpdatesFor(@Nonnull Ref<EntityStore> ref, @Nonnull EffectControllerComponent effectControllerComponent, @Nonnull Map<Ref<EntityStore>, EntityViewer> visibleTo, @Nonnull Map<Ref<EntityStore>, EntityViewer> exclude)`
  - Executes `queueUpdatesFor` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.
- `queueRemove(@Nonnull ComponentUpdateType type)`
  - Executes `queueRemove` behavior.
- `queueUpdate(@Nonnull ComponentUpdate update)`
  - Executes `queueUpdate` behavior.
- `toRemovedArray()`
  - Executes `toRemovedArray` behavior.
- `toUpdatesArray()`
  - Executes `toUpdatesArray` behavior.

## Notes
- No additional notes.
