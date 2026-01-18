# PathFollower

## Overview
- Documentation for `PathFollower`.
- Declared as a class in `com.hypixel.hytale.server.npc.navigation`.

## Constructors
- None.

## Methods
- `setPathSmoothing(int pathSmoothing)`
  - Executes `setPathSmoothing` behavior.
- `getRelativeSpeed()`
  - Executes `getRelativeSpeed` behavior.
- `setRelativeSpeed(double relativeSpeed)`
  - Executes `setRelativeSpeed` behavior.
- `setRelativeSpeedWaypoint(double relativeSpeedWaypoint)`
  - Executes `setRelativeSpeedWaypoint` behavior.
- `setWaypointRadius(double waypointRadius)`
  - Executes `setWaypointRadius` behavior.
- `setDebugNodes(boolean debugNodes)`
  - Executes `setDebugNodes` behavior.
- `shouldSmoothPath()`
  - Executes `shouldSmoothPath` behavior.
- `setRejectionWeight(double rejectionWeight)`
  - Executes `setRejectionWeight` behavior.
- `setBlendHeading(double blendHeading)`
  - Executes `setBlendHeading` behavior.
- `getCurrentWaypoint()`
  - Executes `getCurrentWaypoint` behavior.
- `getCurrentWaypointPosition()`
  - Executes `getCurrentWaypointPosition` behavior.
- `getNextWaypoint()`
  - Executes `getNextWaypoint` behavior.
- `getNextWaypointPosition()`
  - Executes `getNextWaypointPosition` behavior.
- `setPath(IWaypoint firstWaypoint, @Nonnull Vector3d startPosition)`
  - Executes `setPath` behavior.
- `clearPath()`
  - Executes `clearPath` behavior.
- `pathInFinalStage()`
  - Executes `pathInFinalStage` behavior.
- `freezeWaypoint()`
  - Executes `freezeWaypoint` behavior.
- `isWaypointFrozen()`
  - Executes `isWaypointFrozen` behavior.
- `setWaypointFrozen(boolean waypointFrozen)`
  - Executes `setWaypointFrozen` behavior.
- `executePath(@Nonnull Vector3d currentPosition, @Nonnull MotionController activeMotionController, @Nonnull Steering desiredSteering)`
  - Executes `executePath` behavior.
- `computeRejection(@Nonnull Vector3d currentPosition, @Nonnull Vector3d target, @Nonnull MotionController activeMotionController)`
  - Executes `computeRejection` behavior.
- `updateCurrentTarget(@Nonnull Vector3d entityPosition, @Nonnull MotionController motionController)`
  - Executes `updateCurrentTarget` behavior.
- `smoothPath(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull MotionController motionController, @Nonnull ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `smoothPath` behavior.
- `canMoveTo(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull Vector3d position, @Nonnull Vector3d targetPosition, @Nonnull ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canMoveTo` behavior.
- `getLength()`
  - Executes `getLength` behavior.
- `getPosition()`
  - Executes `getPosition` behavior.
- `advance(int skip)`
  - Executes `advance` behavior.
- `next()`
  - Executes `next` behavior.

## Notes
- No additional notes.
