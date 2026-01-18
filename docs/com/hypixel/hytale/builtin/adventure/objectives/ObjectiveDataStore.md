# ObjectiveDataStore

## Overview
- Documentation for `ObjectiveDataStore`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.objectives`.

## Constructors
- `ObjectiveDataStore(@Nonnull DataStore<Objective> dataStore)`
  - Creates a `ObjectiveDataStore` instance.

## Methods
- `getObjective(UUID objectiveUUID)`
  - Executes `getObjective` behavior.
- `getEntityTasksForPlayer(UUID playerUUID)`
  - Executes `getEntityTasksForPlayer` behavior.
- `getObjectiveCollection()`
  - Executes `getObjectiveCollection` behavior.
- `getTaskRefsForType(Class<T> taskClass)`
  - Executes `getTaskRefsForType` behavior.
- `addTaskRef(@Nonnull ObjectiveTaskRef<T> taskRef)`
  - Executes `addTaskRef` behavior.
- `removeTaskRef(@Nullable ObjectiveTaskRef<T> taskRef)`
  - Executes `removeTaskRef` behavior.
- `registerTaskRef(Class<T> taskClass)`
  - Executes `registerTaskRef` behavior.
- `saveToDisk(String objectiveId, @Nonnull Objective objective)`
  - Executes `saveToDisk` behavior.
- `saveToDiskAllObjectives()`
  - Executes `saveToDiskAllObjectives` behavior.
- `removeFromDisk(String objectiveId)`
  - Executes `removeFromDisk` behavior.
- `addObjective(UUID objectiveUUID, Objective objective)`
  - Executes `addObjective` behavior.
- `removeObjective(UUID objectiveUUID)`
  - Executes `removeObjective` behavior.
- `addEntityTaskForPlayer(UUID playerUUID, String taskId, UUID objectiveUUID)`
  - Executes `addEntityTaskForPlayer` behavior.
- `removeEntityTask(UUID objectiveUUID, String taskId)`
  - Executes `removeEntityTask` behavior.
- `removeEntityTaskForPlayer(UUID objectiveUUID, String taskId, UUID playerUUID)`
  - Executes `removeEntityTaskForPlayer` behavior.
- `loadObjective(@Nonnull UUID objectiveUUID, @Nonnull Store<EntityStore> store)`
  - Executes `loadObjective` behavior.
- `unloadObjective(UUID objectiveUUID)`
  - Executes `unloadObjective` behavior.

## Notes
- No additional notes.
