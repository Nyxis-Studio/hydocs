# BreakBlockInteraction

## Overview
- Documentation for `BreakBlockInteraction`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.client`.

## Constructors
- `BreakBlockInteraction()`
  - Creates a `BreakBlockInteraction` instance.

## Methods
- `tick0(boolean firstRun, float time, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `tick0` behavior.
- `interactWithBlock(@Nonnull World world, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack heldItemStack, @Nonnull Vector3i targetBlock, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `interactWithBlock` behavior.
- `simulateInteractWithBlock(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull World world, @Nonnull Vector3i targetBlock)`
  - Executes `simulateInteractWithBlock` behavior.
- `generatePacket()`
  - Executes `generatePacket` behavior.
- `configurePacket(Interaction packet)`
  - Executes `configurePacket` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
