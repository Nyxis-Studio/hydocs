# OpenBenchPageInteraction

## Overview
- Documentation for `OpenBenchPageInteraction`.
- Declared as a class in `com.hypixel.hytale.builtin.crafting.interaction`.

## Constructors
- `OpenBenchPageInteraction("*Simple_Crafting_Default", PageType.SIMPLE_CRAFTING)`
  - Creates a `OpenBenchPageInteraction` instance.
- `OpenBenchPageInteraction("*Diagram_Crafting_Default", PageType.DIAGRAM_CRAFTING)`
  - Creates a `OpenBenchPageInteraction` instance.
- `OpenBenchPageInteraction("*Structural_Crafting_Default", PageType.STRUCTURAL_CRAFTING)`
  - Creates a `OpenBenchPageInteraction` instance.
- `OpenBenchPageInteraction(@Nonnull String id, @Nonnull PageType pageType)`
  - Creates a `OpenBenchPageInteraction` instance.
- `OpenBenchPageInteraction()`
  - Creates a `OpenBenchPageInteraction` instance.

## Methods
- `interactWithBlock(@Nonnull World world, @Nonnull CommandBuffer<EntityStore> commandBuffer, @Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull Vector3i targetBlock, @Nonnull CooldownHandler cooldownHandler)`
  - Executes `interactWithBlock` behavior.
- `simulateInteractWithBlock(@Nonnull InteractionType type, @Nonnull InteractionContext context, @Nullable ItemStack itemInHand, @Nonnull World world, @Nonnull Vector3i targetBlock)`
  - Executes `simulateInteractWithBlock` behavior.

## Notes
- No additional notes.
