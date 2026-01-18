# FluidTicker

## Overview
- Documentation for `FluidTicker`.
- Declared as a class in `com.hypixel.hytale.server.core.asset.type.fluid`.

## Constructors
- None.

## Methods
- `getSupportedById()`
  - Executes `getSupportedById` behavior.
- `tick(@Nonnull CommandBuffer<ChunkStore> commandBuffer, @Nonnull CachedAccessor cachedAccessor, @Nonnull FluidSection fluidSection, @Nonnull BlockSection blockSection, @Nonnull Fluid fluid, int fluidId, int worldX, int worldY, int worldZ)`
  - Executes `tick` behavior.
- `process(World world, long tick, @Nonnull Accessor accessor, @Nonnull FluidSection fluidSection, @Nonnull BlockSection blockSection, @Nonnull Fluid fluid, int fluidId, int worldX, int worldY, int worldZ)`
  - Executes `process` behavior.
- `isAlive(@Nonnull Accessor accessor, @Nonnull FluidSection fluidSection, @Nonnull BlockSection blockSection, Fluid fluid, int fluidId, byte fluidLevel, int worldX, int worldY, int worldZ)`
  - Executes `isAlive` behavior.
- `spread(World var1, long var2, Accessor var4, FluidSection var5, BlockSection var6, Fluid var7, int var8, byte var9, int var10, int var11, int var12)`
  - Executes `spread` behavior.
- `setTickingSurrounding(@Nonnull Accessor accessor, BlockSection blockSection, int worldX, int worldY, int worldZ)`
  - Executes `setTickingSurrounding` behavior.
- `getSpreadOffsets(@Nonnull BlockTypeAssetMap<String, BlockType> blockMap, @Nonnull Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, int worldX, int worldY, int worldZ, @Nonnull Vector2i[] offsetArray, int fluidId, int maxDropDistance)`
  - Executes `getSpreadOffsets` behavior.
- `distanceToDrop(@Nonnull BlockTypeAssetMap<String, BlockType> blockMap, @Nonnull Accessor accessor, @Nonnull FluidSection fluidSection, BlockSection blockSection, int worldX, int worldY, int worldZ, @Nonnull Vector2i offset, int fluidId, int maxDropDistance)`
  - Executes `distanceToDrop` behavior.
- `isFullySolid(@Nonnull BlockType blockType)`
  - Executes `isFullySolid` behavior.
- `isSolid(@Nonnull BlockType blockType)`
  - Executes `isSolid` behavior.
- `blocksFluidFrom(@Nonnull BlockType blockType, int rotationIndex, int offsetX, int offsetZ)`
  - Executes `blocksFluidFrom` behavior.
- `blocksFluidFrom(@Nonnull BlockType blockType, int rotationIndex, int offsetX, int offsetZ, int filler)`
  - Executes `blocksFluidFrom` behavior.
- `boxesBlockFace(Box[] boxes, int offsetX, int offsetZ)`
  - Executes `boxesBlockFace` behavior.
- `isSelfFluid(int selfFluidId, int otherFluidId)`
  - Executes `isSelfFluid` behavior.
- `canDemote()`
  - Executes `canDemote` behavior.
- `getFluidSection(int var1, int var2, int var3)`
  - Executes `getFluidSection` behavior.
- `getFluidSectionByBlock(int bx, int by, int bz)`
  - Executes `getFluidSectionByBlock` behavior.
- `getBlockSection(int var1, int var2, int var3)`
  - Executes `getBlockSection` behavior.
- `getBlockSectionByBlock(int bx, int by, int bz)`
  - Executes `getBlockSectionByBlock` behavior.
- `setBlock(int var1, int var2, int var3, int var4)`
  - Executes `setBlock` behavior.
- `of(CommandBuffer<ChunkStore> commandBuffer, @Nonnull FluidSection section, BlockSection blockSection, int radius)`
  - Executes `of` behavior.
- `init(CommandBuffer<ChunkStore> commandBuffer, @Nonnull FluidSection section, BlockSection blockSection, int radius)`
  - Executes `init` behavior.
- `getFluidSection(int cx, int cy, int cz)`
  - Executes `getFluidSection` behavior.
- `getBlockSection(int cx, int cy, int cz)`
  - Executes `getBlockSection` behavior.
- `setBlock(int x, int y, int z, int blockId)`
  - Executes `setBlock` behavior.

## Notes
- No additional notes.
