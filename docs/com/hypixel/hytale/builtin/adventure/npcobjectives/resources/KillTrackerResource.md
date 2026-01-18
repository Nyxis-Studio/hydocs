**Source Hash:** `61eea23c0ff5dab1ebaa8d74daea880062103b05e68df43a1ad68f1ea4d84f8f`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# KillTrackerResource

## Overview
Resource that tracks active kill task transactions. Used by kill tracking systems to notify objective tasks when NPCs die.

## Field Descriptions
- `killTasks`: Active kill task transactions being monitored.

## Constructor Descriptions
- `KillTrackerResource()`: Creates an empty kill task tracker.

## Method Descriptions
- `getResourceType()`: Returns the resource type registered by `NPCObjectivesPlugin`.
- `watch(KillTaskTransaction task)`: Adds a kill task to the tracker.
- `unwatch(KillTaskTransaction task)`: Removes a kill task from the tracker.
- `getKillTasks()`: Returns the current list of kill tasks.
- `clone()`: Creates a new empty resource instance.

## Examples
```java
KillTrackerResource resource = store.getResource(KillTrackerResource.getResourceType());
```
