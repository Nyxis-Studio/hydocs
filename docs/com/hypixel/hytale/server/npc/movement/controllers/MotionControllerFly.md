# MotionControllerFly

## Overview
- Documentation for `MotionControllerFly`.
- Declared as a class in `com.hypixel.hytale.server.npc.movement.controllers`.

## Constructors
- `MotionControllerFly(@Nonnull BuilderSupport builderSupport, @Nonnull BuilderMotionControllerFly builder)`
  - Creates a `MotionControllerFly` instance.

## Methods
- `getType()`
  - Executes `getType` behavior.
- `computeMove(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, @Nonnull Steering steering, double dt, @Nonnull Vector3d translation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `computeMove` behavior.
- `setDirectionFromTranslation(@Nonnull Steering steering, @Nonnull Vector3d translation)`
  - Executes `setDirectionFromTranslation` behavior.
- `probeMove(@Nonnull Ref<EntityStore> ref, @Nonnull ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `probeMove` behavior.
- `isFastMotionKind(double speed)`
  - Executes `isFastMotionKind` behavior.
- `getWanderVerticalMovementRatio()`
  - Executes `getWanderVerticalMovementRatio` behavior.
- `doMove(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull Vector3d translation, @Nonnull PositionProbeAir moveProbe, @Nullable ProbeMoveData probeMoveData, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `doMove` behavior.
- `executeMove(@Nonnull Ref<EntityStore> ref, @Nonnull Role role, double dt, @Nonnull Vector3d translation, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `executeMove` behavior.
- `constrainRotations(Role role, TransformComponent transform)`
  - Executes `constrainRotations` behavior.
- `getCurrentMaxBodyRotationSpeed()`
  - Executes `getCurrentMaxBodyRotationSpeed` behavior.
- `dampForceVelocity(@Nonnull Vector3d forceVelocity, double forceVelocityDamping, double interval, ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `dampForceVelocity` behavior.
- `shouldDampenAppliedVelocitiesY()`
  - Executes `shouldDampenAppliedVelocitiesY` behavior.
- `shouldAlwaysUseGroundResistance()`
  - Executes `shouldAlwaysUseGroundResistance` behavior.
- `spawned()`
  - Executes `spawned` behavior.
- `canAct(@Nonnull Ref<EntityStore> ref, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `canAct` behavior.
- `inAir()`
  - Executes `inAir` behavior.
- `onGround()`
  - Executes `onGround` behavior.
- `inWater()`
  - Executes `inWater` behavior.
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
- `is2D()`
  - Executes `is2D` behavior.
- `canRestAtPlace()`
  - Executes `canRestAtPlace` behavior.
- `getDesiredAltitudeWeight()`
  - Executes `getDesiredAltitudeWeight` behavior.
- `getHeightOverGround()`
  - Executes `getHeightOverGround` behavior.
- `isHorizontalIdle(double speed)`
  - Executes `isHorizontalIdle` behavior.
- `estimateVelocity(Steering steering, @Nonnull Vector3d velocityOut)`
  - Executes `estimateVelocity` behavior.
- `clearOverrides()`
  - Executes `clearOverrides` behavior.
- `setDesiredAltitudeOverride(double[] desiredAltitudeOverride)`
  - Executes `setDesiredAltitudeOverride` behavior.
- `takeOff(@Nonnull Ref<EntityStore> ref, double speed, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `takeOff` behavior.
- `getMinSpeedAfterForceSquared()`
  - Executes `getMinSpeedAfterForceSquared` behavior.
- `getDampingDeceleration()`
  - Executes `getDampingDeceleration` behavior.
- `computeMaxSpeedFromPitch(double pitch)`
  - Executes `computeMaxSpeedFromPitch` behavior.

## Notes
- No additional notes.
