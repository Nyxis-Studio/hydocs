# BodyMotionLand

## Overview
- Documentation for `BodyMotionLand`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.movement`.

## Constructors
- `BodyMotionLand(@Nonnull BuilderBodyMotionLand builderMotionLand, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionLand` instance.

## Methods
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `canComputeMotion(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider positionProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canComputeMotion` behavior.
- `isGoalReached(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController motionController, @Nonnull Vector3d position, @Nonnull Vector3d targetPosition, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGoalReached` behavior.

## Notes
- No additional notes.
