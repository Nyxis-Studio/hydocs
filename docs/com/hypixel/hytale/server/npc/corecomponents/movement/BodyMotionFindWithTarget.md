**Source Hash:** `5ef673b4deac6a7138e9d8cfa12ed0a6a25e840e15ed3dfdc1bb2ba154584990`

# BodyMotionFindWithTarget

## Overview

## Constructor Descriptions
- `BodyMotionFindWithTarget(@Nonnull BuilderBodyMotionFindWithTarget builderMotionFindWithTarget, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionFindWithTarget` instance.

## Method Descriptions
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `activate` behavior.
- `canComputeMotion(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canComputeMotion` behavior.
- `mustRecomputePath(@Nonnull MotionController activeMotionController)`: Add description.
  - Executes `mustRecomputePath` behavior.
- `forceRecomputePath(MotionController activeMotionController)`: Add description.
  - Executes `forceRecomputePath` behavior.
- `shouldDeferPathComputation(@Nonnull MotionController motionController, Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `shouldDeferPathComputation` behavior.
- `mustAbortThrottling(MotionController motionController, Ref<EntityStore> ref)`: Add description.
  - Executes `mustAbortThrottling` behavior.
- `isGoalReached(Ref<EntityStore> ref, MotionController activeMotionController, Vector3d position, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `isGoalReached` behavior.
- `onBlockedPath()`: Add description.
  - Executes `onBlockedPath` behavior.
- `onNoPathFound(MotionController motionController)`: Add description.
  - Executes `onNoPathFound` behavior.
- `onSteering(MotionController activeMotionController, @Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onSteering` behavior.
- `decorateDebugString(@Nonnull StringBuilder dbgString)`: Add description.
  - Executes `decorateDebugString` behavior.
- `isGoalReached(Ref<EntityStore> var1, MotionController var2, Vector3d var3, Vector3d var4, ComponentAccessor<EntityStore> var5)`: Add description.
  - Executes `isGoalReached` behavior.
- `getLastTargetPosition()`: Add description.
  - Executes `getLastTargetPosition` behavior.
- `getLastAccessibleTargetPosition(@Nonnull MotionController motionController, boolean approximate, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `getLastAccessibleTargetPosition` behavior.

## Notes
- No additional notes.
