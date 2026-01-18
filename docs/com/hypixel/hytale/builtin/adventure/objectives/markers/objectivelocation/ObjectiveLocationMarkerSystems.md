# ObjectiveLocationMarkerSystems

## Overview
- Documentation for `ObjectiveLocationMarkerSystems`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.objectives.markers.objectivelocation`.

## Constructors
- None.

## Methods
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<EntityStore> store)`
  - Executes `tick` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `setupMarker(@Nonnull Store<EntityStore> store, @Nonnull ObjectiveLocationMarker entity, @Nonnull Ref<EntityStore> entityReference, @Nonnull Vector3d position, @Nonnull UUID uuid, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `setupMarker` behavior.
- `updateIncomingPlayers(@Nonnull PlayerRef[] playersInArea, int playersInAreaSize, @Nonnull ObjectiveLocationMarker entity, @Nonnull Set<UUID> playerUUIDs, @Nonnull Set<UUID> activePlayerUUIDs, @Nonnull String objectiveId)`
  - Executes `updateIncomingPlayers` behavior.
- `updateOutgoingPlayers(@Nonnull Set<UUID> playersInArea, @Nonnull ObjectiveLocationMarker entity, @Nullable Set<UUID> activePlayerUUIDs, @Nonnull String objectiveId)`
  - Executes `updateOutgoingPlayers` behavior.
- `isPlayerInSpecificEnvironment(@Nonnull ObjectiveLocationMarker entity, @Nonnull WeatherTracker weatherTracker, @Nonnull TransformComponent transform, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `isPlayerInSpecificEnvironment` behavior.
- `untrackEntityObjectiveForPlayer(@Nonnull ObjectiveLocationMarker entity, @Nonnull UUID playerUUID)`
  - Executes `untrackEntityObjectiveForPlayer` behavior.
- `onEntityAdd(@Nonnull Holder<EntityStore> holder, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<EntityStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store)`
  - Executes `onEntityRemoved` behavior.
- `onEntityAdded(@Nonnull Ref<EntityStore> ref, @Nonnull AddReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<EntityStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
