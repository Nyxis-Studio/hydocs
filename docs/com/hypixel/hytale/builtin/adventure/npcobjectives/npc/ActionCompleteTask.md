**Source Hash:** `59c24a5d0f473b577c5463f9aeb467a45a2d42c97db1184e738912d31d6456f1`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# ActionCompleteTask

## Overview
NPC action that completes active objective tasks for the currently iterated player target. Optionally plays the task completion animation when the task reports an animation ID.

## Field Descriptions
- `playAnimation`: Whether to play the completion animation when available.

## Constructor Descriptions
- `ActionCompleteTask(BuilderActionCompleteTask builder, BuilderSupport support)`: Creates the action and resolves the play animation flag.

## Method Descriptions
- `canExecute(Ref<EntityStore> ref, Role role, InfoProvider sensorInfo, double dt, Store<EntityStore> store)`: Ensures the action can run and the target is valid and alive.
- `execute(Ref<EntityStore> ref, Role role, InfoProvider sensorInfo, double dt, Store<EntityStore> store)`: Completes active tasks for the target player and optionally plays the resulting animation.

## Usage Notes
- Active task IDs are collected by the role's entity support during sensor evaluation.

## Examples
```java
ActionCompleteTask action = new ActionCompleteTask(builder, support);
```
