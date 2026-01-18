**Source Hash:** `cb0d4fe6e00264688e62fc4a389dba117d036ed3a4c70d652a9ee2269320f116`

# MotionTimer

## Overview

## Constructor Descriptions
- `MotionTimer(@Nonnull BuilderMotionTimer<T> builder, @Nonnull BuilderSupport builderSupport, T motion)`
  - Creates a `MotionTimer` instance.

## Method Descriptions
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `activate` behavior.
- `deactivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `deactivate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role support, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
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

## Notes
- No additional notes.
