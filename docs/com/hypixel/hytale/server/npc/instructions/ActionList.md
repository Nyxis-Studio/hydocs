# ActionList

## Overview
- Documentation for `ActionList`.
- Declared as a class in `com.hypixel.hytale.server.npc.instructions`.

## Constructors
- `ActionList(Action.EMPTY_ARRAY)`
  - Creates a `ActionList` instance.
- `ActionList(@Nonnull Action[] actions)`
  - Creates a `ActionList` instance.

## Methods
- `setBlocking(boolean blocking)`
  - Executes `setBlocking` behavior.
- `setAtomic(boolean atomic)`
  - Executes `setAtomic` behavior.
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
- `hasCompletedRun()`
  - Executes `hasCompletedRun` behavior.
- `setContext(IAnnotatedComponent parent)`
  - Executes `setContext` behavior.
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
- `clearOnce()`
  - Executes `clearOnce` behavior.
- `onEndMotion()`
  - Executes `onEndMotion` behavior.
- `setOnce()`
  - Executes `setOnce` behavior.
- `actionCount()`
  - Executes `actionCount` behavior.
- `getComponent(int index)`
  - Executes `getComponent` behavior.

## Notes
- No additional notes.
