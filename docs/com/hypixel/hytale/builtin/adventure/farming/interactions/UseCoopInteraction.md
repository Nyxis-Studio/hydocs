# UseCoopInteraction

**Overview**
Interaction that collects produce from a coop block.
Transfers coop inventory items into the player's inventory.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: gathers produce and updates interaction state.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: no-op simulation.

**Notes**
- Updates the block interaction state based on produce availability.
