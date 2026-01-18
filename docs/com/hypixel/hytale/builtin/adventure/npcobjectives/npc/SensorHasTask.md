**Source Hash:** `d9fddd4e5b0d2f73f1a5f8455f5d7df91b4a78cde09e7386f587576991bcfb92`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# SensorHasTask

## Overview
NPC sensor that checks whether the current interaction target has any of the specified task IDs. Adds matching task IDs to the role's active task list for downstream actions.

## Field Descriptions
- `tasksById`: Task IDs to look for on the target player.

## Constructor Descriptions
- `SensorHasTask(BuilderSensorHasTask builder, BuilderSupport support)`: Creates the sensor with the configured task IDs.

## Method Descriptions
- `matches(Ref<EntityStore> ref, Role role, double dt, Store<EntityStore> store)`: Validates the target player and records matching tasks in entity support.
- `getSensorInfo()`: Returns no additional sensor info.

## Usage Notes
- The sensor skips dead targets and returns false when no tasks match.

## Examples
```java
SensorHasTask sensor = new SensorHasTask(builder, support);
```
