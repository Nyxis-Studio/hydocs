**Source Hash:** `a74eb3e7f37d9cd7221e8b8a42e6e8c8a30d1d47b155879f0793ac90c8ef007e`

# ChunkTracker

## Overview

## Constructor Descriptions
- `ChunkTracker()`
  - Creates a `ChunkTracker` instance.
- `ChunkTracker(@Nonnull ChunkTracker other)`
  - Creates a `ChunkTracker` instance.
- `ChunkTracker(this)`
  - Creates a `ChunkTracker` instance.

## Method Descriptions
- `getComponentType()`: Add description.
  - Executes `getComponentType` behavior.
- `unloadAll(@Nonnull PlayerRef playerRefComponent)`: Add description.
  - Executes `unloadAll` behavior.
- `clear()`: Add description.
  - Executes `clear` behavior.
- `tick(@Nonnull Ref<EntityStore> playerRef, float dt, @Nonnull CommandBuffer<EntityStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `isLoaded(long indexChunk)`: Add description.
  - Executes `isLoaded` behavior.
- `removeForReload(long indexChunk)`: Add description.
  - Executes `removeForReload` behavior.
- `shouldBeVisible(long chunkCoordinates)`: Add description.
  - Executes `shouldBeVisible` behavior.
- `getChunkVisibility(long indexChunk)`: Add description.
  - Executes `getChunkVisibility` behavior.
- `getMaxChunksPerSecond()`: Add description.
  - Executes `getMaxChunksPerSecond` behavior.
- `setMaxChunksPerSecond(int maxChunksPerSecond)`: Add description.
  - Executes `setMaxChunksPerSecond` behavior.
- `setDefaultMaxChunksPerSecond(@Nonnull PlayerRef playerRef)`: Add description.
  - Executes `setDefaultMaxChunksPerSecond` behavior.
- `getMaxChunksPerTick()`: Add description.
  - Executes `getMaxChunksPerTick` behavior.
- `setMaxChunksPerTick(int maxChunksPerTick)`: Add description.
  - Executes `setMaxChunksPerTick` behavior.
- `getMinLoadedChunksRadius()`: Add description.
  - Executes `getMinLoadedChunksRadius` behavior.
- `setMinLoadedChunksRadius(int minLoadedChunksRadius)`: Add description.
  - Executes `setMinLoadedChunksRadius` behavior.
- `getMaxHotLoadedChunksRadius()`: Add description.
  - Executes `getMaxHotLoadedChunksRadius` behavior.
- `setMaxHotLoadedChunksRadius(int maxHotLoadedChunksRadius)`: Add description.
  - Executes `setMaxHotLoadedChunksRadius` behavior.
- `getLoadedChunksCount()`: Add description.
  - Executes `getLoadedChunksCount` behavior.
- `getLoadingChunksCount()`: Add description.
  - Executes `getLoadingChunksCount` behavior.
- `getLoadedChunksGrid()`: Add description.
  - Executes `getLoadedChunksGrid` behavior.
- `getLoadedChunksMessage()`: Add description.
  - Executes `getLoadedChunksMessage` behavior.
- `getLoadedChunksDebug()`: Add description.
  - Executes `getLoadedChunksDebug` behavior.
- `setReadyForChunks(boolean readyForChunks)`: Add description.
  - Executes `setReadyForChunks` behavior.
- `isReadyForChunks()`: Add description.
  - Executes `isReadyForChunks` behavior.
- `copyFrom(@Nonnull ChunkTracker chunkTracker)`: Add description.
  - Executes `copyFrom` behavior.
- `clone()`: Add description.
  - Executes `clone` behavior.
- `shouldBeVisible(int chunkViewRadiusSquared, int chunkX, int chunkZ, int x, int z)`: Add description.
  - Executes `shouldBeVisible` behavior.
- `tryUnloadChunk(long chunkIndex, int chunkViewRadiusSquared, int chunkX, int chunkZ, @Nonnull PlayerRef playerRef, @Nonnull LongSet loading)`: Add description.
  - Executes `tryUnloadChunk` behavior.
- `tryLoadChunkAsync(@Nonnull ChunkStore chunkStore, @Nonnull PlayerRef playerRefComponent, long chunkIndex, @Nonnull TransformComponent transformComponent, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`: Add description.
  - Executes `tryLoadChunkAsync` behavior.
- `_loadChunkAsync(long chunkIndex, @Nonnull PlayerRef playerRefComponent, @Nonnull Ref<ChunkStore> chunkRef, @Nonnull ChunkStore chunkStore)`: Add description.
  - Executes `_loadChunkAsync` behavior.

## Notes
- No additional notes.
