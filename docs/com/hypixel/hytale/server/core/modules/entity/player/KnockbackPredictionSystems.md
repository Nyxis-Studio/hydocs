# KnockbackPredictionSystems

## Overview
- Documentation for `KnockbackPredictionSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.player`.

## Constructors
- None.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `convertWishMovement(@Nonnull KnockbackSimulation simulation, @Nonnull MovementStates movementStates, @Nonnull MovementSettings movementSettings)`
  - Executes `convertWishMovement` behavior.
- `computeMoveForce(@Nonnull KnockbackSimulation simulation, @Nonnull MovementStates movementStates, @Nonnull MovementSettings movementSettings)`
  - Executes `computeMoveForce` behavior.
- `convertToNewRange(float value, float oldMinRange, float oldMaxRange, float newMinRange, float newMaxRange)`
  - Executes `convertToNewRange` behavior.
- `applyMovementOffset(@Nonnull World world, @Nonnull Box hitBox, @Nonnull KnockbackSimulation simulation, @Nonnull MovementStates movementStates, @Nonnull Vector3d movementOffset)`
  - Executes `applyMovementOffset` behavior.
- `doMoveCycle(@Nonnull World world, @Nonnull Box hitBox, @Nonnull KnockbackSimulation simulation, @Nonnull MovementStates movementStates, @Nonnull Vector3d offset)`
  - Executes `doMoveCycle` behavior.
- `checkCollision(@Nonnull KnockbackSimulation simulation, @Nonnull World world, @Nonnull Box hitBox, @Nonnull Vector3d position, Vector3d moveOffset, CollisionAxis axis, @Nonnull CollisionResult result)`
  - Executes `checkCollision` behavior.
- `componentType()`
  - Executes `componentType` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull KnockbackSimulation component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, KnockbackSimulation oldComponent, @Nonnull KnockbackSimulation newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull KnockbackSimulation knockbackSimulationComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `onComponentAdded(@Nonnull Ref<EntityStore> ref, @Nonnull Teleport component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentAdded` behavior.
- `onComponentSet(@Nonnull Ref<EntityStore> ref, Teleport oldComponent, @Nonnull Teleport newComponent, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentSet` behavior.
- `onComponentRemoved(@Nonnull Ref<EntityStore> ref, @Nonnull Teleport component, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onComponentRemoved` behavior.

## Notes
- No additional notes.
