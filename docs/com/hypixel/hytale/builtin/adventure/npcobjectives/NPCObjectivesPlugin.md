**Source Hash:** `f2377a6b7c2d2ad3724037f7b54697a5fe8f36c59b7f8ff13c8b6bfda2f1f130`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# NPCObjectivesPlugin

## Overview
Plugin that registers NPC objective task types, tracking systems, and NPC builder components for objective interactions. Provides helpers to check and update NPC-related objective tasks.

## Field Descriptions
- `instance`: Singleton plugin instance.
- `killTrackerResourceType`: Resource type used to track kill tasks.

## Constructor Descriptions
- `NPCObjectivesPlugin(JavaPluginInit init)`: Creates the plugin instance.

## Method Descriptions
- `get()`: Returns the singleton instance.
- `setup()`: Registers objective task types, systems, NPC builder components, and asset load ordering.
- `hasTask(UUID playerUUID, UUID npcId, String taskId)`: Returns whether the player has the specified task entry.
- `updateTaskCompletion(Store<EntityStore> store, Ref<EntityStore> ref, PlayerRef playerRef, UUID npcId, String taskId)`: Updates task progress for a killed NPC and returns an optional animation ID.
- `startObjective(Ref<EntityStore> playerReference, String taskId, Store<EntityStore> store)`: Starts an objective for the player based on a task ID.
- `getKillTrackerResourceType()`: Returns the resource type for the kill tracker.

## Usage Notes
- Task update helpers integrate with `ObjectivePlugin` task tracking and kill task transactions.

## Examples
```java
NPCObjectivesPlugin plugin = NPCObjectivesPlugin.get();
```
