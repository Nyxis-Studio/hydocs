**Source Hash:** `0bb2f6e67f6aeaacf69a4426d920f8bd1b6ffd85a9c7c9c38fede493e8931c6b`

# BlockFilter

## Overview

## Constructor Descriptions
- `BlockFilter(@Nonnull FilterType blockFilterType, @Nonnull String[] blocks, boolean inverted)`
  - Creates a `BlockFilter` instance.
- `BlockFilter(parts.type, blocks, parts.inverted)`
  - Creates a `BlockFilter` instance.

## Method Descriptions
- `resolve()`: Add description.
  - Executes `resolve` behavior.
- `getBlockFilterType()`: Add description.
  - Executes `getBlockFilterType` behavior.
- `getBlocks()`: Add description.
  - Executes `getBlocks` behavior.
- `isInverted()`: Add description.
  - Executes `isInverted` behavior.
- `isExcluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, Vector3i min, Vector3i max, int blockId)`: Add description.
  - Executes `isExcluded` behavior.
- `isExcluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, Vector3i min, Vector3i max, int blockId, int fluidId)`: Add description.
  - Executes `isExcluded` behavior.
- `isIncluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, @Nullable Vector3i min, @Nullable Vector3i max, int blockId)`: Add description.
  - Executes `isIncluded` behavior.
- `isIncluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, @Nullable Vector3i min, @Nullable Vector3i max, int blockId, int fluidId)`: Add description.
  - Executes `isIncluded` behavior.
- `matchesAt(@Nonnull ChunkAccessor accessor, int x, int y, int z)`: Add description.
  - Executes `matchesAt` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `toString0()`: Add description.
  - Executes `toString0` behavior.
- `informativeToString()`: Add description.
  - Executes `informativeToString` behavior.
- `parse(@Nonnull String str)`: Add description.
  - Executes `parse` behavior.
- `parseComponents(@Nonnull String str)`: Add description.
  - Executes `parseComponents` behavior.
- `parseBlocks(@Nonnull String[] blocksArgs)`: Add description.
  - Executes `parseBlocks` behavior.
- `parseBlocksAndFluids(@Nonnull String[] blocksArgs)`: Add description.
  - Executes `parseBlocksAndFluids` behavior.
- `getFluidIdFromItem(@Nonnull Item item)`: Add description.
  - Executes `getFluidIdFromItem` behavior.
- `hasBlocks()`: Add description.
  - Executes `hasBlocks` behavior.
- `getPrefix()`: Add description.
  - Executes `getPrefix` behavior.
- `parse(@Nonnull String str, int index)`: Add description.
  - Executes `parse` behavior.
- `ParsedFilterParts(FilterType type, boolean inverted, String blocks)`: Add description.
  - Executes `ParsedFilterParts` behavior.

## Notes
- No additional notes.
