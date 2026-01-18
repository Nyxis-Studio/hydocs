**Source Hash:** `acc831d77a2d310d32d07ff9a0dd69785584f5442679b10a2b8fd1bb68986350`

# ObjectiveLocationMarkerSystems

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `getDependencies()`: Add description.
  - Executes `getDependencies` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`: Add description.
  - Executes `isParallel` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `tick` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `setupMarker(@Nonnull Store<EntityStore> store, @Nonnull ObjectiveLocationMarker entity, @Nonnull Ref<EntityStore> entityReference, @Nonnull Vector3d position, @Nonnull UUID uuid, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `setupMarker` behavior.
- `updateIncomingPlayers(@Nonnull PlayerRef[] playersInArea, int playersInAreaSize, @Nonnull ObjectiveLocationMarker entity, @Nonnull Set<UUID> playerUUIDs, @Nonnull Set<UUID> activePlayerUUIDs, @Nonnull String objectiveId)`: Add description.
  - Executes `updateIncomingPlayers` behavior.
- `updateOutgoingPlayers(@Nonnull Set<UUID> playersInArea, @Nonnull ObjectiveLocationMarker entity, @Nullable Set<UUID> activePlayerUUIDs, @Nonnull String objectiveId)`: Add description.
  - Executes `updateOutgoingPlayers` behavior.
- `isPlayerInSpecificEnvironment(@Nonnull ObjectiveLocationMarker entity, @Nonnull WeatherTracker weatherTracker, @Nonnull TransformComponent transform, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `isPlayerInSpecificEnvironment` behavior.
- `untrackEntityObjectiveForPlayer(@Nonnull ObjectiveLocationMarker entity, @Nonnull UUID playerUUID)`: Add description.
  - Executes `untrackEntityObjectiveForPlayer` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `onEntityRemoved` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
