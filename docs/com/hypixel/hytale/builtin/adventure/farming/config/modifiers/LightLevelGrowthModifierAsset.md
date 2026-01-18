**Source Hash:** `4881fba0e5f99f8bd0709c637a5acec0e77878e7cf4c55cbc082cfa5254b6b63`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# LightLevelGrowthModifierAsset

## Overview
Growth modifier driven by artificial light and sunlight ranges. Supports checking RGB light channels, sunlight factor, and optional dual requirement.

## Field Descriptions
- `CODEC`: Builder codec for light level modifiers.
- `artificialLight`: Artificial light ranges per color channel.
- `sunlight`: Sunlight range scaled by the world sunlight factor.
- `requireBoth`: Whether artificial and sunlight must both match.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getArtificialLight()`: Returns artificial light configuration.
- `getSunlight()`: Returns sunlight range.
- `isRequireBoth()`: Returns whether both light sources must match.
- `getCurrentGrowthMultiplier(CommandBuffer<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, boolean initialTick)`: Checks artificial/sunlight conditions and returns the base growth multiplier when active, applying a 0.6x factor for initial sunlight-only ticks.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- When only sunlight is present on an initial tick, growth is reduced to 60%.

## Examples
```java
double multiplier = asset.getCurrentGrowthMultiplier(buffer, sectionRef, blockRef, x, y, z, true);
```

---

# LightLevelGrowthModifierAsset.ArtificialLight

## Overview
Defines the acceptable RGB ranges for artificial light.

## Field Descriptions
- `CODEC`: Builder codec for artificial light ranges.
- `red`: Red channel range.
- `green`: Green channel range.
- `blue`: Blue channel range.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getRed()`: Returns the red channel range.
- `getGreen()`: Returns the green channel range.
- `getBlue()`: Returns the blue channel range.
- `toString()`: Returns a diagnostic string.

## Examples
```java
LightLevelGrowthModifierAsset.ArtificialLight light = asset.getArtificialLight();
```
