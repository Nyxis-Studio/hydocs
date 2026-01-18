# BlockFilter

## Overview
- Documentation for `BlockFilter`.
- Declared as a class in `com.hypixel.hytale.server.core.prefab.selection.mask`.

## Constructors
- `BlockFilter(@Nonnull FilterType blockFilterType, @Nonnull String[] blocks, boolean inverted)`
  - Creates a `BlockFilter` instance.
- `BlockFilter(parts.type, blocks, parts.inverted)`
  - Creates a `BlockFilter` instance.

## Methods
- `resolve()`
  - Executes `resolve` behavior.
- `getBlockFilterType()`
  - Executes `getBlockFilterType` behavior.
- `getBlocks()`
  - Executes `getBlocks` behavior.
- `isInverted()`
  - Executes `isInverted` behavior.
- `isExcluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, Vector3i min, Vector3i max, int blockId)`
  - Executes `isExcluded` behavior.
- `isExcluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, Vector3i min, Vector3i max, int blockId, int fluidId)`
  - Executes `isExcluded` behavior.
- `isIncluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, @Nullable Vector3i min, @Nullable Vector3i max, int blockId)`
  - Executes `isIncluded` behavior.
- `isIncluded(@Nonnull ChunkAccessor accessor, int x, int y, int z, @Nullable Vector3i min, @Nullable Vector3i max, int blockId, int fluidId)`
  - Executes `isIncluded` behavior.
- `matchesAt(@Nonnull ChunkAccessor accessor, int x, int y, int z)`
  - Executes `matchesAt` behavior.
- `toString()`
  - Executes `toString` behavior.
- `toString0()`
  - Executes `toString0` behavior.
- `informativeToString()`
  - Executes `informativeToString` behavior.
- `parse(@Nonnull String str)`
  - Executes `parse` behavior.
- `parseComponents(@Nonnull String str)`
  - Executes `parseComponents` behavior.
- `parseBlocks(@Nonnull String[] blocksArgs)`
  - Executes `parseBlocks` behavior.
- `parseBlocksAndFluids(@Nonnull String[] blocksArgs)`
  - Executes `parseBlocksAndFluids` behavior.
- `getFluidIdFromItem(@Nonnull Item item)`
  - Executes `getFluidIdFromItem` behavior.
- `hasBlocks()`
  - Executes `hasBlocks` behavior.
- `getPrefix()`
  - Executes `getPrefix` behavior.
- `parse(@Nonnull String str, int index)`
  - Executes `parse` behavior.
- `ParsedFilterParts(FilterType type, boolean inverted, String blocks)`
  - Executes `ParsedFilterParts` behavior.

## Notes
- No additional notes.
