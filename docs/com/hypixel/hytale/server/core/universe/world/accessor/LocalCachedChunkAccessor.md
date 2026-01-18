# LocalCachedChunkAccessor

## Overview
- Documentation for `LocalCachedChunkAccessor`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.accessor`.

## Constructors
- `LocalCachedChunkAccessor(delegate, centerX, centerZ, chunkRadius)`
  - Creates a `LocalCachedChunkAccessor` instance.
- `LocalCachedChunkAccessor(delegate, chunk.getX()`
  - Creates a `LocalCachedChunkAccessor` instance.
- `LocalCachedChunkAccessor(ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int radius)`
  - Creates a `LocalCachedChunkAccessor` instance.

## Methods
- `atWorldCoords(ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int blockRadius)`
  - Executes `atWorldCoords` behavior.
- `atChunkCoords(ChunkAccessor<WorldChunk> delegate, int centerX, int centerZ, int chunkRadius)`
  - Executes `atChunkCoords` behavior.
- `atChunk(ChunkAccessor<WorldChunk> delegate, @Nonnull WorldChunk chunk, int chunkRadius)`
  - Executes `atChunk` behavior.
- `getDelegate()`
  - Executes `getDelegate` behavior.
- `getMinX()`
  - Executes `getMinX` behavior.
- `getMinZ()`
  - Executes `getMinZ` behavior.
- `getLength()`
  - Executes `getLength` behavior.
- `getCenterX()`
  - Executes `getCenterX` behavior.
- `getCenterZ()`
  - Executes `getCenterZ` behavior.
- `cacheChunksInRadius()`
  - Executes `cacheChunksInRadius` behavior.
- `overwrite(@Nonnull WorldChunk wc)`
  - Executes `overwrite` behavior.
- `getChunkIfInMemory(long index)`
  - Executes `getChunkIfInMemory` behavior.
- `getChunkIfInMemory(int x, int z)`
  - Executes `getChunkIfInMemory` behavior.
- `loadChunkIfInMemory(long index)`
  - Executes `loadChunkIfInMemory` behavior.
- `getChunkIfLoaded(long index)`
  - Executes `getChunkIfLoaded` behavior.
- `getChunkIfLoaded(int x, int z)`
  - Executes `getChunkIfLoaded` behavior.
- `getChunkIfNonTicking(long index)`
  - Executes `getChunkIfNonTicking` behavior.
- `getChunk(long index)`
  - Executes `getChunk` behavior.
- `getNonTickingChunk(long index)`
  - Executes `getNonTickingChunk` behavior.

## Notes
- No additional notes.
