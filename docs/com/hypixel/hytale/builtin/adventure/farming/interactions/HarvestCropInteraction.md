# HarvestCropInteraction

**Overview**
Interaction that harvests resources from a farmable block.
Delegates to `FarmingUtil.harvest` using the block's rotation.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: resolves the block and harvests it.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: no-op simulation.
- `toString()`: returns a diagnostic string.

**Notes**
- Uses chunk references to access block state safely.
