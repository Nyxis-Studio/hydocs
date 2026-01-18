**Source Hash:** `08464c64a888d69a7e00ebd03840bfe70d7c2a42d5922f9bdb4599abf5d696a4`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# FarmingBlockState

## Overview
Deprecated farming block component that stores crop stage timing, spread data, and growth modifiers. Retained for compatibility and does not clone its data, so consumers should treat instances as shared.

## Field Descriptions
- `CODEC`: Builder codec for legacy farming block state.
- `loaded`: Indicates whether legacy state has been loaded.
- `baseCrop`: Base crop asset identifier.
- `stageStart`: Time when the current stage began.
- `currentFarmingStageSetName`: Active stage set name.
- `currentFarmingStageIndex`: Index of the current stage.
- `stageCompletionTimes`: Completion times for each stage in the set.
- `stageSetAfterHarvest`: Stage set to use after harvesting.
- `lastGrowthMultiplier`: Last applied growth multiplier value.
- `spreadRate`: Spread multiplier for legacy growth logic.

## Constructor Descriptions
- `FarmingBlockState()`: Creates a legacy farming block state container.

## Method Descriptions
- `getCurrentFarmingStageSetName()`: Returns the active stage set name.
- `setCurrentFarmingStageSetName(String currentFarmingStageSetName)`: Updates the stage set name.
- `getCurrentFarmingStageIndex()`: Returns the current stage index.
- `setCurrentFarmingStageIndex(int currentFarmingStageIndex)`: Updates the current stage index.
- `getStageSetAfterHarvest()`: Returns the stage set used after harvest.
- `setStageSetAfterHarvest(String stageSetAfterHarvest)`: Updates the post-harvest stage set name.
- `getSpreadRate()`: Returns the spread rate multiplier.
- `setSpreadRate(float spreadRate)`: Updates the spread rate multiplier.
- `toString()`: Returns a debug string with current state values.
- `clone()`: Returns the same instance to preserve legacy behavior.

## Usage Notes
- This class is deprecated for removal; prefer `FarmingBlock` and `TilledSoilBlock` instead.
- `clone()` returns `this`, so callers should not mutate copies independently.

## Examples
```java
FarmingBlockState legacyState = new FarmingBlockState();
```
