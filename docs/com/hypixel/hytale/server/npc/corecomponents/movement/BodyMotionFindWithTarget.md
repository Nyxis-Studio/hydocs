# BodyMotionFindWithTarget

## Overview
- Documentation for `BodyMotionFindWithTarget`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.movement`.

## Constructors
- `BodyMotionFindWithTarget(@Nonnull BuilderBodyMotionFindWithTarget builderMotionFindWithTarget, @Nonnull BuilderSupport support)`
  - Creates a `BodyMotionFindWithTarget` instance.

## Methods
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `canComputeMotion(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canComputeMotion` behavior.
- `mustRecomputePath(@Nonnull MotionController activeMotionController)`
  - Executes `mustRecomputePath` behavior.
- `forceRecomputePath(MotionController activeMotionController)`
  - Executes `forceRecomputePath` behavior.
- `shouldDeferPathComputation(@Nonnull MotionController motionController, Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `shouldDeferPathComputation` behavior.
- `mustAbortThrottling(MotionController motionController, Ref<EntityStore> ref)`
  - Executes `mustAbortThrottling` behavior.
- `isGoalReached(Ref<EntityStore> ref, MotionController activeMotionController, Vector3d position, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isGoalReached` behavior.
- `onBlockedPath()`
  - Executes `onBlockedPath` behavior.
- `onNoPathFound(MotionController motionController)`
  - Executes `onNoPathFound` behavior.
- `onSteering(MotionController activeMotionController, @Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onSteering` behavior.
- `decorateDebugString(@Nonnull StringBuilder dbgString)`
  - Executes `decorateDebugString` behavior.
- `isGoalReached(Ref<EntityStore> var1, MotionController var2, Vector3d var3, Vector3d var4, ComponentAccessor<EntityStore> var5)`
  - Executes `isGoalReached` behavior.
- `getLastTargetPosition()`
  - Executes `getLastTargetPosition` behavior.
- `getLastAccessibleTargetPosition(@Nonnull MotionController motionController, boolean approximate, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `getLastAccessibleTargetPosition` behavior.

## Notes
- No additional notes.
