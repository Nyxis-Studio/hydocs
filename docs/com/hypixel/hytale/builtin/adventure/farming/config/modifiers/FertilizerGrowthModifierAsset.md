# FertilizerGrowthModifierAsset

**Overview**
Growth modifier that boosts crops when the soil below is fertilized.
Delegates to the base growth multiplier only when fertilization is active.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getCurrentGrowthMultiplier(CommandBuffer<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, boolean initialTick)`: checks the soil below and returns the modifier multiplier.

**Notes**
- Requires a `TilledSoilBlock` with `isFertilized()`.
