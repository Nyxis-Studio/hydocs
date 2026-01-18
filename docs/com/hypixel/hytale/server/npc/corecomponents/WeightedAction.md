# WeightedAction

## Overview
- Documentation for `WeightedAction`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents`.

## Constructors
- `WeightedAction(@Nonnull BuilderWeightedAction builder, @Nonnull BuilderSupport support)`
  - Creates a `WeightedAction` instance.

## Methods
- `getWeight()`
  - Executes `getWeight` behavior.
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
- `activate(Role role, InfoProvider infoProvider)`
  - Executes `activate` behavior.
- `deactivate(Role role, InfoProvider infoProvider)`
  - Executes `deactivate` behavior.
- `isActivated()`
  - Executes `isActivated` behavior.
- `getInfo(Role role, ComponentInfo holder)`
  - Executes `getInfo` behavior.
- `processDelay(float dt)`
  - Executes `processDelay` behavior.
- `clearOnce()`
  - Executes `clearOnce` behavior.
- `setOnce()`
  - Executes `setOnce` behavior.
- `isTriggered()`
  - Executes `isTriggered` behavior.
- `registerWithSupport(Role role)`
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

## Notes
- No additional notes.
