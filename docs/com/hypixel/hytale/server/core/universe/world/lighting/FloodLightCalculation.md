**Source Hash:** `06fc130bf319d5173ecf6abebf2fe93888faeaf08383ee00972500434c6fa8bf`

# FloodLightCalculation

## Overview

## Constructor Descriptions
- `FloodLightCalculation(ChunkLightingManager chunkLightingManager)`
  - Creates a `FloodLightCalculation` instance.

## Method Descriptions
- `init(@Nonnull WorldChunk chunk)`: Add description.
  - Executes `init` behavior.
- `initChunk(int x, int z)`: Add description.
  - Executes `initChunk` behavior.
- `initChunk(@Nonnull WorldChunk chunk, int x, int z)`: Add description.
  - Executes `initChunk` behavior.
- `initNeighbours(int x, int z)`: Add description.
  - Executes `initNeighbours` behavior.
- `initSection(@Nonnull WorldChunk chunk, int x, int y, int z)`: Add description.
  - Executes `initSection` behavior.
- `initNeighbours(@Nonnull LocalCachedChunkAccessor accessor, int chunkX, int chunkY, int chunkZ)`: Add description.
  - Executes `initNeighbours` behavior.
- `initNeighbourSections(@Nonnull LocalCachedChunkAccessor accessor, int x, int y, int z)`: Add description.
  - Executes `initNeighbourSections` behavior.
- `calculateLight(@Nonnull Vector3i chunkPosition)`: Add description.
  - Executes `calculateLight` behavior.
- `updateLocalLight(LocalCachedChunkAccessor accessor, @Nonnull WorldChunk worldChunk, int chunkX, int chunkY, int chunkZ, @Nonnull BlockSection toSection, @Nonnull FluidSection fluidSection, @Nonnull AtomicLong chunkLightTiming, boolean fineLoggable)`: Add description.
  - Executes `updateLocalLight` behavior.
- `updateGlobalLight(@Nonnull LocalCachedChunkAccessor accessor, @Nonnull WorldChunk worldChunk, int chunkX, int chunkY, int chunkZ, @Nonnull BlockSection toSection, @Nonnull AtomicLong chunkLightTiming, boolean fineLoggable)`: Add description.
  - Executes `updateGlobalLight` behavior.
- `invalidateLightAtBlock(@Nonnull WorldChunk worldChunk, int blockX, int blockY, int blockZ, @Nonnull BlockType blockType, int oldHeight, int newHeight)`: Add description.
  - Executes `invalidateLightAtBlock` behavior.
- `invalidateLightInChunkSections(@Nonnull WorldChunk worldChunk, int sectionIndexFrom, int sectionIndexTo)`: Add description.
  - Executes `invalidateLightInChunkSections` behavior.
- `floodEmptyChunkSection(@Nonnull WorldChunk worldChunk, short changeCounter, int chunkY)`: Add description.
  - Executes `floodEmptyChunkSection` behavior.
- `floodChunkSection(@Nonnull WorldChunk worldChunk, @Nonnull BlockSection toSection, @Nonnull FluidSection fluidSection, int chunkY)`: Add description.
  - Executes `floodChunkSection` behavior.
- `getSkyValue(WorldChunk worldChunk, int chunkY, int blockX, int blockY, int blockZ, int sectionY, int height)`: Add description.
  - Executes `getSkyValue` behavior.
- `propagateLight(@Nonnull BitSet bitSetQueue, @Nonnull BlockSection section, @Nonnull ChunkLightDataBuilder light)`: Add description.
  - Executes `propagateLight` behavior.
- `testNeighboursForLocalLight(@Nonnull LocalCachedChunkAccessor accessor, @Nonnull WorldChunk worldChunk, int chunkX, int chunkY, int chunkZ)`: Add description.
  - Executes `testNeighboursForLocalLight` behavior.
- `propagateSides(@Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder globalLight, @Nonnull BitSet bitSetQueue)`: Add description.
  - Executes `propagateSides` behavior.
- `propagateSide(@Nonnull BitSet bitSetQueue, @Nullable BlockSection fromSection, @Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder toLight, @Nonnull IntBinaryOperator fromIndex, @Nonnull IntBinaryOperator toIndex)`: Add description.
  - Executes `propagateSide` behavior.
- `propagateEdges(@Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder globalLight, @Nonnull BitSet bitSetQueue)`: Add description.
  - Executes `propagateEdges` behavior.
- `propagateEdge(@Nonnull BitSet bitSetQueue, @Nullable BlockSection fromSection, @Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder toLight, @Nonnull Int2IntFunction fromIndex, @Nonnull Int2IntFunction toIndex)`: Add description.
  - Executes `propagateEdge` behavior.
- `propagateCorners(@Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder globalLight, @Nonnull BitSet bitSetQueue)`: Add description.
  - Executes `propagateCorners` behavior.
- `propagateCorner(@Nonnull BitSet bitSetQueue, @Nullable BlockSection fromSection, @Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder toLight, int fromBlockIndex, int toBlockIndex)`: Add description.
  - Executes `propagateCorner` behavior.
- `propagateLight(@Nonnull BitSet bitSetQueue, byte propagatedRedValue, byte propagatedGreenValue, byte propagatedBlueValue, byte propagatedSkyValue, @Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder toLight, int toBlockIndex)`: Add description.
  - Executes `propagateLight` behavior.

## Notes
- No additional notes.
