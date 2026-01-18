**Source Hash:** `c5d2c7a9012ae11b421bfe97ed013685de884a7c3a0ecae0d9f6def7fb613025`

# BlockMask

## Overview

## Constructor Descriptions
- `BlockMask(BlockFilter.EMPTY_ARRAY)`
  - Creates a `BlockMask` instance.
- `BlockMask(BlockFilter[] filters)`
  - Creates a `BlockMask` instance.
- `BlockMask(filters)`
  - Creates a `BlockMask` instance.
- `BlockMask(new BlockFilter[]{BlockFilter.parse(masks[0])`
  - Creates a `BlockMask` instance.
- `BlockMask(inputFilters)`
  - Creates a `BlockMask` instance.

## Method Descriptions
- `withOptions(@Nonnull BlockFilter.FilterType filterType, boolean inverted)`: Add description.
  - Executes `withOptions` behavior.
- `getFilters()`: Add description.
  - Executes `getFilters` behavior.
- `setInverted(boolean inverted)`: Add description.
  - Executes `setInverted` behavior.
- `isInverted()`: Add description.
  - Executes `isInverted` behavior.
- `isExcluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, Vector3i min, Vector3i max, int blockId)`: Add description.
  - Executes `isExcluded` behavior.
- `isExcluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, Vector3i min, Vector3i max, int blockId, int fluidId)`: Add description.
  - Executes `isExcluded` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `informativeToString()`: Add description.
  - Executes `informativeToString` behavior.
- `joinElements(String separator, @Nonnull Object[] elements)`: Add description.
  - Executes `joinElements` behavior.
- `parse(@Nonnull String masks)`: Add description.
  - Executes `parse` behavior.
- `parse(@Nonnull String[] masks)`: Add description.
  - Executes `parse` behavior.
- `combine(BlockMask ... masks)`: Add description.
  - Executes `combine` behavior.
- `groupFilters(@Nonnull BlockFilter[] inputFilters)`: Add description.
  - Executes `groupFilters` behavior.

## Notes
- No additional notes.
