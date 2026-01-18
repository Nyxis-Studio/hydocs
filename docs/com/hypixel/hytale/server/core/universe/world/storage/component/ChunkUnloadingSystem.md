# ChunkUnloadingSystem

## Overview
- Documentation for `ChunkUnloadingSystem`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.storage.component`.

## Constructors
- None.

## Methods
- `tick(float dt, int systemIndex, @Nonnull Store<ChunkStore> store)`
  - Executes `tick` behavior.
- `tryUnload(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `tryUnload` behavior.
- `isChunkInBox(@Nonnull Box2D box, int x, int z)`
  - Executes `isChunkInBox` behavior.
- `collectTrackers(@Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `collectTrackers` behavior.
- `clone()`
  - Executes `clone` behavior.
- `tick(float dt)`
  - Executes `tick` behavior.

## Notes
- No additional notes.
