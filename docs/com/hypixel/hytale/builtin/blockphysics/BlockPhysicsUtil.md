**Source Hash:** `91e7302e0c3817873e45dcee9ac2f98af85d5541a37a2760a7d8bd79246c90ac`

# BlockPhysicsUtil

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `applyBlockPhysics(@Nullable ComponentAccessor<EntityStore> commandBuffer, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull BlockPhysicsSystems.CachedAccessor chunkAccessor, BlockSection blockSection, @Nonnull BlockPhysics blockPhysics, @Nonnull FluidSection fluidSection, int blockX, int blockY, int blockZ, @Nonnull BlockType blockType, int rotation, int filler)`: Add description.
  - Executes `applyBlockPhysics` behavior.
- `testBlockPhysics(@Nonnull BlockPhysicsSystems.CachedAccessor chunkAccessor, BlockSection blockSection, @Nullable BlockPhysics blockPhysics, @Nonnull FluidSection fluidSection, int blockX, int blockY, int blockZ, @Nonnull BlockType blockType, int rotation, int filler)`: Add description.
  - Executes `testBlockPhysics` behavior.
- `doesSatisfyRequirements(@Nonnull BlockType blockType, Fluid fluid, Vector3i blockFillerOffset, Vector3i neighbourFillerOffset, BlockFace blockFace, BlockFace neighbourBlockFace, int neighbourBlockId, @Nonnull BlockType neighbourBlockType, int neighbourRotation, int neighbourFluidId, @Nonnull Fluid neighbourFluid, @Nonnull RequiredBlockFaceSupport requiredBlockFaceSupport)`: Add description.
  - Executes `doesSatisfyRequirements` behavior.
- `doesMatchFaceType(Vector3i fillerOffset, @Nonnull String faceType, BlockFace blockFace, @Nonnull Map<BlockFace, BlockFaceSupport[]> supporting)`: Add description.
  - Executes `doesMatchFaceType` behavior.

## Notes
- No additional notes.
