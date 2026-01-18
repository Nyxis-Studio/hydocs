**Source Hash:** `f751dda83ac3e27b46b8ed44eb81444a30d5f47b88e5a6eb2213620b80ab3d68`
**Last Updated:** 2026-01-18T18:54:44-03:00

# Objective

## Overview

Core class representing a game objective with multiple task sets that players can complete. Manages objective lifecycle, task progression, participant tracking, and completion rewards. Supports dynamic asset reloading and network synchronization with clients.

## Constructor Descriptions
- `Objective(@Nonnull ObjectiveAsset asset, @Nullable UUID objectiveUUID, @Nonnull Set<UUID> playerUUIDs, @Nonnull UUID worldUUID, @Nullable UUID markerUUID)`
  - Creates an `Objective` instance from an asset configuration.
  - Generates a random UUID if objectiveUUID is null.
  - Initializes task set index to 0 and creates objective history data.
- `Objective()`
  - Protected default constructor for codec deserialization.

## Field Descriptions
- `objectiveUUID`: Unique identifier for this objective instance.
- `objectiveId`: Asset ID referencing the objective configuration.
- `objectiveLineHistoryData`: Optional objective line data.
- `objectiveHistoryData`: History tracking for this objective.
- `playerUUIDs`: All players participating in this objective.
- `activePlayerUUIDs`: Currently active/online participants (thread-safe).
- `currentTasks`: Tasks for the current task set.
- `currentTaskSetIndex`: Index of the currently active task set.
- `completed`: Whether this objective has been completed.
- `worldUUID`: The world where this objective exists.
- `markerUUID`: Optional marker entity for objective positioning.
- `dirty`: Whether the objective state has changed and needs synchronization.
- `objectiveItemStarter`: Item that started this objective.

## Method Descriptions
- `getObjectiveUUID()`: Returns the unique identifier for this objective.
- `getObjectiveId()`: Returns the asset ID for this objective.
- `getObjectiveAsset()`: Retrieves the asset configuration from the asset map.
- `getObjectiveLineHistoryData()`: Returns the objective line history data if present.
- `setObjectiveLineHistoryData(@Nullable ObjectiveLineHistoryData objectiveLineHistoryData)`: Sets the objective line history data.
- `getObjectiveHistoryData()`: Returns the objective's history tracking data.
- `getObjectiveLineAsset()`: Retrieves the objective line asset if history data exists.
- `getPlayerUUIDs()`: Returns all participating player UUIDs.
- `getActivePlayerUUIDs()`: Returns currently active player UUIDs (thread-safe set).
- `getCurrentTasks()`: Returns the current task set array.
- `getCurrentTaskSetIndex()`: Returns the index of the currently active task set.
- `getCurrentDescription()`: Gets the description for the current task set or falls back to objective description.
- `isCompleted()`: Returns whether this objective has been completed.
- `getWorldUUID()`: Returns the world UUID where this objective exists.
- `getMarkerUUID()`: Returns the optional marker entity UUID.
- `isDirty()`: Returns whether the objective needs synchronization.
- `getObjectiveItemStarter()`: Returns the item that initiated this objective.
- `setObjectiveItemStarter(@Nonnull ItemStack objectiveItemStarter)`: Sets the objective starter item.
- `setup(@Nonnull Store<EntityStore> componentAccessor)`: Initializes the objective and creates tasks for the current task set.
  - Returns false if task set index exceeds available task sets or task setup fails.
- `setupCurrentTasks(@Nonnull Store<EntityStore> store)`: Sets up all tasks in the current task set.
  - Reverts all task transactions if any task setup fails.
- `checkTaskSetCompletion(@Nonnull Store<EntityStore> store)`: Checks if all current tasks are complete.
  - Triggers task set completion if all tasks are finished.
- `taskSetComplete(@Nonnull Store<EntityStore> store)`: Handles task set completion.
  - Advances to next task set or completes the objective if all sets are finished.
  - Sends progress updates to participants.
- `complete(@Nonnull Store<EntityStore> store)`: Completes the objective.
  - Sends completion messages to participants and executes completion handlers.
- `cancel()`: Cancels the objective by reverting all current task transactions.
- `unload()`: Unloads the objective by cleaning up all task transaction records.
- `getTaskInfoMessage()`: Builds a message containing current task information.
- `reloadObjectiveAsset(@Nonnull Map<String, ObjectiveAsset> reloadedAssets)`: Handles dynamic asset reloading.
  - Updates tasks when assets change and synchronizes with clients.
- `checkPossibleAssetReload(@Nonnull Map<String, ObjectiveAsset> reloadedAssets)`: Validates if asset reload is possible.
  - Returns task assets for current set or null if reload should be cancelled.
- `setupAndUpdateTasks(@Nonnull ObjectiveTaskAsset[] taskAssets, @Nonnull Store<EntityStore> store)`: Sets up new tasks during reload.
  - Matches existing tasks to new assets when possible to preserve progress.
- `findMatchingObjectiveTask(@Nonnull ObjectiveTaskAsset taskAsset)`: Finds existing task matching the given asset.
- `cancelReload(@Nonnull ObjectiveTask[] newTasks)`: Cancels a failed reload attempt.
- `revertRemovedTasks(@Nonnull ObjectiveTask[] newTasks)`: Reverts tasks that were removed during reload.
- `forEachParticipant(@Nonnull Consumer<Ref<EntityStore>> consumer)`: Executes action for each participating player.
- `forEachParticipant(@Nonnull BiConsumer<Ref<EntityStore>, T> consumer, T meta)`: Executes action for each participant with metadata.
- `forEachParticipant(@Nonnull TriConsumer<Ref<EntityStore>, T, U> consumer, @Nonnull T t, @Nonnull U u)`: Executes action for each participant with two metadata parameters.
- `getPosition(@Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Gets objective position from marker or first participant.
- `addActivePlayerUUID(UUID playerUUID)`: Adds a player to the active participants set.
- `removeActivePlayerUUID(UUID playerUUID)`: Removes a player from the active participants set.
- `markDirty()`: Marks the objective as needing synchronization.
- `consumeDirty()`: Returns and clears the dirty flag atomically.
- `toString()`: Returns detailed string representation of the objective state.

## Notes
- Implements `NetworkSerializable` for client-server synchronization.
- Uses a complex codec for serialization with multiple keyed fields.
- Supports dynamic asset reloading while preserving task progress.
- Thread-safe active player tracking with `ConcurrentHashMap.newKeySet()`.
- Tasks are organized into sequential sets that must be completed in order.
- Completion handlers can execute custom logic when objectives finish.
- Position tracking uses marker entities or participant locations for world positioning.
