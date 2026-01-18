# SensorPath

## Overview
- Documentation for `SensorPath`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.world`.

## Constructors
- `SensorPath(@Nonnull BuilderSensorPath builder, @Nonnull BuilderSupport support)`
  - Creates a `SensorPath` instance.

## Methods
- `matches(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Store<EntityStore> store)`
  - Executes `matches` behavior.
- `getSensorInfo()`
  - Executes `getSensorInfo` behavior.
- `pathMatches(@Nonnull IPath<?> path)`
  - Executes `pathMatches` behavior.
- `isInRange(double squaredDistance)`
  - Executes `isInRange` behavior.
- `findClosestWaypoint(@Nonnull IPath<?> path, @Nonnull Vector3d position, @Nonnull Vector3d cachedTarget, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `findClosestWaypoint` behavior.
- `get()`
  - Executes `get` behavior.

## Notes
- No additional notes.
