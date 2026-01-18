**Source Hash:** `05de2c9c6acc0986210c60d8d341f1f122052c80b76a35fe32079ece5ecec624`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# ActionStartObjective

## Overview
NPC action that starts a configured objective for the player currently targeted in an interaction.

## Field Descriptions
- `objectiveId`: Objective ID to start when the action executes.

## Constructor Descriptions
- `ActionStartObjective(BuilderActionStartObjective builder, BuilderSupport support)`: Resolves the objective ID from the builder configuration.

## Method Descriptions
- `canExecute(Ref<EntityStore> ref, Role role, InfoProvider sensorInfo, double dt, Store<EntityStore> store)`: Requires a valid interaction target to execute.
- `execute(Ref<EntityStore> ref, Role role, InfoProvider sensorInfo, double dt, Store<EntityStore> store)`: Starts the configured objective for the target player.

## Examples
```java
ActionStartObjective action = new ActionStartObjective(builder, support);
```
