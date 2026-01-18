**Source Hash:** `312691bc9d273be0629e329009425f7ca2a1f7b12ae195ef1523cf5d80c73b54`

# BlockTypeModule

## Overview

## Constructor Descriptions
- `BlockTypeModule(@Nonnull JavaPluginInit init)`
  - Creates a `BlockTypeModule` instance.

## Method Descriptions
- `get()`: Add description.
  - Executes `get` behavior.
- `setup()`: Add description.
  - Executes `setup` behavior.
- `getBlockPhysicsComponentType()`: Add description.
  - Executes `getBlockPhysicsComponentType` behavior.
- `onChunkPreLoadProcessEnsureBlockState(@Nonnull ChunkPreLoadProcessEvent event)`: Add description.
  - Executes `onChunkPreLoadProcessEnsureBlockState` behavior.
- `onChunkPreLoadProcess(@Nonnull ChunkPreLoadProcessEvent event)`: Add description.
  - Executes `onChunkPreLoadProcess` behavior.
- `onChunksectionPreLoadProcess(@Nonnull WorldChunk chunk, @Nonnull BlockSection section, int sectionIndex, @Nonnull BlockType[] blocks)`: Add description.
  - Executes `onChunksectionPreLoadProcess` behavior.
- `getBlockType(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull BlockType[] blocks, @Nonnull BlockSection section, int blockX, int blockY, int blockZ, boolean skipEmpty)`: Add description.
  - Executes `getBlockType` behavior.
- `breakOrSetFillerBlocks(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull IndexedLookupTableAssetMap<String, BlockBoundingBoxes> hitboxAssetMap, @Nonnull ChunkAccessor<?> accessor, @Nonnull BlockAccessor chunk, int finalX, int finalY, int finalZ, @Nonnull BlockType blockType, int rotation)`: Add description.
  - Executes `breakOrSetFillerBlocks` behavior.
- `getOriginBlockType(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull ChunkAccessor<?> accessor, @Nonnull BlockAccessor section, int originX, int originY, int originZ)`: Add description.
  - Executes `getOriginBlockType` behavior.
- `setFillerBlocks(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull IndexedLookupTableAssetMap<String, BlockBoundingBoxes> hitboxAssetMap, @Nonnull ChunkAccessor<?> accessor, @Nonnull BlockAccessor chunk, int finalX, int finalY, int finalZ, @Nonnull BlockType originBlockType, int rotation)`: Add description.
  - Executes `setFillerBlocks` behavior.
- `isFillerValid(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull ChunkAccessor<?> accessor, @Nonnull BlockAccessor chunk, @Nonnull BlockType blockType, int filler, int x, int y, int z)`: Add description.
  - Executes `isFillerValid` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`: Add description.
  - Executes `onEntityRemoved` behavior.
- `getQuery()`: Add description.
  - Executes `getQuery` behavior.
- `getDependencies()`: Add description.
  - Executes `getDependencies` behavior.
- `onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onEntityAdded` behavior.
- `fixFillerFor(@Nonnull World world, @Nonnull WorldChunk chunk)`: Add description.
  - Executes `fixFillerFor` behavior.
- `onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`: Add description.
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
