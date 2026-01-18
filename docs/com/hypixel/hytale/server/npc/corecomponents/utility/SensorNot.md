# SensorNot

## Overview
- Documentation for `SensorNot`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.utility`.

## Constructors
- `SensorNot(@Nonnull BuilderSensorNot builder, @Nonnull BuilderSupport support, Sensor sensor)`
  - Creates a `SensorNot` instance.

## Methods
- `matches(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `matches` behavior.
- `getSensorInfo()`
  - Executes `getSensorInfo` behavior.
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
- `done()`
  - Executes `done` behavior.
- `componentCount()`
  - Executes `componentCount` behavior.
- `getComponent(int index)`
  - Executes `getComponent` behavior.
- `setContext(IAnnotatedComponent parent, int index)`
  - Executes `setContext` behavior.

## Notes
- No additional notes.
