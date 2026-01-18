# DeployableAoeConfig

## Overview
- Documentation for `DeployableAoeConfig`.
- Declared as a class in `com.hypixel.hytale.builtin.deployables.config`.

## Constructors
- `DeployableAoeConfig()`
  - Creates a `DeployableAoeConfig` instance.

## Methods
- `tick(@Nonnull DeployableComponent deployableComponent, float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `handleDetection(final Store<EntityStore> store, final CommandBuffer<EntityStore> commandBuffer, final Ref<EntityStore> deployableRef, DeployableComponent deployableComponent, Vector3d position, float radius, final DamageCause damageCause)`
  - Executes `handleDetection` behavior.
- `accept(Ref<EntityStore> entityStoreRef)`
  - Executes `accept` behavior.
- `handleDebugGraphics(World world, Vector3f color, Vector3d position, float scale)`
  - Executes `handleDebugGraphics` behavior.
- `attackTarget(Ref<EntityStore> targetRef, Ref<EntityStore> ownerRef, DamageCause damageCause, CommandBuffer<EntityStore> commandBuffer)`
  - Executes `attackTarget` behavior.
- `applyEffectToTarget(Store<EntityStore> store, Ref<EntityStore> targetRef)`
  - Executes `applyEffectToTarget` behavior.
- `canAttackEntity(Ref<EntityStore> target, DeployableComponent deployable)`
  - Executes `canAttackEntity` behavior.
- `getRadius(Store<EntityStore> store, Instant startInstant)`
  - Executes `getRadius` behavior.
- `getDamageCause()`
  - Executes `getDamageCause` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
