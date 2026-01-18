# BlockConditionInteraction

## Overview
- Documentation for `BlockConditionInteraction`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.client`.

## Constructors
- `BlockConditionInteraction()`
  - Creates a `BlockConditionInteraction` instance.

## Methods
- `interactWithBlock(@Nonnull World world, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull Vector3i targetBlock, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `interactWithBlock` behavior.
- `simulateInteractWithBlock(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull World world, @Nonnull Vector3i targetBlock)`
  - Executes `simulateInteractWithBlock` behavior.
- `doInteraction(@Nonnull InteractionContext context, @Nonnull World world, @Nonnull Vector3i targetBlock, @Nonnull com.hypixel.hytale.protocol.BlockFace face)`
  - Executes `doInteraction` behavior.
- `generatePacket()`
  - Executes `generatePacket` behavior.
- `configurePacket(Interaction packet)`
  - Executes `configurePacket` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
