# TreasureMapObjectiveTask

## Overview
- Documentation for `TreasureMapObjectiveTask`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.objectives.task`.

## Constructors
- `TreasureMapObjectiveTask(@Nonnull TreasureMapObjectiveTaskAsset asset, int taskSetIndex, int taskIndex)`
  - Creates a `TreasureMapObjectiveTask` instance.
- `TreasureMapObjectiveTask()`
  - Creates a `TreasureMapObjectiveTask` instance.

## Methods
- `getAsset()`
  - Executes `getAsset` behavior.
- `getChestMarkerIDFromUUID(@Nonnull UUID uuid)`
  - Executes `getChestMarkerIDFromUUID` behavior.
- `setup0(@Nonnull Objective objective, @Nonnull World world, @Nonnull Store<EntityStore> store)`
  - Executes `setup0` behavior.
- `checkCompletion()`
  - Executes `checkCompletion` behavior.
- `onTreasureChestOpeningEvent(@Nonnull Objective objective, @Nonnull TreasureChestOpeningEvent event)`
  - Executes `onTreasureChestOpeningEvent` behavior.
- `spawnChest(@Nonnull Objective objective, @Nonnull World world, @Nonnull TreasureMapObjectiveTaskAsset.ChestConfig chestConfig, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `spawnChest` behavior.
- `spawnChestBlock(@Nonnull World world, @Nonnull Vector3i conditionPosition, String chestBlockTypeKey, @Nonnull SpawnTreasureChestTransactionRecord transactionRecord)`
  - Executes `spawnChestBlock` behavior.
- `calculateChestSpawnPosition(@Nonnull TreasureMapObjectiveTaskAsset.ChestConfig chestConfig, @Nonnull Objective objective, @Nonnull World world, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `calculateChestSpawnPosition` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
