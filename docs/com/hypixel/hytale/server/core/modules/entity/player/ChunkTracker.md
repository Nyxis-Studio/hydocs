# ChunkTracker

## Overview
- Documentation for `ChunkTracker`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.entity.player`.

## Constructors
- `ChunkTracker()`
  - Creates a `ChunkTracker` instance.
- `ChunkTracker(@Nonnull ChunkTracker other)`
  - Creates a `ChunkTracker` instance.
- `ChunkTracker(this)`
  - Creates a `ChunkTracker` instance.

## Methods
- `getComponentType()`
  - Executes `getComponentType` behavior.
- `unloadAll(@Nonnull PlayerRef playerRefComponent)`
  - Executes `unloadAll` behavior.
- `clear()`
  - Executes `clear` behavior.
- `tick(@Nonnull Ref<EntityStore> playerRef, float dt, @Nonnull CommandBuffer<EntityStore> commandBuffer)`
  - Executes `tick` behavior.
- `isLoaded(long indexChunk)`
  - Executes `isLoaded` behavior.
- `removeForReload(long indexChunk)`
  - Executes `removeForReload` behavior.
- `shouldBeVisible(long chunkCoordinates)`
  - Executes `shouldBeVisible` behavior.
- `getChunkVisibility(long indexChunk)`
  - Executes `getChunkVisibility` behavior.
- `getMaxChunksPerSecond()`
  - Executes `getMaxChunksPerSecond` behavior.
- `setMaxChunksPerSecond(int maxChunksPerSecond)`
  - Executes `setMaxChunksPerSecond` behavior.
- `setDefaultMaxChunksPerSecond(@Nonnull PlayerRef playerRef)`
  - Executes `setDefaultMaxChunksPerSecond` behavior.
- `getMaxChunksPerTick()`
  - Executes `getMaxChunksPerTick` behavior.
- `setMaxChunksPerTick(int maxChunksPerTick)`
  - Executes `setMaxChunksPerTick` behavior.
- `getMinLoadedChunksRadius()`
  - Executes `getMinLoadedChunksRadius` behavior.
- `setMinLoadedChunksRadius(int minLoadedChunksRadius)`
  - Executes `setMinLoadedChunksRadius` behavior.
- `getMaxHotLoadedChunksRadius()`
  - Executes `getMaxHotLoadedChunksRadius` behavior.
- `setMaxHotLoadedChunksRadius(int maxHotLoadedChunksRadius)`
  - Executes `setMaxHotLoadedChunksRadius` behavior.
- `getLoadedChunksCount()`
  - Executes `getLoadedChunksCount` behavior.
- `getLoadingChunksCount()`
  - Executes `getLoadingChunksCount` behavior.
- `getLoadedChunksGrid()`
  - Executes `getLoadedChunksGrid` behavior.
- `getLoadedChunksMessage()`
  - Executes `getLoadedChunksMessage` behavior.
- `getLoadedChunksDebug()`
  - Executes `getLoadedChunksDebug` behavior.
- `setReadyForChunks(boolean readyForChunks)`
  - Executes `setReadyForChunks` behavior.
- `isReadyForChunks()`
  - Executes `isReadyForChunks` behavior.
- `copyFrom(@Nonnull ChunkTracker chunkTracker)`
  - Executes `copyFrom` behavior.
- `clone()`
  - Executes `clone` behavior.
- `shouldBeVisible(int chunkViewRadiusSquared, int chunkX, int chunkZ, int x, int z)`
  - Executes `shouldBeVisible` behavior.
- `tryUnloadChunk(long chunkIndex, int chunkViewRadiusSquared, int chunkX, int chunkZ, @Nonnull PlayerRef playerRef, @Nonnull LongSet loading)`
  - Executes `tryUnloadChunk` behavior.
- `tryLoadChunkAsync(@Nonnull ChunkStore chunkStore, @Nonnull PlayerRef playerRefComponent, long chunkIndex, @Nonnull TransformComponent transformComponent, @Nonnull ComponentAccessor<EntityStore> componentAccessor)`
  - Executes `tryLoadChunkAsync` behavior.
- `_loadChunkAsync(long chunkIndex, @Nonnull PlayerRef playerRefComponent, @Nonnull Ref<ChunkStore> chunkRef, @Nonnull ChunkStore chunkStore)`
  - Executes `_loadChunkAsync` behavior.

## Notes
- No additional notes.
