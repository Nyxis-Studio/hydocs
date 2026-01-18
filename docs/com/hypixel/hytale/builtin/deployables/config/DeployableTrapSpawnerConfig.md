# DeployableTrapSpawnerConfig

## Overview
- Documentation for `DeployableTrapSpawnerConfig`.
- Declared as a class in `com.hypixel.hytale.builtin.deployables.config`.

## Constructors
- None.

## Methods
- `tick(@Nonnull DeployableComponent deployableComponent, float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `tickDeploymentState(@Nonnull Store<EntityStore> store, @Nonnull DeployableComponent component, @Nonnull Ref<EntityStore> entityRef)`
  - Executes `tickDeploymentState` behavior.
- `tickDeployAnimationState(Store<EntityStore> store, DeployableComponent component, Ref<EntityStore> entityRef)`
  - Executes `tickDeployAnimationState` behavior.
- `tickFuzeState(@Nonnull Store<EntityStore> store, @Nonnull DeployableComponent component)`
  - Executes `tickFuzeState` behavior.
- `tickLiveState(@Nonnull Store<EntityStore> store, @Nonnull DeployableComponent component, @Nonnull Ref<EntityStore> entityRef, CommandBuffer<EntityStore> commandBuffer, float dt)`
  - Executes `tickLiveState` behavior.
- `tickTriggeredState(CommandBuffer<EntityStore> commandBuffer, @Nonnull Store<EntityStore> store, @Nonnull DeployableComponent component, @Nonnull Ref<EntityStore> entityRef)`
  - Executes `tickTriggeredState` behavior.
- `tickDespawnState(@Nonnull DeployableComponent component, @Nonnull Ref<EntityStore> entityRef, @Nonnull Store<EntityStore> store)`
  - Executes `tickDespawnState` behavior.
- `onTriggered(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref)`
  - Executes `onTriggered` behavior.

## Notes
- No additional notes.
