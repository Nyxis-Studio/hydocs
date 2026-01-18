# AudioSystems

## Overview
- Documentation for `AudioSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.system`.

## Constructors
- None.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `playMoveInSound(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> store, @Nonnull MovementAudioComponent movementAudioComponent, @Nonnull Vector3d position, int insideBlockTypeId)`
  - Executes `playMoveInSound` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `queueUpdatesFor(@Nonnull Ref<EntityStore> ref, @Nonnull AudioComponent audioComponent, @Nonnull Map<Ref<EntityStore>, EntityTrackerSystems.EntityViewer> visibleTo)`
  - Executes `queueUpdatesFor` behavior.

## Notes
- No additional notes.
