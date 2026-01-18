# NPCObjectivesPlugin

## Overview
- Documentation for `NPCObjectivesPlugin`.
- Declared as a class in `com.hypixel.hytale.builtin.adventure.npcobjectives`.

## Constructors
- `NPCObjectivesPlugin(@Nonnull JavaPluginInit init)`
  - Creates a `NPCObjectivesPlugin` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `hasTask(@Nonnull UUID playerUUID, @Nonnull UUID npcId, @Nonnull String taskId)`
  - Executes `hasTask` behavior.
- `updateTaskCompletion(@Nonnull Store<EntityStore> store, @Nonnull Ref<EntityStore> ref, @Nonnull PlayerRef playerRef, @Nonnull UUID npcId, @Nonnull String taskId)`
  - Executes `updateTaskCompletion` behavior.
- `startObjective(@Nonnull Ref<EntityStore> playerReference, @Nonnull String taskId, @Nonnull Store<EntityStore> store)`
  - Executes `startObjective` behavior.
- `getKillTrackerResourceType()`
  - Executes `getKillTrackerResourceType` behavior.

## Notes
- No additional notes.
