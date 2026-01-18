**Source Hash:** `c3b079b6974ccda351d84fc90fe8fc8671cdb3a42b47bd6d31f38d07f8d73934`

# MotionSequence

## Overview

## Constructor Descriptions
- `MotionSequence(@Nonnull BuilderMotionSequence<T> builder, T[] steps)`
  - Creates a `MotionSequence` instance.

## Method Descriptions
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `activate` behavior.
- `deactivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `deactivate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeSteering` behavior.
- `registerWithSupport(Role role)`: Add description.
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
- `componentCount()`: Add description.
  - Executes `componentCount` behavior.
- `getComponent(int index)`: Add description.
  - Executes `getComponent` behavior.
- `setContext(IAnnotatedComponent parent, int index)`: Add description.
  - Executes `setContext` behavior.
- `restart()`: Add description.
  - Executes `restart` behavior.
- `doActivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `doActivate` behavior.
- `activateNext(@Nonnull Ref<EntityStore> ref, int newIndex, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `activateNext` behavior.

## Notes
- No additional notes.
