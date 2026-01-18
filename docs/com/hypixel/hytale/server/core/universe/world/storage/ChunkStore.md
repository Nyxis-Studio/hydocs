# ChunkStore

## Overview
- Documentation for `ChunkStore`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.storage`.

## Constructors
- `ChunkStore(@Nonnull World world)`
  - Creates a `ChunkStore` instance.

## Methods
- `getWorld()`
  - Executes `getWorld` behavior.
- `getStore()`
  - Executes `getStore` behavior.
- `getLoader()`
  - Executes `getLoader` behavior.
- `getSaver()`
  - Executes `getSaver` behavior.
- `getGenerator()`
  - Executes `getGenerator` behavior.
- `setGenerator(@Nullable IWorldGen generator)`
  - Executes `setGenerator` behavior.
- `getChunkIndexes()`
  - Executes `getChunkIndexes` behavior.
- `getLoadedChunksCount()`
  - Executes `getLoadedChunksCount` behavior.
- `getTotalGeneratedChunksCount()`
  - Executes `getTotalGeneratedChunksCount` behavior.
- `getTotalLoadedChunksCount()`
  - Executes `getTotalLoadedChunksCount` behavior.
- `start(@Nonnull IResourceStorage resourceStorage)`
  - Executes `start` behavior.
- `waitForLoadingChunks()`
  - Executes `waitForLoadingChunks` behavior.
- `shutdown()`
  - Executes `shutdown` behavior.
- `add(@Nonnull Holder<ChunkStore> holder)`
  - Executes `add` behavior.
- `remove(@Nonnull Ref<ChunkStore> reference, @Nonnull RemoveReason reason)`
  - Executes `remove` behavior.
- `getChunkReference(long index)`
  - Executes `getChunkReference` behavior.
- `getChunkSectionReference(int x, int y, int z)`
  - Executes `getChunkSectionReference` behavior.
- `getChunkSectionReference(@Nonnull ComponentAccessor<ChunkStore> commandBuffer, int x, int y, int z)`
  - Executes `getChunkSectionReference` behavior.
- `getChunkSectionReferenceAsync(int x, int y, int z)`
  - Executes `getChunkSectionReferenceAsync` behavior.
- `getChunkComponent(long index, @Nonnull ComponentType<ChunkStore, T> componentType)`
  - Executes `getChunkComponent` behavior.
- `getChunkReferenceAsync(long index)`
  - Executes `getChunkReferenceAsync` behavior.
- `getChunkReferenceAsync(long index, int flags)`
  - Executes `getChunkReferenceAsync` behavior.
- `isChunkStillNeeded(long index)`
  - Executes `isChunkStillNeeded` behavior.
- `isChunkOnBackoff(long index, long maxFailureBackoffNanos)`
  - Executes `isChunkOnBackoff` behavior.
- `preLoadChunkAsync(long index, @Nonnull Holder<ChunkStore> holder, boolean newlyGenerated)`
  - Executes `preLoadChunkAsync` behavior.
- `postLoadChunk(@Nullable Holder<ChunkStore> holder)`
  - Executes `postLoadChunk` behavior.
- `fail(Throwable throwable)`
  - Executes `fail` behavior.
- `getGroup()`
  - Executes `getGroup` behavior.
- `onSystemAddedToStore(@Nonnull Store<ChunkStore> store)`
  - Executes `onSystemAddedToStore` behavior.
- `onSystemRemovedFromStore(@Nonnull Store<ChunkStore> store)`
  - Executes `onSystemRemovedFromStore` behavior.

## Notes
- No additional notes.
