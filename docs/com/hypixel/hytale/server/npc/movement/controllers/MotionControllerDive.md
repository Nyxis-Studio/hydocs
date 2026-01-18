# MotionControllerDive

## Overview
- Documentation for `MotionControllerDive`.
- Declared as a class in `com.hypixel.hytale.server.npc.movement.controllers`.

## Constructors
- `MotionControllerDive(@Nonnull BuilderSupport builderSupport, @Nonnull BuilderMotionControllerDive builder)`
  - Creates a `MotionControllerDive` instance.

## Methods
- `activate()`
  - Executes `activate` behavior.
- `getWanderVerticalMovementRatio()`
  - Executes `getWanderVerticalMovementRatio` behavior.
- `computeMove(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull Steering steering, double dt, @Nonnull Vector3d translation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeMove` behavior.
- `shouldDampenAppliedVelocitiesY()`
  - Executes `shouldDampenAppliedVelocitiesY` behavior.
- `shouldAlwaysUseGroundResistance()`
  - Executes `shouldAlwaysUseGroundResistance` behavior.
- `computeTranslation(@Nonnull Vector3d translation, double dt, float heading, double moveSpeed, double climbSpeed)`
  - Executes `computeTranslation` behavior.
- `isNearZero(float angle)`
  - Executes `isNearZero` behavior.
- `setMotionKind(MotionKind motionKind)`
  - Executes `setMotionKind` behavior.
- `executeMove(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Vector3d translation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `executeMove` behavior.
- `constrainRotations(Role role, @Nonnull TransformComponent transform)`
  - Executes `constrainRotations` behavior.
- `getCurrentMaxBodyRotationSpeed()`
  - Executes `getCurrentMaxBodyRotationSpeed` behavior.
- `canAct(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canAct` behavior.
- `inAir()`
  - Executes `inAir` behavior.
- `inWater()`
  - Executes `inWater` behavior.
- `onGround()`
  - Executes `onGround` behavior.
- `getType()`
  - Executes `getType` behavior.
- `bisect(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d validPosition, double validDistance, @Nonnull Vector3d invalidPosition, double invalidDistance, @Nonnull Vector3d result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `bisect` behavior.
- `bisect(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d validPosition, @Nonnull Vector3d invalidPosition, @Nonnull Vector3d result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `bisect` behavior.
- `probeMove(@Nonnull Ref<EntityStore> ref, @Nonnull ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `probeMove` behavior.
- `spawned()`
  - Executes `spawned` behavior.
- `getCurrentSpeed()`
  - Executes `getCurrentSpeed` behavior.
- `getCurrentTurnRadius()`
  - Executes `getCurrentTurnRadius` behavior.
- `getMaxClimbAngle()`
  - Executes `getMaxClimbAngle` behavior.
- `getMaxSinkAngle()`
  - Executes `getMaxSinkAngle` behavior.
- `getMaximumSpeed()`
  - Executes `getMaximumSpeed` behavior.
- `isFastMotionKind(double speed)`
  - Executes `isFastMotionKind` behavior.
- `is2D()`
  - Executes `is2D` behavior.
- `canRestAtPlace()`
  - Executes `canRestAtPlace` behavior.
- `getDesiredAltitudeWeight()`
  - Executes `getDesiredAltitudeWeight` behavior.
- `getHeightOverGround()`
  - Executes `getHeightOverGround` behavior.
- `estimateVelocity(Steering steering, @Nonnull Vector3d velocityOut)`
  - Executes `estimateVelocity` behavior.
- `updateModelParameters(Ref<EntityStore> ref, Model model, @Nonnull Box boundingBox, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `updateModelParameters` behavior.
- `dampForceVelocity(@Nonnull Vector3d forceVelocity, double forceVelocityDamping, double interval, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `dampForceVelocity` behavior.
- `relativeSwimDepthToBoundingBox(double swimDepth, @Nullable Box boundingBox, float eyeHeight)`
  - Executes `relativeSwimDepthToBoundingBox` behavior.
- `relativeSwimDepthToHeight(double swimDepth, @Nullable Box boundingBox, float eyeHeight)`
  - Executes `relativeSwimDepthToHeight` behavior.
- `relativeSwimDepthToHeight(@Nullable Ref<EntityStore> ref, double swimDepth, Model model, Box boundingBox, @Nullable ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `relativeSwimDepthToHeight` behavior.
- `getDampingDeceleration()`
  - Executes `getDampingDeceleration` behavior.

## Notes
- No additional notes.
