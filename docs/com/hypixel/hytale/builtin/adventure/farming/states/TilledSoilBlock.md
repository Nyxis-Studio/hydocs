**Source Hash:** `7c25d183886d7493bb031e7b4f5bf5d0d7c885ae707fb38cb424adf2fefc9044`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# TilledSoilBlock

## Overview
Chunk component that stores watering, fertilization, and decay information for tilled soil. Computes which block state variant to use based on watering and fertilization conditions.

## Field Descriptions
- `VERSION`: Codec version for serialized data.
- `CODEC`: Builder codec for tilled soil state.
- `planted`: Whether a crop is currently planted on the soil.
- `fertilized`: Whether fertilizer has been applied.
- `externalWater`: Whether external water is providing hydration.
- `wateredUntil`: Timestamp until which the soil remains watered.
- `decayTime`: Timestamp when soil should revert or decay.

## Constructor Descriptions
- `TilledSoilBlock()`: Creates a default tilled soil state.
- `TilledSoilBlock(boolean planted, boolean fertilized, boolean externalWater, Instant wateredUntil, Instant decayTime)`: Creates a tilled soil state with explicit flags and timestamps.

## Method Descriptions
- `getComponentType()`: Returns the chunk component type for tilled soil blocks.
- `isPlanted()`: Returns whether a crop is planted.
- `setPlanted(boolean planted)`: Updates the planted flag.
- `setWateredUntil(Instant wateredUntil)`: Updates the watering expiration time.
- `getWateredUntil()`: Returns the watering expiration time.
- `isFertilized()`: Returns whether the soil is fertilized.
- `setFertilized(boolean fertilized)`: Updates the fertilized flag.
- `hasExternalWater()`: Returns whether external water is providing hydration.
- `setExternalWater(boolean externalWater)`: Updates the external water flag.
- `getDecayTime()`: Returns the decay timestamp.
- `setDecayTime(Instant decayTime)`: Updates the decay timestamp.
- `computeBlockType(Instant gameTime, BlockType type)`: Returns the block state key for the current water and fertilizer conditions.
- `toString()`: Returns a debug string with the current soil state.
- `clone()`: Clones the soil state.

## Usage Notes
- `computeBlockType` selects from `Fertilized_Watered`, `Fertilized`, `Watered`, or `default` block states.

## Examples
```java
TilledSoilBlock soil = new TilledSoilBlock();
```
