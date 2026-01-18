**Source Hash:** `09bb67c502259dab2379b6bc828dd26f89687386f56fe14ae66c748c4b32853c`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# PrefabFarmingStageData

## Overview
Farming stage that spawns or replaces blocks using prefabs. Supports weighted prefab stages, replace masks, and particle effects.

## Field Descriptions
- `MIN_VOLUME_PREFAB`: Minimum prefab volume used for particle rate interpolation.
- `MAX_VOLUME_PREFAB`: Maximum prefab volume used for particle rate interpolation.
- `MIN_BROKEN_PARTICLE_RATE`: Minimum particle rate when replacing prefabs.
- `MAX_BROKEN_PARTICLE_RATE`: Maximum particle rate when replacing prefabs.
- `CODEC`: Builder codec for prefab stages.
- `prefabStages`: Weighted map of prefab choices.
- `replaceMaskTags`: Tag names allowed for replacement.
- `replaceMaskTagIndices`: Cached tag indices for replacements.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getPrefabStages()`: Returns the weighted prefab stage map.
- `apply(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, FarmingStageData previousStage)`: Places prefabs, replacing previous prefabs when intact and unobstructed.
- `remove(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z)`: Removes prefab blocks and spawns break particles based on prefab volume.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- `processConfig()` expands replace mask tags into tag indices for faster checks.
- Prefab replacement uses integrity checks to avoid overwriting damaged prefabs.

## Examples
```java
IWeightedMap<PrefabFarmingStageData.PrefabStage> stages = data.getPrefabStages();
```

---

# PrefabFarmingStageData.PrefabStage

## Overview
Weighted prefab entry with a path to the prefab asset. Resolves paths against asset packs and the prefab store.

## Field Descriptions
- `CODEC`: Builder codec for prefab stage entries.
- `EMPTY_ARRAY`: Empty prefab stage array for weighted map defaults.
- `weight`: Weight for random selection.
- `path`: Relative path to the prefab asset.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getWeight()`: Returns the stage weight.
- `getResolvedPath()`: Resolves the prefab path through asset packs or the prefab store.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Validates `weight` to be >= 1.

## Examples
```java
Path path = stage.getResolvedPath();
```
