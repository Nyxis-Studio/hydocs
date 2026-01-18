**Source Hash:** `272970e82b114002b649f5df7175f97a75c68134e0d6018e5a3beb8b39d65e46`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# KillSpawnBeaconObjectiveTaskAsset

## Overview
Kill objective asset that spawns one or more spawn beacons as part of the task setup.

## Field Descriptions
- `CODEC`: Builder codec for spawn beacon kill assets.
- `spawnBeacons`: Configured spawn beacons to place for the task.

## Constructor Descriptions
- `KillSpawnBeaconObjectiveTaskAsset(String descriptionId, TaskConditionAsset[] taskConditions, Vector3i[] mapMarkers, int count, String npcGroupId, ObjectiveSpawnBeacon[] spawnBeacons)`: Creates the asset with spawn beacon definitions.
- `KillSpawnBeaconObjectiveTaskAsset()`: Creates an empty asset instance for codec use.

## Method Descriptions
- `getSpawnBeacons()`: Returns the configured spawn beacons.
- `matchesAsset0(ObjectiveTaskAsset task)`: Matches another asset by spawn beacon configuration.
- `toString()`: Returns a debug string with spawn beacon data.

## Usage Notes
- Spawn beacon definitions can include offsets and optional world location providers.

## Examples
```java
KillSpawnBeaconObjectiveTaskAsset asset = new KillSpawnBeaconObjectiveTaskAsset();
```

---

# KillSpawnBeaconObjectiveTaskAsset.ObjectiveSpawnBeacon

## Overview
Spawn beacon definition used by kill objectives, including the beacon ID, offset, and optional location rule.

## Field Descriptions
- `CODEC`: Builder codec for objective spawn beacons.
- `spawnBeaconId`: Spawn beacon asset ID.
- `offset`: Optional positional offset from the objective position.
- `worldLocationProvider`: Optional location provider to adjust the spawn position.

## Constructor Descriptions
- `ObjectiveSpawnBeacon()`: Creates an empty spawn beacon definition.

## Method Descriptions
- `getSpawnBeaconId()`: Returns the spawn beacon ID.
- `getOffset()`: Returns the offset vector.
- `getWorldLocationProvider()`: Returns the location provider.
- `equals(Object o)`: Compares beacon definitions by ID, offset, and location provider.
- `hashCode()`: Hashes the beacon definition fields.
- `toString()`: Returns a debug string with beacon data.

## Examples
```java
KillSpawnBeaconObjectiveTaskAsset.ObjectiveSpawnBeacon beacon = new KillSpawnBeaconObjectiveTaskAsset.ObjectiveSpawnBeacon();
```
