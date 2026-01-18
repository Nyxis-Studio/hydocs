# ChangeFarmingStageInteraction

**Overview**
Interaction that changes the current farming stage of a block.
Supports absolute stage setting and relative increase/decrease logic.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getWaitForDataFrom()`: returns `WaitForDataFrom.Server`.
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: applies stage changes and schedules ticks.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: no-op simulation.
- `toString()`: returns a diagnostic string.

**Notes**
- Logs detailed execution flow for debugging stage changes.
