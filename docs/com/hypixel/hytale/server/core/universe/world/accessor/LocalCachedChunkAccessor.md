**Source Hash:** `17405ae8e6895ab01a32b6a2b24748ec9e1bf852d38c362900ec255f891bae09`

# LocalCachedChunkAccessor

## Overview

## Constructor Descriptions
- `LocalCachedChunkAccessor(delegate, centerX, centerZ, chunkRadius)`
  - Creates a `LocalCachedChunkAccessor` instance.
- `LocalCachedChunkAccessor(delegate, chunk.getX()`
  - Creates a `LocalCachedChunkAccessor` instance.
- `LocalCachedChunkAccessor(ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int radius)`
  - Creates a `LocalCachedChunkAccessor` instance.

## Method Descriptions
- `atWorldCoords(ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int blockRadius)`: Add description.
  - Executes `atWorldCoords` behavior.
- `atChunkCoords(ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int chunkRadius)`: Add description.
  - Executes `atChunkCoords` behavior.
- `atChunk(ChunkAccessor<WorldChunk> delegate, @Nonnull WorldChunk chunk, int chunkRadius)`: Add description.
  - Executes `atChunk` behavior.
- `getDelegate()`: Add description.
  - Executes `getDelegate` behavior.
- `getMinX()`: Add description.
  - Executes `getMinX` behavior.
- `getMinZ()`: Add description.
  - Executes `getMinZ` behavior.
- `getLength()`: Add description.
  - Executes `getLength` behavior.
- `getCenterX()`: Add description.
  - Executes `getCenterX` behavior.
- `getCenterZ()`: Add description.
  - Executes `getCenterZ` behavior.
- `cacheChunksInRadius()`: Add description.
  - Executes `cacheChunksInRadius` behavior.
- `overwrite(@Nonnull WorldChunk wc)`: Add description.
  - Executes `overwrite` behavior.
- `getChunkIfInMemory(long index)`: Add description.
  - Executes `getChunkIfInMemory` behavior.
- `getChunkIfInMemory(int x, int z)`: Add description.
  - Executes `getChunkIfInMemory` behavior.
- `loadChunkIfInMemory(long index)`: Add description.
  - Executes `loadChunkIfInMemory` behavior.
- `getChunkIfLoaded(long index)`: Add description.
  - Executes `getChunkIfLoaded` behavior.
- `getChunkIfLoaded(int x, int z)`: Add description.
  - Executes `getChunkIfLoaded` behavior.
- `getChunkIfNonTicking(long index)`: Add description.
  - Executes `getChunkIfNonTicking` behavior.
- `getChunk(long index)`: Add description.
  - Executes `getChunk` behavior.
- `getNonTickingChunk(long index)`: Add description.
  - Executes `getNonTickingChunk` behavior.

## Notes
- No additional notes.
