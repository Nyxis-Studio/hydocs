# FertilizeSoilInteraction

**Overview**
Interaction that fertilizes soil blocks or their supporting soil.
Attempts to mark soil as fertilized and schedules tick updates.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `getWaitForDataFrom()`: returns `WaitForDataFrom.Server`.
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: applies fertilization and updates ticking.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: no-op simulation.

**Notes**
- Optionally refreshes growth modifiers via `refreshModifiers`.
