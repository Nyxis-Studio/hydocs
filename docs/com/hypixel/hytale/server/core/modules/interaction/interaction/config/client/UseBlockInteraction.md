# UseBlockInteraction

## Overview
- Documentation for `UseBlockInteraction`.
- Declared as a class in `com.hypixel.hytale.server.core.modules.interaction.interaction.config.client`.

## Constructors
- `UseBlockInteraction()`
  - Creates a `UseBlockInteraction` instance.

## Methods
- `interactWithBlock(@Nonnull World world, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull Vector3i targetBlock, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `interactWithBlock` behavior.
- `simulateInteractWithBlock(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull World world, @Nonnull Vector3i targetBlock)`
  - Executes `simulateInteractWithBlock` behavior.
- `doInteraction(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nonnull World world, @Nonnull Vector3i targetBlock, boolean fireEvent)`
  - Executes `doInteraction` behavior.
- `generatePacket()`
  - Executes `generatePacket` behavior.
- `toString()`
  - Executes `toString` behavior.

## Notes
- No additional notes.
