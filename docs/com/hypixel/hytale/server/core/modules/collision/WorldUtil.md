# WorldUtil

## Overview
- Documentation for `WorldUtil`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.collision`.

## Constructors
- None.

## Methods
- `isFluidOnlyBlock(@Nonnull BlockType blockType, int fluidId)`
  - Executes `isFluidOnlyBlock` behavior.
- `isSolidOnlyBlock(@Nonnull BlockType blockType, int fluidId)`
  - Executes `isSolidOnlyBlock` behavior.
- `isEmptyOnlyBlock(@Nonnull BlockType blockType, int fluidId)`
  - Executes `isEmptyOnlyBlock` behavior.
- `getFluidIdAtPosition(@Nonnull ComponentAccessor<ChunkStore> chunkStore, @Nonnull ChunkColumn chunkColumnComponent, int x, int y, int z)`
  - Executes `getFluidIdAtPosition` behavior.
- `getPackedMaterialAndFluidAtPosition(@Nonnull Ref<ChunkStore> chunkRef, @Nonnull ComponentAccessor<ChunkStore> chunkStore, double x, double y, double z)`
  - Executes `getPackedMaterialAndFluidAtPosition` behavior.
- `findFluidBlock(@Nonnull ComponentAccessor<ChunkStore> chunkStore, @Nonnull ChunkColumn chunkColumnComponent, @Nonnull BlockChunk blockChunkComponent, int x, int y, int z, boolean allowBubble)`
  - Executes `findFluidBlock` behavior.
- `getWaterLevel(@Nonnull ComponentAccessor<ChunkStore> chunkStore, @Nonnull ChunkColumn chunkColumnComponent, @Nonnull BlockChunk blockChunkComponent, int x, int z, int startY)`
  - Executes `getWaterLevel` behavior.
- `findFarthestEmptySpaceBelow(@Nonnull ComponentAccessor<ChunkStore> chunkStore, @Nonnull ChunkColumn chunkColumnComponent, @Nonnull BlockChunk blockChunkComponent, int x, int y, int z, int yFail)`
  - Executes `findFarthestEmptySpaceBelow` behavior.
- `findFarthestEmptySpaceAbove(@Nonnull ComponentAccessor<ChunkStore> chunkStore, @Nonnull ChunkColumn chunkColumnComponent, @Nonnull BlockChunk blockChunkComponent, int x, int y, int z, int yFail)`
  - Executes `findFarthestEmptySpaceAbove` behavior.

## Notes
- No additional notes.
