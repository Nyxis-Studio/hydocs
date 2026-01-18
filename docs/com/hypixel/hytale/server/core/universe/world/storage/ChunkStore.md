**Source Hash:** `7ea9d035dcae3be905522338703b0d14e5726f3353d294af1af45db2523e54c5`

# ChunkStore

## Overview

## Constructor Descriptions
- `ChunkStore(@Nonnull World world)`
  - Creates a `ChunkStore` instance.

## Method Descriptions
- `getWorld()`: Add description.
  - Executes `getWorld` behavior.
- `getStore()`: Add description.
  - Executes `getStore` behavior.
- `getLoader()`: Add description.
  - Executes `getLoader` behavior.
- `getSaver()`: Add description.
  - Executes `getSaver` behavior.
- `getGenerator()`: Add description.
  - Executes `getGenerator` behavior.
- `setGenerator(@Nullable IWorldGen generator)`: Add description.
  - Executes `setGenerator` behavior.
- `getChunkIndexes()`: Add description.
  - Executes `getChunkIndexes` behavior.
- `getLoadedChunksCount()`: Add description.
  - Executes `getLoadedChunksCount` behavior.
- `getTotalGeneratedChunksCount()`: Add description.
  - Executes `getTotalGeneratedChunksCount` behavior.
- `getTotalLoadedChunksCount()`: Add description.
  - Executes `getTotalLoadedChunksCount` behavior.
- `start(@Nonnull IResourceStorage resourceStorage)`: Add description.
  - Executes `start` behavior.
- `waitForLoadingChunks()`: Add description.
  - Executes `waitForLoadingChunks` behavior.
- `shutdown()`: Add description.
  - Executes `shutdown` behavior.
- `add(@Nonnull Holder<ChunkStore> holder)`: Add description.
  - Executes `add` behavior.
- `remove(@Nonnull Ref<ChunkStore> reference, @Nonnull RemoveReason reason)`: Add description.
  - Executes `remove` behavior.
- `getChunkReference(long index)`: Add description.
  - Executes `getChunkReference` behavior.
- `getChunkSectionReference(int x, int y, int z)`: Add description.
  - Executes `getChunkSectionReference` behavior.
- `getChunkSectionReference(@Nonnull ComponentAccessor<ChunkStore> commandBuffer, int x, int y, int z)`: Add description.
  - Executes `getChunkSectionReference` behavior.
- `getChunkSectionReferenceAsync(int x, int y, int z)`: Add description.
  - Executes `getChunkSectionReferenceAsync` behavior.
- `getChunkComponent(long index, @Nonnull ComponentType<ChunkStore, T> componentType)`: Add description.
  - Executes `getChunkComponent` behavior.
- `getChunkReferenceAsync(long index)`: Add description.
  - Executes `getChunkReferenceAsync` behavior.
- `getChunkReferenceAsync(long index, int flags)`: Add description.
  - Executes `getChunkReferenceAsync` behavior.
- `isChunkStillNeeded(long index)`: Add description.
  - Executes `isChunkStillNeeded` behavior.
- `isChunkOnBackoff(long index, long maxFailureBackoffNanos)`: Add description.
  - Executes `isChunkOnBackoff` behavior.
- `preLoadChunkAsync(long index, @Nonnull Holder<ChunkStore> holder, boolean newlyGenerated)`: Add description.
  - Executes `preLoadChunkAsync` behavior.
- `postLoadChunk(@Nullable Holder<ChunkStore> holder)`: Add description.
  - Executes `postLoadChunk` behavior.
- `fail(Throwable throwable)`: Add description.
  - Executes `fail` behavior.
- `getGroup()`: Add description.
  - Executes `getGroup` behavior.
- `onSystemAddedToStore(@Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `onSystemAddedToStore` behavior.
- `onSystemRemovedFromStore(@Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `onSystemRemovedFromStore` behavior.

## Notes
- No additional notes.
