**Source Hash:** `633462f60d530ed2008a1081358d194f2b2328b7746a74bc09c6bef84e55f0fc`
**Last Updated:** 2026-01-18T19:03:47-03:00

# TaskSet

## Overview
Configuration class that groups multiple objective tasks together with a description for organized objective management. TaskSets allow objectives to be broken down into logical groups of related tasks, making complex objectives more manageable and providing better player guidance.

## Field Descriptions
- `CODEC`: BuilderCodec for serializing and deserializing TaskSet instances. Validates that task arrays are non-empty and handles description ID serialization.
- `TASKSET_DESCRIPTION_KEY`: String template "server.objectives.{0}.taskSet.{1}" used to generate default localization keys when no custom description ID is provided.
- `descriptionId`: Optional string identifier for custom task set descriptions. When null, a default description key is generated based on objective and task set index.
- `tasks`: Array of ObjectiveTaskAsset instances that define the individual tasks within this set. Must be non-empty according to codec validation.

## Constructor Descriptions
- `TaskSet(String descriptionId, ObjectiveTaskAsset[] tasks)`: Creates a new task set with specified description ID and task array. Used when programmatically creating task sets with custom descriptions.
- `TaskSet()`: Protected default constructor for codec deserialization. Should not be used directly in application code.

## Method Descriptions
- `getDescriptionId()`: Returns the custom description ID if set, or null if using default generated descriptions.
- `getDescriptionKey(String objectiveId, int taskSetIndex)`: Returns the localization key for this task set's description. Uses custom description ID if available, otherwise generates a default key using the template format.
- `getTasks()`: Returns the array of ObjectiveTaskAsset instances that comprise this task set. All tasks in the set must be completed for the set to be considered complete.
- `toString()`: Returns a string representation including description ID and task array for debugging purposes.

## Usage Notes
- Task sets provide logical grouping for complex objectives with multiple steps
- All tasks within a set typically need to be completed before moving to the next set
- Description IDs should use consistent naming conventions for localization
- Task arrays cannot be empty - each set must contain at least one task
- Task sets can be used to create sequential or parallel task completion flows

## Examples
```java
// Create a task set with custom description
ObjectiveTaskAsset[] tasks = {
    new GatherObjectiveTaskAsset("minecraft:iron_ore", 10),
    new CraftObjectiveTaskAsset("minecraft:iron_ingot", 5)
};
TaskSet miningTasks = new TaskSet("mining_tutorial.iron_tasks", tasks);

// Get localization key
String key = miningTasks.getDescriptionKey("mining_tutorial", 0);
// Returns: "mining_tutorial.iron_tasks" or "server.objectives.mining_tutorial.taskSet.0"
```
