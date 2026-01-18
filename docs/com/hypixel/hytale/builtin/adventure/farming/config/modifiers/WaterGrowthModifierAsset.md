**Source Hash:** `672a6d4b2246bada7c6abf9281f55c8c977b4080ba499ba330cdd1cc25c8c21f`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# WaterGrowthModifierAsset

## Overview
Growth modifier based on nearby fluids and weather conditions. Tracks water exposure, rainfall, and soil watering duration.

## Field Descriptions
- `CODEC`: Builder codec for water growth modifiers.
- `fluids`: Fluid id strings to treat as watering sources.
- `fluidIds`: Cached fluid indices for quick lookup.
- `weathers`: Weather id strings to treat as rain sources.
- `weatherIds`: Cached weather indices for quick lookup.
- `rainDuration`: Duration used when watering via rain.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getFluids()`: Returns fluid ids as strings.
- `getFluidIds()`: Returns cached fluid indices.
- `getWeathers()`: Returns weather ids as strings.
- `getWeatherIds()`: Returns cached weather indices.
- `getRainDuration()`: Returns the configured rain duration.
- `getCurrentGrowthMultiplier(CommandBuffer<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, boolean initialTick)`: Checks adjacent fluids and weather, updates soil external-water state, and returns the base growth multiplier when active.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Updates `TilledSoilBlock` external-water state based on detected water/rain and refreshes ticking when the state changes.

## Examples
```java
double multiplier = asset.getCurrentGrowthMultiplier(buffer, sectionRef, blockRef, x, y, z, false);
```
