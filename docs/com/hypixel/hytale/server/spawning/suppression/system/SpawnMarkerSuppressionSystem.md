# SpawnMarkerSuppressionSystem

## Overview
- Documentation for `SpawnMarkerSuppressionSystem`.
- Declared as a class in `com.hypixel.hytale.server.spawning.suppression.system`.

## Constructors
- `SpawnMarkerSuppressionSystem(ComponentType<EntityStore, SpawnMarkerEntity> spawnMarkerEntityComponentType, ResourceType<EntityStore, SpawnSuppressionController> spawnSuppressionControllerResourceType)`
  - Creates a `SpawnMarkerSuppressionSystem` instance.

## Methods
- `onEntityAdded(@Nonnull Ref<EntityStore> reference, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> reference, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.

## Notes
- No additional notes.
