**Source Hash:** `e9eb778926a6125f7f139e5b1e28459e48764cecd870c11ce7e89ead152f312c`

# SensorEntityBase

## Overview

## Constructor Descriptions
- `SensorEntityBase(@Nonnull BuilderSensorEntityBase builder, ISensorEntityPrioritiser prioritiser, @Nonnull BuilderSupport builderSupport)`
  - Creates a `SensorEntityBase` instance.

## Method Descriptions
- `matches(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `matches` behavior.
- `done()`: Add description.
  - Executes `done` behavior.
- `getSensorInfo()`: Add description.
  - Executes `getSensorInfo` behavior.
- `registerWithSupport(@Nonnull Role role)`: Add description.
  - Executes `registerWithSupport` behavior.
- `motionControllerChanged(@Nullable Ref<EntityStore> ref, @Nonnull NPCEntity npcComponent, MotionController motionController, @Nullable ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `motionControllerChanged` behavior.
- `loaded(Role role)`: Add description.
  - Executes `loaded` behavior.
- `spawned(Role role)`: Add description.
  - Executes `spawned` behavior.
- `unloaded(Role role)`: Add description.
  - Executes `unloaded` behavior.
- `removed(Role role)`: Add description.
  - Executes `removed` behavior.
- `teleported(Role role, World from, World to)`: Add description.
  - Executes `teleported` behavior.
- `initialisePrioritiser()`: Add description.
  - Executes `initialisePrioritiser` behavior.
- `isGetPlayers()`: Add description.
  - Executes `isGetPlayers` behavior.
- `isGetNPCs()`: Add description.
  - Executes `isGetNPCs` behavior.
- `isExcludingOwnType()`: Add description.
  - Executes `isExcludingOwnType` behavior.
- `filterLockedEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull Role role, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `filterLockedEntity` behavior.
- `filterEntityWithRange(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Vector3d position, @Nonnull Role role, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `filterEntityWithRange` behavior.
- `filterEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `filterEntity` behavior.
- `filterPrioritisedPlayer(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `filterPrioritisedPlayer` behavior.
- `filterPrioritisedNPC(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `filterPrioritisedNPC` behavior.
- `filterPrioritisedEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> targetRef, @Nonnull Role role, @Nonnull Store<EntityStore> store, @Nonnull IEntityByPriorityFilter playerPrioritiser)`: Add description.
  - Executes `filterPrioritisedEntity` behavior.
- `findPlayerOrEntity(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull Role role, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `findPlayerOrEntity` behavior.

## Notes
- No additional notes.
