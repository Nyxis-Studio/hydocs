**Source Hash:** `dba68a890dfd0eba71efffd151383496c86887b48aba0e79d424116805d72f78`

# BlockStateModule

## Overview

## Constructor Descriptions
- `BlockStateModule(@Nonnull JavaPluginInit init)`
  - Creates a `BlockStateModule` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `getItemContainerSpatialResourceType()`: Add description.
  - Executes `getItemContainerSpatialResourceType` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `registerBlockState(@Nonnull Class<T> clazz, @Nonnull String key, Codec<T> codec)`: Add description.
  - Executes `registerBlockState` behavior.
- `registerBlockState(@Nonnull Class<T> clazz, @Nonnull String key, @Nullable Codec<T> codec, Class<D> dataClass, @Nullable Codec<D> dataCodec)`: Add description.
  - Executes `registerBlockState` behavior.
- `unregisterBlockState(Class<T> clazz, @Nullable Class<D> dataClass)`: Add description.
  - Executes `unregisterBlockState` behavior.
- `createBlockState(Class<T> clazz, WorldChunk chunk, Vector3i pos, BlockType blockType)`: Add description.
  - Executes `createBlockState` behavior.
- `createBlockState(String key, WorldChunk chunk, Vector3i pos, BlockType blockType)`: Add description.
  - Executes `createBlockState` behavior.
- `getComponentType(@Nullable Class<T> entityClass)`: Add description.
  - Executes `getComponentType` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.
- `toString()`: Add description.
  - Executes `toString` behavior.
- `getDependencies()`: Add description.
  - Executes `getDependencies` behavior.
- `tick(float dt, int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `tick` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `onEntityRemoved` behavior.
- `toMetricResults(Store<ChunkStore> store)`: Add description.
  - Executes `toMetricResults` behavior.
- `fetch(int index, @Nonnull ArchetypeChunk<ChunkStore> archetypeChunk, Store<ChunkStore> store, CommandBuffer<ChunkStore> commandBuffer, PlayerRef player, List<Packet> results)`: Add description.
  - Executes `fetch` behavior.

## Notes
- No additional notes.
