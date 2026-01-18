# LightLevelGrowthModifierAsset

**Overview**
Growth modifier driven by artificial light and sunlight ranges.
Supports checking RGB light channels, sunlight factor, and optional dual requirement.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getArtificialLight()`: returns artificial light configuration.
- `getSunlight()`: returns sunlight range.
- `isRequireBoth()`: returns whether both light sources must match.
- `getCurrentGrowthMultiplier(CommandBuffer<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, boolean initialTick)`: computes whether light conditions apply.
- `toString()`: returns a diagnostic string.

**Notes**
- `ArtificialLight` encapsulates RGB ranges for the light test.

---

# LightLevelGrowthModifierAsset.ArtificialLight

**Overview**
Defines the acceptable RGB ranges for artificial light.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getRed()`: returns the red channel range.
- `getGreen()`: returns the green channel range.
- `getBlue()`: returns the blue channel range.
- `toString()`: returns a diagnostic string.
