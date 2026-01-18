# MotionSequence

## Overview
- Documentation for `MotionSequence`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.utility`.

## Constructors
- `MotionSequence(@Nonnull BuilderMotionSequence<T> builder, T[] steps)`
  - Creates a `MotionSequence` instance.

## Methods
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `deactivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `deactivate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
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
- `componentCount()`
  - Executes `componentCount` behavior.
- `getComponent(int index)`
  - Executes `getComponent` behavior.
- `setContext(IAnnotatedComponent parent, int index)`
  - Executes `setContext` behavior.
- `restart()`
  - Executes `restart` behavior.
- `doActivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `doActivate` behavior.
- `activateNext(@Nonnull Ref<EntityStore> ref, int newIndex, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activateNext` behavior.

## Notes
- No additional notes.
