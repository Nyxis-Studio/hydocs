# DeployableTrapConfig

## Overview
- Documentation for `DeployableTrapConfig`.
- Declared as a class in `com.hypixel.hytale.builtin.deployables.config`.

## Constructors
- `DeployableTrapConfig()`
  - Creates a `DeployableTrapConfig` instance.

## Methods
- `tick(@Nonnull DeployableComponent deployableComponent, float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `handleDetection(final Store<EntityStore> store, final CommandBuffer<EntityStore> commandBuffer, final Ref<EntityStore> deployableRef, final DeployableComponent deployableComponent, Vector3d position, float radius, final DamageCause damageCause)`
  - Executes `handleDetection` behavior.
- `accept(Ref<EntityStore> entityStoreRef)`
  - Executes `accept` behavior.
- `isLive(@Nonnull Store<EntityStore> store, @Nonnull DeployableComponent comp)`
  - Executes `isLive` behavior.
- `onTriggered(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref)`
  - Executes `onTriggered` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
