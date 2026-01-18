# SensorEntityBase

## Overview
- Documentation for `SensorEntityBase`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.entity`.

## Constructors
- `SensorEntityBase(@Nonnull BuilderSensorEntityBase builder, ISensorEntityPrioritiser prioritiser, @Nonnull BuilderSupport builderSupport)`
  - Creates a `SensorEntityBase` instance.

## Methods
- `matches(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `matches` behavior.
- `done()`
  - Executes `done` behavior.
- `getSensorInfo()`
  - Executes `getSensorInfo` behavior.
- `registerWithSupport(@Nonnull Role role)`
  - Executes `registerWithSupport` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `motionControllerChanged` behavior.
- `loaded(Role role)`
  - Executes `loaded` behavior.
- `spawned(Role role)`
  - Executes `spawned` behavior.
- `unloaded(Role role)`
  - Executes `unloaded` behavior.
- `removed(Role role)`
  - Executes `removed` behavior.
- `teleported(Role role, World from, World to)`
  - Executes `teleported` behavior.
- `initialisePrioritiser()`
  - Executes `initialisePrioritiser` behavior.
- `isGetPlayers()`
  - Executes `isGetPlayers` behavior.
- `isGetNPCs()`
  - Executes `isGetNPCs` behavior.
- `isExcludingOwnType()`
  - Executes `isExcludingOwnType` behavior.
- `filterLockedEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull Role role, @Nonnull Store<EntityStore> store)`
  - Executes `filterLockedEntity` behavior.
- `filterEntityWithRange(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Vector3d position, @Nonnull Role role, @Nonnull Store<EntityStore> store)`
  - Executes `filterEntityWithRange` behavior.
- `filterEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store)`
  - Executes `filterEntity` behavior.
- `filterPrioritisedPlayer(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store)`
  - Executes `filterPrioritisedPlayer` behavior.
- `filterPrioritisedNPC(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store)`
  - Executes `filterPrioritisedNPC` behavior.
- `filterPrioritisedEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store, @Nonnull IEntityByPriorityFilter playerPrioritiser)`
  - Executes `filterPrioritisedEntity` behavior.
- `findPlayerOrEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull Role role, @Nonnull Store<EntityStore> store)`
  - Executes `findPlayerOrEntity` behavior.

## Notes
- No additional notes.
