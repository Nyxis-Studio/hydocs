# BlockStateModule

## Overview
- Documentation for `BlockStateModule`.
- Declared as a class in `com.hypixel.hytale.server.core.universe.world.meta`.

## Constructors
- `BlockStateModule(@Nonnull JavaPluginInit init)`
  - Creates a `BlockStateModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `getItemContainerSpatialResourceType()`
  - Executes `getItemContainerSpatialResourceType` behavior.
- `setup()`
  - Executes `setup` behavior.
- `registerBlockState(@Nonnull Class<T> clazz, @Nonnull String key, Codec<T> codec)`
  - Executes `registerBlockState` behavior.
- `registerBlockState(@Nonnull Class<T> clazz, @Nonnull String key, @Nullable Codec<T> codec, Class<D> dataClass, @Nullable Codec<D> dataCodec)`
  - Executes `registerBlockState` behavior.
- `unregisterBlockState(Class<T> clazz, @Nullable Class<D> dataClass)`
  - Executes `unregisterBlockState` behavior.
- `createBlockState(Class<T> clazz, WorldChunk chunk, Vector3i pos, BlockType blockType)`
  - Executes `createBlockState` behavior.
- `createBlockState(String key, WorldChunk chunk, Vector3i pos, BlockType blockType)`
  - Executes `createBlockState` behavior.
- `getComponentType(@Nullable Class<T> entityClass)`
  - Executes `getComponentType` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.
- `toString()`
  - Executes `toString` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `tick` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityRemoved` behavior.
- `toMetricResults(Store<ChunkStore> store)`
  - Executes `toMetricResults` behavior.
- `fetch(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer, PlayerRef player, List<Packet> results)`
  - Executes `fetch` behavior.

## Notes
- No additional notes.
