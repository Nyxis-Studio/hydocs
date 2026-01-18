# ChunkSavingSystems

## Overview
- Documentation for `ChunkSavingSystems`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.storage.component`.

## Constructors
- None.

## Methods
- `saveChunksInWorld(@Nonnull Store<ChunkStore> store)`
  - Executes `saveChunksInWorld` behavior.
- `tryQueue(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store)`
  - Executes `tryQueue` behavior.
- `tryQueueSync(@Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `tryQueueSync` behavior.
- `saveChunk(@Nonnull Ref<ChunkStore> reference, @Nonnull Data data, boolean report, @Nonnull Store<ChunkStore> store)`
  - Executes `saveChunk` behavior.
- `clone()`
  - Executes `clone` behavior.
- `clearSaveQueue()`
  - Executes `clearSaveQueue` behavior.
- `push(@Nonnull Ref<ChunkStore> reference)`
  - Executes `push` behavior.
- `poll()`
  - Executes `poll` behavior.
- `checkTimer(float dt)`
  - Executes `checkTimer` behavior.
- `waitForSavingChunks()`
  - Executes `waitForSavingChunks` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `tick(float dt, int systemIndex, @Nonnull Store<ChunkStore> store)`
  - Executes `tick` behavior.
- `onSystemAddedToStore(@Nonnull Store<ChunkStore> store)`
  - Executes `onSystemAddedToStore` behavior.
- `onSystemRemovedFromStore(@Nonnull Store<ChunkStore> store)`
  - Executes `onSystemRemovedFromStore` behavior.

## Notes
- No additional notes.
