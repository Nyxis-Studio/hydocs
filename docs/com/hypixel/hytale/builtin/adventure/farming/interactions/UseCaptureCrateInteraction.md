# UseCaptureCrateInteraction

**Overview**
Interaction that captures NPCs into a crate or releases them to a coop/world.
Handles validation against accepted NPC groups and item metadata.

**Constructors**
- Uses the codec builder to construct instances; no explicit constructor defined.

**Methods**
- `tick0(boolean firstRun, float time, InteractionType type, InteractionContext context, CooldownHandler cooldownHandler)`: captures NPCs into the held item.
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: places NPCs into a coop or spawns them.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: no-op simulation.

**Notes**
- Resolves accepted NPC groups into indices during decode.
