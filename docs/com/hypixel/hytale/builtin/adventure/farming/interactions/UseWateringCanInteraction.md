# UseWateringCanInteraction

**Overview**
Interaction that waters soil or farm blocks for a duration.
Sets watered-until time and schedules ticking updates.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getWaitForDataFrom()`: returns `WaitForDataFrom.Server`.
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: applies watering and schedules ticks.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: no-op simulation.

**Notes**
- Uses `duration` in seconds to compute `wateredUntil`.
