# BlockTypeModule

## Overview
- Documentation for `BlockTypeModule`.
- Declared as a class in `com.hypixel.hytale.server.core.blocktype`.

## Constructors
- `BlockTypeModule(@Nonnull JavaPluginInit init)`
  - Creates a `BlockTypeModule` instance.

## Methods
- `get()`
  - Executes `get` behavior.
- `setup()`
  - Executes `setup` behavior.
- `getBlockPhysicsComponentType()`
  - Executes `getBlockPhysicsComponentType` behavior.
- `onChunkPreLoadProcessEnsureBlockState(@Nonnull ChunkPreLoadProcessEvent event)`
  - Executes `onChunkPreLoadProcessEnsureBlockState` behavior.
- `onChunkPreLoadProcess(@Nonnull ChunkPreLoadProcessEvent event)`
  - Executes `onChunkPreLoadProcess` behavior.
- `onChunksectionPreLoadProcess(@Nonnull WorldChunk chunk, @Nonnull BlockSection section, int sectionIndex, @Nonnull BlockType[] blocks)`
  - Executes `onChunksectionPreLoadProcess` behavior.
- `getBlockType(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull BlockType[] blocks, @Nonnull BlockSection section, int blockX, int blockY, int blockZ, boolean skipEmpty)`
  - Executes `getBlockType` behavior.
- `breakOrSetFillerBlocks(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull IndexedLookupTableAssetMap<String, BlockBoundingBoxes> hitboxAssetMap, @Nonnull ChunkAccessor<?> accessor, @Nonnull BlockAccessor chunk, int finalX, int finalY, int finalZ, @Nonnull BlockType blockType, int rotation)`
  - Executes `breakOrSetFillerBlocks` behavior.
- `getOriginBlockType(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull ChunkAccessor<?> accessor, @Nonnull BlockAccessor section, int originX, int originY, int originZ)`
  - Executes `getOriginBlockType` behavior.
- `setFillerBlocks(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull IndexedLookupTableAssetMap<String, BlockBoundingBoxes> hitboxAssetMap, @Nonnull ChunkAccessor<?> accessor, @Nonnull BlockAccessor chunk, int finalX, int finalY, int finalZ, @Nonnull BlockType originBlockType, int rotation)`
  - Executes `setFillerBlocks` behavior.
- `isFillerValid(@Nonnull BlockTypeAssetMap<String, BlockType> blockTypeAssetMap, @Nonnull ChunkAccessor<?> accessor, @Nonnull BlockAccessor chunk, @Nonnull BlockType blockType, int filler, int x, int y, int z)`
  - Executes `isFillerValid` behavior.
- `onEntityAdd(@Nonnull Holder<ChunkStore> holder, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityAdd` behavior.
- `onEntityRemoved(@Nonnull Holder<ChunkStore> holder, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store)`
  - Executes `onEntityRemoved` behavior.
- `getQuery()`
  - Executes `getQuery` behavior.
- `getDependencies()`
  - Executes `getDependencies` behavior.
- `onEntityAdded(@Nonnull Ref<ChunkStore> ref, @Nonnull AddReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityAdded` behavior.
- `fixFillerFor(@Nonnull World world, @Nonnull WorldChunk chunk)`
  - Executes `fixFillerFor` behavior.
- `onEntityRemove(@Nonnull Ref<ChunkStore> ref, @Nonnull RemoveReason reason, @Nonnull Store<ChunkStore> store, @Nonnull CommandBuffer<ChunkStore> commandBuffer)`
  - Executes `onEntityRemove` behavior.

## Notes
- No additional notes.
