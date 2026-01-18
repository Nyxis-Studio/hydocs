# FluidSystems

## Overview
- Documentation for `FluidSystems`.
- Declared as a class in `com.hypixel.hytale.builtin.fluid`.

## Constructors
- None.

## Methods
- `isParallel(int archetypeChunkSize, int taskCount)`
  - Executes `isParallel` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `tick` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `fetch(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer, PlayerRef query, @Nonnull List<CompletableFuture<Packet>> results)`
  - Executes `fetch` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityRemoved` behavior.

## Notes
- No additional notes.
