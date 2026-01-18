**Source Hash:** `f731a16a521ecc539deb843900488c42a4f3bcb7cf7dc4cad99b603272a2733a`

# BodyMotionFindBase

## Overview

## Constructor Descriptions
- `BodyMotionFindBase(@Nonnull BuilderBodyMotionFindBase builderBodyMotionFindBase, @Nonnull BuilderSupport support, @Nonnull T aStar)`
  - Creates a `BodyMotionFindBase` instance.

## Method Descriptions
- `activate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `activate` behavior.
- `deactivate(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `deactivate` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider infoProvider, double dt, @Nonnull Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeSteering` behavior.
- `findBestPath(AStarBase var1, MotionController var2)`: Add description.
  - Executes `findBestPath` behavior.
- `startPathFinder(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, Role role, @Nonnull MotionController activeMotionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `startPathFinder` behavior.
- `continuePathFinder(@Nonnull Ref<EntityStore> ref, @Nonnull MotionController activeMotionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `continuePathFinder` behavior.
- `updatePathFollower(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull MotionController activeMotionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `updatePathFollower` behavior.
- `canSwitchToSteering(@Nonnull Ref<EntityStore> ref, MotionController motionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canSwitchToSteering` behavior.
- `shouldSkipSteering(@Nonnull Ref<EntityStore> ref, MotionController activeMotionController, Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `shouldSkipSteering` behavior.
- `computeSteering(@Nonnull Ref<EntityStore> ref, Role role, Vector3d position, Steering desiredSteering, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeSteering` behavior.
- `scaleSteering(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull SteeringForceWithTarget steeringForce, @Nonnull Steering desiredSteering, double desiredAltitudeWeight, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `scaleSteering` behavior.
- `computeDesiredYTranslation(@Nonnull Steering desiredSteering, float maxAngle, double desiredAltitudeWeight)`: Add description.
  - Executes `computeDesiredYTranslation` behavior.
- `onNoPathFound(MotionController motionController)`: Add description.
  - Executes `onNoPathFound` behavior.
- `onBlockedPath()`: Add description.
  - Executes `onBlockedPath` behavior.
- `onSteering(MotionController activeMotionController, Ref<EntityStore> ref, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onSteering` behavior.
- `onThrottling(MotionController motionController, Ref<EntityStore> ref, Steering steering, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onThrottling` behavior.
- `onDeferring(MotionController motionController, Ref<EntityStore> ref, Steering steering, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onDeferring` behavior.
- `mustAbortThrottling(MotionController motionController, Ref<EntityStore> ref)`: Add description.
  - Executes `mustAbortThrottling` behavior.
- `isGoalReached(Ref<EntityStore> var1, MotionController var2, Vector3d var3, ComponentAccessor<EntityStore> var4)`: Add description.
  - Executes `isGoalReached` behavior.
- `setNavState(NavState state, String label, boolean reset, @Nonnull MotionController activeMotionController)`: Add description.
  - Executes `setNavState` behavior.
- `decorateDebugString(StringBuilder dbgString)`: Add description.
  - Executes `decorateDebugString` behavior.
- `setNavStateInit(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateInit` behavior.
- `setNavStateComputing(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateComputing` behavior.
- `setNavStateDeferred(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateDeferred` behavior.
- `setNavStateAtGoal(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateAtGoal` behavior.
- `setNavStateFollowing(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateFollowing` behavior.
- `setNavStateSteering(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateSteering` behavior.
- `setNavStateBlocked(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateBlocked` behavior.
- `setNavStateAborted(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateAborted` behavior.
- `setNavStateThrottling(@Nonnull MotionController motionController)`: Add description.
  - Executes `setNavStateThrottling` behavior.
- `setPath(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull MotionController activeMotionController, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `setPath` behavior.
- `resetThrottleCount()`: Add description.
  - Executes `resetThrottleCount` behavior.
- `shouldDeferPathComputation(MotionController motionController, Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `shouldDeferPathComputation` behavior.
- `canComputeMotion(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nullable InfoProvider positionProvider, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canComputeMotion` behavior.
- `mustRecomputePath(@Nonnull MotionController activeMotionController)`: Add description.
  - Executes `mustRecomputePath` behavior.
- `getRelativeSpeed()`: Add description.
  - Executes `getRelativeSpeed` behavior.
- `forceRecomputePath(MotionController activeMotionController)`: Add description.
  - Executes `forceRecomputePath` behavior.
- `get()`: Add description.
  - Executes `get` behavior.

## Notes
- No additional notes.
