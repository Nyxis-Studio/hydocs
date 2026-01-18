# ChunkBlockTickSystem

## Overview
- Documentation for `ChunkBlockTickSystem`.
- Declared as a class in `com.hypixel.hytale.builtin.blocktick.system`.

## Constructors
- None.

## Methods
- `getQuery()`
  - Executes `getQuery` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `tick` behavior.
- `tick(Ref<ChunkStore> ref, @Nonnull WorldChunk worldChunk)`
  - Executes `tick` behavior.
- `tickProcedure(@Nonnull World world, @Nonnull WorldChunk chunk, int blockX, int blockY, int blockZ, int blockId)`
  - Executes `tickProcedure` behavior.
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.

## Notes
- No additional notes.
