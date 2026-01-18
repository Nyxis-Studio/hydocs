# DeployableTurretConfig

## Overview
- Documentation for `DeployableTurretConfig`.
- Declared as a class in `com.hypixel.hytale.builtin.deployables.config`.

## Constructors
- None.

## Methods
- `processConfig()`
  - Executes `processConfig` behavior.
- `tick(@Nonnull DeployableComponent deployableComponent, float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `tickInitState(@Nonnull Ref<EntityStore> entityRef, @Nonnull DeployableComponent component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tickInitState` behavior.
- `tickStartDeployState(@Nonnull Ref<EntityStore> ref, @Nonnull DeployableComponent component, @Nonnull Store<EntityStore> store)`
  - Executes `tickStartDeployState` behavior.
- `tickAwaitDeployState(@Nonnull Ref<EntityStore> ref, @Nonnull DeployableComponent component, @Nonnull Store<EntityStore> store)`
  - Executes `tickAwaitDeployState` behavior.
- `tickAttackState(@Nonnull Ref<EntityStore> ref, @Nonnull DeployableComponent component, float dt, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tickAttackState` behavior.
- `calculatedTargetPosition(@Nonnull Vector3d original)`
  - Executes `calculatedTargetPosition` behavior.
- `isValidTarget(@Nonnull Ref<EntityStore> ref, @Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> targetRef)`
  - Executes `isValidTarget` behavior.
- `testLineOfSight(@Nonnull Vector3d attackerPos, @Nonnull Vector3d targetPos, @Nonnull Vector3d direction, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `testLineOfSight` behavior.
- `updateProjectiles(@Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull DeployableProjectileShooterComponent shooterComponent)`
  - Executes `updateProjectiles` behavior.
- `updateProjectile(@Nonnull Ref<EntityStore> projectileRef, @Nonnull DeployableProjectileShooterComponent shooterComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `updateProjectile` behavior.
- `projectileHit(@Nonnull Ref<EntityStore> ref, @Nonnull Ref<EntityStore> projectileRef, @Nonnull DeployableProjectileShooterComponent shooterComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `projectileHit` behavior.
- `applyKnockback(@Nonnull Ref<EntityStore> targetRef, @Nonnull Vector3d attackerPos, float attackerYaw, @Nonnull Store<EntityStore> store)`
  - Executes `applyKnockback` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
