**Source Hash:** `f2c6ff013e9732ef04db7623f8b90e33399685e18864bdeeb79478a5aaf5b8ce`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# BlockTypeFarmingStageData

## Overview
Farming stage that replaces the block with a specific block type. Uses a block id reference and validates it against the asset registry.

## Field Descriptions
- `CODEC`: Builder codec for block type stages.
- `block`: Block id string to place.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getBlock()`: Returns the block id string.
- `apply(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, FarmingStageData previousStage)`: Applies the base stage and swaps the block to the configured type while preserving rotation.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Validates block ids using `BlockType.VALIDATOR_CACHE`.

## Examples
```java
String blockId = stage.getBlock();
```
