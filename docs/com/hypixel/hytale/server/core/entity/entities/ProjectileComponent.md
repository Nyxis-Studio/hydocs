**Source Hash:** `825beffe6c9968bc83814d5ceb433a96046949ca3f860d68b3d0a8df4979265a`

# ProjectileComponent

## Overview

## Constructor Descriptions
- `ProjectileComponent()`
  - Creates a `ProjectileComponent` instance.
- `ProjectileComponent(@Nonnull String projectileAssetName)`
  - Creates a `ProjectileComponent` instance.
- `ProjectileComponent(projectileAssetName)`
  - Creates a `ProjectileComponent` instance.
- `ProjectileComponent(@Nonnull ProjectileComponent other)`
  - Creates a `ProjectileComponent` instance.
- `ProjectileComponent(this)`
  - Creates a `ProjectileComponent` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `assembleDefaultProjectile(@Nonnull TimeResource time, @Nonnull String projectileAssetName, @Nonnull Vector3d position, @Nonnull Vector3f rotation)`: Add description.
  - Executes `assembleDefaultProjectile` behavior.
- `initialize()`: Add description.
  - Executes `initialize` behavior.
- `initializePhysics(@Nonnull BoundingBox boundingBox)`: Add description.
  - Executes `initializePhysics` behavior.
- `onProjectileBounce(@Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onProjectileBounce` behavior.
- `onProjectileHitEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onProjectileHitEvent` behavior.
- `consumeDeadTimer(float dt)`: Add description.
  - Executes `consumeDeadTimer` behavior.
- `bounceHandler(@Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `bounceHandler` behavior.
- `impactHandler(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nullable Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `impactHandler` behavior.
- `onProjectileMissEvent(@Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `onProjectileMissEvent` behavior.
- `onProjectileDeath(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onProjectileDeath` behavior.
- `shoot(@Nonnull Holder<EntityStore> holder, @Nonnull UUID creatorUuid, double x, double y, double z, float yaw, float pitch)`: Add description.
  - Executes `shoot` behavior.
- `computeStartOffset(boolean pitchAdjust, double verticalCenterShot, double horizontalCenterShot, double depthShot, float yaw, float pitch, @Nonnull Vector3d offset)`: Add description.
  - Executes `computeStartOffset` behavior.
- `isOnGround()`: Add description.
  - Executes `isOnGround` behavior.
- `getProjectile()`: Add description.
  - Executes `getProjectile` behavior.
- `getAppearance()`: Add description.
  - Executes `getAppearance` behavior.
- `getProjectileAssetName()`: Add description.
  - Executes `getProjectileAssetName` behavior.
- `getSimplePhysicsProvider()`: Add description.
  - Executes `getSimplePhysicsProvider` behavior.
- `applyBrokenPenalty(float penalty)`: Add description.
  - Executes `applyBrokenPenalty` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.

## Notes
- No additional notes.
