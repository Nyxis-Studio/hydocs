**Source Hash:** `d4a943c740ec9f3438feb22b915ffcff4d248d1dbc07477a2fff528b0bd3faab`

# MotionControllerFly

## Overview

## Constructor Descriptions
- `MotionControllerFly(@Nonnull BuilderSupport builderSupport, @Nonnull BuilderMotionControllerFly builder)`
  - Creates a `MotionControllerFly` instance.

## Method Descriptions
- `getType()`: Add description.
  - Executes `getType` behavior.
- `computeMove(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull Steering steering, double dt, @Nonnull Vector3d translation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `computeMove` behavior.
- `setDirectionFromTranslation(@Nonnull Steering steering, @Nonnull Vector3d translation)`: Add description.
  - Executes `setDirectionFromTranslation` behavior.
- `probeMove(@Nonnull Ref<EntityStore> ref, @Nonnull ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `probeMove` behavior.
- `isFastMotionKind(double speed)`: Add description.
  - Executes `isFastMotionKind` behavior.
- `getWanderVerticalMovementRatio()`: Add description.
  - Executes `getWanderVerticalMovementRatio` behavior.
- `doMove(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull Vector3d translation, @Nonnull PositionProbeAir moveProbe, @Nullable ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `doMove` behavior.
- `executeMove(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Vector3d translation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `executeMove` behavior.
- `constrainRotations(Role role, TransformComponent transform)`: Add description.
  - Executes `constrainRotations` behavior.
- `getCurrentMaxBodyRotationSpeed()`: Add description.
  - Executes `getCurrentMaxBodyRotationSpeed` behavior.
- `dampForceVelocity(@Nonnull Vector3d forceVelocity, double forceVelocityDamping, double interval, ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `dampForceVelocity` behavior.
- `shouldDampenAppliedVelocitiesY()`: Add description.
  - Executes `shouldDampenAppliedVelocitiesY` behavior.
- `shouldAlwaysUseGroundResistance()`: Add description.
  - Executes `shouldAlwaysUseGroundResistance` behavior.
- `spawned()`: Add description.
  - Executes `spawned` behavior.
- `canAct(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `canAct` behavior.
- `inAir()`: Add description.
  - Executes `inAir` behavior.
- `onGround()`: Add description.
  - Executes `onGround` behavior.
- `inWater()`: Add description.
  - Executes `inWater` behavior.
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
- `is2D()`: Add description.
  - Executes `is2D` behavior.
- `canRestAtPlace()`: Add description.
  - Executes `canRestAtPlace` behavior.
- `getDesiredAltitudeWeight()`: Add description.
  - Executes `getDesiredAltitudeWeight` behavior.
- `getHeightOverGround()`: Add description.
  - Executes `getHeightOverGround` behavior.
- `isHorizontalIdle(double speed)`: Add description.
  - Executes `isHorizontalIdle` behavior.
- `estimateVelocity(Steering steering, @Nonnull Vector3d velocityOut)`: Add description.
  - Executes `estimateVelocity` behavior.
- `clearOverrides()`: Add description.
  - Executes `clearOverrides` behavior.
- `setDesiredAltitudeOverride(double[] desiredAltitudeOverride)`: Add description.
  - Executes `setDesiredAltitudeOverride` behavior.
- `takeOff(@Nonnull Ref<EntityStore> ref, double speed, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `takeOff` behavior.
- `getMinSpeedAfterForceSquared()`: Add description.
  - Executes `getMinSpeedAfterForceSquared` behavior.
- `getDampingDeceleration()`: Add description.
  - Executes `getDampingDeceleration` behavior.
- `computeMaxSpeedFromPitch(double pitch)`: Add description.
  - Executes `computeMaxSpeedFromPitch` behavior.

## Notes
- No additional notes.
