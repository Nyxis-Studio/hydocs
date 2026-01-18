# BodyMotionLeave

## Overview
- Documentation for `BodyMotionLeave`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.movement`.

## Constructors
- `BodyMotionLeave(@Nonnull BuilderBodyMotionLeave builderMotionLeave, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionLeave` instance.

## Methods
- `isGoalReached(Ref<EntityStore> ref, @Nonnull MotionController controller, Vector3d position, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGoalReached` behavior.
- `isGoalReached(Ref<EntityStore> ref, @Nonnull AStarBase aStarBase, @Nonnull AStarNode aStarNode, @Nonnull MotionController controller, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGoalReached` behavior.
- `estimateToGoal(AStarBase aStarBase, Vector3d fromPosition, MotionController motionController)`
  - Executes `estimateToGoal` behavior.
- `findBestPath(@Nonnull AStarBase aStarBase, MotionController controller)`
  - Executes `findBestPath` behavior.

## Notes
- No additional notes.
