**Source Hash:** `ebeff5b8f923082db3c11c3b248fefcf82f01aa02d02ab88e6ec6eca738e4248`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# KillSpawnMarkerObjectiveTaskAsset

## Overview
Kill objective asset that triggers spawn markers within a radius around the objective when the task starts.

## Field Descriptions
- `CODEC`: Builder codec for spawn marker kill assets.
- `spawnMarkerIds`: Spawn marker IDs that may be triggered.
- `radius`: Search radius around the objective for spawn markers.

## Constructor Descriptions
- `KillSpawnMarkerObjectiveTaskAsset(String descriptionId, TaskConditionAsset[] taskConditions, Vector3i[] mapMarkers, int count, String npcGroupId, String[] spawnMarkerIds, float radius)`: Creates the asset with marker IDs and radius.
- `KillSpawnMarkerObjectiveTaskAsset()`: Creates an empty asset instance for codec use.

## Method Descriptions
- `getSpawnMarkerIds()`: Returns the spawn marker IDs.
- `getRadius()`: Returns the search radius.
- `matchesAsset0(ObjectiveTaskAsset task)`: Matches another asset by marker IDs and radius.
- `toString()`: Returns a debug string with marker data.

## Examples
```java
KillSpawnMarkerObjectiveTaskAsset asset = new KillSpawnMarkerObjectiveTaskAsset();
```
