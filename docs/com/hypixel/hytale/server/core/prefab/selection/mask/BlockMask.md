# BlockMask

## Overview
- Documentation for `BlockMask`.
- Declared as a class in `com.hypixel.hytale.server.core.prefab.selection.mask`.

## Constructors
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

## Methods
- `withOptions(@Nonnull BlockFilter.FilterType filterType, boolean inverted)`
  - Executes `withOptions` behavior.
- `getFilters()`
  - Executes `getFilters` behavior.
- `setInverted(boolean inverted)`
  - Executes `setInverted` behavior.
- `isInverted()`
  - Executes `isInverted` behavior.
- `isExcluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, Vector3i min, Vector3i max, int blockId)`
  - Executes `isExcluded` behavior.
- `isExcluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, Vector3i min, Vector3i max, int blockId, int fluidId)`
  - Executes `isExcluded` behavior.
- `toString()`
  - Executes `toString` behavior.
- `informativeToString()`
  - Executes `informativeToString` behavior.
- `joinElements(String separator, @Nonnull Object[] elements)`
  - Executes `joinElements` behavior.
- `parse(@Nonnull String masks)`
  - Executes `parse` behavior.
- `parse(@Nonnull String[] masks)`
  - Executes `parse` behavior.
- `combine(BlockMask ... masks)`
  - Executes `combine` behavior.
- `groupFilters(@Nonnull BlockFilter[] inputFilters)`
  - Executes `groupFilters` behavior.

## Notes
- No additional notes.
