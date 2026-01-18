# DeployablesSystem

## Overview
- Documentation for `DeployablesSystem`.
- Declared as a class in `com.hypixel.hytale.builtin.deployables.system`.

## Constructors
- None.

## Methods
- `spawnParticleEffect(Ref<EntityStore> sourceRef, CommandBuffer<EntityStore> commandBuffer, Vector3d position, ModelParticle particle)`
  - Executes `spawnParticleEffect` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int index, ArchetypeChunk<EntityStore> archetypeChunk, Store<EntityStore> store, CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `deregisterOwner(@Nonnull Ref<EntityStore> ref, @Nonnull DeployableComponent deployableComponent, @Nonnull DeployableConfig deployableConfig)`
  - Executes `deregisterOwner` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
