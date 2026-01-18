# SimplePhysicsProvider

## Overview
- Documentation for `SimplePhysicsProvider`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.physics`.

## Constructors
- `SimplePhysicsProvider()`
  - Creates a `SimplePhysicsProvider` instance.
- `SimplePhysicsProvider(@Nonnull BiConsumer<Vector3d, ComponentAccessor<EntityStore>> bounceConsumer, @Nonnull QuadConsumer<Ref<EntityStore>, Vector3d, Ref<EntityStore>, ComponentAccessor<EntityStore>> impactConsumer)`
  - Creates a `SimplePhysicsProvider` instance.

## Methods
- `setImpacted(boolean impacted)`
  - Executes `setImpacted` behavior.
- `isImpacted()`
  - Executes `isImpacted` behavior.
- `setResting(boolean resting)`
  - Executes `setResting` behavior.
- `isResting()`
  - Executes `isResting` behavior.
- `onCollisionDamage(int blockX, int blockY, int blockZ, Vector3d direction, BlockContactData collisionData, BlockData blockData)`
  - Executes `onCollisionDamage` behavior.
- `onCollisionFinished()`
  - Executes `onCollisionFinished` behavior.
- `tick(double dt, @Nonnull Velocity entityVelocity, @Nonnull World entityWorld, @Nonnull TransformComponent entityTransform, Ref<EntityStore> selfRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `tick` behavior.
- `finishTick(@Nonnull TransformComponent position, @Nonnull Velocity velocity)`
  - Executes `finishTick` behavior.
- `rotateBody(double dt, @Nonnull Vector3f bodyRotation)`
  - Executes `rotateBody` behavior.
- `isOnGround()`
  - Executes `isOnGround` behavior.
- `isSwimming()`
  - Executes `isSwimming` behavior.
- `computeReflectedVector(@Nonnull Vector3d vec, @Nonnull Vector3d normal, @Nonnull Vector3d result)`
  - Executes `computeReflectedVector` behavior.
- `isProvidingCharacterCollisions()`
  - Executes `isProvidingCharacterCollisions` behavior.
- `setProvideCharacterCollisions(boolean provideCharacterCollisions)`
  - Executes `setProvideCharacterCollisions` behavior.
- `setGravity(double gravity, @Nonnull BoundingBox boundingBox)`
  - Executes `setGravity` behavior.
- `setBounciness(double bounciness)`
  - Executes `setBounciness` behavior.
- `setTerminalVelocities(double terminalVelocityAir, double terminalVelocityWater, @Nonnull BoundingBox boundingBox)`
  - Executes `setTerminalVelocities` behavior.
- `setTerminalVelocities(double terminalVelocity1, double density1, double terminalVelocity2, double density2, @Nonnull BoundingBox boundingBox)`
  - Executes `setTerminalVelocities` behavior.
- `setImpactSlowdown(double impactSlowdown)`
  - Executes `setImpactSlowdown` behavior.
- `setSticksVertically(boolean sticksVertically)`
  - Executes `setSticksVertically` behavior.
- `isComputeYaw()`
  - Executes `isComputeYaw` behavior.
- `setComputeYaw(boolean computeYaw)`
  - Executes `setComputeYaw` behavior.
- `isComputePitch()`
  - Executes `isComputePitch` behavior.
- `setComputePitch(boolean computePitch)`
  - Executes `setComputePitch` behavior.
- `setCreatorId(UUID creatorUuid)`
  - Executes `setCreatorId` behavior.
- `initialize(@Nullable Projectile projectile, @Nonnull BoundingBox boundingBox)`
  - Executes `initialize` behavior.
- `getVelocity()`
  - Executes `getVelocity` behavior.
- `addVelocity(float x, float y, float z)`
  - Executes `addVelocity` behavior.
- `setVelocity(@Nonnull Vector3d velocity)`
  - Executes `setVelocity` behavior.
- `setMoveOutOfSolid(boolean moveOutOfSolid)`
  - Executes `setMoveOutOfSolid` behavior.
- `setMoveOutOfSolid(double speed)`
  - Executes `setMoveOutOfSolid` behavior.
- `getDragCoefficient(double density)`
  - Executes `getDragCoefficient` behavior.
- `recomputeDragFactors(@Nonnull BoundingBox boundingBoxComponent)`
  - Executes `recomputeDragFactors` behavior.

## Notes
- No additional notes.
