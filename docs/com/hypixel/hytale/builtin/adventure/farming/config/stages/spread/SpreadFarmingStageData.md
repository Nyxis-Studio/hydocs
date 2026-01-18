**Source Hash:** `356963839fad7d3bc41c83bb41e3c37d65e912d4ac3c43f01c9d0871df04ae99`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# SpreadFarmingStageData

## Overview
Farming stage that executes one or more spread behaviors multiple times. Tracks execution limits and decay of spread rate for spawned blocks.

## Field Descriptions
- `CODEC`: Builder codec for spread stages.
- `executions`: Range of execution counts.
- `spreadDecayPercent`: Percent range used to decay spread rate for spawned blocks.
- `spreadGrowthBehaviours`: Array of spread behaviors to execute.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getExecutions()`: Returns the configured execution range.
- `getSpreadDecayPercent()`: Returns the configured decay percentage range.
- `getSpreadGrowthBehaviours()`: Returns the configured spread behavior array.
- `implementsShouldStop()`: Enables `shouldStop` checks for spread rate and execution limits.
- `shouldStop(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z)`: Stops when spread rate is zero or the randomized execution limit has been reached.
- `apply(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, FarmingStageData previousStage)`: Applies each spread behavior, decays the spread rate, and increments the execution counter for the stage.
- `remove(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z)`: No extra removal behavior for spread stages.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Decode-time validation enforces execution min >= 1 and decay min >= 0.

## Examples
```java
IntRange range = stage.getExecutions();
```
