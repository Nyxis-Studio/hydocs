# ObjectivePlugin

## Overview
- Documentation for `ObjectivePlugin`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.objectives`.

## Constructors
- `ObjectivePlugin(@Nonnull JavaPluginInit init)`
  - Creates a `ObjectivePlugin` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `getObjectiveHistoryComponentType()`
  - Executes `getObjectiveHistoryComponentType` behavior.
- `getObjectiveLocationMarkerModel()`
  - Executes `getObjectiveLocationMarkerModel` behavior.
- `getObjectiveDataStore()`
  - Executes `getObjectiveDataStore` behavior.
- `setup()`
  - Executes `setup` behavior.
- `start()`
  - Executes `start` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `getReachLocationMarkerComponentType()`
  - Executes `getReachLocationMarkerComponentType` behavior.
- `getObjectiveLocationMarkerComponentType()`
  - Executes `getObjectiveLocationMarkerComponentType` behavior.
- `registerTask(String id, Class<T> assetClass, Codec<T> assetCodec, Class<U> implementationClass, Codec<U> implementationCodec, TriFunction<T, Integer, Integer, U> generator)`
  - Executes `registerTask` behavior.
- `registerCompletion(String id, Class<T> assetClass, Codec<T> codec, Function<T, U> generator)`
  - Executes `registerCompletion` behavior.
- `createTask(@Nonnull ObjectiveTaskAsset task, int taskSetIndex, int taskIndex)`
  - Executes `createTask` behavior.
- `createCompletion(@Nonnull ObjectiveCompletionAsset completionAsset)`
  - Executes `createCompletion` behavior.
- `startObjective(@Nonnull String objectiveId, @Nonnull Set<UUID> playerUUIDs, @Nonnull UUID worldUUID, @Nullable UUID markerUUID, @Nonnull Store<EntityStore> store)`
  - Executes `startObjective` behavior.
- `startObjective(@Nonnull String objectiveId, @Nullable UUID objectiveUUID, @Nonnull Set<UUID> playerUUIDs, @Nonnull UUID worldUUID, @Nullable UUID markerUUID, @Nonnull Store<EntityStore> store)`
  - Executes `startObjective` behavior.
- `canPlayerDoObjective(@Nonnull Player player, @Nonnull String objectiveAssetId)`
  - Executes `canPlayerDoObjective` behavior.
- `startObjectiveLine(@Nonnull Store<EntityStore> store, @Nonnull String objectiveLineId, @Nonnull Set<UUID> playerUUIDs, @Nonnull UUID worldUUID, @Nullable UUID markerUUID)`
  - Executes `startObjectiveLine` behavior.
- `canPlayerDoObjectiveLine(@Nonnull Player player, @Nonnull String objectiveLineId)`
  - Executes `canPlayerDoObjectiveLine` behavior.
- `objectiveCompleted(@Nonnull Objective objective, @Nonnull Store<EntityStore> store)`
  - Executes `objectiveCompleted` behavior.
- `storeObjectiveHistoryData(@Nonnull Objective objective)`
  - Executes `storeObjectiveHistoryData` behavior.
- `storeObjectiveLineHistoryData(@Nonnull ObjectiveLineHistoryData objectiveLineHistoryData, @Nonnull Set<UUID> playerUUIDs)`
  - Executes `storeObjectiveLineHistoryData` behavior.
- `cancelObjective(@Nonnull UUID objectiveUUID, @Nonnull Store<EntityStore> store)`
  - Executes `cancelObjective` behavior.
- `untrackObjectiveForPlayer(@Nonnull Objective objective, @Nonnull UUID playerUUID)`
  - Executes `untrackObjectiveForPlayer` behavior.
- `addPlayerToExistingObjective(@Nonnull Store<EntityStore> store, @Nonnull UUID playerUUID, @Nonnull UUID objectiveUUID)`
  - Executes `addPlayerToExistingObjective` behavior.
- `removePlayerFromExistingObjective(@Nonnull Store<EntityStore> store, @Nonnull UUID playerUUID, @Nonnull UUID objectiveUUID)`
  - Executes `removePlayerFromExistingObjective` behavior.
- `onPlayerDisconnect(@Nonnull PlayerDisconnectEvent event)`
  - Executes `onPlayerDisconnect` behavior.
- `onObjectiveLineAssetLoaded(@Nonnull LoadedAssetsEvent<String, ObjectiveLineAsset, DefaultAssetMap<String, ObjectiveLineAsset>> event)`
  - Executes `onObjectiveLineAssetLoaded` behavior.
- `onObjectiveAssetLoaded(@Nonnull LoadedAssetsEvent<String, ObjectiveAsset, DefaultAssetMap<String, ObjectiveAsset>> event)`
  - Executes `onObjectiveAssetLoaded` behavior.
- `onObjectiveLocationMarkerChange(@Nonnull LoadedAssetsEvent<String, ObjectiveLocationMarkerAsset, DefaultAssetMap<String, ObjectiveLocationMarkerAsset>> event)`
  - Executes `onObjectiveLocationMarkerChange` behavior.
- `onModelAssetChange(@Nonnull LoadedAssetsEvent<String, ModelAsset, DefaultAssetMap<String, ModelAsset>> event)`
  - Executes `onModelAssetChange` behavior.
- `onLivingEntityInventoryChange(@Nonnull LivingEntityInventoryChangeEvent event)`
  - Executes `onLivingEntityInventoryChange` behavior.
- `onWorldAdded(AddWorldEvent event)`
  - Executes `onWorldAdded` behavior.
- `getObjectiveDataDump()`
  - Executes `getObjectiveDataDump` behavior.
- `getDataStoreProvider()`
  - Executes `getDataStoreProvider` behavior.

## Notes
- No additional notes.
