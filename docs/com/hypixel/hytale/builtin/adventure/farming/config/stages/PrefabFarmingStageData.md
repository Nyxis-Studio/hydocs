# PrefabFarmingStageData

**Overview**
Farming stage that spawns or replaces blocks using prefabs.
Supports weighted prefab stages, replace masks, and particle effects.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getPrefabStages()`: returns the weighted prefab stage map.
- `apply(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, FarmingStageData previousStage)`: places or transitions prefab blocks.
- `remove(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z)`: removes prefab blocks with particles.
- `toString()`: returns a diagnostic string.

**Notes**
- `processConfig()` expands replace mask tags into tag indices.
- Uses cached prefab buffers for placement and integrity checks.

---

# PrefabFarmingStageData.PrefabStage

**Overview**
Weighted prefab entry with a path to the prefab asset.
Resolves paths against asset packs and prefab store.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getWeight()`: returns the stage weight.
- `getResolvedPath()`: resolves the prefab path via asset packs or prefab store.
- `toString()`: returns a diagnostic string.

**Notes**
- Validates `weight` to be >= 1.
