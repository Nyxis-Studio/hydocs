**Source Hash:** `6ffe6af4a991b48919c7248b8c95dcf2627dd5460afe4a97e2ecb5edc1bb4569`
**Last Updated:** `2026-01-18T17:26:43-03:00`

# UseCaptureCrateInteraction

## Overview
Interaction that captures NPCs into a crate or releases them to a coop/world. Handles validation against accepted NPC groups and item metadata.

## Field Descriptions
- `CODEC`: Builder codec for capture crate interactions.
- `acceptedNpcGroupIds`: Accepted NPC group ids.
- `acceptedNpcGroupIndexes`: Cached group indices for fast membership checks.
- `fullIcon`: Optional icon to apply when the crate is filled.

## Constructor Descriptions
- None. Instances are built via `CODEC`.

## Method Descriptions
- `tick0(boolean firstRun, float time, InteractionType type, InteractionContext context, CooldownHandler cooldownHandler)`: Captures a valid NPC into the held crate, updates metadata, and removes the NPC entity.
- `interactWithBlock(World world, CommandBuffer<EntityStore> commandBuffer, InteractionType type, InteractionContext context, ItemStack itemInHand, Vector3i targetBlock, CooldownHandler cooldownHandler)`: Places the captured NPC into a coop or spawns it into the world, then clears the crate metadata.
- `simulateInteractWithBlock(InteractionType type, InteractionContext context, ItemStack itemInHand, World world, Vector3i targetBlock)`: No-op simulation.

## Usage Notes
- Decoding resolves accepted NPC group ids into indices for fast checks.

## Examples
```java
UseCaptureCrateInteraction interaction = UseCaptureCrateInteraction.CODEC.decode(reader, extraInfo);
```
