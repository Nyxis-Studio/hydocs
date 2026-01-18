**Source Hash:** `3b286cf484ad169aab8fb7915f1b2f4ea5940d12235111a05ea56d980dfda7b5`

# BlockHarvestUtils

## Overview

## Constructor Descriptions
- `none()`: No documented methods.

## Method Descriptions
- `getSpecPowerDamageBlock(@Nullable Item item, @Nullable BlockType blockType, @Nullable ItemTool tool)`: Add description.
  - Executes `getSpecPowerDamageBlock` behavior.
- `calculateDurabilityUse(@Nonnull Item item, @Nullable BlockType blockType)`: Add description.
  - Executes `calculateDurabilityUse` behavior.
- `performBlockDamage(@Nonnull Vector3i targetBlock, @Nullable ItemStack itemStack, @Nullable ItemTool tool, float damageScale, int setBlockSettings, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `performBlockDamage` behavior.
- `performBlockDamage(@Nullable LivingEntity entity, @Nullable Ref<EntityStore> ref, @Nonnull Vector3i targetBlockPos, @Nullable ItemStack itemStack, @Nullable ItemTool tool, @Nullable String toolId, boolean matchTool, float damageScale, int setBlockSettings, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<EntityStore> entityStore, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `performBlockDamage` behavior.
- `performBlockBreak(@Nullable Ref<EntityStore> ref, @Nullable ItemStack heldItemStack, @Nonnull Vector3i targetBlock, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<EntityStore> entityStore, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `performBlockBreak` behavior.
- `performBlockBreak(@Nullable Ref<EntityStore> ref, @Nullable ItemStack heldItemStack, @Nonnull Vector3i targetBlock, int setBlockSettings, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<EntityStore> entityStore, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `performBlockBreak` behavior.
- `performBlockBreak(@Nonnull World world, @Nonnull Vector3i blockPosition, @Nonnull BlockType targetBlockTypeKey, @Nullable ItemStack heldItemStack, int dropQuantity, @Nullable String dropItemId, @Nullable String dropListId, int setBlockSettings, @Nullable Ref<EntityStore> ref, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<EntityStore> entityStore, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `performBlockBreak` behavior.
- `naturallyRemoveBlockByPhysics(@Nonnull Vector3i blockPosition, @Nonnull BlockType blockType, int filler, int setBlockSettings, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<EntityStore> entityStore, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `naturallyRemoveBlockByPhysics` behavior.
- `naturallyRemoveBlock(@Nonnull Vector3i blockPosition, @Nullable BlockType blockType, int filler, int quantity, String itemId, String dropListId, int setBlockSettings, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<EntityStore> entityStore, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `naturallyRemoveBlock` behavior.
- `shouldPickupByInteraction(@Nullable BlockType blockType)`: Add description.
  - Executes `shouldPickupByInteraction` behavior.
- `performPickupByInteraction(@Nonnull Ref<EntityStore> ref, @Nonnull Vector3i targetBlock, @Nonnull BlockType blockType, int filler, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<EntityStore> entityStore, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `performPickupByInteraction` behavior.
- `removeBlock(@Nonnull Vector3i blockPosition, @Nonnull BlockType blockType, int setBlockSettings, @Nonnull Ref<ChunkStore> chunkReference, @Nonnull ComponentAccessor<ChunkStore> chunkStore)`: Add description.
  - Executes `removeBlock` behavior.
- `getDrops(@Nonnull BlockType blockType, int quantity, @Nullable String itemId, @Nullable String dropListId)`: Add description.
  - Executes `getDrops` behavior.

## Notes
- No additional notes.
