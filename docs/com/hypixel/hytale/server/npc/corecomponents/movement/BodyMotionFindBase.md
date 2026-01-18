# BodyMotionFindBase

## Overview
- Documentation for `BodyMotionFindBase`.
- Declared as a class in `com.hypixel.hytale.server.npc.corecomponents.movement`.

## Constructors
- `BodyMotionFindBase(@Nonnull BuilderBodyMotionFindBase builderBodyMotionFindBase, @Nonnull BuilderSupport support, @Nonnull T aStar)`
  - Creates a `BodyMotionFindBase` instance.

## Methods
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `activate` behavior.
- `deactivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `deactivate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `findBestPath(AStarBase var1, MotionController var2)`
  - Executes `findBestPath` behavior.
- `startPathFinder(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, Role role, @Nonnull MotionController activeMotionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `startPathFinder` behavior.
- `continuePathFinder(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController activeMotionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `continuePathFinder` behavior.
- `updatePathFollower(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull MotionController activeMotionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `updatePathFollower` behavior.
- `canSwitchToSteering(@Nonnull Ref<EntityStore> ref, MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canSwitchToSteering` behavior.
- `shouldSkipSteering(@Nonnull Ref<EntityStore> ref, MotionController activeMotionController, Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `shouldSkipSteering` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, Role role, Vector3d position, Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeSteering` behavior.
- `scaleSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull SteeringForceWithTarget steeringForce, @Nonnull Steering desiredSteering, double desiredAltitudeWeight, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `scaleSteering` behavior.
- `computeDesiredYTranslation(@Nonnull Steering desiredSteering, float maxAngle, double desiredAltitudeWeight)`
  - Executes `computeDesiredYTranslation` behavior.
- `onNoPathFound(MotionController motionController)`
  - Executes `onNoPathFound` behavior.
- `onBlockedPath()`
  - Executes `onBlockedPath` behavior.
- `onSteering(MotionController activeMotionController, Ref<EntityStore> ref, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onSteering` behavior.
- `onThrottling(MotionController motionController, Ref<EntityStore> ref, Steering steering, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onThrottling` behavior.
- `onDeferring(MotionController motionController, Ref<EntityStore> ref, Steering steering, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onDeferring` behavior.
- `mustAbortThrottling(MotionController motionController, Ref<EntityStore> ref)`
  - Executes `mustAbortThrottling` behavior.
- `isGoalReached(Ref<EntityStore> var1, MotionController var2, Vector3d var3, ComponentAccessor<EntityStore> var4)`
  - Executes `isGoalReached` behavior.
- `setNavState(NavState state, String label, boolean reset, @Nonnull MotionController activeMotionController)`
  - Executes `setNavState` behavior.
- `decorateDebugString(StringBuilder dbgString)`
  - Executes `decorateDebugString` behavior.
- `setNavStateInit(@Nonnull MotionController motionController)`
  - Executes `setNavStateInit` behavior.
- `setNavStateComputing(@Nonnull MotionController motionController)`
  - Executes `setNavStateComputing` behavior.
- `setNavStateDeferred(@Nonnull MotionController motionController)`
  - Executes `setNavStateDeferred` behavior.
- `setNavStateAtGoal(@Nonnull MotionController motionController)`
  - Executes `setNavStateAtGoal` behavior.
- `setNavStateFollowing(@Nonnull MotionController motionController)`
  - Executes `setNavStateFollowing` behavior.
- `setNavStateSteering(@Nonnull MotionController motionController)`
  - Executes `setNavStateSteering` behavior.
- `setNavStateBlocked(@Nonnull MotionController motionController)`
  - Executes `setNavStateBlocked` behavior.
- `setNavStateAborted(@Nonnull MotionController motionController)`
  - Executes `setNavStateAborted` behavior.
- `setNavStateThrottling(@Nonnull MotionController motionController)`
  - Executes `setNavStateThrottling` behavior.
- `setPath(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull MotionController activeMotionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `setPath` behavior.
- `resetThrottleCount()`
  - Executes `resetThrottleCount` behavior.
- `shouldDeferPathComputation(MotionController motionController, Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `shouldDeferPathComputation` behavior.
- `canComputeMotion(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider positionProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canComputeMotion` behavior.
- `mustRecomputePath(@Nonnull MotionController activeMotionController)`
  - Executes `mustRecomputePath` behavior.
- `getRelativeSpeed()`
  - Executes `getRelativeSpeed` behavior.
- `forceRecomputePath(MotionController activeMotionController)`
  - Executes `forceRecomputePath` behavior.
- `get()`
  - Executes `get` behavior.

## Notes
- No additional notes.
