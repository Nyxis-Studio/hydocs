# ActionSequence

## Overview
- Documentation for `ActionSequence`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.utility`.

## Constructors
- `ActionSequence(@Nonnull BuilderActionSequence builder, @Nonnull BuilderSupport support)`
  - Creates a `ActionSequence` instance.

## Methods
- `canExecute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `canExecute` behavior.
- `execute(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, InfoProvider sensorInfo, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `execute` behavior.
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
- `setOnce()`
  - Executes `setOnce` behavior.
- `componentCount()`
  - Executes `componentCount` behavior.
- `getComponent(int index)`
  - Executes `getComponent` behavior.
- `setContext(IAnnotatedComponent parent, int index)`
  - Executes `setContext` behavior.

## Notes
- No additional notes.
