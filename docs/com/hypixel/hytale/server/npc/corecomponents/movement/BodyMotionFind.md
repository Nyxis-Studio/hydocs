# BodyMotionFind

## Overview
- Documentation for `BodyMotionFind`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.movement`.

## Constructors
- `BodyMotionFind(@Nonnull BuilderBodyMotionFind builderMotionFind, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionFind` instance.

## Methods
- `canSwitchToSteering(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canSwitchToSteering` behavior.
- `shouldSkipSteering(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController activeMotionController, @Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `shouldSkipSteering` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull Vector3d position, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `canComputeMotion(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canComputeMotion` behavior.
- `isGoalReached(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull Vector3d position, @Nonnull Vector3d targetPosition, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGoalReached` behavior.
- `isGoalReached(@Nonnull Ref<EntityStore> ref, AStarBase aStarBase, @Nonnull AStarNode aStarNode, @Nonnull MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGoalReached` behavior.
- `estimateToGoal(@Nonnull AStarBase aStarBase, @Nonnull Vector3d fromPosition, MotionController motionController)`
  - Executes `estimateToGoal` behavior.
- `findBestPath(@Nonnull AStarBase aStarBase, MotionController controller)`
  - Executes `findBestPath` behavior.
- `onThrottling(MotionController motionController, @Nonnull Ref<EntityStore> ref, @Nonnull Steering steering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onThrottling` behavior.
- `onDeferring(MotionController motionController, @Nonnull Ref<EntityStore> ref, @Nonnull Steering steering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onDeferring` behavior.
- `lookAtTarget(@Nonnull Ref<EntityStore> ref, @Nonnull Steering steering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `lookAtTarget` behavior.
- `canReachTarget(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull Vector3d position, @Nonnull Vector3d targetPosition, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canReachTarget` behavior.
- `isBoundingBoxesOverlapping(@Nonnull Vector3d position, @Nonnull Vector3d endPosition)`
  - Executes `isBoundingBoxesOverlapping` behavior.
- `containsPosition(@Nonnull Vector3d position, @Nonnull Vector3d endPosition)`
  - Executes `containsPosition` behavior.
- `containsPosition(double p, double min, double max, double v)`
  - Executes `containsPosition` behavior.

## Notes
- No additional notes.
