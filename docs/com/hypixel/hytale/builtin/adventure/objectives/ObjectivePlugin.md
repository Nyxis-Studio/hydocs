**Source Hash:** `f540c4b7b0333d7a5044e4d6d4ec7ee047b3e86613688b6d0613a3e6e12d24e5`

# ObjectivePlugin

## Overview

## Constructor Descriptions
- `ObjectivePlugin(@Nonnull JavaPluginInit init)`
  - Creates a `ObjectivePlugin` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `getObjectiveHistoryComponentType()`: Add description.
  - Executes `getObjectiveHistoryComponentType` behavior.
- `getObjectiveLocationMarkerModel()`: Add description.
  - Executes `getObjectiveLocationMarkerModel` behavior.
- `getObjectiveDataStore()`: Add description.
  - Executes `getObjectiveDataStore` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `start()`: Add description.
  - Executes `start` behavior.
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.
- `getReachLocationMarkerComponentType()`: Add description.
  - Executes `getReachLocationMarkerComponentType` behavior.
- `getObjectiveLocationMarkerComponentType()`: Add description.
  - Executes `getObjectiveLocationMarkerComponentType` behavior.
- `registerTask(String id, Class<T> assetClass, Codec<T> assetCodec, Class<U> implementationClass, Codec<U> implementationCodec, TriFunction<T, Integer, Integer, U> generator)`: Add description.
  - Executes `registerTask` behavior.
- `registerCompletion(String id, Class<T> assetClass, Codec<T> codec, Function<T, U> generator)`: Add description.
  - Executes `registerCompletion` behavior.
- `createTask(@Nonnull ObjectiveTaskAsset task, int taskSetIndex, int taskIndex)`: Add description.
  - Executes `createTask` behavior.
- `createCompletion(@Nonnull ObjectiveCompletionAsset completionAsset)`: Add description.
  - Executes `createCompletion` behavior.
- `startObjective(@Nonnull String objectiveId, @Nonnull Set<UUID> playerUUIDs, @Nonnull UUID worldUUID, @Nullable UUID markerUUID, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `startObjective` behavior.
- `startObjective(@Nonnull String objectiveId, @Nullable UUID objectiveUUID, @Nonnull Set<UUID> playerUUIDs, @Nonnull UUID worldUUID, @Nullable UUID markerUUID, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `startObjective` behavior.
- `canPlayerDoObjective(@Nonnull Player player, @Nonnull String objectiveAssetId)`: Add description.
  - Executes `canPlayerDoObjective` behavior.
- `startObjectiveLine(@Nonnull Store<EntityStore> store, @Nonnull String objectiveLineId, @Nonnull Set<UUID> playerUUIDs, @Nonnull UUID worldUUID, @Nullable UUID markerUUID)`: Add description.
  - Executes `startObjectiveLine` behavior.
- `canPlayerDoObjectiveLine(@Nonnull Player player, @Nonnull String objectiveLineId)`: Add description.
  - Executes `canPlayerDoObjectiveLine` behavior.
- `objectiveCompleted(@Nonnull Objective objective, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `objectiveCompleted` behavior.
- `storeObjectiveHistoryData(@Nonnull Objective objective)`: Add description.
  - Executes `storeObjectiveHistoryData` behavior.
- `storeObjectiveLineHistoryData(@Nonnull ObjectiveLineHistoryData objectiveLineHistoryData, @Nonnull Set<UUID> playerUUIDs)`: Add description.
  - Executes `storeObjectiveLineHistoryData` behavior.
- `cancelObjective(@Nonnull UUID objectiveUUID, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `cancelObjective` behavior.
- `untrackObjectiveForPlayer(@Nonnull Objective objective, @Nonnull UUID playerUUID)`: Add description.
  - Executes `untrackObjectiveForPlayer` behavior.
- `addPlayerToExistingObjective(@Nonnull Store<EntityStore> store, @Nonnull UUID playerUUID, @Nonnull UUID objectiveUUID)`: Add description.
  - Executes `addPlayerToExistingObjective` behavior.
- `removePlayerFromExistingObjective(@Nonnull Store<EntityStore> store, @Nonnull UUID playerUUID, @Nonnull UUID objectiveUUID)`: Add description.
  - Executes `removePlayerFromExistingObjective` behavior.
- `onPlayerDisconnect(@Nonnull PlayerDisconnectEvent event)`: Add description.
  - Executes `onPlayerDisconnect` behavior.
- `onObjectiveLineAssetLoaded(@Nonnull LoadedAssetsEvent<String, ObjectiveLineAsset, DefaultAssetMap<String, ObjectiveLineAsset>> event)`: Add description.
  - Executes `onObjectiveLineAssetLoaded` behavior.
- `onObjectiveAssetLoaded(@Nonnull LoadedAssetsEvent<String, ObjectiveAsset, DefaultAssetMap<String, ObjectiveAsset>> event)`: Add description.
  - Executes `onObjectiveAssetLoaded` behavior.
- `onObjectiveLocationMarkerChange(@Nonnull LoadedAssetsEvent<String, ObjectiveLocationMarkerAsset, DefaultAssetMap<String, ObjectiveLocationMarkerAsset>> event)`: Add description.
  - Executes `onObjectiveLocationMarkerChange` behavior.
- `onModelAssetChange(@Nonnull LoadedAssetsEvent<String, ModelAsset, DefaultAssetMap<String, ModelAsset>> event)`: Add description.
  - Executes `onModelAssetChange` behavior.
- `onLivingEntityInventoryChange(@Nonnull LivingEntityInventoryChangeEvent event)`: Add description.
  - Executes `onLivingEntityInventoryChange` behavior.
- `onWorldAdded(AddWorldEvent event)`: Add description.
  - Executes `onWorldAdded` behavior.
- `getObjectiveDataDump()`: Add description.
  - Executes `getObjectiveDataDump` behavior.
- `getDataStoreProvider()`: Add description.
  - Executes `getDataStoreProvider` behavior.

## Notes
- No additional notes.
