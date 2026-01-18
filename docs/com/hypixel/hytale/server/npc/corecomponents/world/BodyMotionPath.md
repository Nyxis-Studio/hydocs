**Source Hash:** `8dd70f8c4881ae838c31eface5a4ab69079358664c7aa7ce7dd783349e4ee2ed`

# BodyMotionPath

## Overview

## Constructor Descriptions
- `BodyMotionPath(@Nonnull BuilderBodyMotionPath builder, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionPath` instance.

## Method Descriptions
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `activate` behavior.
- `loaded(Role role)`: Add description.
  - Executes `loaded` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeSteering` behavior.
- `tickObservationDelay(double dt)`: Add description.
  - Executes `tickObservationDelay` behavior.
- `pickNextObservationAngle()`: Add description.
  - Executes `pickNextObservationAngle` behavior.
- `closeToPosition(Vector3d position, @Nonnull MotionController motionController)`: Add description.
  - Executes `closeToPosition` behavior.
- `invalidateWaypoint()`: Add description.
  - Executes `invalidateWaypoint` behavior.
- `nextWayPoint(@Nonnull IPath<?> path, @Nonnull WorldSupport support, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `nextWayPoint` behavior.
- `getFirstWaypoint(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable IPath<?> path, @Nonnull Vector3d lastPos, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getFirstWaypoint` behavior.
- `waypointIndexUpdated(@Nonnull IPath<?> path, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `waypointIndexUpdated` behavior.
- `initializeCurrentDirection()`: Add description.
  - Executes `initializeCurrentDirection` behavior.
- `reset()`: Add description.
  - Executes `reset` behavior.
- `get()`: Add description.
  - Executes `get` behavior.

## Notes
- No additional notes.
