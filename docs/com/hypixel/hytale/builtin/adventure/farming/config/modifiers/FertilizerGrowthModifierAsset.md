**Source Hash:** `f3908f30037ce92a05b8e25fb7615ba4a7cb67fd43bf765483fe851ee8aa4538`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# FertilizerGrowthModifierAsset

## Overview
Growth modifier that boosts crops when the soil below is fertilized. Delegates to the base growth multiplier only when fertilization is active.

## Field Descriptions
- `CODEC`: Builder codec for fertilizer growth modifiers.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getCurrentGrowthMultiplier(CommandBuffer<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, boolean initialTick)`: Checks for fertilized soil below and returns the base growth multiplier when active; otherwise returns 1.

## Usage Notes
- Requires a `TilledSoilBlock` with `isFertilized()` to be present beneath the crop.

## Examples
```java
double multiplier = asset.getCurrentGrowthMultiplier(buffer, sectionRef, blockRef, x, y, z, false);
```
