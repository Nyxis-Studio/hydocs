**Source Hash:** `af743eb98b47b0c3d08c1fd9599344c16e26c306d26cd98f159a70f6a15a558a`

# SimplePhysicsProvider

## Overview

## Constructor Descriptions
- `SimplePhysicsProvider()`
  - Creates a `SimplePhysicsProvider` instance.
- `SimplePhysicsProvider(@Nonnull BiConsumer<Vector3d, ComponentAccessor<EntityStore>> bounceConsumer, @Nonnull QuadConsumer<Ref<EntityStore>, Vector3d, Ref<EntityStore>, ComponentAccessor<EntityStore>> impactConsumer)`
  - Creates a `SimplePhysicsProvider` instance.

## Method Descriptions
- `setImpacted(boolean impacted)`: Add description.
  - Executes `setImpacted` behavior.
- `isImpacted()`: Add description.
  - Executes `isImpacted` behavior.
- `setResting(boolean resting)`: Add description.
  - Executes `setResting` behavior.
- `isResting()`: Add description.
  - Executes `isResting` behavior.
- `onCollisionDamage(int blockX, int blockY, int blockZ, Vector3d direction, BlockContactData collisionData, BlockData blockData)`: Add description.
  - Executes `onCollisionDamage` behavior.
- `onCollisionFinished()`: Add description.
  - Executes `onCollisionFinished` behavior.
- `tick(double dt, @Nonnull Velocity entityVelocity, @Nonnull World entityWorld, @Nonnull TransformComponent entityTransform, Ref<EntityStore> selfRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `tick` behavior.
- `finishTick(@Nonnull TransformComponent position, @Nonnull Velocity velocity)`: Add description.
  - Executes `finishTick` behavior.
- `rotateBody(double dt, @Nonnull Vector3f bodyRotation)`: Add description.
  - Executes `rotateBody` behavior.
- `isOnGround()`: Add description.
  - Executes `isOnGround` behavior.
- `isSwimming()`: Add description.
  - Executes `isSwimming` behavior.
- `computeReflectedVector(@Nonnull Vector3d vec, @Nonnull Vector3d normal, @Nonnull Vector3d result)`: Add description.
  - Executes `computeReflectedVector` behavior.
- `isProvidingCharacterCollisions()`: Add description.
  - Executes `isProvidingCharacterCollisions` behavior.
- `setProvideCharacterCollisions(boolean provideCharacterCollisions)`: Add description.
  - Executes `setProvideCharacterCollisions` behavior.
- `setGravity(double gravity, @Nonnull BoundingBox boundingBox)`: Add description.
  - Executes `setGravity` behavior.
- `setBounciness(double bounciness)`: Add description.
  - Executes `setBounciness` behavior.
- `setTerminalVelocities(double terminalVelocityAir, double terminalVelocityWater, @Nonnull BoundingBox boundingBox)`: Add description.
  - Executes `setTerminalVelocities` behavior.
- `setTerminalVelocities(double terminalVelocity1, double density1, double terminalVelocity2, double density2, @Nonnull BoundingBox boundingBox)`: Add description.
  - Executes `setTerminalVelocities` behavior.
- `setImpactSlowdown(double impactSlowdown)`: Add description.
  - Executes `setImpactSlowdown` behavior.
- `setSticksVertically(boolean sticksVertically)`: Add description.
  - Executes `setSticksVertically` behavior.
- `isComputeYaw()`: Add description.
  - Executes `isComputeYaw` behavior.
- `setComputeYaw(boolean computeYaw)`: Add description.
  - Executes `setComputeYaw` behavior.
- `isComputePitch()`: Add description.
  - Executes `isComputePitch` behavior.
- `setComputePitch(boolean computePitch)`: Add description.
  - Executes `setComputePitch` behavior.
- `setCreatorId(UUID creatorUuid)`: Add description.
  - Executes `setCreatorId` behavior.
- `initialize(@Nullable Projectile projectile, @Nonnull BoundingBox boundingBox)`: Add description.
  - Executes `initialize` behavior.
- `getVelocity()`: Add description.
  - Executes `getVelocity` behavior.
- `addVelocity(float x, float y, float z)`: Add description.
  - Executes `addVelocity` behavior.
- `setVelocity(@Nonnull Vector3d velocity)`: Add description.
  - Executes `setVelocity` behavior.
- `setMoveOutOfSolid(boolean moveOutOfSolid)`: Add description.
  - Executes `setMoveOutOfSolid` behavior.
- `setMoveOutOfSolid(double speed)`: Add description.
  - Executes `setMoveOutOfSolid` behavior.
- `getDragCoefficient(double density)`: Add description.
  - Executes `getDragCoefficient` behavior.
- `recomputeDragFactors(@Nonnull BoundingBox boundingBoxComponent)`: Add description.
  - Executes `recomputeDragFactors` behavior.

## Notes
- No additional notes.
