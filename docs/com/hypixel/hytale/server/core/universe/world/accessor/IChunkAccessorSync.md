# IChunkAccessorSync

## Overview
- Documentation for `IChunkAccessorSync`.
- Declared as a interface in `com.hypixel.hytale.server.core.universe.world.accessor`.

## Constructors
- None.

## Methods
- `getChunkIfInMemory(long var1)`
  - Executes `getChunkIfInMemory` behavior.
- `loadChunkIfInMemory(long var1)`
  - Executes `loadChunkIfInMemory` behavior.
- `getChunkIfLoaded(long var1)`
  - Executes `getChunkIfLoaded` behavior.
- `getChunkIfNonTicking(long var1)`
  - Executes `getChunkIfNonTicking` behavior.
- `getChunk(long var1)`
  - Executes `getChunk` behavior.
- `getNonTickingChunk(long var1)`
  - Executes `getNonTickingChunk` behavior.
- `getBlock(@Nonnull Vector3i pos)`
  - Executes `getBlock` behavior.
- `getBlock(int x, int y, int z)`
  - Executes `getBlock` behavior.
- `getBlockType(@Nonnull Vector3i pos)`
  - Executes `getBlockType` behavior.
- `getBlockType(int x, int y, int z)`
  - Executes `getBlockType` behavior.
- `setBlock(int x, int y, int z, String blockTypeKey)`
  - Executes `setBlock` behavior.
- `setBlock(int x, int y, int z, String blockTypeKey, int settings)`
  - Executes `setBlock` behavior.
- `breakBlock(int x, int y, int z, int settings)`
  - Executes `breakBlock` behavior.
- `testBlockTypes(int x, int y, int z, @Nonnull BlockType blockTypeToTest, int rotation, @Nonnull TestBlockFunction predicate)`
  - Executes `testBlockTypes` behavior.
- `testPlaceBlock(int x, int y, int z, @Nonnull BlockType blockTypeToTest, int rotation)`
  - Executes `testPlaceBlock` behavior.
- `testPlaceBlock(int x, int y, int z, @Nonnull BlockType blockTypeToTest, int rotation, @Nonnull TestBlockFunction predicate)`
  - Executes `testPlaceBlock` behavior.
- `getState(int x, int y, int z, boolean followFiller)`
  - Executes `getState` behavior.
- `getBlockComponentHolder(int x, int y, int z)`
  - Executes `getBlockComponentHolder` behavior.
- `setBlockInteractionState(@Nonnull Vector3i blockPosition, @Nonnull BlockType blockType, @Nonnull String state)`
  - Executes `setBlockInteractionState` behavior.
- `getBaseBlock(@Nonnull BlockPosition position)`
  - Executes `getBaseBlock` behavior.
- `test(int var1, int var2, int var3, BlockType var4, int var5, int var6)`
  - Executes `test` behavior.

## Notes
- No additional notes.
