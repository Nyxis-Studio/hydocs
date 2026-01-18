# LegacyEntityTrackerSystems

## Overview
- Documentation for `LegacyEntityTrackerSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.tracker`.

## Constructors
- None.

## Methods
- `sendPlayerSelf(@Nonnull Ref<EntityStore> viewerRef, @Nonnull Store<EntityStore> store)`
  - Executes `sendPlayerSelf` behavior.
- `clear(@Nonnull Player player, @Nonnull Holder<EntityStore> holder)`
  - Executes `clear` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `queueUpdatesFor(@Nonnull Ref<EntityStore> ref, @Nonnull LivingEntity entity, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo)`
  - Executes `queueUpdatesFor` behavior.
- `queueUpdatesFor(Ref<EntityStore> ref, @Nonnull PlayerSkinComponent component, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo)`
  - Executes `queueUpdatesFor` behavior.
- `queueUpdatesFor(Ref<EntityStore> ref, @Nullable ModelComponent model, float entityScale, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo)`
  - Executes `queueUpdatesFor` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `canHideEntities(Entity entity, @Nonnull PlayerSettings settings)`
  - Executes `canHideEntities` behavior.

## Notes
- No additional notes.
