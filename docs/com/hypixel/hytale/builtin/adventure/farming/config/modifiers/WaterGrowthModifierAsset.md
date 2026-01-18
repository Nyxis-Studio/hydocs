# WaterGrowthModifierAsset

**Overview**
Growth modifier based on nearby fluids and weather conditions.
Tracks water exposure, rainfall, and soil watering duration.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getFluids()`: returns fluid ids as strings.
- `getFluidIds()`: returns cached fluid indices.
- `getWeathers()`: returns weather ids as strings.
- `getWeatherIds()`: returns cached weather indices.
- `getRainDuration()`: returns the configured rain duration.
- `getCurrentGrowthMultiplier(CommandBuffer<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, boolean initialTick)`: checks water/rain and updates soil state.
- `toString()`: returns a diagnostic string.

**Notes**
- Updates `TilledSoilBlock` external-water state based on detection.
