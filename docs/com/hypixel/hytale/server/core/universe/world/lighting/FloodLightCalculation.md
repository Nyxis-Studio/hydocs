# FloodLightCalculation

## Overview
- Documentation for `FloodLightCalculation`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.lighting`.

## Constructors
- `FloodLightCalculation(ChunkLightingManager chunkLightingManager)`
  - Creates a `FloodLightCalculation` instance.

## Methods
- `init(@Nonnull WorldChunk chunk)`
  - Executes `init` behavior.
- `initChunk(int x, int z)`
  - Executes `initChunk` behavior.
- `initChunk(@Nonnull WorldChunk chunk, int x, int z)`
  - Executes `initChunk` behavior.
- `initNeighbours(int x, int z)`
  - Executes `initNeighbours` behavior.
- `initSection(@Nonnull WorldChunk chunk, int x, int y, int z)`
  - Executes `initSection` behavior.
- `initNeighbours(@Nonnull LocalCachedChunkAccessor accessor, int chunkX, int chunkY, int chunkZ)`
  - Executes `initNeighbours` behavior.
- `initNeighbourSections(@Nonnull LocalCachedChunkAccessor accessor, int x, int y, int z)`
  - Executes `initNeighbourSections` behavior.
- `calculateLight(@Nonnull Vector3i chunkPosition)`
  - Executes `calculateLight` behavior.
- `updateLocalLight(LocalCachedChunkAccessor accessor, @Nonnull WorldChunk worldChunk, int chunkX, int chunkY, int chunkZ, @Nonnull BlockSection toSection, @Nonnull FluidSection fluidSection, @Nonnull AtomicLong chunkLightTiming, boolean fineLoggable)`
  - Executes `updateLocalLight` behavior.
- `updateGlobalLight(@Nonnull LocalCachedChunkAccessor accessor, @Nonnull WorldChunk worldChunk, int chunkX, int chunkY, int chunkZ, @Nonnull BlockSection toSection, @Nonnull AtomicLong chunkLightTiming, boolean fineLoggable)`
  - Executes `updateGlobalLight` behavior.
- `invalidateLightAtBlock(@Nonnull WorldChunk worldChunk, int blockX, int blockY, int blockZ, @Nonnull BlockType blockType, int oldHeight, int newHeight)`
  - Executes `invalidateLightAtBlock` behavior.
- `invalidateLightInChunkSections(@Nonnull WorldChunk worldChunk, int sectionIndexFrom, int sectionIndexTo)`
  - Executes `invalidateLightInChunkSections` behavior.
- `floodEmptyChunkSection(@Nonnull WorldChunk worldChunk, short changeCounter, int chunkY)`
  - Executes `floodEmptyChunkSection` behavior.
- `floodChunkSection(@Nonnull WorldChunk worldChunk, @Nonnull BlockSection toSection, @Nonnull FluidSection fluidSection, int chunkY)`
  - Executes `floodChunkSection` behavior.
- `getSkyValue(WorldChunk worldChunk, int chunkY, int blockX, int blockY, int blockZ, int sectionY, int height)`
  - Executes `getSkyValue` behavior.
- `propagateLight(@Nonnull BitSet bitSetQueue, @Nonnull BlockSection section, @Nonnull ChunkLightDataBuilder light)`
  - Executes `propagateLight` behavior.
- `testNeighboursForLocalLight(@Nonnull LocalCachedChunkAccessor accessor, @Nonnull WorldChunk worldChunk, int chunkX, int chunkY, int chunkZ)`
  - Executes `testNeighboursForLocalLight` behavior.
- `propagateSides(@Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder globalLight, @Nonnull BitSet bitSetQueue)`
  - Executes `propagateSides` behavior.
- `propagateSide(@Nonnull BitSet bitSetQueue, @Nullable BlockSection fromSection, @Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder toLight, @Nonnull IntBinaryOperator fromIndex, @Nonnull IntBinaryOperator toIndex)`
  - Executes `propagateSide` behavior.
- `propagateEdges(@Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder globalLight, @Nonnull BitSet bitSetQueue)`
  - Executes `propagateEdges` behavior.
- `propagateEdge(@Nonnull BitSet bitSetQueue, @Nullable BlockSection fromSection, @Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder toLight, @Nonnull Int2IntFunction fromIndex, @Nonnull Int2IntFunction toIndex)`
  - Executes `propagateEdge` behavior.
- `propagateCorners(@Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder globalLight, @Nonnull BitSet bitSetQueue)`
  - Executes `propagateCorners` behavior.
- `propagateCorner(@Nonnull BitSet bitSetQueue, @Nullable BlockSection fromSection, @Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder toLight, int fromBlockIndex, int toBlockIndex)`
  - Executes `propagateCorner` behavior.
- `propagateLight(@Nonnull BitSet bitSetQueue, byte propagatedRedValue, byte propagatedGreenValue, byte propagatedBlueValue, byte propagatedSkyValue, @Nonnull BlockSection toSection, @Nonnull ChunkLightDataBuilder toLight, int toBlockIndex)`
  - Executes `propagateLight` behavior.

## Notes
- No additional notes.
