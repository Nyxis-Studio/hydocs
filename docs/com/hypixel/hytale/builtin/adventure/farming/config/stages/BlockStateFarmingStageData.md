**Source Hash:** `83b67f1d1097c9f54138233db7aaa684ad50e531ed38db5f93e30f4d72c9ff22`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# BlockStateFarmingStageData

## Overview
Farming stage that swaps a block to a new state variant. Uses a block state id to resolve the target block type.

## Field Descriptions
- `CODEC`: Builder codec for block state stages.
- `state`: Block state identifier to apply.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `getState()`: Returns the target state string.
- `apply(ComponentAccessor<ChunkStore> commandBuffer, Ref<ChunkStore> sectionRef, Ref<ChunkStore> blockRef, int x, int y, int z, FarmingStageData previousStage)`: Applies the base stage, resolves the state to a block type, and swaps the block while preserving rotation.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Keeps rotation when swapping the block type.

## Examples
```java
String state = stage.getState();
```
