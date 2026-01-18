**Source Hash:** `202a776017860e49673d3b7ad2aa7f4b85a318fa9013f3b77a16f9ab9c23f467`

# BodyMotionMoveAway

## Overview

## Constructor Descriptions
- `BodyMotionMoveAway(@Nonnull BuilderBodyMotionMoveAway builderMotionFind, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionMoveAway` instance.

## Method Descriptions
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `activate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeSteering` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, Vector3d position, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeSteering` behavior.
- `isGoalReached(Ref<EntityStore> ref, AStarBase aStarBase, @Nonnull AStarNode aStarNode, MotionController motionController, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `isGoalReached` behavior.
- `isGoalReached(Ref<EntityStore> ref, @Nonnull MotionController motionController, Vector3d position, Vector3d lastTestedPosition, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `isGoalReached` behavior.
- `estimateToGoal(@Nonnull AStarBase aStarBase, Vector3d fromPosition, @Nonnull MotionController motionController)`: Add description.
  - Executes `estimateToGoal` behavior.
- `findBestPath(@Nonnull AStarBase aStarBase, MotionController controller)`: Add description.
  - Executes `findBestPath` behavior.

## Notes
- No additional notes.
