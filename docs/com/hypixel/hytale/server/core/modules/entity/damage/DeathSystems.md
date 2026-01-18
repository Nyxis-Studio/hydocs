# DeathSystems

## Overview
- Documentation for `DeathSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.damage`.

## Constructors
- None.

## Methods
- `playDeathAnimation(@Nonnull Ref<EntityStore> ref, @Nonnull DeathComponent deathComponent, @Nullable ModelComponent modelComponent, @Nonnull MovementStatesComponent movementStatesComponent, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `playDeathAnimation` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull DeathComponent component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, DeathComponent oldComponent, @Nonnull DeathComponent newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull DeathComponent component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.

## Notes
- No additional notes.
