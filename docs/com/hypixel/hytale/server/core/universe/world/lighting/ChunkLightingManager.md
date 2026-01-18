# ChunkLightingManager

## Overview
- Documentation for `ChunkLightingManager`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.lighting`.

## Constructors
- `ChunkLightingManager(@Nonnull World world)`
  - Creates a `ChunkLightingManager` instance.

## Methods
- `getLogger()`
  - Executes `getLogger` behavior.
- `getWorld()`
  - Executes `getWorld` behavior.
- `setLightCalculation(LightCalculation lightCalculation)`
  - Executes `setLightCalculation` behavior.
- `getLightCalculation()`
  - Executes `getLightCalculation` behavior.
- `start()`
  - Executes `start` behavior.
- `run()`
  - Executes `run` behavior.
- `process(Vector3i chunkPosition)`
  - Executes `process` behavior.
- `interrupt()`
  - Executes `interrupt` behavior.
- `stop()`
  - Executes `stop` behavior.
- `init(WorldChunk worldChunk)`
  - Executes `init` behavior.
- `addToQueue(Vector3i chunkPosition)`
  - Executes `addToQueue` behavior.
- `isQueued(int chunkX, int chunkZ)`
  - Executes `isQueued` behavior.
- `isQueued(Vector3i chunkPosition)`
  - Executes `isQueued` behavior.
- `getQueueSize()`
  - Executes `getQueueSize` behavior.
- `invalidateLightAtBlock(WorldChunk worldChunk, int blockX, int blockY, int blockZ, BlockType blockType, int oldHeight, int newHeight)`
  - Executes `invalidateLightAtBlock` behavior.
- `invalidateLightInChunk(WorldChunk worldChunk)`
  - Executes `invalidateLightInChunk` behavior.
- `invalidateLightInChunkSection(WorldChunk worldChunk, int sectionIndex)`
  - Executes `invalidateLightInChunkSection` behavior.
- `invalidateLightInChunkSections(WorldChunk worldChunk, int sectionIndexFrom, int sectionIndexTo)`
  - Executes `invalidateLightInChunkSections` behavior.
- `invalidateLoadedChunks()`
  - Executes `invalidateLoadedChunks` behavior.

## Notes
- No additional notes.
