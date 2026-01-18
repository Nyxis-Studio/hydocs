# BodyMotionPath

## Overview
- Documentation for `BodyMotionPath`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.world`.

## Constructors
- `BodyMotionPath(@Nonnull BuilderBodyMotionPath builder, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionPath` instance.

## Methods
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `loaded(Role role)`
  - Executes `loaded` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider sensorInfo, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `tickObservationDelay(double dt)`
  - Executes `tickObservationDelay` behavior.
- `pickNextObservationAngle()`
  - Executes `pickNextObservationAngle` behavior.
- `closeToPosition(Vector3d position, @Nonnull MotionController motionController)`
  - Executes `closeToPosition` behavior.
- `invalidateWaypoint()`
  - Executes `invalidateWaypoint` behavior.
- `nextWayPoint(@Nonnull IPath<?> path, @Nonnull WorldSupport support, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `nextWayPoint` behavior.
- `getFirstWaypoint(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable IPath<?> path, @Nonnull Vector3d lastPos, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getFirstWaypoint` behavior.
- `waypointIndexUpdated(@Nonnull IPath<?> path, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `waypointIndexUpdated` behavior.
- `initializeCurrentDirection()`
  - Executes `initializeCurrentDirection` behavior.
- `reset()`
  - Executes `reset` behavior.
- `get()`
  - Executes `get` behavior.

## Notes
- No additional notes.
