# BodyMotionMoveAway

## Overview
- Documentation for `BodyMotionMoveAway`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.movement`.

## Constructors
- `BodyMotionMoveAway(@Nonnull BuilderBodyMotionMoveAway builderMotionFind, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionMoveAway` instance.

## Methods
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, Vector3d position, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `isGoalReached(Ref<EntityStore> ref, AStarBase aStarBase, @Nonnull AStarNode aStarNode, MotionController motionController, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGoalReached` behavior.
- `isGoalReached(Ref<EntityStore> ref, @Nonnull MotionController motionController, Vector3d position, Vector3d lastTestedPosition, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGoalReached` behavior.
- `estimateToGoal(@Nonnull AStarBase aStarBase, Vector3d fromPosition, @Nonnull MotionController motionController)`
  - Executes `estimateToGoal` behavior.
- `findBestPath(@Nonnull AStarBase aStarBase, MotionController controller)`
  - Executes `findBestPath` behavior.

## Notes
- No additional notes.
