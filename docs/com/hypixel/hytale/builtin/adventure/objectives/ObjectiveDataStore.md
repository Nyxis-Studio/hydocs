**Source Hash:** `231f284685842426a0c4ac5fd26c304af8d61626da260c609d25f3c059372076`

# ObjectiveDataStore

## Overview

## Constructor Descriptions
- `ObjectiveDataStore(@Nonnull DataStore<Objective> dataStore)`
  - Creates a `ObjectiveDataStore` instance.

## Method Descriptions
- `getObjective(UUID objectiveUUID)`: Add description.
  - Executes `getObjective` behavior.
- `getEntityTasksForPlayer(UUID playerUUID)`: Add description.
  - Executes `getEntityTasksForPlayer` behavior.
- `getObjectiveCollection()`: Add description.
  - Executes `getObjectiveCollection` behavior.
- `getTaskRefsForType(Class<T> taskClass)`: Add description.
  - Executes `getTaskRefsForType` behavior.
- `addTaskRef(@Nonnull ObjectiveTaskRef<T> taskRef)`: Add description.
  - Executes `addTaskRef` behavior.
- `removeTaskRef(@Nullable ObjectiveTaskRef<T> taskRef)`: Add description.
  - Executes `removeTaskRef` behavior.
- `registerTaskRef(Class<T> taskClass)`: Add description.
  - Executes `registerTaskRef` behavior.
- `saveToDisk(String objectiveId, @Nonnull Objective objective)`: Add description.
  - Executes `saveToDisk` behavior.
- `saveToDiskAllObjectives()`: Add description.
  - Executes `saveToDiskAllObjectives` behavior.
- `removeFromDisk(String objectiveId)`: Add description.
  - Executes `removeFromDisk` behavior.
- `addObjective(UUID objectiveUUID, Objective objective)`: Add description.
  - Executes `addObjective` behavior.
- `removeObjective(UUID objectiveUUID)`: Add description.
  - Executes `removeObjective` behavior.
- `addEntityTaskForPlayer(UUID playerUUID, String taskId, UUID objectiveUUID)`: Add description.
  - Executes `addEntityTaskForPlayer` behavior.
- `removeEntityTask(UUID objectiveUUID, String taskId)`: Add description.
  - Executes `removeEntityTask` behavior.
- `removeEntityTaskForPlayer(UUID objectiveUUID, String taskId, UUID playerUUID)`: Add description.
  - Executes `removeEntityTaskForPlayer` behavior.
- `loadObjective(@Nonnull UUID objectiveUUID, @Nonnull Store<EntityStore> store)`: Add description.
  - Executes `loadObjective` behavior.
- `unloadObjective(UUID objectiveUUID)`: Add description.
  - Executes `unloadObjective` behavior.

## Notes
- No additional notes.
