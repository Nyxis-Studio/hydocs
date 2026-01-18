# BrushConfigChunkAccessor

## Overview
- Documentation for `BrushConfigChunkAccessor`.
- Declared as a class in `com.hypixel.hytale.builtin.buildertools.scriptedbrushes`.

## Constructors
- `BrushConfigChunkAccessor(editOperation, delegate, centerX, centerZ, chunkRadius)`
  - Creates a `BrushConfigChunkAccessor` instance.
- `BrushConfigChunkAccessor(BrushConfigEditStore editOperation, ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int radius)`
  - Creates a `BrushConfigChunkAccessor` instance.

## Methods
- `atWorldCoords(BrushConfigEditStore editOperation, ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int blockRadius)`
  - Executes `atWorldCoords` behavior.
- `atChunkCoords(BrushConfigEditStore editOperation, ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int chunkRadius)`
  - Executes `atChunkCoords` behavior.
- `getBlock(@Nonnull Vector3i pos)`
  - Executes `getBlock` behavior.
- `getBlock(int x, int y, int z)`
  - Executes `getBlock` behavior.
- `getBlockIgnoringHistory(@Nonnull Vector3i pos)`
  - Executes `getBlockIgnoringHistory` behavior.
- `getBlockIgnoringHistory(int x, int y, int z)`
  - Executes `getBlockIgnoringHistory` behavior.
- `getFluidId(int x, int y, int z)`
  - Executes `getFluidId` behavior.

## Notes
- No additional notes.
