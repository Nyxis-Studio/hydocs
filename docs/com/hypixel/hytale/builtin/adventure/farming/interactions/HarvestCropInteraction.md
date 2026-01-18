**Source Hash:** `ae7f79fa29679c25f93dbd25a604caa6e43b27501144e756714c0610dfb03dbd`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# HarvestCropInteraction

## Overview
Interaction that harvests resources from a farmable block. Delegates to `FarmingUtil.harvest` using the block's rotation.

## Field Descriptions
- `CODEC`: Builder codec for harvest interactions.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: Resolves chunk state, determines block rotation, and triggers harvesting.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: No-op simulation.
- `toString()`: Returns a diagnostic string.

## Usage Notes
- Skips harvest if the target chunk or block type is unavailable.

## Examples
```java
HarvestCropInteraction interaction = HarvestCropInteraction.CODEC.decode(reader, extraInfo);
```
