**Source Hash:** `801ff620aa9679c9397a014ed3ddc36c6a61adcd7d1ac92666f8f03fecd9134d`

# DeployableTurretConfig

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `processConfig()`: Add description.
  - Executes `processConfig` behavior.
- `tick(@Nonnull DeployableComponent deployableComponent, float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `tickInitState(@Nonnull Ref<EntityStore> entityRef, @Nonnull DeployableComponent component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tickInitState` behavior.
- `tickStartDeployState(@Nonnull Ref<EntityStore> ref, @Nonnull DeployableComponent component, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `tickStartDeployState` behavior.
- `tickAwaitDeployState(@Nonnull Ref<EntityStore> ref, @Nonnull DeployableComponent component, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `tickAwaitDeployState` behavior.
- `tickAttackState(@Nonnull Ref<EntityStore> ref, @Nonnull DeployableComponent component, float dt, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tickAttackState` behavior.
- `calculatedTargetPosition(@Nonnull Vector3d original)`: Add description.
  - Executes `calculatedTargetPosition` behavior.
- `isValidTarget(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> targetRef)`: Add description.
  - Executes `isValidTarget` behavior.
- `testLineOfSight(@Nonnull Vector3d attackerPos, @Nonnull Vector3d targetPos, @Nonnull Vector3d direction, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `testLineOfSight` behavior.
- `updateProjectiles(@Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull DeployableProjectileShooterComponent shooterComponent)`: Add description.
  - Executes `updateProjectiles` behavior.
- `updateProjectile(@Nonnull Ref<EntityStore> projectileRef, @Nonnull DeployableProjectileShooterComponent shooterComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `updateProjectile` behavior.
- `projectileHit(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> projectileRef, @Nonnull DeployableProjectileShooterComponent shooterComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `projectileHit` behavior.
- `applyKnockback(@Nonnull Ref<EntityStore> targetRef, @Nonnull Vector3d attackerPos, float attackerYaw, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `applyKnockback` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.

## Notes
- No additional notes.
