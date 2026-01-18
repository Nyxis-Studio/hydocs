**Source Hash:** `6b345931c4edc26ff804f81184172a7188fd4fb78fa0b1a8363e3a0322b4ff82`
**Last Updated:** `2026-01-18T18:19:14-03:00`

# FarmingBlock

## Overview
Chunk component that tracks growth progress and state for a farmed block. Stores the active stage set, growth progress, generation metadata, and spread settings used by farming systems.

## Field Descriptions
- `DEFAULT_STAGE_SET`: Default stage set identifier used when none is provided.
- `CODEC`: Builder codec for serializing farming block state.
- `currentStageSet`: Current farming stage set identifier.
- `growthProgress`: Accumulated growth progress for the current stage.
- `lastTickGameTime`: Timestamp of the last growth tick.
- `generation`: Generation counter used for spread and regrowth logic.
- `previousBlockType`: Original block type before farming changes.
- `spreadRate`: Multiplier used when spreading stages to adjacent blocks.
- `executions`: Number of times growth logic has executed.

## Constructor Descriptions
- `FarmingBlock()`: Creates a farming block with default stage set and zero progress.
- `FarmingBlock(String currentStageSet, float growthProgress, Instant lastTickGameTime, int generation, String previousBlockType, float spreadRate, int executions)`: Creates a farming block with explicit state values.

## Method Descriptions
- `getComponentType()`: Returns the chunk component type for farming blocks.
- `getCurrentStageSet()`: Returns the current stage set identifier.
- `setCurrentStageSet(String currentStageSet)`: Sets the stage set identifier, falling back to the default when null.
- `getGrowthProgress()`: Returns the growth progress value.
- `setGrowthProgress(float growthProgress)`: Updates the growth progress value.
- `getLastTickGameTime()`: Returns the last tick timestamp.
- `setLastTickGameTime(Instant lastTickGameTime)`: Updates the last tick timestamp.
- `getGeneration()`: Returns the generation counter.
- `setGeneration(int generation)`: Updates the generation counter.
- `getPreviousBlockType()`: Returns the previous block type identifier.
- `setPreviousBlockType(String previousBlockType)`: Updates the previous block type identifier.
- `getSpreadRate()`: Returns the spread rate multiplier.
- `setSpreadRate(float spreadRate)`: Updates the spread rate multiplier.
- `getExecutions()`: Returns the execution count.
- `setExecutions(int executions)`: Updates the execution count.
- `clone()`: Clones the farming block state.
- `toString()`: Returns a debug string with the current state values.

## Usage Notes
- Growth systems should update `lastTickGameTime` and `growthProgress` together to maintain consistency.

## Examples
```java
FarmingBlock farmingBlock = new FarmingBlock();
```
