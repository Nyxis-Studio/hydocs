**Source Hash:** `7d119eb35301a67b3a255d7b934444941019f055645afe7c7a7f4b0fd77f52a7`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# UseCoopInteraction

## Overview
Interaction that collects produce from a coop block. Transfers coop inventory items into the player's inventory.

## Field Descriptions
- `CODEC`: Builder codec for coop interaction.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: Resolves the coop block, transfers produce to the player inventory, and updates block interaction state.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: No-op simulation.

## Usage Notes
- Updates block interaction state based on produce availability.

## Examples
```java
UseCoopInteraction interaction = UseCoopInteraction.CODEC.decode(reader, extraInfo);
```
