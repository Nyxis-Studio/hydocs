# BlockPhysicsUtil

## Overview
- Documentation for `BlockPhysicsUtil`.
- Declared as a class in `com.hypixel.hytale.builtin.blockphysics`.

## Constructors
- None.

## Methods
- `applyBlockPhysics(@Nullable ComponentAccessor<EntityStore> commandBuffer, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull BlockPhysicsSystems.CachedAccessor chunkAccessor, BlockSection blockSection, @Nonnull BlockPhysics blockPhysics, @Nonnull FluidSection fluidSection, int blockX, int blockY, int blockZ, @Nonnull BlockType blockType, int rotation, int filler)`
  - Executes `applyBlockPhysics` behavior.
- `testBlockPhysics(@Nonnull BlockPhysicsSystems.CachedAccessor chunkAccessor, BlockSection blockSection, @Nullable BlockPhysics blockPhysics, @Nonnull FluidSection fluidSection, int blockX, int blockY, int blockZ, @Nonnull BlockType blockType, int rotation, int filler)`
  - Executes `testBlockPhysics` behavior.
- `doesSatisfyRequirements(@Nonnull BlockType blockType, Fluid fluid, Vector3i blockFillerOffset, Vector3i neighbourFillerOffset, BlockFace blockFace, BlockFace neighbourBlockFace, int neighbourBlockId, @Nonnull BlockType neighbourBlockType, int neighbourRotation, int neighbourFluidId, @Nonnull Fluid neighbourFluid, @Nonnull RequiredBlockFaceSupport requiredBlockFaceSupport)`
  - Executes `doesSatisfyRequirements` behavior.
- `doesMatchFaceType(Vector3i fillerOffset, @Nonnull String faceType, BlockFace blockFace, @Nonnull Map<BlockFace, BlockFaceSupport[]> supporting)`
  - Executes `doesMatchFaceType` behavior.

## Notes
- No additional notes.
