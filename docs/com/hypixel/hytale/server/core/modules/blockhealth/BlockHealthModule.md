# BlockHealthModule

## Overview
- Documentation for `BlockHealthModule`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.blockhealth`.

## Constructors
- `BlockHealthModule(@Nonnull JavaPluginInit init)`
  - Creates a `BlockHealthModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `getBlockHealthChunkComponentType()`
  - Executes `getBlockHealthChunkComponentType` behavior.
- `handle(int index, @Nonnull ArchetypeChunk<EntityStore> archetypeChunk, @Nonnull Store<EntityStore> store, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull PlaceBlockEvent event)`
  - Executes `handle` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityRemoved` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `tick` behavior.
- `isParallel()`
  - Executes `isParallel` behavior.
- `fetch(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer, PlayerRef player, @Nonnull List<Packet> results)`
  - Executes `fetch` behavior.

## Notes
- No additional notes.
