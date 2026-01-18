# PatrolPath

## Overview
- Documentation for `PatrolPath`.
- Declared as a class in `com.hypixel.hytale.builtin.path.path`.

## Constructors
- `PatrolPath(int worldgenId, UUID id, String name)`
  - Creates a `PatrolPath` instance.

## Methods
- `getId()`
  - Executes `getId` behavior.
- `getName()`
  - Executes `getName` behavior.
- `getPathWaypoints()`
  - Executes `getPathWaypoints` behavior.
- `registerNewWaypoint(@Nonnull IPrefabPathWaypoint waypoint, int worldGenId)`
  - Executes `registerNewWaypoint` behavior.
- `registerNewWaypointAt(int index, @Nonnull IPrefabPathWaypoint waypoint, int worldGenId)`
  - Executes `registerNewWaypointAt` behavior.
- `addLoadedWaypoint(@Nonnull IPrefabPathWaypoint waypoint, int pathLength, int index, int worldGenId)`
  - Executes `addLoadedWaypoint` behavior.
- `removeWaypoint(int index, int worldGenId)`
  - Executes `removeWaypoint` behavior.
- `unloadWaypoint(int index)`
  - Executes `unloadWaypoint` behavior.
- `hasLoadedWaypoints()`
  - Executes `hasLoadedWaypoints` behavior.
- `isFullyLoaded()`
  - Executes `isFullyLoaded` behavior.
- `loadedWaypointCount()`
  - Executes `loadedWaypointCount` behavior.
- `getWorldGenId()`
  - Executes `getWorldGenId` behavior.
- `getNearestWaypointPosition(@Nonnull Vector3d origin, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getNearestWaypointPosition` behavior.
- `mergeInto(@Nonnull IPrefabPath target, int worldGenId, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `mergeInto` behavior.
- `compact(int worldGenId)`
  - Executes `compact` behavior.
- `length()`
  - Executes `length` behavior.
- `get(int index)`
  - Executes `get` behavior.

## Notes
- No additional notes.
