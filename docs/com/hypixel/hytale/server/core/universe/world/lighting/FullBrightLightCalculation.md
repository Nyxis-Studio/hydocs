# FullBrightLightCalculation

## Overview
- Documentation for `FullBrightLightCalculation`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.lighting`.

## Constructors
- `FullBrightLightCalculation(ChunkLightingManager chunkLightingManager, LightCalculation delegate)`
  - Creates a `FullBrightLightCalculation` instance.

## Methods
- `init(@Nonnull WorldChunk worldChunk)`
  - Executes `init` behavior.
- `calculateLight(@Nonnull Vector3i chunkPosition)`
  - Executes `calculateLight` behavior.
- `invalidateLightAtBlock(@Nonnull WorldChunk worldChunk, int blockX, int blockY, int blockZ, @Nonnull BlockType blockType, int oldHeight, int newHeight)`
  - Executes `invalidateLightAtBlock` behavior.
- `invalidateLightInChunkSections(@Nonnull WorldChunk worldChunk, int sectionIndexFrom, int sectionIndexTo)`
  - Executes `invalidateLightInChunkSections` behavior.
- `setFullBright(@Nonnull WorldChunk worldChunk, int chunkY)`
  - Executes `setFullBright` behavior.

## Notes
- No additional notes.
