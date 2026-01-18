# EmptyBlockAccessor

## Overview
- Documentation for `EmptyBlockAccessor`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.accessor`.

## Constructors
- `EmptyBlockAccessor()`
  - Creates a `EmptyBlockAccessor` instance.

## Methods
- `getX()`
  - Executes `getX` behavior.
- `getZ()`
  - Executes `getZ` behavior.
- `getChunkAccessor()`
  - Executes `getChunkAccessor` behavior.
- `getBlock(int x, int y, int z)`
  - Executes `getBlock` behavior.
- `setBlock(int x, int y, int z, int id, BlockType blockType, int rotation, int filler, int settings)`
  - Executes `setBlock` behavior.
- `breakBlock(int x, int y, int z, int filler, int settings)`
  - Executes `breakBlock` behavior.
- `testBlocks(int x, int y, int z, BlockType blockTypeToTest, int rotation, TriIntPredicate predicate)`
  - Executes `testBlocks` behavior.
- `testBlockTypes(int x, int y, int z, BlockType blockTypeToTest, int rotation, IChunkAccessorSync.TestBlockFunction predicate)`
  - Executes `testBlockTypes` behavior.
- `testPlaceBlock(int x, int y, int z, BlockType blockTypeToTest, int rotation)`
  - Executes `testPlaceBlock` behavior.
- `testPlaceBlock(int x, int y, int z, BlockType blockTypeToTest, int rotation, IChunkAccessorSync.TestBlockFunction filter)`
  - Executes `testPlaceBlock` behavior.
- `setTicking(int x, int y, int z, boolean ticking)`
  - Executes `setTicking` behavior.
- `isTicking(int x, int y, int z)`
  - Executes `isTicking` behavior.
- `getState(int x, int y, int z)`
  - Executes `getState` behavior.
- `getBlockComponentHolder(int x, int y, int z)`
  - Executes `getBlockComponentHolder` behavior.
- `setState(int x, int y, int z, BlockState state, boolean notify)`
  - Executes `setState` behavior.
- `getFluidId(int x, int y, int z)`
  - Executes `getFluidId` behavior.
- `getFluidLevel(int x, int y, int z)`
  - Executes `getFluidLevel` behavior.
- `getSupportValue(int x, int y, int z)`
  - Executes `getSupportValue` behavior.
- `getFiller(int x, int y, int z)`
  - Executes `getFiller` behavior.
- `getRotationIndex(int x, int y, int z)`
  - Executes `getRotationIndex` behavior.

## Notes
- No additional notes.
