**Source Hash:** `8a3f320c026137daac91f26eb31565c833c81d5d0ce22ea80ebcda79e5c7a4b2`

# BodyMotionFind

## Overview

## Constructor Descriptions
- `BodyMotionFind(@Nonnull BuilderBodyMotionFind builderMotionFind, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionFind` instance.

## Method Descriptions
- `canSwitchToSteering(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canSwitchToSteering` behavior.
- `shouldSkipSteering(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController activeMotionController, @Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `shouldSkipSteering` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull Vector3d position, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeSteering` behavior.
- `canComputeMotion(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canComputeMotion` behavior.
- `isGoalReached(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull Vector3d position, @Nonnull Vector3d targetPosition, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `isGoalReached` behavior.
- `isGoalReached(@Nonnull Ref<EntityStore> ref, AStarBase aStarBase, @Nonnull AStarNode aStarNode, @Nonnull MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `isGoalReached` behavior.
- `estimateToGoal(@Nonnull AStarBase aStarBase, @Nonnull Vector3d fromPosition, MotionController motionController)`: Add description.
  - Executes `estimateToGoal` behavior.
- `findBestPath(@Nonnull AStarBase aStarBase, MotionController controller)`: Add description.
  - Executes `findBestPath` behavior.
- `onThrottling(MotionController motionController, @Nonnull Ref<EntityStore> ref, @Nonnull Steering steering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onThrottling` behavior.
- `onDeferring(MotionController motionController, @Nonnull Ref<EntityStore> ref, @Nonnull Steering steering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onDeferring` behavior.
- `lookAtTarget(@Nonnull Ref<EntityStore> ref, @Nonnull Steering steering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `lookAtTarget` behavior.
- `canReachTarget(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull Vector3d position, @Nonnull Vector3d targetPosition, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canReachTarget` behavior.
- `isBoundingBoxesOverlapping(@Nonnull Vector3d position, @Nonnull Vector3d endPosition)`: Add description.
  - Executes `isBoundingBoxesOverlapping` behavior.
- `containsPosition(@Nonnull Vector3d position, @Nonnull Vector3d endPosition)`: Add description.
  - Executes `containsPosition` behavior.
- `containsPosition(double p, double min, double max, double v)`: Add description.
  - Executes `containsPosition` behavior.

## Notes
- No additional notes.
