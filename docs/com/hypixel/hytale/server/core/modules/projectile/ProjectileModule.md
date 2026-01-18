# ProjectileModule

## Overview
- Documentation for `ProjectileModule`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.projectile`.

## Constructors
- `ProjectileModule(@Nonnull JavaPluginInit init)`
  - Creates a `ProjectileModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `spawnProjectile(Ref<EntityStore> creatorRef, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull ProjectileConfig config, @Nonnull Vector3d position, @Nonnull Vector3d direction)`
  - Executes `spawnProjectile` behavior.
- `spawnProjectile(@Nullable UUID predictionId, Ref<EntityStore> creatorRef, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull ProjectileConfig config, @Nonnull Vector3d position, @Nonnull Vector3d direction)`
  - Executes `spawnProjectile` behavior.
- `onProjectileSpawnInteraction(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> creatorRef, @Nonnull Store<EntityStore> store)`
  - Executes `onProjectileSpawnInteraction` behavior.
- `getProjectileComponentType()`
  - Executes `getProjectileComponentType` behavior.
- `getStandardPhysicsProviderComponentType()`
  - Executes `getStandardPhysicsProviderComponentType` behavior.
- `getPredictedProjectileComponentType()`
  - Executes `getPredictedProjectileComponentType` behavior.

## Notes
- No additional notes.
