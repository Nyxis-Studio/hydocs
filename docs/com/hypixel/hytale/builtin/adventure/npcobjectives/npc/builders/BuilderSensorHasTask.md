**Source Hash:** `0360058fb9013e8ee13a3ae2cac1d4b5b81a41f86e0f7bd84a14a5f634bc5a90`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# BuilderSensorHasTask

## Overview
Builder for the `SensorHasTask` NPC sensor. Configures which task IDs to check on the target player.

## Field Descriptions
- `tasksById`: String array holder for task IDs.

## Constructor Descriptions
- `BuilderSensorHasTask()`: Creates the sensor builder.

## Method Descriptions
- `getShortDescription()`: Returns the sensor description for tooling.
- `getLongDescription()`: Returns the same description as the short description.
- `build(BuilderSupport builderSupport)`: Creates a `SensorHasTask` instance.
- `getBuilderDescriptorState()`: Returns the stable descriptor state.
- `readConfig(JsonElement data)`: Reads task IDs and validates instruction type.
- `getTasksById(BuilderSupport support)`: Returns the configured task IDs.

## Examples
```java
BuilderSensorHasTask builder = new BuilderSensorHasTask();
```
