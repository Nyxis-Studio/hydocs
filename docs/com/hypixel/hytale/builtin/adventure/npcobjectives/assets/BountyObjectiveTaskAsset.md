**Source Hash:** `cbb2f13af76ab09fbaf21b676048904b84746ab08522f13f960864351631260e`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# BountyObjectiveTaskAsset

## Overview
Objective task asset that spawns a specific NPC bounty target at a location determined by a world location provider.

## Field Descriptions
- `CODEC`: Builder codec for bounty task assets.
- `npcId`: NPC ID to spawn as the bounty target.
- `worldLocationProvider`: Location provider used to choose a spawn position.

## Constructor Descriptions
- `BountyObjectiveTaskAsset(String descriptionId, TaskConditionAsset[] taskConditions, Vector3i[] mapMarkers, String npcId, WorldLocationProvider worldLocationProvider)`: Creates a bounty task asset with target NPC and location rules.
- `BountyObjectiveTaskAsset()`: Creates an empty asset instance for codec use.

## Method Descriptions
- `getTaskScope()`: Returns `PLAYER` scope for bounty tasks.
- `getNpcId()`: Returns the NPC ID for the bounty target.
- `getWorldLocationProvider()`: Returns the world location provider.
- `matchesAsset0(ObjectiveTaskAsset task)`: Matches another bounty asset by NPC ID and location provider.
- `toString()`: Returns a debug string with bounty task data.

## Examples
```java
BountyObjectiveTaskAsset asset = new BountyObjectiveTaskAsset();
```
