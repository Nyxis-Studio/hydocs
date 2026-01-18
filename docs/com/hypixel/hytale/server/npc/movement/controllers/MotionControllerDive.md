**Source Hash:** `8c29517a9e720f9771ea885747394e4071dfff07d60167ec376755f6cacba33c`

# MotionControllerDive

## Overview

## Constructor Descriptions
- `MotionControllerDive(@Nonnull BuilderSupport builderSupport, @Nonnull BuilderMotionControllerDive builder)`
  - Creates a `MotionControllerDive` instance.

## Method Descriptions
- `activate()`: Add description.
  - Executes `activate` behavior.
- `getWanderVerticalMovementRatio()`: Add description.
  - Executes `getWanderVerticalMovementRatio` behavior.
- `computeMove(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull Steering steering, double dt, @Nonnull Vector3d translation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeMove` behavior.
- `shouldDampenAppliedVelocitiesY()`: Add description.
  - Executes `shouldDampenAppliedVelocitiesY` behavior.
- `shouldAlwaysUseGroundResistance()`: Add description.
  - Executes `shouldAlwaysUseGroundResistance` behavior.
- `computeTranslation(@Nonnull Vector3d translation, double dt, float heading, double moveSpeed, double climbSpeed)`: Add description.
  - Executes `computeTranslation` behavior.
- `isNearZero(float angle)`: Add description.
  - Executes `isNearZero` behavior.
- `setMotionKind(MotionKind motionKind)`: Add description.
  - Executes `setMotionKind` behavior.
- `executeMove(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Vector3d translation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `executeMove` behavior.
- `constrainRotations(Role role, @Nonnull TransformComponent transform)`: Add description.
  - Executes `constrainRotations` behavior.
- `getCurrentMaxBodyRotationSpeed()`: Add description.
  - Executes `getCurrentMaxBodyRotationSpeed` behavior.
- `canAct(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canAct` behavior.
- `inAir()`: Add description.
  - Executes `inAir` behavior.
- `inWater()`: Add description.
  - Executes `inWater` behavior.
- `onGround()`: Add description.
  - Executes `onGround` behavior.
- `getType()`: Add description.
  - Executes `getType` behavior.
- `bisect(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d validPosition, double validDistance, @Nonnull Vector3d invalidPosition, double invalidDistance, @Nonnull Vector3d result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `bisect` behavior.
- `bisect(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d validPosition, @Nonnull Vector3d invalidPosition, @Nonnull Vector3d result, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `bisect` behavior.
- `probeMove(@Nonnull Ref<EntityStore> ref, @Nonnull ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `probeMove` behavior.
- `spawned()`: Add description.
  - Executes `spawned` behavior.
- `getCurrentSpeed()`: Add description.
  - Executes `getCurrentSpeed` behavior.
- `getCurrentTurnRadius()`: Add description.
  - Executes `getCurrentTurnRadius` behavior.
- `getMaxClimbAngle()`: Add description.
  - Executes `getMaxClimbAngle` behavior.
- `getMaxSinkAngle()`: Add description.
  - Executes `getMaxSinkAngle` behavior.
- `getMaximumSpeed()`: Add description.
  - Executes `getMaximumSpeed` behavior.
- `isFastMotionKind(double speed)`: Add description.
  - Executes `isFastMotionKind` behavior.
- `is2D()`: Add description.
  - Executes `is2D` behavior.
- `canRestAtPlace()`: Add description.
  - Executes `canRestAtPlace` behavior.
- `getDesiredAltitudeWeight()`: Add description.
  - Executes `getDesiredAltitudeWeight` behavior.
- `getHeightOverGround()`: Add description.
  - Executes `getHeightOverGround` behavior.
- `estimateVelocity(Steering steering, @Nonnull Vector3d velocityOut)`: Add description.
  - Executes `estimateVelocity` behavior.
- `updateModelParameters(Ref<EntityStore> ref, Model model, @Nonnull Box boundingBox, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `updateModelParameters` behavior.
- `dampForceVelocity(@Nonnull Vector3d forceVelocity, double forceVelocityDamping, double interval, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `dampForceVelocity` behavior.
- `relativeSwimDepthToBoundingBox(double swimDepth, @Nullable Box boundingBox, float eyeHeight)`: Add description.
  - Executes `relativeSwimDepthToBoundingBox` behavior.
- `relativeSwimDepthToHeight(double swimDepth, @Nullable Box boundingBox, float eyeHeight)`: Add description.
  - Executes `relativeSwimDepthToHeight` behavior.
- `relativeSwimDepthToHeight(@Nullable Ref<EntityStore> ref, double swimDepth, Model model, Box boundingBox, @Nullable ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `relativeSwimDepthToHeight` behavior.
- `getDampingDeceleration()`: Add description.
  - Executes `getDampingDeceleration` behavior.

## Notes
- No additional notes.
