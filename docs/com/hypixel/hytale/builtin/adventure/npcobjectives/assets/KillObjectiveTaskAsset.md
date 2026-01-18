**Source Hash:** `6c030c6f126e56c0dcf7d647766abaec689d7dd0f1c444fceaf0eb62f8973f2e`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# KillObjectiveTaskAsset

## Overview
Objective task asset that requires killing NPCs belonging to a configured NPC group.

## Field Descriptions
- `CODEC`: Builder codec for kill objective assets.
- `npcGroupId`: NPC group identifier to match against kills.

## Constructor Descriptions
- `KillObjectiveTaskAsset(String descriptionId, TaskConditionAsset[] taskConditions, Vector3i[] mapMarkers, int count, String npcGroupId)`: Creates a kill objective asset with a target group and count.
- `KillObjectiveTaskAsset()`: Creates an empty asset instance for codec use.

## Method Descriptions
- `getTaskScope()`: Returns `PLAYER_AND_MARKER` scope for kill objectives.
- `getNpcGroupId()`: Returns the NPC group ID.
- `matchesAsset0(ObjectiveTaskAsset task)`: Matches another kill asset by group ID.
- `toString()`: Returns a debug string with group ID and inherited data.

## Examples
```java
KillObjectiveTaskAsset asset = new KillObjectiveTaskAsset();
```
