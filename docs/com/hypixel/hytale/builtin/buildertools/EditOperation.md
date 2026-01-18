# EditOperation

## Overview
- Documentation for `EditOperation`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools`.

## Constructors
- `EditOperation(@Nonnull World world, int x, int y, int z, int editRange, Vector3i min, Vector3i max, BlockMask blockMask)`
  - Creates a `EditOperation` instance.

## Methods
- `getBlockMask()`
  - Executes `getBlockMask` behavior.
- `getBefore()`
  - Executes `getBefore` behavior.
- `getAfter()`
  - Executes `getAfter` behavior.
- `getAccessor()`
  - Executes `getAccessor` behavior.
- `getBlock(int x, int y, int z)`
  - Executes `getBlock` behavior.
- `setBlock(int x, int y, int z, int blockId)`
  - Executes `setBlock` behavior.
- `setBlock(int x, int y, int z, int blockId, int rotation)`
  - Executes `setBlock` behavior.
- `setFluid(int x, int y, int z, int fluidId, byte fluidLevel)`
  - Executes `setFluid` behavior.
- `getFluid(int x, int y, int z)`
  - Executes `getFluid` behavior.
- `setMaterial(int x, int y, int z, @Nonnull Material material)`
  - Executes `setMaterial` behavior.

## Notes
- No additional notes.
