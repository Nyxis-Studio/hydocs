# ProjectileComponent

## Overview
- Documentation for `ProjectileComponent`.
- Declared as a class in `com.hypixel.hytale.server.core.entity.entities`.

## Constructors
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

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `assembleDefaultProjectile(@Nonnull TimeResource time, @Nonnull String projectileAssetName, @Nonnull Vector3d position, @Nonnull Vector3f rotation)`
  - Executes `assembleDefaultProjectile` behavior.
- `initialize()`
  - Executes `initialize` behavior.
- `initializePhysics(@Nonnull BoundingBox boundingBox)`
  - Executes `initializePhysics` behavior.
- `onProjectileBounce(@Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onProjectileBounce` behavior.
- `onProjectileHitEvent(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onProjectileHitEvent` behavior.
- `consumeDeadTimer(float dt)`
  - Executes `consumeDeadTimer` behavior.
- `bounceHandler(@Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `bounceHandler` behavior.
- `impactHandler(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nullable Ref<EntityStore> targetRef, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `impactHandler` behavior.
- `onProjectileMissEvent(@Nonnull Vector3d position, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `onProjectileMissEvent` behavior.
- `onProjectileDeath(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3d position, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onProjectileDeath` behavior.
- `shoot(@Nonnull Holder<EntityStore> holder, @Nonnull UUID creatorUuid, double x, double y, double z, float yaw, float pitch)`
  - Executes `shoot` behavior.
- `computeStartOffset(boolean pitchAdjust, double verticalCenterShot, double horizontalCenterShot, double depthShot, float yaw, float pitch, @Nonnull Vector3d offset)`
  - Executes `computeStartOffset` behavior.
- `isOnGround()`
  - Executes `isOnGround` behavior.
- `getProjectile()`
  - Executes `getProjectile` behavior.
- `getAppearance()`
  - Executes `getAppearance` behavior.
- `getProjectileAssetName()`
  - Executes `getProjectileAssetName` behavior.
- `getSimplePhysicsProvider()`
  - Executes `getSimplePhysicsProvider` behavior.
- `applyBrokenPenalty(float penalty)`
  - Executes `applyBrokenPenalty` behavior.
- `clone()`
  - Executes `clone` behavior.

## Notes
- No additional notes.
